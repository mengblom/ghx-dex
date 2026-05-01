# Vault Changelog

This file tracks significant changes to vault structure, automation, and workflows.

## 2026-04-20

### process-inbox Skill: Eliminate Topics, Use Only Tags

**Changed**: Updated process-inbox skill to remove redundant `topics` property from frontmatter and consolidate all categorization into `tags`.

**Why**: Topics and tags were serving the same purpose, but tags are more functional in Obsidian (clickable, searchable, visible in graph view). This eliminates redundancy and improves usability.

**Tag Structure** (3-8 tags per file):
- **Specific topics** (2-4): Proper nouns, team names, products, initiatives (e.g., CoreUI, Mapping, IPA, GitHub, MongoDB)
- **Broad themes** (1-3): High-level categories (e.g., Engineering, Architecture, Hiring, AI-Platform, Testing)
- **Content-type** (1): Structural tag (e.g., daily_note, meeting, email, interview)

**Impact**: 
- All new files processed through inbox will use tags-only approach
- Existing files with `topics` property are unaffected but can be migrated
- Improved tag extraction identifies specific topics from content instead of generic fallbacks

**Migration**: Run process-inbox to reprocess files with new tag extraction logic.
