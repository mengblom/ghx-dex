# CJ Strategic Deliverables - Due Thursday 2026-05-08

**Context:** Follow-up meeting from Technical Priorities Review (2026-05-01)  
**Meeting Notes:** [[00-Inbox/Meetings/2026-05-01/Technical_Priorities_Review.md]]  
**Deadline:** Thursday, May 8, 2026 (30-minute review session)

---

## 🎯 Three Core Deliverables

### 1. Define 3-5 Specific "Breaking the Monolith" Deliverables

**Why this matters:**
> "Breaking the monolith" is #3 of Curtis's 5 technical priorities and THE MOST AMBIGUOUS. Risk of endless engineering without clear scope. How to ensure not underdoing or overdoing it?

**What CJ needs:**
- 3-5 **specific deliverables** (not vague statements)
- **Clear completion criteria** for each
- Black and white success metrics (like DB migration and DR goals)
- Scope boundaries to avoid "tech for tech's sake"

**Approach:**
1. Reference the work you've already done:
   - [[06-Resources/Architecture Principles and Anti-Patterns.md|Architecture Anti-Patterns doc]]
   - [[04-Projects/Exchange Platform Architecture/Architecture Picture/Architecture Flaws, Improvement Areas.md|Architecture Flaws]]
   - India trip pivot: Push teams to own their data and data stores

2. Define deliverables with DONE criteria:
   - Example: "Decouple SFTP endpoints from Audit DB dependency" → DONE = SFTP can process documents while Audit DB is down
   - Example: "Extract Document Enrichment service" → DONE = Can deploy enrichment changes without deploying monolith
   - Example: "Team-owned data stores for [X] domains" → DONE = 3 teams have independent databases with no shared schemas

3. Tie to business outcomes:
   - Faster deployment cycles (monthly → weekly?)
   - Reduced blast radius (% of system affected by average deployment)
   - Team autonomy metrics (can teams deploy independently?)

**Connection to Thinktiv/Kickdrum:**
Your Platform Architecture session will help validate these deliverables are realistic and scoped correctly.

---

### 2. Create Capacity Allocation Roadmap

**Why this matters:**
> "Even if you guys are not working on stability, there's nothing else for engineers to work on. There is no clear product direction." — Steve's assessment

