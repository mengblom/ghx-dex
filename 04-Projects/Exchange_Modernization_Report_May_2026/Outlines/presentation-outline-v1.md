# CJ Strategic Update - Presentation Outline

**File:** `CJ-Strategic-Update.pptx`  
**Purpose:** Brief CJ before CJ→Steve Jackson (CPO) discussion  
**Date:** 2026-05-08

---

## SLIDE 1: Executive Summary

**Layout:** Three-column layout with header

**Header:** Executive Summary

**Column 1: Productivity**
- **Heading:** Productivity
- **Subhead:** Measurable improvement, structural ceiling remains
- Stories completed up 86% (207→386)
- Cycle time down 48% (44→23 days)
- Gains are incremental until monolith + org structure changes complete

**Column 2: Resiliency Endgame**
- **Heading:** Resiliency - "When are we done?"
- **Subhead:** 2 Must-Do
- 12 autonomous teams deploying independently (70% org work done)
- Data layer modernization (MongoDB → purpose-built stores)

**Column 3: Capacity Forecast**
- **Heading:** Capacity Forecast
- **Subhead:** Shift from reactive to strategic
- Q2: 60% firefighting / 40% strategic
- Q4: 30% firefighting / 70% strategic

**Talking Points:**
- "This is the soundbite version. Three questions, three answers."
- "Key insight: Productivity gains are real but incremental. Structural changes unlock exponential gains."
- "Resiliency 'done' = these two things. Everything else is negotiable."
- **If Steve asks:** "When are we done?" → Point to the two criteria with current progress %

---

## SLIDE 2: Productivity - The Data

**Layout:** Two-column (left: text, right: chart)

**Header:** Productivity - The Data

**Left Column:**
**Heading:** 4-Month Trends (Jan → Mar)

**Metrics:**
- Stories Completed: 207 → 271 → 386 (+86%)
- Lead Time to Change: 30 → 33 → 8 days (-73%)
- Cycle Time: 44 → 44 → 23 days (-48%)

**Also:**
- Last 3 releases clean (no major incidents)
- AI library launched (Claude Code adoption growing)
- Exchange Health Score beta (leading indicator dashboard)

**Right Column:**
**Chart:** Grouped bar chart showing three metrics (Stories Completed, Lead Time, Cycle Time) across Jan/Feb/Mar. Left vertical axes showing number of stories for Stories Completed (0-400), Right vertical axes showing Days (0 - 50) for Lead Time and Cycle TIme

**Talking Points:**
- "4-month trend is positive. We're completing more, faster."
- "Lead time drop (33→8 days) is the most telling — we're deciding faster."
- "But notice: Feb→Mar jump is bigger than Jan→Feb. Why? Org changes starting to land."
- "Caveat: This is monolith velocity. Still one big deployment, still monthly releases."
- **If Steve asks:** "Why only monthly releases?" → Next slide addresses that

---

## SLIDE 3: Productivity - Context & Ceiling

**Layout:** Two-column with bottom callout box

**Header:** Productivity - Context & Ceiling

**Column 1: What's Working**
- Org transformation
	- From: 1 director, 3 managers
	- To: 4 directors, 12 managers (hands-on, player-coach)
- AI-native SDLC (Aaron hired, tooling deployed)
- Cultural shifts (teams requesting testing ownership, incremental delivery)
- Leadership stability (hands-on through transformation)

**Column 2: What's Limiting**
- The monolith (testing/risk/blast radius bottleneck)
- Legacy org structure (just started transitioning)
- Culture debt (fear of releasing, "everything is a project")
- Competing priorities (roadmap vs. resiliency vs. tech debt)

**Bottom Callout Box:**
**REALITY:** Incremental improvements until structural changes complete. We're making progress, but fighting the structure of the system.

**Talking Points:**
- "We're making progress, but we're fighting the structure of the system."
- "Every feature still deploys the entire monolith. That's a 14-year-old codebase with 80 engineers touching it."
- "The org structure was 1 director for 80 people. That's not scalable. We're fixing it."
- "The good news: Cultural shifts are happening. Teams WANT autonomy. That's huge."
- **If Steve asks:** "When do improvements become transformational?" → When the two criteria on Slide 1 are met

---

## SLIDE 4: Other Resiliency Priorities - Scorecard

**Layout:** Full-slide table

**Header:** Other Resiliency Priorities - Scorecard

**Table:**
| Priority | Status | Notes |
|----------|--------|-------|
| DB Migration to Managed Databases | 🟢 On track | Atlas Migration completion Aug 29 |
| DR Test (RTO/RPO) | 🟢 On track | Lower environment test: RTO 4:45, RPO: 0:15, Internal target October, External comms December  |
| Red Mythos/Vulnerabilities | 🟡 Complex | Monolith dependencies - still targeting Q2 |
| EOL Technologies | 🟡 Complex  | Atlas, Elasticsearch, Java upgrades, OSS upgrades |
| ICS (Industry Continuity) | 🟢 On track | Building FTE team to own this |
| Breaking the Monolith | 🟡 In progress | The big one (next slides) |

