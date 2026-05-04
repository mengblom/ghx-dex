# Thinktiv/Kickdrum - Priority Reading List

**Source:** Confluence Rovo search results [[00-Inbox/Kickdrum Prep from Confluence.md]]  
**Goal:** Focus your limited prep time on highest-value documents for both sessions

---

## 🔥 Must-Read Before Daniel/Mike Session (Top Priority)

### Session 1: Platform Architecture

**1. [Exchange Architecture Diagrams](https://prd.hub.ghx.com/wiki/spaces/SRE/pages/1180991550/Exchange+Architecture+Diagrams)** ⭐⭐⭐
- **Why:** SOURCE OF TRUTH - canonical Exchange Data Flow Diagram
- **Contains:** High-Level Architecture, Document Lifecycle, IO Engine, Processing Engine, Eventbus
- **Use for:** Understanding overall system topology, integration points

**2. [CoreX Architecture Review - 2023 Update](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28796788/CoreX+Architecture+Review+-+2023+Update)** ⭐⭐⭐
- **Why:** Comprehensive tech inventory and component list
- **Contains:** Event-driven architecture, all CoreX engines, technology stack (Java, MongoDB, MySQL, Redis, Elasticsearch)
- **Use for:** Technology stack discussion, understanding component boundaries

**3. [Resiliency Future Plan - April 2025](https://prd.hub.ghx.com/wiki/spaces/EA/pages/296812545/Resiliency+Future+Plan+-+April+2025)** ⭐⭐⭐
- **Why:** Documents monolith reality AND Gen3 microservices vision
- **Contains:** "Not trying to re-architecture Exchange... Those efforts are for Gen3"
- **Use for:** CJ's "breaking the monolith" deliverables - shows current thinking on scope

---

### Session 2: Platform-Enabling Services (You're Presenting!)

#### Topic 1: Identity/SSO (Mike's Expertise)

**4. [Workforce Identity Management](https://prd.hub.ghx.com/wiki/spaces/EA/pages/39166013/Workforce+Identity+Management)** ⭐⭐⭐
- **Why:** Explains the TWO identity systems
- **Contains:** Okta (ghxsso.okta.com for corporate) vs GHX Identity Service (login.ghx.com for products)
- **Use for:** High-level overview, when to use which system

**5. [GHX SSO](https://prd.hub.ghx.com/wiki/spaces/EA/pages/646840321/GHX+SSO)** ⭐⭐
- **Why:** Technical implementation details
- **Contains:** SAML multi-tenant federation, OIDC auth, OAuth2 authorization
- **Technical owner:** Daniel Milburn, Prashanth Garlapati (your direct reports!)

**6. [Tenancy Model](https://prd.hub.ghx.com/wiki/spaces/EA/pages/39165324/Tenancy+Model)** ⭐⭐⭐
- **Why:** Critical for multi-tenancy discussion
- **Contains:** JWT-based tenant determination, TPM as tenant store, single-user multi-tenant support
- **Use for:** Explaining how customer data isolation works

#### Topic 2: UI Shared Components (Daniel's Team)

**7. [CoreUI](https://prd.hub.ghx.com/wiki/spaces/EA/pages/645398551/CoreUI)** ⭐⭐⭐
- **Why:** THE design system, Angular library `@ghx/ui-core`
- **Contains:** 20+ applications using it, technical owner Anthony Middleton
- **Live docs:** coreui.ghx.com
- **Use for:** Showing reusability across teams, SSO integration, standard components

**8. [Frontend Application Tech Stack](https://prd.hub.ghx.com/wiki/spaces/NEX/pages/893059503/Frontend+Application+Tech+Stack)** ⭐⭐
- **Why:** Modern Angular SPA standards
- **Contains:** Angular 21, TypeScript strict mode, Okta OIDC, 80% test coverage requirement
- **UI hierarchy:** GHX Core-UI (first) → Angular Material (fallback) → TailwindCSS (utility)
- **Use for:** Explaining frontend technology choices and standards

#### Topic 3: IPA (Your Responsibility)

**9. [IPA (EA Landscape)](https://prd.hub.ghx.com/wiki/spaces/EA/pages/655818795/IPA)** ⭐⭐⭐
- **Why:** High-level business + technical overview
- **Contains:** UiPath-based, GFax (PO), PriceSync, eInvoicing, MSOT pillars
- **Use for:** Explaining IPA capabilities to consultants

**10. [IPA Production Architecture (PPT)](https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=28852907&preview=%2F28852907%2F28832544%2FIPA-ProductionArchitecture+%5BAutosaved%5D.pptx)** ⭐⭐⭐
- **Why:** Component inventory and architecture diagram
- **Contains:** Orchestrator, Robot Server, GFax/Image API (Python, Tesseract OCR, ECS), IPA Journal (Elasticsearch), Integration with CoreX (S3, SQS)
- **Use for:** Technical architecture walkthrough

**11. [G-Fax NA Full Automation](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28910771/G-Fax+NA+Full+Automation)** ⭐⭐
- **Why:** Performance metrics and automation scope
- **Contains:** 98.7% OCR accuracy, 75-attribute PO data model, >60% capture target
- **Use for:** Showing business value and technical sophistication

---

## 📚 Secondary Reading (If Time Permits)

### For Deeper Platform Architecture Understanding

**12. [Exchange Platform - ITSM Operator Guide](https://prd.hub.ghx.com/wiki/spaces/IE/pages/1216053256/Exchange+Platform+-+ITSM+Operator+Guide)**
- Distinguishes CoreX (EDI processing) from Exchange Platform (UI, jobs, data)
- Infrastructure details (AWS US/EU, MongoDB cluster, Elasticsearch)

**13. [Exchange Disaster Recovery Analysis](https://prd.hub.ghx.com/wiki/spaces/EX/pages/33880466/Exchange+Disaster+Recovery+Analysis)**
- Lists all CoreX engines as "Monolith Web App"
- Contivo Standalone (CSA) noted as "java based lambda micro-services"

### For Integration Pattern Details

**14. [EGX Event Bus Architecture](https://prd.hub.ghx.com/wiki/spaces/EX/pages/33887628/EGX+Event+Bus+Architecture)**
- SOA2 event-based processing model
- Typed immutable events, EEB framework

### For IPA Technical Details

**15. [IPA GFax Classification & Keyword APIs](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28836386/IPA+GFax+Classification+Keyword+APIs)**
- 10-step PO classification pipeline
- API inputs, response schema, configuration

**16. [IPA - eInvoicing Process](https://prd.hub.ghx.com/wiki/spaces/dev/pages/151585738/IPA+-+eInvoicing+Process)**
- Invoice automation pipeline: OCR → Validation → Enrichment → Mapper → EDI 810

---

## 🎯 How to Use This for Your Two Key Meetings

### For Daniel/Mike Prep Session (Tue/Wed)

**Agenda Item 1: Platform Architecture (45 min)**
- Walk through Exchange Architecture Diagrams together
- Use CoreX Architecture Review to understand component boundaries
- Discuss Resiliency Future Plan → informs CJ's "breaking monolith" deliverables

**Agenda Item 2: Identity/SSO (30 min with Mike)**
- Mike walks you through the two identity systems (Okta vs GHX Identity)
- Discuss Tenancy Model for multi-tenant customer isolation
- Get talking points for consultant presentation

**Agenda Item 3: UI Components (15 min with Daniel)**
- Daniel shows CoreUI live documentation (coreui.ghx.com)
- Discuss reusability story across 20+ applications
- Get component inventory talking points

**Agenda Item 4: IPA (Action Item)**
- These docs might be enough for consultant presentation
- Decide if you need separate session with IPA team lead

---

### For CJ's "Breaking the Monolith" Deliverable

**Key Finding from Rovo Results:**

From [Resiliency Future Plan - April 2025](https://prd.hub.ghx.com/wiki/spaces/EA/pages/296812545/Resiliency+Future+Plan+-+April+2025):
> "Not trying to re-architecture the Exchange (i.e. re-design EventBus or move to micro-services). Those type efforts are for Gen3."

**This is CRITICAL context:**
- Current resiliency work explicitly NOT redesigning EventBus or moving to microservices
- "Gen3" is the placeholder for full microservices transformation
- Your "breaking the monolith" deliverables should be scoped BETWEEN current state and Gen3

**CJ's Question:** "How to ensure not underdoing or overdoing it?"

**Your Answer (informed by this doc):**
- **Underdoing:** Leaving database dependencies that block team autonomy
- **Right-sizing:** Decouple specific services (SFTP, Doc Enrichment) without redesigning EventBus
- **Overdoing:** Full Gen3 microservices transformation (not in scope for current 5 priorities)

**Suggested "Breaking the Monolith" Deliverables (from Rovo findings):**

1. **Decouple Database Dependencies** (from Architecture Flaws doc)
   - DONE = SFTP endpoints don't depend on Audit DB
   - DONE = Remove MongoDB 188M ActivityFlow docs/day pattern (use S3 directly)

2. **Extract Document Enrichment Service** (separate team, separate codebase)
   - DONE = Can deploy enrichment changes without monolith deploy
   - DONE = IPA integration doesn't require monolith code changes

3. **Expand Contivo Standalone (CSA) Lambda Conversions** (already happening)
   - DONE = 10 more actions converted from monolith to Lambdas
   - DONE = Mapping team can deploy transformations independently

4. **Team-Owned Data Stores** (your India trip priority)
   - DONE = Mapping Team owns transformation data (no shared schemas)
   - DONE = Visibility Team owns portal data independently

5. **Gen3 Foundation Architecture** (discovery/planning only)
   - DONE = Define domain boundaries for future microservices
   - DONE = Document strangler fig migration approach
   - NOT IN SCOPE: Actually building Gen3 (that's post-5 priorities)

---

## 📊 Technology Stack Summary (for quick reference)

**From CoreX Architecture Review:**

| Layer | Technologies |
|-------|-------------|
| **Languages** | Java (primary), Python (IPA/ML), AngularJS/Angular (frontend) |
| **Databases** | MongoDB (BT/BD, Eventbus, Audit), MySQL (TPM), Elasticsearch (Activity Flow), Amazon S3 |
| **Infrastructure** | AWS (EC2, S3, SQS, ECS, Lambda, API Gateway), New Relic, Redis |
| **Frameworks** | Spring Security, Quartz Scheduler, Smooks, GraphQL |
| **Frontend** | Angular 21, CoreUI (@ghx/ui-core), Angular Material, TailwindCSS |
| **Identity** | Okta (corporate SSO), GHX Identity Service (product login), SAML, OIDC, OAuth2 |
| **IPA** | UiPath Orchestrator, Python, Tesseract OCR, DynamoDB, Elasticsearch/Kibana |

---

## ✅ Pre-Meeting Action Items

**Before Daniel/Mike Session:**
- [ ] Read docs #1, #2, #3 (Platform Architecture essentials)
- [ ] Skim docs #4, #5, #6 (Identity/SSO for Mike's discussion)
- [ ] Skim docs #7, #8 (CoreUI for Daniel's discussion)
- [ ] Read docs #9, #10, #11 (IPA for your presentation)

**During Daniel/Mike Session:**
- [ ] Ask Daniel about technical ownership (he's listed as GHX SSO technical owner!)
- [ ] Get Mike's perspective on User/Org Platform data architecture (tenancy model)
- [ ] Validate your "breaking monolith" deliverables against Resiliency Future Plan scope

**After Session:**
- [ ] Draft 3-5 monolith deliverables for CJ using Resiliency Plan as scope boundary
- [ ] Create capacity roadmap showing Gen3 as future state (not current 5 priorities)
- [ ] Prepare talking points for Thinktiv/Kickdrum using architecture diagrams

---

## 🎬 Time Estimate

**Focused reading (Must-Read docs #1-11):** ~3-4 hours
- Platform Architecture (docs #1-3): 1 hour
- Identity/SSO (docs #4-6): 1 hour
- CoreUI (docs #7-8): 30 min
- IPA (docs #9-11): 1.5 hours

**Recommendation:** 
- Block Monday afternoon for reading docs #1-3 and #9-11 (Platform + IPA)
- Read docs #4-8 (Identity + UI) Tuesday morning before Daniel/Mike session
- Use session to fill gaps and get expert perspective

---

*Created: 2026-05-01*  
*Source: [[00-Inbox/Kickdrum Prep from Confluence.md]]*  
*Next: Book Daniel/Mike prep session, block reading time Monday*
