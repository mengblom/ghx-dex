# Exchange Resiliency Work Originally Identified
## Comprehensive List with References to Source Documents

**Reference Documents:**
- **[Board Deck]**: 2025.02 Exchange_Board Deck_Feb.2025.pdf
- **[Exchange Plan]**: Exchange_Plan_Latest.pptx  
- **[Product Health]**: 2026 Product Health Portfolio - Copy.pptx (slides 41-49)

---

## PRIORITY 1: DATABASE STABILIZATION

### AuditDB Stabilization
**References:** 
- [Exchange Plan] Slide 10: "Exchange Database Stabilization"
- [Exchange Plan] Slide 11: "Exchange Database Contention Incident Tracking"
- [Board Deck] Slide 5: "Exchange Incident Identified Root Causes" - shows database issues as major root cause

**Stabilization Outcomes Identified:**
- Write ticket exhaustion near zero
- 30% request activity reduction
- Approximately 35% AuditDb data footprint reduction
- Unrelated collections migration (7%)

**Expected Long-Term Impact:**
- Sustained stability and performance efficiency
- Lower maintenance overhead and reduced resource consumption
- Minimized risk of cascading failures due to improved isolation

---

### BT/BD Database Stabilization
**References:**
- [Exchange Plan] Slide 10: "Exchange Database Stabilization"
- [Exchange Plan] Slide 11: "Exchange Database Contention Incident Tracking"
- [Board Deck] Slide 5: Shows BT database-related incidents increased 1→4 in January

**Stabilization Outcomes Identified:**
- Write ticket exhaustion stabilized
- 20% index reduction for BT, 50% reduction for BD
- Decreased total index size by ~40GB
- Feed Processor concurrency reduced by 50%

**Expected Long-Term Impact:**
- Improved query efficiency and reduced database contention
- Lower CPU/memory usage, enhancing overall system throughput
- Optimized concurrency management, minimizing processing delays

---

### Database Managed Services Initiative (MongoDB Atlas Migration)
**References:**
- [Exchange Plan] Slide 12: "Exchange Database Managed Services Initiative"

**Current State Problems Identified:**
- Manual scaling, security, and tuning create high overhead
- Over-provisioned to compensate for inefficiencies
- Manual failover, no automated backups, self-managed maintenance increase downtime risks
- Manual security setup, no built-in compliance, delayed patching create vulnerabilities
- Manual scaling and provisioning lead to inefficiencies and resource constraints
- High KTLO burden, fragmented monitoring, no native performance advisory

**Future State Benefits (MongoDB Atlas):**
- **Cost & Efficiency**: 12% cost savings via automation, optimized infrastructure management, reduced DBA workload
- **Reliability & Uptime**: 99.995% uptime, automated failover, managed updates, proactive monitoring reduce outages
- **Security & Compliance**: Automated security & compliance (SOC 2, ISO 27001, HIPAA, GDPR) with built-in encryption & authentication
- **Scalability & Flexibility**: On-demand automated scaling, multi-cloud & serverless options, data tiering improve performance
- **Long-Term Vision**: Managed-first strategy reduces KTLO, enables centralized monitoring, optimizes query performance

**Key Business Drivers:**
- Streamline operations
- Enhance scalability
- Strengthen security
- Reduce maintenance overhead

---

## PRIORITY 2: INCREASE RIGOR IN RELEASE MANAGEMENT

### Release Management Process Improvements
**References:**
- [Exchange Plan] Slide 14: "Release Management"
- [Board Deck] Slide 2: "Increased rigor in change management and release management processes have had a significant impact in reducing incidents due to changes/releases"

**Key Takeaways:**
1. Since implementing these changes, zero release-related incidents post-October 2024
2. Continue to deliver business value by alternating between Functional and Resiliency releases

**Focus Areas & Implementation Details:**

#### Feature Flagging & Rollback Testing
- All stories now require feature flags; if not feasible, rollback testing is mandatory

#### Risk-Based Release Decisions
For each release, a risk metrics framework evaluates:
- **Database Impact**: Quantify the increase in load on the database
- **Code Change Complexity**: Quantify the number and scope of code changes across components
- **Testing Coverage**: Quantify unit and regression test coverage
- **Release Bundling**: Qualify the impact of bundling different components in same release

#### Testing Strategy
- Depending on the release, perform load, automation and regression in STG environment

