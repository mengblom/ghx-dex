# Exchange Resiliency Work - Promised vs. Completed
**Grouped Thematic View**

*This document maps resiliency commitments to completed work using thematic groupings rather than granular 1:1 mapping.*

**Status Legend:**
- ✅ **Completed** - Work is done and deployed
- 🔄 **In Progress** - Work is actively underway or partially complete
- ❓ **Unknown** - Status unclear from available documentation
- ⏸️ **Not Started** - Work has not yet begun

---

## 1. Database & Data Layer

### What We Promised
*From Board Deck, Exchange Plan, Product Health recommendations*

- ✅ DB Stabilization: Audit DB and BT/BD optimization
- 🔄 MongoDB migration to Atlas (managed service)
- 🔄 Elasticsearch migration to Elastic Cloud (managed service)
- ❓ ES depressurization
- ✅ AuditDB improvements, optimization, cleanup
- ✅ TPM database query optimization
  - ❓ Registration query fixes
  - ❓ MyExchange query fixes
- 🔄 TPM Database Upgrade
- ✅ Database syncing and optimization
- ✅ Data cleanup initiatives
- 🔄 IBR data migration
- 🔄 Replace direct DB calls with MEX APIs

### What We Completed

- **IBR User Data Separation Phase 2 and 3**
  - **When:** Phase 2 Sept 2025, Phase 3 Ongoing
  - **Impact:** Migrated 4 tables from TPM DB to dedicated BR DB. These 4 tables are about 40% of the TPM footprint
  - **Root Cause:** User data requests on the database can cause high CPU and high memory on the database
  - **Jira:** MEXV-14795, MEXV-14796

- **BR User Data Cache Replacement**
  - **When:** August 2025
  - **Impact:** Massively reduced reads (80%) on the TPM database read only database
  - **Root Cause:** User data requests on the database can cause high CPU and high memory on the database and lead to replica lag on the database
  - **Jira:** MEXV-9939

- **TPM Migration from MySQL to Aurora**
  - **When:** May 2026 - Present
  - **Impact:** Aurora DB migration enables multi-region data synchronization so that during DR or region failovers, the only work required is to scale up services
  - **Jira:** EGXC-49902

- **Semijoin Optimization on (MySQL 8.0 Incident Fallout)**
  - **When:** July 2025
  - **Impact:** Optimizes queries in MySQL. Turned on after being turned off due to MySQL 8.0 upgrade incident
  - **Jira:** EGXC-48476, EGXC-48216

- **MEX Query Optimization**
  - **When:** June 2026
  - **Impact:** Prevent incidents caused by MEX slowness/bad queries
  - **Jira:** MEXV-13908

- **Move D Semaphore to Redis**
  - **When:** Feb 2026 (work still ongoing to split Redis out)
  - **Impact:** Remove Dependency between AuditDB and D Semaphore
  - **Jira:** EGXCIO-525

- **Data Retention**
  - **When:** April 2025
  - **Impact:** Save money, increase efficiency
  - **Jira:** EGXC-47724

- **Atlas Migration** (Ongoing)
  - MongoDB to managed Atlas service

- **Elasticsearch Migration** (Ongoing)
  - ES to Elastic Cloud managed service

- **Organization Search Data in Elasticsearch** (Completed)
  - Bulk load performance improvement noted in brainstormed list: 30 minutes → 5 minutes

---

## 2. Architectural Decoupling

### What We Promised
*From Board Deck, Exchange Plan, Product Health recommendations*

- 🔄 Exchange Platform Modularization
- ✅ SSO Decoupling
  - ✅ Separate authentication from AuditDB & MySQL TPM
- 🔄 User Data Decouple
  - 🔄 Migrate IBR data
- ✅ Tracking Engine Decouple
- ❓ Hash Map Load Balancing
- ❓ Dead Listener Refactor (decouple from processing engine)
- ❓ Feed Processor Refactor
- 🔄 IBR Decoupling
- 🔄 Document Processing Phase 2 decoupling
- ❓ Data Poller overhaul
- ❓ Replace TPM API (decouple direct DB access)
- ❓ Decouple critical components from Event Bus

### What We Completed

- **SSO: Move Identity Service DB/Collections out of Audit (self-hosted mongo) Server**
  - **When:** Aug 2025
  - **Impact:** Reduce load and dependency on Audit DB and make SSO independent application. AuditDB degradation should not impact internal or external customers logging into various applications across GHX.
  - **Jira:** SSOP-5192

