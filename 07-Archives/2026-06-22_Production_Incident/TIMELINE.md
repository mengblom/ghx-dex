# Production Incident Timeline - June 22-24, 2026

**Incident:** CoreX-ALL 2.273.x Release | **Duration:** 02:00 MT June 22 → June 24 EOD

---

## June 22, 2026 (Day 1)

- **02:00** - Release begins (CoreX-ALL 2.273.4)
- **~02:30** - Multiple issues start appearing: EU non-functional (DB connection strings), GFax PDF conversion failures, MEX Orders purchase details loading failures, tracking document loops, EML2PDF Word conversion failures
- **~05:30** - Incident channels activated (#ghx_incident_rm_1 primary, #ghx_incident_rm_2 EU)
- **11:07** - Summary captured: GFax identified as biggest customer-facing issue, customer communications sent, hourly status updates initiated
- **14:30** - Customer impact quantified: **5,200+ GFax purchase orders undelivered** (continuing to grow), **1,891 invoice documents failed** (Word-to-PDF), MEX/IBR issues impacting order visibility, Stryker and other major customers impacted by multiple issues simultaneously
- **~15:00** - Fixes developed for GFax and EML2PDF issues, testing complete, ready for deployment but blocked
- **~19:00** - Fixes blocked on deployment pipeline issues (pipelines modified by Happiest Minds contractors, US team unfamiliar with pipeline state)
- **19:30** - Executive summary drafted and vetted with Daniel Milburn, Suresh Kumar, Kooper Frahm
- **19:38** - **[COMMUNICATION]** Marten sends executive summary to Curtis Roady and CJ Singh (6 issues, customer impact, deployment pipeline gaps surfaced) → [Executive Summary](2026-06-22_19.38_Executive_Summary_to_Curtis_and_CJ.md)
- **~19:45** - Daniel Milburn coordinating with Happiest Minds leadership to find DevOps resources (Ramya, Sujith, Vignesh)
- **19:58** - **[COMMUNICATION]** Marten sends email update to CJ and Curtis (details 6 production issues and status, quantifies customer impact, identifies deployment pipeline knowledge gaps) → [Initial Email Update](2026-06-22_Executive_Email_Thread_Complete.md#initial-update-june-22-758-pm-mt)
- **21:02** - **CJ Singh asks questions:** (1) How many incidents open vs closed? (2) Was there anything different about this release?
- **21:12** - DevOps lead (Anandaraj) appears to drop off / lose connectivity
- **22:12** - **[COMMUNICATION]** Marten responds to CJ's questions (2 official incidents covering 6 issues, risk factor analysis: 10+ parallel initiatives, environment drift (Atlas), resource fragmentation) → [Risk Analysis Response](2026-06-22_Executive_Email_Thread_Complete.md#martens-response---incident-count--risk-analysis-june-22-1012-pm-mt)
- **22:17** - **CJ responds:** Requests deep dive on root causes once incidents closed
- **22:19** - Request for Ramesh handoff due to HM DevOps challenges
- **23:38** - Marten and Daniel officially hand off to Ramesh Donnipadu
- **23:40** - Daniel Milburn watching "Lonesome Dove" (second incident movie reference)
- **23:42** - Oliver Kampmann takes over EU incident manager role
- **23:52** - **[COMMUNICATION]** Marten posts formal handoff message in #ghx_incident_rm_1 (designates Ramesh as decision authority, provides prioritization guidance) → [Handoff Message](2026-06-22_23.52_Handoff_to_Ramesh_Slack.md)
- **23:55** - **[COMMUNICATION]** Marten sends handoff email to CJ, Curtis, Ramesh ("I am signing off for tonight, Ramesh is taking over oversight and decision making") → [Email Handoff](2026-06-22_Executive_Email_Thread_Complete.md#handoff-to-ramesh-june-22-1155-pm-mt)

## June 23, 2026 (Day 2)

- **~01:00** - STG validation passes for 2.273.5 hotfix (fixes for GFax PDF and EML2PDF issues)
- **~03:00** - PRD deployment completes (2.273.5) after ~10 hours of deployment pipeline struggles
- **05:30** - **Ramesh sends morning update email:** Initial fix incomplete - second root cause identified (separate class with same defect), new SCA issue discovered (data type mismatch affecting millions of documents), ETA for complete fix: 7:30 AM MT → [Ramesh Morning Update](2026-06-22_Executive_Email_Thread_Complete.md#rameshs-morning-update-june-23-530-am-mt)
- **~07:59** - **[COMMUNICATION]** Marten sends "Exchange Incident Update" to GLT (started rollback process, ~6,500 GFax POs undelivered over last ~30 hours, MEX/IBR suppliers unable to view orders, internal ETA for rollback: 90-120 minutes)
- **10:30** - Vast majority of GFax orders successfully processed and sent (hotfix validated as working)
- **~10:34** - **[COMMUNICATION]** Marten sends follow-up to GLT (unable to rollback to previous release, hotfix did resolve GFax issue, evaluating whether to rollback or fix forward for IBR issue, will provide update by afternoon)
- **11:42** - IBR/MEX "red banner" issue resolved with hotfix (US)
- **12:13** - **Steve Jackson requests "blast radius" analysis** (unique suppliers impacted, order volumes, timing metrics; context: gFax reliability declining over 4-8 weeks)
- **12:24** - IBR/MEX issue resolved (EU)
- **~14:00** - Data correction decision made (script running to correct residual data issues impacting CDP, Analytics, other downstream systems)
- **~21:00** - **[COMMUNICATION]** Marten sends EOD update to GLT/Steve Jackson (pivoted from rollback to fixing forward, GFax orders processed as of 10:30 AM, IBR/MEX resolved US 11:42/EU 12:24, DB data correction script running ~8 hour ETA for CDP impact)
- **21:06** - Marten agrees blast radius data should come from RCA follow-up
- **22:26** - **Christopher Luoma suggests RCA consider "full order journey"** (GFax orders flow through IBR → multiple incident impacts cascade on same customers)

## June 24, 2026 (Day 3)

- **~02:00** - Hotfix 2.273.7 deployed to address remaining email-to-PDF issue (DevOps deployed to wrong environment first, testing failed; once deployed correctly, testing passed; hotfix included unrelated eInvoicing library modification)
- **04:36** - **EU AS2 issues begin** (BouncyCastle library version conflict 1.68 vs 1.78, Error: `java.lang.NoSuchFieldError: id_ori_kem`, ~336+ failed flows in CoreX EU)
- **04:56** - **US AS2 issues begin** (~5,186 transactions affected, major customers: Owens & Minor, Intertrade, Philips Healthcare, Cook Medical)
- **~05:00** - DB data correction scripts complete (BigDecimal vs long data type issue resolved, CDP and downstream systems data corrected)
- **06:52** - EU AS2 mitigated (hotfix rolled back to 2.273.6, Matthew Turner confirms via Graylog: `id_ori_kem` errors gone)
- **07:14** - US AS2 mitigated (rollback complete)
- **08:02** - **Chrystie Leonard inquires about "incident turbulence"** (reports "significant unrest among customers", requests update when available)
- **08:30** - **Daniel Milburn DM to Marten** (catching up on overnight events): (1) Bank rejected fix due to wrong environment deployment (2) Once deployed correctly, testing passed (3) Hotfix deployed (4) Hotfix had negative impact on AS2 (5) First rollback FAILED (didn't actually rollback) (6) Second rollback succeeded
- **09:08** - **Arshad Mahammad questions engineering team in #ghx_incident_rm_1:** "Can't keep going back and forth on this anymore", questions engineering rigor and testing discipline, implies "lack of clean code"
  - **Daniel Milburn responds to Arshad:** Explains tight coupling makes dependency conflicts unpredictable, eInvoicing library change from "a while ago" bundled with hotfix, AS2 flow wasn't in scope for testing, decoupling work added to Resiliency roadmap, also discovered pre-existing Odap flows issue (not a regression)
- **09:35** - **[COMMUNICATION]** Marten asks in #ghx_incident_rm_1: "During the short time this hotfix was in production, did we validate that it worked (aside from AS2 issues)?" → **Matthew Turner confirms:** Yes, `OnDemandAP Email To PDF` action was working
- **10:00** - **[COMMUNICATION]** Marten defends engineering team in leadership group DM (to Arshad, Daniel, Ramesh): "To be fair, we are also spending a lot of time on deployments and rollbacks due to the team deploying to the wrong environments (twice in the last couple of days)", "Complete mess with the deployment pipelines", "I just want to make sure we keep all root causes, as well as contributing and compounding issues in sight" → [Slack Context - Organizational Tensions](2026-06-24_Slack_Context_AS2_Rollback.md)
- **Later AM** - **Ramesh sends detailed observations to Arshad:** AllRepos build failures (disk space), deployment without version increment (forcing full rebuild), pipeline confusion (wrong region deployment), 18-month knowledge transfer failure (Gagan → HM DevOps, escalated to Curtis/Taylor previously)
- **15:51** - **[COMMUNICATION]** Marten sends update to GLT/SLT (response to Chrystie Leonard's inquiry, explains hotfix rollback and AS2 impact, identifies "monolithic coupling/dependencies/deployment footprint" as root cause, provides precise timeline 04:36-07:14, decision framework: remove eInvoicing changes and re-release depends on defect impact vs risk tolerance, commits to sync with CJ and SMEs before next decision) → [June 24 Hotfix Rollback Communications](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md)
- **EOD Status:** AS2 flows restored and operational, GFax processing normally (June 23 fix still in place), MEX/IBR operational (June 23 fix still in place), Data cleanup complete (CDP/Analytics corrected), Email-to-PDF still broken (original hotfix target), Decision pending: Re-attempt hotfix with eInvoicing changes removed

---

## Summary Statistics

**Duration:**
- Primary incident: 02:00 MT June 22 → 21:00 MT June 23 (~43 hours)
- Secondary incident (AS2): 04:36 MT June 24 → 07:14 MT June 24 (~2.5 hours)
- Marten's active leadership: 02:00 MT June 22 → 23:52 MT June 22 (21 hours 52 minutes)

**Customer Impact:**
- GFax orders: 5,200+ undelivered (June 22-23)
- Invoice documents: 1,891 failed (Word-to-PDF)
- AS2 transactions: ~5,186 US, ~336+ EU (June 24)
- Major customers: Stryker, Hartford Healthcare, Owens & Minor, Intertrade, Philips Healthcare, Cook Medical

**Issues Resolved:**
- ✅ EU Database Connection Failures | ✅ GFax SFTP/SSH Algorithm Negotiation | ✅ GFax PDF Conversion Failures | ✅ EML2PDF Word Conversion Failures | ✅ MEX Orders Purchase Details Loading | ✅ DB Data Correction (BigDecimal vs long) | ✅ AS2 Connection Failures (rollback)

**Issues Remaining:**
- 🟡 Tracking Document Loops (lower priority) | 🟡 Email-to-PDF Conversion (hotfix rolled back)

**Hotfix Versions:**
- 2.273.4 - Initial problematic release
- 2.273.5 - First hotfix (incomplete fix for GFax/EML2PDF)
- 2.273.6 - Second hotfix (complete fix for GFax/EML2PDF, MEX/IBR)
- 2.273.7 - Third hotfix (attempted PDF fix, broke AS2, rolled back)

**Key Inflection Points:**
1. **19:38 MT June 22** - Marten escalates to Curtis/CJ with executive summary
2. **22:12 MT June 22** - Marten provides risk factor analysis to CJ
3. **23:52 MT June 22** - Formal handoff to Ramesh (21-hour leadership shift)
4. **10:34 MT June 23** - Decision to fix forward instead of rollback
5. **15:51 MT June 24** - Marten explains AS2 rollback and monolithic coupling to GLT/SLT

---

**Purpose:** Chronological reference for RCA, retrospective, and incident pattern analysis  
**Related:** [Comprehensive Record](2026-06-22_Production_Incident_Comprehensive_Record.md) | [Communications Index](COMMUNICATIONS_INDEX.md)
