# Exchange Incident Games 2026 - READOUT

**Date:** 2026-05-08  
**Time:** 8:00 AM - 10:00 AM (1h 34m 42s)  
**Location:** Microsoft Teams Meeting

## Attendees
Pete Ferguson (facilitating), Marten Engblom, Daniel Milburn, Adam Gordon, Suresh Kumar, Piyush Srivastava, Matthew Turner, Pratik Panchal, Gregory Bank, Philippe Scoffie, Aaron (mentioned), Jeff Sherard, others

## Agenda
- Review DR exercise readout and gather feedback on gaps/concerns
- **Evolved into:** Strategic discussion on monolith decoupling vs DR prioritization

**Note:** Full unedited transcript saved to: [`Exchange_Incident_Games_2026_READOUT_TRANSCRIPT.md`](./Exchange_Incident_Games_2026_READOUT_TRANSCRIPT.md)

---

## Executive Summary

**Part 1 - DR Exercise Results:** Recent stage DR test showed promising RTO reduction to ~7 hours (from 13+ hours in December), with projections of 2-3 hours once Atlas/Elasticsearch migrations complete. However, significant manual dependencies and human coordination gaps remain concerns.

**Part 2 - Strategic Pivot:** Meeting evolved into intensive 70-minute discussion about **fundamental approach to monolith decoupling**. Team debated whether to prioritize DR automation work vs aggressive decoupling strategy. **Emerging consensus: "Lift and shift" approach** where teams carve out their domains (even if messy initially) to achieve autonomy, which naturally delivers DR capabilities as byproduct.

**Critical Insight:** The discussion revealed organization-wide recognition that **autonomous teams are the #1 unlock** - everything becomes easier after decoupling, even if first pass is imperfect.

---

## Part 1: DR Exercise Readout (Pete Ferguson)

### RTO Timeline Analysis

**Actual Performance:**
- **Total RTO:** 7 hours 9 minutes (missed 4-hour target)
  - 2.5 hours: Database restoration (pre-drill, not counted in December)  
  - 4 hours 45 min: Day 1 drill execution
  - Additional time: Day 2/3 SSO troubleshooting

**Projected with Infrastructure Upgrades:**
- **With Atlas:** ~4 hours 39 min (eliminates 2.5hr database restore)
- **With Atlas + SSO fixes:** ~2 hours 15 min (well under target)

### Key Failures

1. **Bamboo Plan Outdated** - Plans from December inconsistent with current state
2. **Stage vs Production Gaps** - Some differences need documentation before October prod test
3. **DNS Service/SSO Issues** - Spent entire extra day troubleshooting, undocumented User API had to be rebuilt mid-incident
4. **Route 53 Not Pre-staged** - Manual updates required
5. **Lambda Cold Start** - Lambdas in stage expire if not exercised regularly
6. **Human Dependencies** - Heavy reliance on specific people for troubleshooting

### Time Additions Identified

- **Name Drift:** 30 minutes (Corex stage infra vs Corex stage commons)
- **SSO Coordination:** 44 minutes  
- **Waiting for Verbal Confirmations:** No automated readiness checks
- **Manual CloudFront/DNS Updates**

### Key Improvements

Significant time savings across most categories compared to December baseline

### Future Considerations

- Next large-scale test will include CCX and other products
- Getting Exchange to 4 hours doesn't mean all dependent products are up
- Need well-documented procedures to reduce dependency on specific individuals

---

## Part 2: Strategic Monolith Decoupling Discussion

### The Central Debate (70% of meeting)

**Triggered by:** Pete's observation that human dependencies in DR are "scary" - "What if 2-3 key people aren't available?"

**Three Approaches Debated:**