#### Cross Functional Communication
- A new communication path provides business leaders with visibility into upcoming releases

---

### Q1 2025 Release Plan
**References:**
- [Exchange Plan] Slide 15: "Q1 2025 Release Plan Summary"

**All releases include:**
- Completed Resiliency features
- Mix of Product release backlog with current Q1 features

#### 02/06 Release - DEPLOYED
**Category:** Product & Platform
- EU Exchange gaps and Peppol Reporting
- MEX, Reg Center, and CCX performance
- Bulk Upload enhancements for TPM and Reg Center
- Intelligent Business Rules supporting split orders and consignment enrichment
- Database and ILM strategies
- Increase automated test coverage (AT)

**Value:**
- Maintains EU compliance for Exchange, Peppol, transformation
- User experience for G-Fax, IPA, and einvoicing
- IBR support for consignment processing
- Database ILM strategies to continuously improve platform and application performance

#### Early March Release - PENDING
**Category:** Resiliency Roadmap Managed Svc eInvoicing Regulatory
- Database and Query Optimization
- Visibility Improvements for Internal/External tooling
- Document tracking for MS Agents
- Document Status consistency increased test coverage
- EU Peppol requirements for reporting and NL Support

**Value:**
- Incident Risk Reduction, Improves usability and reduces DB risk
- User experience for G-Fax, IPA, and internal monitoring
- Visibility for consignment order type processing
- Customer sees valid invoice status across all applications
- Regulatory and certification requirements to support the EU business

#### Late March Release - PENDING
**Category:** Resiliency Roadmap KLO Managed Svc eInvoicing
- IBR decoupling, query optimization, API tuning
- IBR backlog, validation and splitting
- Heartbeat and metric alerting
- Contact Management updates for accuracy and performance

**Value:**
- Incident Risk Reduction, Improves usability and reduces DB risk
- IBR supports order splitting and increased Bill Only use cases
- Understand baselines for next areas of optimization
- Customer communications are accurate and to the right user

#### Mid April Release - PENDING
**Category:** Resiliency Roadmap KLO
- Database syncing, and database optimization
- G-Fax enhancements for Account validation
- IBR support for multiple order splitting

**Value:**
- Customer visibility and user experience improvements
- Final G-Fax account management for US and initial EU testing increasing accuracy of ShipTo/SoldTo AI/ML process

---

## PRIORITY 3: CREATE HIGHER FIDELITY PERFORMANCE ENVIRONMENTS

### Performance Environment
**References:**
- [Exchange Plan] Slide 17: "Performance Environment"

**Composition:**
- Infrastructure is like Production, except for data retention policy and replications
- Setup in AWS-West region
- Excludes ingress/egress components & customer connections

**How does it differ from current load test:**
- 60% more variability in load tests
- A 360% increase in document volume testing
- 60% backend job coverage, 20% UI load testing coverage
- Overall, 60% more coverage from existing load test setup

**Why is it essential:**
- Required for infrastructure updates, system decoupling, refactoring, and major releases
- Not needed for day-to-day releases

**Progress:**
- On track to finish phase 1 scope by April 15 in partnership with third-party testing experts (Cigniti) introduced by the Warburg team
- Env is stood up in the AWS West region to act as DR env down the line
- The basic infrastructure deployment is 40% complete, and the app deployment is 60% complete
- Cigniti has automated 6/11 test cases, and document replay coding is 20% complete

**Key Takeaways:**
1. Despite being in its early stages, the perf environment is proving valuable for validating database changes before release
2. Perf environment moves us closer to Disaster Recovery readiness by automating deployments
3. Some of the modularization work is dependent on Perf environment being ready

---

## OTHER PRIORITIES

### Modularization Initiative
**References:**
- [Exchange Plan] Slide 20: "Exchange Platform Modularization Initiative"

**Description:** Strategic initiative to decouple tightly integrated components, enabling independent scaling, improved maintainability, and reduced system dependencies.

**Key Takeaways:**
1. **IBR Caching Layer and Tracking Engine Decoupling** are nearing production readiness, with successful testing in lower environments and upcoming regression testing
2. **SSO, User Data, and Adapter API** are progressing steadily, with foundational work in place to support future decoupling and performance improvements
3. **On Deck**: Finalizing deployments, conducting extensive testing, and optimizing operational workflows to ensure seamless transitions and long-term system resiliency

