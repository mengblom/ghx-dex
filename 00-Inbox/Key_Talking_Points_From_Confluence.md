# Key Talking Points from Confluence Documentation

**Source:** Rovo search results [[00-Inbox/Kickdrum Prep from Confluence.md]]  
**Purpose:** Quick reference sheet for Thinktiv/Kickdrum presentations and CJ meeting

---

## 🔥 CRITICAL FINDING for CJ's "Breaking the Monolith" Deliverable

### From: [Resiliency Future Plan - April 2025](https://prd.hub.ghx.com/wiki/spaces/EA/pages/296812545/Resiliency+Future+Plan+-+April+2025)

> **"Not trying to re-architecture the Exchange (i.e. re-design EventBus or move to micro-services). Those type efforts are for Gen3."**

**Why this matters:**
- Current stability work (DB migration, DR maturity, resiliency spike) is NOT full microservices transformation
- "Gen3" is the future state with domain-based microservices, serverless, eventual consistency
- Your "breaking the monolith" scope should be BETWEEN today and Gen3

**Implications for CJ deliverable:**
- ✅ Right-size: Decouple specific database dependencies, extract specific services
- ✅ Right-size: Expand Lambda conversions (Contivo Standalone already happening)
- ❌ Out of scope: Redesigning EventBus core architecture
- ❌ Out of scope: Full microservices transformation (that's Gen3, not current 5 priorities)

**Use this to answer CJ's question:** "How to ensure not underdoing or overdoing it?"

---

## Session 1: Platform Architecture - Key Points

### High-Level Architecture

**CoreX vs Exchange Platform:**
- **CoreX** = EDI transaction processing (the monolith engines)
- **Exchange Platform** = User interfaces, job scheduling, data management

**CoreX Engines (all "Monolith Web App" per DR Analysis):**
- Engine-PE (Processing Engine)
- Engine-IO (Input/Output)
- Engine-DataPoller
- Engine-Jobs
- Engine-EINV (eInvoicing)
- Heimdall

**Technology Stack:**
- **Languages:** Java (primary), Python (IPA/ML), Angular (frontend)
- **Databases:** MongoDB (BT/BD, Eventbus, Audit), MySQL (TPM), Elasticsearch, S3
- **Infrastructure:** AWS (EC2, S3, SQS, ECS, Lambda, API Gateway)
- **Frameworks:** Spring Security, Quartz, Smooks, GraphQL, New Relic

### Integration Patterns

**Event-Driven Architecture (EGX Event Bus):**
- SOA2 event-based processing model
- Typed immutable events
- EEB framework for publishing/dispatching
- MongoDB Eventbus as coordination layer

**Document Flow:**
- Inbound: SFTP → IO Engine → Processing Engine → Eventbus → Actions → Downstream systems
- Actions framework: Some converted to Lambdas (Contivo Standalone - CSA)
- Mapping: Contivo or Smooks transformations

**Downstream Systems:**
- MEX (My Exchange portal)
- Heimdall (notification/routing)
- Registration Center
- eInvoicing

### Monolith Reality

**Current State (from DR Analysis):**
- All engines deployed as monolith
- Blue-Green deployment in us-east-1
- Pilot Light DR in us-west-2

**Progress Toward Services:**
- Contivo Standalone (CSA) = "java based lambda micro-services"
- 5+ actions already converted from monolith to Lambdas
- Offloading transformation work from monolith

**Gen3 Vision (future, not current scope):**
- Domain-based microservices
- Serverless architecture
- Eventual consistency
- GHX App Platform

---

## Session 2: Platform-Enabling Services - Talking Points

### Topic 1: Identity, SSO, Authentication & Authorization

**Two Identity Systems:**

1. **Okta** (ghxsso.okta.com)
   - Corporate/workforce identity
   - SAML-based SSO
   - For GHX internal applications

2. **GHX Identity Service** (login.ghx.com)
   - Product/customer identity
   - OpenID Connect (OIDC) for authentication
   - OAuth 2.0 for authorization
   - SAML multi-tenant federation
   - **Technical owners:** Daniel Milburn, Prashanth Garlapati

**Authentication Flow:**
- User logs in via GHX Identity Service or Okta
- OIDC auth code flow (redirect-based PKCE for SPAs)
- JWT issued with tenant info (agent tuple with organization EID)
- Spring Security handles session (JSESSIONID)

**Authorization (RBAC):**
- Bronze/Silver/Gold tiers
- Permissions always restricted to specific tenant
- TPM database = tenant store
- Product subscription → role mapping → access

**Multi-Tenancy:**
- Tenant determined at login via JWT
- Single-user can have multiple tenant roles (alternate organizations)
- Subscribed product parameters for per-tenant config

**Key Technologies:**
- MITREid-based OpenID Connect implementation
- Spring Security
- Nimbus JOSE & JWT
- SAML 2.0 Spring Security Extension

### Topic 2: Core UI/UX Shared Components

**CoreUI = The Design System:**
- Angular library: `@ghx/ui-core`
- 20+ applications using it
- Standards and guidelines for all GHX products
- Built on Angular Material
- Live documentation: coreui.ghx.com
- **Technical owner:** Anthony Middleton

**Module Inventory:**

| Module | Package | Purpose |
|--------|---------|---------|
| Common | @ghx/ui-core/common | Utilities, directives, pipes, services |
| Core | @ghx/ui-core/core | App shell (header, footer, sidebar, breadcrumbs) |
| Security | @ghx/ui-core/security | OIDC authentication, guards |
| Ag-Table | @ghx/ui-core/ag-table | Data tables with ag-grid |
| Forms | @ghx/ui-core/forms | Form components and validators |
| Chart | @ghx/ui-core/chart | Vega-Lite charts with GHX theme |
| Chat | @ghx/ui-core/chat | Chat/Copilot UI components |
| File | @ghx/ui-core/file | File viewers and diff tools |
| Dashboard | @ghx/ui-core/dashboard | Dashboard tiles and Looker embeds |

**Frontend Tech Stack (Modern Angular SPAs):**
- Angular 21 with TypeScript Strict Mode
- Angular Signals for state management
- Vite-based builds
- **UI hierarchy:** GHX Core-UI (first) → Angular Material (fallback) → TailwindCSS (utility)
- Authentication: Okta with OIDC/OAuth 2.0
- Testing: Vitest, minimum 80% coverage

**Reusability Story:**
- SSO integration built-in
- Consistent headers/footers across products
- Custom Angular Material components
- Theming capabilities
- Design tokens / Style Dictionary approach
- Figma integration for design handoff

**Real-World Adoption:**
- BIAP: 533 components, 735 files using ui-core
- InvoSight: 15 components, 21 files using ui-core
- MEX Notifications UI: Uses @ghx/ui-core and @ghx/mex-ui-core

### Topic 3: Intelligent Process Automation (IPA)

**High-Level:**
- Combines RPA with AI
- **Platform:** UiPath cloud-based automation
- **Mission:** Replace $5M FirstSource manual digitization cost
- Became part of value proposition (not just cost savings)

**Four Pillars:**

1. **GFax** (Purchase Order automation)
   - PO classification & data extraction
   - ~300 customers
   - 45-50% automated
   - 98.7%+ OCR accuracy via UiPath AI Center
   - 75-attribute PO data model
   - Target: >60% capture rate (Phase 1.5)

2. **PriceSync**
   - Automated weekly price exception decks
   - RPA-based

3. **eInvoicing** (Invoice automation)
   - 15% automated (growing)
   - Invoice classification, validation, transformation to EDI 810
   - Pipeline: OCR → Validation → Enrichment → CoreX Mapper → EDI 810
   - Target: 90% field extraction, 98% correct placement
   - Throughput: 2,000 docs/hour, 12,000 full automation in 12-hour SLA

4. **MSOT** (Manual Sales Order Processing)
   - UI automation for email correlation and PO acknowledgments
   - RPA-based workflow automation

**Technical Architecture:**

| Component | Purpose | Technologies |
|-----------|---------|--------------|
| Orchestrator | RPA code management, scheduling | UiPath Cloud Orchestration |
| Robot Server | RPA code execution | UiPath Robot, Windows Server, AWS EC2 |
| GFax/Image API | OCR, classification, keyword filtering, PHI/CC detection | Python, Tesseract (ML/OCR), ECS, Stoplight |
| IPA Journal | Reporting and logs | Elasticsearch (AWS Managed), Kibana |
| IPA Configuration | Config storage | DynamoDB |
| App Integration | CoreX integration | AWS S3, AWS SQS |

**GFax 10-Step Classification Pipeline:**
1. Page length check
2. OCR/ML extraction (Tesseract)
3. Language detection
4. PO number extraction
5. PHI detection (protected health info)
6. Credit card detection
7. Terms & Conditions filtering
8. Keyword rejection
9. PO validation
10. Results return (JSON response)

**Performance Metrics:**
- GFax OCR accuracy: 98.7%+
- GFax processing SLA: 10-15 minutes per transaction
- eInvoicing field accuracy: 90% extraction, 98% correct placement
- eInvoicing throughput: 2,000 docs/hour

**Integration with Exchange:**
- S3 for document storage
- SQS for message queuing
- CoreX actions framework integration
- Two-stage validation: classification → keyword rejection

**Service Reusability:**
- APIs exposed via Stoplight documentation
- Potential for other GHX products to leverage OCR/classification capabilities
- Configuration-driven (DynamoDB, UiPath Orchestrator assets)

---

## Topic 4 (Bonus): Service Consumption Model Across Pods

**Current Patterns (from docs):**
- Event-driven via EGX Event Bus
- REST APIs (GraphQL for some services)
- S3/SQS for async integration
- Shared databases (anti-pattern, being addressed)

**Questions to Address:**
- Standard API gateway or service mesh approach?
- Service discovery mechanisms?
- Versioning and backward compatibility?
- Rate limiting, quotas, SLAs?
- Documentation for service consumers (Stoplight for IPA)?

**Ideal State (to discuss with consultants):**
- API-first design
- Contract-first development
- Consumer-driven contract testing
- Self-service onboarding for new consumers
- Observability (tracing, metrics, logs)

---

## Database Dependencies (Critical for "Breaking Monolith")

**Known Anti-Patterns from Architecture Flaws doc:**

1. **Audit DB dependencies:**
   - SFTP endpoints shouldn't go down because Audit DB is unresponsive
   - Core document processing shouldn't depend on Audit DB

2. **MongoDB ActivityFlow pattern:**
   - 188M documents/day stored in MongoDB
   - Deleted and archived to S3 after 3 days
   - Why not write directly to S3 when we have rehydration mechanisms?

3. **Shared schemas:**
   - Multiple teams accessing same databases
   - Creates hidden dependencies, blocks independent deployment
   - Forces coordination across teams

**Goal:** Teams own their data and data stores (your India trip priority)

---

## Deployment & SDLC Context

**Current Deployment Model:**
- Monolithic deployment (all engines together)
- Blue-Green in us-east-1
- Pilot Light DR in us-west-2
- Monthly release cadence (defensive posture due to blast radius)

**Progress Toward Independent Deployment:**
- Lambda conversions (Contivo Standalone) can deploy independently
- IPA services deploy independently (UiPath Orchestrator, Python services)
- UI applications can deploy independently (SPAs with CoreUI)

**Testing Challenges (from your vault):**
- Tandoori legacy testing framework
- Manual testing still required
- Hard to achieve trusted automated coverage for monolith

---

## Quick Reference: Who Owns What

**Teams (from Architecture Picture):**
- **Mapping Team:** Contivo/Smooks maps, Lambda conversions, Actions framework
- **IPA Team:** GFax, PriceSync, eInvoicing, MSOT (UiPath-based)
- **Visibility Team:** My Exchange portal, Angular/Tomcat/SpringBoot, CoreUI adoption
- **Doc Enrichment Team:** Rules engine, actions framework, IBR, Odin, Complex Ordering, DREF extraction
- **User Platform (Mike Mitchell):** Identity, SSO, User/Org management
- **Org Platform (Mike Mitchell):** Organization data, multi-tenancy

**Technical Owners (per Confluence):**
- **GHX SSO:** Daniel Milburn, Prashanth Garlapati
- **CoreUI:** Anthony Middleton
- **IPA:** (Partnership with Global Logic and UiPath)

---

## Consultant Questions You'll Likely Get

**Platform Architecture:**
1. Why is EventBus still on MongoDB? (Answer: Gen3 will address, not current scope)
2. What's blocking independent deployment? (Answer: Database dependencies, shared schemas)
3. Why monthly releases? (Answer: Monolithic blast radius, defensive testing posture)
4. What's the strangler fig strategy? (Answer: Lambda conversions, service extraction, Gen3 planning)

**Identity/SSO:**
1. Why two identity systems? (Answer: Okta for workforce, GHX Identity for products/customers)
2. How do you handle multi-tenancy? (Answer: JWT with tenant info, TPM as tenant store)
3. What's the authorization model? (Answer: RBAC, roles scoped to tenant)
4. Any plans to consolidate? (Answer: Ask Mike/Daniel)

**UI Components:**
1. What's the adoption rate? (Answer: 20+ apps, but varies - BIAP high, InvoSight low)
2. How do you govern updates? (Answer: npm package @ghx/ui-core, versioning strategy)
3. Accessibility compliance? (Answer: Roadmap item, design tokens approach)
4. Design system ownership? (Answer: Anthony Middleton, CDM team)

**IPA:**
1. Can other products use IPA? (Answer: Yes, APIs exposed, configuration-driven)
2. What's the ROI? (Answer: $5M FirstSource replacement, now value-add for customers)
3. Technical debt? (Answer: 2020-21 startup mode, now focusing on engineering rigor)
4. Scaling constraints? (Answer: 45% bandwidth on data ingestion/business rules, not core automation)

---

*Created: 2026-05-01*  
*Source: [[00-Inbox/Kickdrum Prep from Confluence.md]]*  
*Print this for quick reference during meetings*
