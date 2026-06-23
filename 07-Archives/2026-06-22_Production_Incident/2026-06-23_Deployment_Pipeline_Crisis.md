# Deployment Pipeline Crisis During Incident Response

**Date:** June 22-23, 2026  
**Context:** Production incident response blocked by deployment pipeline issues  
**Impact:** Multi-hour delay in deploying critical hotfixes

---

## Overview

During the June 22-23 production incident, the team had **fixes ready but could not deploy them** due to deployment pipeline issues. This became a critical bottleneck that extended customer impact and required emergency coordination with offshore contractors.

---

## Timeline of Pipeline Issues

### June 22, Evening (US Time)
- Fixes for GFax PDF conversion and EML2PDF ready
- Team unable to deploy to STG for testing
- Deployment pipelines in "unfamiliar state" to US team

### June 22, 7:45 PM MT
- [[Daniel_Milburn|Daniel Milburn]] successfully reaches Happiest Minds DevOps resources in India
- Resources needed: Ramya, Sujith, Vignesh

### June 23, 11:37 AM MT (Mahboob Update)
**From:** [[Md_Mahboob_Alam_Beg|Md Mahboob Alam Beg]] in #exchange-incident-deployment-updates

> Hi [[Arshad_Mahammad|Arshad]]
>
> [[Gaurav_Duddukuri|Gagan]] and I are currently working on the STG pipeline. **The pipeline configuration appears to be quite messy.** We are not sure why it was copied from the incident-game pipeline, as **most of the configurations were pointing to the west region.**
>
> We have updated all stages to use the east region, including the AMI region configuration.
>
> At the moment, we are facing an **AWS credential ID mismatch issue**, due to which the template is unable to fetch the AMI from the shared account.
>
> Gagan and I took a short break for dinner and will resume once he is back. Meanwhile, I am reviewing the template configuration.
>
> **Action Item (if the STG pipeline still does not work):**
> As [[Anand_Nayak|Anand]] successfully ran the incident pipeline for STG earlier, we may use that pipeline instead, since the stack creation issue appears to have been resolved in the last run based on the logs.
>
> Earlier today, we were facing an application deployment issue in the incident pipeline used by Anand. This was resolved after setting the Auto Scaling Group capacity to 1 (it was previously 0). The Dev team made this configuration change in the morning.

---

## Specific Problems Identified

### 1. Pipeline Cloning and Duplication

**Exchange DevOps Channel - June 23, 1:27 PM MT**

**[[Suresh_Kumar|Suresh Kumar]]:**
> I have done several upgrade work in past and had **never had the need to clone any build and deployment pipelines.** This is not the correct way to do things. **Not only are you losing all historical build and deployment information, but you enter into this mess where its hard to tell which is what.**

**[[Anandaraj_Thangavelu|Anandaraj Thangavelu]]:**
> Yes [[Suresh_Kumar|Suresh Kumar]] I am completely accepting your concern but I thought you gave the permission to alter the main deployment plan for DR activity it was even affecting us too there was some configuration errors too while I use that.
>
> **During our linux upgrade we have no other option instead of cloning** we thought not to affect current pipeline so we made duplicates will be deleted when current release was successful

### 2. Wrong Region Configuration

- Pipelines copied from "incident-game" template
- **Most configurations were pointing to West region**
- Production was in East region
- All stages had to be manually reconfigured

### 3. AWS Credential Mismatch

- Template couldn't fetch AMI from shared account
- Credential ID mismatches blocking deployments

### 4. Auto Scaling Group Misconfiguration

- ASG capacity set to 0 instead of 1
- Prevented application deployment even when pipeline succeeded
- Required manual intervention by Dev team

---

## Impact on Incident Response

### From Marten's DM to [[Arshad_Mahammad|Arshad]] (June 23, 10:17 AM MT)

> They definitely need some support if they can get it. We have compounding issues of:
> - **Deployment pipelines in disarray**
> - **Deployments going to the wrong data center** 😮
> - **Failing builds**
> - Not very accurate updates

### From Marten's DM to [[Rammi_Gill|Rammi Gill]] (June 23, 6:55 AM MT)

**Context:** Discussion about whether to roll back the release

> I agree. As of last night we had fixes ready, but **the holdup was related to deployment pipelines, meaning we would have the same issue with a rollback as with rolling forward.**
>
> However, since then at least 1 more issue with the actual release have surfaced, and although a fix is in progress I do want to re-open the rollback discussion. Will try to get the right minds together asap.

**Key insight:** Deployment pipeline issues **prevented rollback as an option**, forcing the team to roll forward with fixes.

---

## Deployment Timeline for Fixes

### CoreX-ALL-2.273.7 Deployment (June 23, 2:49 PM MT)

**[[Maria_Livingston|Maria Livingston]] in #ghx_incident_rm_1:**

> Hi Team, please find the release status for **CoreX-ALL-2.273.7** below:
>
> - JIRA/PR Merged: DocEnrich/MEXV-16689
> - Version Bump: Completed
> - Build: Initiated
>
> **You can track the build status via the Bamboo build pipeline:**
> 🔗 https://bmb01.ghx.com:8443/browse/EGX-CORAL-17
>
> **Bamboo deployment plan:**
> 🔗 https://bmb01.ghx.com:8443/deploy/viewDeploymentProjectEnvironments.action?id=185237507
>
> Thanks for your support today!!
>
> CC: [[Kooper_Frahm|Kooper Frahm]] [[Gregory_Bank|Gregory Bank]]

---

## Root Cause Categories

### 1. Process Issues
- Pipeline cloning during DR work and Linux upgrades
- No change management process for pipeline modifications
- Lack of documentation for pipeline state

### 2. Knowledge Management
- Pipeline changes made by offshore contractors
- US team unfamiliar with modified configuration
- Knowledge not transferred effectively

### 3. Configuration Management
- No automated validation of pipeline configs
- Region mismatches not caught until incident
- Credential management issues

### 4. Testing Gaps
- Modified pipelines not tested before production need
- No validation that rollback paths still work

---

## Leadership Visibility

### From Marten's Email to CJ/Curtis (June 22, 7:58 PM MT)

> **Current state:**
>
> We have fixes ready for issues #5 and #6 but are having issues deploying them to staging for testing. Our deployment pipelines are in a state that is unfamiliar to our US-based team and require knowledge held by Happiest Minds contractors who made recent changes to the pipelines. [[Daniel_Milburn|Daniel Milburn]] is actively working to reach the necessary resources in India (Ramya, Sujith, Vignesh) to execute the deployments.
>
> **There are definitely gaps in our incident response and deployment processes that we will need to address thoroughly in the Root Cause Analysis and retrospective following resolution.**

---

## Lessons Learned

### What Worked
- Eventually reached the right people in India
- Team persisted and found workarounds
- Used alternative pipelines when primary paths blocked

### What Didn't Work
- Pipeline modifications made without proper documentation
- No handoff process for pipeline changes
- US team couldn't operate independently during incident
- Rollback became impossible due to same pipeline issues

### Critical Questions for RCA
1. Why were pipelines cloned instead of properly versioned?
2. Who approved region configuration changes?
3. What testing was done on modified pipelines before they were needed?
4. Why was US team unaware of pipeline state?
5. What change management process should exist for pipelines?
6. How do we ensure rollback paths remain viable?

---

## Related Documents

- [[2026-06-22_Executive_Email_Thread_Complete.md]] - Executive communication during incident
- [[2026-06-22_Production_Incident_Comprehensive_Record.md]] - Full incident timeline
- [[2026-06-23_Incident_Reflection_with_Curtis.md]] - Post-incident discussion