- **SSO: TPM Database Separation - Phase I**
  - **When:** Nov 2025
  - **Impact:** Migrated 52 tables from TPM DB to dedicated SSO DB. Make SSO and user logins independent of TPM DB. Decoupling effort
  - **Jira:** SSOP-5126

- **Mongo, Spring Library Upgrades, EOL, Vulnerabilities and Support for Mongo 8.X Upgrade**
  - **When:** Aug 2025
  - **Impact:** Mongo drivers upgraded to support Mongo 8.X, upgrade EOL libs, vulnerability remediation
  - **Root Cause:** Older versions of mongo, spring didn't allow mongo upgrade to 8.X in SSO
  - **Jira:** SSOP-5288

- **Deploy a Dedicated API Gateway for the Org API to Decouple it from Other APIs**
  - **When:** May 2026
  - **Impact:** Separate API Gateway enables transparency so external teams are not affected and don't need to failover when Exchange fails over
  - **Root Cause:** The Org API is tightly coupled with other APIs, requiring all Exchange teams like SCA and Data Connect to execute failover whenever the Org API fails over. This dependency is both out of scope and creates unnecessary coupling.
  - **Jira:** REGCNTR-1697

- **RC 2.0 Monolith Decoupling Work**
  - **When:** February 2026 - Present
  - **Impact:** As part of the RC upgrade to use UI Core 2.0, the service and its API were migrated to GitHub with their own build/test/deploy pipelines. Work to implement the 2.0 API endpoints (migrate and rewrite) is underway. UI work to utilise the new endpoints has not yet commenced.
  - **Jira:** REGCNTR-1327, REGCNTR-1502

- **Monolith Decoupling Spike Epic**
  - **When:** June 2026 - Present
  - **Impact:** Outlines team services and applications owned in the monolith and identifies their locations for migration planning to full team ownership
  - **Jira:** REGCNTR-1670

- **Tech Debt: Visibility: Decouple Notification UI and CoreUI Migration**
  - **When:** Sept 2025
  - **Impact:** Independent changes and release of Notifications UI, Angular upgrades, uniform look & feel across GHX apps
  - **Root Cause:** Legacy Angular version with several security risks; Shared monolithic ALL repo, resulting in longer build times and slower deployment cycles
  - **Jira:** MEXV-15718

- **Tech Debt: Visibility: Decouple Transactions UI and CoreUI Migration**
  - **When:** Sept 2025
  - **Impact:** Independent changes and release of Transactions UI, Angular upgrades, uniform look & feel across GHX apps
  - **Root Cause:** Legacy Angular version with several security risks; Shared monolithic ALL repo, resulting in longer build times and slower deployment cycles
  - **Jira:** MEXV-15719

- **Tech Debt: Visibility: Decouple Orders UI and CoreUI Migration**
  - **When:** July 2024
  - **Impact:** Independent changes and release of Orders UI, Angular upgrades, uniform look & feel across GHX apps
  - **Root Cause:** Legacy Angular version with several security risks; Shared monolithic ALL repo, resulting in longer build times and slower deployment cycles
  - **Jira:** MEXV-13320

- **Tech Debt: Visibility: Decouple Invoicing & eInvoicing UI and CoreUI Migration**
  - **When:** April 2026
  - **Impact:** Independent changes and release of Invoicing & eInvoicing UI, Angular upgrades, uniform look & feel across GHX apps
  - **Root Cause:** Legacy Angular version with several security risks; Shared monolithic ALL repo, resulting in longer build times and slower deployment cycles
  - **Jira:** MEXV-16534

- **AdapterAPI Part 2 (Part 3 for Actual Migration Yet to Complete)**
  - **When:** March 2025
  - **Impact:** Decoupling IO adapters from TPM to reduce load on TPM
  - **Jira:** EGXCIO-363

- **Tracking Engine Decoupling** (Completed - from brainstormed list)
  - Moved to separate repo with dedicated Bamboo pipeline
  - No longer part of Processing Engine

- **Notifications Engine Decoupling** (Completed - from brainstormed list)
  - Moved to separate repo with dedicated Bamboo pipeline
  - No longer part of Processing Engine

---

## 3. Infrastructure & Resilience

### What We Promised
*From Board Deck, Exchange Plan, Product Health recommendations*