**Workstreams and Progress:**

| Workstream | Description | Progress |
|------------|-------------|----------|
| **SSO Decouple** | Separating authentication from AuditDB & MySQL TPM | 🔴 (nearing production) |
| **User Data Decouple** | Migrating IBR data to improve resiliency | 🔴 |
| **Cache Layer** | Code complete, pending regression testing | 🔴 |
| **Phase 2 Data Separation** | Backend and libraries refactored | 🟠 |
| **IO Guarantee** | Ensuring Exchange can accept documents during failures | 🟠 |
| **Phase 2 Adapter API** | Decoupling Adapter API from MySQL TPM | 🟠 |
| **Tracking Engine Decouple** | Separating tracking from document processing | 🔴 |
| **TPM Query Optimization** | Moving TPM reads to ElasticSearch | 🟠 |

Legend: 🔴 = nearing production/code complete, 🟠 = in progress

---

### Incident Management and Problem Management Maturity (Improving MTTR)
**References:**
- [Exchange Plan] Slide 22: "Key findings from AKF workshop on incident management"
- [Board Deck] Slide 2: "Review of the incident and problem management processes (to help respond to incidents and learn from them better) with a top-tier third party (AKF Partners) completed and recommendations initiated"

**AKF Partners Workshop - Key Findings:**

| Observation | Recommendation | When |
|-------------|----------------|------|
| Severity levels are inconsistent across products | • Define severity levels with clear differentiation based on customer business impact<br>• Tie definitions to business impact | • Started<br>• Q1 |
| Inconsistent process for working an incident | • Map select Sev1 incidents from initiation to resolution<br>• Identify inputs/outputs and skillsets required<br>• Eliminate and automate low-level tasks | • Not Started<br>• Q1-Q2 |
| Problems not distinguished from Incidents | • Separate discussion of problems from incidents<br>• Make sure problems are represented in backlogs<br>• Associate problems with incidents to spotlight ongoing impact assessment | • Started<br>• Q1 |

---

### Industry BCP Initiative
**References:**
- [Exchange Plan] Slide 24: "Industry Business Continuity Planning"
- [Exchange Plan] Slide 25: "Industry BCP: Key Milestones and Next Steps"

**Description:** A collaborative industry initiative focused on strengthening resilience to ensure that critical supply chain operations can continue seamlessly, even in the face of significant incidents, thus protecting patient care and maintaining service reliability.

**Key Takeaways:**
1. **Customers are focused on BCP with GHX as priority**
2. **Communication transparency is critical to customer operations**
3. **BCP Activation timing and requirements vary by customer and region**
4. **Preliminary models validated and reaching a static point**

**Focus Areas & Implementation Details:**

#### GHX Continuity Plan
- Customers need and expect collaborative BCP with GHX Exchange if a prolonged outage occurs, and GHX DR strategy fails
- **Incident Communications**: Evolve incident communications to be more relevant and action focused for the customer
- **Alternate Delivery Paths**: Establish alternate data delivery methods with minimal GHX processing
- **Business Priority**: Priority to Distributor and Critical Care orders
- **Reconciliation/Recovery**: Reduce risk of duplicate orders post recovery

#### Customer Events
- **Provider Event**: Multiphase requirements based on duration and impact/type of event
- **Supplier Event**: Multiphase requirements based on duration and impact/type of event – requires delineation of specific aspects of supplier operations

**Product Discovery:** 16 Product Discovery meetings completed (6 providers, 8 suppliers, 2 distributors)
- Product Requirements to be completed by the end of Q1

**Key Milestones:**

| Milestone | Recommendation | When |
|-----------|----------------|------|
| Finalize GHX Alternate Light-Weight Solution (v0.5) | • Requirements completed<br>• Architecture reviewed and committed<br>• Capacity plan/Commitment for Q2 execution | • In Progress<br>• Target: March 30 |
| Customer Tabletop Exercise | • Virtual session with select CAB members representing providers, distributors, suppliers<br>• Validate models, run use case exercises | • In Progress<br>• Week of April 14 |
| Draft and Execute Runbooks | • Next Version of internal GHX Runbooks for GHX, hospital and Supplier outages<br>• Collaborate on customer BCP for GHX | • Not Started<br>• Q2 |
| Finalize Customer specific BCP and mutual playbooks | • Continue customer engagement and deep dive collaboration meetings by customer segment<br>• Business Case for investment models (Q2)<br>• 3 Customers collaborated on mutual playbook | • In Progress<br>• Q2-Q4 |

