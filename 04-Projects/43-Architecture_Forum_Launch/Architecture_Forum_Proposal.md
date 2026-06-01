# Architecture Forum - Proposal

**Purpose:** Regular forum for leads and senior engineers to discuss, debate, and align on architecture improvements  
**Goals:**
- Build shared opinions on technical direction
- Create alignment across teams
- Kindle ownership - teams/individuals drive initiatives forward
- Debate trade-offs and alternatives openly

**Launch:** Week of May 12, 2026 (after housekeeping rollout)

---

## Why Now

**Context:**
- Breaking the monolith work needs shared vision across teams
- Database dependencies, deployment independence, service boundaries - need alignment
- Thinktiv/Kickdrum will ask about our architecture direction
- Gen3 vision exists, but how do we get there incrementally?

**From Architecture Anti-Patterns doc:**
> "Never let a crisis go to waste" - We have momentum from resiliency work, India trip pivots, and CJ's strategic asks. Channel it into aligned architectural improvements.

**Current gap:**
- Teams operating somewhat independently
- Architectural decisions happening in silos
- No forum to debate "should we?" before "how do we?"

---

## Format

### Cadence
**Option A:** Weekly, 1 hour (preferred)
**Option B:** Bi-weekly, 1.5 hours

**Recommended:** Start weekly to build momentum, adjust if needed

### Attendees
- **Core:** Tech leads from each team
- **Extended:** Senior engineers (Principal, Staff level)
- **Leadership:** Marten, Daniel, Mike, Ramesh, Aaron (observe/guide, not dictate)
- **Guest speakers:** Invite specific engineers when deep expertise needed

**Estimated size:** 12-18 people (6-8 tech leads/senior engineers + leadership)

**Note:** Final attendee list confirmed after Stage 1 & 2 reviews

### Time
**Recommended:** Thursday afternoons (before end of week, can act on decisions next week)

---

## Meeting Structure (1 hour)

### 15 min: Topic Introduction
- Presenter shares context, problem statement, current state
- Use diagrams, architecture docs, data
- "Here's what we're seeing, here's what we're considering"

### 30 min: Discussion & Debate
- Open floor for questions, alternatives, concerns
- Challenge assumptions
- Explore trade-offs
- Surface risks and dependencies

### 10 min: Decision or Next Steps
- **If ready:** Make architectural decision (document in ADR)
- **If not ready:** Define what's needed (spike, POC, more research)
- **Who owns next steps:** Assign driver

### 5 min: Queue Next Topics
- What's coming up next week/next month
- Prioritize discussion topics

---

## Topic Source: Your Architecture Discussion Backlog

**Existing backlog:** [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]]

You've already cataloged comprehensive topics covering:
- General architecture north star (services vs monolith, no shared DBs, streaming vs batch)
- MongoDB inventory and optimization (EventBus, AuditDB, usage patterns)
- Breaking the monolith (short-term goals)
- Observability (7-day retention, Graylog evaluation, proactive alerting)
- Testing (team-owned quality, inverted pyramid, Tandoori replacement)
- SSO (homegrown IdP evaluation)
- Feature flags
- SDLC metrics

**Recent incidents/discussions to build on:**
- EventBus MongoDB cluster incident (April 17, 2026)
- Audit DB migration challenges (Q1 2026)
- RegCenter decoupling success (Q1 2026)

---

## Suggested First 6 Weeks (Prioritized from Your Backlog)

### Week 1: Kickoff & Scope
**Topic:** What are we trying to accomplish with this forum?
- Review Gen3 vision (from Resiliency Future Plan) - sets "overdo it" boundary
- Review "breaking the monolith" deliverables (from CJ ask) - sets scope for next quarter
- Walk through the Architecture Discussion Backlog - what's here?
- Discuss forum norms: how do we make decisions? Who has veto power?
- **Prioritize:** Vote on which topics from backlog are most urgent