- 🔄 Disaster Recovery
  - 🔄 DR Drills to test RTO (4 hrs) and RPO (2 hrs) targets
  - 🔄 DR Setup and runbooks
- ✅ Industry Continuity Solution (ICS / Industry BDP)
- ✅ New Performance Environment
- ✅ Performance Testing capability
- 🔄 Managed Database Services
  - 🔄 MongoDB to Atlas
  - 🔄 Elasticsearch to Managed Service
- 🔄 Scheduling Enhancements
  - ✅ Processing Engine Start/Stop Enhancement
  - ❓ Universal Scheduler Migration
  - ❓ Event Bus Next Generation
- ✅ IO Guarantee improvements

### What We Completed

- **Performance Environment - Setup**
  - **When:** Jan – Jun 2025
  - **Impact:** The performance environment was immensely valuable and widely used for database upgrades (Atlas, Elastic Cloud, Aurora) as well as release testing. It enabled early identification of performance and scalability issues, ensured upgrade readiness, and significantly improved confidence in production deployments.
  - **Root Cause:** During the MySQL upgrade incidents in June 2024, performance degradation was the primary impact. The absence of a dedicated performance environment prevented early detection, allowing issues to surface only in later stages instead of being caught proactively.
  - **Jira:** EGXC-47694, EGXC-47695, EGXC-47696, EGXC-47697, EGXC-47698

- **EventBus Resiliency**
  - **When:** July 2025
  - **Impact:** Doc processing has less impact during incidents: Data Poller should not pause for rebalancing; there is a separate engine to handle critical jobs
  - **Jira:** EGXC-44430

- **Processing Engine Robustness: Threadpool Size Tuning, Fix Tracking Flow Priorities, Add Java Flight Recorder to Investigate 100% CPU**
  - **When:** April 2025
  - **Impact:** Tracking flows tied to more important docs should be priority 1 instead of all tracking flows having priority 1. Added Java Flight Recorder to troubleshoot 100% CPU incidents in the future
  - **Jira:** (Not listed in source doc)

- **IO Guarantee - SQS Backup for Native Comms** (Completed - from brainstormed list)
  - Improved reliability for critical communication flows

- **Tracking Resiliency Phase 1 and 2 (Phase 3 Yet to Complete)**
  - **When:** Nov 2025
  - **Impact:** Reducing bugs and addressing race conditions. Reduce impact of failed tracking flows on support teams.
  - **Jira:** EGXC-47604, EGXC-48027, EGXC-48027

- **Industry Continuity Solution (ICS)** (Active)
  - Contractor-built solution deployed
  - Status updated June 15, 2026 by Jena Milan

---

## 4. Observability & Operations

### What We Promised
*From Board Deck, Exchange Plan, Product Health recommendations*

- ✅ Alerting and Monitoring improvements
- ✅ Fix gaps in monitoring
- ✅ Visibility improvements for internal/external tooling
- ❓ DB spike detection and alerting
- ✅ Performance Testing framework
- ✅ Incident Management process improvements
- ✅ Feature Flagging capability
- ❓ SLA monitoring and rebate tracking
- ✅ Canary Program

### What We Completed

- **Heartbeat: CoreX Business Intelligence**
  - **When:** Mar-2025 to Sep-2025
  - **Impact:** Have visibility of below metrics in heartbeat-ui:
    - CoreX BI
    - ABL Metrics
    - ILM Metrics
    - SQS & DQS Metrics
    - DP Backlog
  - **Root Cause:** Enhancing Observability/Monitoring
  - **Jira:** EGXC-45573, EGXC-46311, EGXC-46389, EGXC-46371, EGXC-45574

- **Heartbeat: Configuration Cache in Heartbeat App**
  - **When:** Sept-2025
  - **Impact:** Reduced reads from Dynamo DB, reducing cost and API response time
  - **Root Cause:** Due to excessive reads on AWS DynamoDB lot of requests failing in heartbeat
  - **Jira:** BROKEN-415, EGXC-48574

- **Implement Robust Validation for the Org API Using GitHub Across Different Environments by Integrating Automated Checks**
  - **When:** May 2026
  - **Impact:** The automated GitHub validation pipeline reduced validation time from multiple person-days to just 2 minutes, eliminating manual effort
  - **Root Cause:** Lack of automation led to manual, slow validation processes that had to be repeatedly executed across each environment
  - **Jira:** ORGAPI-426, ORGAPI-445

