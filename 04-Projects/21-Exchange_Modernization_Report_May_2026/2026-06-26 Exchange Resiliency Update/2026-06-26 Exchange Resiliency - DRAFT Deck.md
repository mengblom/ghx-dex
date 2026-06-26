# Exchange Resiliency & Transformation Update
**June 26, 2026**  
**Marten Engblom → CJ Singh**

*Note: Draft deck - impacted by June 22-24 production incident response*

---

## Slide 1: Opening Frame

**Title: Exchange Transformation - Progress & Path Forward**

**Context:**
- This week's production incident is not noise - it's signal
- Shows exactly why the transformation work matters
- Perfect case study for the journey from "heroic firefighting" to "resilient systems"

**Today's agenda:**
1. Resiliency commitments - status update
2. Transformation story - what we've actually built
3. Current focus - why autonomous teams change everything
4. What remains - the honest technical debt roadmap

---

## Slide 2: The Six Resiliency Commitments - Status

**From 2026 Tech Org Priorities**

| Commitment | Status | Owner | Notes |
|------------|--------|-------|-------|
| DB Migration to managed databases | ✅ In Progress | Daniel | MongoDB → Atlas, ES → Elastic Cloud |
| DR Drills (4hr RTO, 2hr RPO) | ✅ Active | Daniel | Oct 8 failover planned, runbooks current |
| Vulnerabilities within SLA | ✅ In Progress | Aaron | Red Mythos Exchange project |
| Eliminate EOL technologies | ✅ In Progress | Aaron | Red Mythos Exchange project |
| Industry Continuity Solution | ✅ Active | Jena Milan | Contractor-built, June 15 status update |
| Increase Modularity | 🔄 Ongoing | Marten | Multiple initiatives, see org transformation |

**Key insight:** We're executing on all six - but this week's incident proves modularity is the linchpin.

---

## Slide 3: The Org Transformation Story

**Before (2024):**
- 1 Director
- 3 Managers  
- ~100 Engineers in large, loosely organized teams
- Reactive firefighting culture
- Monolithic coupling everywhere

**After (2026):**
- 4 Directors
- 12 Managers
- 3-5 person teams (Spotify/FAANG model)
- Proactive engineering culture
- Modern organizational structure

**References:**
- Henrik Kniberg's Spotify Engineering Culture (YouTube)
- Team Topologies by Matthew Skelton
- FAANG engineering blog posts (Google, Netflix, Amazon)

**The transformation isn't just org chart shuffling - it's enabling autonomous teams that can move fast without breaking things.**

---

## Slide 4: Resiliency Work - Promised vs. Completed

**The story of comprehensive execution**

Over the last 18 months, we've made progress across **all five dimensions** of resiliency:

1. **Database & Data Layer** - Foundation stabilization
2. **Architectural Decoupling** - Breaking the monolith
3. **Infrastructure & Resilience** - Platform capabilities
4. **Observability & Operations** - Seeing what's happening
5. **Process, Governance & Security** - How we work

**Format:** Each section shows what we promised (left) vs. what we completed (right)

**Key insight:** 43 completed or in-progress items - not cherry-picked wins, comprehensive coverage

---

## Slide 5: Database & Data Layer

| **What We Promised** | **What We Completed** |
|---------------------|----------------------|
| • DB Stabilization: Audit DB and BT/BD optimization<br>• MongoDB migration to Atlas (managed service)<br>• Elasticsearch migration to Elastic Cloud<br>• AuditDB improvements, optimization, cleanup<br>• TPM database query optimization<br>• TPM Database Upgrade<br>• IBR data migration<br>• Replace direct DB calls with MEX APIs | • **IBR User Data Separation** (Phase 2: Sept 2025, Phase 3: Ongoing) - Migrated 4 tables (~40% of TPM footprint)<br>• **BR User Data Cache** (Aug 2025) - 80% reduction in TPM reads<br>• **TPM to Aurora Migration** (May 2026+) - Multi-region sync enabled<br>• **Semijoin Optimization** (July 2025) - Re-enabled post-MySQL 8.0 incident<br>• **MEX Query Optimization** (June 2026) - Prevents slowness incidents<br>• **AuditDB ILM Data Cleanup** - Completed<br>• **D Semaphore to Redis** (Feb 2026) - Removed AuditDB dependency<br>• **Atlas Migration** - Ongoing<br>• **ES Migration** - Ongoing<br>• **Org Search in ES** - Bulk load: 30min → 5min |