### Week 2: General Architecture North Star
**Topic:** Level set on where we're going (from your backlog)
- More services vs monolith - what does this mean practically?
- No shared databases - how do we get there from here?
- Streaming vs batch architecture - where does this make sense?
- Connection to Gen3 vision and current "breaking monolith" work
- **Outcome:** Shared mental model of target state

**Source:** Architecture Discussion Backlog - "General architecture north star"

### Week 3: Database Dependencies Deep Dive
**Topic:** Shared database anti-pattern - what's the damage?
- Inventory and map dependencies at DB level (which apps/services talk to each DB)
- **Case study:** Audit DB (SFTP/processing shouldn't fail when Audit DB down)
- **Case study:** ActivityFlow pattern (188M docs/day → delete → S3)
- What's the first dependency we should break?
- **Owner:** Volunteer to lead dependency mapping exercise

**Source:** Architecture Discussion Backlog - "MongoDBs in General", "AuditDB (MongoDB)"

### Week 4: EventBus Replacement Strategy
**Topic:** MongoDB-based EventBus → proper queueing/eventing system
- **Context:** April 17, 2026 incident highlighted fragility
- Requirements from backlog:
  - Managed services (SQS, Kafka)
  - Internal SDK with opinionated patterns
  - Native observability with correlation ID tracing
  - Multi-region DR capability
  - Delayed retries with backoff
- Evaluate options, propose architecture
- **Owner:** Volunteer to lead evaluation

**Source:** Architecture Discussion Backlog - "EventBus (MongoDB)", "Recently Discussed"

### Week 5: Breaking the Monolith - Short Term Goals
**Topic:** What are reasonable deliverables for Q2/Q3?
- Align on CJ's 3-5 deliverables (using forum's input)
- Use RegCenter decoupling as success pattern
- Identify next service to extract
- Team ownership and deployment independence criteria
- **Outcome:** Finalize scope for CJ deliverable

**Source:** Architecture Discussion Backlog - "Breaking the monolith", CJ's strategic ask

### Week 6: Observability & Incident Response
**Topic:** Can we catch failures before customers do?
- 7-day log retention - is this enough for incident investigation?
- Proactive alerting gaps (example: 1000s of invoice failures discovered via customer complaint)
- Is Graylog the right tool?
- What observability should each team own vs platform?
- **Case study:** Feed Processor Observability platform success (Q1 2026)

**Source:** Architecture Discussion Backlog - "Observability", "Current Problems"

---

## Ongoing Topic Sources

**Primary source:** [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]]

Your backlog already has rich topics organized by category:
- **Current Problem/Opportunity Areas:** MongoDB optimization, testing strategy, SSO evaluation, feature flags, SDLC metrics
- **Current Problems:** Documented pain points (monolith coupling, batch processing, observability gaps)
- **Opportunities:** EDI to JSON migration, streaming architecture, AI enablement
- **Proposed Improvements:** Prioritized improvements with clear goals
- **Tech Debt:** AWS SDK 2.0, Linux 2023, vulnerability remediation, Tandoori replacement
- **Recently Discussed:** Context from recent incidents and decisions

**How to add new topics:**
1. **Team pain points** - Team leads add to backlog when hitting architectural friction
2. **Incidents** - Post-mortems generate topics (example: EventBus April 17 incident → Week 4 topic)
3. **Strategic initiatives** - CJ's asks, Gen3 planning, Thinktiv/Kickdrum findings
4. **New capabilities** - Teams propose new services/patterns for forum alignment

**Backlog maintenance:** Update `Architecture_Discussion_Backlog.md` with new topics and mark discussed items as "Recently Discussed"

---

## Decision-Making Model

### Types of Decisions

**Type 1: Reversible (Easy to undo)**
- Experiment, gather data, reverse if needed
- Example: Try new testing framework on one service
- **Decision maker:** Team lead with forum input

