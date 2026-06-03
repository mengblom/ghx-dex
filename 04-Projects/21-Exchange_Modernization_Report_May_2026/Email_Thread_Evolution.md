# Exchange Modernization Email Thread - Evolution

**Thread Duration:** May 23 - June 2, 2026  
**Participants:** Marten Engblom, [[CJ_Singh|CJ Singh]], [[Curtis_Nielsen|Curtis Nielsen]]  
**Subject:** Exchange Modernization Update

---

## Thread Timeline

### May 23, 2026 - Initial Presentation Share
**From:** Marten → CJ (cc Curtis)

Marten shares deck with:
- Timeline and capacity split targets
- Phase 1 DOD for Autonomous Teams
- Must-Dos before capacity shift (Autonomous Teams + P0 DB work)
- Aggressive but realistic timeline
- Risks and mitigations

### May 22, 2026 - CJ's Five Questions
**From:** CJ → Marten (cc Curtis)

After reviewing the deck, CJ asks:
1. How many new services are we creating?
2. How are we prioritizing them? Tied to incident root causes?
3. What can be done in parallel vs sequential? (Gantt chart view)
4. Is there a logical arch diagram of target state by end of Q1?
5. What's the tradeoff if we shift to 50-50 in Q3 instead of waiting?

**Action:** Requests 1-hour meeting next Friday

### May 28, 2026 - Detailed Response
**From:** Marten → CJ (cc Curtis)

Key clarifications:
- **Phase 1 is about team decoupling, not service proliferation**
  - Might create zero new services initially
  - Focus: independent deployment, own pipelines, own schedules
  - Architecture may look similar to today initially
  
- **No Gantt chart because it's bottom-up**
  - Driven by team readiness and coupling complexity
  - Some teams break free sooner (incremental)
  - Details discovered incrementally
  
- **DR work blocks parallel execution**
  - DR touches same infra (IaC, deployments, automation)
  - Must happen mostly sequentially
  - Some synergies (DR necessitates decoupling)
  
- **P0 Database work is critical before capacity shift**
  - Most serious incidents are DB-related
  - Audit DB, BT/BD, data layer reliability assessment
  
- **Red Mythos and DR currently taking priority**
  - Will shift after Red Mythos closes (July target)
  - Mike Mitchell helping with daily execution
  
- **Next 3-4 weeks focus:**
  - Infrastructure setup (new JIRA, workflows, standards)
  - Domain definition sessions per team
  - Map ownership, coupling points, target architecture

**Strategic recommendation:** Stay 25/75 through Q4, shift to 50/50 in Q1 2027

### June 1, 2026 - Playback Email
**From:** Marten → CJ (cc Curtis)

Echoes back understanding of CJ's asks:

**Two tracks before capacity shift:**
1. Autonomous Teams - enable nimble, incremental improvements
2. P0 Database Improvements - address largest stability threats

**Four things CJ is asking for:**
1. Definition of done (epic/story level)
2. Way to track progress (milestones, percent complete)
3. How this improves resilience
4. What decoupling work has been done

**Marten's response:**
- DOD: High-level checklists provided (teams not yet ready for epic breakdown)
- Tracking: Will fill in over next few weeks as teams engage
- Resilience: Explains blast radius, recovery time, team accountability
- Decoupling: "I'll follow up with more details"

### June 1, 2026 (Evening) - CJ's Inline Comments ⚠️ CRITICAL
**From:** CJ → Marten (cc Curtis)

**"You got what I am asking for right …let me add more details below."**

#### On Autonomous Teams → Resilience Link:
> **CJ:** "use data from incidents to clarify how this is tied to resiliency"
> 
> **CJ:** "backed by data from incidents… when we built the initial resiliency surge plan … we went through all incidents and use root cause categories to define work. have you seen those decks?"

**Translation:** CJ wants incident-backed proof that autonomous teams solves real problems

#### On P0 Database Work:
> **CJ (Audit DB):** "use metrics to define a clear From and To. Have you seen the detailed work done on DB stabalization by Dermot in the past to get a sense of how data driven we were about a yr ago?"
> 
> **CJ (BT/BD):** "same comment as above"
> 
> **CJ (Data layer reliability):** "same comment as above"

**Translation:** Follow Dermot's model from ~1 year ago - metrics-driven "From → To" for each P0 item

#### On Decoupling Progress:
> **CJ:** "update the box of 'exchange resiliency' in that 1-pager I shared"
> 
> Link: `ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/_layouts/15/Doc.aspx?sourcedoc=%7B480F0475-98C3-4ABA-86D3-52CD6B7E7BBA%7D&file=20260519%20-%20GHX%20India%20Tech%20Org%20All%20Hands.pptx`

**Translation:** Update specific slide in CJ's May 19 India All Hands deck

#### On Oct 1 vs Jan 1:
> **CJ:** "additionally clarify the stability risk if we change the capacity to 50-50 on Oct 1 vs. Jan 1"
> 
> **CJ:** "I met with Steve today and ask him to start thinking about product direction of exchange assuming we have 50-50 capacity starting Oct 1. He is ok doing that but need confidence that we will not change direction. which is essentially only going to come from doing this work."

