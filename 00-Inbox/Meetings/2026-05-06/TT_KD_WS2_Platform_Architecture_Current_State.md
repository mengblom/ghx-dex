# TT/KD WS2 - Platform Architecture (Current State)

## Meeting Info

| Field | Value |
|-------|-------|
| **Date** | 2026-05-06 |
| **Time** | 4:00 PM - 5:30 PM MDT |
| **Duration** | 90 minutes |
| **Meeting Type** | Technical Architecture Review |
| **Source** | Granola + Calendar |
| **Granola ID** | d30880ae-0c9b-4c72-9f2b-c30944de7502 |
| **Calendar Event ID** | AFEC14D1-8299-457E-9014-B8C5AC911FFF:65E3E235-D8DD-48A5-85F7-FB5CBBF7CE3C |
| **Location** | Zoom (https://us02web.zoom.us/j/89337897732) |

## Attendees

**Internal (GHX):**
- [[Marten_Engblom|Marten Engblom]] (mengblom@ghx.com) - Accepted
- [[CJ_Singh]] (csingh@ghx.com)
- [[Bharat_Patel|Bharat Patel]] (bsharma@ghx.com) - CDP Lead
- [[Daniel_Milburn|Daniel Milburn]] (dmilburn@ghx.com) - Fusion History
- Geoff Wilson (gwilson@ghx.com)
- [[Anand_Mani|Anand Mani]] (amahammad@ghx.com)

**External (Kickdrum):**
- Hong Lim (hong.lim@kickdrumtech.com) - Organizer
- Michael Schnapf (michael.schnapf@kickdrumtech.com)
- Ryan Kennedy (ryan@kickdrumtech.com)
- Ryan Donnelly (ryan.donnelly@kickdrumtech.com)
- Tim LoGrasso (tim@kickdrumtech.com)
- Jay Kamm (jay@kickdrumtech.com)

**External (TechTern/Thinktiv):**
- Joe Petro (jpetro@thinktiv.com)
- Sha Waters (swaters@thinktiv.com)
- Ankit Malhotra (amalhotra@thinktiv.com)

**External (Veritas Capital):**
- Vinay George (vgeorge@veritascapital.com) - Optional

## Context

Deep dive session on GHX's shared platform architecture - covering Common Data Platform (CDP), Fusion integration layer, SSO, and AI Platform. Part of architecture review workshops with external consultants.

**Meeting Purpose:** Review GHX's current platform architecture and shared services to understand the foundation for transformation initiatives.

**Calendar Match Notes:**
- ✅ Matched with calendar event at 4:00-5:30 PM MDT
- ✅ Added 15 attendees with full email addresses from calendar
- ⚠️ Granola identified "Mike Mitchell" in attendance, but calendar shows "Geoff Wilson" (gwilson@ghx.com) instead
- ✅ Identified external consultants from Kickdrum, TechTern/Thinktiv, and Veritas Capital

## Executive Summary

**Core Platforms:** GHX's architecture centers on two platforms: CDP (Common Data Platform) for batch analytics and Fusion for ERP integration. These enable data correlation and new product development (NPIs) while reducing redundant ETL work.

**Strategic Buy vs. Build:** A key strategic shift is underway to replace custom-built systems with commercial tools. The legacy SSO system will be replaced by Auth0 to standardize security and enable mandatory MFA, and a custom MDM tool (Redsel POC) is being built to replace the problematic Atakam platform.

**Platform 2.0 & AI:** The "Orchestration Platform" is the next major initiative, building on the existing "AI Platform" (for copilots) to create agent-based workflow automation. This requires a new semantic layer ("Platinum layer") and near real-time data ingestion into CDP.

**Infrastructure Modernization:** The infrastructure is migrating entirely to AWS, with a goal to shut down the last on-prem data center by EOY. A "TechDP" (Developer Platform) is also in development to standardize Kubernetes and accelerate team adoption.

## Key Discussion Points

### Infrastructure & AWS Migration
- **Single data center remaining** (North America, from acquisition)
- **Goal:** Complete AWS migration by end of year
- **Approach:** Full re-platforming (not lift-and-shift) for remaining workloads
- **Historical:** Started with lift-and-shift, refined over time

### Common Data Platform (CDP)
**Current Scale:**
- **188 terabytes** storage
- **40 data producers** (internal apps, external feeds, provider ERPs)
- **120+ consumers**, 211 monthly platform users
- **Key consumers:** Data Connect, EIPP, Price Workbench, analytics platforms, AI use cases

**Architecture:**
- Bronze → Silver → Gold layers (canonical GHX format)
- **Semantic Layer (Platinum):** Planned on top of Gold layer for orchestration platform
- Source of truth varies by data type:
  - Customer ERPs for transactional data
  - Exchange for some operational data
- Provides queryable repository for products
- **Purpose:** Central repository for reusable data, enabling correlation and NPIs while reducing redundant ETL. Does NOT replace product-specific transactional data stores.

**Current Limitations:**
- Batch processing (minutes latency)
- Near real-time streaming planned for orchestration platform use cases

**Access Patterns:**
- REST APIs for real-time access
- Data marts for complex processing (Snowflake-based)
- SQL access available

**Tech Debt Focus:**
- Low test automation coverage (using AI to accelerate)
- Data quality improvements (rule-based → AI-driven)
- Infrastructure modernization:
  - Move from self-hosted to managed databases
  - Transition to serverless compute
  - Replace custom event bus (MongoDB-based) with modern messaging

### Fusion Integration Platform
**Age:** 6-7 years in operation
**Four Core Components:**
1. **Fusion Gateway** - Third-party API calls into GHX systems
2. **Control Tower** - Visibility/configurability across integrations
3. **Fusion Stream** - Cloud ERP connectivity (Workday, Oracle, Infor)
4. **Fusion Connect** - On-premise ERP connectivity

**Architecture:**
- Kubernetes-based, modular, independently deployable by ERP
- Stateless design using Redis for internal state, SQS for permanent messaging

**Data Routing:**
- Transactional data → Exchange
- Non-transactional data → CDP (purchase order history, invoices, item data)

**Critical Usage:**
- Used by all products: Data Connect, Price Workbench, Content Workbench, Inversion Payment, Exchange

### Single Sign-On (SSO) Platform
**Age:** 14 years old (originally from acquisition)
**Current Scale:** 300K annual users across 6-7 major applications

**Adoption Challenges:**
- Not universal across all GHX products due to legacy product stacks and integration effort
- Some products still use separate authentication systems

**Capabilities:**
- Username/password authentication
- Federated SSO (Azure, Okta, Ping)
- MFA available but not universally enforced (can be enforced at IDN org level)

**Authorization Limitations:**
- Separate lightweight "User Management" tool provides only coarse-grained access control (Admin/Manager/User at product level)
- Granular permissions handled by individual applications
- Customer admin designation at facility level
- No standardized authorization framework across products

**Planned Migration:**
- **Auth0 migration on roadmap** (prioritized)
- Driven by MFA enforcement requirements
- Auth0 provides shorter path to mandatory MFA
- Offers more familiar, trusted integration experience for customers
- Reduce custom platform maintenance

### AI Platform & Orchestration
**AI Platform:**
- Common services for copilot implementations
- RAG architecture, LLM communication, agent orchestration
- Enables rapid copilot deployment across teams
- Uses LangChain, LangFuse for orchestration
- Custom similarity models for RAG

**Orchestration Platform 2.0:**
- Micro-workflow automation for customers
- Agent-based architecture leveraging AI Platform
- Requires semantic layer/ontology development
- Integration with existing CDP data assets

### Platform Development Standards
**TechDP (Developer Platform):**
- Kubernetes-based platform standardization across teams
- Provides common functions to accelerate team adoption
- Moving teams off self-managed EC2 instances to standardized platform
- VAST team as initial pilot
- Part of broader infrastructure modernization (managed services, serverless)

**Current Gaps:**
- Inconsistent logging/auditing across products
- No standardized authorization framework
- Multiple authentication systems still in use
- Security concerns around distributed auth/authz systems
- Security logging exists for SSO users but inconsistent across non-SSO products

### Buy vs Build Considerations

**Buy (Replace Custom with Commercial):**
- **SSO → Auth0 migration** (prioritized) - Replace 14-year-old custom system
- **Event bus replacement** - Modernize custom MongoDB-backed event bus with Kafka or SQS-based messaging

**Build (Custom Solutions):**
- **MDM (Master Data Management)** - Building custom "Redsel POC" to replace problematic Atakam platform
  - Atakam issues: Black-box problems, performance issues, scalability/usability concerns
  - Also evaluated and retired EPIM for similar reasons
  - Considering build-your-own approach with AI capabilities

**Evaluate:**
- **Orchestration platform** vs Palantir - Agent-based workflow automation
- **AI Platform partnerships** - Potential Google/AWS collaborations under discussion
- Currently using hybrid: open-source frameworks (LangChain, LangFuse) + custom AI models (RAG similarity)

## Technical Debt Highlights

**CDP:**
- Low test automation (AI acceleration in progress)
- Data quality (moving to AI-driven)
- Infrastructure modernization (managed services, serverless)

**Fusion:**
- Generally modern architecture (Kubernetes, modular)
- Continue data streamlining across products

**Exchange/Core:**
- Custom event bus on MongoDB → needs modern messaging
- Lift-and-shift footprint on EC2 → containerization needed
- Self-hosted databases → managed services

## Key Architectural Decisions Discussed

1. **Real-time data ingestion to CDP** - Feature-driven, not tech debt (orchestration platform use cases requiring near real-time via CDC)
2. **MDM tools evaluated and retired** - EPIM and Atakam had scalability/usability issues and black-box problems; building custom "Redsel POC" with AI capabilities
3. **Authorization strategy** - No standard authz across products, each app manages its own; lightweight "User Management" tool provides only coarse-grained product-level access
4. **Security logging** - Exists for SSO users, but inconsistent across non-SSO products
5. **Infrastructure strategy** - Moving from self-hosted databases (e.g., Mongo on EC2) to cloud-managed services (e.g., Atlas)

## Open Questions / Follow-ups

- **Data governance artifacts** - Bharath to share confluence documentation
- **Data flow diagrams** - End-to-end inbound/outbound through services (may not exist)
- **Architecture drift tracking** - How current are architecture diagrams?
- **Semantic layer design** - Design meeting tomorrow on orchestration platform
- **Tech debt backlog** - Top 5 largest tech debt items per platform

## Action Items

### For Me
- [ ] Review semantic layer/ontology design for orchestration platform (design meeting tomorrow) ^task-20260506-009
- [ ] Consider Auth0 migration priority vs MFA enforcement requirements ^task-20260506-010
- [ ] Add shared docs from this call to IRL; upload to data room ^task-20260506-011

### For GHX Team
- **Bharat Patel:** Email Confluence links re: CDP data governance/hygiene to Timothy LoGrasso (Kickdrum)
- **Bharat Patel:** Share data governance confluence documentation
- **Marten/Daniel:** Check for end-to-end Fusion data flow diagram; if exists, share with Vinay George (Veritas)
- **Daniel/Marten:** Discuss event bus replacement options (Kafka vs SQS-based)

### For Kickdrum
- Review provided materials to prepare for upcoming CDP deep dive
- Participate in orchestration platform technical design meeting to provide external perspective

## Related Projects
- [[04-Projects/Exchange Platform Architecture/]]
- [[04-Projects/AI Platform/]]

## Tags
#meeting #architecture #platform #cdp #fusion #sso #ai-platform

---

**Granola Chat:** https://notes.granola.ai/t/c4956a0a-851b-4320-9b57-cb0510d471cb

**Notes:**
- This meeting record was enriched with calendar data (15 attendees with full email addresses)
- Reconciled with Kickdrum summary sent by Tim LoGrasso (stored in `00-Inbox/Temp/`)
- Combined Granola transcript analysis with Kickdrum's executive summary and action items
