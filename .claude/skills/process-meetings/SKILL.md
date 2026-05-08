---
name: process-meetings
description: Process synced Granola meetings to update person pages, extract tasks, and organize meeting notes
model_hint: balanced
context: fork
hooks:
  PostToolUse:
    - matcher: Write
      type: command
      command: "node .claude/hooks/post-meeting-person-update.cjs"
  Stop:
    - type: command
      command: "node .claude/hooks/meeting-summary-generator.cjs"
---

# Process Meetings

Process meetings that have been synced from Granola by the background automation. Updates person pages, extracts tasks, and organizes meeting notes.

## Background Execution

This skill supports background execution. When invoked:
1. Acknowledge: "Processing [N] meetings in the background. I'll let you know when done."
2. Process all meetings
3. On completion, provide summary: "[N] meetings processed. [X] person pages updated. [Y] action items created."

## How It Works

When you run `/process-meetings`:
1. Fetches meetings from Granola (API or local cache fallback)
2. Runs LLM extraction to generate structured notes
3. Creates/updates person and company pages
4. Extracts action items to 03-Tasks/Tasks.md
5. Links everything together

## Arguments

- No arguments: Sync and process all unprocessed meetings from the last 7 days
- `today`: Only process today's meetings
- `"search term"`: Find meetings by title/attendee
- `--people-only`: Only update person/company pages (skip tasks)
- `--no-todos`: Create notes but don't extract tasks

## Pre-flight: Granola Check

Mobile recordings sync automatically as long as Granola is installed and the user is signed in to the desktop app. No separate authentication step needed.

---

## Process

### Step 1: Sync from Granola

First, fetch new meetings from Granola:

```bash
node .scripts/meeting-intel/sync-from-granola.cjs
```

This will:
- Fetch meetings from Granola API (or local cache as fallback)
- Run LLM extraction to generate structured notes
- Create/update files in `00-Inbox/Meetings/`
- Track processed meetings in state file

