---
date: 2026-04-06
participants:
  - Mårten Engblom
companies: []
tags:
  - meeting
meeting_type: general
source: granola
granola_id: 5e5cac9a-e0b3-4ccd-84f3-344088881644
---

# Interview: Jeff Sherard for Principal Software Engineer - Data,  Data Architecture, AWS, Full stack or Backend

### Role Vision & The Data Gap

- Role created to bridge gap between DBAs (container/maintenance focus) and application engineers (ORM-heavy, no data layer ownership)
- Core problem: engineers default to ORM (Morphia, plain Java objects) with no query optimization instinct

- “Select star from everywhere and wonder why it’s slow”
- Works fine at 10 objects in dev; breaks at 6TB in prod
- Jeff’s framing: equivalent to a “Database Engineer” (DBE) role — application-side, focused on query writing, schema design, data modeling
- EA guidance too high-level to solve ground-level problems like the audit DB abuse

- EA says “transactional separated from reporting” — won’t tell you whether 188M audit records/day belong in Mongo

### Current State of the Data Estate

- ~8–9 Mongo clusters post-migration (Jeff’s view: shouldn’t need that many)
- Automation pod portfolio: Mongo, Elasticsearch, MySQL, Redis, DocumentDB, DynamoDB
- Other pods: self-hosted SQL Server on EC2 (Always On AGs), Oracle (Europe), various Mongo/Elastic implementations

- SQL Server → RDS or Postgres migration in discussion
- BT database alone has 66 collections, not all related to business documents
- Audit DB: 188M records/day, ~$100K/month — storing everything forever by default

- Root cause: “never lose a document” golden rule + customer demand for real-time 10-year access
- Estimate: ~10% of that data is actually meaningful

### Prioritized Approach Jeff Would Take

1. Full database fleet inventory — ownership, performance, scalability, usage patterns, risk hotspots
2. Continue migration and stabilization to hosted databases (Atlas, Elastic)
3. Optimization and modernization — get 10 years of data out of transactional stores

- Stream/offload to Common Data Platform (Snowflake) for reporting use cases
- Audit data: consider Elasticsearch for queryable fields → pointer to full doc stored in S3/file system
- MongoDB frozen tier / queryable backups as an intermediate step (rehydrates in ~10 min)
4. Microservice data layer split — e.g., audit breaking into mailbox statistics, notifications, etc.

- Risk: going too far → thousands of micro-databases with 10 records each, unmanageable to patch/maintain

### Jeff’s Background & Motivations

- Currently in shared services DB team: spans 9 pods, multiple DB technologies
- Active in AWS/Atlas/Elastic cost ops (monthly analysis with Steve Kirkpatrick)

- 70–80% of total AWS spend is Mårten’s org
- Manages GHX India offshore team and Happiest Minds managed services partner; mentoring Ali as successor
- Building “Project Jarvis” — AI operating system for infrastructure team using Claude Code
- Motivation for move: compensation (no bonus in current role), focus (laser on automation pod / CoreX), and market value alignment
- Willing to leave current responsibilities behind; sees Ali and Steve Kirkpatrick stepping up
- Interested in bringing AI ambassador role into the new org

### Next Steps

- Mårten Engblom

- Work with TA to set up abbreviated interview loop for Jeff
- Jeff Sherard

- Tell Sean (current manager) this afternoon that he and Mårten talked and the move is a real possibility

Chat with meeting transcript: https://notes.granola.ai/t/e569bf4f-9555-4386-9686-735fe1d29568

