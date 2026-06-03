---
date: 2026-05-29
type: Strategic Conversation
participants: 
  - [[Marten_Engblom|Marten Engblom]]
  - [[Curtis_Schroeder|Curtis]]
tags: [resiliency, communication, board-pressure, definition-of-done]
related_projects:
  - Exchange Modernization
status: action-items-pending
---

# Debrief with Curtis - Communication Strategy & CJ Alignment

**Context:** Follow-up call with Curtis to unpack a confusing conversation with CJ about resiliency work definition, timelines, and board reporting requirements.

---

## The CJ Communication Gap

### What Happened
- **CJ's question:** "What's the definition of done for the resiliency spike / breaking the monolith?"
- **Your answer:** Teams operating autonomously + first pass at database layer = ready to shift capacity (end of Q4)
- **CJ's response:** "That's not specific enough. How does this improve resiliency? What Curtis put in the box isn't what's happening on the ground."

### The Confusion Loop
You kept going in circles because:
1. CJ wants **specifics** (lists, services, milestones, percent complete)
2. You're giving **conceptual outcomes** (autonomous teams, database improvements)
3. CJ's asking "how does this improve resiliency?" even though his stated need is "when can we shift capacity?"
4. He never explicitly said "I need to track progress" - but that's what he means

### Curtis's Interpretation
**Root cause:** Board meeting pressure (2 weeks out)
- CJ needs to show **clear milestones** and **measurable progress**
- He promised resiliency work done by summer 2025 (now 1 year late)
- Getting daily pressure: "No capacity because resiliency work"
- Board wants: Definition of done, percent complete, progress tracking

**Translation:** CJ's not questioning the strategy - he needs a **reporting framework**

---

## The Strategic Reframe

### What CJ Actually Needs

**Framework:** Initiatives → Epics → Stories with trackable milestones

#### Initiative: Exchange Resiliency & Decoupling

**Two pillars:**

##### 1. Data Layer Stability (P0 Database Work)
Epics:
- **Audit DB re-architecture**
  - Question: Do we even need this? Defensible use case?
  - If yes: Explore S3 storage instead of Mongo
  - If no: Sunset the feature
- **BTBD scalability deep-dive**
  - Review past reliability incidents
  - Identify data architecture improvements
  - Right-size storage requirements
- **Event bus replacement**
  - Replace Mongo-based event bus with proper messaging solution
  - Current state: Tuned but wrong tool
  - Not a P0 stability issue, but architectural debt
- **S3 storage optimization** (P1, not P0)
  - Stop writing 50 copies of each document
  - Challenge 11-year retention policy for all snapshots
  - Estimated impact: $1M/year savings

**Definition of done:** P0 database issues resolved (audit DB + BTBD stabilized, event bus replaced)

##### 2. Team Decoupling & Autonomous Deployment
Epics:
- Move all code to GitHub
- Each team has 1+ deployment pipelines they own
- Teams can deploy weekly without cross-team coordination
- Team standards implemented (Jira + Compass + metrics)

**Definition of done:** Each team box in org chart = separate deployment pipeline(s) + averaging 1 deploy/week

---

## Key Insights from the Call

### The Services Red Herring
CJ kept asking "how many services are you creating?"
- **Reality:** Might not create new services at all
- **What we're doing:** Carving up monolith, detangling dependencies, enabling independent deployment
- **The trap:** Listing "services being extracted" feels like small potatoes if scrutinized
- **The risk:** Kick Drum sees the list and thinks "this is the resiliency work? Get new staff."

### The Stability Question
CJ: "How does autonomous teams improve resiliency?"
- **Your struggle:** It doesn't directly - it enables us to work on resiliency incrementally without blocking commercial work
- **What you said:** "Truthfully not much in and of itself. The P0 database work will have outsized impact."
- **Curtis's POV:** We don't have before/after data, so proving stability improvement is impossible
  - Throughput is up → solving problems faster
  - Decoupled teams → can track uptime per service (future capability)
  - But no baseline metrics from before

### The Communication Pattern
Curtis's advice: "Just keep saying the same things over and over"
- Decoupling = (1) breaking apart teams for independent deployment (people + tech), (2) fixing data layer first pass
- Some people just need repetition to internalize concepts
- CJ might have been having an off day / one-off weird conversation

---

## The Email Strategy