**Talking Points:**
- "Most resiliency work is on track. The hard one is breaking the monolith."
- "Vulnerabilities: The 858→98 analysis is misleading. Aaron/Ben doing horizontal dependency analysis — it's wholesale upgrades, not story-by-story."
- "DR test happened this week (Incident Games). Early results look good."
- **If Steve asks:** "What's the risk?" → Monolith dependencies create coupling. We're breaking those dependencies with autonomous teams.

---

## SLIDE 5: The Monolith Problem

**Layout:** Two-column with subtitle

**Header:** The Monolith Problem

**Subtitle:** The monolith is both technical and organizational

**Column 1: Technical Reality**
- 14-year-old codebase, 80+ engineers, monthly releases
- Single deployment footprint (Blue-Green in us-east-1)
- Shared database schemas = blast radius on every change
- Testing bottleneck = defensive, slow releases

**Column 2: Organizational Reality**
- 1 director for 80 people = impossible span of control
- Everything needs cross-team coordination
- Fear culture ("what if we break something?")
- Product launches = big-bang, not incremental

**Talking Points:**
- "This is why productivity gains are incremental. We're optimizing within a constrained system."
- "The monolith isn't just code. It's how we're organized. You can't fix one without the other (Reverse Conway)."
- "The Kickdrum consultants saw this immediately. They validated: Gen3 scope needs boundaries."
- **If Steve asks:** "Why didn't we fix this years ago?" → We are now. That's the resiliency work.

---

## SLIDE 6: The Cost of the Monolith

**Layout:** Two-column

**Header:** The Cost of the Monolith

**Column 1: Cost for Product & Customers**
- Innovation throttled (everything is a "project")
- Poor deployment frequency
- Long lead time for changes
- Cannot respond quickly to customer needs
- Slow incident remediation
- Delayed security fixes

**Column 2: Cost for Engineering**
- Things that should be easy are now high risk and difficult
- Uncertainty of impact / side effects
- Coordination overhead
- Lack of autonomy
- Difficult to prioritize and manage mixed work streams

**Talking Points:**
- "The monolith creates costs for everyone — customers waiting for features, product unable to iterate, engineers losing autonomy."
- "Long lead times aren't just internal inefficiency — they're customer-facing delays."
- "Engineering talent ceiling: Senior engineers want ownership, not coordination tax."

---

## SLIDE 7: Resiliency Endgame - Completion Criteria

**Layout:** Two-column (Must Haves | Negotiables) with subtitle

**Header:** Resiliency Endgame - Completion Criteria

**Subtitle:** WHEN ARE WE DONE? Two completion criteria:

