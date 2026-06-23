# Executive Email Thread - Update on Ongoing Incidents

**Date Range:** June 22-23, 2026  
**Participants:** [[Marten_Engblom|Marten Engblom]], [[CJ_Singh|CJ Singh]], [[Curtis_Nielsen|Curtis Nielsen]], [[Arshad_Mahammad|Arshad Mahammad]], [[Ramesh_Donnipadu|Ramesh Donnipadu]]

---

## Initial Update (June 22, 7:58 PM MT)

**From:** [[Marten_Engblom|Marten Engblom]]  
**To:** [[CJ_Singh|CJ]], [[Curtis_Nielsen|Curtis]]  
**Time:** Monday, June 22, 2026 at 7:58 PM MT

CJ, Curtis,

I just wanted to provide an update on a number of incidents related to the Exchange release this morning, in case you get questions.

Following this morning's early release (approx. 2:00 AM MT), we experienced six production issues. Here's where we stand as of 7:30 PM MT:

1. **RESOLVED:** EU wasn't functional after the release due to missing DB users for BT connection strings
2. **IN PROGRESS:** MEX Orders can't load purchase details - Owned by Visibility team in India, will be picked up when they come back online. A workaround exists but is suboptimal for customers.
3. **IN PROGRESS:** Tracking issue causing document loops and concurrent retry failures
4. **RESOLVED:** GFax SFTP/SSH Algorithm Negotiation Failure - IO Release rolled back
5. **FIX READY:** GFax PDF Conversion Failure - Fix coded and tested, blocked on deployment pipeline (see below)
6. **FIX READY:** EML2PDF Action Word conversion failures - Fix coded and tested, blocked on deployment pipeline (see below)

See Slack thread here for more details: https://ghx.slack.com/archives/CEY5JQ7KJ/p1782141473955759

### Customer impact

We have **5,200+ purchase orders undelivered via GFax** as of 2:30 PM and that number continues to grow. Additionally, **1,891 invoice documents** have failed due to Word-to-PDF conversion issues, and we're seeing MEX/IBR application issues impacting order visibility and processing.

**Stryker and other major customers** are impacted by multiple incidents simultaneously. We are providing hourly status updates as required for purchase order-impacting incidents.

### Current state

We have fixes ready for issues #5 and #6 but are having issues deploying them to staging for testing. Our deployment pipelines are in a state that is unfamiliar to our US-based team and require knowledge held by Happiest Minds contractors who made recent changes to the pipelines. [[Daniel_Milburn|Daniel Milburn]] is actively working to reach the necessary resources in India (Ramya, Sujith, Vignesh) to execute the deployments.

**There are definitely gaps in our incident response and deployment processes that we will need to address thoroughly in the Root Cause Analysis and retrospective following resolution.**

### Next steps

1. We just now (7:45) got a hold of the Happiest Minds DevOps resources to execute the staging deployment.
2. The goal is to test and deploy the fixes for the GFax PDF conversion and EML2PDF issues tonight.
3. Tomorrow morning when the Visibility team in India comes back online, they'll resume work on the MEX issue. We'll then deploy the tested fixes to production and begin reconciliation of failed transactions.

Feel free to reach out with any questions.

---

## CJ's Questions (June 22, 9:02 PM MT)

**From:** [[CJ_Singh|CJ Singh]]  
**To:** [[Marten_Engblom|Marten]], [[Curtis_Nielsen|Curtis]]  
**Cc:** [[Arshad_Mahammad|Arshad]]  
**Time:** Monday, June 22, 2026 at 21:02 MT

+Arshad

Thanks for the update, Marten.

Few questions:

1. How many incidents are called and open right now? How many are closed?
2. Was there anything different about this release? I don't recall a release causing so many incidents?

---

## Marten's Response - Incident Count & Risk Analysis (June 22, 10:12 PM MT)

**From:** [[Marten_Engblom|Marten Engblom]]  
**To:** [[CJ_Singh|CJ]], [[Curtis_Nielsen|Curtis]]  
**Cc:** [[Arshad_Mahammad|Arshad]]  
**Time:** Monday, June 22, 2026 at 22:12 MT

There are **2 official incidents open** (but they comprise the 6 issues below):

- **4-0011979642** is the incident ticket for Gfax, eInv incident.
- **4-0011979745** is the EU incident (running in incident room 2) for the Red bar/MEX/IBR incident

### For your second question

Nothing dramatically different about this release at a glance, and although I am hesitant to speculate, but thinking freely here, in hindsight there might be a few things that arguably increased the risk:

