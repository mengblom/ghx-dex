---
project_name: Disaster Recovery
status: active
priority: P0
start_date: 2025-12-01
contractual_deadline: 2026-12-31
internal_target: 2026-10-31
owner: Daniel Milburn
executive_sponsor: Marten Engblom
strategic_classification: Big 4 - Critical Technical Execution
capacity_allocation: 25% of Q3 technical work
tags:
  - disaster-recovery
  - resilience
  - RTO
  - contractual-obligation
  - critical-technical-execution
  - Big 4
---

# Disaster Recovery

**One of GHX's "Big 4" strategic initiatives alongside MongoDB Atlas Migration, Red Mythos, and Autonomous Teams.**

## Executive Summary

Disaster Recovery project to achieve multi-region failover capability for Exchange platform with contractual obligation to Cardinal Health. Target: Under 3-hour RTO by December 2026.

**Two Core Objectives:**
1. **Contractual obligation to Cardinal Health** - Conduct DR failover in production (flip and stay) before end of 2026
2. **Operational confidence** - Build genuine capability to recover quickly in real disaster scenarios

**Current RTO:** 7 hours 9 minutes (May 2026 test)  
**Projected RTO (with Atlas + SSO fixes):** 2 hours 15 minutes  
**Target:** Under 3 hours

## Current Status (As of June 1, 2026)

### Recent DR Test Results (May 2026 - "Exchange Incident Games")

**Actual Performance:**
- **Total RTO:** 7 hours 9 minutes (missed initial 4-hour target)
- **Breakdown:**
  - 2.5 hours: Database restoration (pre-drill, not counted initially)
  - 4 hours 45 minutes: Day 1 drill execution
  - Additional time: Day 2/3 SSO troubleshooting and API rebuilding

**RTO Projection Analysis (with infrastructure modernization):**
- Current actual: **7h 9m**
- With Atlas migration alone: **4h 39m** (eliminates 2.5h database restore)
- **With Atlas + SSO fixes: 2h 15m** ✅ (well under 3-hour target)
- **Strategic decision: Accept current RTO projections as meeting contractual obligation**

### Key Failures Identified
1. **Bamboo plans outdated** - Inconsistent with current state
2. **Stage vs. production environment gaps** - Requires documentation
3. **DNS Service/SSO issues** - Spent entire extra day troubleshooting
4. **Undocumented User API** - Had to be rebuilt mid-incident
5. **Route 53 not pre-staged** - Manual updates required
6. **Lambda cold starts** - Stage Lambdas expire if not exercised regularly
7. **Heavy reliance on specific people** - "Scary" level of human risk

### Time Additions Identified
- Name Drift: 30 minutes
- SSO Coordination: 44 minutes + 2 hours troubleshooting
- Waiting for Verbal Confirmations: No automated readiness checks
- Manual CloudFront/DNS Updates: ~30 minutes

## Strategic Context

### Big 4 Framework (Q3 2026)
Disaster Recovery is one of four interdependent strategic initiatives representing 75% of engineering capacity:

1. **Red Mythos / Vulnerabilities** (25% capacity)
2. **Disaster Recovery** (25% capacity) ← This project
3. **Autonomous Teams / Breaking the Monolith** (50% capacity)
4. **MongoDB to Atlas Migration** (integrated with DR)

### Contractual Obligation Details
- **Customer:** Cardinal Health (major strategic customer)
- **Requirement:** "Flip and stay" exercise in production
- **Deadline:** December 2026 (non-negotiable)
- **Executive visibility:** Cardinal escalates to investor level; daily PowerPoints on incidents/DR/everything
- **Real operational resilience** - Confidence we can recover if needed
- **RTO target:** Under 3 hours

## Timeline & Milestones

### Q2 2026 (Current)
- ✅ **May 4-8:** Exchange Incident Games (lower environment test)
  - Initial assessment: 4h 45m (revised to 7h+)
  - Identified SSO and database restore bottlenecks
  - Revealed coupling between systems and human dependencies

