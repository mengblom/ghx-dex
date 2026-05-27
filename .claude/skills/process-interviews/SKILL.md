---
name: process-interviews
description: Process candidate interviews by extracting Q&A, scoring against role criteria, and analyzing resume vs. interview performance
model_hint: balanced
context: fork
---

# Process Interviews

Transform raw interview notes with Granola transcripts into polished candidate assessment documents. Extracts Q&A, scores against role-specific criteria, and generates explicit resume vs. interview comparison analysis.

## What It Does

Creates four documents for each candidate interview:

1. **Interview Questions** - Q&A extraction with red flags from transcript
2. **Interview Scorecard** - Scored evaluation against role criteria with resume vs. interview comparison
3. **Resume** - Parsed resume with observations section highlighting disconnects
4. **Original Interview File** - Moves raw notes and transcript from 00-Inbox/ to candidate folder

**Key Innovation:** Explicitly compares resume evidence vs. interview performance to identify critical disconnects (e.g., resume shows recent AWS certifications but candidate says "I haven't done a lot" of managed services).

## Usage

**Required Arguments:**
- `"Candidate Name"` OR `--file "path/to/interview.md"` - Which interview to process
- `"Role Folder Path"` - Which role this interview is for (relative or full path)

**Examples:**
```bash
# Using candidate name + role folder
/process-interviews "Richard P. Monson" "13 - Principal Engineer - Data Architecture and Engineering"

# Using full role path
/process-interviews "Jane Doe" "04-Projects/21 Recruiting/Roles/12 - Engineering Manager"

# Using specific interview file
/process-interviews --file "00-Inbox/2026-05-18 12.00 Interview - Richard P. Monson.md" "13 - Principal Engineer - Data Architecture and Engineering"

# Get help (lists available roles)
/process-interviews --help
```

---

## Step 0: Parse and Validate Arguments

### Parse Arguments

Extract two required arguments from user input:

1. **Interview identifier:** Candidate name OR `--file` flag with path
2. **Role folder path:** Relative folder name OR full path

**If `--help` flag detected:**
```markdown
# Process Interviews - Usage

**Required Arguments:**
  /process-interviews "Candidate Name" "Role Folder Path"
  /process-interviews --file "interview.md" "Role Folder Path"

**Available roles in 04-Projects/21 Recruiting/Roles/:**
[List all folder names in recruiting roles directory]

**Examples:**
  /process-interviews "Richard P. Monson" "13 - Principal Engineer - Data Architecture"
  /process-interviews --file "00-Inbox/interview.md" "13 - Principal Engineer - Data Architecture"
```
Exit after showing help.

**If missing arguments (less than 2 arguments provided):**
```markdown
❌ Missing required arguments

**Usage:**
  /process-interviews "Candidate Name" "Role Folder Path"
  /process-interviews --file "interview.md" "Role Folder Path"

**Available roles:**
[List folders in 04-Projects/21 Recruiting/Roles/]

**Example:**
  /process-interviews "Jane Doe" "12 - Engineering Manager"
```
Exit after showing error.

---

## Step 1: Locate Interview File

### If `--file` flag provided:
Use the provided path directly. Verify file exists:
```bash
test -f "[provided-path]" || echo "ERROR: File not found"
```

### If candidate name provided:
Search for interview file in `00-Inbox/`:

```bash
# Search for interview matching candidate name (last 30 days)
find 00-Inbox -name "*Interview*" -name "*${CANDIDATE_NAME}*.md" -type f -mtime -30
```

**Fuzzy name matching:**
- Try full name first: `*Interview*Richard P. Monson*.md`
- Try last name only: `*Interview*Monson*.md`  
- Try last two names: `*Interview*P. Monson*.md`

**If no matches found:**
```markdown
❌ No interview file found for "[Candidate Name]"

**Searched:** 00-Inbox/*Interview*[Name]*.md (last 30 days)

**Options:**
1. Use --file flag with exact path: `/process-interviews --file "path/to/interview.md" "Role Folder"`
2. Check filename matches pattern: `YYYY-MM-DD HH.MM Interview - Name for Role.md`
3. Verify file is in 00-Inbox/ directory
```
Exit after showing error.

**If multiple matches:**
```markdown
⚠️ Multiple interview files found for "[Candidate Name]":

1. 00-Inbox/2026-05-18 12.00 Interview - Richard P. Monson for Principal Engineer.md (May 18)
2. 00-Inbox/2026-05-10 14.30 Interview - Richard P. Monson for Technical Screen.md (May 10)

Which interview should I process? [1-2]:
```
Wait for user response, then use selected file.

