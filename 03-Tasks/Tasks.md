# Tasks

Your task backlog organized by priority.

## This Week

<!-- Tasks promoted to this week's focus -->

## P0 - Urgent (max 3)

<!-- Critical items that must be done today/tomorrow -->

- [ ] **Prepare presentation for CJ/Steve meeting on productivity improvements** — Three main topics: 1) Productivity improvements state of the union, 2) Exchange resiliency update (5 components), 3) Competing priorities roadmap. CJ has escalated competing priorities issue to Christie/Steve. [[CJ_Singh]] [[00-Inbox/Meetings/2026-05-07/2026-05-07 - Marten Curtis 1-1.md|Meeting Context]] ^task-20260507-001 #org_foundation
- [ ] **Define 3-5 specific "breaking the monolith" deliverables** — Use Gen3 scope boundary from Resiliency Plan. Clear completion criteria, avoid endless engineering. Validate with Daniel Monday 4 PM. Due for CJ Thursday 2026-05-08. [[00-Inbox/Meetings/2026-05-01/Technical_Priorities_Review.md|Meeting Notes]] ^task-20260501-011 #break_monolith #critical_execution
- [ ] **Create capacity allocation roadmap** — Show current (100% stability) → Q3 → Q4 pie charts to demonstrate shift toward product work. Due Thursday 2026-05-08. ^task-20260501-012 #org_foundation

## P1 - Important (max 5)

- [ ] **Document exchange resiliency status across 5 components** — Part of CJ/Steve presentation. Reference end-of-year presentation with 2026 roadmap. Include Atlas migration, LastCloud, SSO, DR improvements, and automation progress. [[CJ_Singh]] [[00-Inbox/Meetings/2026-05-07/2026-05-07 - Marten Curtis 1-1.md|Meeting Context]] ^task-20260507-002 #critical_execution
- [ ] **Draft competing priorities roadmap clarification** — CJ escalated competing priorities creating churn (email to Christie/Steve). Need clear roadmap to reduce priority whiplash from multiple executives. [[CJ_Singh]] ^task-20260507-003 #org_foundation
- [ ] **Review automation epic backlog for ROI analysis** — With RTO dropping to ~2hrs 15min, prioritize automation epics that provide biggest bang for buck. Focus on high-impact items (SSO scripts, Max automation), defer low-ROI work. [[00-Inbox/Meetings/2026-05-07/2026-05-07 - Exchange DR Gap Remediation Check in.md|DR Meeting Context]] ^task-20260507-005 #critical_execution
- [ ] **Test SSO deployment scripts individually before September** — SSO deployment scripts are critical path for RTO. Need confidence building through individual component testing before mid-September full DR test. SSO issues added 2+ hours during last exercise. ^task-20260507-007 #critical_execution
- [ ] **Coordinate with SSO team on confidence-building test schedule** — SSO team fixed scripts after 2-day struggle. Need regular testing cadence to build confidence and catch issues early. Critical for 2hr RTO target. ^task-20260507-009 #critical_execution
- [ ] **Plan mid-September DR test including Fusion, SCA, CCX** — Full DR test after Atlas/LastCloud completion (end of August). First test with all systems included. Validates 2hr 15min RTO projection before October prod validation. [[00-Inbox/Meetings/2026-05-07/2026-05-07 - Exchange DR Gap Remediation Check in.md|Meeting Notes]] ^task-20260507-010 #critical_execution
- [ ] **Continue OSS environment setup for Red Mythos testing** — Aaron setting up OSS environment for automated testing with Ben. Target: First VM fix in 1-2 weeks. [[Aaron_Srivastava]] ^task-20260506-001 #critical_execution
- [ ] **Meet with DevOps on Golden AMI pipeline automation** — Set up automated AMI refresh pipeline. Goal: Weekly production refreshes after soak testing. Verify redeploying same code with new AMI won't break things. [[Aaron_Srivastava]] ^task-20260506-002 #critical_execution 

## P2 - Normal (max 10)

