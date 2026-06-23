# DR/BCP Team Meeting Summaries

**Date:** June 23, 2026 (morning)  
**Context:** Disaster Recovery and Business Continuity Planning check-ins  
**Note:** These meetings occurred while production incidents were still active

---

## Overview

Three product teams held DR/BCP status meetings on the morning of June 23, 2026. These summaries were posted to Slack channels by [[Pete_Ferguson|Pete Ferguson]]. The timing is notable—these meetings occurred while the team was still resolving multiple production incidents from the June 22 release.

---

## 1. GHX Fusion DR/BCP Status Check-In

**Channel:** #dr-bcp-fusion  
**Time:** 11:02 AM MT  
**Summary Author:** [[Pete_Ferguson|Pete Ferguson]]

### DR Strategy & Targets

- **Core assumption:** US East becomes completely unavailable, requiring all systems and data operational in US West within 4 hours
- **RTO:** 4 hours
- **RPO:** 2 hours
- Fusion must meet these targets to enable Exchange and downstream apps to recover within their own SLAs
- **Critical dependency:** Fusion must be operational before Exchange can function after a region switch
- All authentication, storage, and scripts should be region-agnostic by design
- Lower environment DR test planned for July/August in INT (targeted for production-like features)
- DR runbooks, playbooks, and SOPs to be stored in Confluence for audit and operational readiness

### Fusion Application Architecture & Active-Active Readiness

**Three components:**
1. **Streams** (cloud-to-cloud integration)
2. **Connect** (on-prem integrations)
3. **Gateway** (inbound API connectivity)

Each has different SLAs and integration methods (AS2, SFTP, API)

**Connect:**
- Nearly active-active
- UI is the only gap
- Making it region-switchable requires minimal effort
- Jira story to be created

**Streams:**
- Currently single-region dependent
- Has infrastructure in place for secondary region failover

**Database:**
- AWS RDS read replicas exist in secondary region
- Can be manually promoted to primary during failover
- SOPs and DevOps coverage in place

**Technical Debt:**
- Quartz job scheduler needs validation/upgrade to supported version before August
- Cost implications of running active-active compute in both regions to be projected and escalated to [[Brath_Schaufenbuel|Brath]], [[CJ_Singh|CJ]], and [[Curtis_Nielsen|Curtis]] if significant

### Connector Dependencies & Configuration

- API calls and S3 bucket configurations already region-configurable
- Managed via property files
- **Previous DR exercises limited by incomplete Corex configuration**
- All adapters and routing changes must be tested and ready across all environments before October
- Need comprehensive inventory of all endpoint connector dependencies

### In-Progress Documents During Failover

- Documents in transit during region switch will stall
- Need to be retried in new region
- Customer experience teams currently handle manual reprocessing
- Long-term goal: automate this

### Customer Communication

- StatusPage.io for outage notifications
- Managed by support or business organization, not development team
- [[Pete_Ferguson|Pete]] emphasized keeping DR procedures, runbooks, and playbooks current and accessible

### Follow-Up Items

- **[[Gregg_Anderson|Gregg Anderson]]:** Create Jira story to make Connect UI region-switchable, share with [[Ted_Powers|Ted]] for Q3 tracking
- **[[Uma|Uma]] & [[Gregg_Anderson|Gregg Anderson]]:** Validate Quartz scheduler is on supported version and not at risk before August
- **[[Uma|Uma]] & [[Gregg_Anderson|Gregg Anderson]]:** Schedule and plan lower environment DR test in INT for July/August
- **[[Uma|Uma]] & [[Gregg_Anderson|Gregg Anderson]]:** Identify and complete all required Corex tasks (adapter config, routing changes) to ensure Fusion documents process correctly in West prior to DR exercise
- **[[Uma|Uma]]:** Project estimated monthly AWS cost impact of running active-active compute for Fusion; escalate to [[Brath_Schaufenbuel|Brath]], [[CJ_Singh|CJ]], and [[Curtis_Nielsen|Curtis]] if significant
- **[[Uma|Uma]]:** Add relevant DR readiness and active-active epics to Q3 planning
- **[[Pete_Ferguson|Pete]]:** Request [[Philippe_Gravel|Philippe]] to share the Exchange Jira dashboard with [[Donald|Don]], [[Gregg_Anderson|Gregg]], and [[Uma|Uma]]
- **[[Donald|Donald]]:** Review previous action items to identify and clarify the one outstanding item dependent on another team