---

## Step 2: Validate Role Folder

### Expand role folder path:

**If relative path provided** (e.g., "13 - Principal Engineer"):
```bash
# Search in recruiting roles directory
find "04-Projects/21 Recruiting/Roles" -type d -name "*${ROLE_PATH}*" | head -1
```

**If full path provided:**
Use directly and verify it exists.

**If role folder not found:**
```markdown
⚠️ Role folder not found: "[Role Path]"

**Available roles in 04-Projects/21 Recruiting/Roles/:**
[List all folders with numbers]

**Options:**
1. Use folder name: `/process-interviews "[Name]" "13 - Principal Engineer - Data Architecture"`
2. Use full path: `/process-interviews "[Name]" "04-Projects/21 Recruiting/Roles/13 - Principal Engineer..."`

Which role should I use? [Enter folder name or path]:
```
Wait for user response, then use provided path.

### Verify required template files exist:

Check for:
- `{Role Folder}/*Job Description*.md`
- `{Role Folder}/*Scorecard*.md`

**If scorecard template missing:**
```markdown
⚠️ No scorecard template found in role folder

**Found:** Job Description ✓
**Missing:** Scorecard Template ✗

Without a scorecard template, I can only generate:
- Interview Questions (Q&A extraction from transcript)
- Resume (if found)

**Cannot generate:** Interview Scorecard (requires template)

Continue without scorecard? [y/n]:
```
If user says no, exit. If yes, proceed without scorecard generation.

---

## Step 3: Extract Interview Metadata

Read the interview file and extract metadata from filename and content.

### From filename pattern:
Expected: `YYYY-MM-DD HH.MM Interview - [Candidate Name] for [Role Title].md`

Extract:
- **Date:** `2026-05-18`
- **Time:** `12:00` (convert HH.MM to HH:MM)
- **Candidate name:** `Richard P. Monson`
- **Role title:** `Principal Software Engineer, Data Architecture and Engineering`

**If filename doesn't match pattern:**
Try to extract what's possible, then:
```markdown
⚠️ Filename doesn't match expected pattern

Expected: YYYY-MM-DD HH.MM Interview - [Name] for [Role].md
Found: [actual filename]

Extracted:
- Date: [date or "unknown"]
- Candidate: [name or "unknown"]
- Role: [role or "unknown"]

Continue with extracted information? [y/n]:
```

### Get interviewer name:
Read `System/user-profile.yaml` → extract `name` field for interviewer attribution.

### Determine interview stage:
- Check filename for keywords: "HM Screen", "Technical", "Panel", "Final"
- Check frontmatter if present: `stage: [value]`
- Default to "hm-screen" if not specified

---

## Step 4: Parse Interview File Structure

Read interview file and split into sections.

### Expected structure:
```markdown
### My Notes ###
[Interviewer's raw notes, red flags, impressions]

### Transcript from Granola ###
Me: [questions]
Them: [answers]
```

### Parsing logic:

1. **Find transcript section:**
   - Search for headings: `### Transcript from Granola ###`, `## Transcript`, `### Transcript:`
   - Split file into two parts: before transcript (notes) and after transcript (conversation)

2. **Extract interviewer notes:**
   - Everything before transcript heading
   - Remove heading markers
   - Preserve bullet points and formatting
   - This contains red flags and overall impressions

3. **Extract transcript:**
   - Everything after transcript heading
   - Preserve speaker labels (`Me:`, `Them:`)
   - Keep full conversation intact for Q&A extraction

**If no clear transcript section:**
```markdown
⚠️ Could not identify transcript section in interview file

Expected: Section heading like "### Transcript from Granola ###"

**File structure found:**
[Show headings detected in file]

**Options:**
1. Manually specify transcript start line number
2. Process entire file as transcript (no separate notes section)
3. Cancel processing

Choice [1-3]:
```

---

## Step 5: Find and Parse Resume

Search for candidate's resume in multiple locations.

### Search order:

**1. Downloads folder** (last 30 days, most recent first):
```bash
# Extract last name from candidate name
LAST_NAME=$(echo "$CANDIDATE_NAME" | awk '{print $NF}')

# Search with progressively broader patterns
find ~/Downloads -name "*${CANDIDATE_NAME}*.pdf" -mtime -30 -type f | xargs ls -t | head -1
find ~/Downloads -name "*${LAST_NAME}*Resume*.pdf" -mtime -30 -type f | xargs ls -t | head -1
find ~/Downloads -name "*${LAST_NAME}*.pdf" -mtime -30 -type f | xargs ls -t | head -1
```

**2. Inbox folder:**
```bash
find 00-Inbox -name "*${CANDIDATE_NAME}*.pdf" -type f | xargs ls -t | head -1
find 00-Inbox -name "*${LAST_NAME}*Resume*.pdf" -type f | xargs ls -t | head -1
```

**3. Role Interviews folder:**
```bash
find "{Role Folder}/Interviews" -name "*${CANDIDATE_NAME}*.pdf" -type f | head -1
```

**If multiple resume files found with similar scores:**
```markdown
⚠️ Multiple resume files found for [Candidate Name]:

1. ~/Downloads/Richard Monson - Resume.pdf (May 18, 2.2 MB)
2. ~/Downloads/R Monson Resume 2026.pdf (May 15, 1.8 MB)

Which resume should I use? [1-2]:
```

**If no resume found:**
```markdown
⚠️ Resume not found for [Candidate Name]

**Searched:**
- ~/Downloads/*[Name]*.pdf (last 30 days)
- 00-Inbox/*[Name]*.pdf
- {Role Folder}/Interviews/*[Name]*.pdf

**Options:**
1. Provide path to resume PDF: [enter path]
2. Continue without resume (will create placeholder Resume file)
3. Skip resume file entirely (only Q&A + Scorecard)

Choice [1-3]:
```
Handle user response.

### Parse resume PDF:

Use the Read tool to extract text from PDF:
```
Read the PDF at [resume-path]
```

Extract and preserve:
- Contact information (email, phone, LinkedIn, location)
- Summary/Profile section
- Certifications & Professional Development
- Technical Profile/Skills
- Work Experience (full preservation with dates, titles, accomplishments)
- Education
- Patents/Publications (if present)

**If PDF parsing fails:**
```markdown
❌ Could not parse resume PDF: [filename]

Error: [specific error message]

**Options:**
1. Try different resume file
2. Continue without resume (placeholder created)
3. Cancel processing

Choice [1-3]:
```

---

## Step 6: Extract Q&A from Transcript

Process the transcript section to generate structured Q&A document.

### Identify Q&A pairs:

1. **Find conversation pattern:**
   - Look for `Me:` followed by `Them:`
   - Group consecutive speaker turns (handle interruptions)
   - Track which topic each exchange relates to

2. **Topic detection:**
   - Analyze first few questions to identify topic areas
   - Common topics: Career Overview, Technical Skills, Data Products, Technology Selection, Red Flags
   - Create sections for each major topic area

3. **Summarize questions:**
   - Extract the essence of what was asked
   - Remove conversational artifacts ("um", "uh", "you know", false starts)
   - Format as clear, professional question
   - Keep technical terminology intact

4. **Summarize answers:**
   - Extract key points from candidate's response
   - **Preserve technical details** and specific examples (dates, technologies, metrics)
   - Note when answers go off-topic or are vague
   - Flag tangential responses
   - Capture specific quotes when important

5. **Extract red flags:**
   - Pull concerns from interviewer notes section
   - Note specific quotes that raised concerns
   - Flag: tangential responses, outdated knowledge, communication issues, incorrect terminology
   - Group by category (Communication Issues, Technical Gaps, Experience Concerns, etc.)

### Output structure:

```markdown
## [Topic Area 1 - e.g., Career Overview]

**Q: [Summarized question]**

**A:** [Key points from answer. Preserve technical details like "Spring Data JDBC optimization at US Bank (2022-2025)" or "MongoDB ~10 years ago". Note when answers are vague or go off-topic.]

---

## [Topic Area 2 - e.g., Data Products & Technologies]

**Q: [Question]**

**A:** [Answer]

---

## Red Flags / Concerns

1. **[Category - e.g., Outdated Experience]:**
   - [Specific issue with supporting quote]
   - [Another specific issue]

2. **[Another Category - e.g., Communication Issues]:**
   - [Issue with example]

---

## Closing Questions

**Q: Any questions for me?**

**A:** [What candidate asked about]

---

## Interviewer Notes

**Overall Impression:** [Pull from "My Notes" section - raw interviewer assessment]
```