### Q3 2026 (June-August)
- **End of August:** Atlas migration completion (target)
- **June-July:** Elasticsearch migration (enables 2h+ RTO reduction)
- **Mid-September:** Full DR test including Fusion, SCA, CCX (all dependent products)
- **Internal DR capability ready by October**

### Q4 2026 (October-December)
- **October 2026:** Internal production DR test (flip and stay) 🎯
- **December 2026:** Contractual deadline - production flip and stay with Cardinal Health 🎯

## Technical Approach

### RTO Reduction Strategy

#### Root Cause Analysis of 7-Hour Current State:

**1. Database restoration: 2.5 hours**
- **Solution:** Atlas migration (managed MongoDB → MongoDB Atlas)
- **Benefit:** Replace restore with secondary promotion
- **Timeline impact:** -2.5 hours
- **Status:** In progress, target end of August 2026
- **Risk:** May 29 STG attempt failed (retrying June 3)

**2. SSO troubleshooting: 2+ hours**
- **Solution:** Automate SSO deployment scripts
- **Root issue:** Undocumented User API, dependency on specific individuals
- **Timeline impact:** -2 hours
- **Status:** SSO team working on scripts, testing before September

**3. Manual infrastructure updates: ~30 minutes**
- CloudFront updates, DNS Route 53 changes, Name drift issues
- **Solution:** Automated runbooks and pre-staging
- **Status:** Runbook extraction from transcripts ongoing

**4. Coordination overhead: ~44 minutes**
- Verbal confirmations instead of automated checks
- Waiting for people to complete portions
- **Solution:** Automated readiness checks

### Key Technical Gaps Discovered

**SSO-Specific Issues (44 min + 2h):**
- Undocumented User API had to be rebuilt mid-incident
- SSO team is decoupling SSO from org data dependencies (SMTP config, etc.)
- Making pragmatic decisions: Leave data with Org temporarily
- Once application boundaries clear, can tackle persistence layer

**Manual Dependencies - "Scary" Level Human Risk:**
- Heavy reliance on 2-3 specific people for troubleshooting
- No automated readiness checks
- Verbal confirmations vs. automated validation
- **Solution:** Document all procedures and reduce individual dependencies

**Stage/Production Gaps:**
- Bamboo plans from December inconsistent with current state
- Some differences need clear documentation before October prod test
- STG must match PROD topology to catch production-class issues

### Infrastructure Modernization Dependencies
- **Atlas migration** (end of August): Eliminates database restore, enables secondary promotion
- **Elasticsearch migration:** Performance optimization
- **Automated runbooks:** Reduces manual steps and human coordination

## Ownership & Governance

### Ownership Model

**Execution Owner:**
**[[Daniel_Milburn]]** (Senior Director)
- Drives the work and coordinates teams
- Tracks progress and runs DR steering committee
- Owns domain definition and team coordination
- Assesses if current DR roadmap can be scoped to August timeline

**Strategic Direction:**
**Marten Engblom** (VP Engineering, Executive Sponsor)
- Sets strategic direction and priority calls
- Makes resource allocation decisions
- Communicates with leadership and CJ
- Final decisions on team topology changes
- Protects the work from competing priorities

### Key Team Members
- **Pete Ferguson** - Facilitates DR exercise readouts, leadership perspective
- **[[Philippe_Scoffie]]** - Project Lead for MongoDB Atlas Migration (critical dependency)
- **[[Jeff_Sherard]]** - Principal DBA, database architecture and RTO feasibility
- **Pratik Panchal** - SSO team lead, decoupling identity from org data
- **Adam Gordon** - Org team, lift-and-shift feasibility assessment
- **[[Suresh_Kumar]]** - Senior IC, application architecture & code changes
- **Gregory Bank** - Voice of team PTSD on past failed attempts (cautiously optimistic)

## Key Dependencies

