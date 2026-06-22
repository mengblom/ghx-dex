# Tasks

## Next Week
- [ ] **Start architecture forum discussion on decoupling roadmap** ^task-20260601-031
	- During team meetup Mon-Wed next week. Discuss what gets decoupled when, gather technical details to inform epics/stories for JIRA boards. Will help answer "what's actually happening on the ground" question.
	- Pillar: Breaking the Monolith → Autonomous Teams | Priority: P3


Your task backlog organized by priority.

## This Week
- [ ] **Conduct data-backed risk analysis for Oct 1 vs Jan 1 capacity shift to 50-50** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-038
	- What's incomplete if we shift capacity Oct 1? What stability risks/incidents are we exposed to? Steve needs confidence to commit to Oct 1 timeline for product planning. Deliver data-backed recommendation on timeline.
	- Pillar: Organizational Foundation (People & Process) | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [ ] **Draft data-backed email response to CJ with resiliency case and timeline recommendation** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-037
	- Synthesis email with: (1) incident data linking Autonomous Teams to resiliency, (2) metrics-driven "From → To" for P0 database work, (3) Oct 1 vs Jan 1 risk analysis and recommendation. Goal: Give CJ/Steve confidence to commit to Oct 1 timeline.
	- Pillar: Organizational Foundation (People & Process) | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [ ] **Access and update SharePoint 1-pager "Exchange resiliency" box with current metrics** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-036
	- Update the "exchange resiliency" box in CJ's May 19 India All Hands presentation with current status and metrics. Link: ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/_layouts/15/Doc.aspx?sourcedoc=%7B480F0475-98C3-4ABA-86D3-52CD6B7E7BBA%7D&file=20260519%20-%20GHX%20India%20Tech%20Org%20All%20Hands.pptx
	- Pillar: Organizational Foundation (People & Process) | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [ ] **Build metrics-driven "From → To" analysis for P0 database work with incident data** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-035
	- CJ wants "clear From and To" with metrics for each P0 item (Audit DB, BT/BD, data layer). Include current state numbers, target state numbers, and expected resiliency improvements (incident reduction, performance gains).
	- Pillar: Critical Technical Execution | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [ ] **Gather current DB metrics for 3 P0 items (Audit DB, BT/BD, data layer reliability)** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-034
	- For each item need: current response times, error rates, capacity %, storage costs, query patterns, incidents caused. This becomes the "From" state in the metrics-driven analysis.
	- Pillar: Critical Technical Execution | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [ ] **Find Dermot's DB stabilization work from ~1 year ago (metrics-driven approach reference)** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-033
	- CJ referenced Dermot's work as example of "how data driven we were about a yr ago" - need to review this to understand the expected format and rigor for "From → To" metrics presentation.
	- Pillar: Critical Technical Execution | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [ ] **Find and review resiliency surge plan decks with incident root cause categories** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260602-032
	- CJ asked: "Have you seen those decks?" - need to find decks showing how incidents mapped to root cause categories (deployment issues, database problems, etc.). This data backs up the Autonomous Teams → resiliency improvement claim.
	- Pillar: Critical Technical Execution | Priority: P0 | Weekly priority: [week-2026-W23-p1]

- [x] **Draft email to CJ with initiative/epic framework for resiliency work** | 05-Areas/People/Internal/CJ_Singh.md ^task-20260601-030 ✅ 2026-06-02 11:15
	- Echo back understanding of what CJ needs: definition of done, how it impacts resiliency, and trackable progress framework. Present two-pillar structure (Data Layer + Team Decoupling) with epics underneath. Acknowledge board reporting pressure. Keep response concise.
	- Pillar: Organizational Foundation (People & Process) | Priority: P0

- [ ] **Document P0 database work details (audit DB, BTBD, event bus)** ^task-20260601-029
	- Expand specifics on three P0 items: (1) Audit DB re-architecture (defensible use case? S3 vs Mongo?), (2) BTBD scalability deep-dive (past incidents, improvements), (3) Event bus replacement (Mongo → proper messaging). Include S3 optimization as P1 ($1M/year savings, 50 copies per doc, 11-year retention).
	- Pillar: Critical Technical Execution | Priority: P1

- [ ] **Gather specific decoupling examples from teams (databases, tables, components)** ^task-20260601-028
	- Pull together concrete list of what's being separated/decoupled to support CJ email. Include database moves, table splits, etc. Position as supporting evidence, not the main story. Avoid "small potato" items that could be second-guessed.
	- Pillar: Breaking the Monolith → Autonomous Teams | Priority: P1


