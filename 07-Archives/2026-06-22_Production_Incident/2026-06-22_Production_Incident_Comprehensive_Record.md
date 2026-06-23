# Production Incident - June 22, 2026
## CoreX-ALL 2.273.x Release

**Incident Duration:** 02:00 MT (release) → Ongoing (multi-day resolution)  
**Incident Managers:** [[Gaurav_Saini]] (IM), [[Oliver_Kampmann]] (EU IM)  
**GHX Engineering Leadership:** [[Marten_Engblom]], [[Daniel_Milburn]], [[Ramesh_Donnipadu]] (handoff)  
**Key Contributors:** [[Gregory_Bank]], [[Matt_Walker]], [[Suresh_Kumar]], [[Paul_Bobbitt]], [[Kooper_Frahm]]

---

## Executive Summary

Following the early morning release (approx. 02:00 MT), we experienced **six simultaneous production issues** — an unprecedented event for the Exchange platform. By 23:45 MT (nearly 22 hours later), four issues were resolved or had fixes deployed, with two remaining in progress for handoff to the India team.

**Customer Impact:**
- 5,200+ purchase orders undelivered via GFax (as of 14:30 MT, continuing to grow)
- 1,891 invoice documents failed PDF conversion
- MEX/IBR application issues impacting order visibility and processing
- Multiple major customers impacted simultaneously (Stryker, Hartford Healthcare)
- Hourly status updates required per incident protocol

**Incident Channels:**
- #ghx_incident_rm_1 (Primary)
- #ghx_incident_rm_2 (EU paused incident)
- #eu-incident-managers
- #ghx_tsoc_incident_notifications

---

## Issues and Resolution Status

### 1. ✅ RESOLVED: EU Database Connection Failures
**Impact:** EU region completely non-functional after release  
**Root Cause:** Missing database users for BT/BD connection strings in Atlas migration  
**Resolution:** Connection strings corrected, EU restored  
**Category:** Atlas Migration / Sloppy Migration Work

