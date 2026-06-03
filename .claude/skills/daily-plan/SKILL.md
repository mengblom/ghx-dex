---
name: daily-plan
description: Generate context-aware daily plan with calendar, tasks, and priorities. Includes midweek awareness, meeting intelligence, commitment tracking, and smart scheduling suggestions.
model_routing:
  default: balanced
  steps:
    data-gathering: fast
    synthesis: balanced
context: fork
hooks:
  Stop:
    - type: command
      command: "node .claude/hooks/daily-plan-quick-ref.cjs"
---

## Purpose

Generate your daily plan with full context awareness. Automatically gathers information from your calendar, tasks, meetings, relationships, and weekly progress to create a focused plan with genuine situational awareness.

## Usage

- `/daily-plan` — Create today's daily plan
- `/daily-plan tomorrow` — Plan for tomorrow (evening planning)
- `/daily-plan --setup` — Re-run integration setup

---

## Tone Calibration

Before executing this command, read `System/user-profile.yaml` → `communication` section and adapt tone accordingly (see CLAUDE.md → "Communication Adaptation").

---

## Step 0: Demo Mode Check

Before anything else, check if demo mode is active:

1. Read `System/user-profile.yaml`
2. Check `demo_mode` value
3. **If `demo_mode: true`:**
   - Display banner: "Demo Mode Active — Using sample data from System/Demo/"
   - Use demo paths and skip live integrations
4. **If `demo_mode: false`:** Proceed normally

---

## Step 1: Background Checks (Silent)

Run these silently without user-facing output:

1. **Update check**: `check_for_updates(force=False)` - store notification if available
2. **Self-learning checks**: Run changelog and learning review scripts if due
3. **Search index refresh**: Run `qmd update && qmd embed` to refresh vault search index with any overnight changes (meetings processed, files edited, etc.). If `qmd` is not installed, skip silently.
4. **People index refresh**: Call `build_people_index` from Work MCP. This keeps the People Directory current so person lookups throughout the day are fast. Takes <2 seconds.
5. **Innovation synthesis** (silent): Call `synthesize_changelog()` and `synthesize_learnings()` from Improvements MCP. These run in background and populate the backlog — results are surfaced in Step 1.5 below.
6. **Granola check** (silent): Granola meeting sync uses the desktop app's stored credentials automatically. No migration check needed.

---

## Step 1.5: Innovation Spotlight (Concierge)

After background checks complete, check for noteworthy backlog activity:

1. Call `list_ideas(status="active", min_score=70)` from Improvements MCP
2. Check `System/.synthesis-state.json` for recent synthesis activity (last 7 days)
3. If there are AI-authored or recently enriched ideas, pick the most impactful one

**Surface as a brief spotlight in the plan output (1-2 lines max):**

> **Innovation Spotlight:** Claude Code shipped native memory (v2.1.32) — this could simplify idea-006 (Session Memory MCP). Run `/dex-improve idea-006` to explore.

**Rules:**
- Show at most 1 spotlight per daily plan (don't overwhelm)
- Rotate through ideas — don't show the same one twice in a row
- Only show if there's genuine "Why Now?" urgency (new evidence in last 7 days)
- If no recent synthesis activity, skip this section entirely
- Never block the plan for this — it's a helpful aside, not a gate

---

## Step 2: Morning Journal Check (If Enabled)

If `journaling.morning: true` in user-profile.yaml, check for today's morning journal and prompt if missing.

---

## Step 3: Monday Weekly Planning Gate

If today is Monday and week isn't planned, offer to run `/week-plan` first.

---

## Step 4: Yesterday's Review Check (Soft Gate) + Daily Note Lookback

Check for yesterday's review and daily note to extract context.

**From yesterday's review:**
- Open loops
- Tomorrow's focus (today's intention)
- Blocked items

**From yesterday's daily note:**

