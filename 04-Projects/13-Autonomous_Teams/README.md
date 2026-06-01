---
project_name: Autonomous Teams / Breaking the Monolith
status: active
priority: P0
start_date: 2026-05-28
foundation_target: 2026-07-31
execution_phase: 2026-10-01
owner: Mike Mitchell
executive_sponsor: Marten Engblom
strategic_classification: Big 4 - Critical Technical Execution
capacity_allocation: 50% of Q3 technical work (dominant by Q4)
tags:
  - autonomous-teams
  - monolith
  - decoupling
  - organizational-transformation
  - critical-technical-execution
  - Big 4
---

# Autonomous Teams / Breaking the Monolith

**One of GHX's "Big 4" strategic initiatives - expected to become THE dominant priority in Q4 2026.**

## Executive Summary

Transform Exchange engineering from monolithic, coordinated deployments to autonomous teams with clear domain ownership, independent deployments, and self-service capabilities.

**The Problem:**
- Monolithic architecture creates deployment dependencies
- Teams can't ship independently → slower velocity, coordination overhead
- Shared ownership → diffuse accountability
- Monthly release cycles with 2+ week testing
- 100 engineers coordinating across 19 products and 57 applications

**The Vision:**
- Each team (5-10 engineers) owns clear domain end-to-end
- Teams deploy independently without coordination ("master of your domain")
- Clear metrics at the team level
- Deployment frequency: Monthly → Daily (eventually multiple times daily)
- Faster time-to-market, clearer accountability

## Current Status (As of May 28, 2026)

**Phase:** Foundation building (formal handoff to Mike Mitchell completed May 28)  
**Next Milestone:** End of next week (early June) - JIRA spaces + domain definitions

### What Exists ✅
- **Team Standards Framework** - In progress, being finalized (Mon/Tue in Denver, early June)
- **Matt Turner's Domain Ownership Page** - Initial domain mapping
- **Team Catalog** - Started (incomplete, Aaron asking teams to fill out)
- **JIRA Sandbox Project** - Aaron testing native team spaces for metrics
- **Some Teams Ahead** - Visibility team has already named services to carve out
- **Exchange Team Standards Document** - SharePoint doc outlining autonomy standards

### What's In Progress 🔄
- Defining baseline JIRA space template (Mike + Christine Zhou)
- Aaron planning JIRA instrumentation for automated team metrics (2-week timeline)
- DevOps coordination for team automation needs
- Domain breakdown spreadsheet/template (Aaron + Ben + Matt Turner)

### What's Missing ❌
- **Most teams haven't defined their domains yet** - Don't know boundaries, coupling points, target architecture
- **No timeline/cadence for team sessions** - Mike scheduling working sessions
- **Cross-team ownership ambiguities** - Will surface as teams do the work
- **Formalized tracking mechanism** - How to track which teams are done vs stuck
- **Weekly checkpoint cadence** - Marten/Mike regular sync not yet scheduled
- **Clear escalation path** - For cross-team conflicts not yet defined

## Strategic Context

### Big 4 Framework (Q3 2026)
Autonomous Teams is one of four interdependent strategic initiatives:

1. **Red Mythos / Vulnerabilities** (25% capacity) - Must complete to free capacity
2. **Disaster Recovery** (25% capacity) - Shares infrastructure needs
3. **Autonomous Teams / Breaking the Monolith** (50% capacity) ← This project (THE dominant focus by Q4)
4. **MongoDB to Atlas Migration** - Integrated with DR

**Capacity Evolution:**
- **Q3 2026:** 50% of technical capacity (75% total technical work)
- **Q4 2026:** Dominant focus (Red Mythos wrapped, DR in maintenance mode)

