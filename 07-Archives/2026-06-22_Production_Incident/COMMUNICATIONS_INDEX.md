# Communications Index - Marten Engblom

**Incident:** June 22-24, 2026 Production Incident  
**Purpose:** Comprehensive index of all significant communications sent by Marten during the incident

---

## Quick Reference

| Date/Time | Medium | Audience | Topic | Document Link |
|-----------|--------|----------|-------|---------------|
| **June 22, 19:58 MT** | Email | CJ, Curtis | Initial incident update | [Email Thread](#1-initial-incident-update-email) |
| **June 22, 22:12 MT** | Email | CJ, Curtis, Arshad | Risk factor analysis | [Email Thread](#2-risk-factor-analysis-response) |
| **June 22, 23:52 MT** | Slack | Incident Room | Formal handoff to Ramesh | [Handoff Message](#3-formal-handoff-slack) |
| **June 22, 23:55 MT** | Email | CJ, Curtis, Ramesh | Email handoff notification | [Email Thread](#4-handoff-notification-email) |
| **June 23, ~07:59 MT** | Email | GLT | Incident update - rollback initiated | [Email](#5-gltrequency-update---rollback-initiated) |
| **June 23, ~10:34 MT** | Email | GLT, CJ, Curtis | Follow-up - pivoting to fix forward | [Email](#6-follow-up---fix-forward-decision) |
| **June 23, ~21:06 MT** | Email | GLT, Steve Jackson | EOD update - issues resolved | [Email](#7-end-of-day-june-23-update) |
| **June 24, 09:35 MT** | Slack | Incident Room | Validation question - hotfix effectiveness | [Slack](#8-hotfix-validation-question-slack) |
| **June 24, 10:00 MT** | Slack DM | Arshad, Daniel, Ramesh | Defense of engineering team | [Slack](#9-engineering-defense-leadership-dm) |
| **June 24, 15:51 MT** | Email | GLT, SLT | AS2 rollback explanation | [Email](#10-as2-rollback-explanation-to-gltslt) |
| **June 24, Evening** | Email | GLT, SLT | Comprehensive incident update & RCA plan | [Email](#11-comprehensive-incident-update) |
| **June 25, Morning** | Email | Chrystie Leonard, Ramesh | Clarification of Engineering self-critique | [Email](#12-clarification-to-chrystie-leonard) |

---

## Detailed Communications

### 1. Initial Incident Update (Email)

**Time:** June 22, 2026 at 19:58 MT (7:58 PM)  
**Medium:** Email  
**To:** CJ Singh, Curtis Nielsen  
**Subject:** Update on Ongoing Incidents

**Purpose:** First formal escalation to engineering leadership about the incident

**Key Points:**
- 6 production issues following 02:00 MT release
- 2 resolved, 2 in progress, 2 fix ready but blocked on deployment
- Customer impact: 5,200+ GFax orders undelivered, 1,891 invoice documents failed
- Stryker and other major customers impacted
- Deployment pipeline knowledge gaps identified
- Fixes blocked on Happiest Minds contractor knowledge

**Tone:** Professional, transparent, surfaced systemic issues

**Full Text:** [2026-06-22_Executive_Email_Thread_Complete.md](2026-06-22_Executive_Email_Thread_Complete.md#initial-update-june-22-758-pm-mt)

**Context:**
- Sent after ~18 hours of active incident management
- Vetted with Daniel Milburn, Suresh Kumar, Kooper Frahm prior to sending
- Prompted CJ's questions about incident count and release differences

---

### 2. Risk Factor Analysis Response (Email)

**Time:** June 22, 2026 at 22:12 MT (10:12 PM)  
**Medium:** Email  
**To:** CJ Singh, Curtis Nielsen  
**Cc:** Arshad Mahammad  
**Subject:** Re: Update on Ongoing Incidents

**Purpose:** Answer CJ's questions about incident count and what made this release different

**Key Points:**
- 2 official incidents open (covering 6 issues)
- Incident tickets: 4-0011979642 (GFax, eInv), 4-0011979745 (EU MEX/IBR)
- Risk factor analysis:
  - More initiatives in flight than normal
  - Atlas migrations running parallel to regular development
  - Environment drift (STG on Atlas, PRD still MongoDB)
  - Resources fragmented across 10+ competing priorities
- Listed all concurrent initiatives: commercial work, tech debt, Atlas, Elasticsearch, Aurora, Red Mythos, DR, AI up-leveling, Playwright, hiring

**Tone:** Thoughtful, analytical, appropriately speculative ("thinking freely here")

**Full Text:** [2026-06-22_Executive_Email_Thread_Complete.md](2026-06-22_Executive_Email_Thread_Complete.md#martens-response---incident-count--risk-analysis-june-22-1012-pm-mt)

**Context:**
- Response to CJ's direct questions
- Provided organizational context for incident
- Led to CJ's request for deep dive on root causes

---

### 3. Formal Handoff (Slack)

**Time:** June 22, 2026 at 23:52 MT (11:52 PM)  
**Medium:** Slack  
**Channel:** #ghx_incident_rm_1  
**To:** Incident team (Gaurav Saini, Ian Maclaughlin, Ramesh Donnipadu)

**Purpose:** Formal transfer of decision-making authority to Ramesh after 21 hours 52 minutes

**Key Points:**
- Clear designation of Ramesh as decision authority
- Request for update coordination (not necessarily authoring all updates)
- Prioritization guidance: GFax/EML2PDF first, then MEX
- Professional disengagement vs. abandonment

**Tone:** Clear, authoritative, supportive

**Full Text:** [2026-06-22_23.52_Handoff_to_Ramesh_Slack.md](2026-06-22_23.52_Handoff_to_Ramesh_Slack.md)

**Reactions:** 👍 thanks, +1

**Context:**
- After 21 hours 52 minutes of active leadership
- Appropriate timezone transition point (India team coming online)
- Formal incident management protocol

---

### 4. Handoff Notification (Email)

**Time:** June 22, 2026 at 23:55 MT (11:55 PM)  
**Medium:** Email  
**To:** CJ Singh, Curtis Nielsen, Ramesh Donnipadu  
**Cc:** Arshad Mahammad  
**Subject:** Re: Update on Ongoing Incidents

**Purpose:** Notify leadership of handoff to Ramesh

**Key Message:**
> "Definitely CJ, there will be plenty to discuss it seems.
>
> **I am signing off for tonight, Ramesh is taking over oversight and decision making.** The team is working to get the hot fixes out to production before the start of tomorrow East Coast time."

**Tone:** Brief, clear, confident in handoff

**Full Text:** [2026-06-22_Executive_Email_Thread_Complete.md](2026-06-22_Executive_Email_Thread_Complete.md#handoff-to-ramesh-june-22-1155-pm-mt)

**Context:**
- Aligned with Slack handoff message (3 minutes later)
- Acknowledged CJ's deep dive request
- Set expectations for overnight work

---

### 5. GLT Update - Rollback Initiated (Email)

**Time:** June 23, 2026 at ~07:59 MT (estimated)  
**Medium:** Email  
**To:** #GLT (General Leadership Team)  
**Cc:** CJ Singh, Curtis Nielsen  
**Subject:** Exchange Incident Update

**Purpose:** Morning update on incident status and rollback decision

**Key Points:**
- Multiple issues starting at 02:30 AM MT
- Customer impact: ~6,500 GFax POs undelivered over 30 hours
- MEX/IBR suppliers unable to view orders (workaround suboptimal)
- Started rollback process to previous release
- Internal ETA: 90-120 minutes
- Keeping it concise intentionally

**Tone:** Direct, action-oriented, acknowledges complexity

**Full Text:** Captured in [2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md) (context section) and visible in email thread replies

**Context:**
- Sent morning after handoff to Ramesh
- Rollback decision made overnight/early morning
- Provided to broader leadership team (GLT)

---

### 6. Follow-up - Fix Forward Decision (Email)

**Time:** June 23, 2026 at ~10:34 MT (estimated from reply timestamps)  
**Medium:** Email  
**To:** #GLT  
**Cc:** CJ Singh, Curtis Nielsen  
**Subject:** Re: Exchange Incident Update

**Purpose:** Update on rollback failure and decision to fix forward

**Key Points:**
- Unable to rollback to previous release
- Hotfix deployed earlier validated as working for GFax (vast majority processed)
- Small amount still failing (<10 per hour) being manually handled
- Evaluating whether to rollback or move forward with fixing in place for IBR issue
- Will provide update by afternoon at latest

**Tone:** Transparent about setback, pragmatic about alternatives

**Full Text:** Captured in [2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md) (context section in Chrystie Leonard's email)

**Context:**
- Major decision pivot from rollback to fix forward
- Hotfix effectiveness validated despite rollback inability
- Strategic decision-making under constraint

---

### 7. End of Day (June 23) Update (Email)

**Time:** June 23, 2026 at ~21:06 MT (estimated)  
**Medium:** Email  
**To:** #GLT, Steve Jackson  
**Cc:** CJ Singh, Curtis Nielsen  
**Subject:** Re: Exchange Incident Update

**Purpose:** Final status for June 23 - majority of issues resolved

**Key Points:**
- Pivoted away from rollback in favor of fixing forward
- GFax orders successfully processed as of 10:30 today
- IBR/MEX "red banner" issue resolved with hotfix (US 11:42, EU 12:24)
- DB data correction script running (~8 hour ETA for CDP impact)
- Agreed blast radius data should come from RCA follow-up (response to Steve Jackson)

**Tone:** Summary, resolution-focused, forward-looking to analysis

**Full Text:** Captured in [2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md) (Chrystie Leonard email context)

**Context:**
- Sent after successful resolution of 4 of 6 original issues
- Response to Steve Jackson's "blast radius" request
- Positioned for RCA and retrospective work

---

### 8. Hotfix Validation Question (Slack)

**Time:** June 24, 2026 at 09:35 MT  
**Medium:** Slack  
**Channel:** #ghx_incident_rm_1  
**To:** Matthew Turner, Paul Bobbitt  
**Thread:** Responding to Arshad's "clean code" question

**Purpose:** Verify hotfix addressed target issue despite AS2 collateral damage

**Message:**
> "<@U98MV0K3R|Matthew Turner>, <@U95FZGQFJ|Paul Bobbitt> during the short time this hotfix was in production, did we validate that it worked (i.e. aside from the AS2 issues)?"

**Response (Matthew Turner):**
> "yes we confirmed `OnDemandAP Email To PDF` action was working before we rolled it back"

**Tone:** Investigative, separating target success from side effects

**Full Text:** [2026-06-24_Slack_Context_AS2_Rollback.md](2026-06-24_Slack_Context_AS2_Rollback.md#verification-of-hotfix-effectiveness)

**Context:**
- Asked in thread discussing Arshad's engineering rigor question
- Established that hotfix technically worked for intended purpose
- Important for understanding collateral damage vs. primary failure

---

### 9. Engineering Defense (Slack - Leadership DM)

**Time:** June 24, 2026 at 10:00 MT  
**Medium:** Slack Direct Message (Group)  
**Participants:** Arshad Mahammad, Daniel Milburn, Ramesh Donnipadu, Marten Engblom  
**Context:** Response to Arshad's "clean code" question in public channel

**Purpose:** Provide balanced perspective on root causes (engineering AND DevOps)

**Message 1:**
> "<@U091W4H6475|Arshad>, to be fair, we are also spending a lot of time on deployments and rollbacks due to the team deploying to the wrong environments (twice in the last couple of days), and thinking they rolled back in production when they in fact did not."

**Message 2:**
> "And a complete mess with the deployment pipelines, to the point where the engineering SMEs normally familiar with the environment could not figure out how to trigger a release without the DevOps contractors in India."

**Follow-up:**
> "I agree, it is a difficult situation all around, and many individuals have really gone above and beyond in an admirable way. I just want to make sure we **keep all root causes, as well as contributing and compounding issues in sight**."

**Tone:** Firm but diplomatic, systemic focus, acknowledges effort

**Full Text:** [2026-06-24_Slack_Context_AS2_Rollback.md](2026-06-24_Slack_Context_AS2_Rollback.md#martens-defense-of-engineering-team)

**Context:**
- Arshad publicly questioned engineering rigor ("lack of clean code")
- Marten provided counterbalance highlighting DevOps issues
- Acknowledged effort while maintaining focus on systemic issues
- Led to Ramesh's detailed observations about HM DevOps gaps

---

### 10. AS2 Rollback Explanation to GLT/SLT (Email)

**Time:** June 24, 2026 at 15:51 MT (3:51 PM)  
**Medium:** Email  
**To:** #GLT, #SLT  
**Subject:** Re: Exchange Incident Update  
**Context:** Response to Chrystie Leonard's morning inquiry about customer unrest

**Purpose:** Explain June 24 hotfix rollback and decision framework for next steps

**Key Points:**
1. Hotfix deployed this morning to address remaining email→PDF issue
2. Hotfix did address the issue as expected
3. **BUT** due to monolithic coupling/dependencies/deployment footprint, unrelated eInvoicing modification was released with it
4. eInvoicing modification impacted AS2 flows
5. Hotfix rolled back → back to June 23 stable state

**Timeline Provided:**
- EU Start: 4:36 AM MDT → Mitigated: 6:52 AM MDT
- US Start: 4:56 AM MDT → Mitigated: 7:14 AM MDT

**Decision Framework:**
> "Whether we remove the unrelated changes and re-release this last hot fix will depend on a few things, including the ongoing impact of the remaining defect, and also risk tolerance at this point. We will sync with the appropriate leaders (including CJ), and SMEs to make a decision."

**Tone:** Professional, transparent about architectural constraint, consultative on next steps

**Full Text:** [2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md#primary-communication-to-gltslt)

**Context:**
- Sent ~8 hours after incident resolution
- Response to Chrystie Leonard's report of "significant unrest among customers"
- Called out "monolithic coupling" explicitly as root cause
- Positioned next decision as requiring CJ consultation

---

### 11. Comprehensive Incident Update (Email)

**Time:** June 24, 2026 (evening)  
**Medium:** Email  
**To:** GLT, SLT  
**Cc:** CJ Singh, Ramesh Donnipadu, Arshad Mahammad  
**Subject:** Exchange Incident Update - Status & Path Forward

**Purpose:** Comprehensive update per CJ's directive - cover current status, RCA plan, path forward

**Key Points (per CJ's 10-point structure):**
1. **Current customer impact:** Minimal - AS2 resolved, GFax/MEX/IBR operational
2. **Internal impact:** Minimal - CDP/Analytics data correction complete
3. **Incident status:** 6 of 7 closed, 1 open (Email-to-PDF)
4. **Open incident plan:** Re-deploy Thursday with eInvoicing changes removed
5. **Last deployment before freeze:** Emphasize stability priority entering July 4th period
6. **Confirmation:** Stable state going into freeze Monday
7. **RCA timeline:** Starting Friday with full team
8. **RCA scope:** This incident + broader GFax reliability issues (last several weeks)
9. **Foreshadow findings:** Need to react quicker to PO-impacting issues, monolithic architecture prevents surgical fixes, DevOps complexities, rollback testing gaps, environment drift
10. **Close:** Expect update EOD Monday with RCA status

**Tone:** Confident, transparent, consultative, building trust for freeze period

**Full Text:** [2026-06-24_Email_to_GLT_SLT.md](2026-06-24_Email_to_GLT_SLT.md)

**Context:**
- Sent per CJ's specific directive and 10-point structure
- Included PS note to Ramesh about timezone (EST) and requesting feedback
- Follows afternoon meeting with CJ and Arshad about RCA and CI/CD pipeline standardization
- Addresses historical pattern of July 4th period issues - building confidence for freeze
- Strategic framing: shows we understand what happened (not flying blind)
- 5 specific observations foreshadowed for RCA focus

---

## Communication Patterns

### Audience Adaptation

**To VP/Director (Curtis/CJ):**
- Business impact focus
- Quantified metrics (order counts, customer names)
- Systemic issues surfaced
- Accountability acknowledged

**To General Leadership Team (GLT):**
- Status updates with timeline expectations
- Customer impact emphasis
- Action-oriented (what's being done)

**To Senior Leadership Team (SLT):**
- Strategic context (monolithic coupling)
- Decision frameworks
- Risk vs. defect trade-offs

**To Incident Team:**
- Operational clarity
- Authority designation
- Priority guidance

**To Peers (Arshad, Daniel, Ramesh):**
- Balanced perspective
- Systemic framing
- Acknowledgment of complexity

### Key Messaging Principles

1. **Transparency:** Called out systemic issues explicitly (deployment pipelines, monolithic coupling, DevOps gaps)
2. **Quantification:** Always provided specific customer impact (order counts, customer names)
3. **Accountability:** Acknowledged process gaps requiring RCA
4. **Action-Oriented:** Clear next steps with timeline expectations
5. **Systemic Focus:** Framed issues as organizational, not individual blame
6. **Consultative:** Committed to leadership consultation before major decisions
7. **Immediate Clarification:** When miscommunication detected, owned it immediately and clarified with vulnerability

### What Was Consistently Avoided

- Minimizing or sugarcoating issues
- Individual blame
- Over-promising on timelines
- Abandonment (clear handoffs vs. disappearing)
- Defensive posturing

---

## Supporting Documents

### Email Threads
- **[2026-06-22_Executive_Email_Thread_Complete.md](2026-06-22_Executive_Email_Thread_Complete.md)** - Complete email correspondence with CJ, Curtis, Arshad, Ramesh

### Formal Communications
- **[2026-06-22_19.38_Executive_Summary_to_Curtis_and_CJ.md](2026-06-22_19.38_Executive_Summary_to_Curtis_and_CJ.md)** - Initial executive summary (vetted with team)
- **[2026-06-22_23.52_Handoff_to_Ramesh_Slack.md](2026-06-22_23.52_Handoff_to_Ramesh_Slack.md)** - Formal handoff to Ramesh in Slack
- **[2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md)** - June 24 GLT/SLT update with analysis
- **[2026-06-24_Email_to_GLT_SLT.md](2026-06-24_Email_to_GLT_SLT.md)** - Comprehensive incident update and RCA plan
- **[2026-06-25_Response_to_Chrystie_Leonard.md](2026-06-25_Response_to_Chrystie_Leonard.md)** - Clarification of Engineering self-critique

### Slack Context
- **[2026-06-24_Slack_Context_AS2_Rollback.md](2026-06-24_Slack_Context_AS2_Rollback.md)** - Slack discussions including Marten's contributions

### Analysis
- **[2026-06-22_Incident_Leadership_Communications.md](2026-06-22_Incident_Leadership_Communications.md)** - Communication strategy analysis

---

## Communication Timeline Visual

```
June 22
  19:58 ─┐
  22:12 ─┤ Email to CJ/Curtis
  23:52 ─┤ Slack handoff
  23:55 ─┘ Email handoff

June 23
  07:59 ─┐
  10:34 ─┤ Email to GLT
  21:06 ─┘

June 24
  09:35 ── Slack validation question
  10:00 ── Slack leadership DM (defense)
  15:51 ── Email to GLT/SLT (AS2 rollback)
  Evening ── Email to GLT/SLT (comprehensive update & RCA plan)

June 25
  Morning ── Email to Chrystie/Ramesh (clarification of Engineering self-critique)
```

---

**Purpose:** Comprehensive reference for communication patterns, stakeholder management, and crisis communication examples  
**Created:** 2026-06-24  
**Related:** [Timeline](TIMELINE.md) | [Comprehensive Record](2026-06-22_Production_Incident_Comprehensive_Record.md)
