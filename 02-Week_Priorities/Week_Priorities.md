# Week Priorities

**Week of:** 2026-06-08

**⚠️ SHORT WEEK:** FTO Wed-Fri (only Mon-Tue available, team meetup days)

---

## 📊 Week Shape

**⚠️ SHORT WEEK:** Only Mon-Tue available (FTO Wed-Fri)

**Working days:** Monday and Tuesday only (team meetup days)
- **Mon-Tue:** On-site team meetup - moderate to heavy meetings
- **Wed-Fri:** Flex Time Off (vacation)

**Estimated deep work capacity:** 2-4 hours max (limited to gaps during 2-day meetup)

---

## 🎯 Last Week Context

**Strategic wins:**
- ✅ Veritas Capital relationship established (Var George) - pathway to Kickdrum influence
- ✅ Narrative framework clarified with Curtis - map resiliency work to incident root causes
- ✅ Jira design complete - ready for testing
- ✅ 18 months of resiliency work documented

**What didn't get done:**
- ❌ CJ data-backed response (research phase only)
- ❌ Jira rollout execution (design done, projects not created yet)
- ❌ Architecture forum launch (planning only)

**Key insight from Curtis:**
> "I'm checking a bunch of them off. Like, that one we've done, this one we've done, this one we've halfway done."

The work exists. CJ doesn't know because nobody mapped it to the original incident root causes. **That's the task.**

---

## 🎯 Top 3 This Week

**⚠️ Adjusted for 2-day work week (Mon-Tue only, FTO Wed-Fri)**

### 1. **Launch First Architecture Forum (Team Meetup)** — **Breaking the Monolith** ^week-2026-W24-p1

**Success criteria:** Forum structure defined, first session held Mon or Tue during team meetup, domain boundary discussions initiated

**Why this is Priority #1:**
- **ONLY happens during team meetup** - can't defer to next week
- You're only here Mon-Tue, team disperses after that
- Need venue for decoupling decisions and technical ownership discussions
- First topic: domain boundary definitions (what does each team own?)

**Effort:** Medium work (2-3 hours total over 2 days)
- Forum structure definition: 1 hour (Monday)
- First session during meetup: 1-2 hours (Mon or Tue)
- Domain boundary template: 30 minutes

**Best timing:** Define structure Monday morning, hold session Monday afternoon or Tuesday

**Quarterly goal:** None active (supports "Breaking the Monolith" pillar)

---

### 2. **Request Kickdrum Meeting Access** — **Organizational Foundation** ^week-2026-W24-p2

**Success criteria:** Email sent to Jamie/Curtis requesting access to Kickdrum meetings (daily standup, weekly readout, quarterly readout)

**Why this is Priority #2:**
- Quick win (30 min email)
- High strategic value from Var George conversation
- Positions you for external validation opportunities
- Can be done Monday between meetup sessions

**Effort:** Quick (30 minutes)
- Draft email requesting meeting access
- CC appropriate stakeholders
- Send Monday

**Follow-up:** Attend first Kickdrum meeting when invited (likely next week)

**Quarterly goal:** None active (supports Veritas Capital relationship)

---

### 3. **Defer CJ Work to Next Week** — **Critical Technical Execution** ^week-2026-W24-p3

**Success criteria:** Explicitly acknowledge CJ synthesis work requires 6-8 hours deep work (not possible this week), commit to next week execution

**Why this is Priority #3:**
- Requires sustained deep work (6-8 hours) that doesn't exist in 2-day meetup week
- Thursday/Friday synthesis time = FTO days this week
- Better to explicitly defer than partially attempt and deliver poor quality
- Steve's product planning can wait one more week

**Action for this week:** Send quick note to Curtis: "CJ follow-up needs deep synthesis time - targeting next week Mon-Wed for completion."

**Next week plan:**
- Data gathering: 3-4 hours (find decks, extract metrics)
- Synthesis: 2-3 hours (map work to root causes, build "From → To")
- Email drafting: 1-2 hours
- Target completion: Wednesday June 18

**Quarterly goal:** None active (operates as de facto quarterly goal)

---

## ⚡ High-Value Additions (If Time Mon-Tue)

### 4. **Jira Testing Session - BLOCKED BY FTO** — **Breaking the Monolith**

**Original plan:** Wednesday 14:30 testing session

**Conflict:** You're on FTO Wednesday

**Options:**
1. **Delegate to Mike Mitchell** - He can attend Wed testing, approve template, execute rollout
2. **Reschedule to Tuesday** - If Mike/team available, move testing to Tue during meetup
3. **Defer to next week** - Not urgent, design is done