1. We have a few more initiatives in flight than normal, all contributing with changes to this release package ("regular" commercial and technical work, Atlas migration related changes etc.)
2. We are executing the Atlas migrations and our "regular" development cycles in parallel - we are currently in a state where some lower environments being Atlas but PROD is still self hosted MongoDB
3. Beyond more than usual parallel work contributing to the release footprint, we are arguably also more "parallelized" with our resources (both ICs and supervisors), with many competing priorities in flight at the same time:
   - "Regular" commercial work
   - "Regular" tech debt work
   - Atlas migrations
   - Elasticsearch migrations
   - Aurora migrations
   - Red Mythos vulnerabilities work and environments
   - Disaster Recovery work
   - AI up-leveling and other SDLC changes
   - Hiring and team-building
   - Playwright migrations vs. release testing/certification

**Again, just thinking out loud here. Not at all sure if any of this contributed to the issues.**

---

## CJ's Response - Deep Dive Request (June 22, 10:17 PM MT)

**From:** [[CJ_Singh|CJ Singh]]  
**To:** [[Marten_Engblom|Marten]], [[Curtis_Nielsen|Curtis]]  
**Cc:** [[Arshad_Mahammad|Arshad]]  
**Time:** Monday, June 22, 2026 at 22:17 MT

ok thnx

Once the incidents are closed, lets do a **deep dive on root causes** … this would deserve a dedicated deep dive … we can sort out the specifics of the deep dive once we are all clear

---

## Handoff to Ramesh (June 22, 11:55 PM MT)

**From:** [[Marten_Engblom|Marten Engblom]]  
**To:** [[CJ_Singh|CJ]], [[Curtis_Nielsen|Curtis]], [[Ramesh_Donnipadu|Ramesh]]  
**Cc:** [[Arshad_Mahammad|Arshad]]  
**Time:** Monday, June 22, 2026 at 23:55 MT

+ @[[Ramesh_Donnipadu|Ramesh Rangavithal Donnipadu]]

Definitely CJ, there will be plenty to discuss it seems.

**I am signing off for tonight, Ramesh is taking over oversight and decision making.** The team is working to get the hot fixes out to production before the start of tomorrow East Coast time.

Marten

---

## Ramesh's Morning Update (June 23, 5:30 AM MT)

**From:** [[Ramesh_Donnipadu|Ramesh Rangavithal Donnipadu]]  
**To:** [[Marten_Engblom|Marten]], [[CJ_Singh|CJ]], [[Curtis_Nielsen|Curtis]]  
**Cc:** [[Arshad_Mahammad|Arshad]]  
**Time:** Tuesday, June 23, 2026 at 05:30 AM MT

All,

**Update at 5:30AM MT**

Providing a current status update on three active incidents:

### 1. GFax PDF Conversion Failures & EML2PDF Word Conversion Failures

An initial fix was deployed to STG, INT, and PROD; however, it did not fully resolve the issue. **A second root cause has been identified — a separate class with the same defect.** Dev is actively working the fix. The deployment to STG→INT→PROD will need another 2 hours.

**ETA for resolution: 7:30 AM MT**

### 2. MEX Orders & Tracking Issue

A code fix has been deployed to STG and is currently under QA validation. Promotion to INT and PROD will follow once sign-off is received and no regressions are observed.

**Status:** In validation. Prod deployment pending QA sign-off.

### 3. SCA Scheduled Reports Failure (New)

A new issue has surfaced in SCA — scheduled reports are failing due to a **data type mismatch**. The upstream BT and BD collections are now returning a different data type than expected, causing report generation to fail.

Hari's fix from item 2 above will address the code-level defect. However, **stale data accumulated over the past 24-30 hours will require manual reconciliation** before historical report generation is restored.

**Impacted volume:**
- EU — ~83,700 documents
- NA — Millions of documents

**Recommended action:** Engage the SCA CSM team to proactively communicate impact to affected customers ahead of escalation.

Regards,

Ramesh Donnipadu  
Engineering Director

---

## Key Themes

### 1. Deployment Pipeline Crisis
- Fixes were ready but blocked by deployment pipeline issues
- Pipelines were modified by Happiest Minds contractors in India
- US team was unfamiliar with the modified state
- Required late-night coordination with India-based DevOps resources

### 2. Incomplete Initial Fix
- First hotfix (2.273.5) only addressed one of two affected classes
- Second hotfix (2.273.6) required to fix the missed class
- Pattern suggests rushed deployment under pressure

### 3. Cascading Failures
- New SCA issue discovered overnight
- Data type mismatch (NumberLong → NumberDecimal) caused ETL failures
- Millions of documents affected in US, 83,700 in EU

### 4. Risk Factor Analysis
Marten identified potential contributing factors:
- Higher than normal parallel initiatives in single release
- Mixed environment state (some Atlas, PROD still MongoDB)
- Resource fragmentation across 10+ competing priorities
- Parallel migrations (Atlas, Elasticsearch, Aurora)

### 5. Leadership Expectations
CJ explicitly requested deep dive on root causes once incidents closed
