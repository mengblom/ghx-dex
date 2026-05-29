# Autonomous Teams Program Handoff - Mike Mitchell
**Date:** May 28, 2026, 4:00 PM  
**Duration:** ~15 minutes
**Purpose:** Formal handoff of autonomous teams execution to Mike

**Transcript:** [[00-Inbox/Meetings/2026-05-28 - Autonomous Teams Handoff - Mike Mitchell - Transcript.md]]

---

## Meeting Goal
**Mike owns execution of the autonomous teams program. Marten sets direction, Mike drives implementation.**

**OUTCOME:** ✅ Mike confirmed ownership and is excited about the work. Aligned on phased approach and next steps.

---

## What Was Actually Discussed

### Key Points Covered:

1. **Handoff Confirmation**
   - Mike owns execution of autonomous teams (initial phase)
   - Aaron owns Red Mythos, Daniel owns DR
   - In a few months, everyone will likely pile onto autonomous teams

2. **Initial Playbook - Three Phases**
   - **Phase 0 (Mike's idea):** Deployments and merges first - "master of your domain" without full code separation yet
   - **Phase 1:** Code separation (move to GitHub, independent deployments, infrastructure as code)
   - **Phase 2:** Data separation (later - shared databases not the immediate problem)
   - Key insight: If data is unquestionably owned by one team and no one else is peeking at it, take it with you now

3. **Immediate Next Steps**
   - **Finish team standards** - Mike will schedule working session (same group from May 17 + Anand)
   - **Define team domains** - Matt Turner's page exists as starting point, teams will create Lucid charts showing services, connections, data ownership, what they own
   - **Create new JIRA spaces** - Goal: End of next week for blank spaces created
   - **Simplified workflow** - Aligned workflow that teams can customize on top

4. **Timeline Discussed**
   - **End of next week:** JIRA spaces created + simplified workflow aligned + beta version of team domain definitions (functional level - what belongs to which team)
   - Acknowledged some teams are ahead (Visibility team already identified services to carve out)

5. **Concerns Raised**
   - JIRA project ID changes will break external integrations/reports (but also a forcing function to discover and clean up homegrown integrations)
   - People are reluctant to prune backlogs when moving to new JIRA spaces (need to "hatchet" 3+ year old tickets)

6. **Mike's Excitement**
   - "This is going to be such a huge difference maker... a game changer"
   - "Think about deploying changes every day that you couldn't do for a month before"
   - Sees opportunity to make real impact

---

## What Was NOT Covered (Needs Follow-Up)

### Structural Details Not Discussed:
- **Formal ownership split** - What Mike owns vs what Marten owns (communicated verbally but not the detailed list)
- **Exchange Team Standards doc updates** - Metrics section and team next steps (wasn't mentioned)
- **Mid-Q3 deliverables** - Specific list: documented boundaries, coupling maps, target architecture, plan to break free
- **Tracking mechanism** - How Mike will track team progress (Jira epic? Confluence? Spreadsheet?)
- **Weekly checkpoint cadence** - Marten/Mike regular sync not discussed
- **Coordination with Aaron** - JIRA space setup alignment with domain definitions
- **Pilot vs full rollout decision** - Should we start with 1-2 teams or all teams at once?
- **Staff meeting socialization** - Should this be presented in staff meeting first or just execute?

### Open Questions Still Pending:
- What format for team deliverables? (Confluence pages? Lucid diagrams? Both?)
- How do we handle teams already ahead (like Visibility)?
- What's the escalation path for cross-team ownership conflicts?
- What support does Mike need from Marten to be successful?

### Next Meeting Should Cover:
1. Formalize tracking mechanism for team progress
2. Set up weekly Marten/Mike checkpoint (15-30 min)
3. Review Exchange Team Standards doc once updated
4. Decide on pilot approach vs full rollout
5. Define clear escalation path for blockers
6. Clarify coordination with Aaron on JIRA/domain alignment

---

## ORIGINAL MEETING PLAN (For Reference)

*Note: The actual meeting was more tactical and exploratory than this structured handoff. The sections below represent what was originally planned but not fully covered.*

## 1. Context: Why This Matters (3 min)

**The Problem:**
- Monolithic architecture creates deployment dependencies
- Teams can't ship independently → slower velocity, coordination overhead
- Shared ownership → diffuse accountability, harder to measure team performance

**The Vision:**
- Each team owns a clear domain with defined boundaries
- Teams deploy independently without coordination
- Clear metrics at the team level (not just blended pod metrics)
- Faster time-to-market, clearer accountability

**Why Now:**
- Q3 capacity allocation: 75% of technical work must support Big 3 (Red Mythos, DR, **Breaking the Monolith**)
- CJ pushing for team-level metrics (can't do that without clear team boundaries)
- Native JIRA spaces coming → each team needs defined scope

---

## 2. What Mike Owns vs What Marten Owns (2 min)

### Mike Owns (Execution):
- ✅ Coordinating execution cadence with teams
- ✅ Scheduling team sessions to work through domain definition
- ✅ Tracking progress on deliverables (documented boundaries, coupling maps, target architecture)
- ✅ Surfacing blockers and cross-team conflicts to Marten
- ✅ Working with Aaron on JIRA space setup that aligns with team domains
- ✅ Ensuring teams understand the next steps and have what they need

### Marten Owns (Direction):
- ✅ Setting strategic priorities and capacity allocation (25/75, Big 3)
- ✅ Resolving ambiguous ownership questions between teams
- ✅ Final decisions on team topology changes if needed
- ✅ Communication to leadership and CJ on progress
- ✅ Connecting this work to DR, Red Mythos, and broader tech strategy

---

## 3. Current State: Where We Are (5 min)

### What Exists:
- **Exchange Team Standards doc** — Framework for what autonomous teams need (getting updated with metrics section and next steps)
- **Matt Turner's domain ownership page** — Some initial domain mapping (needs review and broader input)
- **Team catalog** — Started but incomplete (Aaron asking teams to fill it out)
- **JIRA sandbox project** — Aaron testing native team spaces (plan to review next week)
- **Some teams ahead:** Visibility team has already named services they want to carve out

### What's In Progress:
- Defining baseline JIRA space template (Mike + Christine working on this)
- Aaron planning JIRA instrumentation for automated team metrics (2-week timeline)
- DevOps coordination for team automation needs (Bhavna KT process)

### What's Missing:
- **Most teams haven't defined their domains yet** — Don't know boundaries, coupling points, or target architecture
- **No timeline/cadence for team sessions** — Need Mike to schedule and drive
- **Cross-team ownership ambiguities** — Will surface as teams do the work
- **Formalized tracking** — How do we know which teams are done vs stuck?

---

## 4. The Playbook: What Teams Need to Do (5 min)

Each team needs to work through these four areas (in this order):

### 1. **Define Your Domain**
- What's in scope? What's out of scope?
- Where are the boundaries fuzzy or overlapping with other teams?
- What business capabilities do you own?

### 2. **Map Current Coupling Points**
- How are you tied to the monolith or other services?
- Shared repos? Direct code dependencies? Shared databases?
- What forces you to coordinate deployments?

### 3. **Identify Deployment Blockers**
- What specifically prevents you from deploying independently today?
- Shared infrastructure? Shared data? Orchestration dependencies?

### 4. **Document Target Architecture**
- What does your independently deployable future state look like?
- What services will you create? What APIs will you expose?
- What data will you own?

### Deliverable by Mid-Q3:
- ✅ Documented domain boundaries
- ✅ Current coupling points mapped
- ✅ Target architecture documented  
- ✅ Plan to break free (doesn't have to be executed, but clear direction)

---

## 5. How Mike Should Drive This (5 min)

### Proposed Approach:
1. **Schedule 90-minute sessions with each team** (over next 3-4 weeks)
   - Use Exchange Team Standards as framework
   - Walk through the four areas together
   - Capture outputs in Confluence (or team's preferred format)

2. **Create tracking mechanism**
   - Which teams have scheduled sessions?
   - Which teams have documented deliverables?
   - What blockers or ambiguities have surfaced?

3. **Hold weekly checkpoint with Marten** (15-30 min)
   - What progress was made?
   - What's blocked or needs decision?
   - Which teams need escalation?

4. **Coordinate with Aaron on JIRA spaces**
   - Team domain definition should inform JIRA space scope
   - Ensure team boundaries in JIRA match actual ownership

5. **Surface cross-team conflicts early**
   - If two teams think they own the same thing → escalate to Marten
   - If team identifies dependency on another team → coordinate resolution

### What Good Looks Like:
- Every team has a documented domain, coupling map, and target architecture by mid-Q3
- Teams can explain their boundaries and deployment path clearly
- Cross-team ownership conflicts identified and resolved
- Foundation set for Q3 decoupling work to actually execute

---

## 6. Open Questions & Discussion (10 min)

**For Mike:**
- Does this level of ownership make sense? Too much? Too little?
- What format do you want for team deliverables? (Confluence pages? Diagrams? Something else?)
- How do you want to track progress? (Jira epic? Spreadsheet? Confluence tracker?)
- What support do you need from Marten to make this successful?

**For Both:**
- Should we pilot with 1-2 teams first, or roll out to all teams at once?
- How do we handle teams that are already ahead (like Visibility)?
- What's the right cadence for Marten/Mike checkpoint meetings?
- Should this be socialized in staff meeting first, or just start executing?

---

## 7. Next Actions - ACTUAL COMMITMENTS FROM MEETING

### Mike's Immediate Next Steps:
- [x] Schedule working session to finish team standards (same group from May 17 + Anand) - **Target: Monday or Tuesday in Denver**
- [ ] Review Matt Turner's domain ownership page
- [ ] Coordinate with teams on creating Lucid chart domain definitions (services, connections, data ownership)
- [ ] Drive completion of JIRA spaces + simplified workflow by end of next week
- [ ] Book dinner with Marten, Daniel, Aaron on Monday (first time all together)

### Marten's Immediate Next Steps:
- [ ] Send Breaking the Monolith communication to teams (Friday) - **Status: Still planned per 2-Day Focus doc**
- [ ] Update Exchange Team Standards doc (metrics section, team next steps) - **Not discussed in meeting, still needed**
- [ ] Coordinate dinner arrangements for Monday with Mike, Daniel, Aaron

### Still Needs Discussion (Follow-Up Meeting):
- [ ] Formalize tracking mechanism for team progress
- [ ] Set up weekly Marten/Mike checkpoint cadence
- [ ] Decide on pilot vs full rollout approach
- [ ] Define escalation path for cross-team conflicts
- [ ] Confirm coordination approach with Aaron on JIRA/domain alignment
- [ ] Decide if this needs staff meeting socialization first

### Original Plan Items (Not Covered):
- [ ] Review Exchange Team Standards doc (once Marten updates it)
- [ ] Decide on tracking format for team progress
- [ ] Schedule first 1-2 team sessions (pilot approach?)
- [ ] Set up weekly checkpoint with Marten
- [ ] Decide if this needs staff meeting discussion or just execute
- [ ] Confirm cadence for Marten/Mike checkpoints

---

## Success Criteria - ACTUAL OUTCOMES

### ✅ Achieved:
1. ✅ **Mike knows he owns execution and is excited about it** - Confirmed verbally, Mike sees this as a "huge difference maker" and "game changer"
2. ✅ **Aligned on phased approach** - Phase 0 (deployments/merges), Phase 1 (code), Phase 2 (data)
3. ✅ **Clear immediate next steps** - Finish team standards, create JIRA spaces, define domains (Lucid charts)
4. ✅ **Timeline set** - End of next week for JIRA spaces + simplified workflow + beta domain definitions
5. ✅ **Mike will schedule team standards working session** - Same group from May 17 + Anand, targeting Monday/Tuesday in Denver

### ⚠️ Partially Achieved:
- ⚠️ **What teams need to deliver** - Discussed at high level (domains, Lucid charts) but not the full mid-Q3 deliverables list
- ⚠️ **Mike has the playbook** - Matt Turner's page exists, but Exchange Team Standards doc not reviewed/updated yet

### ❌ Not Achieved (Needs Follow-Up):
- ❌ **How Mike and Marten will coordinate** - Weekly checkpoints not discussed or scheduled
- ❌ **Clear escalation path** - Not discussed
- ❌ **Tracking mechanism** - How to track team progress not decided
- ❌ **Formal ownership split** - What Mike owns vs what Marten owns (detailed list not reviewed)

### Recommendation:
Schedule 30-min follow-up after team standards working session to formalize:
1. Tracking mechanism
2. Weekly checkpoint cadence
3. Escalation path
4. Review updated Exchange Team Standards doc

---

*Meeting Owner: Marten Engblom*  
*Expected Outcome: Mike Mitchell formally owns autonomous teams execution*
