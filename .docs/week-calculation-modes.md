# Week Calculation Modes

Dex supports two calendar modes for weekly planning: **Monday-first** (business calendar) and **Sunday-first** (traditional calendar).

## Configuration

Edit `System/user-profile.yaml`:

```yaml
regional_preferences:
  first_day_of_week: "monday"  # or "sunday"
```

## How It Works

### Monday-First Mode (Default)

**Week structure:** Mon-Tue-Wed-Thu-Fri-Sat-Sun  
**Work week:** 5 days (Mon-Fri)

| Day | Display | Days Remaining |
|-----|---------|----------------|
| Monday | Day 1 of 5 | 4 (Tue-Fri) |
| Tuesday | Day 2 of 5 | 3 (Wed-Fri) |
| Wednesday | Day 3 of 5 | 2 (Thu-Fri) |
| Thursday | Day 4 of 5 | 1 (Fri) |
| Friday | Day 5 of 5 | 0 |
| Saturday | Weekend | 0 |
| Sunday | Weekend | 0 |

### Sunday-First Mode

**Week structure:** Sun-Mon-Tue-Wed-Thu-Fri-Sat  
**Work week:** 5 days (Mon-Fri)

| Day | Display | Days Remaining |
|-----|---------|----------------|
| Sunday | Day 1 of 7 | 5 (Mon-Fri) |
| Monday | Day 2 of 7 | 4 (Tue-Fri) |
| Tuesday | Day 3 of 7 | 3 (Wed-Fri) |
| Wednesday | Day 4 of 7 | 2 (Thu-Fri) |
| Thursday | Day 5 of 7 | 1 (Fri) |
| Friday | Day 6 of 7 | 0 |
| Saturday | Day 7 of 7 | 0 |

## Notes

- **Days remaining** always counts work days only (Mon-Fri, excluding today)
- Weekend days show 0 days remaining (no work days left in week)
- Sunday in Sunday-first mode shows 5 days remaining (full work week ahead)
- All date calculations are dynamic - change your preference anytime

## Testing

Run the test suite to validate both modes:

```bash
python3 .scripts/test-date-calculations-simple.py
```

All tests should pass for both Monday-first and Sunday-first modes.
