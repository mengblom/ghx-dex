# Exchange Platform Architecture Roadmap

**Purpose:** High-level roadmap of architectural improvements to guide Q3/Q4 planning, Kickdrum conversations, and Architecture Forum discussions  
**Source:** [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]] - Comprehensive backlog of improvements  
**Owner:** Marten Engblom  
**Last Updated:** 2026-05-11

---

## Strategic Context

**Gen3 Vision (from Resiliency Future Plan):**
- Full microservices architecture
- No shared databases
- Event-driven architecture
- Multi-region deployment

**Current "Breaking the Monolith" Scope (Q2/Q3 2026):**
- Incremental decoupling (NOT full Gen3 redesign)
- Database dependency removal (highest priority)
- Service extraction using RegCenter success pattern
- Team autonomy through deployment independence

**Key Constraint:** Don't "overdo it" - make incremental progress toward Gen3 without attempting full rewrite

---

## Architecture Improvement Categories

### 1. Database Architecture & Dependencies 🔴 **CRITICAL PATH**

**Why Critical:** Shared database dependencies block team autonomy and cause cascading failures

#### MongoDB Usage Optimization
- **Current State:**
  - Multiple MongoDB databases with unclear usage patterns
  - Apps/services sharing databases (tight coupling)
  - Suboptimal queries, missing indexes, poor patterns (delete+insert vs update)
  
- **Target State:**
  - Each service owns its data
  - Clear inventory of which apps talk to which DBs
  - Optimized query patterns and indexes
  - Workloads matched to appropriate storage

- **Initiatives:**
  - [ ] **Inventory & map database dependencies** (at DB and collection level)
    - Which apps/services talk to each MongoDB?
    - Document read/write patterns by use case
    - Identify coupling that blocks deployment independence
  
  - [ ] **Identify workloads that don't belong on transactional DBs**
    - Analytics workloads → move to appropriate data warehouse
    - Archive data → S3 or cold storage
    - Audit/activity logs → optimized storage (S3, DynamoDB)
  
  - [ ] **Document poor usage patterns for remediation**
    - Suboptimal queries (missing correlation IDs, full table scans)
    - Missing indexes causing performance issues
    - Delete+Insert anti-patterns (should be Update)
    - Revisit MongoDB usage by use case: OLTP? OLAP? Document store? Cache?

#### EventBus Replacement
- **Current State:**
  - MongoDB database used as event bus
  - April 2026 incident highlighted fragility and operational risk
  - No native observability, correlation ID tracing, or retry backoff
  
- **Target State:**
  - Managed event/message queueing system (SQS, Kafka, or similar)
  - Internal SDK with opinionated patterns
  - Native observability with correlation ID tracing
  - Multi-region DR capability
  - Delayed retries with backoff policies
  
- **Initiatives:**
  - [ ] **Evaluate replacement options**
    - AWS SQS (simple, managed, lower cost)
    - Kafka (high throughput, event streaming, more complex)
    - Other managed services (EventBridge, SNS/SQS hybrid)
  
  - [ ] **Define migration strategy**
    - Parallel run of old and new systems
    - Incremental service migration
    - Rollback plan if issues arise
  
  - [ ] **Build internal SDK**
    - Opinionated integration patterns
    - Correlation ID propagation built-in
    - Retry logic with exponential backoff
    - Circuit breaker patterns

#### AuditDB Optimization
- **Current State:**
  - Activity Flow data: 188M docs/day written → deleted 3 days later
  - SFTP/processing fails when Audit DB down (coupling)
  - Expensive MongoDB storage for ephemeral data
  
- **Target State:**
  - Activity Flow data stored on cheaper, scalable storage (S3)
  - Rehydration capability when audit queries needed
  - Observability platform covers real-time monitoring needs
  - No cascading failures when Audit DB unavailable
  
- **Initiatives:**
  - [ ] **Activity Flow S3 migration**
    - Write directly to S3 instead of MongoDB
    - Implement rehydration for audit queries
    - Reduce MongoDB costs by 90%+ for this workload
  
  - [ ] **Replace audit use cases with observability**
    - Identify which AuditDB queries can be covered by Graylog
    - Move real-time monitoring to observability platform
    - Keep AuditDB for compliance/historical queries only

