# Release Progression Timeline - 2.273.x Series

**Original Release:** CoreX-ALL-2.273.4 (June 22, 2026 ~12:50 AM MT)  
**Final Fix:** CoreX-ALL-2.273.7 (June 23, 2026 ~3:00 PM MT)  
**Total Duration:** ~38 hours from initial release to final fix deployment

---

## Release Timeline

### 2.273.4 - The Problem Release

**Deployed:** June 22, 2026 at 12:50 AM MT  
**Status:** Introduced 6 production issues

**Issues introduced:**
1. EU non-functional (missing DB users for BT connection strings)
2. MEX Orders can't load purchase details
3. Tracking issue causing document loops and concurrent retry failures
4. GFax SFTP/SSH Algorithm Negotiation Failure (separate IO release, rolled back)
5. GFax PDF Conversion Failure
6. EML2PDF Action Word conversion failures

**Root cause note from [[Gregory_Bank|Gregory Bank]]:**
> "it was caused by the 2.273.4 release, 2.273.5 was the first fix 🙂"

---

### 2.273.5 - First Hotfix Attempt

**Status:** Partial fix - only addressed one of two affected classes

**What it fixed:**
- One class with PDF conversion issue

**What it missed:**
- Second class with the same defect pattern

**Result:**
- Issues persisted after deployment
- Required another hotfix