### What to Send CJ
1. **Echo back understanding:** "It sounds like you need two things - definition of done for decoupling, and how it impacts resiliency"
2. **Reframe as initiatives/epics:** Present the two-pillar structure above
3. **Include examples:** Pull together specific things being decoupled (databases, tables, etc.) - but position as supporting evidence, not the main event
4. **Timeline & tracking:** Note that JIRA boards will be ready end of next week with epics/stories visible
5. **Acknowledge pressure:** "I understand you need trackable progress for board reporting - here's the framework"

### What to Avoid
- Long responses generate more questions
- Giving him a list of "small potato" technical tasks that can be second-guessed
- Pretending autonomous teams directly improve stability (they enable future stability work)

---

## Broader Context

### Other Teams' Capacity
You: "Are we really the bottleneck? 16% of company is Exchange."
Curtis: 
- Content team: ~100 people, struggling with Data Connect product
- Credentialing: 50 people maintaining non-growth product
- Data teams: Some senior leaders leaving, whispers about AI project challenges
- Exchange: Target 75 people (down from 110, already cut 25%)

**Reality check:** Exchange might be getting disproportionate scrutiny

### Product Vision Pressure
CJ to Steve: "Give me a product vision"
Steve to CJ: "Why rush? No capacity - it's all resiliency work"
→ CJ needs to tell Steve when capacity shifts
→ Your answer: End of Q4
→ CJ wants proof of progress toward that date

---

## Action Items

### Immediate (This Week)
- [ ] **Draft email to CJ** - Echo back understanding with initiative/epic framework [[^task-20260601-001]]
- [ ] **List decoupling examples** - Pull from teams what's actually being separated [[^task-20260601-002]]
- [ ] **Document P0 database work** - Expand audit DB / BTBD / event bus specifics [[^task-20260601-003]]

### Next Week (Team Meetup Mon-Wed)
- [ ] **JIRA board tickets submitted** - Create spaces for Exchange work tracking
- [ ] **Architecture forum** - Start discussion on what gets decoupled when [[^task-20260601-004]]
- [ ] **Team standards finalization** - Nail down workflow, statuses, compass integration
- [ ] Curtis considering flying out to join

### Near-Term (2 Weeks)
- [ ] **JIRA boards populated** - Fill with Q3 work including initiative/epic structure
- [ ] **Reporting demo** - Show CJ how he'll see roadmap, initiatives, progress tracking
- [ ] **Piggyback rollout** - Curtis will adopt Exchange's standards for other teams

---

## Relationship Notes

### Curtis
- **Communication style:** Supportive, pattern-matcher, translates CJ's pressure into actionable context
- **His challenge:** "My biggest challenge is just communicating with CJ. Far and away the thing that takes most of my time."
- **His frustration:** Wants to spend time teaching engineering practices, not managing up constantly
- **Confidence in your direction:** "From my side, you're still heading in the right direction. We just have a communication gap with the boss man."

### CJ
- **Current state:** Board meeting in 2 weeks, anxious about demonstrating progress
- **Pressure sources:** Daily questions about capacity, Steve asking for product vision, promised resiliency done a year ago
- **Communication pattern:** Remembers by testing, not grilling - asks questions to get up to speed
- **What he needs:** Vocabulary that maps to "services" and checklists, even if that's not how you think about it

---

## Quotes Worth Remembering

**On proving stability improvements:**
> "How do you prove something that was never measured? Like how do I prove I got better with data if we never had the data of how it used to be?" — Curtis

**On CJ's mindset:**
> "I want the end result. I don't want the steps to get to the end result. I just want the result." — Curtis describing CJ's perspective

**On the contradiction:**
> "If you really want to know when is all the resiliency work done? Well that's like 2029 or you know. And the whole point is we're setting ourselves up so we don't have to do it in the context of the monolith." — You

**On capacity timeline:**
> "He's like 'what if we decrease the scope of resiliency work so we can shift capacity end of Q3 instead of Q4?' And those two things don't even go together - it's so contradictory." — You

---

## Next Steps

1. **Write that email** - Echo back CJ's asks with initiative/epic structure
2. **Build the tracking framework** - JIRA boards → epics → stories with percent complete
3. **Keep Curtis in the loop** - He's piggybacking on your standards rollout
4. **Team meetup prep** - Architecture discussions will inform what actually gets decoupled
5. **Stay confident in the strategy** - Curtis confirmed Kick Drum said the exact same things 2 hours earlier

---

**Last Updated:** 2026-05-29
**Status:** Email draft pending, team meetup next week, JIRA boards in progress