**Recommended:** Delegate to Mike. Design complete, he can execute. Check in with him Monday to confirm.

---

### 5. **Send Kickdrum Punch List** — Deferred to next week

**Action:** Document areas where external validation would be valuable (tech coupling, deployment flexibility, DR architecture, MongoDB strategy, monolith decomposition approach)

**Why deferred:** Requires 1-2 hours synthesis work. Better done after joining first Kickdrum meeting (which likely happens next week after access granted).

**Timing:** Week of June 15 after attending first meeting

---

## 📋 Tasks by Priority

### Must Complete This Week (Mon-Tue Only)

**Architecture Forum (Priority 1):**
- [ ] Define architecture forum structure Monday morning (purpose, format, cadence)
- [ ] Schedule and hold first session Mon or Tue during team meetup
- [ ] Create domain boundary definition template
- [ ] Initiate domain boundary discussions with teams

**Kickdrum Access (Priority 2):**
- [ ] Email Jamie/Curtis requesting Kickdrum meeting access Monday
- [ ] Check in with Mike Mitchell about Jira Wed testing (delegate or reschedule)

### Deferred to Next Week (Post-FTO)

**CJ Follow-up (Now Priority 1 for week of June 15):**
- [ ] Find and review resiliency surge plan decks with incident root cause categories `task-20260602-032`
- [ ] Find Dermot's DB stabilization work (~1 year ago) for metrics approach reference `task-20260602-033`
- [ ] Gather current DB metrics (Audit DB, BT/BD, data layer reliability) `task-20260602-034`
- [ ] Build metrics-driven "From → To" for each P0 database item `task-20260602-035`
- [ ] Map completed 18-month resiliency work to historical incident root causes `task-20260601-027`
- [ ] Analyze stability risk: Oct 1 vs Jan 1 capacity shift `task-20260602-038`
- [ ] Access and update SharePoint 1-pager "Exchange resiliency" box `task-20260602-036`
- [ ] Draft data-backed email response to CJ `task-20260602-037`
- [ ] Send Curtis note: "CJ follow-up targeting next week Mon-Wed completion"

**Kickdrum Punch List (Next week after first meeting):**
- [ ] Attend first Kickdrum meeting
- [ ] Draft and send Kickdrum punch list (tech coupling, deployment, DR, MongoDB validation)

**Jira Rollout (If not delegated to Mike):**
- [ ] Review and approve Jira project template (Mike can handle)
- [ ] Track 12 project creation (Mike executes)
- [ ] Ensure template documentation exists

### Should Complete (P1)

- [ ] Gather specific decoupling examples from teams (databases, tables, components) `task-20260601-028`
- [ ] Document P0 database work details (audit DB, BTBD, event bus) `task-20260601-029`

### If Time Permits (P2)

- [ ] Talk to Daniel about India hiring calibration (3 manager roles stuck for ~2 weeks)
- [ ] Review Chas Narne interview feedback and make decision
- [ ] Start architecture forum discussion on decoupling roadmap `task-20260601-031`

---

## 📅 Key Meetings

| Day | Time | Activity | Purpose | Related Priority |
|-----|------|----------|---------|------------------|
| **Mon-Tue** | TBD | **Team Meetup** | On-site team time (partial attendance) | Priority #1 |
| **Mon-Tue** | TBD | **First Architecture Forum** | Domain boundaries | Priority #1 |
| **Wed-Fri** | — | **FTO (Flex Time Off)** | Vacation | — |
| **Next Week** | TBD | **🎯 Protected: CJ Synthesis** | Map work to incidents, draft email | Deferred Priority |

---

## 📊 Pillar Balance

**⚠️ 2-day week adjustment**

| Pillar | This Week | Balance |
|--------|-----------|---------|
| **Organizational Foundation** | Kickdrum meeting access request | 🟡 Light (20%) |
| **Breaking the Monolith** | Architecture forum launch, domain boundaries | 🟩 Strong (80%) |
| **AI Native SDLC** | Not this week | 🟥 Deferred (0%) |
| **Critical Technical Execution** | Explicitly deferred to next week | 🟥 Deferred (0%) |

**Balance Assessment:** ⚠️ Heavily weighted to Breaking the Monolith - appropriate for 2-day team meetup. CJ work (Critical Technical Execution) deferred to next week when deep work time available.

---

## 🔄 Carried Over from Last Week

All 3 priorities carried over, but **FTO Wed-Fri limits execution:**