**Left Column: Must Haves (We won't be stable without these)**

**1. 12 Autonomous Teams Operating Independently**
- Own their domain/component
- Deploy independently (no monolith coordination)
- Own application-near infrastructure
- Sprint independently
- ✅ Progress: 70% (org structure in place, technical decoupling starting)

**2. Data Stored in Purpose-Built Products**
- MongoDB → RDS, DynamoDB, Aurora (right tool for job)
- Scalability becomes elastic (not manual intervention)
- HA/DR becomes config setting (not a project)
- Cost optimization unlocked
- 🟡 Progress: 20% (Atlas migrations in progress, architectural changes in planning)

**Right Column: Negotiables (Will improve things, but not blocking stability)**

**Platform & Data:**
- Event/messaging system replacement (EventBus MongoDB → SQS/Kafka with SDK)
- Activity Flow optimization (S3-based storage vs 188M docs/day churn)
- Observability: extend log retention (7 days → longer), proactive alerting
- Service health checks and monitoring improvements

**Development & Delivery:**
- Testing framework modernization (replace Tandoori)
- Feature flags system
- Mapping tool modernization (EDI → JSON, evaluate IBM Sterling/Edifecs)
- Infrastructure tooling (GitHub Actions, containerization)

_These are Gen3 scope or continuous improvement. Not blocking "out of the woods."_

**Talking Points:**
- "This is the answer to 'when are we done?' Two things. Everything else is negotiable."
- "The team validated this framing. Curtis validated it. Kickdrum consultants implicitly validated it (Gen3 scope boundary)."
- "Must Have #1 is organizational + technical. We're 70% there. The org structure is in place, now we're breaking technical coupling."
- "Must Have #2 is expensive but unlocks massive operational leverage. HA/DR becomes a checkbox, not a 6-month project."
- "Negotiables: These are improvements we'll make, but they don't define 'done'. EventBus replacement, Activity Flow optimization, better observability — all valuable, none blocking stability."
- **If Steve asks:** "How long?" → Org transformation is 9-12 months (we're 4 months in). Data layer migrations are 12-18 months (overlapping).

---

## SLIDE 8: Current Progress - What's Happening Right Now

**Layout:** Four-quadrant grid

**Header:** Current Progress - What's Happening Right Now

**Quadrant 1: Organizational**
- 1 director/3 EMs → 4 directors/12 EMs (for ~80 engineers)
- Each team defining: domain, coupling points, deployment blockers
- Teams moving to GitHub repos (out of monorepo)

**Quadrant 2: Technical**
- Template for breaking pieces off monolith (repo, CI/CD, infra)
- AI-Native SDLC (Dedicated team for this, Aaron hired, teams adopting)
- Architecture backlog discussions (debt visibility)

**Quadrant 3: Cultural**
- Teams requesting testing ownership (huge shift)
- Incremental delivery wins (MEX Core UI Migrations, EMS Managed Services Portal)
- Teams breaking off components proactively

**Quadrant 4: Hiring**
- 4 directors (3 hired, 1 in final rounds)
- 12 EMs (8 hired, 4 in process)
- Other Key Roles (AI Director, senior ICs)

**Talking Points:**
- "This is the evidence the strategy is working. Org transformation is real."
- "Technical progress: We have a template now. Teams know how to break off components."
- "Cultural shifts are the leading indicator. Teams WANT autonomy. That's not mandated, that's emergent."
- "Hiring: We're building the leadership bench. These directors/EMs will scale beyond Exchange."
- **If Steve asks:** "What's the risk?" → Cultural resistance (fear of releasing). Mitigated by incremental wins + leadership consistency.

---

## SLIDE 9: Capacity Evolution (Q2 → Q3 → Q4)

**Layout:** Three pie charts side by side with subtitle

**Header:** Capacity Evolution (Q2 → Q3 → Q4)

**Subtitle:** Key: Autonomous teams reduce KTO burden, unlock roadmap capacity

**Chart 1: Q2 2026 (Baseline - Current)**
- 70% Technical Work (KTO: incidents, vulnerabilities, DR, migrations + Modernization: breaking monolith, org transformation)
- 30% Commercial Roadmap (new features, customer commitments)

**Chart 2: Q3 2026 (Transition)**
- 60% Technical Work (-10%)
- 40% Commercial Roadmap (+10%)

**Chart 3: Q4 2026 (Stabilized)**
- 50% Technical Work (-10%)
- 50% Commercial Roadmap (+10%)

**Talking Points:**
- "This is the economic argument. Breaking the monolith unlocks capacity."
- "Q2 baseline: 70% of capacity goes to keeping the lights on and modernization. Only 30% for roadmap."
- "Q4 target: 50/50 split. That's the inflection point."
- "The shift happens because autonomous teams reduce firefighting burden and coordination overhead."
- "This is conservative. Once teams are fully autonomous, we could shift even more capacity to roadmap."
- **If Steve asks:** "What does this mean for roadmap commitments?" → By Q4 we can absorb significantly more roadmap work than today.

---

## SLIDE 10: Org Chart - The New Structure

**Layout:** Two-column (left: text, right: org chart visual)

**Header:** Org Chart - The New Structure

**Left Column:**
**The Transformation**
- **Before:** 1 Director → 3 EMs → 80 engineers
- **After:** 4 Directors → 12 EMs → ~80 engineers

**Each Team:**
- 6-8 engineers
- Cross-functional (backend, frontend, QA, DevOps)
- Domain-aligned (Platform Services, Business Logic, Data/Integration, etc.)
- Autonomous delivery capability

**Right Column:**
**Visual:** [Placeholder for org chart - add actual org chart here]

**Talking Points:**
- "This is the organizational foundation for the resiliency endgame."
- "Each EM leads one small team with clear domain ownership."
- "Each director leads a portfolio of related domains (Platform, Business Logic, etc.)."
- "This structure scales. We can add teams without breaking the model."
- **If Steve asks:** "What's the investment?" → 4 directors + 9 EMs (net new). Pays for itself in reduced firefighting by Q4.

---

## Notes for Regeneration

### Design Choices:
- **Color palette:** Navy (#1C2833), slate (#2E4053), light gray backgrounds
- **Typography:** Arial (web-safe, professional)
- **Layout:** Clean, minimal styling to accept company theme easily

### Charts/Tables Used:
- **Slide 2:** Grouped bar chart (3 metrics × 3 months)
- **Slide 4:** Status table (6 priorities)
- **Slide 8:** Three pie charts (capacity allocation)
- **Slide 9:** Placeholder for org chart visual

### Key Message Architecture:
1. **Productivity:** Real gains, but incremental until structure changes
2. **Resiliency:** Two completion criteria define "done"
3. **Capacity:** Shift from 60% reactive → 50% reactive by Q4

### Files:
- **HTML slides:** `slide1.html` through `slide9.html`
- **Generator:** `create-presentation.js`
- **Output:** `CJ-Strategic-Update.pptx`
