#!/usr/bin/env python3
"""GHX to Dex vault migration.

Migrates content from ~/Documents/GHX (Johnny Decimal system) to
~/Documents/ghx-dex (PARA method) with proper format conversion.

Usage:
    # Preview migration
    python3 core/migrations/migrate_ghx_to_dex.py --dry-run

    # Execute migration
    python3 core/migrations/migrate_ghx_to_dex.py --apply

    # Rollback
    python3 core/migrations/migrate_ghx_to_dex.py --rollback
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

# Import existing Dex utilities
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from core.paths import (
    VAULT_ROOT,
    PEOPLE_DIR,
    SYSTEM_DIR,
    PEOPLE_INDEX_FILE,
    TASKS_FILE,
)
from core.utils.file_ops import atomic_write_text, atomic_write_json

# Import migration helpers
from ghx_helpers import (
    parse_frontmatter,
    is_person_folder_content,
    is_meeting_note,
    extract_tasks,
    find_attachment_references,
    update_wiki_links,
    normalize_attachment_paths,
    create_person_page_content,
    get_person_folders,
    extract_person_name_from_folder,
    determine_destination_for_file,
)

# Configuration
GHX_VAULT = Path('~/Documents/GHX').expanduser()
DEX_VAULT = VAULT_ROOT
MANIFEST_PATH = SYSTEM_DIR / '.migration-manifest-ghx-import.json'
BACKUP_ROOT = SYSTEM_DIR / '.migration-backups' / 'ghx-import'

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)


def should_skip_file(filepath: Path) -> bool:
    """Check if file should be skipped during migration."""
    path_str = str(filepath)

    skip_patterns = [
        'CLAUDE.md',
        'README.md',
        '/.git/',
        '/.obsidian/',
        '/_attachments/',
        '.DS_Store',
    ]

    return any(pattern in path_str for pattern in skip_patterns)


def discover_markdown_files(ghx_vault: Path) -> list[Path]:
    """Find all markdown files in GHX vault."""
    files = []

    for md_file in ghx_vault.rglob('*.md'):
        if should_skip_file(md_file):
            continue
        files.append(md_file)

    return sorted(files)


def process_regular_file(
    source_path: Path,
    dest_path: Path,
    metadata: dict,
    dry_run: bool
) -> dict[str, Any]:
    """Process a regular markdown file (not person folder content)."""

    result = {
        'source': str(source_path),
        'destination': str(dest_path) if dest_path else None,
        'success': False,
        'actions': [],
        'errors': [],
        'attachments': [],
        'tasks': [],
    }

    try:
        # Read content
        content = source_path.read_text(encoding='utf-8')

        # Update wiki links
        content = update_wiki_links(content)
        result['actions'].append('updated_links')

        # Normalize attachment paths
        content = normalize_attachment_paths(content)
        result['actions'].append('normalized_attachments')

        # Find attachments
        attachments = find_attachment_references(content)
        result['attachments'] = attachments

        # Extract tasks if meeting note
        if is_meeting_note(source_path, metadata):
            tasks = extract_tasks(content, metadata, source_path.name)
            result['tasks'] = tasks
            if tasks:
                result['actions'].append(f'extracted_{len(tasks)}_tasks')

        # Write to destination
        if not dry_run and dest_path:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            atomic_write_text(dest_path, content)
            result['actions'].append('written')

        result['success'] = True

    except Exception as e:
        result['errors'].append(str(e))
        result['success'] = False

    return result


def process_person_folders(
    ghx_vault: Path,
    dex_vault: Path,
    dry_run: bool
) -> list[dict[str, Any]]:
    """Process all person folders - create person pages and organize documents."""

    results = []
    person_folders = get_person_folders(ghx_vault)

    for person_folder in person_folders:
        result = {
            'source': str(person_folder),
            'success': False,
            'actions': [],
            'errors': [],
            'person_page_created': None,
            'documents_moved': [],
        }

        try:
            # Extract person name
            person_name = extract_person_name_from_folder(person_folder)
            file_safe_name = person_name.replace(' ', '_')

            # Create person page content
            person_page_content = create_person_page_content(person_name, 'GHX')

            # Determine paths
            person_page_path = PEOPLE_DIR / 'Internal' / f'{file_safe_name}.md'
            person_docs_dir = PEOPLE_DIR / 'Internal' / file_safe_name / 'Reviews'

            result['person_page_created'] = str(person_page_path)

            if not dry_run:
                # Write person page
                atomic_write_text(person_page_path, person_page_content)
                result['actions'].append('created_person_page')

                # Create documents directory
                person_docs_dir.mkdir(parents=True, exist_ok=True)

                # Copy all documents from person folder
                for doc in person_folder.glob('*.md'):
                    dest_doc_path = person_docs_dir / doc.name
                    shutil.copy2(doc, dest_doc_path)
                    result['documents_moved'].append(str(dest_doc_path))
                    result['actions'].append(f'copied_{doc.name}')

            result['success'] = True

        except Exception as e:
            result['errors'].append(str(e))
            result['success'] = False

        results.append(result)

    return results


def copy_attachments(attachment_names: set[str], ghx_vault: Path, dex_vault: Path, dry_run: bool) -> int:
    """Copy referenced attachments from GHX to Dex vault."""

    ghx_attachments_dir = ghx_vault / '_attachments'
    dex_attachments_dir = dex_vault / '_attachments'

    if not ghx_attachments_dir.exists():
        logger.warning(f"GHX attachments directory not found: {ghx_attachments_dir}")
        return 0

    copied_count = 0

    for attachment_name in sorted(attachment_names):
        source_path = ghx_attachments_dir / attachment_name

        if not source_path.exists():
            logger.warning(f"  Attachment not found: {attachment_name}")
            continue

        dest_path = dex_attachments_dir / attachment_name

        if dry_run:
            logger.info(f"  Would copy: {attachment_name}")
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, dest_path)
            copied_count += 1

    return copied_count


def append_tasks_to_file(tasks: list[dict], dry_run: bool) -> None:
    """Append extracted tasks to Tasks.md."""

    if not tasks:
        return

    if dry_run:
        logger.info(f"  Would append {len(tasks)} tasks to Tasks.md")
        return

    # Read existing tasks file
    if TASKS_FILE.exists():
        existing_content = TASKS_FILE.read_text(encoding='utf-8')
    else:
        existing_content = "# Tasks\n\n"

    # Add migration section
    today = datetime.now().strftime('%Y-%m-%d')
    task_section = f"\n\n## From Migration - {today}\n\n"

    for i, task in enumerate(tasks, 1):
        task_id = f"task-{today.replace('-', '')}-{i:03d}"
        source = task['source_file'].replace(' ', '-').lower()
        task_line = f"- [ ] {task['description']} ^{task_id} #source/{source}\n"
        task_section += task_line

    # Append to file
    new_content = existing_content + task_section
    atomic_write_text(TASKS_FILE, new_content)


def run_auto_link_people(dex_vault: Path) -> None:
    """Run auto-link-people script on migrated files."""
    try:
        logger.info("\nRunning auto-link-people post-processing...")
        script_path = dex_vault / '.scripts' / 'auto-link-people.cjs'

        if not script_path.exists():
            logger.warning("  Auto-link-people script not found, skipping")
            return

        # Run with --batch flag if available
        result = subprocess.run(
            ['node', str(script_path), '--batch'],
            cwd=dex_vault,
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode == 0:
            logger.info("  ✓ Auto-link-people completed")
        else:
            logger.warning(f"  Auto-link-people failed: {result.stderr}")

    except Exception as e:
        logger.warning(f"  Error running auto-link-people: {e}")


def rebuild_person_index(dex_vault: Path) -> None:
    """Rebuild System/People_Index.json."""
    try:
        logger.info("Rebuilding person index...")

        index = {}

        for subdir in ['Internal', 'External']:
            people_subdir = PEOPLE_DIR / subdir
            if not people_subdir.exists():
                continue

            for person_file in people_subdir.glob('*.md'):
                person_name = person_file.stem.replace('_', ' ')
                index[person_name] = str(person_file.relative_to(dex_vault))

        atomic_write_json(PEOPLE_INDEX_FILE, index)
        logger.info(f"  ✓ Rebuilt person index: {len(index)} people")

    except Exception as e:
        logger.warning(f"  Error rebuilding person index: {e}")


def create_git_backup(dex_vault: Path) -> str:
    """Create git backup before migration."""
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    tag_name = f"pre-ghx-migration-{timestamp}"

    try:
        # Stage all changes
        subprocess.run(['git', 'add', '-A'], cwd=dex_vault, check=True)

        # Commit
        subprocess.run([
            'git', 'commit', '-m',
            f'Pre-migration snapshot - GHX import [{timestamp}]'
        ], cwd=dex_vault)

        # Create tag
        subprocess.run(['git', 'tag', tag_name], cwd=dex_vault, check=True)

        logger.info(f"  ✓ Git backup created: {tag_name}")
        return tag_name

    except subprocess.CalledProcessError as e:
        logger.warning(f"  Git backup failed: {e}")
        return None


def write_manifest(results: dict, manifest_path: Path) -> None:
    """Write migration manifest for rollback."""
    manifest = {
        'migration': 'ghx-to-dex',
        'timestamp': datetime.now(UTC).isoformat(),
        'source_vault': str(GHX_VAULT),
        'target_vault': str(DEX_VAULT),
        'results': results,
    }

    atomic_write_json(manifest_path, manifest)
    logger.info(f"\nManifest written to: {manifest_path}")


def run_migration(dry_run: bool = True) -> dict[str, Any]:
    """Main migration orchestrator."""

    logger.info("="*60)
    logger.info("GHX to Dex Vault Migration")
    logger.info("="*60)

    # Validate
    if not GHX_VAULT.exists():
        raise ValueError(f"GHX vault not found: {GHX_VAULT}")
    if not DEX_VAULT.exists():
        raise ValueError(f"Dex vault not found: {DEX_VAULT}")

    logger.info(f"\nSource: {GHX_VAULT}")
    logger.info(f"Target: {DEX_VAULT}")

    if dry_run:
        logger.info("\n🔍 DRY RUN MODE - No files will be modified\n")
    else:
        logger.info("\n⚠️  LIVE MODE - Files will be modified\n")

    # Create git backup (if not dry run)
    git_tag = None
    if not dry_run:
        logger.info("Creating git backup...")
        git_tag = create_git_backup(DEX_VAULT)

    # Phase 1: Process person folders first
    logger.info("\n" + "="*60)
    logger.info("Phase 1: Processing Person Folders")
    logger.info("="*60)

    person_results = process_person_folders(GHX_VAULT, DEX_VAULT, dry_run)

    for result in person_results:
        if result['success']:
            logger.info(f"✓ {Path(result['source']).name}: {', '.join(result['actions'])}")
        else:
            logger.error(f"✗ {Path(result['source']).name}: {result['errors']}")

    # Phase 2: Process regular files
    logger.info("\n" + "="*60)
    logger.info("Phase 2: Processing Regular Files")
    logger.info("="*60)

    # Discover files
    md_files = discover_markdown_files(GHX_VAULT)

    # Filter out person folder files (already handled)
    regular_files = [f for f in md_files if not is_person_folder_content(f)]

    logger.info(f"\nFound {len(regular_files)} files to process")

    file_results = []
    all_attachments = set()
    all_tasks = []

    for i, source_path in enumerate(regular_files, 1):
        logger.info(f"\n[{i}/{len(regular_files)}] {source_path.name}")

        # Parse frontmatter
        metadata = parse_frontmatter(source_path)

        # Determine destination
        dest_path = determine_destination_for_file(source_path, GHX_VAULT, DEX_VAULT, metadata)

        if dest_path is None:
            # Person folder content - should have been handled in Phase 1
            logger.warning(f"  Skipping person folder file: {source_path}")
            continue

        # Process file
        result = process_regular_file(source_path, dest_path, metadata, dry_run)
        file_results.append(result)

        # Collect attachments and tasks
        all_attachments.update(result['attachments'])
        all_tasks.extend(result['tasks'])

        # Show result
        if result['success']:
            logger.info(f"  ✓ {', '.join(result['actions'])}")
        else:
            logger.error(f"  ✗ ERROR: {result['errors']}")

    # Phase 3: Copy attachments
    logger.info("\n" + "="*60)
    logger.info("Phase 3: Copying Attachments")
    logger.info("="*60)

    logger.info(f"\nFound {len(all_attachments)} unique attachments referenced")
    copied_count = copy_attachments(all_attachments, GHX_VAULT, DEX_VAULT, dry_run)

    if not dry_run:
        logger.info(f"  ✓ Copied {copied_count} attachments")

    # Phase 4: Append tasks
    if all_tasks and not dry_run:
        logger.info("\n" + "="*60)
        logger.info("Phase 4: Extracting Tasks")
        logger.info("="*60)

        logger.info(f"\nAppending {len(all_tasks)} tasks to Tasks.md...")
        append_tasks_to_file(all_tasks, dry_run)
        logger.info("  ✓ Tasks appended")

    # Phase 5: Post-processing
    if not dry_run:
        logger.info("\n" + "="*60)
        logger.info("Phase 5: Post-Processing")
        logger.info("="*60)

        run_auto_link_people(DEX_VAULT)
        rebuild_person_index(DEX_VAULT)

    # Summary
    logger.info("\n" + "="*60)
    logger.info(f"Migration {'Preview' if dry_run else 'Complete'}!")
    logger.info("="*60)

    person_success = sum(1 for r in person_results if r['success'])
    file_success = sum(1 for r in file_results if r['success'])

    logger.info(f"\nPerson folders: {person_success}/{len(person_results)} successful")
    logger.info(f"Regular files: {file_success}/{len(regular_files)} successful")
    logger.info(f"Attachments: {len(all_attachments)} referenced")
    logger.info(f"Tasks extracted: {len(all_tasks)}")

    # Write manifest
    results_data = {
        'person_results': person_results,
        'file_results': file_results,
        'attachments': list(all_attachments),
        'tasks': all_tasks,
        'git_tag': git_tag,
    }

    if not dry_run:
        write_manifest(results_data, MANIFEST_PATH)

    return results_data


def rollback_migration() -> None:
    """Rollback migration to pre-migration state."""

    logger.info("="*60)
    logger.info("Rolling Back Migration")
    logger.info("="*60)

    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"No migration manifest found at: {MANIFEST_PATH}")

    # Load manifest
    manifest = json.loads(MANIFEST_PATH.read_text())

    logger.info(f"\nRolling back migration from {manifest['timestamp']}")

    # Get git tag
    git_tag = manifest['results'].get('git_tag')

    if git_tag:
        try:
            logger.info(f"\nResetting to git tag: {git_tag}")
            subprocess.run(['git', 'reset', '--hard', git_tag], cwd=DEX_VAULT, check=True)
            logger.info("  ✓ Rollback complete via git")
        except subprocess.CalledProcessError as e:
            logger.error(f"  ✗ Git rollback failed: {e}")
    else:
        logger.warning("No git tag found in manifest - manual rollback required")

    logger.info("\n✓ Rollback complete")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Migrate GHX vault to Dex',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview migration
  python3 core/migrations/migrate_ghx_to_dex.py --dry-run

  # Execute migration
  python3 core/migrations/migrate_ghx_to_dex.py --apply

  # Rollback
  python3 core/migrations/migrate_ghx_to_dex.py --rollback
        """
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview migration without making changes'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Execute migration (modifies files)'
    )
    parser.add_argument(
        '--rollback',
        action='store_true',
        help='Rollback previous migration'
    )

    args = parser.parse_args()

    try:
        if args.rollback:
            rollback_migration()
        elif args.apply:
            run_migration(dry_run=False)
        else:
            # Default to dry-run
            run_migration(dry_run=True)

    except Exception as e:
        logger.error(f"\nError: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