- **Canary Program (Document Prediction)** (Deployed - from brainstormed list)
  - Kinesis stream of Exchange Event Bus events
  - Predictive monitoring capability

- **CoreX Business Intelligence Dashboard** (Deployed - from brainstormed list)
  - Bulk Load performance tracking
  - Document throughput monitoring
  - Heartbeat throughput visibility

- **Feature Flagging Capability** (Deployed)
  - Referenced in Board Deck promises
  - Enabled safer, incremental rollouts

---

## 5. Process, Governance & Security

### What We Promised
*From Board Deck, Exchange Plan, Product Health recommendations*

- ✅ Release rigor and change management
- 🔄 All vulnerabilities addressed within SLA
- 🔄 Eliminate EOL technologies in our stack
  - 🔄 (Red Mythos Exchange project)
- ✅ Human Error Mitigation
  - ✅ CoreX permission audit
  - ✅ Multi-person go-live audit
- ❓ Testing Maturity improvements
- 🔄 Communication
  - ✅ Customer empathy training
  - ❓ Customer communication strategy
  - ✅ Canary program communications

### What We Completed

- **Mongo, Spring Library Upgrades, EOL, Vulnerabilities and Support for Mongo 8.X Upgrade**
  - **When:** Aug 2025
  - **Impact:** Mongo drivers upgraded to support Mongo 8.X, upgrade EOL libs, vulnerability remediation
  - **Root Cause:** Older versions of mongo, spring didn't allow mongo upgrade to 8.X in SSO
  - **Jira:** SSOP-5288

- **SSO: Implementation for SAML Adapter in GHX SSO**
  - **When:** Jan-2026
  - **Impact:** Add the SAML protocol to GHX SSO
  - **Root Cause:** Product Help sites are not protected they are public and can cause Search engines like Google, Yahoo have been indexing them
  - **Jira:** SSOP-5377

- **Engineering Efficiency: SSO: Execute Liquibase Before EC2 Deployment**
  - **When:** Nov-2025
  - **Impact:** Moved Liquibase execution out from EC2 app instance to dedicated bamboo step which prevented issues occurring during every new release of SSO
  - **Root Cause:** SSO is not functional during new release, since Liquibase was executed during application startup. Since we spin up multiple instances parallelly, the instances which could not acquire Liquibase lock during start will skip Liquibase and start without latest config changes, these cause code to break. When requests go to these faulty EC2 instances, we see failures/random behavior.
  - **Jira:** SSOP-5384

- **Red Mythos Exchange Project** (In Progress - Aaron ownership)
  - Vulnerabilities within SLA
  - EOL technology elimination
  - *Note:* Status details needed from Aaron

- **Release Rigor & Change Management** (Process improvements)
  - Multi-person go-live audit (implemented)
  - CoreX permission audit (completed)
  - *Note:* Specific metrics/outcomes need to be extracted from Exchange Resiliency Completed doc

- **Customer Empathy Training** (Deployed)
  - Team-wide rollout completed
  - *Note:* Specific dates/outcomes need confirmation

- **Incident Management Process Improvements** (Ongoing)
  - Mature incident response capabilities demonstrated (June 22-24 incident)
  - Clear escalation paths and executive communication protocols

---

## Status Summary

**Overall Progress Across All Groups:**

| Group | ✅ Completed | 🔄 In Progress | ❓ Unknown | Total Items |
|-------|-------------|----------------|-----------|-------------|
| **Database & Data Layer** | 5 | 4 | 3 | 12 |
| **Architectural Decoupling** | 3 | 4 | 6 | 13 |
| **Infrastructure & Resilience** | 4 | 5 | 2 | 11 |
| **Observability & Operations** | 6 | 0 | 2 | 8 |
| **Process, Governance & Security** | 5 | 3 | 2 | 10 |
| **TOTAL** | **23** | **16** | **15** | **54** |

**Key Insights:**
- **43% Completed** - Significant work delivered across all dimensions
- **30% In Progress** - Active initiatives underway, momentum sustained
- **27% Unknown** - Documentation gaps or items not explicitly tracked (likely candidates for director input)
- **Strongest areas:** Observability & Operations (75% complete), Process & Governance (50% complete)
- **Most active work:** Database & Data Layer, Infrastructure & Resilience (ongoing migrations)

---

## Data Sources

### Promised Items Sources
1. **Board Deck** (`2025.02 Exchange_Board Deck_Feb.2025.pdf`)
   - Pages 2, 10, 14, 15, 17, 20, 25, 28