### Atlas Migration (Critical Path) 🔴
- **Status:** In progress, target completion end of August 2026
- **Impact:** Eliminates 2.5 hours from RTO (7h 9m → 4h 39m)
- **Scope:** BusinessTransaction, BusinessDocument, BusinessMetric databases
- **Risk:** May 29 STG attempt failed (database naming conflict, retrying June 3)
- **Executive Sponsor:** Curtis Nielsen
- **Without Atlas:** Cannot meet 3-hour RTO target
- **With Atlas + SSO fixes:** 2h 15m RTO achievable

See: [14-MongoDB_Atlas_Migration](../14-MongoDB_Atlas_Migration/README.md)

### Elasticsearch Migration
- **Status:** In progress, integrated with Atlas effort
- **Impact:** Performance optimization (enables 2h+ reduction in RTO projections)

### Autonomous Teams / Breaking the Monolith (Shared Infrastructure Needs)
**Critical Connection:** DR automation requirements overlap heavily with autonomous teams infrastructure

- **Teams need:** Infrastructure as Code, automated deployment pipelines, independent deployments
- **DR needs:** Automated runbooks, infrastructure as code, rapid spin-up capabilities
- **Strategic insight:** "If we push pedal to metal on decoupling/autonomous teams, we get DR automation for free"

**Q3 Strategy:** GitHub migration is Q3 primary decoupling vehicle
- Every team moves to independent repos + deployment pipelines
- DR automation, decoupling, and autonomous teams all achieved together
- Phase 0: Teams own merges and deployments (even with code still in monolith)

See: [13-Autonomous_Teams](../13-Autonomous_Teams/README.md)

### GitHub Migration as Q3 Primary Vehicle
- Alternative to focusing solely on DR automation
- "If all 12 teams made a copy of the monolith, it's STILL better than where we are today"
- Lift and shift approach: Teams don't need perfect SOA initially, just autonomy
- Expected to deliver DR automation as byproduct

## Relationship to Autonomous Teams

### Strategic Overlap
The May 8 Incident Games readout revealed that **autonomous teams are the #1 organizational unlock:**
- Everything becomes easier after decoupling, even if first pass is imperfect
- Two approaches debated:
  1. **DR-First:** Automate current gaps, decouple later
  2. **Decouple-First:** Prioritize monolith breakup, DR capabilities come as byproduct
- **Hybrid/Emerging Consensus:** Start decoupling now, pivot to DR prep if tracking poorly mid-quarter

### Lift and Shift Strategy (May 8 Decision)
- Each team copies what they need from monolith (overlapping Venn diagrams OK initially)
- Accept temporary code duplication across teams
- Data layer coupling remains initially (tackle later)
- Goal: Get to independently deployable state "at any cost"
- Teams define their domains down to folder/component level by May 18
- Domain review sessions week of May 18

### Consensus Points from May 8 Meeting
1. **#1 Priority:** Get to autonomous team state - "everything becomes easier"
2. **Accept Imperfection:** First pass will be messy, duplicated code OK
3. **Data Layer Separate:** Don't tackle database decoupling in Phase 1
4. **Domain Definition Critical:** Need boundaries down to folder/component level
5. **Product Alignment:** Laura fully supportive - "Take capacity you need"
6. **Learn as We Go:** Cross bridges when we get there vs. waterfall planning

## Team Concerns & Reality Check

### Gregory Bank's PTSD (Cautiously Optimistic)
- "This is about the 5th or 6th time we've heard all this"
- Previous attempts: Full prep, then nothing - rug gets pulled out
- **Key Frustration:** Too many competing #1 priorities
- **Needs:** Consistent messaging and protected capacity

### Leadership Commitment (Pete Ferguson)
- "This time IS different" - new leaders have done this before at other orgs
- Heavy investor scrutiny - daily PowerPoints on incidents, DR, everything
- **"This train is moving"** - not stopping this time
- Acknowledges team PTSD is real and valid

### Suresh Kumar's Integration Concerns
- Integration complexity: Even isolated services need to integrate with rest of Exchange
- Example: Adapter API built fast but integration took year+ due to priorities
- Relationship validation changes ripple across 10+ places
- **Counter:** Acceptable trade-off for autonomy