<!-- Standard priority items -->

- [ ] **Investigate Phantom AI meeting notes tool with IT/security** — Kickdrum uses Phantom for automated meeting summaries (better than Teams Copilot). Currently blocked by GHX security. Explore if this could be added to approved tools portfolio. [[00-Inbox/Meetings/2026-05-07/2026-05-07 - Marten Curtis 1-1.md|Context]] ^task-20260507-004 #ai_native
- [ ] **Ensure GitHub migration plan includes documentation backup** — Moving runbook documentation from Confluence to GitHub for better version control. Must safeguard against losing documentation during migration. ^task-20260507-006 #critical_execution
- [ ] **Extract DR playbook steps from transcripts into sequential runbook** — Pull clean step-by-step playbook from DR exercise transcripts to replace back-and-forth banter. Should be: do step 1, do step 2, do step 3 format. [[00-Inbox/Meetings/2026-05-07/2026-05-07 - Exchange DR Gap Remediation Check in.md|Meeting Context]] ^task-20260507-008 #critical_execution
- [ ] **Migrate runbook documentation to GitHub with version control** — Move DR runbooks from Confluence to GitHub for better collaboration and change tracking. Enables proper version control for critical operational documentation. ^task-20260507-011 #critical_execution
- [ ] **Launch architecture forum for leads and senior engineers** — Weekly forum to discuss, debate, and align on architecture improvements. Build shared opinions, kindle ownership, drive breaking-the-monolith initiatives. Review with Daniel/Mike, set schedule, launch week of May 12. [[00-Inbox/Architecture_Forum_Proposal.md|Proposal]] ^task-20260501-015 #org_foundation #break_monolith
- [ ] **Rollout team housekeeping (5 items)** — Jira projects, Slack channels, email DLs, GitHub repos, Confluence pages. Staff meeting (5 min), Slack message, done by May 16. [[00-Inbox/Team_Housekeeping_Asks.md|The 5 Asks]] ^task-20260501-014 #org_foundation
- [ ] **Define metrics framework for ideal operating model** — Marten owns 10 metrics (stability, quality, security, tech debt), Laura owns 10 metrics (revenue, retention, NPS, usage). Parallel work to main deliverables. [[00-Inbox/Meetings/2026-05-01/Technical_Priorities_Review.md|Context]] ^task-20260501-013 #org_foundation
- [ ] **Ask Ramya to reach out to Ramesh and Mike for direct Happiest Minds relationships** — Distribute vendor management across directors. Each director involves their EMs. Relationship being sunset. [[Daniel_Milburn]] [[Ramesh_Donnipadu]] [[Mike_Mitchell]] ^task-20260506-003 #org_foundation
- [ ] **Schedule follow-up discussion with directors on CJ messaging** — After Thursday CJ meeting. Ramesh-friendly time. Help CJ translate technical roadmap into exec business narrative. [[Daniel_Milburn]] [[Ramesh_Donnipadu]] [[Mike_Mitchell]] ^task-20260506-004 #org_foundation
- [ ] **Set up monthly calls with Happiest Minds (Sujith)** — Engage at exec level. Sujith asking for monthly check-ins. Need 6-9 months for knowledge osmosis before relationship sunset. ^task-20260506-005 #org_foundation
- [ ] **Meet with help channel stakeholders to push back on direct team requests** — Product must route work through proper intake channels. Stop team monitoring help channels. [[Mike_Mitchell]] ^task-20260506-006 #org_foundation
- [ ] **Clarify PO assignments and expectations for teams** — Which POs assigned to which teams? Align on role expectations and responsibilities. [[Mike_Mitchell]] ^task-20260506-007 #org_foundation
- [ ] **Communicate aligned DR timeline to teams** — October internal target, December contractual. Align communication so everyone hears same dates. ^task-20260506-008 #critical_execution
- [ ] **Consider Auth0 migration priority vs MFA enforcement requirements** — SSO platform is 14 years old, Auth0 migration on roadmap. Discuss priority and timeline with Daniel and Mike. [[Daniel_Milburn]] [[Mike_Mitchell]] ^task-20260506-010 #org_foundation
- [ ] **Add shared docs from Kickdrum workshop to IRL; upload to data room** — Ensure Thinktiv/Kickdrum materials are accessible in central location. Related to platform architecture workshop. ^task-20260506-011 #org_foundation