---

### Industry BCP Priority Drivers and Timelines
**References:**
- [Exchange Plan] Slide 34: "Industry BCP Priority Drivers and Timelines"

**Description:** Hospitals must prioritize and manage more than just order processing in system or service disruptions

**Time Segment Priority to Remediate:** 1-10 (representing increasing urgency/timeline)

| Function | Priority Timeline |
|----------|-------------------|
| **Order Management** | Time segments 1-5 |
| - Primary Distributors: Critical Care products | Segments 1-3 |
| - Primary Distributors: Elective Procedure Products | Segments 3-5 |
| - Purchasing Enablement (MP) | Segments 3-5 |
| **Inventory Management** | Time segments 2-5 |
| - Shipment Visibility (ASN) | Segments 2-5 |
| **Cash Management** | Time segments 3-10 |
| - Invoice Delivery | Segments 3-5 |
| - Price Accuracy | Segments 5-8 |
| - Payment | Segments 8-10 |
| **Recovery & Reconciliation** | Time segments 8-10 |

**Note:** Created with output from voice of customer interviews conducted September and January 2025

---

### v0.5 Business Continuity – GHX Event
**References:**
- [Exchange Plan] Slide 35: "v0.5 Business Continuity – GHX Event"

**Priority to critical O2C/P2P – Customer Connectivity Backup/Alternate Path**

**Solution Components:**
- **Order Replay**: "Replay" orders from previous week on behalf of hospital (Can be production)
- **Web Front End**: Marketplace w/ PO workflow, Catalog list w/ acc. Pricing
- **Doc Processing**: ShipTo/BillTo Account Management, Intelligent Business Rules, Mapping Services
- **Visibility**: Single Sign On or Alternate ID, Orders, Business Rules workflow, Transactions
- **Cash/Revenue Management**: Price validation, Invoice Presentment

**Implementation:**
1. Available within GHX Production Systems
2. Publish "Run-book" for cyber preparedness and table top testing
3. Jointly execute "Run-book" upon event

---

### Business Continuity – Alternate path, minimal integration
**References:**
- [Exchange Plan] Slide 36: "Business Continuity – Alternate path, minimal integration"

**Priority to critical O2C/P2P – Connectivity Not Available / Customer Cyber Event**

**Solution Components:**
- **Order Replay**: "Replay" orders from previous week on behalf of hospital, Can be production
- **Web Front End**: Marketplace w/ PO workflow, Catalog list w/ acc. Pricing
- **Doc Processing**: ShipTo/BillTo Account Management, Intelligent Business Rules, Mapping Services
- **Visibility (WebDirect Portal)**: Single Sign On or Alternate ID, Orders, Business Rules workflow, Transactions
- **Cash/Revenue Management**: Price validation, Invoice Presentment

**Key Features:**
1. GHX Production Systems – No impact to Sellers
2. Air-Gap: Infrastructure isolated from current cloud based infrastructure

---

### GHX DR and BCP Maturity
**References:**
- [Exchange Plan] Slide 27: "Continuity Planning Assessment"
- [Exchange Plan] Slide 28: "Disaster Recovery Approach"

**Continuity Planning Assessment** (as of presentation date):

| Company Product | % of ARR | BCP | BCP Testing | Contacts & Comm. Plans |
|----------------|----------|-----|-------------|------------------------|
| Corporate IT | N/A | Yellow | Red | Orange |
| **Exchange** | **44%** | **Red** | **Red** | **Orange** |
| Vendormate | 20% | Yellow | Red | Orange |
| ePay | 10% | Yellow | Yellow | Orange |
| PIM / PLA / CO | 6% | Yellow | Red | Orange |
| Marketplace | 5% | Yellow | Red | Orange |
| Nuvia | 3% | Yellow | Red | Orange |
| CCX | 2% | Yellow | Red | Orange |

**Key Issues Identified for Exchange:**
- BCP & communication plans largely not in place and formal testing has not been conducted

**Disaster Recovery Planning Assessment:**

| Company Product | DRP in place | RTO | RPO | DR Testing | Redundancy |
|----------------|--------------|-----|-----|------------|------------|
| **Exchange** | **Red** | **Red** | **Red** | **Red** | **Yellow** |
| Vendormate | Red | Red | Red | Red | Yellow |
| ePay | Red | Red | Red | Red | Yellow |
| [other products similar patterns] |