**Quality standards:**
- Be thorough but concise
- Preserve technical accuracy
- Don't editorialize - report what was said
- Flag concerning patterns without judgment
- Use actual quotes when impactful

---

## Step 7: Score Against Scorecard Template

**Skip this step if no scorecard template was found.**

Read the scorecard template and extract all evaluation criteria.

### Parse scorecard template:

Look for these sections (typical structure):
- `## Skills` or `## Skills Assessment`
- `## Personality Traits`
- `## Qualifications` or `## Qualifications Assessment`
- `## Other/Details`

For each section, extract the list of criteria. Common formats:
- Markdown list: `- Deep hands-on experience with...`
- Table rows
- Numbered items

### For each criterion:

**1. Search resume for evidence:**
- Look for keywords related to the skill (e.g., "PostgreSQL", "AWS", "event-driven", "Kafka")
- Check work experience dates for recency
- Note certifications, specific projects, quantitative evidence
- Extract relevant quotes: `"Resume: Spring Data JDBC optimization at US Bank (2022-2025)"`

**2. Search interview Q&A for evidence:**
- Check if skill was discussed in transcript
- Note depth of discussion: surface-level vs. detailed examples
- Check for specificity: concrete examples vs. vague generalities
- Extract relevant quotes: `"Interview: Mentioned this story but explanation lacked detail"`
- Mark as "Not discussed" if skill wasn't covered

**3. Compare resume vs. interview:**
- **Key feature:** Explicitly identify disconnects
- Flag when resume shows experience but interview doesn't mention it
- Flag when interview contradicts resume
- Note credibility concerns when major accomplishments aren't discussed
- Example: `Resume: 5 AWS certs (Dec 2025-Mar 2026) | Interview: Said "I haven't done a lot" of managed services **MAJOR DISCONNECT**`

**4. Assign score (1-5 scale or N/A):**

**CRITICAL RULE: Never hallucinate scores or evidence. When in doubt, use N/A.**

- **5 (Strong Yes):** Strong, clear evidence in both resume AND interview. Demonstrated depth.
- **4 (Yes):** Good evidence from both sources, may be slightly stronger in one. Minor gaps acceptable.
- **3 (Mixed):** Some evidence but concerns OR conflicting signals OR resume-interview disconnect.
- **2 (No):** Weak evidence OR significant disconnect between resume and interview.
- **1 (Definitely Not):** No meaningful evidence OR disqualifying concerns.
- **N/A:** Insufficient signal to evaluate. Not discussed or mentioned.

**Prefer N/A over guessing.** Better to have many N/As than fabricated evidence.

### Generate scorecard tables:

**Skills Assessment table:**
```markdown
| Skill | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Deep hands-on experience with relational databases | 2 | Resume: Spring Data JDBC at US Bank (2022-2025) | Interview: Only mentioned 10-year-old Logi Analytics work, couldn't articulate recent work |
| Deep expertise in NoSQL databases | 1 | Resume: No MongoDB/NoSQL mentioned | Interview: Claims MongoDB ~10 years ago, no recent knowledge |
```

**Call out critical disconnects prominently:**
```markdown
**Critical Disconnect:** Resume shows recent, relevant experience (US Bank 2022-2025: Kafka, Spring Boot, event-driven architecture, microservices) and very recent AWS certifications (2025-2026), but candidate **could not articulate any of this** in the interview. Spent most time on 10+ year old Logi Analytics work instead.
```

**Write Skills Summary** (2-3 paragraphs):
- Overall technical assessment
- Key strengths (if any)
- Key gaps
- **Emphasize disconnects** - this is the most valuable insight
- Assessment of whether disconnect indicates: (A) can't communicate own work, (B) resume overstates involvement, or (C) wasn't paying attention

**Repeat for other sections:**
- Personality Traits Assessment (table + summary)
- Qualifications Assessment (table + summary)
- Other/Details (table if criteria exist)

---

## Step 8: Generate Overall Assessment

Create the comprehensive evaluation section.

### Components:

**1. Key Concerns (numbered list):**

Prioritize the most critical issues. Number them (1, 2, 3...) with **bold headings**.

For each concern:
- State the issue clearly
- Provide specific evidence (quotes, examples)
- Explain impact on role fit

