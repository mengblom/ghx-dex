# CJ Strategic Update - Presentation Outline (v2)

**Following Meeting Prep Structure:** `00-Inbox/Meeting_Prep_CJ_2026-05-08.md`  
**Date:** 2026-05-08

---

## SLIDE 1: Executive Summary (3-Column)

**Layout:** Three-column layout with header

**Header:** Executive Summary

**Column 1: Productivity**
- **Heading:** Productivity
- **Subhead:** Measurable improvement, structural ceiling remains
- Stories completed up 86% (207→386)
- Cycle time down 48% (44→23 days)
- Gains are incremental until monolith + org structure changes complete

**Column 2: Resiliency - "When are we done?"**
- **Heading:** Resiliency - "When are we done?"
- **Subhead:** 2 Must-Do
- 12 autonomous teams deploying independently (70% org work done)
- Data layer modernization (MongoDB → purpose-built stores)

**Column 3: Capacity Forecast**
- **Heading:** Capacity Forecast
- **Subhead:** Shift from reactive to strategic
- Q2: 70% technical / 30% roadmap
- Q4: 50% technical / 50% roadmap

**Talking Points:**
- "Three questions CJ needs to answer for Steve: Are we productive? When are we stable? What's the capacity outlook?"
- "This is the soundbite version. Each section gets deeper in the deck."

---

## SLIDE 2: The Ask from CJ

**Layout:** Simple title + 3 bullets

**Header:** Today's Agenda

**Content:**
1. **Commentary / State of the Union on Productivity Improvements**
2. **Update on Exchange Resiliency Work**
3. **Capacity Planning Forecast**

**Talking Points:**
- "CJ asked for three things. We'll walk through each."
- "Productivity first, then resiliency deep dive, then capacity projections."

---

## SLIDE 3: Productivity Assessment - Positive Signs

**Layout:** Two-column (left: metrics, right: chart)

**Header:** Productivity - Positive Signs in the Data

**Left Column:**
**4-Month Trends (Jan → Mar)**
- Stories Completed: 207 → 271 → 386 (+86%)
- Lead Time to Change: 30 → 33 → 8 days (-73%)
- Cycle Time: 44 → 44 → 23 days (-48%)

**Also:**
- Last 3 releases clean (no major incidents)
- AI library launched (Claude Code adoption growing)
- Exchange Health Score beta (leading indicator dashboard)

**Right Column:**
**Chart:** Productivity trends (Stories, Lead Time, Cycle Time)

**Talking Points:**
- "4-month trend is positive. We're completing more, faster."
- "Lead time drop (33→8 days) is the most telling — we're deciding faster."
- "Feb→Mar jump is bigger than Jan→Feb. Why? Org changes starting to land."
- "Exchange Health Score gives us leading indicators instead of lagging metrics."

---

## SLIDE 4: Productivity Assessment - Challenges

**Layout:** Two-column list

**Header:** Productivity - Challenges

**Column 1: Technical & Organizational**
- The monolith (testing/risk/blast radius bottleneck)
- The org was also "monolithic" (1 director, 80 people) — we're solving this
- Culture debt (fear of releasing, "everything is a project")