---

## Slide 6: Architectural Decoupling

| **What We Promised** | **What We Completed** |
|---------------------|----------------------|
| • Exchange Platform Modularization<br>• SSO Decoupling from AuditDB & TPM<br>• User Data Decouple (IBR migration)<br>• Tracking Engine Decouple<br>• Hash Map Load Balancing<br>• Dead Listener Refactor<br>• Feed Processor Refactor<br>• Document Processing Phase 2<br>• Data Poller overhaul<br>• Replace TPM API | • **SSO: Identity Service DB out of Audit** (Aug 2025) - AuditDB degradation no longer impacts logins<br>• **SSO: TPM DB Separation Phase I** (Nov 2025) - 52 tables migrated to dedicated SSO DB<br>• **Org API Gateway** (May 2026) - Decoupled from Exchange, no SCA/Data Connect coupling<br>• **RC 2.0 Monolith Decoupling** (Feb 2026+) - Own GitHub repo and pipelines<br>• **UI Decoupling** - 4 UIs separated: Orders (July 2024), Notifications (Sept 2025), Transactions (Sept 2025), Invoicing (April 2026)<br>• **AdapterAPI Part 2** (March 2025) - IO adapters decoupled from TPM<br>• **Tracking Engine** - Separate repo and pipeline<br>• **Notifications Engine** - Separate repo and pipeline<br>• **Doc IO API Split** - Completed |

---

## Slide 7: Infrastructure & Resilience

| **What We Promised** | **What We Completed** |
|---------------------|----------------------|
| • DR Drills (4hr RTO, 2hr RPO)<br>• Industry Continuity Solution (ICS)<br>• New Performance Environment<br>• Performance Testing capability<br>• Managed Database Services<br>• Scheduling Enhancements<br>• Processing Engine improvements<br>• Event Bus Next Generation<br>• IO Guarantee improvements | • **Performance Environment** (Jan-Jun 2025) - Critical for upgrades, caught issues pre-prod<br>• **EventBus Resiliency** (July 2025) - Reduced doc processing impact during incidents<br>• **Processing Engine Robustness** (April 2025) - Threadpool tuning, priority fixes, Java Flight Recorder<br>• **IO Guarantee - SQS Backup** - Native Comms reliability<br>• **Tracking Resiliency Phase 1 & 2** (Nov 2025) - Reduced bugs, race conditions, support impact<br>• **Industry Continuity Solution** - Active (Jena Milan, June 15 update) |

---

## Slide 8: Observability & Operations

| **What We Promised** | **What We Completed** |
|---------------------|----------------------|
| • Alerting and Monitoring improvements<br>• Fix gaps in monitoring<br>• Visibility improvements<br>• DB spike detection<br>• Performance Testing framework<br>• Incident Management maturity<br>• Feature Flagging capability<br>• SLA monitoring<br>• Canary Program | • **CoreX Business Intelligence** (Mar-Sep 2025) - CoreX BI, ABL, ILM, SQS/DQS, DP Backlog visibility<br>• **Heartbeat Configuration Cache** (Sept 2025) - Reduced DynamoDB reads, faster API response<br>• **Canary Program (Document Prediction)** - Kinesis stream monitoring<br>• **CoreX BI Dashboard** - Bulk Load, Doc throughput, Heartbeat visibility<br>• **Org API GitHub Validation** (May 2026) - Automated: person-days → 2 minutes<br>• **Feature Flagging** - Deployed |

---

## Slide 9: Process, Governance & Security

