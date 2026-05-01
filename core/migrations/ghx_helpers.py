#!/usr/bin/env python3
"""Helper functions for GHX to Dex vault migration."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


def parse_frontmatter(filepath: Path) -> dict[str, Any]:
    """Extract YAML frontmatter from markdown file."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        return {}

    # Check for frontmatter
    if not content.startswith('---'):
        return {}

    # Find closing ---
    end_match = re.search(r'^---\s*$', content[3:], re.MULTILINE)
    if not end_match:
        return {}

    # Extract and parse YAML
    fm_text = content[3:3 + end_match.start()]
    try:
        return yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return {}


def is_person_folder_content(filepath: Path) -> bool:
    """Check if file is from 40-49 People folder."""
    return '40-49 People' in str(filepath)


def is_meeting_note(filepath: Path, metadata: dict) -> bool:
    """Detect if file is a meeting note."""
    # Check frontmatter
    if metadata.get('meeting') == 'true':
        return True
    if metadata.get('content_type') == 'meeting_note':
        return True
    if metadata.get('meeting_type'):
        return True

    # Check filename pattern
    name = filepath.name
    if re.match(r'\d{4}-\d{2}-\d{2}.*meeting', name, re.I):
        return True

    # Check location
    path_str = str(filepath)
    if '61 Meeting Notes' in path_str:
        return True
    if '00 - Inbox' in path_str and 'meeting' in name.lower():
        return True

    return False


def extract_tasks(content: str, metadata: dict, source_file: str) -> list[dict]:
    """Extract action items from meeting notes."""
    tasks = []

    # Method 1: Find "Action Items" sections
    action_pattern = r'##\s*Action Items?\s*\n(.*?)(?=\n##|$)'
    for match in re.finditer(action_pattern, content, re.DOTALL | re.I):
        section_content = match.group(1)

        # Extract checkbox items
        checkbox_pattern = r'^\s*-\s*\[\s*\]\s*(.+)$'
        for line in section_content.split('\n'):
            if checkbox_match := re.match(checkbox_pattern, line):
                task_text = checkbox_match.group(1).strip()
                tasks.append({
                    'description': task_text,
                    'source_file': source_file,
                    'source_date': metadata.get('date', ''),
                })

    # Method 2: Extract from frontmatter
    if 'action_items' in metadata:
        action_items = metadata['action_items']
        if isinstance(action_items, list):
            for item in action_items:
                tasks.append({
                    'description': str(item),
                    'source_file': source_file,
                    'source_date': metadata.get('date', ''),
                })

    # Method 3: Find "Follow-up" sections
    followup_pattern = r'##\s*Follow[- ]?up\s*\n(.*?)(?=\n##|$)'
    for match in re.finditer(followup_pattern, content, re.DOTALL | re.I):
        section_content = match.group(1)

        # Extract checkbox items
        checkbox_pattern = r'^\s*-\s*\[\s*\]\s*(.+)$'
        for line in section_content.split('\n'):
            if checkbox_match := re.match(checkbox_pattern, line):
                task_text = checkbox_match.group(1).strip()
                # Avoid duplicates
                if not any(t['description'] == task_text for t in tasks):
                    tasks.append({
                        'description': task_text,
                        'source_file': source_file,
                        'source_date': metadata.get('date', ''),
                    })

    return tasks


def find_attachment_references(content: str) -> list[str]:
    """Extract attachment filenames from markdown."""
    attachments = set()

    # Pattern: ![alt](../../_attachments/file.png)
    md_image_pattern = r'!\[.*?\]\((.*?_attachments/.*?)\)'
    for match in re.finditer(md_image_pattern, content):
        rel_path = match.group(1)
        # Extract just the filename
        attachment_name = Path(rel_path).name
        attachments.add(attachment_name)

    # Pattern: [[_attachments/file.pdf]]
    wiki_attach_pattern = r'\[\[.*?_attachments/(.*?)\]\]'
    for match in re.finditer(wiki_attach_pattern, content):
        attachment_name = match.group(1).split('|')[0].strip()  # Handle [[file|display]]
        attachments.add(attachment_name)

    return list(attachments)


def update_wiki_links(content: str) -> str:
    """Update wiki links from GHX paths to Dex PARA structure."""
    # Mapping of old paths to new
    link_mapping = {
        '00 - Inbox': '00-Inbox',
        '10-19 Planning/11 Quarterly Planning': '01-Quarter_Goals',
        '10-19 Planning/12 Ideas and Drafts': '00-Inbox/Ideas',
        '10-19 Planning/13 Meeting Preparation': '00-Inbox/Meetings',
        '10-19 Planning/14 Draft Correspondence': '00-Inbox',
        '10-19 Planning': '01-Quarter_Goals',  # Generic planning
        '20-29 Projects': '04-Projects',
        '30-39 Areas': '05-Areas',
        '40-49 People': '05-Areas/People',
        '50-59 Knowledge Base': '06-Resources',
        '60-69 Archive': '07-Archives',
        '70-79 Templates': 'System/Templates',
    }

    for old, new in link_mapping.items():
        # Replace in wiki links
        content = content.replace(f'[[{old}/', f'[[{new}/')
        content = content.replace(f'[[{old}|', f'[[{new}|')
        content = content.replace(f'[[{old}/README', f'[[{new}')
        content = content.replace(f'[[{old}]]', f'[[{new}]]')

    return content