**Column 2: Process & Visibility**
- Visibility/reporting problem (roadmaps at epic level, always a new data request)
- Competing priorities, "show your progress" asks
- Product-Engineering engagement (best practice: 1-1 PO to EM, we don't have that)
- Large opportunity cost at leadership level (hands-on leadership required through change)

**Talking Points:**
- "These challenges aren't excuses — they're the work."
- "The monolith is both technical and organizational. You can't fix one without the other."
- "Hands-on leadership through transformation is expensive but necessary."

---

## SLIDE 5: Productivity - Summary

**Layout:** Single callout box centered

**Header:** Productivity - In Summary

**Callout Box:**
**We are making incremental productivity improvements.**

As long as we operate in a monolithic codebase, deployment footprint, and team structure, improvements will be incremental rather than transformational.

The org transformation (1 director → 4 directors, 12 EMs) is the foundation for exponential gains.

**Talking Points:**
- "Incremental is good. But we need transformational."
- "Transformational requires breaking the monolith — both code and org."
- "We're doing both simultaneously."

---

## SLIDE 6: Other Resiliency Priorities - Scorecard

**Layout:** Full-slide table

**Header:** Other Resiliency Priorities - Scorecard

**Table:**
| Priority | Status | Notes |
|----------|--------|-------|
| DB Migration to Managed Databases | 🟢 On track | Atlas Migration completion Aug 29 |
| DR Test (RTO/RPO) | 🟢 On track | Lower environment test: RTO 4:45, RPO 0:15. Internal target October, External comms December |
| Red Mythos/Vulnerabilities | 🟡 Complex | Monolith dependencies - targeting July 2 completion |
| EOL Technologies | 🟡 Complex | Atlas, Elasticsearch, Java upgrades, OSS upgrades |
| ICS (Industry Continuity) | 🟢 On track | Building FTE team to own this (transitioning from contractors) |
| Breaking the Monolith | 🟡 In progress | The big one (next slides) |

**Talking Points:**
- "Most resiliency work is on track. Breaking the monolith is the hard one."
- "Vulnerabilities: Targeting July 2 completion, but monolith dependencies add complexity."
- "DR test went well this week — Incident Games validated RTO/RPO targets."
- "ICS: Building internal FTE capability to reduce contractor dependency."

---

## SLIDE 7: The Monolith Problem

**Layout:** Two-column with subtitle

**Header:** The Monolith Problem

**Subtitle:** The monolith is both technical and organizational

**Column 1: Technical Reality**
- 14-year-old codebase, 80+ engineers, monthly releases
- Single deployment footprint (Blue-Green in us-east-1)
- Shared database schemas = blast radius on every change
- Testing bottleneck = defensive, slow releases
- At this size, everything needs to be a "project"

**Column 2: Organizational Reality**
- 1 director for 80 people = impossible span of control
- Everything needs cross-team coordination
- Fear culture ("what if we break something?")
- Product launches = big-bang, not incremental
- Deep changes require hands-on leadership

**Talking Points:**
- "You can't fix the technical monolith without fixing the organizational monolith."
- "Reverse Conway Maneuver: Change the org structure to force the architectural change."
- "This is not how we want to work long-term, even post-monolith."

---

## SLIDE 8: The Cost of the Monolith

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
- Talent ceiling (senior engineers want ownership)

**Talking Points:**
- "The monolith creates costs for everyone."
- "With AI, this will get worse — more code, faster, larger blast radius."
- "Senior engineers leave when they can't own anything end-to-end."

---

## SLIDE 9: The Goal - Autonomous Teams

**Layout:** Single-column with bullets

**Header:** The Goal - Autonomous Teams

**The Exchange is too big to work on as 1 team, 1 system**

**What does "autonomous" mean?**
- Dedicated EM and Product Owner (1:1 ratio)
- Own and deploy their component independently (no monolith coordination)
- Own their application-near infrastructure
- Own their deployment pipelines
- Sprint independently (dedicated Jira project, backlog)
- "Team API" (Slack channels per convention, clear interfaces)

**Why autonomous teams?**
- Smaller blast radius = faster, safer releases
- Clear ownership = accountability and pride
- Things that required a "project" become normal work
- Reverse Conway Maneuver: Org structure drives architectural decoupling

**Talking Points:**
- "This is not just about structure. It's about empowerment."
- "Autonomous teams can move fast because they own their destiny."
- "This includes current resiliency work AND future roadmap work."

---

## SLIDE 10: Progress So Far - The New Org

**Layout:** Two-column

**Header:** Progress So Far - The New Org

**Column 1: Before → After**

**Before:**
- 1 Director
- 3 Engineering Managers
- 80+ engineers
- Heavy contractor mix

**After:**
- 4 Directors
- 12 Engineering Managers (each leading 1 small team)
- ~80 engineers (6-8 per team)
- Transitioning contractors → FTEs

**Column 2: Hiring Progress**
- **Directors:** 3 hired, 1 in final rounds
- **EMs:** 8 hired, 4 in process
- **Key IC roles:** AI Director (Aaron), senior ICs for platform/infrastructure
- **Org chart:** [Reference separate slide]

**Talking Points:**
- "Org structure is 70% complete."
- "Each EM leads one small team — no matrix, clear ownership."
- "FTE conversion creates stability and institutional knowledge."

---

## SLIDE 11: Progress So Far - Technical & Cultural

**Layout:** Two-column

**Header:** Progress So Far - Technical & Cultural

**Column 1: Technical Progress**
- Template for breaking pieces off monolith (repo, CI/CD, infra)
- AI-Native SDLC (Aaron hired, dedicated team, tooling deployed)
- Architecture backlog discussions (debt visibility)
- Teams moving to GitHub repos (out of monorepo)

**Column 2: Cultural Progress (Signs of Change)**
- Teams requesting testing ownership (huge shift from fear culture)
- Teams breaking off components proactively (not mandated)
- Incremental delivery wins:
  - MEX Core UI Migrations
  - EMS Managed Services Portal (quarterly commits to 2027 Q2)

**Talking Points:**
- "Cultural shifts are the leading indicator. Teams WANT autonomy."
- "The template for breaking from the monolith is proven — teams know how to do it."
- "AI-Native SDLC: This transformation is a golden opportunity to build AI into the process from day one."

---

## SLIDE 12: What's Happening Right Now

**Layout:** Single-column with sections

**Header:** What's Happening Right Now

**Each Team is Defining:**
- **Your domain** — What's in scope, what's out, where are the boundaries fuzzy?
- **Coupling points** — How are you tied to the monolith or other services? Shared repos, direct dependencies, shared databases?
- **Deployment blockers** — What prevents you from deploying independently today?

**Template Activities in Progress:**
1. Move components to GitHub repos
2. Stand up deployment pipelines
3. Define team APIs and integration contracts
4. Break database coupling

**Autonomous Team Behaviors Emerging:**
- Teams making decisions (testing strategies, tooling choices)
- Freedom to move forward without cross-team coordination
- Architecture backlog discussions surfacing tech debt

**Talking Points:**
- "This isn't theory. It's happening now."
- "Each team is doing the hard work of understanding their dependencies."
- "The template gives them a playbook — they're not starting from scratch."

---

## SLIDE 13: Resiliency Endgame - "When Are We Done?"

**Layout:** Two-column (Must Haves | Negotiables) with subtitle

**Header:** Resiliency Endgame - "When Are We Done?"

**Subtitle:** 2 completion criteria define "done"

**Left Column: Must Haves (We won't be stable without these)**

**1. Autonomous Teams Operating Independently**
- Dedicated EM, PO (1:1 ratio)
- Own and deploy components independently
- Own application-near infrastructure
- Own deployment pipelines
- Sprint independently
- "Team API" (Slack channels, clear interfaces)
- ✅ Progress: 70% (org structure in place, technical decoupling starting)

**2. Data Stored in Purpose-Built Products**
- MongoDB → RDS, DynamoDB, Aurora, S3 (right tool for job)
- Scalability becomes elastic (not manual intervention)
- HA/DR becomes config setting (not a project)
- Cost optimization unlocked
- Redirect dependencies to CDP where appropriate
- 🟡 Progress: 20% (Atlas migrations in progress, architectural changes in planning)

**Right Column: Negotiables (Still required, timing negotiable)**

**Platform & Data:**
- Event/messaging system replacement (EventBus MongoDB → SQS/Kafka with SDK)
- Infinitely scalable queue/event subscribers (Lambdas)
- Activity Flow optimization (S3-based storage vs 188M docs/day churn)
- Observability improvements (extend log retention, proactive alerting)

**Development & Delivery:**
- Testing framework modernization (replace Tandoori)
- Feature flags system
- Mapping tool modernization (EDI → JSON)
- Cloud-native infra (serverless, managed services)

_These will continue to hold us back, but they don't define "done."_

**Talking Points:**
- "This is the answer to 'when are we done?' Two things. Everything else is negotiable."
- "Must Have #1 is organizational + technical. We're 70% there."
- "Must Have #2 is expensive but unlocks massive operational leverage."
- "Negotiables: I'd be shocked if Veritas/Kickdrum doesn't comment on these. But they don't block stability."
- **If Steve asks:** "How long?" → Org transformation is 9-12 months (we're 4 months in). Data layer migrations are 12-18 months (overlapping).

---

## SLIDE 14: Capacity Evolution (Q2 → Q3 → Q4)

**Layout:** Three pie charts side by side with subtitle

**Header:** Capacity Evolution (Q2 → Q3 → Q4)

**Subtitle:** Key: Autonomous teams reduce KTO burden, unlock roadmap capacity

**Chart 1: Q2 2026 (Baseline)**
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
- "Q2 baseline: 70% of capacity goes to keeping the lights on and modernization."
- "Q4 target: 50/50 split. That's the inflection point where we can absorb significantly more roadmap work."
- "This is conservative. Once teams are fully autonomous, we could shift even more to roadmap."
- **If Steve asks:** "What does this mean for roadmap commitments?" → By Q4 we can absorb 2x the roadmap work we can today.

---

## SLIDE 15: Org Chart - The New Structure

**Layout:** Two-column (left: transformation summary, right: visual org chart)

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
**Visual:** [Placeholder for org chart]

**Talking Points:**
- "This is the organizational foundation for the resiliency endgame."
- "Each EM leads one small team with clear domain ownership."
- "This structure scales. We can add teams without breaking the model."
- **If Steve asks:** "What's the investment?" → 4 directors + 9 EMs (net new). Pays for itself in reduced firefighting by Q4.

---

## SLIDE 16: The Future - Steve's Vision

**Layout:** Single-column with vision statement

**Header:** The Future - 100% Self-Serve

**Vision Statement:**
Steve's vision: 100% self-serve customer experience

**What this requires from us:**
- Autonomous teams that can move fast without coordination tax
- Modern, decoupled architecture that supports rapid iteration
- Data layer that scales infinitely without manual intervention
- Platform capabilities (CDP, AI Platform) that enable new products quickly
- Culture of experimentation and incremental delivery

**Why we're building for this:**
- Self-serve reduces CAC, increases NPS, unlocks new markets
- Requires architecture and org that can ship features weekly, not monthly
- The work we're doing now (autonomous teams, data layer, breaking monolith) is the foundation

**Talking Points:**
- "Steve's vision is ambitious. It requires everything we're building."
- "Self-serve isn't just a feature. It's an architectural and organizational capability."
- "By Q4, we'll have the foundation to accelerate toward this vision."

---

## Notes for Generation

**Design:**
- Same clean professional style (navy/slate palette, Arial typography)
- Minimal styling to accept GHX company theme

**Key Changes from Previous Version:**
- Follows user's original meeting prep flow
- More narrative progression (problem → goal → progress → endgame)
- Added slides: The Ask, Challenges, Summary, Goal, What's Happening Right Now, The Future
- Kept best content: Executive Summary, Productivity data with chart, Resiliency Scorecard, Must Haves/Negotiables, Simplified Capacity charts

**Files:**
- New HTML slides: `slide-v2-01.html` through `slide-v2-16.html`
- New generator: `create-presentation-v2.js`
- Output: `CJ-Strategic-Update-v2.pptx`