Example:
```markdown
**Key Concerns:**

1. **Cannot effectively communicate own experience:**
   - Resume shows US Bank work (2022-2025) with Kafka, event-driven architecture, Spring Boot
   - In interview, spent most time on 10+ year old Logi Analytics work instead
   - Never mentioned Kafka despite being primary resume accomplishment
   - When asked about managed services, said "I haven't done a lot" despite 5 AWS certifications earned Dec 2025-Mar 2026

2. **Critical for Principal role: Position requires enabling application teams:**
   - If candidate cannot clearly explain their own recent work, they cannot enable teams
   - Goes on tangents constantly - shows inability to tailor message to audience
   - Uses incorrect terminology ("Azure Tables") despite certifications
```

**2. Key Strengths:**

Be honest. If there aren't many strengths, say so clearly.
- List genuine positives from interview or resume
- Don't manufacture strengths to be nice
- It's okay to say "None identified from this interview" if true

**3. Fit for Role Score (1-5):**

Single score based on overall assessment:
- 5 = Strong Yes (excellent fit, advance immediately)
- 4 = Yes (good fit, advance)
- 3 = Mixed (concerns and strengths balanced)
- 2 = No (significant concerns, likely pass)
- 1 = Definitely Not (clear pass, do not advance)

**4. Reasoning (2-4 paragraphs):**

Write clear recommendation connecting assessment to role requirements:
- Address the "hire or pass" decision directly
- Connect to specific role requirements
- For passes: be clear about why this is disqualifying
- For advances: be clear about strengths that make them a fit
- If there's a critical concern, emphasize it: "**Most concerning:** [issue]"

**5. Recommendation checkbox:**

```markdown
**Recommendation:** ☒ Do Not Advance

or

**Recommendation:** ☑ Advance
```

**6. Feedback to Agency (if passing on candidate):**

Provide constructive feedback explaining:
- What went wrong with the match
- What skills/experience were missing
- What to look for in future candidates
- Be professional but direct

Example:
```markdown
**Feedback to Agency:**

Critical issue: **Resume-interview disconnect.** Candidate's resume shows relevant recent experience (US Bank 2022-2025: Kafka, event-driven architecture, Spring Boot) and recent AWS certifications (Dec 2025-Mar 2026), but **could not articulate any of this** in the interview.

**What we need:**
- Candidates who can clearly communicate technical concepts (this is a teaching/enabling role)
- Strong application development background (embedded with app teams, not isolated)
- Modern data architecture experience they can **articulate clearly**
- Demonstrated collaboration and listening skills

**Please recalibrate:** "Principal Data Architect for application teams" means working side-by-side with engineers. Communication ability is as important as technical depth.
```

---

## Step 9: Create Candidate Folder Structure

Prepare the output directory and files.

### Check if folder exists:

```bash
CANDIDATE_FOLDER="{Role Folder}/Interviews/{Candidate Name}"
test -d "$CANDIDATE_FOLDER"
```

**If folder already exists:**
```markdown
⚠️ Candidate folder already exists:
{Role Folder}/Interviews/{Candidate Name}/

**Existing files:**
- Interview Questions - {Name}.md (modified [date])
- Interview Scorecard - {Name}.md (modified [date])
- Resume - {Name}.md (modified [date])

This appears to be a previously processed interview.

**Options:**
1. Overwrite existing files (previous files backed up with .backup extension)
2. Create new dated folder: "{Name} (2026-05-18)"
3. Cancel processing

Choice [1-3]:
```

Handle user choice:
- Option 1: Rename existing files with `.backup` extension, proceed with creation
- Option 2: Create new folder with date suffix, proceed
- Option 3: Exit

**If folder doesn't exist:**
```bash
mkdir -p "$CANDIDATE_FOLDER"
```

### Determine file tags:

Extract from scorecard template or job description:
- `role-level`: principal-engineer, staff-engineer, engineering-manager, etc.
- `role-domain`: data-architecture, platform-engineering, frontend, backend, etc.

Fallback: Use folder name patterns to infer tags.

### Prepare frontmatter for all files:

```yaml
---
tags:
  - [file-type: interview-questions/interview-scorecard/resume]
  - [role-level from template]
  - [role-domain from template]
candidate: [Full Name]
date: [YYYY-MM-DD from filename]
interviewer: [From System/user-profile.yaml name field]
stage: [hm-screen / technical / panel / final]
---
```

For resume file, add:
```yaml
location: [Extract from resume if available]
```

---

## Step 10: Generate and Write Files

Create the three output files with all extracted and analyzed content.

### File 1: Interview Questions