| **What We Promised** | **What We Completed** |
|---------------------|----------------------|
| • Release rigor and change management<br>• All vulnerabilities within SLA<br>• Eliminate EOL technologies (Red Mythos)<br>• CoreX permission audit<br>• Multi-person go-live audit<br>• Testing Maturity improvements<br>• Customer empathy training<br>• Communication improvements | • **Mongo & Spring Library Upgrades** (Aug 2025) - Mongo 8.X support, EOL remediation, vulnerabilities fixed<br>• **SSO: SAML Adapter** (Jan 2026) - Protected Product Help sites<br>• **SSO: Liquibase Improvement** (Nov 2025) - Eliminated release dysfunction from parallel instance conflicts<br>• **Red Mythos Exchange** (In Progress - Aaron) - Vulnerabilities & EOL elimination<br>• **Multi-person go-live audit** - Implemented<br>• **CoreX permission audit** - Completed<br>• **Customer Empathy Training** - Rolled out<br>• **Incident Management Maturity** - Demonstrated June 22-24 |

**Key insight:** 43 completed or in-progress items across all 5 dimensions of resiliency

---

## Slide 10: This Week's Incident - The Case for Transformation

**What happened:**
- CoreX-ALL 2.273.x release → 6 simultaneous production issues
- 21-hour sustained incident response (June 22-23)
- Secondary hotfix rollback incident (June 24)
- AS2 connection failures, BouncyCastle library conflicts, deployment pipeline failures