**Type 2: Irreversible (Hard/expensive to undo)**
- Need broader alignment and careful consideration
- Example: Choose new database technology, extract major service
- **Decision maker:** Consensus in forum, escalate to Marten/Daniel/Mike if no consensus

### Documentation
- **Architecture Decision Records (ADRs):** Document significant decisions in `docs/adr/` in relevant repo
- **Confluence:** Link ADRs from forum meeting notes
- **Backlog maintenance:** After each session, update [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]]:
  - Move discussed topic to "Recently Discussed" section with date
  - Add any new topics that emerged from discussion
  - Update "Next Steps" based on decisions/owners
- **Communicate:** Share decisions in #exchange-all or team channels

---

## Success Metrics (3 Months)

**Qualitative:**
- [ ] Teams report feeling more aligned on technical direction
- [ ] Senior engineers feel heard and valued in architectural discussions
- [ ] Decisions are being made and acted on (not just discussions)
- [ ] Architectural improvements are happening across teams (not just one team)

**Quantitative:**
- [ ] 10+ architectural decisions documented (ADRs)
- [ ] 3+ teams have driven initiatives from forum discussions
- [ ] Database dependencies reduced (measurable via deployment independence)
- [ ] Forum attendance remains high (>80% of invites attending)

**Watch out for:**
- Forum becomes "talking shop" with no action
- Decisions aren't being implemented (assign owners!)
- Only Marten/Daniel/Mike talking (need to empower engineers)
- Topics are too tactical (code reviews) or too abstract (no actionable outcome)

---

## Confluence Setup

**Page:** `Exchange/Architecture Forum`

### Sections:
1. **Purpose & Norms** - What this forum is, how we make decisions
2. **Meeting Schedule** - Recurring calendar invite, time, location
3. **Topic Backlog** - Link to [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]] (source of truth)
4. **Upcoming Topics** - Next 4-6 weeks scheduled (copied from backlog)
5. **Meeting Notes** - Archive of past discussions and decisions
6. **ADR Index** - Links to all architectural decisions made

### Upcoming Topics Section Format:
```markdown
## Upcoming Topics (Next 6 Weeks)

**Source:** [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]]

- **Week 1 (May 12):** Kickoff & Scope - Review Gen3 vision, prioritize backlog
- **Week 2 (May 19):** General Architecture North Star - Services vs monolith, no shared DBs, streaming vs batch
- **Week 3 (May 26):** Database Dependencies Deep Dive - Inventory, Audit DB case study, ActivityFlow pattern
- **Week 4 (Jun 2):** EventBus Replacement Strategy - MongoDB → proper queueing (SQS, Kafka evaluation)
- **Week 5 (Jun 9):** Breaking the Monolith - Short term goals, align on CJ deliverables
- **Week 6 (Jun 16):** Observability & Incident Response - 7-day retention, proactive alerting, Graylog evaluation

### How to Propose New Topics
1. Add to [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]] under appropriate section
2. Bring to forum for prioritization vote
3. Once scheduled, add to "Upcoming Topics" with date
```

---

## Review Process & Talking Points

### Stage 1: Leadership Review (Daniel, Mike, Ramesh, Aaron)

**Purpose:** Get alignment on forum structure and strategic fit

**Talking points (15-20 min):**

1. **Context (3 min):**
   - We have a rich Architecture Discussion Backlog but no forum to work through it
   - Need shared opinions on architecture improvements across the org
   - CJ's "breaking monolith" ask requires alignment on what we're doing

2. **Forum format (5 min):**
   - Weekly, 1 hour (or bi-weekly 1.5 hours - your input?)
   - Tech leads + senior engineers from each team
   - 15 min topic introduction, 30 min debate, 10 min decision, 5 min queue next
   - Document decisions in ADRs

3. **First 6 topics (5 min):**
   - Walk through Week 1-6 from seed topics
   - Based on existing Architecture Discussion Backlog
   - Week 5 specifically addresses CJ's deliverable

