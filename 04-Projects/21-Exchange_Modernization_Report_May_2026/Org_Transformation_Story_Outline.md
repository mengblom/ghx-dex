# Exchange Organization Transformation Story

**Purpose:** Show the organizational evolution that enables sustained resiliency improvements

**Timeline:** 2024-2026

**Audience:** Non-tech stakeholders (board, exec leadership, product partners)

---

## The Transformation Arc

### Before (2024): Centralized Bottleneck Model

**Structure:**
- 1 Director
- 3 Hands-on Managers
- ~50+ engineers in flat structure
- Shared deployment pipeline
- Monolithic release cycle (2-3 weeks)
- Cross-team coordination required for most work

**Resiliency Challenges:**
- Large blast radius (one deployment = all of Exchange)
- Slow incident recovery (required cross-team coordination)
- Unclear ownership (who owns what?)
- Deployment coupling (teams blocked on each other)
- Communication overhead (3 managers can't scale to 50+ people)

**Incident Patterns Caused:**
- "Lack of Domain Separation" (4 incidents in Jan 2025)
- "Synchronous Data Dependency" (3 incidents in Oct 2024)
- "Synchronous/Dependent Communications" (2 incidents in Jan 2025)
- "Communications Failure - Miscomms Across Teams" (2 incidents in Nov 2024)

---

### Transition (2025): Building the Foundation

**What We Did:**

#### Phase 1: Leadership Structure (Q1-Q2 2025)
- Hired/promoted to **12 IC-first Engineering Managers**
  - [NEED TO LIST: Names and when they joined]
  - 2 still pending hire (as of June 2026)
- Created clear team boundaries and ownership domains
- Established manager-team ratios that enable mentorship

#### Phase 2: Team Autonomy Infrastructure (Q2-Q3 2025)
- Defined "Autonomous Team Template":
  - Dedicated Engineering Manager
  - Dedicated Product Owner assignment
  - Native Jira project (not just boards)
  - Dedicated Slack channels
  - Owned GitHub repos
  - Independent deployment pipeline
  - Clear domain ownership documentation

#### Phase 3: Process & Standards (Q3 2025 - Q2 2026)
- **GitHub Migration:** 100% of Exchange repos migrated [VERIFY %]
- **GHX Exchange Team Standards:**
  - Standard Jira workflows
  - Custom fields for ownership metadata
  - Deployment pipeline standards
  - Testing and quality gates
- **Release Rigor Framework** (implemented Oct 2024)
- **Architecture Forum** (launching June 2026)

---

### After (2026): Autonomous Teams Operating Model

**Structure:**
- 1 Senior Director (Marten)
- **12 Engineering Managers** (IC-first, team-focused)
  - [LIST MANAGERS HERE]
- 12 Autonomous Teams (1 per manager)
- Each team owns:
  - Full stack (services, DBs, infrastructure)
  - Deployment pipeline
  - On-call rotation
  - Quality gates
  - Domain expertise

**Resiliency Benefits:**

#### 1. Smaller Blast Radius
- Team deploys independently
- Failure in Team A doesn't impact Team B
- ~92% reduction in deployment blast radius (1 team vs 12 teams)

#### 2. Faster Recovery
- Team owns full stack (no cross-team coordination during incidents)
- Clear escalation path (Manager → Director)
- Average recovery time: [NEED DATA]

#### 3. Team Accountability
- Per-team uptime metrics
- Team owns their domain's stability
- OKRs tied to resiliency outcomes

#### 4. Continuous Improvement at Scale
- 12 teams working in parallel (not sequentially)
- Each team can address resiliency issues in their domain
- No monolithic "Exchange resiliency sprint" needed

#### 5. Eliminated Root Causes
- **"Lack of Domain Separation"** → Architectural domains now clear
- **"Communications Failure"** → Reduced from 2 incidents to [CURRENT?]
- **"Synchronous Dependencies"** → Teams decouple over time

---

## The Numbers

### Organizational Scale
- **Before:** 1 director + 3 managers for 50+ people
- **After:** 1 director + 12 managers for 50+ people
- **Manager:IC ratio:** Improved from ~17:1 to ~4-5:1
- **Leadership capacity:** 4x increase in hands-on leadership

### Team Structure
- **Number of autonomous teams:** 12
- **Teams with independent pipelines:** [NEED COUNT as of June 2026]
- **Teams deploying weekly:** [NEED COUNT]
- **Average team size:** ~4-6 engineers per team

### Deployment Metrics
- **Before:** Monolithic 2-3 week release cycle
- **After:** Teams deploy weekly/on-demand [VERIFY]
- **Deployment blast radius:** Reduced by ~92% (1/12 instead of 12/12)

### Incident Metrics
- **Release-related incidents:** Zero since Oct 2024 (19+ months)
- **Database incidents:** Zero Nov 2024 - Mar 2025 (4 months)
- **"Lack of Domain Separation" incidents:** [BEFORE vs AFTER?]

---

## Why This Matters (Non-Tech Translation)

### For Board / Exec Leadership
**Old way:** Like having one kitchen for a 12-restaurant hotel
- One chef (director), three sous chefs (managers)
- Everyone uses same equipment, same schedule
- If one restaurant has a problem, all kitchens shut down
- Takes weeks to make any menu changes

**New way:** Each restaurant has its own kitchen
- Each restaurant has a head chef (manager)
- Independent schedules, equipment, menus
- Problem in Restaurant 3 doesn't affect Restaurant 7
- Menu changes happen continuously, not in big batches

### For Product Partners
**Old way:** "We need to coordinate with 11 other teams to deploy this"
- Long lead times
- High coordination overhead
- Unclear who to talk to
- Deployment windows weeks apart

**New way:** "Your team can deploy this independently"
- Short lead times
- Clear team ownership
- One manager, one team to coordinate with
- Deploy when ready (not waiting on others)

---

## The Human Side

### What Changed for Engineers
- **Clear ownership:** "This is my team's domain"
- **Manageable scope:** Working on 1/12 of Exchange, not all of it
- **Faster feedback:** Deploy weekly, not every 2-3 weeks
- **Career growth:** IC-first managers invested in mentorship

### What Changed for Managers
- **Span of control:** 4-5 people (vs 17:1 before)
- **Ownership:** Full accountability for team domain
- **Autonomy:** Make decisions locally, not through director bottleneck
- **Career path:** IC-first model (technical + people leadership)

---

## Critical Success Factors

### What Made This Work

1. **Phased approach** (structure → infrastructure → process)
2. **Standards first** (GHX Exchange Team Standards document)
3. **Process rigor** (Release Framework, Architecture Forum)
4. **Measurement** (per-team metrics, incident tracking)
5. **Executive support** (CJ's commitment to org transformation)

### What's Still In Progress

1. **Hiring:** 2 managers still pending
2. **GitHub migration:** [% complete?]
3. **Decoupling work:** 6 workstreams at 50%+ (as of Feb 2025)
4. **Team standards rollout:** 12 Jira projects being created (June 2026)
5. **Architecture Forum:** First session next week

---

## Forward Looking: What Autonomous Teams Enable

### Short Term (Next 6 months)
- All 12 teams have independent deployment pipelines
- Weekly deployments become standard
- Per-team uptime SLOs established
- Decoupling workstreams completed

### Medium Term (Next 12 months)
- Teams own their resiliency roadmap
- Incidents handled locally (no cross-team coordination)
- Commercial vs tech work balanced at team level (50-50)
- New team members onboard faster (smaller scope)

### Long Term (2+ years)
- Continuous architectural improvement (not big-bang migrations)
- Teams evolve independently
- Organization scales (can add teams without coordination overhead)
- "Lack of Domain Separation" completely eliminated as incident cause

---

## Appendix: Team Roster (As of June 2026)

**Need to populate:**

### Senior Director
- Marten Engblom

### Engineering Managers (12 total, 2 pending hire)
1. [Manager Name] - [Team/Domain]
2. [Manager Name] - [Team/Domain]
3. Daniel Milburn - [Team/Domain]
4. Mike Mitchell - [Team/Domain]
5. Aaron Srivastava - [Team/Domain]
6. [Continue list...]
7. [TBD - Pending hire]
8. [TBD - Pending hire]

---

## Sources Needed

To complete this story:
1. **Manager roster** with names, domains, join dates
2. **Current deployment metrics** (teams deploying independently, frequency)
3. **Incident reduction data** tied to org changes
4. **GitHub migration %** complete
5. **Team size** breakdown (how many engineers per team)
6. **Before/after examples** of coordination overhead reduced

---

## Presentation Format Recommendations

### Slide Structure (Draft)
1. **The Challenge** (incident patterns showing org/architectural issues)
2. **The Transformation** (1 director/3 mgrs → 1 director/12 mgrs)
3. **The Infrastructure** (autonomous team template, standards, pipelines)
4. **The Results** (blast radius reduction, incident elimination, deployment speed)
5. **The Future** (what autonomous teams enable next)

### Visual Elements
- Org chart (before/after)
- Incident timeline (showing reduction over time)
- Deployment flow diagram (monolithic → independent)
- Team domain map (12 teams, their ownership)

---

## Next Steps

1. **Gather missing data** (manager roster, metrics, completion %)
2. **Draft presentation deck** (target: next 2 weeks)
3. **Dry run with Curtis** (validate story and data)
4. **Dry run with CJ** (get feedback, refine message)
5. **Final presentation** (board? exec team? stakeholders?)
