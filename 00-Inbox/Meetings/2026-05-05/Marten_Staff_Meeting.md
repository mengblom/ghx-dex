---
date: 2026-05-05
participants:
  - Marten Engblom
  - Aaron Srivastava
  - Daniel Milburn
  - Ramesh Rangavithal Donnipadu
  - Michael Mitchell
tags:
  - meeting
  - staff-meeting
  - leadership
meeting_type: staff_meeting
source: teams_transcript
---

# Marten Staff Meeting - May 5, 2026

## Round-Robin Updates

### Aaron Srivastava - Red Mythos & Automated Deployments

**Automated Deployments Discussion:**
- Exploring automated deployments to production for smaller repos as teams break off from monolith
- **Not recommended for the All repo** currently due to culture shift needed
- Target environment: **OSS** (all other environments needed for other migrations)
- Feature flags will be key enabler - cultural shift needed so teams think "this PR goes to prod immediately"
- Historical context: Deployed All repo 95 times mid-day in automated fashion before a bug caused business pushback
- Resistance sometimes comes from product side (user manual updates, training prep, go-to-market strategy)

**Red Mythos Progress:**
- **Target environment:** OSS - Ben starting work on automated tests in this environment
- **Testing resources:** P.Bob allocated 1 person for testing + 1 lead to guide
- **Library upgrade decisions:**
  - Smooks: Deferring (business critical, don't rush)
  - Mitra ID: Deferring (end of life, needs replacement - big effort)
  - Focus: Fix all other vulnerabilities, take the hit on these two
- **Golden AMI Pipeline:** Meetings this week with DevOps to get automated AMI refresh pipeline
  - Goal: Refresh underlying servers frequently to stay ahead of critical SLA on infrastructure vulnerabilities
  - Plan: Weekly production refreshes after soak testing in Dev/lower environments
  - Process: Get list of updates before deployment to vet, then automate rollout
- **Timeline:** First VM fix probably 1-2 weeks out (OSS environment still being set up)

**Key concern:** Need to verify with DevOps that redeploying same code with new AMI won't break things (library incompatibilities historically an issue)

### Daniel Milburn - Vendor Management (Happiest Minds)

**Current State:**
- Daniel has traditionally managed Happiest Minds relationship and resource allocation
- **Standing calls:**
  - Monthly with Sujith (Program Director)
  - Weekly/as-needed with Ramya (Delivery Manager)
- Resource management includes people movements between teams (e.g., Naga Raju backfilling Aravu, Tamil backfilling him, OSS team backfilling Tamil)
- ~70% resource changes are their choice, 30% are GHX-initiated due to performance issues

**Decision: Distribute ownership across Directors**
- Daniel will ask Ramya to reach out to Ramesh and Mike to set up direct relationships
- Each director should involve their EMs in resource discussions as appropriate
- Aaron can shuffle issues to Daniel if needed for OSS team
- Marten will engage at exec level (Sujith has been asking for monthly check-ins)

**Performance Management Concerns:**
- **Mixed quality:** Some contractors very good (long tenure, know the system), others not as useful
- **Ramesh (Visibility team):** 7 contractors total, 2-3 are very helpful, not everyone equally useful
- **Mike (Continuity/ICS teams):** Bar acceptance has become too low - "at least they're producing some code"
  - Some may not be at the level needed
  - No control over who joins team - Happiest Minds does internal training then assigns
  - Skill level varies significantly
- **Knowledge silos:** Some Happiest Minds staff are only ones who work on certain areas (e.g., UI in Mike's teams)

**Key Actions Needed:**
1. **More intentional performance management** - need to get better at holding contractors accountable
2. **Knowledge transfer planning** - begin extracting knowledge from silos, cross-train FTEs
3. **Transparency about offboarding timeline** - need to communicate intentions so HM can prepare professionally
4. **Deeper FTE engagement** - FTEs need to own quality from HM team members (historically offshore leads were held responsible)
5. **Stop operating in silos** - need FTEs working alongside contractors on same work, not separate streams

**Context:** Relationship being sunset as FTE headcount grows, but need 6-9 months for knowledge osmosis if we start now.

### Ramesh Rangavithal Donnipadu - Hiring & ICS Platform

**Hiring Updates:**
- **Engineering Manager for Continuity Assurance (ICS):** Starts tomorrow
- **Staff Engineer:** Decision almost made between two finalists, offer process this week

**ICS Platform - Startup Mode Expectation Reset:**
- **Context:** Migrating UiPath-based data extraction in IPA to LLM platform
- **Misalignment:** Operations and product expecting traditional enterprise approach:
  - Full architecture documented upfront
  - Complete testing strategy before start
  - Hard commitments on delivery timelines
- **Ramesh's approach:** Operating as **startup mode**
  - Better clarity for next 1-2 sprints
  - Rough ideas for 2+ months out
  - Iterate and learn as we build
- **Status:** Expectations reset, but taking time for teams to shift from compliance-heavy enterprise model

**DR for ICS:**
- Curtis clarified: Every component should have DR plan
- This is about DR **within ICS**, not a failover test **to** ICS

**Curtis AI Transformation Meetings:**
- Curtis visiting GHX India teams on AI transformation
- **Aggressive goal:** AI maturity **Level 3 by July 4th**
  - Level 3 definition: Developer pulls ticket from backlog, AI agent does the work
  - Note: Aaron mentioned L1-L8 scale exists elsewhere, but Curtis using L1-L3 framework from Eric's deck
- **Target:** Every team releasing to production **twice a day**
- Curtis will share details at next all-employee meeting

**Visibility Team:** Participating in DR activities with Curtis, Eric, and Seth

### Michael Mitchell - DR Timeline, Hiring, Product Alignment, Resiliency Center 2.0

**DR Test Timeline Clarification:**
- **December:** Contractual deadline (cannot be missed)
- **October:** Internal target (need buffer in case test doesn't go as planned)
- **Action:** Need to align communication - everyone hearing different dates
- All incident follow-up work + gaps must target October completion

**Hiring:**
- **Anand Mani:** Starts as Engineering Manager next Monday
- **Software Engineer II:** Follow-up interview today, likely resulting in offer

**Product Owner Assignments & Expectations:**
- **Need clarity on:**
  - Which POs are assigned to which teams
  - Alignment on role expectations and responsibilities
- **Current problem:** Some expectation that team members monitor and respond to "Help Channels"
  - Mike pushing back - this needs to stop
  - Product has been saying for a year+ that work must come through proper intake channels
  - Team members should not be responding to random requests outside backlog
- **Product engagement:** Unclear when new PO model will start
  - Several open product roles not yet filled
  - Need names (even if "new hire TBD") to start planning
  - Hope: As product gets staffed, they'll naturally meet traditional PO expectations

**Resiliency Center 2.0:**
- **Context:** GHX leadership (Steve Jackson, Chris Luoma, CJ, possibly Marlin Doner on product side) wants to execute new use cases for new revenue streams
- **Approach:** Fast, independent teams meeting with customers, showing progress, starting to sell
- **Current blocker:** Technical ownership misalignment
  - Platform/orchestration team believes they should build platform **before** any use cases start
  - This prevents fast progress and quick customer demos
- **Status:** Still churning - being pushed back up to leadership, no decision yet
- **Note:** Mike dropped from active involvement, just FYI for team awareness

## CJ Meeting Update (Competing Priorities Discussion)

**Background:**
Marten had lunch with CJ last week after sending him a detailed update from India trip. CJ wanted to discuss first impressions after ~5 months at GHX.

**Marten's Core Message:**
Most challenging environment for **competing priorities** and misaligned incoming requests - not just from stakeholders/product (normal), but from executive level:
- Mix of CJ, Curtis, Marlin, Steve, Rammi, Christine, Tian, security team
- Everyone name-dropping, declaring "code red", citing executive mandates
- Constant onslaught of urgent priorities

**Specific Examples Shared with CJ:**
1. **Q2 Roadmap:** Just completed substantial planning effort (product + engineering leaders), detailed down to epic/story level
2. **Committed vs. Non-Committed:** Immediately asked to re-categorize roadmap items after "completion"
3. **Strategic Priority:** Staff meeting message about breaking monolith → autonomous teams (everyone excited)
4. **Immediate Conflict #1 - DR Work:** Known/reserved capacity, but when test scheduled this week → "roadmap shifting 4 days" treated like crisis
5. **Immediate Conflict #2 - Red Mythos:** Week later, "number one priority, all hands on deck"
6. **Immediate Conflict #3 - Resiliency Center 2.0:** Same week, Mike asked to write lists of names to steal from teams for tiger team
7. **Ongoing Pressure - AI:** Curtis drumbeat on AI leveling up

**CJ's Response:**
- Took message seriously
- Forwarding emails to C-suite standing up for engineering teams
- Message: "We need to let our teams do the work they need to do"
- Committed to helping solve the prioritization problem

**CJ's Ask - Three Deliverables for Thursday Follow-Up Meeting:**

1. **Resiliency Progress Report** (data-backed)
   - What progress made on resiliency work?
   - What's improved in last 6-12 months?
   - Quantifiable improvements

2. **"End State" Definition**
   - When can we declare quasi-victory on resiliency work?
   - What state must be achieved to shift from:
     - Current: 60-70% capacity → technical maintenance/improvement
     - Target: 30% maintenance, 70% innovation/new features
   - What must be "done" before letting foot off gas on technical work?

3. **Capacity Evolution - Pie Chart Projections**
   - Q2 baseline → Q3 → Q4 projections
   - Loose expectations, not commitments
   - How does capacity allocation change quarter by quarter?

**Context Documents from CJ:**
- Recent doc showing "increase modularity, continue breaking the monolith" (too technical for Steve Jackson)
- Older Exchange roadmap doc (automation pod details) - too detailed for exec consumption
- **CJ's need:** Help explaining technical work in layman's terms for peers (Steve Jackson, Christine)
- CJ too far removed to dissect/translate himself

**Daniel's Jaded Perspective:**
- Supportive of Marten raising this with CJ
- Curtis has been hitting this drum for quite some time
- **Question:** Why is CJ asking these questions when he's been fed this information many times before?
- Possibilities:
  - Testing if everyone still aligned on end goal?
  - Doesn't pay attention?
  - Needs help articulating to Steve Jackson why decoupling increases robustness/uptime?

**Historical Context:**
- Old resiliency success criteria: databases to managed services, breaking out top 10 components
- Unclear if CJ needs help with specific service justifications or conceptual articulation

**Next Steps:**
- Marten preparing deliverables for Thursday meeting with CJ
- May schedule follow-up discussion with directors (Ramesh-friendly time if possible)
- Goal: Help CJ translate technical roadmap into executive-level business narrative

---

## Key Themes

**Culture Shifts Needed:**
- Automated deployments (feature flags, incremental releases)
- Product go-to-market (stop treating every change as major launch)
- Contractor performance management (raise the bar)
- Proper intake channels (kill help channel monitoring)
- Startup mode vs. enterprise mode (ICS platform)

**Vendor Management Evolution:**
- Distribute ownership across directors
- More intentional performance management
- Begin knowledge transfer planning now (6-9 months needed)
- Increase transparency about offboarding timeline

**Organizational Challenges:**
- Competing priorities from multiple executive sources
- Need clearer decision-making and prioritization framework
- CJ committed to helping solve, but needs data and business narrative

**Technical Progress:**
- Red Mythos moving forward (OSS environment, AMI pipeline, library decisions)
- Hiring momentum (multiple managers and engineers joining)
- AI maturity aggressive goals (Level 3 by July 4)

---

## Action Items

**Aaron:**
- [ ] Continue OSS environment setup for Red Mythos testing
- [ ] Meet with DevOps this week on Golden AMI pipeline automation

**Daniel:**
- [ ] Ask Ramya to reach out to Ramesh and Mike to establish direct relationships
- [ ] Coordinate with Ramesh/Mike on bringing EMs into resource discussions

**Marten:**
- [ ] Prepare 3 deliverables for Thursday CJ meeting:
  - Resiliency progress report (data-backed)
  - End state definition for technical work
  - Capacity pie chart evolution (Q2→Q3→Q4)
- [ ] Schedule follow-up discussion with directors on CJ messaging
- [ ] Forward Ramesh's ICS startup-mode email to team for context
- [ ] Set up monthly calls with Happiest Minds (Sujith)

**Mike:**
- [ ] Meet with help channel stakeholders to push back on direct requests to team
- [ ] Clarify PO assignments and expectations for teams

**Team-wide:**
- [ ] Communicate aligned DR timeline: October internal target, December contractual
- [ ] Begin more intentional Happiest Minds performance management and knowledge transfer

---

Chat with meeting transcript: *Teams recording, no Granola link*