Look for `00-Inbox/Daily_Notes/YYYY-MM-DD.md` (yesterday's date).

If found:
- Extract uncompleted tasks → Surface as potential carryovers
- Extract notes mentioning "tomorrow" or "follow up" → Surface as context
- Extract journal insights → Provide emotional continuity

**Example output:**

> 📝 **From Yesterday's Daily Note:**
> 
> Uncompleted task: "Review pricing proposal" — should this be in today's plan?
> 
> Note: "Need to follow up with Sarah about Q2 budget" — relevant for today?

**If neither review nor daily note exist:** Proceed without yesterday's context.

---

## Step 5: Context Gathering (ENHANCED)

Gather context from all available sources. **This is where the magic happens.**

**CRITICAL: Calendar Configuration**

Before making ANY calendar queries, read `System/user-profile.yaml` and check for `calendar.primary_calendar_name`. If present, pass this value as the `calendar_name` parameter to ALL calendar MCP calls. If not present, let the MCP use its default.

Example:
```yaml
calendar:
  primary_calendar_name: "mengblom@ghx.com"
```

Then call:
```
calendar_get_today(calendar_name="mengblom@ghx.com")
calendar_get_events(calendar_name="mengblom@ghx.com", ...)
```

**CRITICAL: Calendar Validation (BLOCKING)**

After calling the calendar MCP, validate the response:

1. **Check if the call succeeded:**
   - If `success: false` or the MCP call errors → STOP IMMEDIATELY
   - Display error message:
     ```
     ❌ Calendar integration failed. Cannot generate daily plan without accurate calendar data.
     
     Error: [error message from MCP]
     
     Please check:
     - Calendar MCP is running: pkill -f calendar_server.py && restart
     - Calendar access is granted
     - Calendar name is correct in System/user-profile.yaml
     
     Run /health-check to diagnose.
     ```
   - Exit the skill - DO NOT proceed with daily plan generation

2. **Sanity check event count (weekdays only):**
   - If today is Monday-Friday AND event count < 3:
     ```
     ⚠️ Calendar returned only [X] events for today ([Day]).
     
     Events found:
     - [list events with times]
     
     This seems low for a typical work day. Is this correct?
     
     Options:
     1. Yes, this is accurate (proceed with plan)
     2. No, something's wrong (exit and check calendar)
     3. Check a different calendar (specify name)
     ```
   - Wait for user confirmation before proceeding
   - If user says "No" or "something's wrong" → exit and suggest /health-check
   
3. **Only proceed if:**
   - Calendar MCP returned success: true
   - Event count validated (either ≥3 events, OR user confirmed <3 is correct, OR weekend)

**This is a BLOCKING check. Never generate a daily plan with incomplete calendar data.**

### 5.0.5 Timezone Conversion (CRITICAL)

**IMPORTANT:** Calendar events are returned in UTC. They MUST be converted to the user's timezone before display or use.

**Process:**
1. Read `System/user-profile.yaml` → `timezone` field (e.g., `America/Denver`)
2. For EVERY calendar event, convert UTC time to user's timezone
3. Display times in 24-hour format (e.g., "09:05 MT")

**Example:**
- Calendar returns: `Start Time: 2026-06-03 15:05:00 +0000` (UTC)
- User timezone: `America/Denver` (Mountain Time, UTC-6 in summer)
- Convert: 15:05 - 6 = 09:05
- Display: "09:05 MT"

**Reference:** See `.claude/lib/timezone-utils.md` for complete conversion rules and common pitfalls.

**Rules:**
- NEVER display UTC times directly to the user
- Always reference the timezone explicitly (e.g., "MT", "Mountain Time")
- Use 24-hour format (09:05, 14:30, not 9:05 AM or 2:30 PM)
- Convert ALL times: meeting start/end, free blocks, capacity analysis

### 5.1 Midweek Progress Check (NEW)

```
Use: get_week_progress()
```

This is critical for genuine situational awareness. Extract:
- Day of week and days remaining
- Weekly priority status (complete / in_progress / not_started)
- Warnings for priorities with no activity

**Surface this prominently:**

> "It's **Wednesday**. Here's where you are on this week's priorities:
> 
> 1. ✅ **Ship pricing page** — Complete (finished Monday)
> 2. 🔄 **Review proposal** — In progress (2 of 5 tasks done)
> 3. ⚠️ **Customer interviews** — Not started (no activity yet)
> 
> You have 2 days left this week. Priority 3 needs attention."

### 5.2 Calendar Capacity Analysis (NEW)

```
Use: analyze_calendar_capacity(days_ahead=1, events=[...from calendar MCP...])
```

Understand the *shape* of today:

- **Day type**: stacked / moderate / open
- **Meeting count and hours**
- **Free blocks available**
- **Recommendation**: What kind of work fits today

**Surface this:**

> "📅 **Today's shape:** Moderate (4 meetings, 3 hours total)
> 
> **Free blocks:**
> - 8:00-9:30 AM (90 min) — Morning focus time
> - 2:00-4:00 PM (120 min) — Afternoon block
> 
> **Recommendation:** Good for medium tasks and meeting prep. Deep work fits the 2-4pm block."

### 5.3 Meeting Intelligence (NEW)

For each meeting today:

```
Use: get_meeting_context(meeting_title="...", attendees=[...])
```

Get genuine context, not just attendee names:
- **Related project**: What project is this connected to?
- **Project status**: What's outstanding? What's blocked?
- **Outstanding tasks with attendees**: What do you owe them? What do they owe you?
- **Prep suggestions**: What should you review before this meeting?

**Surface this with surprise and delight:**

> "📍 **Meeting: Acme Quarterly Review** (2pm with Sarah Chen, Mike Ross)
> 
> **Related project:** Acme Implementation (Phase 2)
> - Status: On track, but pricing section still in draft
> - Outstanding: You owe Sarah the pricing proposal
> 
> **Prep suggestion:** Review proposal draft, prepare pricing options. Block 30 min before this meeting?"

### 5.4 Commitment Tracking (NEW)

```
Use: get_commitments_due(date_range="today")
```

Surface things you said you'd do:

> "⚡ **Commitments due today:**
> 
> - You told Mike you'd get back to him by Wednesday (from Monday 1:1)
> - Follow up on competitive analysis (from Acme meeting)"

### 5.5 Task Scheduling Suggestions (NEW)

```
Use: suggest_task_scheduling(include_all_tasks=False, calendar_events=[...])
```

Match tasks to available time based on effort classification:

> "📋 **Scheduling suggestions:**
> 
> | Task | Effort | Suggested Time |
> |------|--------|----------------|
> | Write Q1 strategy doc | Deep work (2-3h) | Tomorrow (you have a 3h morning block) |
> | Review Sarah's proposal | Medium (1h) | Today 2-3pm (before Acme meeting) |
> | Reply to Mike | Quick (15min) | Between meetings |
> 
> ⚠️ **Heads up:** You have 2 deep work tasks but today's too fragmented. Consider protecting tomorrow morning."

### 5.6 Semantic Context Enrichment (if QMD available)

**This step runs automatically when QMD is installed via `/enable-semantic-search`.** It adds a semantic search layer on top of the standard context gathering to surface connections that keyword search misses.

Check if QMD MCP tools are available by calling `qmd_status`. **If available:**

1. **For each meeting today**, run:
   ```
   qmd_search(query="[meeting topic] [attendee names]", limit=3)
   ```
   Surface: past discussions, related decisions, relevant commitments that share **meaning** but not keywords with this meeting. Example: a meeting about "customer onboarding" finds notes about "activation rates" and "time to value".

2. **For each weekly priority that's lagging**, run:
   ```
   qmd_search(query="[priority description]", limit=3)
   ```
   Surface: vault content that advances or relates to this priority but wouldn't appear in a keyword search. Especially useful for finding forgotten context about stalled work.

3. **Cross-topic connection scan:**
   ```
   qmd_search(query="[today's key themes combined]", limit=5)
   ```
   Surface: unexpected connections between today's meetings, tasks, and priorities. This is where semantic search shines — finding that a 2pm customer call relates to a PRD you wrote last month using completely different terminology.

4. **Merge with existing context** — only add genuinely new insights. Don't duplicate what Steps 5.1-5.5 already found. Mark semantic results with their source so the plan output can distinguish them.

**What this enables in the plan output:**
- Meeting context sections include "**Also relevant:**" with thematically related past discussions
- Priority recommendations cite relevant vault content discovered by meaning
- "Heads Up" section catches connections between seemingly unrelated items
- Focus recommendations are informed by deeper vault knowledge

**If QMD is not available:** Skip silently. Steps 5.1-5.5 and 5.7 provide full context via standard methods.

---

### 5.7 Reminders Completion Sync (Dex Today → Dex)

Check if any tasks were completed on phone since the last plan:

```
Use: reminders_list_completed(list_name="Dex Today")
```

For each completed item:
- Match to a Dex task by title
- Update task status via Work MCP: `update_task_status(task_title="...", status="d")`
- Surface what was synced:

> "📱 **Synced from phone:**
> - ✅ "Follow up with Hero Coders" — marked done in Dex"

**If nothing to sync:** Skip silently.

### 5.8 Email Intelligence (if Gmail connected)

Check `System/integrations/config.yaml` for `google-workspace.enabled: true`.

If enabled and MCP healthy:
1. Get unread count and priority emails from monitored labels
2. Flag emails needing reply (> 48h since received, from key contacts in `05-Areas/People/`)
3. Surface email threads with today's meeting attendees

Include in plan:

> "Email: [X] unread, [Y] need replies. [Z] threads with today's meeting attendees."

If unhealthy: skip silently (graceful degradation -- no error to user).

### 5.9 Teams Intelligence (if Teams connected)

Check `System/integrations/config.yaml` for `teams.enabled: true`.

If enabled and MCP healthy:
1. Get unread messages from priority channels
2. Surface DMs needing response
3. Check for mentions

Include in plan:

> "**Teams:** [X] unread chats, [Y] mentions. [Z] threads with today's meeting attendees."

If BOTH Slack and Teams enabled:
- Show both digests, clearly labeled: "**Slack:** ..." and "**Teams:** ..."
- Deduplicate if the same person appears in both (merge context, label the source)
- Present side by side in the plan output under a combined "Chat Intelligence" heading

If unhealthy: skip silently (graceful degradation -- no error to user).

### 5.10a Mobile Capture Check (Dex Inbox)

```
Use: reminders_list_items(list_name="Dex Inbox")
```

If items found, surface:

> 📱 **Captured on phone** (3 items in Dex Inbox):
>
> 1. "Follow up with Peter about roadmap" — captured yesterday 4:32pm
> 2. "Look into Rovo for in-app guides" — captured today 2:15pm
> 3. "Send Anastasia the productized offering doc" — captured today 11:45am
>
> **Triage these now?** I'll help assign pillars and priorities.

**Triage flow:**
- Present each item
- Infer pillar (using existing smart pillar inference)
- Confirm with user
- Create task via Work MCP `process_inbox_with_dedup`
- Mark Reminder as complete via `reminders_complete_item`

**If Dex Inbox is empty:** Skip silently (no "0 items captured" noise).

### 5.10b Standard Context Gathering

Also gather:
- **Calendar**: Today's meetings with times and attendees
  - **CRITICAL: Calendar times are the SINGLE SOURCE OF TRUTH**
  - Never override calendar times with information from project docs, week priorities, or any other source
  - Project docs provide CONTEXT (topics, prep materials) but calendar provides WHEN
  - If calendar says 4:00 PM and project doc says 1:30 PM → calendar wins, always
- **Tasks**: P0, P1, started-but-not-completed, overdue
- **Week Priorities**: This week's Top 3
- **Work Summary**: Quarterly goals context (if enabled)
- **People**: Context for meeting attendees
- **Self-Learning Alerts**: Changelog updates, pending learnings

---

## Step 6: Synthesis

Combine all gathered context into actionable recommendations:

### Focus Recommendation

Generate 3 recommended focus items based on:
- P0 tasks (highest weight)
- Weekly priority alignment (especially lagging priorities!)
- Meeting prep needs
- Commitments due

**The system should actively recommend, not just list:**

> "Based on your week progress and today's shape, I recommend focusing on:
> 
> 1. **Prep for Acme meeting** — Priority 2 is lagging and this meeting is critical
> 2. **Reply to Mike** — Commitment due today
> 3. **Task X from Priority 1** — Keeps momentum on your shipped priority"

### Meeting Prep (Enhanced)

**CRITICAL: Display ALL calendar events returned by the MCP.**
- No filtering, no de-duplication, no smart selection
- If calendar returns 8 events, the plan must show 8 meetings
- If there are duplicate titles at the same time (e.g., two Kickdrum meetings), show both
- ONLY exclude all-day events (e.g., "Out of Office", holidays)

For each meeting, show:
- **Meeting time from calendar** (NEVER from project docs or other sources)
  - **IMPORTANT:** Convert UTC times to user's timezone (see Step 5.0.5)
  - Display in 24-hour format with timezone (e.g., "09:05 MT")
- Who's attending + People/ context
- Related project status
- Outstanding tasks with attendees
- Suggested prep time and what to prepare

**CRITICAL RULES:**
- Use calendar times exclusively (Project documents provide context about WHAT to discuss, but calendar is authoritative for WHEN)
- Convert ALL times from UTC to user's timezone before display (read `timezone` from `System/user-profile.yaml`)
- Use 24-hour format (09:05, 14:30, not 9:05 AM or 2:30 PM)

### Heads Up (Enhanced)

Flag potential issues:
- Weekly priorities with no activity (midweek warning)
- Commitments due today
- Back-to-back meetings
- P0 items with no time blocked
- Deep work tasks with no suitable slot this week

---

## Step 7: Generate Daily Plan

**IMPORTANT - Date Calculation:**
- The MCP returns `days_elapsed` (0=Monday, 1=Tuesday, ..., 4=Friday)
- For display "Day X of 5", use: `X = days_elapsed + 1`
- Example: Wednesday has days_elapsed=2, so "Day 3 of 5"
- For frontmatter `week_day`, use: `days_elapsed + 1`
- The MCP returns `days_remaining` counting work days only (Mon-Fri)

**CRITICAL - Meeting Times:**
- **ALL meeting times must come from the calendar query results**
- **Convert UTC times to user's timezone** (read from `System/user-profile.yaml` → `timezone`)
- Display in 24-hour format with timezone reference (e.g., "09:05 MT")
- Do NOT use times from Week Priorities, project documents, or any other source
- Project documents provide context (agenda, prep materials) but calendar is authoritative for times
- If there's a conflict between calendar and other sources, calendar always wins

Create `00-Inbox/Daily_Plans/YYYY-MM-DD.md` (note: active plans go in Inbox, not Archives):

```markdown
---
date: YYYY-MM-DD
type: daily-plan
week_day: {{days_elapsed + 1}}  # 1=Monday, 2=Tuesday, 3=Wednesday, etc.
days_remaining: {{days_remaining}}  # Work days left (Mon-Fri only)
integrations_used: [calendar, tasks, people, work-intelligence]  # calendar is ALWAYS present (required)
calendar_events_count: {{X}}  # Number of events returned by calendar MCP
---

# Daily Plan — {{Day}}, {{Month}} {{DD}}

## TL;DR
- {{1-2 sentence summary including week progress}}
- {{X}} meetings today, day is {{stacked/moderate/open}}
- {{Key focus area based on week priorities}}

---

## 📊 Week Progress (Midweek Check)

**Day {{X}} of 5** — {{days_remaining}} days left this week

| Priority | Status | Notes |
|----------|--------|-------|
| {{Priority 1}} | ✅ Complete | Finished {{day}} |
| {{Priority 2}} | 🔄 In progress | {{X}} of {{Y}} tasks done |
| {{Priority 3}} | ⚠️ Not started | Needs attention |

**This week's focus:** {{Recommendation based on lagging priorities}}

---

## 📅 Today's Shape

**Day type:** {{stacked/moderate/open}} ({{X}} meetings, {{Y}} hours)

**Free blocks:**
- {{Time range}}: {{Size}} — {{Recommended use}}

**Best for:** {{Quick tasks only / Medium tasks / Deep work opportunity}}

---

## ⚡ Commitments Due Today

- [ ] {{Commitment}} — from {{source}}
- [ ] {{Commitment}} — from {{source}}

---

## 🎯 Today's Focus

**If I only do three things today:**

1. [ ] {{Focus item 1}} — {{Pillar}} *(supports Week Priority #X)*
2. [ ] {{Focus item 2}} — {{Pillar}} *(supports Week Priority #Y)*
3. [ ] {{Focus item 3}} — {{Pillar}}

---

## 📍 Meetings (with Context)

### {{Time}} — {{Meeting Title}}

**Attendees:** {{Names}}
**Related project:** {{Project name}} ({{status}})
**Outstanding with them:**
- {{Task/commitment}}

**Prep needed:** {{What to review/prepare}}
**Suggested prep time:** {{Block X min before}}

---

### {{Time}} — {{Meeting Title}}

[Repeat for each meeting]

---

## 📋 Task Scheduling

| Task | Effort | Suggested Slot | Reason |
|------|--------|----------------|--------|
| {{Task}} | Deep work | {{Day/time}} | {{Reason}} |
| {{Task}} | Medium | {{Day/time}} | {{Reason}} |
| {{Task}} | Quick | Between meetings | Batch these |

{{If deep work capacity warning}}
> ⚠️ You have {{X}} deep work tasks but only {{Y}} suitable slots this week. Consider protecting time or deferring.

---

## ⚠️ Heads Up

- {{Warning about lagging weekly priority}}
- {{Commitment due today}}
- {{Back-to-back meetings}}
- {{Other flags}}

---

*Generated: {{timestamp}}*
*Week progress: {{X}}/{{Y}} priorities on track*
```

---

## Step 7.5: Push Focus Tasks to Reminders (Dex → iPhone)

After generating the plan, push today's P0 and P1 focus tasks to Apple Reminders for native iOS notifications:

1. **Clear yesterday's items:**
   ```
   Use: reminders_clear_completed(list_name="Dex Today")
   ```

2. **Push today's focus items:**
   For each P0/P1 task in today's focus:
   ```
   Use: reminders_create_item(
       list_name="Dex Today",
       title="Task title",
       notes="From Dex daily plan",
       due_date="YYYY-MM-DD"
   )
   ```

3. **Confirm silently:**
   > "📱 Pushed 3 focus tasks to iPhone Reminders (Dex Today)"

**If Reminders MCP unavailable:** Skip silently.

---

## Step 8: Track Usage (Silent)

Update `System/usage_log.md` to mark daily planning as used.

**Analytics (Silent):**

Call `track_event` with event_name `daily_plan_completed` and properties:
- `meetings_count`: number of meetings today
- `tasks_surfaced`: number of tasks shown
- `priorities_count`: number of priorities

This only fires if the user has opted into analytics. No action needed if it returns "analytics_disabled".

---

## Graceful Degradation

**Calendar MCP is REQUIRED** - the skill will not run without it (see Step 5 validation).

For other MCPs, the plan degrades gracefully:

### Full Context (All MCPs available)
- Complete week progress, meeting intelligence, scheduling suggestions
- Maximum "surprise and delight"

### Partial Context (Calendar + some other MCPs)
- Calendar meetings always shown (required)
- Week progress if Work MCP available
- Task scheduling if Work MCP available
- Other integrations degrade gracefully

### Calendar MCP Failure
- Skill exits immediately with error message
- User directed to /health-check
- No daily plan generated with incomplete data

---

## MCP Dependencies (Updated)

| Integration | MCP Server | Tools Used |
|-------------|------------|------------|
| Calendar | dex-calendar-mcp | `calendar_get_today`, `calendar_get_events_with_attendees` |
| Reminders | dex-calendar-mcp | `reminders_list_items`, `reminders_complete_item`, `reminders_create_item`, `reminders_ensure_lists`, `reminders_list_completed`, `reminders_find_and_complete`, `reminders_clear_completed` |
| Granola | dex-granola-mcp | `get_recent_meetings` |
| Work | dex-work-mcp | `list_tasks`, `get_week_progress`, `get_meeting_context`, `get_commitments_due`, `analyze_calendar_capacity`, `suggest_task_scheduling` |
| Improvements | dex-improvements-mcp | `synthesize_changelog`, `synthesize_learnings`, `list_ideas` |
| Google Workspace | google-workspace-mcp | Gmail query, email search (if enabled) |
| Teams | teams-mcp | `teams_list_chats`, `teams_search_messages`, `teams_health_check` (if enabled) |