#!/usr/bin/env python3
"""
Daily Note Parser Utility

Parses daily notes with structured sections (Tasks, Notes, Journal).
Reuses career_parser.py patterns for robust section extraction.
"""

from pathlib import Path
from typing import Dict, List, Optional
from core.mcp.career_parser import extract_section_list, extract_section


def parse_daily_note(file_path: Path) -> Optional[Dict[str, List[str]]]:
    """
    Parse a daily note file and extract structured sections.

    Args:
        file_path: Path to daily note (e.g., 00-Inbox/Daily_Notes/2026-05-08.md)

    Returns:
        {
            'tasks': ['Task 1', 'Task 2'],
            'notes': ['Note 1', 'Note 2'],
            'journal': ['Journal entry 1']
        }
        Returns None if file doesn't exist or can't be read.
    """
    if not file_path.exists():
        return None

    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception:
        return None

    # Extract each section using career_parser utilities
    tasks = extract_section_list(content, "Tasks")
    notes = extract_section_list(content, "Notes")
    journal = extract_section_list(content, "Journal")

    # Handle both bullet points and paragraphs in Journal section
    if not journal:
        journal_raw = extract_section(content, "# Journal")
        if journal_raw:
            # Split by paragraphs or bullet points
            journal = [
                line.strip().lstrip('- ')
                for line in journal_raw.split('\n')
                if line.strip() and not line.strip().startswith('#')
            ]

    return {
        'tasks': tasks,
        'notes': notes,
        'journal': journal
    }


def find_daily_note(vault_root: Path, date_str: str) -> Optional[Path]:
    """
    Find a daily note by date, checking both Daily_Notes/ folder and root fallback.

    Args:
        vault_root: Root of the vault
        date_str: Date in YYYY-MM-DD format

    Returns:
        Path to daily note if found, None otherwise
    """
    # Primary location
    primary_path = vault_root / "00-Inbox" / "Daily_Notes" / f"{date_str}.md"
    if primary_path.exists():
        return primary_path

    # Fallback: root of 00-Inbox (for legacy files)
    fallback_path = vault_root / "00-Inbox" / f"{date_str}.md"
    if fallback_path.exists():
        return fallback_path

    return None


def format_daily_note_summary(data: Dict[str, List[str]], max_items: int = 10) -> str:
    """
    Format daily note data for display in skill output.

    Args:
        data: Parsed daily note data
        max_items: Maximum items to show per section (truncate if longer)

    Returns:
        Formatted markdown string
    """
    sections = []

    if data['tasks']:
        task_list = data['tasks'][:max_items]
        truncated = len(data['tasks']) > max_items
        sections.append("**Quick Tasks:**")
        for task in task_list:
            sections.append(f"- {task}")
        if truncated:
            sections.append(f"  _(+{len(data['tasks']) - max_items} more)_")

    if data['notes']:
        note_list = data['notes'][:max_items]
        truncated = len(data['notes']) > max_items
        sections.append("\n**Notes Captured:**")
        for note in note_list:
            sections.append(f"- {note}")
        if truncated:
            sections.append(f"  _(+{len(data['notes']) - max_items} more)_")

    if data['journal']:
        sections.append("\n**Journal:**")
        sections.append(f"- {' '.join(data['journal'][:3])}")  # First 3 items or paragraphs

    return '\n'.join(sections) if sections else "_No content captured_"