**Key Issues Identified for Exchange:**
- Informal or incomplete plans exist for most products but need updates or to be completed
- Following updates/completion, these plans need to be fully tested by product
- RTO/RPO targets are largely aspirational vs. tested

**Backup Strategy Assessment:**

| Company Product | Backup Immutability | Backup Location | Backup Frequency | Backup Encryption | Backup Access Controls |
|----------------|---------------------|-----------------|------------------|-------------------|----------------------|
| **Exchange** | **Red** | **Red** | **Green** | **Green** | **Green** |

**Key Issues Identified for Exchange:**
- No immutability in place and current backup location (same AWS account, but cross-region) is insufficient

---

### Disaster Recovery Approach
**References:**
- [Exchange Plan] Slide 28: "Disaster Recovery Approach"

**To mature our disaster recovery competence in the event of an emergency**

**Key Takeaways:**
1. **Contracting just completed. Kickoff next week.**
2. **First product will be Credential manager (20% of ARR)** to work out process and plans
3. **DR Plans will consist of current state of technology and what it takes to restore today**
4. **A follow-on step will be to evaluate the business value of improving the RTO and RPO**
5. **Immutable backups have started.**

**Focus Areas & Implementation Details:**

| Focus Area | Implementation Details |
|------------|------------------------|
| **Business Continuity Plan** | Write BCP for engineering as a whole. Each product will have a DR plan that relates to the company BCP |
| **Business Impact Analysis** | Analyze the products for key processes and dependencies. Set desired RTO and RPO |
| **Business Continuity Plan Testing** | Test the BCP with tabletop exercises |
| **Disaster Recovery Plan** | Write the plan for restoring our existing services today. Include step by step instructions to follow in an emergency |
| **Disaster Recovery Plan Testing** | Test the written plan by restoring services in a 2nd region. Measure the actual RTO/RPO of the test |
| **Disaster Recovery improvement** | Decide business value of improving the RTO/RPO and automating and set plans to make this |
| **Backup Immutability** | Expand existing backup strategy to enable immutable backups. Instrument backups based on DR plan and BIA |

---

## INCIDENT ROOT CAUSE ANALYSIS

### Exchange Incident Identified Root Causes (Oct 2024 - Jan 2025)
**References:**
- [Board Deck] Slide 5: "Exchange Incident Identified Root Causes"

**October 2024 (10 Incidents)**

Top 3 RCAs Identified:
- **4 incidents**: Data Issue - Poorly Segmented Domains
- **3 incidents**: Data Issue - Synchronization Problems
- **3 incidents**: Design Limitation - Synchronous Data Dependency

**November 2024 (5 Incidents)**

Top 3 RCAs Identified:
- **2 incidents**: Human Error - Misconfiguration of Systems
- **2 incidents**: Communications Failure - Miscomms Across Teams
- **2 incidents**: Software Defect - Inadequate QA & Outdated Libraries

**December 2024 (7 Incidents)**

Top 3 RCAs Identified:
- **3 incidents**: Data Issue - Data System Quality in Up/Downstream
- **1 incident**: Human Error - Misconfiguration of Systems
- **1 incident**: Infrastructure - System Overload

**January 2025 (12 Incidents)**

Top 3 RCAs Identified:
- **4 incidents**: Infrastructure - System Overloads (Tiger Tickets)
- **4 incidents**: Design Limitation - Lack of Domain Separation
- **2 incidents**: Design Limitation - Synchronous or Dependent Comms

**Key Takeaways:**
- Audit DB stabilization led to zero related incidents in December and January
- A peer review process was introduced to reduce human errors in configuration changes
- BT database-related incidents increased from 1→4 in January. The team pivoted during December to resolve

---

### Executive Summary (from Oct 29, 2024 deck in appendix)
**References:**
- [Board Deck] Slide 31: "Executive Summary" (2-slides from Oct 29, 2024)

**State of Exchange Stability:**
- Sev 1 & Sev 2 incident volume remains largely unchanged YoY (2023 to 2024), however, overall incident volume is down 50%
- Mean Time To Recover (MTTR) is worse in 2024 due to a few big incidents related to database upgrades in January and July