1. **CJ Follow-up** — **DEFERRED to next week** (requires 6-8 hours deep work, not possible in 2-day meetup week)
2. **Jira Rollout** — **DELEGATED to Mike** (Wed testing conflicts with FTO, Mike can execute)
3. **Architecture Forum** — **EXECUTING Mon-Tue** (only priority that requires team meetup presence)

**Why low completion last week:** Strategic pivot to context gathering (Var George conversation, Curtis narrative framing). Higher value than immediate execution.

**This week:** Only Architecture Forum can realistically complete. Other priorities defer to week of June 15.

---

## 🎯 Quarterly Goals Context

**Status:** No quarterly goals currently tracked in system.

**Observation:** Weekly priorities are operating as de facto goals, but lacking explicit quarterly framework limits ability to show multi-week momentum.

**Recommendation:** Consider running `/quarter-plan` after this execution-heavy week to establish Q2 2026 goals that weekly priorities ladder up to.

---

## 💡 Strategic Context

### The Big Stakes

**CJ Follow-up (Priority 1):**
- Steve needs confidence to plan for Oct 1 capacity shift (50-50 product vs. tech debt)
- Your initial email was conceptual - CJ needs incident data, metrics, risk analysis
- This determines if you get 3 more months (Oct 1 vs Jan 1)
- Curtis revealed the gap: work exists, story wasn't told

**What CJ is really asking:**
- "Show me with incident data that Autonomous Teams reduces resiliency risk"
- "Give me metrics-driven 'From → To' for database work, like Dermot did"
- "Tell me the stability risk if we shift capacity too early"
- "Update the resiliency slide I showed India with current status"

**The answer exists:** 18 months of systematic improvements (DB stabilization, I/O throttling, release rigor). Zero DB incidents Nov 2024 - Mar 2025. Zero release incidents Oct 2024 - present. Just need to map it to original root causes.

### External Validation Opportunity

**Var George (Veritas Capital) creates options:**
- Get Kickdrum visibility → direct them to high-value areas
- External endorsement of technical strategy
- Either collapse timeline (if they validate aggressive approach) OR create peace with product org (if they endorse complexity)
- Both outcomes valuable

**Var's key validation:**
> "When people talk about the monolith, most think about the code base. But it's the organization, the processes, and the deployment footprint that's actually more important."

Your org-first approach aligns with expert assessment. Use this.

### Team Transformation Evidence

**You're ahead of the curve (per Var):**
- IC-first managers (your structure) = Valley trend
- Team sizes collapsing with AI (6 → 3 members) - you're already there
- Organizational decoupling before code = reverse Conway, validated by external expert
- "Good command of the situation" - implicit assessment

### Quality Execution Gap (Curtis's Insight)

**Pattern observed:**
> "Good is an unknown concept to a team"

- Jira: teams don't know how to use effectively
- Testing: UI tests actually testing backend (wasteful), blind Selenium → Playwright migration
- Work categorization: ~70% of "technical work" is actually commercial

**Implications:** Approach problems, not just resource problems. This is why standardization (Jira template, architecture forum) matters.

---

## 🏁 Week Success Definition

**⚠️ Adjusted for 2-day work week**

This week is successful if:

1. ✅ **First architecture forum held** Mon or Tue during team meetup with domain boundary discussions initiated
2. ✅ **Kickdrum meeting access** requested via email to Jamie/Curtis
3. ✅ **CJ work explicitly deferred** to next week with Curtis notified

**Critical success:** Architecture Forum launched while team is together (can't defer to next week)

**Stretch goals:**
- Mike Mitchell confirmed for Wed Jira testing (delegated)
- Domain boundary template created and in use
- Quick check-ins with key team members during meetup

---

## ⚠️ Blocked Items

| Item | Blocked Since | What Would Unblock It |
|------|---------------|-----------------------|
| Contractor extension decision | June 4 | Testing strategy approach finalized (keep/throw away evaluation) |
| India hiring (3 manager roles) | ~2 weeks | Talk to Daniel about calibration, possible Ramesh support |
| Chas Narne candidate decision | June 4 | Review final interview feedback, schedule debrief if needed |

---

## 🏁 End of Week Review

*Fill in on Friday, June 13*

### Completed
- 

### Didn't Finish
- 

### Learnings
- 

### Next Week Focus
- 

---

*Generated: 2026-06-08 (Monday morning)*  
*Command: /week-plan*  
*Context: Execution week after strategic pivot - all 3 priorities carry over with clearer path*