<!-- Tasks promoted to this week's focus -->

## P0 - Urgent (max 3)

<!-- Critical items that must be done today/tomorrow -->

## P1 - Important (max 5) 

## P2 - Normal (max 10)

<!-- Standard priority items -->

- [ ] **Check Jira rollout completion status with Mike Mitchell** ^task-20260622-001
	- Was this completed during your June 11-14 FTO? Need to verify 12 project spaces created, templates approved, and teams onboarded. If incomplete, identify blockers.
	- Pillar: Organizational Foundation (People & Process) | Priority: P2
	- Source: Daily note May 26 (orphaned task)

- [ ] **Set up Confluence space for team domain ownership documentation** ^task-20260622-002
	- Create central place to document each team's domain/area of responsibility, decoupling plans, and architectural decisions. Supports Architecture Forum launch.
	- Pillar: Breaking the Monolith → Autonomous Teams | Priority: P2
	- Source: Daily notes June 5/8 (orphaned task)
	- Related: Architecture Forum Priority #2 this week

- [ ] **Follow up with Chantelle/Tasha on GHXi salary information** ^task-20260622-003
	- Sandy Chronister mentioned salaries might be missing from GHXi system for India hires. Verify if this is blocking hiring or compensation discussions.
	- Pillar: Organizational Foundation (People & Process) | Priority: P2
	- Source: Daily note June 9 (orphaned task from Sandy 1x1)

- [ ] **Verify project/initiative tracking above sprint level** ^task-20260622-004
	- Check if Jira spaces rollout solved visibility gap for strategic initiatives that span multiple sprints/teams. If not, define tracking mechanism.
	- Pillar: Organizational Foundation (People & Process) | Priority: P2
	- Source: Daily note May 27 (orphaned task)

## P3 - Backlog

- [ ] **Set up Marten Staff Confluence page** ^task-20260622-005
	- Create team documentation hub on Confluence for staff-level information, meeting notes, and team resources.
	- Pillar: Organizational Foundation (People & Process) | Priority: P3
	- Source: Daily notes June 5/8 (orphaned task)

- [ ] **Process transcripts from prior meetings (May/early June)** ^task-20260622-006
	- Review and extract action items from unprocessed meeting transcripts. Low ROI after 2+ weeks but may surface missed commitments.
	- Pillar: Organizational Foundation (People & Process) | Priority: P3
	- Source: Daily notes June 5/8 (orphaned task)

### Archived from May 2026 (marked complete 2026-06-01)

- [x] **Prepare presentation for CJ/Steve meeting on productivity improvements** ^task-20260507-001 
- [x] **Define 3-5 specific "breaking the monolith" deliverables** ^task-20260501-011
- [x] **Create capacity allocation roadmap** ^task-20260501-012
- [x] **Document exchange resiliency status across 5 components** ^task-20260507-002
- [x] **Draft competing priorities roadmap clarification** ^task-20260507-003
- [x] **Review automation epic backlog for ROI analysis** ^task-20260507-005
- [x] **Test SSO deployment scripts individually before September** ^task-20260507-007
- [x] **Coordinate with SSO team on confidence-building test schedule** ^task-20260507-009
- [x] **Plan mid-September DR test including Fusion, SCA, CCX** ^task-20260507-010
- [x] **Continue OSS environment setup for Red Mythos testing** ^task-20260506-001
- [x] **Meet with DevOps on Golden AMI pipeline automation** ^task-20260506-002
- [x] **Investigate Phantom AI meeting notes tool with IT/security** ^task-20260507-004
- [x] **Ensure GitHub migration plan includes documentation backup** ^task-20260507-006
- [x] **Extract DR playbook steps from transcripts into sequential runbook** ^task-20260507-008
- [x] **Migrate runbook documentation to GitHub with version control** ^task-20260507-011
- [x] **Launch architecture forum for leads and senior engineers** ^task-20260501-015
- [x] **Rollout team housekeeping (5 items)** ^task-20260501-014
- [x] **Define metrics framework for ideal operating model** ^task-20260501-013
- [x] **Ask Ramya to reach out to Ramesh and Mike for direct Happiest Minds relationships** ^task-20260506-003
- [x] **Schedule follow-up discussion with directors on CJ messaging** ^task-20260506-004
- [x] **Set up monthly calls with Happiest Minds (Sujith)** ^task-20260506-005
- [x] **Meet with help channel stakeholders to push back on direct team requests** ^task-20260506-006
- [x] **Clarify PO assignments and expectations for teams** ^task-20260506-007
- [x] **Communicate aligned DR timeline to teams** ^task-20260506-008
- [x] **Consider Auth0 migration priority vs MFA enforcement requirements** ^task-20260506-010
- [x] **Add shared docs from Kickdrum workshop to IRL; upload to data room** ^task-20260506-011