**Translation:** 
- Need data-backed risk analysis for Oct vs Jan
- Steve (Product) is planning around Oct 1 assumption
- Steve needs confidence = completing this analysis work

> **CJ:** "Do you need a call tomorrow to talk through this or is it clear what I am asking for?"

### June 2, 2026 - Curtis Offers Historical Context
**From:** Curtis → Marten (cc CJ)

"I'll grab those original docs and share with you Mårten. So you have the context."

### June 2, 2026 - Curtis Shares Board Decks
**From:** Curtis → Marten (cc CJ)

Provides links to:
1. **Board update from October 2024:**  
   `Exchange Plan Latest - Copy.pptx`
   
2. **Board update from Feb 2025:**  
   `2025.02 Exchange_Board Deck_Feb.2025.pdf`

**Note:** These decks contain:
- Incident root cause categories from resiliency surge plan
- Dermot's DB stabilization work (the data-driven model CJ references)
- Historical "From → To" metrics

---

## Key Insights from Thread Evolution

### 1. CJ's Communication Style
- Asks high-level questions first (May 22)
- Waits for response (May 28)
- Then adds very specific requirements inline (June 1)
- References prior work as the standard ("Dermot's DB work", "incident root cause categories")

### 2. What CJ Actually Wants
**Not:** Conceptual explanations of why autonomous teams are good  
**Instead:** Data-backed proof using the same methodology GHX used in past resiliency work

**Not:** Generic DB improvement goals  
**Instead:** Metrics-driven "From → To" following established precedent

**Not:** Vague answers about decoupling  
**Instead:** Update specific slide in his deck with concrete progress

### 3. The Historical Precedent Model
CJ references two pieces of prior work as the standard:

**Incident Root Cause Analysis (Resiliency Surge Plan):**
- Went through all incidents
- Categorized by root cause
- Used categories to define work
- **This is the model for linking Autonomous Teams to resilience**

**Dermot's DB Stabilization (~1 year ago):**
- Metrics-driven "From → To" format
- Quantified improvements
- Data-backed approach
- **This is the model for P0 Database work**

### 4. The Steve (Product) Constraint
- Steve is planning product roadmap assuming 50-50 capacity Oct 1
- Steve needs confidence direction won't change
- That confidence comes from completing this analysis work
- **Implication:** This isn't just academic - product decisions hinge on it

### 5. Curtis's Role
- Offers to provide historical context immediately
- Shares Board decks proactively
- Acts as institutional memory / reference librarian
- Helps bridge Marten to CJ's expectations

---

## Action Items Generated (as of June 2)

From CJ's inline comments:

### 1. Autonomous Teams → Resilience Link
- [ ] Review historical incident root cause categories from resiliency surge plan
- [ ] Map current autonomous teams work to those root cause categories
- [ ] Show with data how autonomous teams addresses real incident patterns

### 2. P0 Database Work - Metrics-Driven "From → To"
- [ ] Find Dermot's DB stabilization work from ~1 year ago (model)
- [ ] Gather current metrics for Audit DB (From state)
- [ ] Gather current metrics for BT/BD (From state)
- [ ] Gather current metrics for data layer reliability (From state)
- [ ] Define To state with quantified improvements
- [ ] Link to incident reduction

### 3. Decoupling Progress Documentation
- [ ] Update "exchange resiliency" box in May 19 India All Hands deck
- [ ] Show concrete decoupling work completed
- [ ] Quantify impact (incidents prevented, independence gained)

### 4. Oct 1 vs Jan 1 Risk Analysis
- [ ] Clarify stability risk if shifting to 50-50 on Oct 1
- [ ] Clarify stability risk if shifting to 50-50 on Jan 1
- [ ] Data-backed comparison
- [ ] Give Steve confidence for product planning

### 5. Review Historical Board Decks
- [ ] Read Oct 2024 Board deck (Curtis shared)
- [ ] Read Feb 2025 Board deck (Curtis shared)
- [ ] Extract incident data, DB stabilization model, precedents

---

## References

**SharePoint Links:**
- CJ's May 19 India Tech Org All Hands: `ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/_layouts/15/Doc.aspx?sourcedoc=%7B480F0475-98C3-4ABA-86D3-52CD6B7E7BBA%7D&file=20260519%20-%20GHX%20India%20Tech%20Org%20All%20Hands.pptx`

**Board Decks (Curtis shared June 2):**
- Oct 2024: Exchange Plan Latest - Copy.pptx
- Feb 2025: 2025.02 Exchange_Board Deck_Feb.2025.pdf

**Related Project Files:**
- `CJ_Data_Requirements_Status.md` - Tracking progress on data gathering
- `2026-06-01 Email to CJ - Playback.md` - Original playback (without CJ's inline comments)
- `2026-05-29 CJ Follow-up Call/` - Prior meeting notes and prep

---

**Last Updated:** June 3, 2026  
**Status:** Historical thread context documented, action items in progress