**Requirements:**
- Granola app installed ([granola.ai](https://granola.ai))
- User signed in to Granola desktop app
- An LLM API key in `.env` (GEMINI_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY)

### Step 2: Enrich with Calendar Context

For each synced meeting, match it with calendar events to get additional context:

1. **Read meeting frontmatter** to get `date` and approximate time
2. **Query calendar for that date:**
   ```javascript
   // Use calendar MCP to get events on the meeting date
   calendar_get_events({ date: "2026-05-06" })
   ```
3. **Match Granola meeting to calendar event:**
   - Compare meeting times (within ±30 min window)
   - Compare participant names/emails
   - Compare meeting titles (fuzzy match)
4. **Merge calendar context into meeting file:**
   - Add calendar attendees with full emails to frontmatter
   - Update meeting title if calendar has better context
   - Add meeting description if available
   - Mark participants as Internal/External based on email domains

**Benefits:**
- Full email addresses for accurate person page routing
- Better participant identification (calendar has full names + emails)
- Meeting purpose/context from calendar description
- More accurate internal vs external classification

**Frontmatter updates:**
```yaml
calendar_matched: true
calendar_event_id: "calendar-event-123"
calendar_attendees:
  - name: Aaron Srivastava
    email: aaron.srivastava@ghx.com
    status: accepted
```

### Step 3: Find Meetings to Process

Check which meetings have already been fully processed by the skill:
```bash
# Skill state file tracks person pages + task extraction
test -f .scripts/meeting-intel/skill-state.json && cat .scripts/meeting-intel/skill-state.json || echo '{}'
```

List meeting files from last 7 days:
```bash
find 00-Inbox/Meetings -name "*.md" -mtime -7 -type f
```

For each meeting file:
1. Read frontmatter to get `granola_id` (or `meeting_id`), `participants`, `companies`, `date`
2. Check skill state file - **skip if already processed** (unless meeting file was modified after processing)
3. For unprocessed meetings:
   - Check if person/company pages need creating/updating
   - Check for unchecked tasks in "For Me" / "Action Items" sections

Report findings:
> "Found X meetings. Y already processed (skipping). Z new meetings to process."

### Step 4: Update Person Pages

For each participant in synced meetings:

1. **Load user profile** for email domain:
   ```
   Read System/user-profile.yaml → get email_domain
   ```

2. **Classify as Internal/External:**
   - If participant email domain matches user's domain → Internal
   - Otherwise → External

3. **Check if person page exists:**
   - Internal: `05-Areas/People/Internal/{Name}.md`
   - External: `05-Areas/People/External/{Name}.md`

4. **If page doesn't exist, create it:**
   ```markdown
   # {Name}

   ## Overview

   | Field | Value |
   |-------|-------|
   | **Company** | {company from meeting} |
   | **Email** | {if available} |
   | **First Met** | {meeting date} |

   ## Recent Interactions

   - [{Meeting Title}](00-Inbox/Meetings/{date}/{slug}.md) — {date}

   ## Notes

   *Auto-created from meeting on {date}*
   ```

5. **If page exists, add meeting to Recent Interactions:**
   - Read existing page
   - Add new meeting link under "## Recent Interactions"
   - Keep max 20 entries (remove oldest if needed)
   - Update "Last Interaction" in frontmatter

### Step 5: Update Company Pages

For each unique external company domain:

1. **Check if company page exists:** `05-Areas/Companies/{Company}.md`

2. **If doesn't exist, create it:**
   ```markdown
   # {Company Name}

   ## Overview

   | Field | Value |
   |-------|-------|
   | **Website** | {domain} |
   | **Stage** | Unknown |
   | **First Contact** | {date} |

   ## Key Contacts

   - [[05-Areas/People/External/{Person}|{Person}]]

   ## Meeting History

   - [{Meeting Title}](00-Inbox/Meetings/{date}/{slug}.md) — {date}

   ## Notes

   *Auto-created from meeting on {date}*
   ```

3. **If exists, update:**
   - Add any new contacts to "Key Contacts"
   - Add meeting to "Meeting History"

### Step 6: Semantic Enrichment (if QMD available)

**Check if semantic search is available** by looking for `qmd` in PATH.

If available, enhance meeting processing with meaning-based intelligence:

1. **Detect implicit commitments:** For each meeting's discussion notes, search semantically:
   ```
   qmd query "we should circle back on..." --limit 3
   qmd query "let me think about..." --limit 3
   ```
   Catch soft commitments that regex action-item extraction misses.
   - Examples: "we should probably revisit the pricing model" → implicit action item
   - "I need to noodle on the migration approach" → implicit commitment
   - "Let's reconnect after the board meeting" → implicit follow-up

2. **Link meetings to projects:** For the meeting topic, search:
   ```
   qmd query "meeting topic/title" --limit 3
   ```
   against `04-Projects/` to auto-link the meeting to relevant projects that keyword matching would miss.

3. **Enrich person context:** For each new person encountered, search:
   ```
   qmd query "person name + company" --limit 3
   ```
   Find if they've been mentioned in other meetings/notes, even if they weren't a direct participant.

**Integration:**
- Add implicit commitments to the action items list with a note: "*(detected — not explicitly stated)*"
- Add project links to meeting frontmatter
- Merge person context into newly-created person pages
- If QMD unavailable, skip silently — regex extraction still works

### Step 7: Extract Tasks (unless --no-todos or --people-only)

For each meeting with unextracted tasks:

1. **Find action items** in the "## Action Items > ### For Me" section
2. **For each unchecked item** (`- [ ]`):
   - Extract task description
   - Get task ID (format: `^task-YYYYMMDD-XXX`)
   - Read pillar from meeting frontmatter

3. **Create task** using Work MCP:
   ```
   create_task(
     title: "Task description",
     priority: "P2",  // default, P1 if "urgent" mentioned
     pillar: "{from meeting}",
     people: ["{participants}"],
     source: "meeting:{meeting-path}"
   )
   ```

4. **Mark as extracted** by adding comment to meeting note:
   ```markdown
   <!-- tasks-extracted: 2026-02-03T10:30:00Z -->
   ```

5. **Update skill state file** after processing each meeting:
   ```javascript
   // Add to .scripts/meeting-intel/skill-state.json
   {
     "processedMeetings": {
       "meeting-id-123": {
         "processedAt": "2026-05-06T14:30:00Z",
         "filepath": "00-Inbox/Meetings/2026-05-06/Meeting_Title.md",
         "peopleUpdated": ["Aaron_Srivastava", "Daniel_Milburn"],
         "tasksExtracted": 3
       }
     }
   }
   ```

### Step 8: Summary Report

```
## Meeting Processing Complete ✅

**Synced from Granola:** X meetings (last 7 days)
**Already processed:** Y meetings (skipped)
**Newly processed:** Z meetings

### Updates Made

**Person pages:**
- Created: 3 new (Alice Chen, Bob Smith, Carol Wang)
- Updated: 5 existing

**Company pages:**
- Created: 1 new (Acme Corp)
- Updated: 2 existing

**Tasks extracted:** 7 items added to 03-Tasks/Tasks.md

### Recent Meetings

| Date | Meeting | Company | Participants |
|------|---------|---------|--------------|
| May 6 | Product Review | Acme | Alice, Bob |
| May 5 | Strategy Call | BigCo | Carol |
```

## Error Handling

**If no meetings found in Granola:**
> "No meetings found in the last 7 days. Make sure:
> 1. Granola is installed and you're signed in to the desktop app
> 2. You're recording meetings with Granola
> 3. Check Granola credentials: `~/Library/Application Support/Granola/supabase.json`"

**If sync script fails:**
> "Sync from Granola failed. Check:
> 1. `.env` has LLM API key (GEMINI_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY)
> 2. Granola credentials exist (signed in to desktop app)
> 3. Logs: `.scripts/logs/meeting-intel.stderr.log`"

## Examples

```
/process-meetings
```
> "Syncing from Granola... Found 8 meetings. 3 already processed (skipping). Processing 5 new meetings..."

```
/process-meetings today
```
> "Syncing from Granola... Found 2 meetings from today. Processing..."

```
/process-meetings --people-only
```
> "Syncing from Granola... Updating person and company pages only (skipping task extraction)..."

```
/process-meetings "Acme"
```
> "Syncing from Granola... Found 3 meetings matching 'Acme'. Processing..."

---

## Track Usage (Silent)

Update `System/usage_log.md` to mark meeting processing as used.

**Analytics (Silent):**

Call `track_event` with event_name `meetings_processed` and properties:
- `meetings_count`: number of meetings processed
- `people_created`: number of new person pages created
- `todos_extracted`: number of tasks extracted

This only fires if the user has opted into analytics. No action needed if it returns "analytics_disabled".
