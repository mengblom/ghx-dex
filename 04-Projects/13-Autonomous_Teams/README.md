# Autonomous Teams / Breaking the Monolith

**Status:** Active (Q3/Q4 2026 primary focus)  
**Owner:** [[Mike_Mitchell]] (Director)  
**Executive Sponsor:** Marten Engblom  
**Priority:** P0 - Strategic unlock for engineering velocity

---

## Overview

Transform Exchange engineering from monolithic, coordinated deployments to autonomous teams with clear domain ownership, independent deployments, and self-service capabilities. This is one of the "Big 3" technical priorities for Q3 2026, and expected to become THE dominant priority by Q4.

---

## Strategic Context

**The Problem:**
- Monolithic architecture creates deployment dependencies
- Teams can't ship independently → slower velocity, coordination overhead
- Shared ownership → diffuse accountability, harder to measure team performance
- Merge coordination, shared deployment pipelines, coupled release schedules

**The Vision:**
- Each team owns a clear domain with defined boundaries
- Teams deploy independently without coordination ("master of your domain")
- Clear metrics at the team level (not just blended pod metrics)
- Faster time-to-market, clearer accountability
- Teams own their own merges, deployments, infrastructure

**Why Now:**
- Q3 capacity allocation: 75% of technical work must support Big 3, with autonomous teams as the biggest unlock
- CJ pushing for team-level metrics (can't do that without clear team boundaries)
- Native JIRA spaces coming → each team needs defined scope
- Overlaps with DR automation needs (infrastructure as code, automated deployments)

**Q3 Planning Guidance:**
All technical work in Q3 should roll up to one of the Big 3:
1. Red Mythos / Vulnerabilities
2. Disaster Recovery
3. **Autonomous Teams / Breaking the Monolith** ← This project (expected to dominate by Q4)

---

## Ownership Model

### Mike Owns (Execution):
- Coordinating execution cadence with teams
- Scheduling team sessions to work through domain definition
- Tracking progress on deliverables (documented boundaries, coupling maps, target architecture)
- Surfacing blockers and cross-team conflicts to Marten
- Working with Aaron on JIRA space setup that aligns with team domains
- Ensuring teams understand next steps and have what they need

### Marten Owns (Direction):
- Setting strategic priorities and capacity allocation (25/75, Big 3)
- Resolving ambiguous ownership questions between teams
- Final decisions on team topology changes if needed
- Communication to leadership and CJ on progress
- Connecting this work to DR, Red Mythos, and broader tech strategy

---

## Phased Approach

### Phase 0: Deployments and Merges First (Quick Win)
- Teams own their own merge process (no more cross-team merge coordination)
- Teams own their deployment pipelines (even if code stays in monolith temporarily)
- Goal: "Master of your domain" - independent control without full code separation yet
- **Why:** Fastest path to reducing coordination overhead

### Phase 1: Code Separation
- Move components to GitHub
- Independent deployments with GitHub Actions
- Infrastructure as Code for all team-owned infrastructure
- Teams own repos, pipelines, and deployment automation
- **Note:** Data can stay shared for now

### Phase 2: Data Separation (Later)
- Decouple shared databases
- Each team owns their data
- Clear data boundaries and contracts
- **Exception:** If data is unquestionably owned by one team and no one else touches it, take it now in Phase 1

**Key Decision:** Phase 0/1 doesn't require perfect microservices architecture. Acceptable intermediate state: mini-monoliths per team (e.g., "deploy all of Exchange Automation" is way better than "deploy entire All repo")

---

## Current State (May 28, 2026)

### What Exists:
- **Team Standards framework** - In progress, being finalized in working session (Mon/Tue early June in Denver)
- **Matt Turner's domain ownership page** - Initial domain mapping exists as starting point
- **Team catalog** - Started but incomplete (Aaron asking teams to fill it out)
- **JIRA sandbox project** - Aaron testing native team spaces
- **Some teams ahead:** Visibility team has already named services to carve out

### What's In Progress:
- Defining baseline JIRA space template (Mike + Christine)
- Aaron planning JIRA instrumentation for automated team metrics (2-week timeline)
- DevOps coordination for team automation needs

### What's Missing:
- **Most teams haven't defined their domains yet** - Don't know boundaries, coupling points, target architecture
- **No timeline/cadence for team sessions** - Mike scheduling working sessions
- **Cross-team ownership ambiguities** - Will surface as teams do the work
- **Formalized tracking** - Need to decide how to track which teams are done vs stuck

---

## The Playbook: What Teams Need to Do

Each team works through these four areas:

### 1. Define Your Domain
- What's in scope? What's out of scope?
- Where are boundaries fuzzy or overlapping with other teams?
- What business capabilities do you own?
- **Deliverable:** Lucid chart or Confluence page documenting domain

### 2. Map Current Coupling Points
- How are you tied to the monolith or other services?
- Shared repos? Direct code dependencies? Shared databases?
- What forces you to coordinate deployments?
- **Deliverable:** Documented coupling map

### 3. Identify Deployment Blockers
- What specifically prevents you from deploying independently today?
- Shared infrastructure? Shared data? Orchestration dependencies?
- **Deliverable:** List of blockers with severity/effort estimates

### 4. Document Target Architecture
- What does your independently deployable future state look like?
- What services will you create? What APIs will you expose?
- What data will you own?
- **Deliverable:** Target architecture diagram (Lucid chart)

### By Mid-Q3, Every Team Should Have:
1. ✅ Documented domain boundaries
2. ✅ Current coupling points mapped
3. ✅ Target architecture documented
4. ✅ A plan to break free of the monolith (doesn't have to be executed, but clear direction)

---

## Timeline & Next Steps

**End of Next Week (Early June 2026):**
- ✅ JIRA spaces created (blank, ready for teams)
- ✅ Simplified workflow aligned (teams can customize on top)
- ✅ Beta version of team domain definitions (functional level - what belongs to which team)

**Mid-Q3 2026:**
- ✅ All teams have documented domains, coupling maps, target architecture, and decoupling plans
- ✅ Cross-team ownership conflicts identified and resolved
- ✅ Foundation set for Q3/Q4 decoupling execution work

**Q4 2026 and Beyond:**
- Execution phase - teams actually decoupling, moving to GitHub, establishing independent deployments
- Expected to be THE dominant engineering focus (Red Mythos wrapped, DR in maintenance mode)

---

## Immediate Actions (May 28, 2026)

### Mike's Next Steps:
- [x] Schedule working session to finish team standards (targeting Mon/Tue in Denver, same group from May 17 + Anand)
- [ ] Review Matt Turner's domain ownership page
- [ ] Coordinate with teams on creating Lucid chart domain definitions
- [ ] Drive completion of JIRA spaces + simplified workflow by end of next week

### Marten's Next Steps:
- [ ] Send "Breaking the Monolith" communication to teams (Friday, May 31)
- [ ] Update Exchange Team Standards doc (can happen in working session or before)
- [ ] Schedule 30-min follow-up with Mike after working session to formalize tracking, checkpoints, escalation

### Still Needs Discussion:
- [ ] Formalize tracking mechanism for team progress
- [ ] Set up weekly Marten/Mike checkpoint cadence
- [ ] Decide on pilot vs full rollout approach (1-2 teams first or all teams?)
- [ ] Define escalation path for cross-team conflicts
- [ ] Confirm coordination approach with Aaron on JIRA/domain alignment
- [ ] Decide if this needs staff meeting socialization first

---

## Key Meeting Notes

- [[00-Inbox/Meetings/2026-05-28 - Autonomous Teams Handoff - Mike Mitchell]] - Formal handoff meeting
- [[00-Inbox/Meetings/2026-05-28 - Autonomous Teams Handoff - Mike Mitchell - Transcript]] - Full transcript
- [[00-Inbox/Meetings/2026-05-08/Road_to_Autonomy_Github_Migrations]] - Early discussion connecting DR, autonomous teams, GitHub migrations

---

## Related Materials

### Strategic Documents
- [[00-Inbox/Ideas/Q3_Roadmap_Planning_Communications]] - Q3 capacity allocation guidance sent to org + Product (May 28)
- [[00-Inbox/2-Day_Focus_May_28-29]] - Current 2-day execution focus
- [[00-Inbox/Weekly_Synthesis_2026-05-24]] - Recent weekly context

### People Context
- [[Mike_Mitchell]] - Execution owner
- [[Aaron_Srivastava]] - JIRA space setup, team metrics instrumentation
- [[Daniel_Milburn]] - Coordination on DR/autonomous teams overlap

### Related Projects
- [[04-Projects/Disaster_Recovery/]] - Overlapping infrastructure requirements (IaC, automated deployments)
- [[04-Projects/Exchange Platform Architecture/]] - Broader architectural context
- [[04-Projects/Automation Team - Vision and Strategy/]] - Automation infrastructure supporting this work

---

## Mike's Excitement (From Handoff Meeting)

> "This is going to be such a huge difference maker... a game changer. Think about deploying changes every day that you couldn't do for a month before."

> "I don't know how anybody could stay working on the product the way it is today. I feel bad for people that have done it so long. But that's why I think this is huge opportunity to make an impact."

---

## Notes & Considerations

### What Good Looks Like:
- Every team has documented domain, coupling map, and target architecture by mid-Q3
- Teams can explain their boundaries and deployment path clearly
- Cross-team ownership conflicts identified and resolved
- Foundation set for Q3 decoupling work to actually execute
- Teams excited about the change, not just compliant

### Concerns to Watch:
- **Backlog pruning resistance:** Teams reluctant to "hatchet" 3+ year old tickets when moving to new JIRA spaces
- **JIRA integration breakage:** New project IDs will cause external reports/integrations to be incomplete (but also surfaces homegrown integrations that should be retired)
- **Unknown coupling:** Teams will discover coupling they didn't know about when they map dependencies
- **Perfectionism trap:** Don't need perfect microservices architecture - mini-monoliths per team are acceptable intermediate state

---

*Created: 2026-05-28*  
*Last Updated: 2026-05-28*