**Filename:** `Interview Questions - {Candidate Name}.md`

**Content structure:**
```markdown
---
[frontmatter from Step 9]
---

# Interview Questions: [Candidate Name]
**Role:** [Full Role Title]
**Date:** [YYYY-MM-DD]
**Interviewer:** [Name]
**Stage:** [HM Screen (30 min) / Technical Interview / etc.]

---

[Q&A sections from Step 6]

## [Topic Area 1]
**Q: [Question]**
**A:** [Answer]

## [Topic Area 2]
...

## Red Flags / Concerns
1. **[Category]:** [Issues]

## Closing Questions
**Q: Any questions for me?**
**A:** [What they asked]

## Interviewer Notes
**Overall Impression:** [From interviewer notes section]
```

Write this file using the Write tool.

### File 2: Interview Scorecard

**Filename:** `Interview Scorecard - {Candidate Name}.md`

**Content structure:**
```markdown
---
[frontmatter from Step 9]
---

# Interview Scorecard: [Candidate Name]
**Role:** [Full Role Title]
**Date:** [YYYY-MM-DD]
**Stage:** [Stage]

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

[Table from Step 7 with Resume Evidence | Interview Evidence columns]

**Critical Disconnect:** [If major disconnect exists]

**Skills Summary:** [2-3 paragraphs from Step 7]

---

## Personality Traits Assessment

[Table from Step 7]

**Personality Traits Summary:** [Assessment paragraph]

---

## Qualifications Assessment

[Table from Step 7]

**Qualifications Summary:** [Assessment paragraph]

---

## Other/Details

[Table from Step 7 if criteria exist]

---

## Overall Assessment

[Full content from Step 8]

**Key Concerns:**
1. **[Concern]**
   - [Evidence]

**Key Strengths:**
- [Strengths or "None identified"]

**Fit for Role:** [1-5] ([Rating Text])

**Reasoning:**
[2-4 paragraphs]

**Recommendation:** ☐ Do Not Advance / ☑ Advance

**Feedback to Agency:** [If passing]

---

## Interview Notes

**Interviewer's raw notes:**
[From "My Notes" section of interview file]

**Key moments that led to decision:**
[Specific quotes/exchanges with brief context]
```

Write this file using the Write tool.

### File 3: Resume

**Filename:** `Resume - {Candidate Name}.md`

**Content structure:**
```markdown
---
[frontmatter from Step 9 including location if available]
---

# Resume: [Candidate Name]

**Contact:**
- Email: [email]
- Phone: [phone]
- LinkedIn: [URL]
- Location: [location]

---

[Full resume content parsed from PDF, preserving all structure]

## Summary
[Resume summary/profile]

## Certifications & Professional Development
[If present]

## Technical Profile
[Skills, languages, frameworks]

## Work Experience

### [COMPANY NAME]
**[Title]** | [Dates]

- [Accomplishment bullets - preserve all]

[Repeat for all positions]

---

## Education
[Degrees, institutions, dates]

---

## Patents / Publications
[If present]

---

## Resume vs. Interview Observations

**Strengths on Resume:**
- [Notable positives from resume]
- [Recent relevant experience with dates]
- [Certifications, patents, achievements]

**Major Disconnects in Interview:**
- [Resume shows X but interview focused on Y instead]
- [Resume claims recent work but candidate spent time on old work]
- [Claimed Z on resume but said "haven't done much" in interview]
- [Used outdated terminology despite recent certifications]
- [Never mentioned primary accomplishment despite being asked about career]

**Assessment:** [2-3 paragraph summary of whether resume aligns with interview performance. Note credibility concerns if disconnect is significant. This is the KEY value-add of this skill - explicit comparison analysis that highlights when candidates can't articulate their own experience.]
```

**If resume was not found:**
Create placeholder:
```markdown
---
[frontmatter]
---

# Resume: [Candidate Name]

**Status:** Resume not provided with interview materials.

**To add resume:**
1. Obtain resume PDF from candidate or recruiting agency
2. Replace this file content with parsed resume
3. Add "Resume vs. Interview Observations" section

**Candidate mentioned during interview:**
[Any resume-related details from interview - certifications, companies, roles]
```

Write this file using the Write tool.

### File 4: Move Original Interview File

**Filename:** Keep original filename

**Action:** Move the original interview file from `00-Inbox/` to the candidate folder.

```bash
# Move original interview file to candidate folder
mv "[original-interview-path]" "{Candidate Folder}/[original-filename]"
```