### Older Backlog

- [ ] Need to formalize the name of my org - Should probably be Automation; it is already established, makes sense since the scope is broader than Exchange etc. Need to vet this with Ramesh, Daniel and Mike.

### From India Trip 2026-04 (Archived)

- [x] **Pivot AI Native SDLC strategy** — Shift from incubate in 1-2 teams to broader rollout #ai_native
- [x] **Facilitate team ownership of repos and deployments** — Teams take ownership of migrations, deployment pipelines (Github Actions) #org_foundation #break_monolith
- [x] **Shift to team-owned quality decisions** — Teams decide their own test strategies and coverage #org_foundation
- [x] **Discuss UI Test Automation shared function model** — How to manage automation going forward as teams become autonomous #org_foundation
- [x] **Push teams to own their data and data stores** — Data layer is biggest problem area, needs more attention #break_monolith #critical_execution

### From Daily Notes April 2026 (Archived)

- [x] **Send memo to leadership team** — Next steps on architecture, talks, and Q2 direction #org_foundation #break_monolith
- [x] **Schedule staff meeting** — Regular cadence with leadership team #org_foundation
- [x] **Follow up with Aaron on next steps** — AI Native SDLC rollout and priorities #ai_native
- [x] **Set up 1x1 with Aaron** — Regular sync on AI enablement strategy #ai_native
- [x] **Set up 1x1 with Mike** — Check-in and alignment #org_foundation
- [x] **Recap meeting with CJ** — Document outcomes and follow-ups from CJ discussion #org_foundation
- [x] **Send Peter Attia jetlag episode to CJ** — Follow-up from conversation #org_foundation
- [x] **Plan meeting with CJ, Steve, Curtis, Laura, Marlin** — Strategic alignment session on autonomous teams and product development #org_foundation #break_monolith

---

## Task Format

```
- [ ] **Task title** — Context or notes #pillar
- [s] Started task
- [b] Blocked task (note blocker)
- [x] Completed task
```

## Pillars

Tasks should align to your strategic pillars (configured during `/setup`).


## From Migration - 2026-05-01 (Archived)

- [x] Review quarterly planning outcomes and org change implications ^task-20260324-001 ^task-20260501-001 #source/2026-03-24-21.12---quarterly-planning-product-team.md
- [x] Complete intake form and provide interview panel for principal role (this afternoon) ^task-20260326-001 ^task-20260501-002 #source/2026-03-26-14.02---exchange-recruiting-weekly-team-meeting.md
- [x] Get Sandy's approval for Principal Architect title vs Principal Software Engineer ^task-20260326-002 ^task-20260501-003 #source/2026-03-26-14.02---exchange-recruiting-weekly-team-meeting.md
- [x] Work with TA to set up abbreviated interview loop for Ravi Kumar Kotha ^task-20260403-003 ^task-20260501-004 #source/2026-04-03-12.01---interview-ravi-kumar-kotha.md
- [x] Meet with Eric and Daniel on Monday to finalize dependency mapping approach for roadmap acceleration ^task-20260403-001 ^task-20260501-005 #source/2026-04-03-13.06---jarvis-steerco.md
- [x] Review tech debt one-slide summary from Bharata/Curtis ahead of Thursday meeting ^task-20260403-002 ^task-20260501-006 #source/2026-04-03-13.06---jarvis-steerco.md
- [x] Continue discussion in-person Wednesday in Hyderabad ^task-20260410-001 ^task-20260501-007 #source/2026-04-10-10.00-ipa-introduction-to-msot-and-pricesync-workflows.md
- [x] Explore Nuvia team technical architecture meeting (Scott owns Nuvia and CDP systems) ^task-20260410-002 ^task-20260501-008 #source/2026-04-10-10.00-ipa-introduction-to-msot-and-pricesync-workflows.md