---

### 2. Compute Architecture & Processing 🟡 **HIGH PRIORITY**

#### Processing Engine Workload Optimization
- **Current State:**
  - Homegrown Processing Engine handling various workloads
  - Mix of batch, streaming, event-driven processing
  - EC2-based infrastructure (monolithic deployment)
  
- **Target State:**
  - Workloads matched to appropriate compute patterns
  - Serverless (Lambda) for event-driven, bursty workloads
  - Containers (ECS/EKS) for long-running services
  - Clear separation of batch vs streaming
  
- **Initiatives:**
  - [ ] **Inventory Processing Engine workloads**
    - Categorize by pattern: batch, streaming, event-driven, scheduled
    - Document current resource usage and scaling characteristics
    - Identify candidates for Lambda vs container migration
  
  - [ ] **Lambda migration strategy**
    - Event-driven workloads (triggered by SQS, S3 events)
    - Bursty workloads with unpredictable load
    - Short-lived processing tasks
  
  - [ ] **Container migration strategy**
    - Long-running services
    - Stateful workloads
    - Services requiring persistent connections

#### Batch Processing → Streaming Architecture
- **Current State:**
  - Data Poller batch processing allows surges to propagate
  - Monthly release cadence forces batching of changes
  - No backpressure or flow control
  
- **Target State:**
  - Streaming architecture with flow control
  - Progressive backoff and circuit breakers
  - Real-time processing with bounded queues
  
- **Initiatives:**
  - [ ] **Identify batch → streaming migration candidates**
    - Invoice processing pipeline
    - Data synchronization workloads
    - ETL processes
  
  - [ ] **Implement progressive backoff**
    - Replace "10x retry hammering DB" with exponential backoff
    - Circuit breaker patterns for degraded dependencies
    - Dead letter queues for permanent failures

---

### 3. Service Architecture & Monolith Decomposition 🟡 **HIGH PRIORITY**

#### Breaking the Monolith - Short Term Goals
- **Current State:**
  - Monolithic architecture with tight coupling
  - Whole-system deployment required for any change
  - High blast radius and defensive posture
  
- **Target State:**
  - Services with clear boundaries and ownership
  - Teams can deploy independently
  - Reduced blast radius and faster release cycles
  