**Purpose:**
- Keeps all candidate materials together in one location
- Clears processed interviews from inbox
- Preserves the raw data (interviewer notes + transcript) for future reference

**If move fails (permission issues, cross-device, etc.):**
- Fall back to copy + delete: `cp "[source]" "[dest]" && rm "[source]"`
- If that also fails, leave in place and note in summary: "⚠️ Original interview file left in 00-Inbox/ (move failed)"

---

## Step 11: Validation and Summary

Before finishing, validate the output and present summary to user.

### Validation checklist:

```markdown
✓ Interview file parsed successfully
✓ Q&A extracted ([X] questions identified)
✓ Red flags noted ([Y] concerns flagged)
✓ Role templates located (Job Description + Scorecard)
✓ Resume found and parsed ([filename] - [size])
✓ Scorecard completed ([N]/[M] criteria scored, [P] marked N/A)
✓ Resume vs. interview comparison included
✓ Critical disconnects highlighted
✓ Overall recommendation clear ([Advance / Do Not Advance])
✓ Files created in correct location
✓ Original interview file moved to candidate folder
```

### Summary report:

```markdown
## Interview Processing Complete ✅

**Candidate:** [Candidate Name]
**Role:** [Full Role Title]
**Date:** [YYYY-MM-DD]

### Files Created:

1. **Interview Questions - [Name].md**
   - [X] questions extracted
   - [Y] red flags identified
   - Interviewer notes included

2. **Interview Scorecard - [Name].md**
   - [N]/[M] criteria scored ([P] N/A)
   - Resume vs. interview comparison table
   - Overall score: [1-5] ([Rating])
   - Recommendation: [Advance / Do Not Advance]

3. **Resume - [Name].md**
   - Full resume parsed ([X] pages)
   - Resume vs. Interview Observations section
   - [Major disconnects highlighted / No significant disconnects found]

4. **[Original Interview Filename].md** (moved from 00-Inbox/)
   - Raw interview notes and transcript
   - Preserved for reference

**Location:** `{Role Folder}/Interviews/{Candidate Name}/`

---

### Assessment Summary

**Overall Score:** [1-5]/5 ([Rating Text])

**Recommendation:** [☑ Advance / ☒ Do Not Advance]

**Key Finding:** [One-line critical insight - especially if major disconnect exists]

**Critical Disconnect (if any):** [Brief description of most significant resume-interview mismatch]

---

**Next Steps:**
- Review generated scorecard: [link to file]
[If pass:] - Send feedback to agency (see "Feedback to Agency" section in scorecard)
[If advance:] - Schedule next interview round
```

---

## Step 12: Track Usage (Silent)

Update usage log to track feature adoption.

Read `System/usage_log.md` and find the recruiting workflows section.

**If section doesn't exist, create it:**
```markdown
## Recruiting Workflows (3 features)

- [x] Interview processed (`/process-interviews`)
- [x] Candidate folder created
- [x] Resume vs. interview analysis generated
```

**If section exists:**
Update checkboxes to mark features as used:
- `- [ ] Interview processed` → `- [x] Interview processed`
- `- [ ] Candidate folder created` → `- [x] Candidate folder created`
- `- [ ] Resume vs. interview analysis generated` → `- [x] Resume vs. interview analysis generated`

**Do not announce this update to the user** - it's silent tracking for `/dex-level-up`.

---

## Error Handling

### Missing Arguments
Already handled in Step 0.

### Interview File Not Found
Already handled in Step 1.

### Role Folder Not Found
Already handled in Step 2.

### Scorecard Template Missing
Already handled in Step 2 - offer to continue without scorecard (Q&A + Resume only).

### Resume Not Found
Already handled in Step 5 - offer options (provide path / continue without / skip resume).

### Transcript Parsing Failure

**If cannot identify transcript structure:**
```markdown
⚠️ Could not parse interview file structure

Expected clear sections like:
- "### My Notes ###" or "## Interviewer Notes"
- "### Transcript from Granola ###" or "## Transcript"

**File structure found:**
[List headings detected]

**Options:**
1. Process entire file as transcript (assume all content is Q&A)
2. Manually specify line number where transcript starts: [enter number]
3. Cancel processing

Choice [1-3]:
```

### PDF Parsing Failure
Already handled in Step 5.

### Write Failures