1. **DR-First Approach (Adam's initial position)**
   - Focus on automating current DR gaps
   - Decouple later after October deadline met
   - **Concern:** Builds throwaway bamboo automation, doesn't solve root problem

2. **Decouple-First Approach (Marten's position)**  
   - Prioritize aggressive monolith breakup
   - DR capabilities come "for free" as byproduct
   - **Concern:** Timeline risk - might miss October DR deadline

3. **Hybrid/Pivot Approach (Discussion outcome)**
   - Start decoupling now, pivot to DR prep if tracking poorly mid-quarter
   - "Lift and shift" / "clone and delete" strategy for teams

### "Lift and Shift" Strategy (Daniel's Breakthrough Idea)

**Core Concept:** Teams don't need perfect SOA architecture initially - just need autonomy.

**Approach:**
- Each team copies what they need from monolith (overlapping Venn diagrams OK initially)
- Delete what they don't own
- Accept temporary code duplication across teams
- Data layer coupling remains initially - tackle later
- **Goal:** Get to independently deployable state "at any cost"

**Marten's Framing:**
```
"If 12 teams all made a copy of the monolith, 
it's STILL better than where we are today."
```

### Team Reactions & Concerns

**Suresh Kumar (Pragmatic Concerns):**
- Integration complexity: Even isolated services need to integrate with rest of Exchange
- Example: Adapter API built fast but integration took year+ due to priorities
- Relationship validation changes ripple across 10+ places
- **Counter:** Marten argues this is acceptable trade-off for autonomy

**Piyush Srivastava (Domain-Driven Design Advocate):**
- Need proper domain modeling first
- IO team should own document data, provide APIs to others  
- Current library-based sharing creates tight coupling
- **Phase 1:** Identify domains (already done via team structure)
- **Phase 2:** True domain ownership with service boundaries
- **Acknowledges:** Takes long time, difficult while in monolith

**Matthew Turner (Boundary Clarity):**
- **Key Problem:** "Teams don't understand what they own and what they don't own"
- Example: Actions + Transformations teams have crossover, both depend on Events rules/routing
- Product doesn't understand boundaries either - get requests for wrong teams
- **Critical Need:** Define boundaries down to folder level in mono repo

**Adam Gordon (Org Team Lead):**
- Initially low confidence in October timeline for full decoupling
- Open to "lift and shift" approach - hadn't considered it
- **Key Question:** "Can we do a lift and shift of what we own in Bitbucket?"
- If locked in basement with no distractions: "Absolutely confident we can get it done"
- Concerns are about competing priorities, not technical feasibility

**Gregory Bank (Voice of PTSD):**
- "This is about the 5th or 6th time we've heard all this"
- Previous attempts: Full prep, then nothing - rug gets pulled out
- **"Cautiously optimistic"** but hard to get hopes up
- **Key Frustration:** Too many competing #1 priorities
- Needs consistent messaging and protected capacity

**Pratik Panchal (SSO Perspective):**
- Currently decoupling SSO from org data dependencies (SMTP config, etc.)
- Making pragmatic decisions: Leave data with Org temporarily
- Once application boundaries clear, can tackle persistence layer
- **Supporting lift-and-shift:** Can make temporary compromises

**Pete Ferguson (Leadership Perspective):**
- **"This time IS different"** - new leaders have done this before at other orgs
- Heavy investor scrutiny - daily PowerPoints on incidents, DR, everything
- **"This train is moving"** - not stopping this time
- Acknowledges team PTSD is real and valid

### Consensus Points

1. **#1 Priority:** Get to autonomous team state - "everything becomes easier"
2. **Accept Imperfection:** First pass will be messy, duplicated code OK
3. **Data Layer Separate:** Don't tackle database decoupling in Phase 1
4. **Domain Definition Critical:** Need boundaries down to folder/component level
5. **Product Alignment:** Laura fully supportive - "Take capacity you need"
6. **Definition of Done Needed:** So it's not endless black hole
7. **Learn as We Go:** Cross bridges when we get there vs waterfall planning

### Key Insights & Quotes

**On Autonomy as Unlock:**
> "Everything is a project right now because you're coordinating 80 engineers across monolith. After decoupling, things become easier - not easy, but easier." - Marten

**On Trade-offs:**
> "We'd rather have duplicated code for autonomy. That's a pretty healthy trade." - Daniel Milburn

**On Starting:**
> "The key is we have to start somewhere. The iceberg is very big. We just gotta chip away at it." - Adam Gordon

**On Past Failures:**
> "The problem is the company comes in and says these glass balls are now rubber balls, these are the new glass balls." - Gregory Bank

**On Pragmatism:**
> "Damn the torpedoes approach - #1 goal is carve out your domain, get to autonomy at any cost." - Marten

---

## Decisions Made

### DR Exercise Decisions
1. **Accept current RTO projections** (2-3 hours with Atlas/ES) as meeting contractual obligation
2. **Plan October production DR test** after Atlas/Elasticsearch complete (end August)
3. **Focus automation on high-ROI items** - not all gaps need scripting
4. **Document stage/prod differences** clearly before October
5. **Schedule mid-September full test** including Fusion, SCA, CCX

### Strategic Decoupling Decisions
1. **Decoupling is #1 organizational priority** - unanimous agreement
2. **Adopt "lift and shift" / "clone what you need" approach** - not one-size-fits-all
3. **Teams define their domains** down to folder level by May 18th week
4. **Weekly planning meetings** - next Friday (May 15), then May 22  
5. **Q3 capacity allocation** - product (Laura) supportive of taking what's needed
6. **Defer data layer decoupling** - focus on deployment autonomy first
7. **Protect the work** - leadership accountable for shielding from priority shifts

---

## Action Items

### DR Readout Follow-ups
- [ ] Review automation epic backlog for ROI analysis [[^task-20260508-012]]
- [ ] Document all stage/prod differences before October [[^task-20260508-013]]
- [ ] Test SSO deployment scripts individually before September [[^task-20260508-014]]
- [ ] Plan mid-September full DR test (Fusion, SCA, CCX) [[^task-20260508-015]]

### Domain Definition (Critical Path)
- [ ] **Each team:** Define what you own down to folder/component level by May 18 [[^task-20260508-016]]
- [ ] **Matthew Turner:** Get Daniel's component list, create shared document structure [[^task-20260508-017]]
- [ ] **Matthew Turner + Philippe:** Set up shared canvas/hub for domain definitions [[^task-20260508-018]]
- [ ] **Aaron/Ben/Matt Turner:** Coordinate on domain breakdown spreadsheet [[^task-20260508-019]]
- [ ] **Aaron + Daniel:** Write definition of autonomous teams for staff page [[^task-20260508-020]]
- [ ] **Aaron:** Draft definition of done for decoupling work [[^task-20260508-021]]

### Team-Specific Spikes
- [ ] **Adam Gordon (Org team):** Meet with John Tuesday - assess lift-and-shift feasibility [[^task-20260508-022]]
- [ ] **Adam Gordon:** Run discovery spikes on org decoupling boundaries [[^task-20260508-023]]
- [ ] **All Teams:** Review DR gaps spreadsheet, add notes on relevance/approach [[^task-20260508-024]]

### Meetings & Planning
- [ ] **Pete Ferguson:** Schedule weekly planning meetings (May 15, May 22) [[^task-20260508-025]]
- [ ] **Domain Review Sessions:** Week of May 18 - sanity check each team's definitions [[^task-20260508-026]]
- [ ] **Q3 Planning:** Incorporate decoupling work with clear definition of done [[^task-20260508-027]]

---

## Follow-ups

**Immediate (Next Week):**
- Friday May 15: Weekly planning session (1 hour) - ideation, no PowerPoints
- Teams working on domain definitions

**May 18 Week:**
- Domain review sessions with each team
- Sanity check boundaries and ownership

**Q3 (Starting ~June):**
- Full focus on decoupling work  
- Teams executing lift-and-shift in their own way
- Weekly check-ins to maintain momentum

**August-September:**
- Atlas/Elasticsearch migrations complete (end August)
- Mid-September: Full DR test including all products
- October: Production DR flip-and-stay

**Long-term:**
- After autonomous state achieved: Tackle data layer decoupling
- Continue incremental improvements to each team's domain
- Identify shared libraries that warrant extraction to artifactory

---

## Related

**People:** Pete Ferguson, [[Marten_Engblom|Marten Engblom]], [[Daniel_Milburn|Daniel Milburn]], Adam Gordon, Suresh Kumar, Piyush Srivastava, Matthew Turner, Pratik Panchal, Gregory Bank, Philippe Scoffie, Jeff Sherard, [[Aaron_Srivastava|Aaron Srivastava]] (mentioned), Curtis (referenced), [[CJ_Singh|CJ]] (referenced), Laura (referenced), Venkatesh (mentioned), Trevor (mentioned), Ben (mentioned), John (mentioned), Banks (mentioned)

**Projects:** [[04-Projects/Exchange_Resiliency_2026]], Exchange Atlas Migration, Exchange Elasticsearch Migration, Monolith Decoupling Initiative

**Companies:** Cardinal (DR contractual obligation driver)

**Context:** This meeting represents a critical inflection point where DR concerns catalyzed recognition that **architectural transformation is prerequisite to operational excellence**. The extended strategic discussion (70% of meeting time) shows organization-wide alignment emerging on aggressive decoupling approach, with leadership commitment to protect the work from competing priorities that derailed past attempts.

**Key Tension:** Balance contractual DR obligation (October deadline) with long-term architectural transformation. Resolution: Decoupling work naturally delivers DR capabilities, making it highest-leverage path forward.

---

*Created: 2026-05-08*  
*Full Transcript: Exchange_Incident_Games_2026_READOUT_TRANSCRIPT.md (874 lines)*