---

## 2. Vendormate Credentialing DR/BCP Status Check-In

**Channel:** #dr-bcp-credentialing  
**Time:** 11:01 AM MT  
**Summary Author:** [[Pete_Ferguson|Pete Ferguson]]

### DR Exercise Schedule & Participation

**Two exercises planned:**
1. Lower environment test in July/August (using INT, not staging)
2. Major production failover on **October 8th**

**October exercise details:**
- Exchange and related apps move from AWS East to AWS West
- **Switch-and-stay** (remain there for several months)
- Vendormate was first team to complete full production DR exercise last year
- Previous exercise: took app offline 4-6 hours, used internal URLs for testing to avoid customer impact, communicated proactively
- Some asynchronicity expected across teams—some will simulate outages rather than actually taking systems offline

### Technical Changes Since Last DR Exercise

**Major architecture changes:**
- Migrated to **MongoDB Atlas**
- Migrated to **Elasticsearch cloud**
- Migrated to **microservices backend**

**Impact on DR:**
- All changes will affect DR procedures
- Move to cloud-managed services eliminates manual backup/restore steps
- Should improve RTO/RPO and reduce overall downtime
- DR playbooks and runbooks need updating to reflect new architecture
- **Responsibility now sits with application team, not external vendors**
- Both staging and INT environments available for lower environment DR testing

### Dependencies & Outstanding Gaps

**Corex dependency:**
- Limited to registration and authentication only
- No inbound or outbound file transfers
- S3 bucket reconfiguration not a concern for this team

**New features:**
- New dynamic reporting feature will introduce Snowflake/CDP dependency
- Not mission-critical for credentialing
- Can be managed separately if needed

**Open items:**
- Some gaps from last year's DR exercise may still be unresolved
- [[Dhaval_Shah|Dhaval]] to review and confirm status
- Third-party integrations (e.g., Chase payment gateway) need analysis for IP whitelisting and connectivity issues post-region switch
- SSO, TPM, and other cross-application dependencies need verification

### Customer Communication Strategy

**Multi-channel approach:**
- In-app message center
- Multiple reminder emails ahead of planned downtime
- Clear outage window and instructions
- Maintenance pages deployed during DR events
- Phased re-enablement:
  1. Internal validation in new region first
  2. Maintenance page removed
  3. External customers allowed back in

**Future plans:**
- StatusPage.io being considered for organization-wide consistency
- Especially important when SSO and multiple products affected simultaneously

### Follow-Up Items

- **[[Dhaval_Shah|Dhaval Shah]] & [[Jennifer_Bettis|Jennifer Bettis]]:** Review and update DR playbook/runbook to reflect recent architectural changes
- **[[Dhaval_Shah|Dhaval Shah]]:** Confirm whether any gaps from last year's DR test remain unresolved and address as needed
- **[[Dhaval_Shah|Dhaval Shah]] & [[Balaji|Balaji]]:** Analyze all third-party integrations (e.g., Chase payment gateway) for IP whitelisting and connectivity issues after region migration
- **[[Jennifer_Bettis|Jennifer Bettis]] & [[Balaji|Balaji]]:** Coordinate with GHX on consistent customer communication tools (StatusPage.io, message center) for the October exercise

---

## 3. VASS (Value Analysis & Strategic Sourcing) DR/BCP Status Check-In

**Channel:** #dr-bcp-vass  
**Time:** 11:03 AM MT  
**Summary Author:** [[Pete_Ferguson|Pete Ferguson]]

### Application Overview

**VASS (BlueMare):**
- Web-based product supporting hospital value analysis teams
- Analytics, change management workflows, research library
- **Not a procurement platform**
- **No government clients**

**PHI considerations:**
- PHI in system includes:
  - Procedural information
  - Operating room logs
  - Physician identifiers used for clinical sourcing decisions
- Hospitals sometimes inadvertently enter PHI during onboarding
- Must be scrubbed when discovered

**Data residency requirements:**
- Contractual requirements **prohibit PHI and customer data** from being:
  - Transmitted from offshore locations
  - Stored in offshore locations
  - Viewed from offshore locations