### Piyush Srivastava's Domain Design Perspective
- Need proper domain modeling first
- IO team should own document data, provide APIs to others
- Current library-based sharing creates tight coupling
- Takes long time, but necessary prerequisite

### Matthew Turner's Boundary Clarity Problem
- "Teams don't understand what they own and what they don't own"
- Example: Actions + Transformations teams have crossover
- Product doesn't understand boundaries either - get requests for wrong teams
- **Critical Need:** Define boundaries down to folder level in mono repo

## Executive Context & Communications

### Strategic Importance (Big 4 Framework)
One of 4 critical strategic initiatives (reshaped as "Big 4" in Q3):
1. Red Mythos / Vulnerabilities (must-do)
2. **Disaster Recovery** (must-do, this project)
3. Autonomous Teams / Breaking the Monolith (biggest unlock)
4. MongoDB to Atlas Migration (integrated)

### Capacity Allocation (Q3 Guidance)
- **25% commercial work**
- **75% technical work**, which should roll up to one of the Big 4
- All line items must have "Technical Initiative" filled in

### CJ Singh (CTO) Context
- Pushing for team-level metrics (can't do without clear team boundaries)
- Customer-facing communications on productivity, resiliency, capacity
- Three deliverables for executive review:
  1. Productivity state
  2. Resiliency status
  3. Capacity roadmap
- Emphasized need for clear "good enough interim state" definition

### Marten's Q3 Messaging
- "We're spending 75% on technical work, 25% on commercial"
- "Before we shift that balance, we need to get to better state technically"
- "DR deadline is October internally, December contractually"
- "GitHub migration is Q3 primary vehicle for decoupling"

## Related Documents

### Primary Project Documentation
- `/04-Projects/12-Disaster_Recovery/README.md` - This file

### Meeting Notes & Readouts
- `/00-Inbox/Meetings/2026-05-08/Exchange_Incident_Games_2026_READOUT.md` - Comprehensive readout with RTO analysis
- `/00-Inbox/Meetings/2026-05-08/Exchange_Incident_Games_2026_READOUT_TRANSCRIPT.md` - Full transcript (874 lines)
- `/00-Inbox/Meetings/2026-05-08/Road_to_Autonomy_Github_Migrations.md` - Connection between DR, autonomous teams, GitHub
- `/00-Inbox/Meetings/2026-05-07/2026-05-07 - Exchange DR Gap Remediation Check in.md` - RTO reduction analysis

### Daily Notes & Reviews
- `/00-Inbox/Daily_Reviews/2026-05-07.md` - Breakthrough RTO analysis (7h 9m → 2h 15m projected)
- `/00-Inbox/Daily_Reviews/2026-05-08.md` - DR readiness validation post-Incident Games

### Strategic Planning
- `/00-Inbox/Ideas/Q3_Roadmap_Planning_Communications.md` - Q3 capacity allocation rules (Big 4 framework)
- `/02-Week_Priorities/Q2_Pillar_Breakdown.md` - Q2 priority breakdown including DR milestone

### Critical Dependencies
- [14-MongoDB_Atlas_Migration](../14-MongoDB_Atlas_Migration/README.md) - Atlas migration status
- [13-Autonomous_Teams](../13-Autonomous_Teams/README.md) - Autonomous teams roadmap and overlap

### CJ Presentation Materials
- `/04-Projects/21-Exchange_Modernization_Report_May_2026/CJ_Feedback_and_Slide_Outline.md` - Executive communication on DR

## Open Questions & Risks

### Open Questions
1. **Database migration to Atlas timeline?** (Target: end of August, but May 29 STG failure caused delay)
2. **How much DR work is truly independent vs. part of autonomous teams decoupling?** (Answer emerging: Very little - lift and shift approach makes them interdependent)
3. **Who owns runbook automation - DevOps? Teams themselves?** (Still being clarified)
4. **Can all 12 teams execute lift-and-shift by October?** (Concern: competing priorities, team PTSD)
5. **Will stage/prod differences be documented in time for October test?** (Critical path item)
6. **How do we reduce "if Banks goes on vacation for 2 weeks" single-person risk?** (Need documentation and automation)

### Top Risks

#### 1. Atlas Migration Delay - CRITICAL 🔴
- May 29 STG attempt failed (database naming conflict)
- Retry scheduled June 3
- Without Atlas, cannot achieve 3-hour RTO target
- Could jeopardize October internal timeline

#### 2. Human Dependency on Key People
- Team PTSD from past failures affecting confidence
- Need consistent messaging and protected capacity
- SSO troubleshooting required specific individual expertise

#### 3. Competing Priorities & Priority Whiplash
- Gregory Bank: "Too many competing #1 priorities"
- Risk: Rug gets pulled out like past attempts
- Mitigation: Leadership protection and transparent capacity allocation

#### 4. Autonomous Teams vs. DR Sequencing
- Unclear if decoupling work delivers DR capabilities fast enough for October deadline
- May need to run parallel efforts vs. pure lift-and-shift approach

#### 5. Stage/Production Parity
- Gaps between stage and production discovered in test
- Could cause October test to fail if not addressed
- Requires clear documentation and alignment

### Mitigation Strategies

**For Atlas Dependency:**
- Fast-track the June 3 retry
- Have fallback plan for manual database operations if needed
- Clear handoff points between Atlas and DR teams

**For Human Dependencies:**
- Aggressive runbook documentation and testing
- SSO team focus on script automation before September
- Coordinate with SSO team on confidence-building test schedule

**For Priority Protection:**
- Q3 capacity allocation framework (25/75 commercial/technical)
- Big 4 framework ensures focus
- Leadership accountability for shielding from shifts

**For Stage/Prod Alignment:**
- Document all stage/prod differences before October
- Make STG match PROD topology to catch production-class issues
- Require production-like testing for critical systems

## Next Steps (Action Items)

### Immediate (Next 1-2 weeks)
- [ ] **Atlas retry June 3** - STG + PERF BT/BD cutover (critical path)
- [ ] **SSO deployment scripts testing** - Individual script testing before September
- [ ] **Domain definition by teams** - Down to folder/component level
- [ ] **Stage/production differences documentation** - Before October test
- [ ] **Automation epic ROI analysis** - Prioritize high-impact items

### Mid-term (June-August)
- [ ] **Mid-September full DR test** - Including Fusion, SCA, CCX (all dependent products)
- [ ] **GitHub migration planning** - Q3 primary vehicle for autonomous teams + DR automation
- [ ] **Domain review sessions** - Week of May 18 (sanity check boundaries)
- [ ] **Weekly planning meetings** - Maintain momentum on decoupling work
- [ ] **Atlas/Elasticsearch migrations complete** - End of August (critical for RTO targets)

### Pre-October Test
- [ ] **October production DR test** - Internal "flip and stay" exercise
- [ ] **Runbooks extraction from transcripts** - Replace back-and-forth with clean step-by-step
- [ ] **Runbook migration to GitHub** - Better collaboration and version control
- [ ] **Confidence-building test schedule** - Regular SSO team testing cadence

### December Delivery
- [ ] **December production flip and stay** - Contractual deadline with Cardinal Health

## Success Metrics

### Primary Metrics
- **RTO:** Under 3 hours (target: 2h 15m with Atlas + SSO fixes)
- **Automated runbook coverage:** 90%+ of procedures
- **Manual coordination overhead:** < 30 minutes
- **Single-person dependencies:** Zero critical paths

### Health Indicators
- Stage/prod environment parity: 100%
- SSO deployment scripts: Fully automated
- Database failover time: < 30 seconds (with Atlas secondary promotion)
- Readiness checks: Automated (no verbal confirmations)

---

**Last Updated:** June 1, 2026  
**Next Review:** Weekly (DR Steering Committee)  
**Internal Target:** October 2026  
**Contractual Deadline:** December 2026