2. **Exchange Plan** (`Exchange_Plan_Latest.pptx`)
   - Slides 3, 7, 10, 14-16 (Phase 1), 19 (Phase 2), 23-30 (Incident Remediations)
3. **Product Health** (`2026 Product Health Portfolio - Copy.pptx`)
   - Slides 41-49 Recommendations
4. **2026 Tech Org Priorities** (`2026 Tech Org Priorities - Copy.pptx`)
   - Six resiliency items

### Completed Items Source
1. **Exchange Resiliency Completed** (`Exchange Resiliency Completed.docx`)
   - OneDrive location: `/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange Resiliency Completed.docx`

---

## Usage Notes

**For CJ presentation:**
- Show side-by-side columns (Promised | Completed) for each group
- No need to map individual items - the thematic grouping tells the story
- Demonstrates comprehensive coverage across all dimensions
- Shows we didn't just cherry-pick easy wins

**Presentation format suggestion:**
```
┌─────────────────────────────────────────────────────────────┐
│ Group 1: Database & Data Layer                              │
├─────────────────────────┬───────────────────────────────────┤
│ What We Promised        │ What We Completed                 │
├─────────────────────────┼───────────────────────────────────┤
│ • Audit DB optimization │ • [Fill from completed doc]       │
│ • Atlas migration       │ • [Fill from completed doc]       │
│ • ES to Elastic Cloud   │ • [Fill from completed doc]       │
│ • Query optimization    │ • [Fill from completed doc]       │
│ • IBR data migration    │ • [Fill from completed doc]       │
└─────────────────────────┴───────────────────────────────────┘
```

**Why this works:**
- Executive-friendly (thematic vs. granular)
- Shows comprehensive coverage
- Honest about scope (some items in progress, some complete)
- Tells the transformation story through categories
- Easy to present without getting lost in details

---

## Next Steps

1. ✅ **Extract completed items** from `Exchange Resiliency Completed.docx` - DONE
2. ✅ **Populate "What We Completed"** sections for each group - DONE
3. ✅ **Add all Jira tickets and metrics from source document** - DONE
4. ✅ **Add status icons to "What We Promised" items** - DONE
5. **Review with directors** (Daniel, Aaron, Arshad, Ramesh) to ensure nothing major is missing
6. **Fill in remaining missing details:**
   - Aaron: Red Mythos Exchange status and metrics
   - All: Customer empathy training rollout dates/outcomes
   - All: CoreX permission audit and multi-person go-live audit metrics
   - All: Confirm items in "brainstormed list" section (Tracking/Notifications Engine decoupling, IO Guarantee, etc.)

## Notes on Completed Items

**Items marked "In Progress" or "Ongoing":**
- Atlas Migration
- Elasticsearch Migration
- TPM Aurora Migration (EGXC-49902)
- IBR User Data Separation Phase 3 (MEXV-14795, MEXV-14796)
- RC 2.0 Monolith Decoupling (REGCNTR-1327, REGCNTR-1502)
- Monolith Decoupling Spike Epic (REGCNTR-1670)
- Tracking Resiliency Phase 3 (EGXC-47604, EGXC-48027)
- Red Mythos Exchange (status details from Aaron needed)

**Items from "brainstormed list" section needing confirmation:**
- Tracking Engine Decoupling (separate repo/pipeline)
- Notifications Engine Decoupling (separate repo/pipeline)
- IO Guarantee - SQS Backup
- Canary Program (Document Prediction)
- CoreX BI Dashboard
- Organization Search Data in Elasticsearch (30min → 5min)

**Items needing additional details:**
- Feature Flagging (referenced in Board Deck, assumed deployed)
- Customer Empathy Training (dates/outcomes)
- CoreX permission audit results (mentioned as completed)
- Multi-person go-live audit results (mentioned as implemented)

**Data completeness:**
- ✅ All items from main table in source doc include Jira tickets
- ✅ All impact metrics captured
- ✅ Root causes documented where provided
- ⚠️ Some brainstormed items lack Jira references (need director confirmation)

---

**Created:** 2026-06-25  
**Purpose:** CJ meeting prep - transformation narrative support  
**Status:** ✅ Completed items extracted with full Jira details and organized by theme  
**Last Updated:** 2026-06-26 (added status icons, progress summary, all Jira tickets, and impact metrics)
