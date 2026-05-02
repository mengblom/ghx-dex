# Architecture Discussion Backlog

*Purpose: Catalog architectural improvements, problems, and opportunities for incremental discussion and prioritization with team leadership and senior ICs.*

## Intent ##
- For each area, we (anyone with architecture inclinations/experience/authority)
	- should build a good understanding of where we are currently
	- an opinion on where we want to be
	- and ultimately how we should get there
	- how urgent it is

---
## Current Problem / Opportunity Areas
- Level set on current system
	- Overall architecture
	- Data volumes
		- Number of documents
		- Transactions per document
- General architecture north star ("meta" discussion)
	- More services vs monolith
	- No shared databases
	- More streaming vs batch architecture
- MongoDBs in General
	- Need to inventory and map dependencies at the DB level - i.e. which apps/services talk to each DB (maybe even at the collection level?)
	- Need to identify workloads that don't belong on the transactional DBs
		- Analytics workloads
		- ???
	- Need to identify / inventory poor usage patterns
		- Suboptimal queries
		- Missing indexes
		- Delete+Insert vs. Update
- EventBus (MongoDB)
	- MongoDB database used as an event bus
	- Should be replaced by a event / message queuing system that: 
		- leverages managed services (SQS, Kafka etc.)
		- provides an opinionated integration / usage pattern (i.e. has an internal SDK)
		- Provides native obervability & monitoring (i.e. insights into queue statistics), including correlation ID tracing between services
		- Has, or at least can be extended to, multi-region deployment, i.e. multi-region high-availability / disaster recovery
		- Allows for delayed retries (with backoff policies) without holding up the queue
		- 
- AuditDB (MongoDB)
	- Need to evaluate how we could store Activity Flow data (and other related data?) on cheaper, "infinitely" scalable storage (S3, DynamoDB etc.)
	- Are there aspects of the apps/use cases that rely on AuditDB that can/should be replaced/covered by an observability platform (Graylog as of now)?
- Breaking the monolith
	- What are reasonable short term goals?
- Observability
	- 7 day data retention - seems limiting?
	- How is our logging dicipline?
		- Granularity
		- Verbosity
		- Structured (vs. unstructured)
	- Proactive alerting
	- Is Graydog the right tool?
- Testing
	- Each team responsible for quality - make their own testing choices
	- Inverted test pyramid?
		- UI Tests
			- Our current suites of UI tests are extensive, brittle and expensive
			- Converting them to Playwright should help, but we should still ask ourselves
				- Do we need that high UI test coverage?
				- Should we need that high UI test coverage? Especially as we should be able to get unit test coverage very high very cheaply (AI)
		- Integration tests
			- What do we have?
	- PERF environment
		- Do we need it?
		- Has it ever "saved" us?
- Repo and Deployments
	- Bitbucket -> Github
	- 
- SSO
	- Homegrown IdP?
- Agile Process
- SDLC Metrics
- Feature Flags

## Current Problems

- Monolithic architecture with tight coupling forcing whole-system deployment
- Shared database dependencies causing cascading failures (SFTP/processing shouldn't fail when Audit DB down)
- EventBus MongoDB cluster instability (April 2026 incident)
- Batch processing (Data Poller) allowing surges to propagate through system
- Insufficient observability: 7-day log retention (Graylog), no batch failure alerting, discovered 1000s of invoice failures only after customer complaint
- Legacy testing framework (Tandoori) creating steep learning curve and maintenance friction
- Homegrown tools requiring specialized knowledge, lacking community support
- High cognitive load from large, coupled codebase with hidden dependencies
- Service-level health checks need improvement
- Slow build and deployment cycles impacting developer productivity

## Opportunities

- Migrate from EDI to modern canonical format (JSON) for mapping - improves developer experience and enables self-service
- Move to streaming architecture from batch processing
- Build proper event bus/queueing system to replace MongoDB-based event bus
- Activity Flow optimization (currently 188M docs/day written to MongoDB, deleted 3 days later - could use S3 directly with rehydration)
- Improve observability platforms: extend log retention, add proactive alerting
- Leverage crises as opportunities for deep architectural improvements rather than band-aids
- Adopt AI platform enablement model rather than centralized patterns (avoid repeating DevOps mistakes)

## Proposed Improvements

- Break database coupling to enable independent service deployment (highest priority)
- Modernize mapping tooling: evaluate IBM Sterling, Edifecs vs current Contivo (9+ years old)
- Replace MongoDB-based EventBus with proper queueing/eventing system
- Implement progressive backoff for SQS retry logic (current 10x retry without backoff hammers DB)
- Extend log retention beyond 7 days for incident investigation
- Improve service-level health checks and proactive monitoring
- Replace Tandoori with modern testing framework
- Systematically adopt industry-standard tools over homegrown alternatives
- Activity Flow sharding plan and diff engine for long-term scaling
- Continue monolith decomposition (RegCenter success model)

## SDLC & Delivery

- Vicious cycle: monolithic deployment → massive blast radius → extended testing → monthly releases → larger batches → more testing
- Monthly release cadence forces batching of changes
- Defensive posture due to high rollback/fix costs for monolithic deployments
- Difficulty achieving trusted automated test coverage at scale
- Merge conflicts and hidden dependencies create uncertainty about change impacts
- Steep learning curve for making changes safely
- Slow build and deployment cycles
- Need for more frequent, smaller deployments to break the cycle

## Tech Debt

- AWS SDK 2.0 migration (2 of 6 repos remaining)
- Linux 2023 upgrade (19 repos completed, ongoing)
- OSS vulnerability remediation (KEV, Critical, High severity)
- Tandoori testing framework replacement
- Custom-built tools maintenance burden
- Monolith decomposition (multi-quarter effort)
- Contivo mapping tool modernization (9+ years old)
- Infrastructure modernization: Bitbucket→GitHub, Bamboo→GitHub Actions, EC2→Containers (ongoing)
- EventBus architecture replacement
- Database coupling removal

## Recently Discussed

- EventBus MongoDB cluster incident (April 17, 2026) - highlighted need for proper event bus/queueing system
- Nanoclaw development and AI platform strategy (April 9, 2026) - enablement vs centralization
- Audit DB migration challenges (Q1 2026) - database dependency removal
- Feed Processor Observability platform success (Q1 2026) - real-time visibility model
- RegCenter decoupling from monolith (Q1 2026) - successful decomposition pattern with AI-assisted development
- Product-Engineering collaboration patterns (April 2026) - joint planning and commitment philosophy
- Monolith SDLC impact analysis (March 2026) - vicious cycle documentation
- MongoDB Atlas migrations (Q1 2026) - Archive DB success, Audit DB challenges 

---

**Next Steps:**
- [ ] Initial topic brainstorm session
- [ ] Group and prioritize topics
- [ ] Identify discussion leads for high-priority items