**Architecture:**
- The architecture is modular, but a few databases are becoming choke points due to the tight coupling of key modules/components of the architecture (Modular but Tightly Coupled Architecture)

**We are accelerating our Exchange Resiliency Roadmap by doing three things:**
- Reallocating internal resources to Exchange
- Bringing in help from the outside to augment (DBAs, Performance Testing, DR, Incident & Problem Management)
- Allocating more capacity within the existing Exchange engineering team toward Resiliency efforts

**We have a two-phase roadmap rooted in after-actions from incidents, foundational technology improvements, and improving communication with our customers:**
- **Phase 1 priorities** immediate focus areas over 30-90-180 days:
  - Addressing root causes of database spikes that have caused 50%+ incidents
  - Enhanced Performance Testing, which would have mitigated the risk of 60% of the incidents
  - Alerting and Monitoring Improvements
  - Incident Management and Problem Management Improvements. Both of which help with lower Mean Time To Recover
  
- **Phase 2 priorities** activities for the longer-term health of Exchange to mitigate risk and meet customer expectations and growth

**We will remain in a release-by-exception mode** at least through the end of the year to prioritize the stability of the system

---

### Exchange Incident Analysis: Mean Time to Recover
**References:**
- [Board Deck] Slide 32: "Exchange Incident Analysis: Mean Time to Recover"

**Exchange Incident Frequency, Transaction Volume, Mean Time to Recover**
*Incident Data as of 10/18/24*

**Key Takeaways:**
1. Mean Time To Recover (MTTR) is substantially worse in 2024 due to a few big incidents related to two database upgrade efforts in January and July
2. Customer frustration and concern are high due to the spillover impact of the two big incidents
3. Monthly transaction volume is largely stable but impacts specific parts of the architecture

**Chart shows:**
- Major MTTR spikes in Jan-24 (84.8 hrs), Feb-24 (43.5 hrs), Apr-24 (28.0 hrs), Jul-24 (20.2 hrs)
- Incident counts varying between 5-10 per month
- Transaction volume remaining relatively stable around 35,000-40,000

---

## SUPPORT TICKET TRENDS

**References:**
- [Exchange Plan] Slide 7: "MoM Case Volume Trends Generally Stable; Minimal Noise"

**Case Volume Upticks Driven by One Time Events or Seasonality; Otherwise Generally Consistent MoM**

**Notes from chart:**
1. July incident led to increased support volume before subsiding
2. Cases related to yearly file imports typically result in spikes during specific months
3. Registration, Procurement, and Credentialing activity are consistently managed within acceptable ranges

**Case trends shown for:**
- Exchange (highest volume ~2,000-3,000 cases/month)
- G-Fax (second highest ~1,500-2,500 cases/month)
- Lower volume products: IBR, Content, Invoice, ePay, Value Analysis, Registration, Inventory Management, Procurement, Credentialing

---

## SUMMARY FROM BOARD DECK

**References:**
- [Board Deck] Slide 2: "Exchange Resiliency Executive Summary"

**Significant improvements have materially reduced incidents related to databases:**
- Database Stability Swarm Team Efforts initiated in October have materially improved the health of key databases, resulting in zero database-related incidents for the last 4 months
- Increased rigor in change management and release management processes have had a significant impact in reducing incidents due to changes/releases

**Top 3 priorities remain in the roadmap:**
- **#1 Priority** - Database Stabilization: Audit DB and BT DB (two key databases) in a significantly healthier state
- **#2 Priority** - Increased Release Rigor: Continuing the Release By Exception mode, but business is not at a standstill as we are making high-priority low-risk releases to meet customer commitments
- **#3 Priority** - Performance Environment: On track to finish Phase 1 scope by April 15 in partnership with third-party testing experts (Cigniti) introduced by the Warburg team. Env is stood up in the AWS West region to act as DR env down the line

**Other key initiatives:**
- Review of the incident and problem management processes (to help respond to incidents and learn from them better) with a top-tier third party (AKF Partners) completed and recommendations initiated
- Industry BCP effort kicked off. 16 Product Discovery meetings completed (6 providers, 8 suppliers, 2 distributors). Product Requirements to be completed by the end of Q1
- Continued engagement with the Customer Advisory Board and key customers on overall Exchange Resiliency to build confidence with customers. It is early days, but customer sentiment is trending up

---

*This document catalogs all resiliency work identified in the three reference decks with specific citations to source slides/pages.*
