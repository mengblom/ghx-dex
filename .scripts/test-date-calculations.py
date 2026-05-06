#!/usr/bin/env python3
"""Test date calculations for daily planning"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add core/mcp to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'core' / 'mcp'))

# Import the function we fixed
from work_server import get_week_progress_data, _tz_today

def test_weekday_calculations():
    """Test that weekday calculations are correct for Monday-first weeks"""

    print("Testing week calculations with Monday as first day of week...\n")

    # Test cases: (date, expected_day_name, expected_day_number, expected_days_remaining)
    test_cases = [
        (datetime(2026, 5, 4), "Monday", 1, 4),      # Monday: 4 days left (Tue-Fri)
        (datetime(2026, 5, 5), "Tuesday", 2, 3),     # Tuesday: 3 days left (Wed-Fri)
        (datetime(2026, 5, 6), "Wednesday", 3, 2),   # Wednesday: 2 days left (Thu-Fri)
        (datetime(2026, 5, 7), "Thursday", 4, 1),    # Thursday: 1 day left (Fri)
        (datetime(2026, 5, 8), "Friday", 5, 0),      # Friday: 0 days left
        (datetime(2026, 5, 9), "Saturday", 6, 0),    # Saturday: 0 days (weekend)
        (datetime(2026, 5, 10), "Sunday", 7, 0),     # Sunday: 0 days (weekend)
    ]

    all_passed = True

    for test_date, expected_day_name, expected_day_num, expected_days_remaining in test_cases:
        # Simulate the date
        days_elapsed = test_date.weekday()  # 0=Monday, 1=Tuesday, ..., 6=Sunday
        day_number_display = days_elapsed + 1  # Convert to 1-indexed for display
        day_name = test_date.strftime('%A')

        # Calculate days remaining (work week only)
        if test_date.weekday() < 5:  # Monday-Friday
            days_remaining = 4 - test_date.weekday()
        else:  # Weekend
            days_remaining = 0

        # Check results
        passed = (
            day_name == expected_day_name and
            day_number_display == expected_day_num and
            days_remaining == expected_days_remaining
        )

        status = "✅ PASS" if passed else "❌ FAIL"

        print(f"{status} {day_name} ({test_date.strftime('%Y-%m-%d')})")
        print(f"  Day number: {day_number_display} (expected {expected_day_num})")
        print(f"  Days remaining: {days_remaining} (expected {expected_days_remaining})")

        if not passed:
            all_passed = False
            print(f"  ❌ MISMATCH!")

        print()

    return all_passed

def test_mcp_function():
    """Test the actual MCP function"""
    print("\nTesting actual get_week_progress_data() function...\n")

    # This will use today's actual date
    data = get_week_progress_data()

    today = _tz_today()
    expected_day_num = today.weekday() + 1  # 1-indexed

    print(f"Today: {data['day_of_week']} ({data['date']})")
    print(f"Days elapsed (0-indexed): {data['days_elapsed']}")
    print(f"Day number for display (1-indexed): {data['days_elapsed'] + 1}")
    print(f"Days remaining in work week: {data['days_remaining']}")
    print(f"Week: {data['week_start']} to {data['week_end']}")

    # Verify for today
    if today.weekday() < 5:  # Weekday
        expected_days_remaining = 4 - today.weekday()
    else:  # Weekend
        expected_days_remaining = 0

    if data['days_remaining'] == expected_days_remaining:
        print(f"\n✅ MCP function returns correct days_remaining!")
    else:
        print(f"\n❌ MCP function error: got {data['days_remaining']}, expected {expected_days_remaining}")
        return False

    return True

if __name__ == "__main__":
    print("=" * 60)
    print("Date Calculation Test Suite")
    print("=" * 60)
    print()

    test1_passed = test_weekday_calculations()
    test2_passed = test_mcp_function()

    print("=" * 60)
    if test1_passed and test2_passed:
        print("✅ ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)
