# Production Incident - June 22-24, 2026
## CoreX-ALL 2.273.x Release

**Quick Status:** Six simultaneous production issues + secondary AS2 hotfix rollback incident  
**Duration:** June 22 02:00 MT → June 24 EOD (~67 hours)  
**Marten's Leadership:** 21 hours 52 minutes (June 22 02:00 → 23:52 MT)  
**Customer Impact:** 5,200+ GFax orders, 1,891 invoices, ~5,186 AS2 transactions

---

## Start Here

### 📍 New to This Incident?

**1. [TIMELINE.md](TIMELINE.md)** - Complete chronological timeline with all events  
**2. [COMMUNICATIONS_INDEX.md](COMMUNICATIONS_INDEX.md)** - All of Marten's communications indexed and linked  
**3. [2026-06-22_Production_Incident_Comprehensive_Record.md](2026-06-22_Production_Incident_Comprehensive_Record.md)** - Full incident analysis, root causes, organizational factors

### 🎯 Looking for Something Specific?

| I need... | Go here |
|-----------|---------|
| **When did X happen?** | [TIMELINE.md](TIMELINE.md) |
| **What did Marten communicate?** | [COMMUNICATIONS_INDEX.md](COMMUNICATIONS_INDEX.md) |
| **Root causes & analysis** | [Comprehensive Record](2026-06-22_Production_Incident_Comprehensive_Record.md#root-causes--contributing-factors) |
| **Technical details (BouncyCastle, AS2)** | [June 24 Slack Context](2026-06-24_Slack_Context_AS2_Rollback.md) |
| **Email threads with CJ/Curtis** | [Executive Email Thread](2026-06-22_Executive_Email_Thread_Complete.md) |
| **Deployment pipeline issues** | [Deployment Pipeline Crisis](2026-06-23_Deployment_Pipeline_Crisis.md) |
| **Leadership handoff** | [Handoff Message](2026-06-22_23.52_Handoff_to_Ramesh_Slack.md) |

---

## Executive Summary

Following the June 22 early morning release (02:00 MT), Exchange experienced **six simultaneous production issues** — unprecedented for the platform. By end of June 23, four issues were resolved with two remaining. A secondary incident occurred June 24 when a hotfix rollback was required due to AS2 connection failures from a BouncyCastle library conflict.

### Customer Impact
- **5,200+ GFax purchase orders** undelivered (June 22-23)
- **1,891 invoice documents** failed PDF conversion
- **~5,186 US transactions + 336+ EU flows** affected by AS2 issue (June 24)
- **Major customers:** Stryker, Hartford Healthcare, Owens & Minor, Intertrade, Philips Healthcare, Cook Medical

### Issues Resolved
✅ EU Database Connection Failures  
✅ GFax SFTP/SSH Algorithm Negotiation  
✅ GFax PDF Conversion Failures  
✅ EML2PDF Word Conversion Failures  
✅ MEX Orders Purchase Details Loading  
✅ DB Data Correction (BigDecimal vs long)  
✅ AS2 Connection Failures (rollback)

### Issues Remaining
🟡 Tracking Document Loops (lower priority)  
🟡 Email-to-PDF Conversion (hotfix rolled back due to AS2 side effects)

---

## Key Root Causes

### Technical
1. **Environment Drift** - STG on Atlas/Aurora/ES, PRD still MongoDB
2. **Sloppy Migration Work** - EU connection strings incomplete
3. **Library Conflicts** - BouncyCastle version conflict (1.68 vs 1.78)
4. **Monolithic Coupling** - Cannot deploy isolated fixes without bundling unrelated changes
5. **Team Without Manager** - Actions team (GFax, EML2PDF) orphaned

### Organizational
1. **Team Stretched Across 10+ Initiatives** - Commercial work, tech debt, Atlas, Elasticsearch, Aurora, Red Mythos, DR, AI, Playwright, hiring
2. **Resource Fragmentation** - Key people focused on migrations vs. release hardening
3. **First Time Unable to Release with FTE Resources Alone** - HM DevOps knowledge gaps exposed

### Process
1. **Deployment Pipeline Complexity** - 10 hours to deploy tested hotfix
2. **Wrong Environment Deployments** - Twice in 2 days
3. **Failed Rollback** - First attempt didn't actually rollback
4. **18-Month Knowledge Transfer Failure** - Gagan → HM DevOps
5. **Pipeline Proliferation** - Too many cloned pipelines, poor documentation

---

## Documents by Category

### 📅 Timeline & Status
- **[TIMELINE.md](TIMELINE.md)** - Complete chronological timeline
- **[2026-06-22_Release_Progression_Timeline.md](2026-06-22_Release_Progression_Timeline.md)** - Detailed progression from 2.273.4 → 2.273.7
- **[2026-06-24_Incident_Update_Summary.md](2026-06-24_Incident_Update_Summary.md)** - June 24 daily summary

### 💬 Communications (Marten)
- **[COMMUNICATIONS_INDEX.md](COMMUNICATIONS_INDEX.md)** - Master index of all communications
- **[2026-06-22_Executive_Email_Thread_Complete.md](2026-06-22_Executive_Email_Thread_Complete.md)** - Email thread with CJ, Curtis, Arshad, Ramesh
- **[2026-06-22_19.38_Executive_Summary_to_Curtis_and_CJ.md](2026-06-22_19.38_Executive_Summary_to_Curtis_and_CJ.md)** - Initial executive summary (19:38 MT)
- **[2026-06-22_23.52_Handoff_to_Ramesh_Slack.md](2026-06-22_23.52_Handoff_to_Ramesh_Slack.md)** - Formal handoff to Ramesh (23:52 MT)
- **[2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md)** - AS2 rollback explanation to GLT/SLT (15:51 MT)
- **[2026-06-24_Email_to_GLT_SLT.md](2026-06-24_Email_to_GLT_SLT.md)** - Comprehensive incident update and RCA plan (evening)
- **[2026-06-25_Response_to_Chrystie_Leonard.md](2026-06-25_Response_to_Chrystie_Leonard.md)** - Clarification of Engineering self-critique (morning)
- **[2026-06-22_Incident_Leadership_Communications.md](2026-06-22_Incident_Leadership_Communications.md)** - Communication strategy analysis

### 🔧 Technical Deep Dives
- **[2026-06-22_Production_Incident_Comprehensive_Record.md](2026-06-22_Production_Incident_Comprehensive_Record.md)** - Complete analysis with root causes
- **[2026-06-24_Slack_Context_AS2_Rollback.md](2026-06-24_Slack_Context_AS2_Rollback.md)** - BouncyCastle technical details, organizational tensions
- **[2026-06-23_Deployment_Pipeline_Crisis.md](2026-06-23_Deployment_Pipeline_Crisis.md)** - DevOps pipeline issues in detail

### 🤝 Meetings & Context
- **[2026-06-23_Incident_Reflection_with_Curtis.md](2026-06-23_Incident_Reflection_with_Curtis.md)** - 1:1 debrief with Curtis
- **[2026-06-23_DR_BCP_Meeting_Summaries.md](2026-06-23_DR_BCP_Meeting_Summaries.md)** - DR/BCP meetings during active incident
- **[2026-06-24_CJ_Arshad_RCA_Planning_Meeting.md](2026-06-24_CJ_Arshad_RCA_Planning_Meeting.md)** - RCA directive, CI/CD pipeline standardization, leadership communication strategy

---

## Critical Moments

### Decision Points

**June 22, 22:12 MT** - Marten provides risk factor analysis to CJ  
→ Led to CJ's request for deep dive on root causes

**June 22, 23:52 MT** - Formal handoff to Ramesh after 21+ hours  
→ Appropriate timezone transition, formal incident protocol

**June 23, 10:34 MT** - Decision to fix forward instead of rollback  
→ Rollback failed, hotfix validated as working for GFax

**June 24, 06:52-07:14 MT** - AS2 hotfix rolled back  
→ BouncyCastle library conflict, return to stable state

**June 24, 15:51 MT** - Explanation of monolithic coupling to GLT/SLT  
→ Decision framework for next hotfix attempt (consult CJ/SMEs)

### Organizational Tensions

**June 24, 09:08 MT** - Arshad questions engineering rigor ("clean code")  
→ Daniel explains tight coupling, Marten counters with DevOps issues  
→ Ramesh documents 18-month KT failure and pipeline proliferation

---

## Key Quotes

### Daniel Milburn (June 22, 21:39 MT DM)
> "We used to be myopically focused on one thing at a time. We'd do a release or an upgrade or a DB change. The exchange we've made is risk vs speed... To enable that I've handed off responsibility for hardening the release to HM, but obviously that cost us on this release."

> "This was our first stress test, and we sprung some leaks. Which, you know, we didn't sink. But our first class passengers got wet and that's not good."

### Marten Engblom (June 24, 10:00 MT Group DM)
> "I just want to make sure we keep all root causes, as well as contributing and compounding issues in sight."

### Chrystie Leonard (June 24, 08:02 MT)
> "It seems we are seeing more incident turbulence this morning, which is causing significant unrest among customers."

---

## Next Steps Identified

### Immediate
- ✅ Resume MEX Orders fix (RESOLVED June 23)
- ✅ DB data correction scripts (COMPLETED June 24)
- 🟡 Complete tracking issue investigation
- 🟡 Decision on re-attempting PDF hotfix (remove eInvoicing changes)

### Short-term (Week of June 24)
- **RCA Sessions:** Friday June 26 and Monday June 29 (Marten/Arshad partnering to lead, blameless postmortem, everyone has voice)
- **RCA Scope:** This incident + all GFax issues from last month (Steve Jackson raised reliability concerns over 4-8 weeks)
- **RCA Publication:** End of day Monday, June 29
- **Leadership Communication:** Draft email to GLT/SLT (pending Ramesh review) covering status, path forward, RCA timeline
- **CI/CD Pipeline Standardization:** Arshad to lead accelerated plan for 100% teams on standard pipelines (CJ: "all options on table")
- HM DevOps capability and hand-off protocol review
- Address Actions team manager gap
- Document rollback procedures

### Medium-term (Strategic)
- Evaluate team distribution across initiatives
- Re-assess risk vs. speed trade-offs
- Review environment parity (STG vs. PRD)
- Address monolithic deployment coupling
- Strengthen testing protocols for library upgrades
- Clarify FTE vs. contractor ownership boundaries
- Pipeline audit and cleanup

---

## Related Documents

**Career Evidence:** [05-Areas/Career/Evidence/2026-06-22_Multi_Issue_Production_Incident_Leadership.md](../../05-Areas/Career/Evidence/2026-06-22_Multi_Issue_Production_Incident_Leadership.md)

**Session Learnings:** System/Session_Learnings/2026-06-23.md

---

## Document Metadata

**Incident Managers:** Gaurav Saini (US), Oliver Kampmann (EU)  
**Engineering Leadership:** Marten Engblom (21h 52m active), Daniel Milburn, Ramesh Donnipadu (handoff)  
**Created:** June 23, 2026  
**Last Updated:** June 24, 2026  
**Status:** Incident resolved, follow-up work ongoing

**Salesforce Cases:** 4-0011979642 (GFax, eInv), 4-0011979745 (EU Orders), 4-0011987121 (AS2)  
**JIRA:** EGXC-53892 (MEX Orders)  
**Slack:** #ghx_incident_rm_1, #ghx_incident_rm_2
