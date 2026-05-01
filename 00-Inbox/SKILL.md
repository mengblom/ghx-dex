---
name: process-inbox
description: Process and organize all files in the Obsidian vault inbox. Use when the user asks to "process inbox", "organize inbox", "clean up inbox", or mentions inbox processing/management.
user-invocable: true
---

# Process Inbox - Obsidian Vault Automation

You are processing files in the user's Obsidian vault inbox (00 - Inbox) according to their Johnny Decimal organizational system.

## Your Task

Systematically process ALL files in "00 - Inbox" and "00 - Inbox/Daily Notes/" ONE FILE AT A TIME:

**For each file** (Steps 2-13):
1. Standardize, enrich, categorize, link, and move to permanent location
2. QA check filename immediately after move
3. Extract user opinions for KB immediately if file has kb_insights: true

⚠️ **ALL STEPS PER FILE** - Each file is fully processed (including QA and opinion extraction) before starting the next file.

## Frontmatter Template

All processed files must have this frontmatter:

```yaml
---
date: "YYYY-MM-DD"                    # ISO format date
tags: [tag1, tag2, tag3]              # Both specific topics AND broad thematic categories (3-8 tags)
content_type: "meeting_note"          # See Step 4 for decision tree: meeting_note (most common), daily_note, email, interview, presentation, document (rare)
participants: [Person1, Person2]      # For meetings and interviews only
meeting_type: "1-on-1"                # For meetings: 1-on-1, staff_meeting, technical_review, planning_session, recruiting
project: "Project Name"               # If applicable: AI Native Dev, Recruiting, New Org 2026, Laguna Offsite, Exchange Platform Architecture, IdP Replacement
destination_category: "60-69 Archive" # Where file was moved
kb_insights: true                     # Whether KB insights should be extracted
---
```

**⚠️ IMPORTANT**: Most files are `meeting_note` or `daily_note`. Use `document` ONLY when file doesn't fit other categories. See Step 4 for detailed decision tree.

## Processing Workflow

**⚠️ SEQUENTIAL PROCESSING REQUIRED**: Complete ALL steps (2-13) for ONE file before starting the next file. No batch processing. No parallel operations.

### Step 1: List All Files
```bash
obsidian files folder="00 - Inbox" format=json
obsidian files folder="00 - Inbox/Daily Notes" format=json
```

**EXCEPTION**: Skip today's daily note (YYYY-MM-DD.md matching current date). It must remain active.

### Step 1.5: Read Category README Files
**⚠️ CRITICAL**: Read these READMEs to understand categorization rules:

```bash
obsidian read path="10-19 Planning/README.md"
obsidian read path="20-29 Projects/README.md"
obsidian read path="40-49 People/README.md"
obsidian read path="50-59 Knowledge Base/README.md"
obsidian read path="60-69 Archive/README.md"
```

Extract from READMEs: Purpose, what belongs/doesn't belong, subcategories, organization guidelines, lifecycle workflows.

### Step 2: Read File Content
```bash
obsidian read file="[filename]"
```

### Step 3: Standardize Filename IMMEDIATELY
**⚠️ CRITICAL**: Rename BEFORE analyzing content.

**Format Rules**:
- **Regular files**: `YYYY-MM-DD HH.MM [ORIGINAL TITLE].md`
- **Daily notes**: `YYYY-MM-DD.md` (no time)
- **No date duplication**: If title starts with YYYY-MM-DD, add time only

**Process**: Extract date/time from filename, metadata, frontmatter, email headers, or meeting metadata. Convert time to HH.MM format (e.g., "14:30" → "14.30", "2:00 PM" → "14.00").

```bash
obsidian rename file="[original-name]" name="YYYY-MM-DD HH.MM [TITLE].md"
```

**Examples**: `Meeting.md` → `2026-03-05 14.00 Meeting.md` | `2026-03-05 Staff.md` → `2026-03-05 14.00 Staff.md` | `Daily Notes/2026-04-17.md` stays as-is

### Step 4: Analyze Content

**Determine content_type using this decision tree** (check in order):

