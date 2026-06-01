# Thinktiv/Kickdrum Deep Dive - Exchange Architecture Topics

**Date Created:** 2026-05-01  
**Meeting Target:** Week of 2026-05-05  
**Experts:** [[Daniel_Milburn]], [[Mike_Mitchell]]

**Goal:** Get educated on Exchange architecture details before deep dives with Thinktiv/Kickdrum consultants.

---

## Your Meeting Responsibilities

### Session 1: Platform Architecture (Current State) - 90 min
**Role:** Attendee (with CJ, Bharat, Arshad, Greg Wilson)  
**Topics:**
- Logical architecture of each product/platform
- Technology stack of each product/platform
- Integration patterns between products and platforms

### Session 2: Platform-Enabling Services - 60 min
**Role:** Lead presenter for 3 of 4 topics  
**Your Topics:**
1. Identity, SSO, authentication, and authorization
2. Core UI/UX shared components
3. Intelligent Process Automation (IPA) capabilities

**Others' Topics:**
- Payments, BI, and observability (Tony M)
- Service consumption model across pods (owner unclear)

---

## Priority Prep for Your Sessions

### 🎯 Session 1: Platform Architecture (Current State)

**What you need to know:**

**Exchange Platform:**
- [ ] High-level logical architecture (monolith vs services)
- [ ] Technology stack: languages, frameworks, databases
- [ ] Deployment model: AWS regions, services, scaling approach
- [ ] Integration with other GHX products (how does Exchange connect to other platforms)

**Key Integration Patterns:**
- [ ] How documents flow in/out (SFTP, APIs, event-driven)
- [ ] How mapping works (Contivo/Smooks → Lambdas)
- [ ] How IPA integrates with Exchange processing pipeline
- [ ] How Visibility portal connects to backend services

**Questions to ask Daniel/Mike:**
- What diagram(s) best show Exchange architecture at a high level?
- What are the most common integration patterns we use?
- Where do we deviate from standard patterns and why?
- What should I emphasize vs gloss over in this session?

---

### 🎯 Session 2: Platform-Enabling Services (YOU'RE PRESENTING!)

**Topic 1: Identity, SSO, Authentication & Authorization** ⚠️ Mike Mitchell owns this

