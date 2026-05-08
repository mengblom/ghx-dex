# CJ Strategic Update - Presentation Outline (v3 - Concise)

**Following:** `00-Inbox/Temp/CJ Meeting Prep - More Concise Slide Outline.md`  
**Total Slides:** 13

---

## SLIDE 1: The Asks from CJ

**Layout:** Simple title + 3 bullets

**Header:** Today's Agenda

**Content:**
1. **Commentary / State of the Union on Productivity Improvements**
2. **Update on Exchange Resiliency Work**
3. **Capacity Planning Forecast**

**Talking Points:**
- "CJ asked for three things. Let's walk through each."

---

## SLIDE 2: Executive Summary

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
- "Three questions: Are we productive? When are we stable? What's the capacity outlook?"

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
**Chart:** Productivity trends bar chart

**Talking Points:**
- "4-month trend is positive. Feb→Mar jump is bigger than Jan→Feb. Why? Org changes starting to land."

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

---

## SLIDE 5: In Summary - Incremental Improvements

**Layout:** Single callout box centered

**Header:** Productivity - In Summary

**Callout Box:**
**We are making incremental productivity improvements.**

As long as we operate in a monolithic codebase, deployment footprint, and team structure, improvements will be incremental rather than transformational.

The org transformation (1 director → 4 directors, 12 EMs) is the foundation for exponential gains.

**Talking Points:**
- "Incremental is good. But we need transformational."
- "Transformational requires breaking the monolith — both code and org."

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
| ICS (Industry Continuity) | 🟢 On track | Building FTE team to own this |
| Breaking the Monolith | 🟡 In progress | The big one (next slides) |

**Talking Points:**
- "Most resiliency work is on track. Breaking the monolith is the hard one."

---

## SLIDE 7: The Monolith

**Layout:** Reference slide from "Building Autonomous Teams" deck (slide 4)

**Header:** The Monolith

**Content:** [Visual from existing deck showing the vicious cycle]

**Talking Points:**
- "The monolith is both technical and organizational."
- "Vicious cycle: Large codebase → High risk → Defensive testing → Slow releases → Batching → Larger changes → Higher risk"

---

## SLIDE 8: The Cost of the Monolith

**Layout:** Two-column (reference slides 6-7 from "Building Autonomous Teams" deck)

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

---

## SLIDE 9: Monolith vs. Services Owned by Autonomous Teams

**Layout:** Reference slide 9 from "Building Autonomous Teams" deck

**Header:** Monolith vs. Services Owned by Autonomous Teams

**Content:** [Visual from existing deck showing the comparison]

**Talking Points:**
- "This is the target state. Smaller services, clear ownership, independent deployment."
- "Reverse Conway Maneuver: Org structure drives architectural change."

---

## SLIDE 10: What Does Autonomous Teams Mean?

**Layout:** Single-column with definition

**Header:** What Does Autonomous Teams Mean?

**Subtitle:** It is team structure, process, AND architectural

**Content:**

**Team Structure & Process:**
- Dedicated EM and Product Owner (1:1 ratio)
- 6-8 engineers (cross-functional: backend, frontend, QA, DevOps)
- Sprint independently (dedicated Jira project, backlog)
- "Team API" (Slack channels per convention, clear interfaces)

**Architectural:**
- Own and deploy their component independently (no monolith coordination)
- Own their application-near infrastructure
- Own their deployment pipelines
- Services, not monolith modules

**This is how it ties back to "Increase Modularity" priority**

**Talking Points:**
- "Autonomous teams require architectural decoupling. You can't have one without the other."
- "This ties to the 5th Exchange priority: 'Increase Modularity' = breaking the monolith."

---

## SLIDE 11: "End" of Resiliency Work - When Are We Out of the Woods?

**Layout:** Two sections (Must Haves)

**Header:** "When Are We Out of the Woods?"

**Must Haves (We won't be stable without these):**

**1. 12 Autonomous Teams Operating Independently**
- Dedicated EM, PO (1:1 ratio)
- Own and deploy components independently
- Own application-near infrastructure
- Own deployment pipelines
- Sprint independently
- ✅ Progress: 70% (org structure in place, technical decoupling starting)

**2. Data Stored in Purpose-Built Products**
- MongoDB → RDS, DynamoDB, Aurora, S3 (right tool for job)
- Scalability becomes elastic (not manual intervention)
- HA/DR becomes config setting (not a project)
- Cost optimization unlocked
- 🟡 Progress: 20% (Atlas migrations in progress, architectural changes in planning)

**Talking Points:**
- "Two things define 'done.' Everything else is negotiable."

---

## SLIDE 12: Backlog of Resiliency/Tech Debt Work

**Layout:** Two-column list

**Header:** We Will Still Have a Backlog

**Subtitle:** Still required, but timing negotiable. Veritas/Kickdrum will likely comment.

**Column 1: Platform & Data**
- Event/messaging system replacement (EventBus MongoDB → SQS/Kafka)
- Activity Flow optimization (S3-based storage vs 188M docs/day churn)
- Observability improvements (extend log retention, proactive alerting)
- Service health checks

**Column 2: Development & Delivery**
- Testing framework modernization (replace Tandoori)
- Feature flags system
- Mapping tool modernization (EDI → JSON)
- Cloud-native infra (serverless, managed services)

**Talking Points:**
- "These are improvements, not blockers."
- "Kickdrum will see these gaps. We know. Timing is negotiable."

---

## SLIDE 13: Capacity Pie Chart Evolution

**Layout:** Three pie charts side by side

**Header:** Capacity Evolution (Q2 → Q3 → Q4)

**Subtitle:** Autonomous teams reduce KTO burden, unlock roadmap capacity

**Chart 1: Q2 2026 (Baseline)**
- 70% Technical Work (KTO + Modernization)
- 30% Commercial Roadmap

**Chart 2: Q3 2026 (Transition)**
- 60% Technical Work
- 40% Commercial Roadmap

**Chart 3: Q4 2026 (Stabilized)**
- 50% Technical Work
- 50% Commercial Roadmap

**Talking Points:**
- "Q2 baseline: 70% technical. Q4 target: 50/50 split."
- "By Q4 we can absorb significantly more roadmap work."

---

## Notes for Generation

**Design:**
- Same clean professional style (navy/slate palette, Arial)
- Reuse slides from v2 where possible

**Slides to Reuse from v2:**
- Slide 1 (The Ask) → slide02.html
- Slide 2 (Executive Summary) → slide01.html
- Slide 3 (Productivity Positive) → slide03.html
- Slide 4 (Productivity Challenges) → slide04.html
- Slide 5 (Summary) → slide05.html
- Slide 6 (Resiliency Scorecard) → slide06.html
- Slide 8 (Cost of Monolith) → slide08.html
- Slide 13 (Capacity) → slide14.html

**New Slides to Create:**
- Slide 7: The Monolith (placeholder reference to existing deck)
- Slide 9: Monolith vs Services (placeholder reference to existing deck)
- Slide 10: What Does Autonomous Teams Mean?
- Slide 11: When Are We Out of the Woods?
- Slide 12: Backlog of Work

**Files:**
- Directory: `v3/`
- Output: `CJ-Strategic-Update-v3.pptx`