1. **daily_note** - Daily journal entry
   - Signals: In Daily Notes folder, filename is YYYY-MM-DD.md, contains multiple unrelated topics, personal reflections, tasks/todos for the day
   - NOT a daily note if: Focused on single meeting/topic

2. **meeting_note** - Notes from a meeting or discussion
   - Signals: Has participants, contains discussion/decisions/action items, mentions meeting time, agenda items, has structure like "Topics Discussed" or "Action Items"
   - Includes: 1-on-1s, staff meetings, technical reviews, planning sessions
   - NOT a meeting note if: No discussion or participants

3. **interview** - Recruiting interview notes
   - Signals: Candidate name, interview questions/answers, scorecard, hiring decision, resume discussion
   - NOT an interview if: Not about hiring

4. **email** - Email or message captures
   - Signals: Has "To:", "From:", "Subject:", email headers, or explicitly says "email" or "message" in title/content
   - Includes: Slack messages, correspondence captures
   - NOT email if: Formatted as normal prose without headers

5. **presentation** - Presentation materials or slide content
   - Signals: Slide structure, bullet points per slide, "Slide 1", "Slide 2", presentation agenda
   - NOT presentation if: Just normal notes

6. **document** - Formal documents, reports, reference materials (RARE - use only if none of the above fit)
   - Signals: Formal structure, executive summary, structured report format, reference material
   - Use ONLY when file doesn't fit any category above
   - **Most files should NOT be documents** - they're usually meeting notes

**Then determine**:
- **Tags** (3-8 tags combining specific topics AND broad themes):
  - **Specific topics**: Extract proper nouns, team names, products, initiatives, technologies
    - Examples: CoreUI, Mapping, IPA, MongoDB, AuditDB, JFrog, GitHub, Happiest-Minds, Visibility-Team
  - **Broad thematic categories**: High-level themes that group related work
    - Examples: Engineering, Product, Organization, Hiring, AI-Platform, Architecture, Leadership, Strategy, Performance, Testing, Infrastructure, Automation, Security, OKR
  - **Content-type tags**: Always include structural tags
    - Examples: daily_note, meeting, journal, email, interview, reference, correspondence
  - **Process**: 
    1. Scan headings, key phrases, and proper nouns for specific topics
    2. Identify 2-4 specific topics (teams, products, initiatives mentioned)
    3. Identify 1-3 broad themes (what areas of work does this touch?)
    4. Add content-type structural tag
    5. Total: 3-8 tags (avoid generic tags like "work_updates", "meetings", "daily_planning")
- Participants (if meeting or interview)
- Related project (if applicable)
- Destination category (consult READMEs from Step 1.5)
- KB insights (flag if contains strategic insights, principles, lessons, or perspectives)
- **Transcript detection**: >500 lines, speaker labels, timestamps, "transcript" in title

### Step 4.5: Handle Transcripts (if detected)
**Only if transcript detected in Step 4**, perform these substeps:

1. Extract transcript content from original file
2. Create transcript file: `[filename]-Transcript.md` in `60-69 Archive/63 Transcripts/YYYY/QN/`
3. Add transcript frontmatter: `date`, `content_type: "transcript"`, `source_note: "[[original]]"`, `destination_category`
4. Create summary (5-15 bullets): decisions, action items, root causes, strategic insights
5. Replace transcript in original with: `## Summary\n[bullets]\n\n**Full Transcript**: [[filename-Transcript]]`
6. Archive transcript file to `60-69 Archive/63 Transcripts/YYYY/QN/`

**After Step 4.5 is complete (or skipped if no transcript)**, continue with Step 5.

### Step 5: Check for Ambiguity
**Before asking user**: Consult READMEs (Step 1.5) to resolve ambiguity. Re-read "What Belongs Here", "What Does NOT Belong Here", "Typical Workflow", subcategories, and organization guidelines.

**Only use AskUserQuestion if**: READMEs don't resolve destination, multiple categories fit, project association unclear, or content type ambiguous.