**What you need to know:**
- [ ] Current identity provider (Okta? Internal?)
- [ ] SSO implementation (SAML, OAuth, OIDC?)
- [ ] How users authenticate to Exchange/Visibility portal
- [ ] Authorization model (RBAC? Claims-based?)
- [ ] Where user/org data is stored (Mike's teams own this)
- [ ] Integration with customer identity systems
- [ ] Multi-tenancy isolation approach

**Questions for Mike:**
- Walk me through the authentication flow for a typical user
- How do we handle authorization across Exchange services?
- What's the current state vs ideal state for identity management?
- Known pain points or tech debt in this area?
- How does this tie into the User Platform and Org Platform teams?

---

**Topic 2: Core UI/UX Shared Components** ⚠️ Visibility Team context

**What you need to know:**
- [ ] What shared UI components exist (design system, component library?)
- [ ] Which teams use these components (just Visibility or broader?)
- [ ] Technology stack (Angular, React, Vue?)
- [ ] How components are distributed (npm, monorepo?)
- [ ] Governance: who owns and maintains shared components
- [ ] Theming and customization capabilities
- [ ] Accessibility compliance

**Questions for Daniel (Visibility Team):**
- What UI component library or design system do we use?
- How standardized are our UI patterns across Exchange?
- What's reusable vs team-specific UI code?
- Are there shared UI components that other GHX products could use?

---

**Topic 3: Intelligent Process Automation (IPA)** ⚠️ IPA Team context

**What you need to know from your vault:**
- [ ] History: $5M FirstSource cost savings initiative
- [ ] Scope: ~300 customers, PO and Invoice digitization
- [ ] Automation rates: GFax 45-50%, Invoicing 15%
- [ ] How IPA became part of value prop (not just cost savings)

**What you need to know from experts:**
- [ ] IPA technical architecture (OCR, classification, human-in-loop)
- [ ] How IPA integrates with Exchange document processing
- [ ] What services/capabilities are exposed to other products
- [ ] Reusability: Can IPA be used outside Exchange?
- [ ] Consumption model: How would other teams use IPA?
- [ ] Roadmap: Where is IPA heading?

**Questions for IPA team lead:**
- Walk me through IPA architecture from document ingestion to enrichment
- What services/APIs does IPA expose?
- How could other GHX products leverage IPA capabilities?
- What's the ideal consumption model for IPA as a shared service?

---

**Topic 4 (Bonus): Service Consumption Model Across Pods**

**What you might need to address:**
- [ ] How do teams/pods consume shared services today?
- [ ] API gateway or service mesh approach?
- [ ] Service discovery and routing
- [ ] Versioning and backward compatibility strategy
- [ ] Rate limiting, quotas, SLAs for shared services
- [ ] Documentation and onboarding for service consumers

**Questions:**
- Do we have a standard pattern for service consumption?
- How do teams discover and integrate with shared services?
- Who defines the consumption model (platform team, each service owner)?

---

## Comprehensive Reference Topics (for deeper dives)

## 1. Core Exchange Platform Architecture

### High-Level System Design
- [ ] Overall system topology and data flow
- [ ] Service boundaries and responsibilities
- [ ] Integration points (internal and external)
- [ ] Request/response vs event-driven patterns
- [ ] Deployment architecture (regions, availability zones)

### Monolith Characteristics
- [ ] Current monolith scope and boundaries
- [ ] Deployment model and cadence
- [ ] Coupling points and dependencies
- [ ] Why breaking the monolith is hard (technical blockers)
- [ ] Current blast radius of deployments

---

## 2. Database Architecture & Dependencies

### Database Landscape
- [ ] List of all databases used by Exchange
- [ ] Which services/teams own which databases
- [ ] Shared database anti-patterns (who shares what)
- [ ] Database sizing and performance characteristics

### Critical Dependencies
- [ ] Audit DB dependencies (why SFTP and processing depend on it)
- [ ] MongoDB usage patterns (ActivityFlow 188M docs/day pattern)
- [ ] Why we can't deploy services independently due to DB coupling
- [ ] Data retention and archival patterns (MongoDB → S3)

### Data Ownership & Boundaries
- [ ] Which teams should own which data
- [ ] Current vs ideal data ownership model
- [ ] Cross-team data access patterns
- [ ] Impact of shared schemas on autonomy

---

## 3. Team Structure & Responsibilities

### Current Teams (from Architecture Picture)
- [ ] **Mapping Team**: Actions, Contivo/Smooks maps, Lambda conversions
- [ ] **IPA Team**: Document digitization, GFax, Invoice automation
- [ ] **Visibility Team**: Self-service portal, Angular/Tomcat/SpringBoot
- [ ] **Doc Enrichment Team**: Rules engine, actions framework, IBR, Odin, Complex Ordering

### Team Autonomy Gaps
- [ ] What prevents teams from deploying independently
- [ ] Shared codebases vs team ownership
- [ ] Cross-team coordination requirements
- [ ] Skills gaps or knowledge silos

---

## 4. Integration Patterns & Data Exchange

### Document Processing Pipeline
- [ ] Inbound document flow (SFTP → processing → enrichment)
- [ ] Outbound document flow
- [ ] File identification and routing
- [ ] Document types and formats (EDI X12, XML, JSON)

### Mapping & Transformation
- [ ] Contivo vs Smooks maps (when to use which)
- [ ] Current canonical format strategy (X12 as default)
- [ ] Modernization opportunity (JSON as canonical)
- [ ] Map compilation and execution (Lambdas vs monolith)
- [ ] Self-service mapping vision

### Actions Framework
- [ ] What actions are and how they execute
- [ ] Lambda-converted actions (5 so far)
- [ ] Special action that wraps maps
- [ ] Processing Engine execution model

---

## 5. Operational Challenges

### Observability & Monitoring
- [ ] Current logging retention (7 days in Graylog)
- [ ] Alerting gaps (batch failures not caught)
- [ ] Service health check maturity
- [ ] How incidents are detected (customer complaints vs proactive)

### Batch Processing Issues
- [ ] Data Poller and batch patterns
- [ ] Why batches propagate surges through the system
- [ ] Event streaming opportunities

### Resilience & Recovery
- [ ] Current DR capabilities
- [ ] Rollback complexity for monolith
- [ ] Recovery time objectives (RTOs)
- [ ] Impact of database dependencies on recovery

---

## 6. Development Friction & Tooling

### Build & Deploy
- [ ] Build times for monolith
- [ ] Deployment process and coordination
- [ ] Testing requirements before deploy
- [ ] CI/CD pipeline maturity

### Testing Challenges
- [ ] Tandoori testing framework issues
- [ ] Automated test coverage gaps
- [ ] Why manual testing is still required
- [ ] Slow test execution times

### Developer Experience
- [ ] Cognitive load of working in the monolith
- [ ] Onboarding new engineers (time to productivity)
- [ ] Homegrown components that require specialized knowledge
- [ ] Standard tooling adoption vs NIH syndrome

---

## 7. Modernization & Migration Strategy

### Breaking the Monolith
- [ ] Sequencing strategy (which services first)
- [ ] Domain-driven design boundaries identified
- [ ] Migration approach (strangler fig vs big bang)
- [ ] Success metrics for autonomous teams

### Technical Debt Priorities
- [ ] Database dependency removal roadmap
- [ ] Mapping solution modernization (Contivo replacement)
- [ ] Batch → stream processing migration
- [ ] Observability improvements

### Complex Ordering (Commercial Roadmap)
- [ ] Doc Enrichment team involvement
- [ ] DREF extraction from monolith
- [ ] TPM user data dependencies

---

## 8. IPA (Intelligent Process Automation)

### Current State
- [ ] History: $5M FirstSource cost savings
- [ ] Scope: ~300 customers for PO and Invoice digitization
- [ ] Automation rates: GFax 45-50%, Invoicing 15%
- [ ] How IPA fits into value proposition (beyond cost savings)

### Technical Architecture
- [ ] Document ingestion pipeline
- [ ] OCR and classification technology
- [ ] Human-in-the-loop workflows
- [ ] Integration with Exchange processing

---

## 9. Security & Compliance

### Access Control
- [ ] How customer data is isolated
- [ ] Role-based access control (RBAC) maturity
- [ ] Audit trail capabilities

### Vulnerability Management
- [ ] Current vulnerability backlog (Project Red Mythos context)
- [ ] Patching cadence and constraints
- [ ] Security debt priorities

---

## 10. Organizational & Process Context

### Delivery Challenges
- [ ] Monthly release cadence drivers
- [ ] Why can't we release more frequently
- [ ] Commercial roadmap vs tech debt balance
- [ ] Resourcing constraints (40+ open roles)

### Leadership Guidance
- [ ] Curtis's directive: "provide if you have it, don't create artifacts"
- [ ] Visibility expectations (Aha/roadmap/Jira initiative)
- [ ] Strategic pivots from India trip (AI Native SDLC, team autonomy)

---

## Questions to Ask Daniel & Mike

1. What are the top 3 things Thinktiv/Kickdrum will want to dive deep on?
2. Where do we have good documentation vs gaps?
3. What questions stumped us in past architecture reviews?
4. Which database dependencies are the most painful to untangle?
5. What's the realistic timeline for breaking apart the monolith?
6. Where are the biggest knowledge silos (bus factor = 1)?
7. What keeps you up at night about Exchange architecture?

---

## Preparation Checklist

- [ ] Schedule 90-min session with Daniel and Mike
- [ ] Review this topics list together
- [ ] Identify which topics need documentation/diagrams
- [ ] Assign prep work (who researches what)
- [ ] Create a "known unknowns" list for Thinktiv/Kickdrum
- [ ] Build a FAQ document from this session
- [ ] Share context with team leads before consultant engagement

---

*Next: Book meeting with Daniel and Mike for week of 2026-05-05*