### 2. 🟡 IN PROGRESS: MEX Orders - Purchase Details Loading Failure
**Impact:** Customers unable to view order purchase details in MyExchange  
**Root Cause:** BTBD (Atlas-migrated database) behavior change causing query failures  
**Status:** Code fix complete, awaiting testing and deployment  
**Owner:** Visibility team ([[Prashanth_Garlapati]], [[Hari_Prasad_Narasapu]])  
**ETA:** Testing in STG → PRD deployment when India team returns online  
**Category:** Atlas Migration / Environment Drift (STG has Atlas, PRD doesn't)  
**JIRA:** EGXC-53892

### 3. 🟡 IN PROGRESS: Tracking Document Loops and Retry Failures
**Impact:** Documents stuck in retry loops, concurrent modification failures  
**Status:** Investigation ongoing  
**Category:** Unknown / Code Issue

### 4. ✅ RESOLVED: GFax SFTP/SSH Algorithm Negotiation Failure
**Impact:** GFax unable to connect to customer SFTP servers  
**Root Cause:** Library upgrade in IO release (SSH algorithm compatibility)  
**Resolution:** IO release rolled back  
**Category:** Library Upgrade / Insufficient Testing

### 5. ✅ DEPLOYED: GFax PDF Conversion Failures
**Impact:** ~5,200+ purchase orders failed conversion/delivery (~75% failure rate)  
**Root Cause:** Code issue in Actions team area  
**Resolution:** Fix coded by [[Matt_Walker]], tested in STG, deployed to PRD overnight  
**Version:** 2.273.5 hotfix  
**Deployment Completion:** ~03:00 MT June 23 (after ~10 hours of deployment pipeline struggles)  
**Category:** Code Issue / Actions Team (no manager)

### 6. ✅ DEPLOYED: EML2PDF Word Conversion Failures
**Impact:** 1,891 invoice documents failed Word-to-PDF conversion  
**Root Cause:** Code issue in Actions team area  
**Resolution:** Bundled with issue #5, same hotfix deployment  
**Version:** 2.273.5 hotfix  
**Category:** Code Issue / Actions Team (no manager)

---

## Timeline (Key Events)

**02:00 MT** - Release begins  
**~05:30 MT** - Multiple issues detected, incident channels activated  
**11:07 MT** - Summary captured: GFax biggest issue, customer comms sent  
**14:30 MT** - 5,200+ failed GFax orders counted  
**~19:00 MT** - Fixes for issues #5 & #6 code complete, blocked on deployment  
**19:30 MT** - Executive summary written, major deployment pipeline struggles  
**21:12 MT** - DevOps lead (Anandaraj) appears to drop off / lose connectivity  
**22:19 MT** - Request for Ramesh handoff due to HM DevOps challenges  
**23:38 MT** - Official handoff to [[Ramesh_Donnipadu]], Marten and Daniel sign off  
**23:40 MT** - Daniel watching "Lonesome Dove" as second incident movie  
**23:42 MT** - Oliver takes over EU incident manager role  
**~01:00 MT June 23** - STG validation passes for 2.273.5 hotfix  
**~03:00 MT June 23** - PRD deployment completes for issues #5 & #6

---

## Root Causes & Contributing Factors

### Technical Factors
1. **Environment Drift:** STG migrated to Atlas/Aurora/ES, but PRD hasn't → issues not caught in testing
2. **Sloppy Migration Work:** EU connection strings incomplete (Atlas)
3. **Library Upgrades Without Adequate Testing:** IO SFTP/SSH algorithm issues
4. **Team Area Without Manager:** Actions team (GFax, EML2PDF) issues orphaned
5. **No Rollback Testing:** Extended downtime because rollback capability unclear

### Organizational Factors (DM Analysis with Daniel)
1. **Team Stretched Across Too Many Initiatives:**
   - "Regular" commercial work
   - "Regular" tech debt
   - Atlas migrations
   - Elasticsearch migrations
   - Aurora migrations
   - Red Mythos vulnerability work
   - Disaster Recovery work
   - AI up-leveling and SDLC changes
   - Playwright migration vs. release testing/certification
   - Hiring and team-building

2. **Key People Focused Elsewhere:**
   - Bank/Pbob: Playwright migration and testing strategy (not Certification)
   - Suresh/Matt: Atlas and Mapping (not release hardening)
   - DevOps responsibility handed to HM but capability gaps exposed

3. **First Time Unable to Release with FTE Resources Alone**
   - HM DevOps team knowledge gaps
   - Infrastructure changes unfamiliar to US team
   - Hand-off failures and communication gaps
   - DevOps lead dropped off mid-incident (~21:12 MT)

### Process Gaps
1. **Incident Response Dysfunctions:** Witnessed firsthand, need RCA
2. **Deployment Pipeline Complexity:** ~10 hours to deploy tested hotfix
3. **Knowledge Silos:** Critical deployment knowledge held by specific HM contractors
4. **Team Participation Gaps:** Hari participated, but Prashanth and Ramesh did not initially

---

## Leadership Decisions & Actions

### Incident Management (Marten)
- Active oversight and decision-making for ~21 hours (02:00 → 23:38 MT)
- Coordinated with Daniel, Gregory, and incident managers
- Ensured hand-off to Ramesh with clear context and decision authority
- Requested hourly updates in incident channels

### Technical Leadership (Daniel)
- More involved in incident process than usual, witnessed organizational dysfunctions
- Coordinated with HM leadership to find DevOps resources
- Supported fix development and testing coordination
- Provided historical context on team changes and risk trade-offs

### Key Quote (Daniel, 21:39 MT DM)
> "We used to be myopically focused on one thing at a time. We'd do a release or an upgrade or a DB change. The exchange we've made is risk vs speed... To enable that I've handed off responsibility for hardening the release to HM, but obviously that cost us on this release."

> "This was our first stress test, and we sprung some leaks. Which, you know, we didn't sink. But our first class passengers got wet and that's not good."

---

## Next Steps Identified

### Immediate (June 23)
- [ ] Resume MEX Orders fix testing/deployment (Visibility team, India)
- [ ] Complete tracking issue investigation and fix
- [ ] Begin reconciliation of failed GFax transactions

### Short-term (Week of June 23)
- [ ] Root Cause Analysis for all 6 issues
- [ ] Retrospective on incident response process gaps
- [ ] Follow up with HM about DevOps capability and hand-off protocols
- [ ] Address Actions team manager gap
- [ ] Document rollback procedures and testing requirements

### Medium-term (Strategic)
- [ ] Evaluate team distribution across initiatives
- [ ] Re-assess risk vs. speed trade-offs
- [ ] Review environment parity requirements (STG vs. PRD)
- [ ] Strengthen testing protocols for library upgrades
- [ ] Clarify FTE vs. contractor ownership boundaries
- [ ] Release note discipline (Summary, Test Plan consistently documented)

---

## References

**Slack Channels:**
- #ghx_incident_rm_1 (Primary incident coordination)
- #ghx_incident_rm_2 (EU paused incident - MEX Orders)
- #exchange_devops (Deployment coordination)
- #help-corex (Infrastructure updates)
- Direct DM with Daniel Milburn (Root cause discussion)

**Salesforce Cases:**
- 4-0011979745 (EU Orders/Worklist)
- Various customer-specific cases (Stryker, Hartford Healthcare)

**JIRA:**
- EGXC-53892 (MEX Orders issue)
- Hotfix version: CoreX-ALL-2.273.5

**Email:**
- Multiple incident updates from Oliver Kampmann (EU IM)
- Internal status updates throughout the day

**Leadership Communications:**
- Executive Summary to Curtis Roady & CJ Singh (19:38 MT) - [`2026-06-22_Executive_Summary_to_Curtis_and_CJ.md`](2026-06-22_Executive_Summary_to_Curtis_and_CJ.md)
- Formal handoff message in #ghx_incident_rm_1 (23:52 MT) - [`2026-06-22_Handoff_Message_Incident_Room.md`](2026-06-22_Handoff_Message_Incident_Room.md)
- Communication analysis - [`2026-06-22_Incident_Leadership_Communications.md`](2026-06-22_Incident_Leadership_Communications.md)
- Internal strategic analysis with Daniel Milburn (captured in this document)

---

## Career Context

This incident represents significant leadership challenges across multiple dimensions:
- **Crisis Management:** Sustained 21-hour incident oversight with complex multi-issue coordination
- **Technical Leadership:** Navigating environment drift, migration complexity, team distribution challenges
- **Organizational Leadership:** Hand-off protocols, vendor management, team capacity assessment
- **Strategic Decision-Making:** Understanding accepted risks that materialized, identifying systemic improvements

**Competencies Demonstrated:**
- Incident Management
- Crisis Leadership
- Technical Architecture (understanding environment drift risks)
- Team Coordination (US/EU/India across timezones)
- Vendor Management (HM DevOps challenges)
- System Thinking (identified organizational factors, not just technical)
- Endurance (21-hour sustained leadership)

---

**Document Status:** Comprehensive incident record for reference, RCA, retrospective, and career evidence  
**Created:** 2026-06-23  
**Last Updated:** 2026-06-23
