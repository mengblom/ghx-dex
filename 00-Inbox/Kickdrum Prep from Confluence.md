Results from the prompt in [[Confluence_Rovo_Search_Prompt]].

Here's a comprehensive documentation guide organized by your four deep-dive topics. I've prioritized architecture diagrams, technical design docs, and API documentation as requested.

---

## 1. Exchange Platform Architecture

### Core Architecture Documents

[**Exchange Architecture Diagrams**](https://prd.hub.ghx.com/wiki/spaces/SRE/pages/1180991550/Exchange+Architecture+Diagrams "https://prd.hub.ghx.com/wiki/spaces/SRE/pages/1180991550/Exchange+Architecture+Diagrams") ⭐ — _The single best starting point._ Contains the canonical Exchange Data Flow Diagram (source of truth), High-Level Architecture diagram, and Document Lifecycle diagram. Covers IO Engine, Processing Engine, Eventbus MongoDB coordination layer, and downstream systems (MEX, Heimdall, Registration Center, eInvoicing).

[**CoreX Architecture Review - 2023 Update**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28796788/CoreX+Architecture+Review+-+2023+Update "https://prd.hub.ghx.com/wiki/spaces/dev/pages/28796788/CoreX+Architecture+Review+-+2023+Update") ⭐ — Comprehensive technical review covering the event-driven architecture, all CoreX components (Engine-PE, Engine-IO, Engine-DataPoller, Engine-Jobs, Engine-EINV, Heimdall), configured frameworks per component, and the full technology inventory (Java, MongoDB, MySQL, Redis, Elasticsearch, GraphQL, Quartz, Smooks, New Relic).

[**GHX CoreX Application Understanding Document-DRAFT**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28784630/GHX+CoreX+Application+Understanding+Document-DRAFT "https://prd.hub.ghx.com/wiki/spaces/dev/pages/28784630/GHX+CoreX+Application+Understanding+Document-DRAFT") — Broader overview with System Context Diagram, functional components (Org Management, Account Management, User Management), transactional components (TPM, Rules Engine, DREV, Data Poller, IBR), and frameworks (Adapters, Event Broker, Audit, SSO, Search, Scheduler).

[**Exchange Platform - ITSM Operator Guide**](https://prd.hub.ghx.com/wiki/spaces/IE/pages/1216053256/Exchange+Platform+-+ITSM+Operator+Guide "https://prd.hub.ghx.com/wiki/spaces/IE/pages/1216053256/Exchange+Platform+-+ITSM+Operator+Guide") — Distinguishes **CoreX** (EDI transaction processing) from **Exchange Platform** (user interfaces, job scheduling, data management). Covers My Exchange, Batch Processing, Data Poller, Document Store, SFTP/Mailbox, Registration Center. Includes infrastructure details (AWS US/EU, MongoDB cluster, Elasticsearch 7.4.2).

### Technology Stack & Data Stores

- **Languages**: Java (primary), Python (IPA/ML), AngularJS/Angular (frontend)
    
- **Databases**: MongoDB (BT/BD, Eventbus, Audit), MySQL (TPM), Elasticsearch (Activity Flow, Business Transaction search), Amazon S3 (document storage)
    
- **Infrastructure**: AWS (EC2, S3, SQS, ECS, Lambda, API Gateway), New Relic (monitoring), Redis (caching)
    
- **Frameworks**: Spring Security, Quartz Scheduler, Smooks (transformation), GraphQL
    

### Monolith vs. Microservices

[**Resiliency Future Plan - April 2025**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/296812545/Resiliency+Future+Plan+-+April+2025 "https://prd.hub.ghx.com/wiki/spaces/EA/pages/296812545/Resiliency+Future+Plan+-+April+2025") — Documents the current monolithic architecture and the vision for Gen3 microservices. Notes: "Not trying to re-architecture the Exchange (i.e. re-design EventBus or move to micro-services). Those type efforts are for Gen3." The vision includes domain-based microservices, serverless, eventual consistency, and the GHX App Platform.

[**Exchange Disaster Recovery Analysis**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/33880466/Exchange+Disaster+Recovery+Analysis "https://prd.hub.ghx.com/wiki/spaces/EX/pages/33880466/Exchange+Disaster+Recovery+Analysis") — Lists all CoreX engines as "Monolith Web App" with EC2 Blue Green deployment in us-east-1 with Pilot Light DR in us-west-2. The **Contivo Standalone (CSA)** framework is noted as "java based lambda micro-services" offloading transformation from the monolith.

### Integration Patterns

[**EGX Event Bus Architecture**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/33887628/EGX+Event+Bus+Architecture "https://prd.hub.ghx.com/wiki/spaces/EX/pages/33887628/EGX+Event+Bus+Architecture") — Describes the SOA2 event-based processing model using typed immutable events, the EEB framework for publishing/dispatching, and service component collaboration patterns.

[**Fusion Platform**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/642450005/Fusion+Platform "https://prd.hub.ghx.com/wiki/spaces/EA/pages/642450005/Fusion+Platform") — Covers Fusion Connect (on-prem ERP integration), Fusion Streams (cloud ERP integration via APIs), and Fusion Gateway (API gateway for customer ERPs to access GHX APIs).

[**VA Architecture Overview**](https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=976519201&preview=%2F976519201%2F976520059%2FVA+architecture+overview+02202024.pptx "https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=976519201&preview=%2F976519201%2F976520059%2FVA+architecture+overview+02202024.pptx") — Shows GHX high-level solution architecture, VA isolated instance in AWS GovCloud, and deployment considerations.

---

## 2. Identity, SSO, and Authentication

### Primary Architecture Documents

[**Workforce Identity Management**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/39166013/Workforce+Identity+Management "https://prd.hub.ghx.com/wiki/spaces/EA/pages/39166013/Workforce+Identity+Management") ⭐ — EA-level overview of the two identity services: **Okta** ([ghxsso.okta.com](http://ghxsso.okta.com/ "http://ghxsso.okta.com"), primarily SAML for GHX corporate apps) and **GHX Identity Service** ([login.ghx.com](http://login.ghx.com/ "http://login.ghx.com"), OpenID Connect reference implementation). Covers authentication, authorization (RBAC preferred over ACL), SAML, OpenID Connect definitions, and workforce service identities with token endpoint details.

[**GHX SSO**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/646840321/GHX+SSO "https://prd.hub.ghx.com/wiki/spaces/EA/pages/646840321/GHX+SSO") ⭐ — EA landscape page for GHX Identity Service. Supports SAML-based multi-tenant federation, OIDC for authentication, OAuth2 for authorization. Contains landscape/logical system diagram link. Technical owners: Daniel Milburn, Prashanth Garlapati.

[**GHX - Identity Service**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/28848020/GHX+-+Identity+Service "https://prd.hub.ghx.com/wiki/spaces/EX/pages/28848020/GHX+-+Identity+Service") ⭐ — Detailed technical documentation covering OpenID Connect implementation (MITREid-based, Spring Security, Nimbus JOSE & JWT), OAuth 2.0 flows, assumptions (TPM as Identity Management System, Active Directory for internal users), and supported scopes (openid, profile, email, plus custom scopes like ldap_access, userInfo, roles, orgid, eid).

### Okta & SAML Integration

[**GHX and Okta Integration Documentation**](https://prd.hub.ghx.com/wiki/spaces/IS/pages/25059137/GHX+and+Okta+Integration+Documentation "https://prd.hub.ghx.com/wiki/spaces/IS/pages/25059137/GHX+and+Okta+Integration+Documentation") — Covers Okta as cloud access management platform providing SSO via SAML, Adaptive MFA, and activity reporting. Includes SAML application configuration details, attribute mapping, and metadata exchange processes.

[**GHX Okta using SAML 2.0 protocol**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/28881272/GHX+Okta+using+SAML+2.0+protocol "https://prd.hub.ghx.com/wiki/spaces/EX/pages/28881272/GHX+Okta+using+SAML+2.0+protocol") — Deep technical documentation on Spring Security SAML Extension integration, IDP-initiated vs SP-initiated SSO flows, metadata configuration, and Maven dependency details.

[**External Identity Provider setup in GHX SSO Portal**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/28969844/External+Identity+Provider+setup+in+GHX+SSO+Portal "https://prd.hub.ghx.com/wiki/spaces/EX/pages/28969844/External+Identity+Provider+setup+in+GHX+SSO+Portal") — Step-by-step guide for configuring external IDPs (Okta, Azure AD) with GHX SSO, including SAML metadata, entity ID, attribute mapping (firstName, lastName, email, organizationId, GROUP_ROLE), and IDP management flags.

[**Identity Federation**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/29062631/Identity+Federation "https://prd.hub.ghx.com/wiki/spaces/EX/pages/29062631/Identity+Federation") — Analysis of federated identity approaches (OIDC auth code flow, SAML, trust chains), architectural design diagrams for existing and proposed auth flows, and comparison table of OAuth 2.0 vs OpenID Connect vs SAML.

[**GHX SSO - SAML IDP Provider**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/632913951/GHX+SSO+-+SAML+IDP+Provider "https://prd.hub.ghx.com/wiki/spaces/EX/pages/632913951/GHX+SSO+-+SAML+IDP+Provider") — Technical implementation for GHX SSO acting as a SAML IDP for external applications (e.g., Madcap Flare Online), including design steps, SQL scripts for product/role setup, and SAML client integration steps.

### Authorization & Tenancy

[**EA RBAC and Authorization Inventory**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/39166997/EA+RBAC+and+Authorization+Inventory "https://prd.hub.ghx.com/wiki/spaces/EA/pages/39166997/EA+RBAC+and+Authorization+Inventory") — Enterprise-level RBAC model with Bronze/Silver/Gold tiers. Key principle: permissions granted by roles are always restricted to access within a specific tenant. Defines role hierarchy patterns and data classification-based access.

[**Tenancy Model**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/39165324/Tenancy+Model "https://prd.hub.ghx.com/wiki/spaces/EA/pages/39165324/Tenancy+Model") ⭐ — Describes GHX's SaaS tenancy model: tenant determined at login via JWT (agent tuple with organization EID), TPM database as tenant store, subscribed product parameters for per-tenant config, single-user multi-tenant support via alternate organization roles.

[**Authentication & Authorization Process**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/82969163/Authentication+Authorization+Process "https://prd.hub.ghx.com/wiki/spaces/EX/pages/82969163/Authentication+Authorization+Process") — Covers Spring Security authentication flow, JSESSIONID session management, and SSO process using OpenID protocol with OIDCClientAuthenticationFilter.

[**GHX Product Subscription and SSO Access**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/28968372/GHX+Product+Subscription+and+SSO+Access "https://prd.hub.ghx.com/wiki/spaces/EX/pages/28968372/GHX+Product+Subscription+and+SSO+Access") — Documents the product subscription → role mapping → SSO client flow. Explains how roles, products, SSO clients, and product role mappings connect to determine user access after authentication.

[**User Management**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/29123935/User+Management "https://prd.hub.ghx.com/wiki/spaces/dev/pages/29123935/User+Management") — Details on domain roles (User, Customer Administrator, Manager, Admin), product roles (Access, Redacted Access, Manage, GHX_Admin), internal/external role flags, and organization selector logic.

---

## 3. UI/UX Shared Components

### Core Design System

[**CoreUI**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/645398551/CoreUI "https://prd.hub.ghx.com/wiki/spaces/EA/pages/645398551/CoreUI") ⭐ — EA landscape page. CoreUI is a design system consisting of standards and guidelines for GHX products, packaged as an **Angular library** (`@ghx/ui-core`). Provides SSO integration, headers, footers, tables, custom Angular Material components, theming. 20+ applications leveraging it. Technical owner: Anthony Middleton. Live documentation: [coreui.ghx.com](http://coreui.ghx.com/ "http://coreui.ghx.com").

[**CoreUI Components and Community**](https://prd.hub.ghx.com/wiki/spaces/CDM/pages/352747688/CoreUI+Components+and+Community "https://prd.hub.ghx.com/wiki/spaces/CDM/pages/352747688/CoreUI+Components+and+Community") — Defines CoreUI as a "one-stop shop for all front-end design and development needs." Built from Angular Material, provides reusable components, styling, and examples. Covers benefits for designers, developers, PMs, and trainers.

[**CoreUI References and Best Practices**](https://prd.hub.ghx.com/wiki/spaces/EBI/pages/1171423237/CoreUI+References+and+Best+Practices "https://prd.hub.ghx.com/wiki/spaces/EBI/pages/1171423237/CoreUI+References+and+Best+Practices") ⭐ — Module inventory:

|   |   |   |
|---|---|---|
|Module|Package|Description|
|Common|@ghx/ui-core/common|Shared utilities, components, directives, pipes, services|
|Core|@ghx/ui-core/core|Application shell (header, footer, sidebar, breadcrumbs)|
|Ag-Table|@ghx/ui-core/ag-table|Data tables with ag-grid|
|Chart|@ghx/ui-core/chart|Vega-Lite charts with GHX theme|
|Chat|@ghx/ui-core/chat|Chat/Copilot UI components|
|Forms|@ghx/ui-core/forms|Form components and validators|
|Security|@ghx/ui-core/security|OIDC authentication, guards|
|File|@ghx/ui-core/file|File viewers and diff tools|
|Dashboard|@ghx/ui-core/dashboard|Dashboard tiles and Looker embeds|

### Frontend Tech Stack Documentation

[**Frontend Application Tech Stack**](https://prd.hub.ghx.com/wiki/spaces/NEX/pages/893059503/Frontend+Application+Tech+Stack "https://prd.hub.ghx.com/wiki/spaces/NEX/pages/893059503/Frontend+Application+Tech+Stack") ⭐ — Comprehensive tech stack for newer Angular SPAs: Angular 21, TypeScript with Strict Mode, Angular Signals for state management, Vite-based builds. **UI hierarchy**: GHX Core-UI (first) → Angular Material (fallback) → TailwindCSS (utility). Authentication via Okta with OIDC/OAuth 2.0 (redirect-based PKCE flow). Testing with Vitest, minimum 80% coverage.

[**Frontend Application Design**](https://prd.hub.ghx.com/wiki/spaces/NEX/pages/893092062/Frontend+Application+Design "https://prd.hub.ghx.com/wiki/spaces/NEX/pages/893092062/Frontend+Application+Design") — Detailed frontend architecture guidelines covering hexagonal architecture adaptation, zoneless vs Zone.js decisions (Zone.js required for Core-UI compatibility), component patterns with Signals, and testing strategy.

[**MEX UI – Coding & Code Review Standards**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/1202913290/MEX+UI+Coding+Code+Review+Standards "https://prd.hub.ghx.com/wiki/spaces/EX/pages/1202913290/MEX+UI+Coding+Code+Review+Standards") — MEX Notifications UI (Angular 20.x) standards. Uses `@ghx/ui-core` and `@ghx/mex-ui-core`, ag-grid-angular, NgRx for state management. Includes project structure, naming conventions, and security standards.

[**CoreUI News and Roadmap**](https://prd.hub.ghx.com/wiki/spaces/CDM/pages/31993026/CoreUI+News+and+Roadmap "https://prd.hub.ghx.com/wiki/spaces/CDM/pages/31993026/CoreUI+News+and+Roadmap") — Angular 14→15 upgrade path, starter application reference, toolkit site, and ChatGHX integration.

[**Core UI Tech Talk - Mar 2022**](https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=28812062&preview=%2F28812062%2F28855062%2FCore+UI+Tech+Talk+-+Mar+2022.pptx "https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=28812062&preview=%2F28812062%2F28855062%2FCore+UI+Tech+Talk+-+Mar+2022.pptx") — Presentation covering CoreUI modules (Common, Core, Security, Forms, AgTable, Files), 13 apps across 5 teams, npm package `@ghx/ui-core`, theming capabilities, Figma migration, design token/Style Dictionary approach, and accessibility roadmap.

[**BIAP × einvoice-invosight-ui × ui-core Component Usage Analysis**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/1139933191/BIAP+einvoice-invosight-ui+ui-core+Component+Usage+Analysis "https://prd.hub.ghx.com/wiki/spaces/dev/pages/1139933191/BIAP+einvoice-invosight-ui+ui-core+Component+Usage+Analysis") — Real-world analysis of Core-UI adoption: BIAP (533 components, 735 files using ui-core) vs InvoSight (15 components, 21 files using ui-core).

[**Design 101**](https://prd.hub.ghx.com/wiki/spaces/GHXH/pages/75794557/Design+101 "https://prd.hub.ghx.com/wiki/spaces/GHXH/pages/75794557/Design+101") — Design principles and CoreUI overview for non-developers. CoreUI toolkit link included.

---

## 4. Intelligent Process Automation (IPA)

### Architecture & Technical Design

[**IPA**](https://prd.hub.ghx.com/wiki/spaces/EA/pages/655818795/IPA "https://prd.hub.ghx.com/wiki/spaces/EA/pages/655818795/IPA") ⭐ — EA landscape page. IPA combines RPA with AI, powered by **UiPath** cloud-based automation platform. Key pillars: **GFax** (PO classification & data extraction), **PriceSync** (automated weekly price exception decks), **eInvoicing** (invoice classification, validation, transformation to EDI 810), **MSOT** (UI automation for email correlation and PO acknowledgments).

[**IPA - The rise of the robots!**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28818433/IPA+-+The+rise+of+the+robots "https://prd.hub.ghx.com/wiki/spaces/dev/pages/28818433/IPA+-+The+rise+of+the+robots") ⭐ — Mission statement, goals, technology platform overview, partnership with Global Logic and UiPath. Contains technology platform diagram and roadmap.

**IPA Production Architecture** ([attachment](https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=28852907&preview=%2F28852907%2F28832544%2FIPA-ProductionArchitecture+%5BAutosaved%5D.pptx "https://prd.hub.ghx.com/wiki/pages/viewpageattachments.action?pageId=28852907&preview=%2F28852907%2F28832544%2FIPA-ProductionArchitecture+%5BAutosaved%5D.pptx")) ⭐ — Production architecture diagram and component inventory:

|   |   |   |
|---|---|---|
|Component|Purpose|Technologies|
|Orchestrator|RPA code management, scheduling|UiPath Cloud Orchestration|
|Robot Server|RPA code execution|UiPath Robot, Windows Server, AWS EC2|
|GFax/Image API|OCR, classification, keyword filtering, PHI/CC detection|Python, Tesseract (ML/OCR), ECS, Stoplight|
|IPA Journal|Reporting and logs|Elasticsearch (AWS Managed), Kibana|
|IPA Configuration|Config storage|DynamoDB|
|App Integration|CoreX integration|AWS S3, AWS SQS|

### Document Processing Pipeline

[**IPA GFax Classification & Keyword APIs**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28836386/IPA+GFax+Classification+Keyword+APIs "https://prd.hub.ghx.com/wiki/spaces/dev/pages/28836386/IPA+GFax+Classification+Keyword+APIs") ⭐ — Technical API documentation covering the PO Classification API (10-step pipeline: page length check → OCR/ML extraction → language detection → PO number extraction → PHI detection → CC detection → T&C filtering → keyword rejection → PO validation → results return). Includes API inputs, response schema, configuration details (DynamoDB, UiPath Orchestrator assets), and example JSON responses.

[**IPA PO Classification and Keyword Validation**](https://prd.hub.ghx.com/wiki/spaces/EX/pages/1002045650/IPA+PO+Classification+and+Keyword+Validation "https://prd.hub.ghx.com/wiki/spaces/EX/pages/1002045650/IPA+PO+Classification+and+Keyword+Validation") — CoreX action integration class for IPA. Documents the processing flow, child flow GFXML structure, context items, and the two-stage validation (classification → keyword rejection).

[**G-Fax NA Full Automation**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/28910771/G-Fax+NA+Full+Automation "https://prd.hub.ghx.com/wiki/spaces/dev/pages/28910771/G-Fax+NA+Full+Automation") ⭐ — Phase-by-phase scope of GFax full automation. Phase 1: Top 20 formats, 98.7%+ OCR accuracy via UiPath AI Center, 75-attribute PO data model, Account Lookup via MyOrg API, content enrichment. Phase 1.5: Expansion to >100 formats with >60% capture goal.

[**IPA - eInvoicing Process**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/151585738/IPA+-+eInvoicing+Process "https://prd.hub.ghx.com/wiki/spaces/dev/pages/151585738/IPA+-+eInvoicing+Process") — eInvoicing pillar documentation. Pipeline: OCR → Validation → Enrichment → CoreX Mapper → EDI 810. Covers pre-validation checks, invoice verification, PO/vendor lookups, data enrichment, and business rules.

[**E-Invoicing Process**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/505512249/E-Invoicing+Process "https://prd.hub.ghx.com/wiki/spaces/dev/pages/505512249/E-Invoicing+Process") — Detailed overview of the provider e-invoicing flow: pre-validation, invoice verification, PO & vendor lookups, data enrichment, and the goal to automate using IPA/ML/AI.

### Metrics & Performance Targets

- **GFax OCR accuracy**: 98.7%+ via UiPath AI Center
    
- **eInvoicing field accuracy target**: 90% field extraction, 98% correct placement
    
- **GFax processing SLA**: 10-15 minutes per transaction
    
- **eInvoicing throughput target**: 2,000 documents/hour, 12,000 full automation within 12-hour SLA
    
- **GFax capture target**: >60% of volume automated (Phase 1.5)
    

[**IPA: Addressing Technical Debt**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/481788726/IPA+Addressing+Technical+Debt+for+Future+Scalability+and+Compliance "https://prd.hub.ghx.com/wiki/spaces/dev/pages/481788726/IPA+Addressing+Technical+Debt+for+Future+Scalability+and+Compliance") — Covers IPA's evolution from 2020-21 startup-mode to the current need for engineering rigor, security governance, and scalability improvements.

[**Beyond Automation — Misaligned Responsibilities**](https://prd.hub.ghx.com/wiki/spaces/dev/pages/1046642754/Beyond+Automation+How+Misaligned+Responsibilities+Are+Limiting+IPA+s+Potential "https://prd.hub.ghx.com/wiki/spaces/dev/pages/1046642754/Beyond+Automation+How+Misaligned+Responsibilities+Are+Limiting+IPA+s+Potential") — Analysis showing data ingestion and business rules consume >45% of IPA engineering bandwidth, with a recommendation to refocus on core document classification/extraction capabilities.

---

This should give your consultants a strong foundation across all four areas. Would you like me to create a Confluence page compiling these references, or dive deeper into any specific topic area?

![confluence](https://prd.hub.ghx.com/gateway/api/assist/rovo/v1/resources/icon/confluence)

![jira](https://prd.hub.ghx.com/gateway/api/assist/rovo/v1/resources/icon/jira)

128 Sources