**If cannot create files:**
```markdown
❌ Error writing files to disk

Error: [specific error message]

**Possible causes:**
- Insufficient permissions for directory
- Disk space issues
- File path too long

**Attempted location:** {Role Folder}/Interviews/{Candidate Name}/

Try:
1. Check directory permissions
2. Verify disk space available
3. Try shorter candidate name or different role folder

Cancel processing? [y/n]:
```

---

## Quality Standards

**Before writing files, ensure:**

1. ✓ **No hallucinated scores** - All scores based on actual evidence or marked N/A
2. ✓ **Disconnects explicitly called out** - Resume-interview mismatches prominently highlighted
3. ✓ **Technical details preserved** - Dates, technologies, metrics from both resume and interview
4. ✓ **Clear recommendation** - Unambiguous Advance/Do Not Advance with rationale
5. ✓ **Agency feedback included** - If passing, constructive feedback on mismatch
6. ✓ **Complete file structure** - All three files with proper frontmatter
7. ✓ **Observations section** - Resume file includes comparison analysis

**The most valuable output:** Explicit resume vs. interview comparison that identifies when candidates cannot articulate their own claimed experience.

---

## Examples

### Example 1: Strong Disconnect (Pass Recommendation)

**Scenario:** Resume shows recent experience and certifications, but candidate couldn't discuss any of it.

**Resume Evidence:** 
- US Bank VP Principal Engineer (2022-2025)
- Kafka, event-driven microservices, SAGA patterns
- 5 AWS certifications (Dec 2025-Mar 2026)

**Interview Performance:**
- When asked about career, focused on 10-year-old Logi Analytics work
- Said "I haven't done a lot" of managed services (contradicts certs)
- Never mentioned Kafka or event-driven work
- Used outdated terminology ("Azure Tables")

**Scorecard Output:**
```markdown
**Critical Disconnect:** Resume shows recent, relevant experience but candidate **could not articulate any of this** in the interview.

| Cloud data platform expertise | 1 | Resume: 5 AWS certs (Dec 2025-Mar 2026) | Interview: **MAJOR DISCONNECT** - said "I haven't done a lot" |

**Overall Score:** 1/5 (Definitely Not)
**Recommendation:** ☒ Do Not Advance

**Most concerning:** For Principal Engineer role requiring team enablement, inability to clearly communicate recent experience is disqualifying regardless of resume content.
```

### Example 2: Strong Alignment (Advance Recommendation)

**Scenario:** Resume and interview align, candidate demonstrates depth.

**Resume Evidence:**
- Senior Engineer at DataCo (2020-2026)
- PostgreSQL, MongoDB, Snowflake expertise
- Led 3 zero-downtime migrations

**Interview Performance:**
- Discussed recent PostgreSQL optimization work with specific examples
- Explained migration strategy with technical details
- Mentioned Snowflake cost optimization with metrics
- Clear communication, adapted explanations appropriately

**Scorecard Output:**
```markdown
| Database performance optimization | 5 | Resume: "Reduced query latency 40%" | Interview: Detailed explanation of indexing strategy, execution plan analysis, specific examples from last 6 months |

**Overall Score:** 4/5 (Yes)
**Recommendation:** ☑ Advance

**Key Strengths:** Strong technical depth demonstrated in both resume and interview. Clear communication, specific examples, recent hands-on work. Resume and interview performance align well.
```

### Example 3: Resume Not Found

**Scenario:** Cannot locate resume, proceeding with Q&A + Scorecard only.

**Files Created:**
1. Interview Questions - Full Q&A extraction
2. Interview Scorecard - Scored based on interview only (Resume Evidence column shows "Resume not provided")
3. Resume - Placeholder file with note

**Resume File Content:**
```markdown
# Resume: Jane Doe

**Status:** Resume not provided with interview materials.

**Candidate mentioned during interview:**
- 8 years of experience in data engineering
- Previous companies: TechCorp, DataSystems Inc.
- Mentioned AWS Solutions Architect certification

**To complete assessment:** Obtain resume from recruiting agency.
```

---

## Notes

- **Resume comparison is the differentiator** - This skill's key innovation is explicitly comparing resume vs. interview, which catches credibility issues that manual review might miss
- **Never hallucinate** - Better to mark N/A than fabricate evidence
- **Be thorough but concise** - Preserve important details, eliminate fluff
- **Professional tone** - Even for passes, feedback should be constructive and professional
- **Trust the disconnect** - If resume and interview don't align, that IS the signal - highlight it prominently
