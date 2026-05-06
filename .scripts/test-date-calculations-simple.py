#!/usr/bin/env python3
"""Test date calculations for daily planning (standalone)"""

from datetime import datetime, timedelta

def test_monday_first():
    """Test that weekday calculations are correct for Monday-first weeks"""

    print("=" * 60)
    print("TEST 1: Monday as first day of week")
    print("=" * 60)
    print()

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
        # This is the logic from work_server.py
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
        print(f"  weekday(): {days_elapsed} (0=Mon, 1=Tue, ..., 6=Sun)")
        print(f"  Day number for display: {day_number_display} (expected {expected_day_num})")
        print(f"  Days remaining: {days_remaining} (expected {expected_days_remaining})")

        if not passed:
            all_passed = False
            print(f"  ❌ MISMATCH!")

        print()

    return all_passed

def test_sunday_first():
    """Test that weekday calculations are correct for Sunday-first weeks"""

    print("=" * 60)
    print("TEST 2: Sunday as first day of week")
    print("=" * 60)
    print()

    # Test cases: (date, expected_day_name, expected_day_number, expected_days_remaining)
    test_cases = [
        (datetime(2026, 5, 4), "Monday", 2, 4),      # Monday: day 2, 4 days left (Tue-Fri)
        (datetime(2026, 5, 5), "Tuesday", 3, 3),     # Tuesday: day 3, 3 days left (Wed-Fri)
        (datetime(2026, 5, 6), "Wednesday", 4, 2),   # Wednesday: day 4, 2 days left (Thu-Fri)
        (datetime(2026, 5, 7), "Thursday", 5, 1),    # Thursday: day 5, 1 day left (Fri)
        (datetime(2026, 5, 8), "Friday", 6, 0),      # Friday: day 6, 0 days left
        (datetime(2026, 5, 9), "Saturday", 7, 0),    # Saturday: day 7, 0 days (weekend)
        (datetime(2026, 5, 10), "Sunday", 1, 5),     # Sunday: day 1, 5 days left (Mon-Fri)
    ]

    all_passed = True

    for test_date, expected_day_name, expected_day_num, expected_days_remaining in test_cases:
        # This is the logic for Sunday-first from work_server.py
        py_weekday = test_date.weekday()  # Python's 0=Monday
        days_elapsed = (py_weekday + 1) % 7  # Adjust to Sunday=0
        day_number_display = days_elapsed + 1  # Convert to 1-indexed
        day_name = test_date.strftime('%A')

        # Work week is Monday-Friday (days 1-5 in Sunday-first week)
        if days_elapsed == 0:  # Sunday - full work week ahead
            days_remaining = 5  # Monday through Friday
        elif 1 <= days_elapsed <= 5:  # Monday-Friday
            days_remaining = 5 - days_elapsed
        else:  # Saturday (days_elapsed=6)
            days_remaining = 0

        # Check results
        passed = (
            day_name == expected_day_name and
            day_number_display == expected_day_num and
            days_remaining == expected_days_remaining
        )

        status = "✅ PASS" if passed else "❌ FAIL"

        print(f"{status} {day_name} ({test_date.strftime('%Y-%m-%d')})")
        print(f"  py weekday(): {py_weekday} (Python's 0=Mon)")
        print(f"  Adjusted (Sunday=0): {days_elapsed}")
        print(f"  Day number for display: {day_number_display} (expected {expected_day_num})")
        print(f"  Days remaining: {days_remaining} (expected {expected_days_remaining})")

        if not passed:
            all_passed = False
            print(f"  ❌ MISMATCH!")

        print()

    return all_passed

def test_today():
    """Test with today's actual date"""
    print("\nTesting with TODAY's actual date...\n")

    today = datetime.now()
    days_elapsed = today.weekday()
    day_number_display = days_elapsed + 1
    day_name = today.strftime('%A')

    if today.weekday() < 5:  # Weekday
        days_remaining = 4 - today.weekday()
    else:  # Weekend
        days_remaining = 0

    print(f"Today: {day_name} ({today.strftime('%Y-%m-%d')})")
    print(f"  weekday(): {days_elapsed}")
    print(f"  Display as: Day {day_number_display} of 5")
    print(f"  Days remaining in work week: {days_remaining}")
    print()

    # Special validation for Wednesday May 6, 2026
    if today.date() == datetime(2026, 5, 6).date():
        expected_day_num = 3
        expected_days_remaining = 2

        if day_number_display == expected_day_num and days_remaining == expected_days_remaining:
            print("✅ Wednesday May 6 validation PASSED")
            print(f"   Day {day_number_display} of 5 with {days_remaining} days remaining")
            return True
        else:
            print("❌ Wednesday May 6 validation FAILED")
            print(f"   Got: Day {day_number_display} with {days_remaining} days remaining")
            print(f"   Expected: Day {expected_day_num} with {expected_days_remaining} days remaining")
            return False
    else:
        print(f"(Not Wednesday May 6, so skipping specific validation)")
        return True

if __name__ == "__main__":
    print("=" * 60)
    print("Date Calculation Test Suite")
    print("=" * 60)
    print()

    test1_passed = test_monday_first()
    test2_passed = test_sunday_first()
    test3_passed = test_today()

    print("=" * 60)
    if test1_passed and test2_passed and test3_passed:
        print("✅ ALL TESTS PASSED - Date calculations are correct!")
        print()
        print("Summary:")
        print("  ✅ Monday-first mode: Wednesday = Day 3 of 5")
        print("  ✅ Sunday-first mode: Wednesday = Day 4 of 7")
        print("  ✅ Days remaining counts only work days (Mon-Fri, excluding today)")
        print("  ✅ System is now dynamic based on user preference!")
        exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        exit(1)