## P3 - Backlog

- [ ] Need to formalize the name of my org - Should probably be Automation; it is already established, makes sense since the scope is broader than Exchange etc. Need to vet this with Ramesh, Daniel and Mike.

### From India Trip 2026-04 (Added 2026-05-01)

- [ ] **Pivot AI Native SDLC strategy** — Shift from incubate in 1-2 teams to broader rollout #ai_native
- [ ] **Facilitate team ownership of repos and deployments** — Teams take ownership of migrations, deployment pipelines (Github Actions) #org_foundation #break_monolith
- [ ] **Shift to team-owned quality decisions** — Teams decide their own test strategies and coverage #org_foundation
- [ ] **Discuss UI Test Automation shared function model** — How to manage automation going forward as teams become autonomous #org_foundation
- [ ] **Push teams to own their data and data stores** — Data layer is biggest problem area, needs more attention #break_monolith #critical_execution

### From Daily Notes April 2026 (Added 2026-05-01)

- [ ] **Send memo to leadership team** — Next steps on architecture, talks, and Q2 direction #org_foundation #break_monolith
- [x] **Schedule staff meeting** — Regular cadence with leadership team #org_foundation
- [ ] **Follow up with Aaron on next steps** — AI Native SDLC rollout and priorities #ai_native
- [ ] **Set up 1x1 with Aaron** — Regular sync on AI enablement strategy #ai_native
- [ ] **Set up 1x1 with Mike** — Check-in and alignment #org_foundation
- [ ] **Recap meeting with CJ** — Document outcomes and follow-ups from CJ discussion #org_foundation
- [ ] **Send Peter Attia jetlag episode to CJ** — Follow-up from conversation #org_foundation
- [ ] **Plan meeting with CJ, Steve, Curtis, Laura, Marlin** — Strategic alignment session on autonomous teams and product development #org_foundation #break_monolith

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


## From Migration - 2026-05-01

- [ ] Review quarterly planning outcomes and org change implications ^task-20260324-001 ^task-20260501-001 #source/2026-03-24-21.12---quarterly-planning-product-team.md
- [ ] Complete intake form and provide interview panel for principal role (this afternoon) ^task-20260326-001 ^task-20260501-002 #source/2026-03-26-14.02---exchange-recruiting-weekly-team-meeting.md
- [ ] Get Sandy's approval for Principal Architect title vs Principal Software Engineer ^task-20260326-002 ^task-20260501-003 #source/2026-03-26-14.02---exchange-recruiting-weekly-team-meeting.md
- [ ] Work with TA to set up abbreviated interview loop for Ravi Kumar Kotha ^task-20260403-003 ^task-20260501-004 #source/2026-04-03-12.01---interview-ravi-kumar-kotha.md
- [ ] Meet with Eric and Daniel on Monday to finalize dependency mapping approach for roadmap acceleration ^task-20260403-001 ^task-20260501-005 #source/2026-04-03-13.06---jarvis-steerco.md
- [ ] Review tech debt one-slide summary from Bharata/Curtis ahead of Thursday meeting ^task-20260403-002 ^task-20260501-006 #source/2026-04-03-13.06---jarvis-steerco.md
- [ ] Continue discussion in-person Wednesday in Hyderabad ^task-20260410-001 ^task-20260501-007 #source/2026-04-10-10.00-ipa-introduction-to-msot-and-pricesync-workflows.md
- [ ] Explore Nuvia team technical architecture meeting (Scott owns Nuvia and CDP systems) ^task-20260410-002 ^task-20260501-008 #source/2026-04-10-10.00-ipa-introduction-to-msot-and-pricesync-workflows.md