### Step 6: Add/Update Frontmatter
**Add these properties for ALL files**:
```bash
obsidian property:set name="date" value="YYYY-MM-DD" file="[filename]"
obsidian property:set name="tags" value="tag1,tag2,tag3" type=list file="[filename]"
# Tags should include: specific topics (2-4) + broad themes (1-3) + content-type tag (1)
# Example: tags="CoreUI,Mapping,IPA,Engineering,AI-Platform,Testing,daily_note"
obsidian property:set name="content_type" value="meeting_note" file="[filename]"
obsidian property:set name="destination_category" value="60-69 Archive" file="[filename]"
obsidian property:set name="kb_insights" value=true type=checkbox file="[filename]"
```

**Add these ONLY when applicable**:
```bash
# For meetings and interviews only:
obsidian property:set name="participants" value="Person1,Person2" type=list file="[filename]"

# For meetings only (not interviews):
obsidian property:set name="meeting_type" value="staff_meeting" file="[filename]"

# If file relates to a known project:
obsidian property:set name="project" value="Project Name" file="[filename]"
```

### Step 7: Add Links Within File (Optional)
**Only if clear relationships exist**, append wikilinks to:
- Related notes (if file references specific other notes)
- Project pages (if file has `project` field set)
- People profiles (if specific people are central to the content)

**Skip this step if**: File is standalone or relationships aren't obvious.

```bash
obsidian append file="[filename]" content="\n\n## Related\n- [[Related Note]]\n- [[Project Name]]\n- [[Person Name]]"
```

### Step 8: Create Destination Folders
Create folder structures as needed:
- Meeting notes: `60-69 Archive/61 Meeting Notes/YYYY/QN/`
- Daily notes: `60-69 Archive/62 Daily Notes/YYYY/MM-Month/`
- Transcripts: `60-69 Archive/63 Transcripts/YYYY/QN/`
- Correspondence: `60-69 Archive/64 Correspondence/YYYY/`

Use `mkdir -p` via Bash tool.

### Step 9: Move to Destination
```bash
obsidian move file="[filename]" to="[destination-path]/"
```

### Step 10: Update Other Files (Optional)
**Only if specific updates needed**, perform:
- Add backlinks in related notes (if file explicitly references them)
- Update MOCs (if file should be listed in a Map of Content)
- Link from project/people files (if central to that entity)

**Skip this step if**: No other files need updating. Most files can skip this.

### Step 11: QA - Verify Filename Format
**⚠️ CRITICAL QA**: After moving file, immediately verify filename conforms.

**Verify**:
- Regular files: `YYYY-MM-DD HH.MM [TITLE].md` (valid date, time with period separator, title, .md extension)
- Daily notes: `YYYY-MM-DD.md` (no time, .md extension)

**If fails**: Report issue, fix immediately in destination folder, re-verify.

### Step 12: Extract User Opinions for KB (if flagged)
**If kb_insights: true for this file**: Immediately extract user opinions and update KB.

**PURPOSE**: Extract the USER'S opinions, thinking, and philosophy from this file - not facts or status updates.

**Look for opinion markers**:
- "I think", "my view", "we should", "better approach", "the problem is"
- Principles being articulated
- Critiques of current approaches
- Lessons learned and philosophical conclusions
- Perspectives on how things should work

**Process**:
1. Read KB README to get current Opinion Categories and Mapping: `obsidian read path="50-59 Knowledge Base/README.md"`
2. Extract opinion categories table from README (section "Opinion Categories and Mapping")
3. Extract evident user opinions from THIS file (detailed but don't extrapolate beyond what's stated)
4. Map opinions to appropriate KB article using the table from step 2
5. Update existing KB article OR create new article if needed (use KB Article Structure from README)
6. Add source attribution: append to ## Sources section with what this source contributed
7. Update *Last Updated* date in article frontmatter
8. Report what was incorporated

**If kb_insights: false**: Skip this step for this file.

**If opinion doesn't fit existing categories**: Flag for user review - may need new KB article/category.

See "Opinion Extraction Details" section below for detailed guidance.

### Step 13: Report Progress
For each file: Original filename, new filename (if changed), destination path, frontmatter added, links created, kb_insights flag, QA result, opinion extraction (if done).

## Opinion Extraction Details

**⚠️ CRITICAL**: Opinion extraction happens in Step 12, immediately after processing each file with kb_insights: true.