### Why Now
- **Q3 capacity allocation:** 75% technical work must support Big 4, autonomous teams as biggest unlock
- **CJ pushing for team-level metrics** (can't do without clear team boundaries)
- **Native JIRA spaces coming** → each team needs defined scope
- **Overlaps with DR automation needs** (Infrastructure as Code, automated deployments)
- **GitHub migration** can't happen before decoupling (would tank team metrics)

### Q3 Planning Guidance (Sent May 28)
All technical work in Q3 should roll up to one of the Big 4. Added "Technical Initiative" column to Q3 planning forcing explicit priority naming.

**Capacity Split:** 25% commercial, 75% technical (supporting Big 4)

## Ownership Model (May 28 Handoff)

### Mike Mitchell Owns (Execution)
- Coordinating execution cadence with teams
- Scheduling team sessions to work through domain definition
- Tracking progress on deliverables (documented boundaries, coupling maps, target architecture)
- Surfacing blockers and cross-team conflicts to Marten
- Working with Aaron on JIRA space setup aligning with team domains
- Ensuring teams understand next steps and have what they need
- **Reports to:** Marten Engblom
- **Direct reports:** 2 (User Platform, Organization Platform teams)

### Marten Engblom Owns (Direction)
- Setting strategic priorities and capacity allocation (25/75, Big 4)
- Resolving ambiguous ownership questions between teams
- Final decisions on team topology changes if needed
- Communication to leadership and CJ on progress
- Connecting this work to DR, Red Mythos, and broader tech strategy
- Formal checkpoints with Mike (to be scheduled - needs follow-up)

### Supporting Cast
- **[[Aaron_Srivastava]]** - JIRA space setup, team metrics instrumentation, domain breakdown template
- **[[Daniel_Milburn]]** - Coordination on DR/autonomous teams overlap, team leadership
- **Christine Zhou** - JIRA baseline space template definition
- **Matt Turner** - Domain ownership documentation
- **Ben Ludkiewicz** - Domain breakdown spreadsheet support
- **Ramesh Donnipadu** - Team coordination (Exchange Mapping, Document Understanding, Visibility, Continuity Assure)

## Phased Approach (3-Phase Strategy)

### Phase 0: Deployments and Merges First (Quick Win)

**Goal:** "Master of your domain" - independent control without full code separation yet

**What happens:**
- Teams own their own merge process (no more cross-team merge coordination)
- Teams own their deployment pipelines (even if code stays in monolith temporarily)
- Each team controls what gets deployed to their services
- Reduced merge coordination overhead

**Why this first:**
- Fastest path to reducing coordination overhead
- Builds team confidence and autonomy muscle
- Doesn't require architectural changes yet
- Measurable quick win

**Outcome if successful:**
- Deployments that are per-team-owned instead of org-wide coordinated
- Visibility team model: Can deploy Exchange Automation without deploying entire All repo

### Phase 1: Code Separation

**What happens:**
- Move components to GitHub
- Independent deployments with GitHub Actions
- Infrastructure as Code for all team-owned infrastructure
- Teams own repos, pipelines, and deployment automation
- Clear team-owned services and their APIs

**What stays shared:**
- **Data can stay shared for now** - Not the immediate blocker
- **Exception:** If data is unquestionably owned by one team and no one else touches it, take it now in Phase 1

**Why defer data:**
- Data changes don't happen as frequently as code changes
- Shared databases not the primary deployment blocker
- Will be tackled in Phase 2 when teams have more autonomy muscle

### Phase 2: Data Separation (Later)

**What happens:**
- Decouple shared databases
- Each team owns their data
- Clear data boundaries and contracts
- Data contracts between services (APIs for data access)

**Timeline:**
- Not in initial scope - will be Phase 2 work
- "Very quick follow phase" if possible sooner than planned

### Key Principle:
**Phase 0/1 doesn't require perfect microservices architecture.** Acceptable intermediate state: **mini-monoliths per team** (e.g., "deploy all of Exchange Automation" is way better than "deploy entire All repo")

## The Playbook: What Teams Must Do

Each team works through these four areas:

### 1. Define Your Domain
- What's in scope? What's out of scope?
- Where are boundaries fuzzy or overlapping with other teams?
- What business capabilities do you own?
- **Deliverable:** Lucid chart or Confluence page documenting domain
- **Format:** Functional level - "what belongs to which team"
- **Effort:** 1-2 sessions, getting input from team

### 2. Map Current Coupling Points
- How are you tied to the monolith or other services?
- Shared repos? Direct code dependencies? Shared databases?
- What forces you to coordinate deployments?
- **Deliverable:** Documented coupling map
- **Format:** Visual diagram or table showing dependencies and severity
- **Effort:** Requires investigation and cross-team discussions

### 3. Identify Deployment Blockers
- What specifically prevents you from deploying independently today?
- Shared infrastructure? Shared data? Orchestration dependencies?
- Severity: What's showstopper vs what's just friction?
- **Deliverable:** List of blockers with severity/effort estimates
- **Format:** Prioritized list with estimation
- **Effort:** 2-3 hours analysis per team

### 4. Document Target Architecture
- What does your independently deployable future state look like?
- What services will you create? What APIs will you expose?
- What data will you own?
- **Deliverable:** Target architecture diagram (Lucid chart)
- **Format:** Visual showing proposed services, boundaries, data ownership
- **Effort:** Design session + documentation

### By Mid-Q3 (End of July 2026), Every Team Should Have:
1. ✅ Documented domain boundaries
2. ✅ Current coupling points mapped
3. ✅ Target architecture documented
4. ✅ A plan to break free of the monolith (doesn't have to be executed, but clear direction)

## Timeline & Immediate Next Steps

### End of Next Week (Early June 2026) - TACTICAL MILESTONES:
- ✅ **JIRA spaces created** (blank, ready for teams to use)
- ✅ **Simplified workflow aligned** (teams can customize on top of template)
- ✅ **Beta version of team domain definitions** (functional level - what belongs to which team)
- ✅ **Team standards finalized** (finishing working session with same group + Anand)

### Mid-Q3 2026 (July 2026) - STRATEGIC MILESTONES:
- ✅ All teams have documented domains, coupling maps, target architecture, and decoupling plans
- ✅ Cross-team ownership conflicts identified and resolved
- ✅ Foundation set for Q3/Q4 decoupling execution work
- ✅ Teams excited about the change, not just compliant

### Q4 2026 and Beyond - EXECUTION PHASE:
- Autonomous teams becomes THE dominant engineering focus
- Red Mythos wrapped, DR in maintenance mode
- Teams actively decoupling, moving to GitHub, establishing independent deployments
- Phase 0 work happening (deployments/merges), Phase 1 starting (code)
- Expected to dominate 100% of technical work by November/December 2026

## May 28 Handoff Meeting Outcomes

### Key Agreements Reached

**1. Ownership Confirmed**
- Mike owns execution of autonomous teams (initial phase)
- In a few months, everyone will likely pile onto it
- Aaron owns Red Mythos, Daniel owns DR

**2. Phased Approach Confirmed**
- Phase 0: Deployments and merges first (Mike's idea)
- Phase 1: Code separation
- Phase 2: Data separation
- Insight: If data unquestionably owned by one team, take it now

**3. Immediate Next Steps Agreed**
- Finish team standards (working session Mon/Tue in Denver)
- Define team domains (teams create Lucid charts)
- Create new JIRA spaces (blank, by end of next week)
- Simplified workflow aligned (one workflow teams can customize)

**4. Timeline Set**
- End of next week: JIRA spaces + simplified workflow + beta domain definitions
- Some teams already ahead (Visibility team identified services)

**5. Concerns Flagged**
- JIRA project ID changes will break external integrations/reports (forcing function to clean up homegrown integrations)
- Backlog pruning resistance (teams reluctant to "hatchet" 3+ year old tickets)

**6. Mike's Excitement Level: HIGH**
- Quote: "This is going to be such a huge difference maker... a game changer"
- Quote: "Think about deploying changes every day that you couldn't do for a month before"
- "I don't know how anybody could stay working on the product the way it is today"

### What Wasn't Covered (Needs Follow-Up):
- **Tracking mechanism** - How Mike will track team progress (Jira epic? Confluence? Spreadsheet?)
- **Weekly checkpoint cadence** - Regular Marten/Mike sync not discussed
- **Coordination with Aaron** - JIRA space setup alignment with domain definitions
- **Pilot vs full rollout** - Should we start with 1-2 teams or all teams?
- **Staff meeting socialization** - Should this be presented in staff meeting first or just execute?

### Committed Actions from Meeting:

**Mike's Immediate Next Steps:**
- [ ] Schedule working session to finish team standards (Mon/Tue in Denver, same group + Anand)
- [ ] Review Matt Turner's domain ownership page
- [ ] Coordinate with teams on creating Lucid chart domain definitions
- [ ] Drive completion of JIRA spaces + simplified workflow by end of next week
- [ ] Book dinner with Marten, Daniel, Aaron on Monday (first time all together in Denver)

**Marten's Immediate Next Steps:**
- [ ] Send "Breaking the Monolith" communication to teams (Friday, May 31)
- [ ] Update Exchange Team Standards doc (metrics section, team next steps)
- [ ] Coordinate dinner arrangements for Monday
- [ ] Schedule 30-min follow-up with Mike after working session

## Team Structure & Autonomy Principles

### Target Exchange Organization

**Product Teams (Stream-Aligned):**
1. Exchange IO
2. Exchange Core
3. Exchange Analytics
4. Exchange Actions & Rules
5. Exchange Mapping
6. Exchange Customer Enablement
7. Exchange Document Understanding
8. Exchange Customer Visibility
9. Organizations Platform (Mike Mitchell's team)
10. Users Platform (Mike Mitchell's team)
11. Continuity Assure

**Enabling Teams:**
- Developer Platform & AI Enablement (Director level hire needed)
- Data Architecture & Engineering (Principal Engineer hire needed)

**Complicated Subsystem Teams:**
- Exchange Performance Environment

### Team Composition Model
- **5-7 engineers per team** (player-coach EM + 4-6 ICs)
- **Cross-functional:** Full-stack capabilities within team
- **Owns end-to-end:** UI, APIs, services, data, deployment
- **Player-coach EM:** 60-70% individual contribution, 30-40% people management

### Core Principle: Reverse Conway Maneuver
- Organization structure should follow desired architecture, not vice versa
- Teams organized around business capabilities produce decoupled services
- Teams organized around technical layers (UI, API, DB teams) produce layered dependencies
- **Form teams around target architecture and domain boundaries**

## Metrics & CJ Context

### Why Metrics Matter
- **CJ Singh** (leadership) asking for team-level metrics, not just pod-level
- Current dashboard tracks incidents (BROKEN tickets) at pod level only
- Can't measure team autonomy without clear team boundaries
- Native JIRA projects per team will enable team-level metrics

### Metrics Phase Implementation

**Phase 1 - Available Now (Bitbucket DC):**
- Deployment Frequency (JIRA Deployment Insights)
- Lead Time / Cycle Time (JIRA Cycle Time Report)
- Sprint velocity, WIP, Issue cycle time (native JIRA reports)
- Security metrics (Wiz/Xray auto-creating tickets in team JIRA)

**Phase 2 - After GitHub Migration:**
- Full Compass DevEx dashboard (Deployment Frequency, Build Success Rate, Build Time, PR Cycle Time, Open PRs)
- MTTR via PagerDuty integration
- Change Failure Rate (Compass - configuration in progress)

### Requirements for Team-Level Metrics
- Native JIRA projects per team (not boards pulling from everywhere)
- CI/CD pipelines sending deployment events to JIRA
- JIRA issue keys in branch names, commit messages, PR titles
- 4 weeks of data before rolling averages display

### CJ's Questions Being Addressed
- "What metrics track effectiveness of your teams?" → Team-level DORA metrics
- "Where are software defects being tracked?" → Security findings in JIRA + bug categorization
- "What about first-pass yield (bugs that leak testing)?" → Native Jira projects enable better defect tracking

## Connection to Other Strategic Initiatives

### Red Mythos / Vulnerabilities
- **Owner:** Aaron Srivastava
- **Status:** Must-do initiative
- **Impact on Autonomous Teams:** Low - parallel track
- **Expected completion:** Early Q3, frees up capacity for autonomous teams

### Disaster Recovery (DR)
- **Owner:** Daniel Milburn
- **Status:** Must-do initiative
- **Impact on Autonomous Teams:** HIGH - shares infrastructure needs (IaC, automated deployments)
- **Sequencing concern:** Can't parallelize IC-level work (both touch deployment automation)
- **GitHub Migration Implication:** DR work + autonomous teams both need GitHub Actions

**Critical Connection:** "If we push pedal to metal on decoupling/autonomous teams, we get DR automation for free"

See: [12-Disaster_Recovery](../12-Disaster_Recovery/README.md)

### MongoDB to Atlas Migration
- **Impact:** Atlas migration (end of August) improves DR RTO, enabling autonomous teams infrastructure work
- **No direct blocker** to autonomous teams work

See: [14-MongoDB_Atlas_Migration](../14-MongoDB_Atlas_Migration/README.md)

### GitHub Migration
- **Current Status:** Lower priority than DR/Vulnerabilities/Decoupling/DB migrations
- **Timeline:** Curtis confirmation - "If it takes longer than October, it takes longer than October"
- **Key Insight from Aaron:** Lift-and-shift from Bitbucket to GitHub before decomposition will tank team metrics
- **Sequence:** Decoupling first, GitHub migration second (not before)

## Known Risks & Concerns

### 1. Backlog Pruning Resistance
- Teams reluctant to "hatchet" 3+ year old tickets when moving to new JIRA spaces
- Resistance: "It's still a valid problem"
- **Counter:** If not touched in 3 years and no one's complaining, probably should be archived
- Moving to new JIRA spaces is forcing function to clean up

### 2. JIRA Integration Breakage
- New project IDs will cause external reports/integrations to have missing data
- Will surface homegrown integrations that should be retired anyway
- **Side benefit:** Forces discovery and cleanup of shadow integration infrastructure

### 3. Unknown Coupling Discovery
- Teams will discover coupling they didn't know about when mapping dependencies
- Will surface cross-team ownership ambiguities
- Requires escalation path to Marten for resolution

### 4. Perfectionism Trap
- Teams might try to design perfect microservices architecture (wrong goal)
- **Correct approach:** Mini-monoliths per team are acceptable intermediate state
- Goal is independence, not perfect bounded contexts

### 5. Organizational Readiness
- Teams newly formed, some still hiring (25+ open roles including 3 managers)
- Organizational research: Teams go through forming/storming/norming before peak performance
- Data collected now = baseline during transition, not steady-state capability
- Need to manage CJ expectations on metrics stabilization timeline

## Immediate Questions Still Pending

### For Mike:
- What format for team deliverables? (Confluence pages? Lucid diagrams? Both?)
- How to handle teams already ahead (like Visibility)?
- What's the escalation path for cross-team ownership conflicts?
- What support does Mike need from Marten to be successful?

### For Both Mike and Marten:
- Should we pilot with 1-2 teams first, or roll out to all teams at once?
- What's the right cadence for Marten/Mike checkpoint meetings? (Proposed: weekly 15-30 min)
- Should this be socialized in staff meeting first, or just start executing?
- What's the tracking mechanism for team progress? (Jira epic? Spreadsheet? Confluence?)

## Related Documents

### Primary Documents
- `/04-Projects/13-Autonomous_Teams/README.md` - This file
- `/00-Inbox/Meetings/2026-05-28 - Autonomous Teams Handoff - Mike Mitchell - Transcript.md` - Full meeting transcript
- `/00-Inbox/Meetings/2026-05-28 - Autonomous Teams Handoff - Mike Mitchell.md` - Meeting summary with outcomes

### Strategic Documents
- `/00-Inbox/Ideas/Q3_Roadmap_Planning_Communications.md` - Q3 capacity guidance (25/75 split, Big 4)
- `/00-Inbox/2-Day_Focus_May_28-29.md` - May 28-29 execution focus plan
- `/00-Inbox/Daily_Reviews/2026-05-28.md` - Daily review with full context

### Exchange Team Strategy
- `/04-Projects/23-Automation_Team_Vision_and_Strategy/Exchange - Building Autonomous Teams.md` - Principles and vision
- `/04-Projects/23-Automation_Team_Vision_and_Strategy/Exchange Team Strategy/Plan Deck/Exchange - New Organization Deck.md` - Detailed org structure

### Metrics & CJ Context
- `/04-Projects/21-Exchange_Modernization_Report_May_2026/2026-05-29 CJ Follow-up Call/Preparation/Email_to_CJ_Metrics.md` - Team-level metrics implementation plan
- `/00-Inbox/Temp/CJ Request for Info on Metrics.md` - CJ's questions and context

### Related Projects
- [12-Disaster_Recovery](../12-Disaster_Recovery/README.md) - Overlapping infrastructure work
- [11-Red_Mythos_Vulnerability_Remediation](../11-Red_Mythos_Vulnerability_Remediation/README.md) - Must complete to free capacity
- [14-MongoDB_Atlas_Migration](../14-MongoDB_Atlas_Migration/README.md) - Infrastructure modernization

### People Pages
- [[Mike_Mitchell]] - Mike Mitchell context (execution owner)
- [[Aaron_Srivastava]] - Aaron context (JIRA/metrics owner)
- [[Daniel_Milburn]] - Daniel context (DR owner)

## Success Metrics & What Good Looks Like

### By Mid-Q3 (End of July 2026):
✅ Every team has documented domain, coupling map, and target architecture  
✅ Teams can explain their boundaries and deployment path clearly  
✅ Cross-team ownership conflicts identified and resolved  
✅ Foundation set for Q3/Q4 decoupling work to actually execute  
✅ Teams excited about the change, not just compliant

### By End of Q3 (End of September 2026):
✅ Phase 0 work started (teams own merges, deployments)  
✅ JIRA spaces live with simplified workflows  
✅ Team-level metrics visible and being tracked  
✅ Decoupling roadmaps documented per team

### By Q4 2026:
✅ Autonomous teams becomes THE dominant engineering focus  
✅ Phase 1 execution underway (code separation)  
✅ GitHub migrations in progress for pilot teams  
✅ Deployment frequency increasing (trend visible)

## Key Quotes & Cultural Context

### From Mike Mitchell (Handoff Meeting):
> "This is going to be such a huge difference maker... a game changer"

> "Think about deploying changes every day that you couldn't do for a month before"

> "I don't know how anybody could stay working on the product the way it is today. I feel bad for people that have done it so long. But that's why I think this is huge opportunity to make an impact."

### From Marten (Strategic Direction):
> "This is one of the 'Big 4' technical priorities for Q3 2026, and expected to become THE dominant priority by Q4"

> "Before we can shift capacity from 75% technical debt to commercial work, we need to get the technical foundation right"

### From Exchange Team Standards:
> "Each team owns a clear domain with defined boundaries... Teams deploy independently without coordination"

> "Goal is not perfect microservices architecture—mini-monoliths per team are acceptable intermediate state"

---

**Last Updated:** June 1, 2026  
**Next Review:** Weekly (Marten/Mike checkpoint - to be scheduled)  
**Foundation Target:** Mid-Q3 2026 (July 31)  
**Execution Dominance:** Q4 2026