- Applied broadly across all customers, not just specific contracts

### DR Dependencies & Data Staleness

**Dependencies:**
- Monthly data pulls from CDP
- Daily data publishing
- CCX data via PubSub model

**Impact of data loss:**
- If sources unavailable, analytics and benchmarking degrade
- **Core workflows remain functional**
- Impact is minimal unless data missing for over a month

**Historical incident:**
- 2023: Cross-functional issues caused data feed delays up to three months
- Nearly triggered financial penalties
- Resolved within days, new processes implemented

**Current architecture note:**
- Some CCX data files already stored in US West S3 buckets
- Due to inherited configuration
- Application is hosted in US East

### DR Testing History & Plans

**May DR exercise:**
- Conducted in separate AWS account
- Revealed gaps in:
  - Networking
  - Backup encryption
- To be addressed before next test

**Infrastructure:**
- VASS uses separate AWS account from Exchange
- Separate Kubernetes cluster structure
- Affects how DR tests are conducted

**Testing approach:**
- DR drills involve standing up copy of application in different cluster
- Closely mirrors production except:
  - Database size
  - S3 configuration

**Schedule:**
- Next lower environment DR test: Q3 target
- Production cutover test: Later in the year

**Documentation:**
- Playbook and runbook exist from after last incident
- Need further review and refinement before next test

### Active-Active & Cross-Region Considerations

**Data transfer volume:**
- A few terabytes per week at most
- Cost impact is negligible

**Long-term vision:**
- Active-active architecture
- Customers pinned to closest region
- Data replicated between regions
- Team agreed incremental cost is minor relative to benefits

### Customer Communication During Outages

**Tools:**
- Intercom is primary tool for customer communications during incidents
- Solution advisors maintain direct relationships with primary users
- Relay information as needed

**Contacts:**
- [[Sarah_Fox|Sarah Fox]]: Current supervisor for solution advisors
- [[Jeff_Edward|Jeff Edward]]: On [[Jonathan_Finch|Jonathan Finch's]] team, contact for technical communications during cutovers or incidents

### Follow-Up Items

- **[[Ted_Powers|Ted]]:** Reach out to [[Sarah_Fox|Sarah Fox]] for overview of customer communication process during DR exercises or outages; consult [[Jeff_Edward|Jeff Edward]] on his role during technical cutovers
- **[[Michael|Michael]]:** Coordinate with [[Seth|Seth]] to select specific date in August for next DR test
- **[[Pete_Ferguson|Pete Ferguson]], [[Trevor|Trevor]] & [[Michael|Michael]]:** Review and update DR playbook and runbook to ensure accuracy and completeness before next lower environment test

---

## Cross-Cutting Themes

### 1. October 8th Production DR Exercise
- Major multi-product exercise planned
- Exchange and related apps switching from East to West
- **Switch-and-stay model** (remain in West for months)
- Requires coordination across multiple products

### 2. Runbook/Playbook Currency
- All three teams emphasized need for updated documentation
- Recent architecture changes (cloud migrations) require documentation refresh
- Responsibility shifting from vendors to internal teams

### 3. Customer Communication
- Multiple teams considering StatusPage.io for consistency
- Important for multi-product outages
- Need coordination when SSO affects multiple apps

### 4. Active-Active Architecture
- Fusion and VASS both discussing active-active approaches
- Cost considerations being evaluated
- Benefits outweigh incremental costs

### 5. Testing Philosophy
- Lower environment tests first (July/August)
- Production tests later in year (October)
- Learning from previous exercises

---

## Context: Timing During Production Incident

**These meetings occurred on the morning of June 23, 2026, while:**
- Multiple production incidents still active from June 22 release
- Team working overnight to deploy hotfixes
- SCA reporting issue discovered overnight
- Deployment pipeline issues still being resolved

**Implications:**
- DR planning continues despite active incidents
- Different teams (DR planning vs. incident response)
- Highlights organizational capacity to handle multiple priorities
- Questions about whether October timeline realistic given current state

---

## Related Documents

- [[2026-06-22_Production_Incident_Comprehensive_Record.md]] - Context of what was happening during these meetings
- [[2026-06-23_Deployment_Pipeline_Crisis.md]] - The deployment issues discussed in executive communications
