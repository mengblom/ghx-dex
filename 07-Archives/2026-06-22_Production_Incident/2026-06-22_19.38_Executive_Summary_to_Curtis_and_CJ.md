# Executive Summary - Production Incident
**To:** [[Curtis_Roady]] (VP Engineering), [[CJ_Singh]] (Engineering Director)  
**From:** [[Marten_Engblom]]  
**Date:** June 22, 2026, 19:38 MT  
**Incident:** CoreX-ALL 2.273.x Release - 6 Production Issues

---

Following this morning's early release (approx. 2:00 AM MT), we experienced six production issues. Here's where we stand as of 7:00 PM MT:

1. RESOLVED: EU wasn't functional after release due to missing DB users for BT connection strings
2. IN PROGRESS: MEX Orders can't load purchase details - Owned by Visibility team in India, will be picked up when they come back online. A workaround exists but is suboptimal for customers.
3. IN PROGRESS: Tracking issue causing document loops and concurrent retry failures
4. RESOLVED: GFax SFTP/SSH Algorithm Negotiation Failure - IO Release rolled back
5. FIX READY: GFax PDF Conversion Failure - Fix coded and tested, blocked on deployment pipeline *(see below)*
6. FIX READY: EML2PDF Action Word conversion failures - Fix coded and tested, blocked on deployment pipeline *(see below)*

**Customer impact:**
We have 5,200+ purchase orders undelivered via GFax as of 2:30 PM and that number continues to grow. Additionally, 1,891 invoice documents have failed due to Word-to-PDF conversion issues, and we're seeing MEX/IBR application issues impacting order visibility and processing.

Stryker and other major customers are impacted by multiple incidents simultaneously. We are providing hourly status updates as required for purchase order-impacting incidents.

**Current state:**
We have fixes ready for issues #5 and #6 but are unable to deploy them to staging for testing. Our deployment pipelines are in a state that is unfamiliar to our US-based team and require knowledge held by Happiest Minds contractors who made recent changes to the infrastructure. Daniel Milburn is actively working to reach the necessary resources in India (Ramya, Sujith, Vignesh) to execute the deployments.

There are definitely gaps in our incident response and deployment processes that we will need to address thoroughly in the Root Cause Analysis and retrospective following resolution.

**Next steps:**
1. We're trying to get a hold of the Happiest Minds DevOps resources to execute the staging deployment.
2. The goal is to deploy and test the fixes for the GFax PDF conversion and EML2PDF issues tonight.
3. Tomorrow morning when the Visibility team in India comes back online, they'll resume work on the MEX issue. We'll then deploy the tested fixes to production and begin reconciliation of failed transactions.

---

**Context:**
- Vetted with [[Daniel_Milburn]], [[Suresh_Kumar]], [[Kooper_Frahm]] before sending
- Approvals: "Looks correct" (Suresh), "Looks good to me" (Daniel)
- Sent after ~17 hours of continuous incident management
- Part of formal executive escalation protocol

**Related:**
- Full incident record: [2026-06-22_Production_Incident_Comprehensive_Record.md](2026-06-22_Production_Incident_Comprehensive_Record.md)
- Communication analysis: [2026-06-22_Incident_Leadership_Communications.md](2026-06-22_Incident_Leadership_Communications.md)