def normalize_attachment_paths(content: str) -> str:
    """Normalize attachment paths to _attachments/ format."""
    # Replace relative paths with vault-level path
    # From: ../../_attachments/file.png
    # To: _attachments/file.png
    content = re.sub(
        r'!\[(.*?)\]\(.*?_attachments/(.*?)\)',
        r'![\1](_attachments/\2)',
        content
    )

    return content


def create_person_page_content(person_name: str, company: str = 'GHX') -> str:
    """Generate person page content from template."""
    today = datetime.now().strftime('%Y-%m-%d')

    # Convert "First Last" to "First_Last"
    file_safe_name = person_name.replace(' ', '_')

    content = f"""# {person_name}

## Overview

| Field | Value |
|-------|-------|
| **Role** | Direct Report |
| **Company** | {company} |
| **Company Page** | 05-Areas/Companies/{company}.md |
| **Type** | Internal |

---

## Relationship Context

**How we met:** Direct report at {company}

**Relationship type:** Direct Report

**Strength:** Strong

**Last interaction:** {today}

---

## Performance Reviews

*Review documents stored in subfolder:*

See `05-Areas/People/Internal/{file_safe_name}/Reviews/` for performance review documentation.

---

## Meeting History

| Date | Topic | Notes Link |
|------|-------|------------|
| | | |

*Auto-populated from meeting notes with this person's name*

---

## Action Items Involving Them

- [ ] Review migrated performance documentation

---

*Created: {today}*
*Migrated from GHX vault*
"""

    return content


def get_person_folders(ghx_vault: Path) -> list[Path]:
    """Find all person folders in 40-49 People/."""
    people_root = ghx_vault / '40-49 People'

    if not people_root.exists():
        return []

    # Get direct child directories (person folders)
    person_folders = [
        d for d in people_root.iterdir()
        if d.is_dir() and not d.name.startswith('.')
    ]

    return person_folders


def extract_person_name_from_folder(folder_path: Path) -> str:
    """Extract person name from folder path."""
    # Folder name is the person name
    return folder_path.name


def determine_destination_for_file(source_path: Path, ghx_vault: Path, dex_vault: Path, metadata: dict) -> Path:
    """Determine Dex destination path for a GHX file."""

    # Check frontmatter destination_category first
    dest_cat = metadata.get('destination_category')
    if dest_cat:
        # Map common destination categories
        category_map = {
            'projects': dex_vault / '04-Projects',
            'areas': dex_vault / '05-Areas',
            'resources': dex_vault / '06-Resources',
            'archive': dex_vault / '07-Archives',
            'inbox': dex_vault / '00-Inbox',
        }
        if dest_cat in category_map:
            return category_map[dest_cat] / source_path.name

    # Otherwise use source path
    parts = source_path.relative_to(ghx_vault).parts

    if '00 - Inbox' in parts:
        return dex_vault / '00-Inbox' / source_path.name

    elif '10-19 Planning' in parts:
        idx = parts.index('10-19 Planning')
        if len(parts) > idx + 1:
            subdir = parts[idx + 1]
            if subdir == '11 Quarterly Planning':
                # Preserve subfolder structure within Quarter Goals
                remaining = Path(*parts[idx + 2:]) if len(parts) > idx + 2 else Path(source_path.name)
                return dex_vault / '01-Quarter_Goals' / remaining
            elif subdir == '12 Ideas and Drafts':
                return dex_vault / '00-Inbox' / 'Ideas' / source_path.name
            elif subdir == '13 Meeting Preparation':
                return dex_vault / '00-Inbox' / 'Meetings' / source_path.name
            elif subdir == '14 Draft Correspondence':
                return dex_vault / '00-Inbox' / source_path.name
        # Generic planning
        return dex_vault / '01-Quarter_Goals' / source_path.name

    elif '20-29 Projects' in parts:
        # Preserve subfolder structure
        idx = parts.index('20-29 Projects')
        if len(parts) > idx + 1:
            subpath = Path(*parts[idx + 1:])
            return dex_vault / '04-Projects' / subpath
        return dex_vault / '04-Projects' / source_path.name

    elif '30-39 Areas' in parts:
        idx = parts.index('30-39 Areas')
        if len(parts) > idx + 1:
            subpath = Path(*parts[idx + 1:])
            return dex_vault / '05-Areas' / subpath
        return dex_vault / '05-Areas' / source_path.name

    elif '40-49 People' in parts:
        # Person folder content - should be handled specially
        # This function returns None to signal special handling
        return None

    elif '50-59 Knowledge Base' in parts:
        idx = parts.index('50-59 Knowledge Base')
        if len(parts) > idx + 1:
            subpath = Path(*parts[idx + 1:])
            return dex_vault / '06-Resources' / subpath
        return dex_vault / '06-Resources' / source_path.name

    elif '60-69 Archive' in parts:
        idx = parts.index('60-69 Archive')
        if len(parts) > idx + 1:
            subpath = Path(*parts[idx + 1:])
            return dex_vault / '07-Archives' / subpath
        return dex_vault / '07-Archives' / source_path.name

    elif '70-79 Templates' in parts:
        return dex_vault / 'System' / 'Templates' / source_path.name

    # Fallback: Inbox
    return dex_vault / '00-Inbox' / source_path.name