**KB is DERIVED content**: Files never moved to KB. Extract USER OPINIONS FROM processed files, ADD/UPDATE KB documents. Source files stay in Archive/Projects/Planning. KB documents contain synthesized opinions.

### How to Get Opinion Mapping

**DO NOT use hardcoded mapping** - always read from KB README:

1. Read KB README: `obsidian read path="50-59 Knowledge Base/README.md"`
2. Extract the "Opinion Categories and Mapping" table
3. Use table to map opinions to KB articles

**Example mapping** (but ALWAYS read live version from README):
- Hiring opinions → `Hiring Principles and Philosophy.md`  
- AI platform opinions → `AI Platform Development Philosophy.md`
- Architecture opinions → `Architecture Principles and Anti-Patterns.md`
- Team strategy opinions → `Autonomous Teams Strategy.md`
- Management opinions → `Leadership and Management Philosophy.md`
- Product-Eng opinions → `Product-Engineering Collaboration.md`

**If opinion doesn't match existing categories**: Flag to user that a new KB article may be needed.

### KB Update Process

**For each opinion extracted**:
1. Read KB README for Article Structure template (use obsidian read)
2. Read existing KB article if it exists
3. **Extract USER'S OPINION** - not facts, look for "I think", "we should", "my view", principles, critiques
4. **Synthesize perspective** - distill the thinking, don't copy verbatim
5. Determine where opinion fits in existing article structure OR create new article using template
6. Use Edit tool for existing articles, Write tool for new articles
7. Preserve existing content, add to appropriate section
8. **ALWAYS update ## Sources section** - append: `- [[source-file|Description]] - Contributed thinking on [specific topic]`
9. Update *Last Updated: YYYY-MM-DD* at top of article
10. If thinking has changed/evolved, add entry to ## Evolution section

**Quality guidelines**:
- Extract **evident opinions** - detailed when clear, but don't extrapolate beyond what's stated
- If user says "I think X", extract it. Don't infer "user probably thinks Y"  
- Synthesize across multiple sources when updating (show patterns)
- Focus on the philosophy and "why", not just "what happened"
- Track evolution when opinions shift over time


### Quality Standards for KB
1. **Opinion-focused**: Capture USER'S thinking, not just facts
2. **Derived, not moved**: Extract from sources, never move files to KB
3. **Evolving with thinking**: Update as opinions develop, track changes in Evolution section
4. **Context for AI**: Write to help AI understand user's perspective and approach
5. **Context-rich**: Include "why" and philosophy, not just "what"
6. **Well-structured**: Follow KB Article Structure from README
7. **Source attribution**: Always list contributing files in Sources section
8. **Consolidated**: Update existing articles when possible, don't duplicate
9. **Synthesized**: Show patterns across multiple sources
10. **Evident opinions only**: Don't extrapolate beyond what's clearly stated

## Categorization Rules

**PRIMARY GUIDANCE**: Consult READMEs (Step 1.5) for categorization. READMEs contain purpose, inclusion/exclusion criteria, subcategories, guidelines, workflows.

**Decision Framework**:
1. Read file content
2. Analyze nature: active planning? completed meeting? project? historical?
3. Consult README "What Belongs Here"
4. Check README "What Does NOT Belong Here"
5. Verify subcategory structure
6. Choose destination per README guidance

**Primary Destinations** (see READMEs for full criteria):

| Content Type | Destination | Structure |
|--------------|-------------|-----------|
| Meeting notes | `60-69 Archive/61 Meeting Notes/` | `YYYY/QN/file.md` |
| Daily notes (old) | `60-69 Archive/62 Daily Notes/` | `YYYY/MM-Month/YYYY-MM-DD.md` |
| Transcripts | `60-69 Archive/63 Transcripts/` | `YYYY/QN/file-Transcript.md` |
| Correspondence | `60-69 Archive/64 Correspondence/` | `YYYY/file.md` |
| Projects | `20-29 Projects/[name]/` | Project folder |
| Planning | `10-19 Planning/[sub]/` | 11, 12, 13, or 14 subfolder |
| People | `40-49 People/[name]/` | Person folder |