**Quote from [[Ramesh_Donnipadu|Ramesh's]] email (June 23, 5:30 AM MT):**
> "An initial fix was deployed to STG, INT, and PROD; however, it did not fully resolve the issue. A second root cause has been identified — a separate class with the same defect."

---

### 2.273.6 - Second Hotfix (GFax/EML2PDF Complete Fix)

**Status:** Successfully fixed the missed class from 2.273.5

**Timeline:**
- Dev team identified second affected class
- Applied same fix pattern to missed class
- Local testing before redeployment
- Full pipeline deployment (STG → INT → PROD)

**Deployment challenges:**
- Blocked by deployment pipeline issues (see [[2026-06-23_Deployment_Pipeline_Crisis.md]])
- Required emergency coordination with India-based DevOps contractors
- Pipeline pointed to wrong region (West instead of East)
- AWS credential mismatches
- Auto Scaling Group capacity issues

**ETA provided:** ~3-4 hours from identification to production

---

### 2.273.7 - MEX/Tracking Fix

**Deployed:** June 23, 2026 ~3:00 PM MT  
**Status:** Fixed MEX Orders and Tracking issues

**Build announcement from [[Maria_Livingston|Maria Livingston]] (June 23, 2:49 PM MT):**

> Hi Team, please find the release status for **CoreX-ALL-2.273.7** below:
>
> - JIRA/PR Merged: DocEnrich/MEXV-16689
> - Version Bump: Completed
> - Build: Initiated
>
> You can track the build status via the Bamboo build pipeline:
> 🔗 https://bmb01.ghx.com:8443/browse/EGX-CORAL-17
>
> Bamboo deployment plan:
> 🔗 https://bmb01.ghx.com:8443/deploy/viewDeploymentProjectEnvironments.action?id=185237507

**PR Details:**
- PR #42196: https://stash.ghx.com:7893/projects/EGX/repos/all/pull-requests/42196/overview
- PR complete 6 hours before merge
- Delayed because team was working on 2.273.6 deployment
- Didn't want to interfere with testing on STG

**Quote from [[Matthew_Turner|Matthew Turner]] (June 23, 2:05 PM MT):**
> "At the point this pr was ready, the other hotfix was being tested on stg. We didn't push this to get merged as the other issue was a priority, and we didn't want to mess with the testing of that work on stg"

**Post-Deployment Work:**
- DB correction script execution
- Tracking flow resends
- Example transactions needing reprocessing:
  - TRXc5c17e38408d440eb6fa9828e92c36a7
  - TRX06bb1d6db1c84ccb8358ca9f3d68a4d9

**Completion from [[Shannon_Medina|Shannon Medina]] (June 23, 3:53 PM MT):**
> "Deelen, Dennis and I have completed tracking flow resends."

---

## Parallel Issue: SCA Scheduled Reports

**Issue discovered:** Overnight June 22-23  
**Not fixed by 2.273.x series** - different root cause

**Technical problem:**
- NumberLong fields began arriving as NumberDecimal after 12:50 AM MT
- Caused ETL pipeline failure
- Affected scheduled report generation

**Impact:**
- EU: ~83,700 documents
- US: Millions of documents
- All SCA customers receiving stale data

**Resolution approach:**
1. Deploy Hari's fix (part of 2.273.7 - handles NumberDecimal for new documents)
2. Run one-time historical data reprocessing (from 12:50 AM MT to post-deployment)
3. Confirm reprocessing scope and ETA with ETL team post-deployment
4. Loop in Product/CSM for customer communication

**Timeline:** 8+ hours for background data correction

---

## Deployment Bottlenecks

### Pipeline Issues (All Releases)

**Problems:**
- Pipelines cloned from "incident-game" template during DR work
- Most configurations pointing to West region (production in East)
- AWS credential ID mismatches
- Auto Scaling Group capacity set to 0
- Knowledge held by offshore contractors

**Impact on fix deployment:**
- Multi-hour delays even with fixes ready
- Required late-night coordination with India team
- Made rollback impossible (same pipeline issues would affect rollback)

**Quote from [[Marten_Engblom|Marten]] to [[Rammi_Gill|Rammi]] (June 23, 6:55 AM MT):**
> "As of last night we had fixes ready, but the holdup was related to deployment pipelines, meaning **we would have the same issue with a rollback as with rolling forward.**"

---

## Why Multiple Hotfixes Were Needed

### Issue 1: Incomplete Fix Pattern Application
- First fix (2.273.5) applied to one affected class
- Pattern existed in two classes
- Developer either missed second class or prioritized speed
- Required 2.273.6 to complete

### Issue 2: Sequential Testing Strategy
- Team tested one fix at a time on STG
- Didn't want to mix fixes and risk test validity
- PR #42196 ready 6 hours before merge
- Intentionally delayed to avoid interfering with GFax/EML2PDF testing

### Issue 3: Different Root Causes
- MEX/Tracking (2.273.7) was different code path than GFax/EML2PDF (2.273.6)
- SCA reporting was data type issue (NumberLong → NumberDecimal)
- Each required separate analysis and fix

---

## Lessons from Release Progression

### What Worked
1. Team identified pattern in failed fix and applied to second class
2. Sequential testing prevented mixing fixes
3. Clear version progression made it easy to track what was deployed where

### What Didn't Work
1. Initial fix incomplete - missed second affected class
2. No automated pattern detection (e.g., "if this class has the issue, are there others?")
3. Deployment pipeline state prevented rapid iteration
4. Rollback not viable due to pipeline issues

### Questions for RCA
1. **Why was the initial fix incomplete?**
   - Time pressure during incident?
   - Inadequate code search for similar patterns?
   - Testing gaps that didn't catch the second class?

2. **Could we have parallel-deployed fixes?**
   - Risk: harder to isolate issues if new problems arose
   - Benefit: faster resolution
   - What's the right balance?

3. **Why did deployment pipelines become a bottleneck?**
   - See [[2026-06-23_Deployment_Pipeline_Crisis.md]]
   - Change management for pipelines?
   - Testing of pipeline modifications?

4. **How do we prevent data type mismatches?**
   - NumberLong → NumberDecimal change
   - Where did this originate?
   - Schema validation at boundaries?

---

## Customer Impact by Release

### 2.273.4 (Problem Release)
- 5,200+ undelivered purchase orders (GFax)
- 1,891 failed invoice documents (EML2PDF)
- MEX/IBR order visibility issues
- EU completely non-functional (4-5 hours)
- Major customers affected: Stryker and others

### 2.273.5 (Partial Fix)
- Reduced but didn't eliminate PDF conversion failures
- Customer impact continued

### 2.273.6 (Complete GFax/EML2PDF Fix)
- Resolved remaining PDF conversion issues
- Began backlog processing
- MEX/Tracking issues still present

### 2.273.7 (MEX/Tracking Fix)
- Resolved MEX order visibility
- Fixed tracking loops
- Required manual transaction reprocessing
- ~50k transactions "In Progress" needing tracking flow resends

### SCA Issue (Parallel Track)
- EU: 83,700 stale documents
- US: Millions of stale documents
- 8+ hour background correction after fix

---

## Timeline Summary

| Time | Event |
|------|-------|
| June 22, 12:50 AM MT | 2.273.4 deployed - introduced 6 issues |
| June 22, ~6:00 AM MT | EU issue resolved (DB users added) |
| June 22, Morning | GFax SFTP issue resolved (IO release rollback) |
| June 22, 7:30 PM MT | 4 issues remain, 2 fixes ready but blocked on pipelines |
| June 22, 7:45 PM MT | Contact established with India DevOps team |
| June 22-23, Overnight | 2.273.5 deployed (partial fix), issues persist |
| June 23, ~5:30 AM MT | Second affected class identified, SCA issue discovered |
| June 23, Morning | 2.273.6 deployment in progress |
| June 23, ~2:49 PM MT | 2.273.7 build initiated |
| June 23, ~3:53 PM MT | Tracking flow resends completed |
| June 23, Evening | Background data correction ongoing (8+ hours) |

**Total resolution time:** ~38 hours from initial release to final fix completion

---

## Related Documents

- [[2026-06-22_Production_Incident_Comprehensive_Record.md]] - Full incident narrative
- [[2026-06-23_Deployment_Pipeline_Crisis.md]] - Why fixes were delayed
- [[2026-06-22_Executive_Email_Thread_Complete.md]] - Leadership communication during progression