4. **Decision-making model (3 min):**
   - Reversible decisions: Team lead with forum input
   - Irreversible decisions: Consensus in forum, escalate if needed
   - Not a rubber-stamp - real debate and alternatives

5. **Ask (2 min):**
   - Alignment on launching this?
   - Weekly or bi-weekly preference?
   - Who from your teams should attend?
   - Time slot preferences?

**Key message:** *"This is how we build architectural alignment AND develop senior engineering talent."*

---

### Stage 2: EM Group Review (All Engineering Managers)

**Purpose:** Get buy-in from EMs who will send their tech leads/senior engineers

**Talking points (15 min):**

1. **What is this (2 min):**
   - Weekly architecture forum for tech leads and senior engineers
   - Leadership already aligned (Daniel, Mike, Ramesh, Aaron)
   - Starting week of May 12

2. **Why this matters for your team (3 min):**
   - Your tech leads get voice in architectural direction
   - Builds cross-team alignment (reduces surprises)
   - Develops your senior engineers' architectural thinking
   - Creates distributed ownership of architectural improvements

3. **What we're asking (3 min):**
   - 1 hour/week commitment for your tech lead(s) and/or senior engineers
   - Encourage them to bring team pain points as discussion topics
   - Support them driving architectural initiatives that come out of forum
   - This is investment in their growth, not "extra meetings"