**What CJ needs:**
- **Current state:** Pie chart showing 100% focus on stability (per Steve's direction)
- **Q3 projected:** How capacity shifts as stability work completes
- **Q4 projected:** Continuing progression toward product work
- Goal: Give Laura clarity to break down Steve's vision into engineering requirements

**Steve's vision:** Exchange should be ~100% self-service

**Approach:**
1. Current capacity breakdown:
   - Database migration %
   - DR maturity work %
   - Breaking the monolith %
   - Vulnerability remediation (Project Red Mythos) %
   - Product roadmap / new features %

2. Q3 allocation (assumptions):
   - DB migration completes → frees X%
   - DR goals met → frees Y%
   - Monolith first deliverable → enables Z% for product

3. Q4 allocation (target state):
   - Stability becomes BAU (maintenance level)
   - Product work increases to X%
   - Self-service enablement work at Y%

**Data sources:**
- Engineering timesheets or Jira time tracking
- Sprint planning commitments
- Team capacity in Aha/roadmap tool

---

### 3. Prepare 4-Month Productivity Assessment

**Why this matters:**
CJ needs **strong, clear, data-backed commentary** on productivity improvements since you joined (roughly January 2026).

**What CJ needs:**
- Not looking for all wins - **balanced view** of what's working vs challenges
- Executive-level, verifiable, data-backed insights
- Concise: "I'm not looking for pages" — executive summary format

**Approach:**

**A. Productivity Wins (with data):**
- [ ] AI Native SDLC adoption metrics (if available)
  - Teams using Cursor/Claude/GitHub Copilot
  - Code generation or time savings estimates
  - Developer sentiment on AI tooling
- [ ] SDLC improvements
  - Deployment frequency changes (before/after)
  - Lead time for changes
  - MTTR improvements
- [ ] Team autonomy improvements
  - Teams owning their deployment pipelines
  - Reduced cross-team coordination time
- [ ] Hiring velocity
  - 40+ open roles progress
  - Time-to-hire improvements

**B. Productivity Challenges (balanced):**
- [ ] Monolith deployment cycle still constrains velocity
- [ ] Testing framework (Tandoori) friction
- [ ] Manual testing still required due to coverage gaps
- [ ] Database dependencies blocking independent deployment

**C. In-Progress/Pipeline:**
- [ ] Breaking the monolith deliverables (from #1 above)
- [ ] Capacity shift toward product (from #2 above)
- [ ] Organizational maturity improvements

**Data sources:**
- KPMD dashboard (Mike Mitchell built it - tracks time-to-approve, targeting time-to-deploy)
- DORA metrics (if instrumented)
- Team surveys or retrospectives
- Hiring pipeline data
- Project Red Mythos vulnerability trend (declining?)

---

## 💡 Key Connections & Synergies

### Thinktiv/Kickdrum ↔ CJ Deliverables

**Breaking the Monolith** (CJ #1) overlaps with **Platform Architecture session**:
- Your prep with Daniel/Mike on Exchange architecture will inform realistic deliverables
- Database dependencies discussion feeds directly into "what to decouple first"
- Team boundaries (Mapping, IPA, Visibility, Doc Enrichment) inform service extraction strategy

**Capacity Roadmap** (CJ #2) informs **consultant engagement context**:
- Thinktiv/Kickdrum will ask about resourcing and priorities
- Your capacity allocation story explains why stability has been 100% focus
- Shows how technical debt remediation unlocks product velocity

**Productivity Assessment** (CJ #3) validates **organizational transformation**:
- Data on AI adoption, team autonomy, hiring supports your org strategy
- Balanced view (wins + challenges) shows you're not overselling
- Metrics framework (#4) becomes foundation for ongoing accountability

---

## 📋 Execution Plan

### Monday (2026-05-05):
- [ ] Book Daniel/Mike prep session for early in the week
- [ ] Gather data for productivity assessment (KPMD dashboard, DORA, hiring stats)
- [ ] Draft current capacity allocation (100% stability baseline)

### Tuesday-Wednesday:
- [ ] Daniel/Mike prep session → Extract architecture insights
- [ ] Use session to validate "breaking the monolith" deliverables
- [ ] Draft 3-5 monolith deliverables with completion criteria
- [ ] Search Confluence (using Rovo prompts) for existing architecture docs

### Wednesday-Thursday AM:
- [ ] Complete capacity roadmap (current/Q3/Q4 projections)
- [ ] Finish productivity assessment draft
- [ ] Review all three deliverables for coherence
- [ ] Prep talking points for CJ meeting

### Thursday (2026-05-08):
- [ ] 30-minute review session with CJ
- [ ] Present three deliverables
- [ ] Discuss metrics framework as next step

---

## 📊 Metrics Framework (Parallel Work - P2)

**For later, not due Thursday:**

**Mårten's accountability (10 metrics):**
- Stability metrics (uptime, MTTR, incident count)
- Quality metrics (defect escape rate, test coverage)
- Security metrics (vulnerability remediation time, security incidents)
- Tech debt metrics (% capacity on debt, debt trend)

**Laura's accountability (10 metrics):**
- Revenue growth
- Customer retention
- NPS
- Daily average usage
- (Others TBD)

**The partnership:** Both contribute to roadmap, but clear metric ownership.

**Key insight:**
> "If the site is down, I'm gonna call you, not Laura" — Mårten owns stability/quality/security outcomes

---

## 🎯 Success Criteria

**Thursday's meeting is successful if:**
1. CJ has radical clarity on "when are we done?" for breaking the monolith
2. CJ can articulate capacity shift story to Steve and Laura
3. CJ has data-backed productivity narrative for leadership discussions
4. You've demonstrated executive-level thinking with concise, verifiable deliverables

**Avoid:**
- Vague statements without completion criteria
- Tech for tech's sake without business outcomes
- Overly optimistic productivity claims without balanced challenges
- Pages of detail when CJ wants executive summary

---

## 🔗 Related Context

- **Curtis's 5 Technical Priorities** (slide incoming from Curtis)
- **Steve's Vision:** Exchange as ~100% self-service platform
- **Laura's Challenge:** Needs capacity clarity to translate vision into requirements
- **Current Reality:** Product measured on revenue, but Mårten accountable for stability/security
- **Interim Approach:** Sequester portion of capacity for technical work (~35% remains for product)

---

*Created: 2026-05-01*  
*Connection: Thinktiv/Kickdrum prep [[00-Inbox/Thinktiv_Kickdrum_Deep_Dive_Topics.md]]*