**Root causes (per Daniel's analysis):**
1. **Monolithic coupling** - change in one area cascades everywhere
2. **Deployment pipeline fragility** - couldn't deploy fixes or rollback easily
3. **Organizational handoff gaps** - 18-month KT failure on DevOps capabilities
4. **Testing environment gaps** - issues not caught pre-production

**Why it validates our strategy:**
- Every root cause is addressed by autonomous teams + continued decoupling
- Can't solve with process alone - need architectural transformation
- Conway's Law in action: organizational structure creates system coupling

**The incident isn't a failure - it's proof we're working on the right problems.**

---

## Slide 11: Current Focus - The Reverse Conway Maneuver

**Strategic bet:** Reorganize teams to force architectural decoupling

**How it works:**
1. **Create small, autonomous teams** (3-5 engineers, cross-functional)
2. **Each team owns a bounded context** (clear domain boundaries)
3. **Teams forced to communicate via APIs** (no shared databases, no shared code)
4. **Conway's Law works FOR us** (team structure drives system architecture)

**Expected outcomes:**
- Resiliency work becomes easier and more organic
- Decoupling happens naturally (teams won't accept coupling)
- Incident blast radius shrinks (changes are localized)
- Development velocity increases (less coordination overhead)
- Testing becomes simpler (smaller, isolated components)

**Current state:**
- Organizational structure in place (4 directors, 12 managers, small teams)
- Now aligning team boundaries to architectural boundaries
- Running in parallel with P0 database work

---

## Slide 12: Current Work - Before Major Capacity Shift

**Priority work in flight:**

**1. Reverse Conway Maneuver** (see previous slide)

**2. Autonomous Teams Enablement**
- Team charters and ownership boundaries
- API contracts and service boundaries
- Self-service infrastructure
- Observability and monitoring per team

**3. Continued Decoupling**
- Breaking monolithic dependencies
- Service extraction from CoreX
- Database separation
- Event-driven architecture patterns

**4. P0 Database Items** (from incident learnings)
- Audit DB reliability improvements
- BT/BD database work
- Data layer metrics and visibility

**Timeline:** Next 3-6 months before significant capacity shift to commercial work

---

## Slide 13: What Remains - The Honest Technical Debt Roadmap

**Infrastructure & Platform:**
- 🔄 Continued DB layer improvements (ongoing)
- 🔜 True Service-Oriented Architecture (SOA)
- 🔜 Replace homegrown Event Bus with enterprise messaging framework
- 🔜 Replace homegrown IdP with Auth0
- 🔜 Kubernetes migration (from monolithic deployment)
- 🔜 Zero-downtime deployment capability

**Operations:**
- 🔜 Automated testing maturity (E2E, integration, chaos engineering)
- 🔜 DR automation (beyond manual drills)
- 🔜 Deployment pipeline standardization (Arshad's accelerated push post-incident)

**Architecture:**
- 🔜 Complete monolith deconstruction
- 🔜 API gateway and service mesh
- 🔜 Event sourcing and CQRS patterns
- 🔜 Multi-region active-active

**Need input from directors on:**
- Priority ordering beyond current commitments
- Resource requirements and timeline estimates
- Dependencies and sequencing

---

## Slide 14: The Narrative - Connecting the Dots

**The transformation story in one page:**

**2024: Heroic Firefighting**
- Large teams, reactive culture, monolithic architecture
- Incidents required all-hands response
- Changes were slow and risky
- Technical debt accumulating faster than we could pay it down

**2025: Building the Foundation**
- Modern org structure (directors, managers, small teams)
- Process improvements (incident management, change management)
- Tactical resiliency work (DB migrations, DR drills, vulnerability management)
- Starting the decoupling work

**2026: Enabling Autonomous Delivery**
- Reverse Conway Maneuver - using org structure to drive architecture
- Teams becoming truly autonomous (bounded contexts, API contracts)
- Resiliency improvements becoming organic (Conway's Law working for us)
- Technical debt roadmap clear and sequenced

**2027: World-Class Engineering**
- SOA fully realized (true service independence)
- High-velocity, low-risk deployments (multiple times per day)
- Incident blast radius contained (service boundaries hold)
- Teams move fast independently (minimal coordination overhead)

**This week's incident is part of the journey - not a detour from it.**

---

## Slide 15: Next Steps & Discussion

**Immediate (this meeting):**
- [ ] Alignment on transformation narrative
- [ ] Confirm priority of autonomous teams work
- [ ] Discuss capacity allocation timeline (tech vs commercial)

**Short-term (next 2 weeks):**
- [ ] Complete June 22-24 incident RCA (Marten/Arshad partnership)
- [ ] Publish blameless postmortem (EOD June 30 per CJ directive)
- [ ] Address GFax reliability concerns (4-8 week issues per Steve Jackson)
- [ ] Launch Arshad's accelerated CI/CD pipeline standardization

**Medium-term (Q3 2026):**
- [ ] P0 database work completion
- [ ] Autonomous team boundaries fully defined
- [ ] First wave of service extractions from CoreX
- [ ] Baseline metrics established

**Long-term (Q4 2026+):**
- [ ] Directors input on extended technical debt roadmap
- [ ] Capacity shift planning (tech → commercial)
- [ ] Multi-year SOA transformation plan

**Discussion questions:**
- How do we balance incident response learnings with forward momentum?
- What's the confidence level on October 8 DR failover?
- When should we communicate this transformation story more broadly?

---

## Appendix: Supporting Materials

**Detailed documentation:**
- Manual Listing of Resiliency Items (this folder)
- Exchange Resiliency Completed.docx (OneDrive)
- Exchange_Plan_Latest.pptx (OneDrive)
- 2026 Tech Org Priorities - Copy.pptx (OneDrive)
- June 22-24 Production Incident materials (vault: 07-Archives/2026-06-22_Production_Incident/)

**Key contacts:**
- Daniel Milburn (Director) - DR, Atlas migration, strategic analysis
- Aaron (Director) - Red Mythos Exchange, vulnerabilities, EOL
- Jena Milan - Industry Continuity Solution status
- Arshad Mahammad (Director) - CI/CD pipeline standardization
- Ramesh Donnipadu (Director) - Incident response, technical execution

---

## Speaker Notes

**Key messages to emphasize:**

1. **Progress is real:** All six resiliency commitments are active/in-progress
2. **Transformation is strategic:** Not just org chart changes - enabling autonomous teams
3. **Incidents validate strategy:** This week proves we're working on the right problems
4. **Honest about debt:** Technical debt roadmap is clear but needs director input
5. **Narrative matters:** Nobody's been telling the transformation story - time to change that

**Tone:**
- Confident but not defensive
- Transparent about challenges
- Forward-looking while acknowledging current state
- Data-driven where possible, honest about gaps

**Handling pushback:**
- "Why another incident?" → This is part of the transformation, not separate from it
- "When will incidents stop?" → As decoupling progresses and teams become autonomous
- "What about commercial work?" → We're planning the capacity shift, but need foundation first
- "Can we move faster?" → Yes, but shortcuts create more incidents (see this week)

**The ask:**
- Alignment on the transformation strategy
- Support for continuing autonomous teams work
- Partnership on communicating this story to broader organization