**Key Rules** (details in READMEs):
- **Archive**: Meeting notes (immediate), daily notes (after month), transcripts, correspondence (after action items)
- **KB**: NOT a destination. Derived content only. Insights incorporated in Step 12.
- **Projects**: Time-bound initiatives with goals/completion criteria
- **Planning**: Active planning (11 Quarterly Planning, 13 Meeting Prep), rough ideas/drafts (12 Ideas and Drafts), correspondence being written (14 Draft Correspondence). If completed or >1 quarter old → Archive. Draft correspondence once sent → Inbox → Archive/64
- **People**: Reference materials only, NOT regular meeting notes

## Ground Rules

1. **PRESERVE CONTENT**: Never delete/modify author's words. Only ADD frontmatter/links. **Exceptions**: (a) Transcripts - replace with summary+link; (b) Minimal content files - ask user confirmation before deleting.

2. **MINIMAL CONTENT**: If file has only sentence fragment/placeholder, report to user, ask "Should I delete? (yes/no)", delete only after "yes".

3. **ASK WHEN AMBIGUOUS**: Use AskUserQuestion if categorization unclear after consulting READMEs. Don't guess.

4. **CONSULT READMEs**: Always reference category READMEs for categorization guidance.

5. **⚠️ PROCESS ONE FILE AT A TIME**: Complete ALL steps (2-13) for ONE file before starting the next file. Never batch process multiple files. Never run operations on multiple files in parallel. Sequential processing only. **EXCEPTION**: Never process today's daily note.

6. **USE OBSIDIAN CLI**: Always use `obsidian` commands, never direct file operations.

7. **AUTO-CREATE FOLDERS**: Create YYYY/QN/ and YYYY/MM-Month/ structures without asking.

8. **PROCESS ALL FILES**: Even if frontmatter exists, process for consistency.

9. **⚠️ OPINION EXTRACTION MANDATORY**: If file has kb_insights: true, extract user opinions in Step 12 immediately after processing that file. Not optional, not skippable.

10. **REPORT PROGRESS**: After each file, report what was done.

11. **HANDLE ERRORS**: If command fails, report error and continue.

## Execution Order

**CRITICAL: STRICT SEQUENTIAL PROCESSING**
- Process ONE file completely through Steps 2-13 before starting next file
- Never batch operations across multiple files
- Never run parallel operations on different files
- Complete file processing order: File 1 (all steps) → File 2 (all steps) → File 3 (all steps) → etc.

1. **One-time setup (Steps 1 and 1.5)**:
   - List all files
   - Read all category READMEs

2. **For EACH file, complete these steps IN ORDER before moving to next file**:
   - Step 2: Read file content
   - Step 3: Standardize filename immediately
   - Step 4: Analyze content (including transcript detection)
   - Step 4.5: Handle transcripts (if detected)
   - Step 5: Check for ambiguity (consult READMEs or ask user)
   - Step 6: Add/update frontmatter
   - Step 7: Add links within file
   - Step 8: Create destination folders
   - Step 9: Move to destination
   - Step 10: Update other files (if relevant)
   - **Step 11: QA check filename for THIS file**
   - **Step 12: Extract user opinions for KB for THIS file (if kb_insights: true)**
   - Step 13: Report progress for THIS file

3. **After ALL files processed**:
   - All done! Each file was QA checked and had user opinions extracted during processing.

## Start Processing

```bash
obsidian files folder="00 - Inbox" format=json
obsidian files folder="00 - Inbox/Daily Notes" format=json
```

**⚠️ CRITICAL PROCESSING ORDER**:
1. List all files (Step 1)
2. Read all READMEs (Step 1.5)
3. **Process File 1**: Complete Steps 2-13 (read, rename, analyze, add frontmatter, move, QA, opinion extraction if flagged, report)
4. **Process File 2**: Complete Steps 2-13 (read, rename, analyze, add frontmatter, move, QA, opinion extraction if flagged, report)
5. **Process File N**: Complete Steps 2-13 for each remaining file
6. **All done!** Each file was fully processed including QA and opinion extraction

**Never batch process. Never parallelize. One file fully processed (including QA and KB) before starting the next.**