4. **Sample topics (3 min):**
   - Database dependencies (affects everyone's deployment independence)
   - EventBus replacement (April incident)
   - Breaking the monolith short-term goals
   - Observability improvements

5. **Logistics (2 min):**
   - Calendar invite coming this week
   - Confluence page with backlog and meeting notes
   - First session is kickoff - scope and prioritize topics together

6. **Q&A (2 min):**
   - Address concerns about time commitment
   - Clarify attendee expectations
   - Collect scheduling constraints

**Key message:** *"Your tech leads will help shape architectural direction, not just receive it. This is leadership development."*

---

## Rollout Plan

### Week of May 5 (This Week)

**Stage 1: Leadership Review**
- [ ] Review with Daniel, Mike, Ramesh, Aaron
- [ ] Get alignment on:
  - Forum purpose and format
  - Weekly vs bi-weekly cadence
  - Decision-making model
  - First 6 topics from backlog
  - Who should attend (tech leads, senior engineers)

**Stage 2: EM Group Review**
- [ ] Review with all EMs (Daniel's, Mike's, Ramesh's, Aaron's teams)
- [ ] Get buy-in on:
  - Sending their tech leads/senior engineers
  - Supporting time commitment (1 hr/week)
  - Encouraging team ownership of architectural initiatives
- [ ] Collect feedback on topics and format

**Finalization:**
- [ ] Incorporate feedback from both review stages
- [ ] Confirm attendee list
- [ ] Find time slot that works

### Week of May 12
- [ ] Send calendar invite for recurring meeting
- [ ] Create Confluence page with purpose, norms, backlog link
- [ ] Communicate launch in staff meeting and #exchange-all
- [ ] **First session:** Kickoff & scope (Week 1 from seed topics)

### Week of May 19 onwards
- [ ] Run weekly sessions with seed topics
- [ ] Document decisions in ADRs
- [ ] Track action items and owners
- [ ] Update Architecture Discussion Backlog after each session

---

## Communication Draft

**Note:** Send after both Stage 1 (leadership) and Stage 2 (EM) reviews are complete and format is finalized.

### Slack Message (to #exchange-all)

```
🏗️ **New: Architecture Forum - Starting Week of May 12**

We're launching a weekly forum for tech leads and senior engineers to discuss, debate, and align on architecture improvements.

**Why:** 
- Build shared opinions on technical direction
- Create alignment across teams
- Empower teams to drive architectural initiatives

**Who:**
- Tech leads from each team
- Senior engineers (Principal, Staff)
- Daniel, Mike, Marten (observe/guide)

**When:** 
- Weekly, 1 hour
- Starting Week of May 12 (specific time TBD)

**Format:**
- Topic introduction (15 min)
- Discussion & debate (30 min)
- Decision or next steps (10 min)
- Queue next topics (5 min)

**First topics:**
- Database dependency decoupling
- MongoDB ActivityFlow patterns
- Lambda migration acceleration
- Service boundaries for team autonomy

**Details:** [link to Confluence page]

**Questions?** Reach out to Marten or your EM.
```

---

## Tips for Success

### For You (Marten)
- **Facilitate, don't dictate** - Let engineers drive the discussion
- **Ask questions, don't give answers** - "What alternatives did you consider?" "What's the trade-off?"
- **Assign owners** - Every discussion ends with "Who's driving this forward?"
- **Celebrate progress** - Shout out teams who implement architectural improvements

### For Daniel/Mike
- **Coach your tech leads** - Help them prepare good proposals
- **Encourage debate** - Healthy disagreement leads to better decisions
- **Follow up on action items** - Check in with owners between meetings
- **Surface team pain points** - Bring architectural friction your teams are hitting

### For Tech Leads/Senior Engineers
- **Come prepared** - If presenting, have diagrams and data ready
- **Challenge respectfully** - Ask hard questions, but be constructive
- **Own initiatives** - Volunteer to drive architectural improvements
- **Share learnings** - What worked, what didn't, what would you do differently

---

## Connection to Strategic Pillars

### Organizational Foundation (People & Process)
- ✅ Develops senior engineering talent through meaningful architectural discussions
- ✅ Creates forum for cross-team collaboration and alignment
- ✅ Empowers engineers to drive technical direction (not top-down)

### Breaking the Monolith → Autonomous Teams
- ✅ Defines service boundaries and ownership
- ✅ Addresses database dependencies blocking independence
- ✅ Enables teams to deploy independently through architectural decoupling

### AI Native Software Development Process
- ✅ Well-documented architecture (ADRs) improves AI code generation context
- ✅ Clear architectural patterns enable AI-assisted refactoring

### Critical Technical Execution
- ✅ Proactively addresses architectural risks before they become incidents
- ✅ Accelerates resiliency improvements through aligned action
- ✅ Creates forcing function for technical debt prioritization

---

## Alignment with CJ's Asks

**"Breaking the Monolith" Deliverables:**
- This forum is HOW you define and drive those deliverables
- Tech leads own the execution, forum provides alignment
- Decisions documented (ADRs) show clear scope and completion criteria

**Productivity Assessment:**
- Forum demonstrates engineering investment in architecture
- ADRs and completed initiatives are concrete productivity evidence
- Shows leadership development of senior engineers

**Capacity Roadmap:**
- Architectural improvements unlock capacity for product work
- Forum prioritizes which technical work enables most product velocity
- Visible connection between tech investment and business outcomes

---

## Related Documents

- **[[06-Resources/Architecture/Architecture_Discussion_Backlog.md]]** - Master topic backlog (primary source)
- [[06-Resources/Architecture Principles and Anti-Patterns.md]] - Architectural friction and patterns to address
- [[04-Projects/Exchange Platform Architecture/Architecture Picture/Architecture Flaws, Improvement Areas.md]] - Known issues
- [[00-Inbox/Kickdrum Prep from Confluence.md]] - Resiliency Future Plan (Gen3 vision and scope boundary)
- [[00-Inbox/Key_Talking_Points_From_Confluence.md]] - Current architecture state from Confluence
- [[00-Inbox/Meetings/2026-05-01/Technical_Priorities_Review.md]] - CJ's "breaking the monolith" ask

---

*Created: 2026-05-01*  
*Owner: Marten Engblom*  
*Reviewers: Daniel Milburn, Mike Mitchell*  
*Launch: Week of May 12, 2026*