- **Initiatives:**
  - [ ] **Define 3-5 specific Q3/Q4 deliverables** (for CJ)
    - Use RegCenter success pattern as model
    - Align with Gen3 vision but stay incremental
    - Document scope boundaries (what's NOT included)
  
  - [ ] **Identify next service extraction candidate**
    - Clear domain boundary
    - Low coupling to rest of monolith
    - High team ownership potential
  
  - [ ] **Document deployment independence criteria**
    - No shared database dependencies
    - Independent release cadence
    - Clear API contracts
    - Rollback capability without affecting other services

#### Service Boundaries & Team Ownership
- **Current State:**
  - Unclear service boundaries
  - Teams share code and databases
  - Merge conflicts and hidden dependencies
  
- **Target State:**
  - Clear service ownership by team
  - Teams control their deployment schedules
  - Well-defined APIs and contracts
  
- **Initiatives:**
  - [ ] **Define autonomous team criteria**
    - Service ownership (no shared services)
    - Data ownership (no shared databases)
    - Deployment independence (own CI/CD)
    - On-call ownership (you build it, you run it)

---

### 4. Observability & Incident Response 🟡 **HIGH PRIORITY**

#### Logging & Observability Improvements
- **Current State:**
  - 7-day log retention (Graylog) - limiting for incident investigation
  - No proactive alerting (discovered 1000s invoice failures via customer complaint)
  - Unclear logging discipline (granularity, verbosity, structured logs)
  
- **Target State:**
  - Extended log retention (30+ days minimum)
  - Proactive alerting before customers see issues
  - Structured logging with correlation IDs
  - Team-owned observability dashboards
  
- **Initiatives:**
  - [ ] **Extend log retention policy**
    - Evaluate Graylog capacity vs cost for 30-day retention
    - Consider tiered storage (hot logs 7 days, warm logs 30 days, cold logs 90+ days)
    - Document retention requirements by log type
  
  - [ ] **Implement proactive alerting**
    - Batch processing failure alerts
    - SLA breach warnings
    - Error rate thresholds
    - Performance degradation detection
  
  - [ ] **Evaluate Graylog vs alternatives**
    - Is Graylog the right long-term tool?
    - Consider: ELK stack, Datadog, Splunk, CloudWatch Logs Insights
    - Cost vs capability trade-offs
  
  - [ ] **Define observability ownership model**
    - Platform provides: log aggregation, metrics collection, APM
    - Teams own: service-specific dashboards, alerts, runbooks
    - Example: Feed Processor Observability success (Q1 2026)

#### Service Health Checks & Monitoring
- **Current State:**
  - Insufficient service-level health checks
  - Hard to distinguish service vs dependency failures
  
- **Target State:**
  - Each service exposes health check endpoint
  - Clear dependency health visibility
  - Automated health check validation in CI/CD
  
- **Initiatives:**
  - [ ] **Standardize health check implementation**
    - /health endpoint for liveness
    - /ready endpoint for readiness (includes dependencies)
    - Consistent response format across services

---

### 5. Testing Strategy & Quality 🟢 **MEDIUM PRIORITY**

#### Testing Framework Modernization
- **Current State:**
  - Tandoori testing framework (legacy, steep learning curve)
  - Inverted test pyramid: extensive UI tests, limited unit/integration tests
  - UI tests are brittle and expensive
  
- **Target State:**
  - Modern testing framework (Playwright for UI)
  - Proper test pyramid: many unit tests, some integration tests, few UI tests
  - AI-assisted test generation for high unit test coverage
  - Teams own their testing choices
  
- **Initiatives:**
  - [ ] **Replace Tandoori with modern framework**
    - Playwright for UI tests (reduce brittleness)
    - Jest/Vitest for unit tests (JavaScript/TypeScript)
    - Appropriate frameworks per language/service
  
  - [ ] **Reduce UI test coverage, increase unit test coverage**
    - Challenge: Do we need this much UI test coverage?
    - AI-assisted unit test generation (cheap, fast, reliable)
    - Focus UI tests on critical user journeys only
  
  - [ ] **Evaluate PERF environment**
    - Do we need it?
    - Has it ever "saved" us from production issues?
    - Cost vs value analysis

---

### 6. Infrastructure & Tooling 🟢 **MEDIUM PRIORITY**

#### Repository & Deployment Modernization
- **Current State:**
  - Bitbucket → GitHub migration in progress
  - Bamboo → GitHub Actions migration planned
  - EC2 → Containers migration ongoing
  
- **Target State:**
  - All repos in GitHub
  - GitHub Actions for CI/CD
  - Containerized deployments (ECS/EKS)
  
- **Initiatives:**
  - [ ] **Complete Bitbucket → GitHub migration**
    - Migrate remaining repos
    - Retire Bitbucket
  
  - [ ] **GitHub Actions CI/CD rollout**
    - Replace Bamboo pipelines
    - Standardized workflows across teams
  
  - [ ] **Container adoption acceleration**
    - EC2 → ECS/EKS for stateless services
    - Lambda for event-driven workloads

#### SSO & Identity Management
- **Current State:**
  - Homegrown IdP (GHX SSO)
  - Specialized knowledge required
  - Maintenance burden
  
- **Target State:**
  - Evaluate options: keep homegrown vs adopt managed (Auth0, Okta, Cognito)
  - Reduce maintenance burden
  - Improve security posture
  
- **Initiatives:**
  - [ ] **Evaluate homegrown IdP vs managed services**
    - Cost analysis (build vs buy)
    - Feature comparison
    - Migration effort estimation

---

### 7. Tech Debt & Compliance 🟢 **ONGOING**

#### Ongoing Tech Debt Initiatives
- **AWS SDK 2.0 migration:** 2 of 6 repos remaining
- **Linux 2023 upgrade:** 19 repos completed, ongoing
- **OSS vulnerability remediation:** KEV, Critical, High severity (continuous)
- **Contivo mapping tool modernization:** 9+ years old, evaluate IBM Sterling, Edifecs

---

## Tentative Timeline View

### Q3 2026 (Jul-Sep)

**Focus: Database decoupling and EventBus replacement foundation**

**Month 1 (July):**
- Complete database dependency inventory and mapping
- Evaluate EventBus replacement options (SQS vs Kafka)
- Define autonomous team criteria with leadership

**Month 2 (August):**
- Start Activity Flow S3 migration (AuditDB optimization)
- Begin EventBus SDK design and prototype
- First service extraction candidate identified

**Month 3 (September):**
- EventBus pilot migration (1-2 services)
- Processing Engine workload categorization complete
- Document lessons learned from service extraction

### Q4 2026 (Oct-Dec)

**Focus: Scaling migrations and improving observability**

**Month 1 (October):**
- EventBus migration accelerates (5-10 services)
- Lambda migration for first Processing Engine workloads
- Extended log retention (30 days) implemented

**Month 2 (November):**
- Second service extraction from monolith
- Proactive alerting rollout (batch processing, SLA monitoring)
- Container migration for long-running services

**Month 3 (December):**
- Q4 retrospective and lessons learned
- Q1 2027 roadmap refinement based on progress
- Celebrate wins and document architectural improvements

---

## Success Metrics

**Q3 2026 Goals:**
- [ ] Database dependency map complete (100% of services inventoried)
- [ ] EventBus replacement architecture selected and prototyped
- [ ] 1 service successfully extracted from monolith (following RegCenter pattern)
- [ ] Activity Flow S3 migration reduces MongoDB costs by 80%+
- [ ] Processing Engine workloads categorized (Lambda vs container candidates identified)

**Q4 2026 Goals:**
- [ ] 10+ services migrated to new EventBus (off MongoDB-based event bus)
- [ ] Log retention extended to 30 days
- [ ] 2-3 teams deploying independently (no monolith coupling)
- [ ] 5+ Processing Engine workloads migrated to Lambda or containers
- [ ] Proactive alerting catches 80%+ of issues before customer reports

**By End of 2026:**
- [ ] 50% reduction in monolith deployment dependencies
- [ ] Zero cascading failures due to AuditDB coupling
- [ ] 3+ services running on new EventBus architecture
- [ ] Observable improvement in release frequency (monthly → bi-weekly for decoupled services)

---

## Links to Detailed Plans

**Backlog (Comprehensive Topics):**
- [[06-Resources/Architecture/Architecture_Discussion_Backlog.md]] - Master backlog of all architectural improvements

**Related Projects:**
- [[04-Projects/Architecture_Forum_Launch/Architecture_Forum_Proposal.md]] - Forum structure and rollout plan
- [[04-Projects/CJ_Q2_Strategic_Deliverables/CJ_Strategic_Deliverables_Next_Week.md]] - Breaking the monolith deliverables for CJ

**Technical Context:**
- [[06-Resources/Architecture Principles and Anti-Patterns.md]] - Architectural friction to address
- [[04-Projects/Exchange Platform Architecture/Architecture Picture/Architecture Flaws, Improvement Areas.md]] - Known issues

**Recent Context:**
- Kickdrum Week 2 sessions (May 12-15, 2026) - External consultant validation and recommendations
- RegCenter decoupling (Q1 2026) - Success pattern for service extraction
- EventBus MongoDB incident (April 17, 2026) - Catalyst for replacement urgency

---

## Notes for Kickdrum Conversations

**Use this roadmap to:**
1. **Validate approach** - Are we prioritizing the right things?
2. **Get external perspective** - What have they seen work/fail at other companies?
3. **Refine timeline** - Are our estimates realistic?
4. **Identify gaps** - What are we missing?
5. **Challenge assumptions** - Are we thinking big enough (or too big)?

**Key questions for Kickdrum:**
- **Database dependencies:** Best practices for dependency mapping and breaking coupling?
- **EventBus replacement:** SQS vs Kafka for our use case (188M events/day)?
- **Service extraction:** How to sequence extractions for maximum team autonomy gain?
- **Observability:** What should teams own vs platform provide?
- **Processing Engine:** Lambda vs containers - decision framework?
- **MongoDB optimization:** When to stay on MongoDB vs migrate to different storage?

---

**Version:** 1.0  
**Created:** 2026-05-11  
**Next Review:** After Kickdrum Week 2 sessions (May 15, 2026)  
**Owner:** Marten Engblom
