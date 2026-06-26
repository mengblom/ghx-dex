# Email to GLT/SLT - Incident Status & Path Forward

**Status:** SENT  
**Author:** Marten Engblom  
**Date:** June 24, 2026  
**Recipients:** GLT/SLT Group  
**Per directive from:** CJ Singh

---

## Email Draft

**Subject:** Exchange Incident Update - Status & Path Forward

**To:** GLT/SLT  
**Cc:** CJ Singh, Ramesh Donnipadu, Arshad Mahammad

---

Hi team,

Following up on this morning's AS2 rollback and the broader incident from June 22-24. Here's where we stand and the path forward.

**Summary - Current State and Impact**

We're in a **stable state** with **minimal customer and internal impact** at this point:
- **6/7 issues** with Monday's release have been resolved (GFax processing normally, MEX/IBR operational). 
- **1 issue remains open:** email-to-PDF conversion (see below)
- Internally, the data correction scripts completed this morning, which remediated the remaining internal impact to downstream systems (CDP and Analytics data etc.). 
- The AS2 issue from this morning (4:36-7:14 AM MT) was resolved via rollback. 
- **All customer-facing systems are operational**

**Remaining Issue**

One incident remains open: the email-to-PDF conversion. We had a hotfix ready but rolled it back this morning when it impacted AS2 flows due to an unrelated eInvoicing library change that got bundled with it. The hotfix **did address the target issue successfully** before we rolled it back.

**Current Plan**

We're planning to re-deploy the hot fix with the problematic eInvoicing changes removed - the tentative timeframe is **tomorrow Thursday**. This will be our **last deployment**, and we will be in a **stable state going into the quiet period** that starts Monday for the July 4th holiday. Given that context, we're being especially careful to make sure we go into the freeze in a solid state.

**Friday** we will start a thorough root cause analysis with the full team. We'll cover both this incident and the **broader GFax reliability concerns** that have come up over the last several weeks. 

**Some Observations**

Without jumping the gun and foregoing the RCA, there are a few things I already anticipate will be central to the analysis:

1. We need to **react quicker to issues that are customer impacting**, particularly POs. I am gleaning that we (Engineering) are overly reliant on Customer Experience to advise us on level of impact etc. I am anticipating that we determine that we **should have rolled back the original release** as soon as the impact to customers and POs was known.
2. Already a known fact, but our **monolithic architecture and monolithic operational processes prevents us from deploying surgical fixes** - changes sometimes have unpredictable side effects "far away", which is what happened with the AS2 issue this morning.
3. We have **complexities on the DevOps** side that are making the mechanics of releasing, testing, rolling back etc. more difficult than it should be and lead to several delays and mistakes in the process. There are in-place improvements to make, but ultimately the answer here are **autonomous teams** that own, maintain and operate their own release pipelines. 
4. While we do **rollback testing**, it seems we have gaps here, especially when a new release alters data in a way that is not compatible with the previous release.
5. And then of course there are going to be some l**earnings with respect to the actual bugs in the release**: drift between lower environments and Production due to the mid-stream Atlas migrations, connection string configuration issues, library dependency conflicts, misses in testing, etc.


If anything changes with this plan, I'll let you know immediately. Otherwise, expect an update from me **end of day Monday** with a status of the RCA.

Thanks,  
Marten

PS. Rammi, I wanted to review this with you, but forgot that your are EST. Any feedback is appreciated.

---

## Review Notes

**Before sending:**
- [ ] Review with Ramesh Donnipadu
- [ ] Align on messaging and tone
- [ ] Confirm target deployment date for Email-to-PDF hotfix (or confirm "TBD pending consultation")
- [ ] Verify accuracy of customer impact numbers
- [ ] Confirm RCA schedule (Friday/Monday) doesn't conflict with other priorities

**CJ's Key Messaging Principles:**
- ✅ Be very precise about current customer impact (minimal, specific details)
- ✅ Clear about internal impact (minimal)
- ✅ Status of closed vs open incidents
- ✅ Plan for open incident (measured approach, specific or pending date)
- ✅ Last deployment before freeze (build confidence)
- ✅ Confirm stable state entering freeze
- ✅ RCA scope and timeline (Friday/Monday, publish EOD Monday)
- ✅ Foreshadow material findings (show we understand what happened)
- ✅ Clear close (expect update EOD Monday, will notify if changes)

---

## Related Documents

- [CJ/Arshad Meeting Summary](2026-06-24_CJ_Arshad_RCA_Planning_Meeting.md) - Context for this email
- [TIMELINE.md](TIMELINE.md) - Full incident chronology
- [Comprehensive Record](2026-06-22_Production_Incident_Comprehensive_Record.md) - Initial root cause analysis

---

**Document Status:** SENT  
**Created:** June 24, 2026  
**Sent:** June 24, 2026
