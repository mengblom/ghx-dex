---
tags:
  - interview-questions
  - principal-engineer
  - data-architecture
candidate: Jason Craumer
date: 2026-05-29
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Questions: Jason Craumer
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-29
**Interviewer:** Marten Engblom
**Stage:** HM Screen (36 min)

---

## Career Overview

**Q: Give me your high-level executive summary of yourself, your career, and what you're an expert in.**

**A:** Worked at Verizon for 27 years total, with the past 10 years focused on monitoring, data engineering, and networking. Built systems for log capture, anomaly detection, and automated feedback loops. Created ML-based predictive maintenance system for fiber lasers (95% accuracy, predicted failures 2 weeks in advance). Built entire data platform with architecture team (5 people) using Apache open-source tools (Flink, Spark, Hadoop, Kafka, Splunk) processing 5-10TB/day. Administered Kafka, Flink, Splunk, and GIS databases. Managed team of 8 data scientists doing code reviews, git administration, and CI/CD pipeline setup.

---

## Data Platform Architecture

**Q: Pick one of the projects that captured and stored decent volumes of data and walk me through the architecture.**

**A:** Streaming platform processing 5-10TB/day. Sources would gather data and put on Kafka topic, platform would pull data off Kafka, run through augmentation/matching, put back on Kafka for downstream consumption. Decoupled design allowing any downstream tool (Splunk, Tableau, Looker, Click) with Kafka connector. Storage in Hadoop (later switched to GCP Big Data) - held raw data feeds for a few months for reprocessing if logic changed. In-transit data held on separate Kafka topics for 5-15 minutes waiting for matching records. Failed records went to "fail topics" (dead letter queue pattern) with alerting via Grafana and Splunk. Finished products sent downstream as JSON or Avro key-value pairs, also stored in Hadoop for ~6 months.

---

## Traditional Database Experience

**Q: Talk to me about some project involving more traditional databases - document or relational databases.**

**A:** Built document server for GIS data tables (census data, population, cell tower coverage overlay). Previously done ad hoc for 52 different market areas - one person spending 40 hours/week manually querying and emailing files. Built Django portal with relational database pool and subqueries per market area. First person to request would trigger 3-4 minute file generation, subsequent users would download existing file. Built custom SAML SSO middleware, handled PKI/certificate management. Converted 40 hours/week manual work into self-service portal with weekly data dumps.

Also built similar portal using Flask for sample data uploads.

---

## Core Expertise

**Q: What's on the short list of things you are extremely good at? What's your core expertise - the thing where everyone knows Jason needs to be involved?**

**A:** Primary areas of expertise:
- **ETL work** - cited as "probably one of my strong points"
- **Splunk and ELK Stack** (Elasticsearch)
- **Kafka administration**
- **Data translation and data typing** - helping teams understand data type casting issues (e.g., text fields that should be floats for lat/long)
- **Writing custom data ingestion platforms** in Python for systems with APIs but poor native ingest capabilities. Built web app where users upload data, pick data types, system auto-detects best fit with forced fields (e.g., latitude/longitude must be float)
- **Backend administration** - NGINX, HAProxy, API services
- **API development** - "hundreds of Python API services" or Java APIs
- **System administration**
- **Cloud platforms** - "good working knowledge" of GCP and AWS with admin roles

---

## Database Technology Preferences

**Q: What would you choose for document storage? What have you had better experiences with?**

**A:** Prefers DynamoDB and DocumentDB (AWS) over MongoDB for actual document storage (full image documents). Reasoning: "Transactions seem to be a lot faster, especially when you're doing very large volume of transactions." Sees DocumentDB as "more efficient" at high volume. Claims MongoDB has lag issues at "thousands and thousands of transactions" due to lock management being "not quite as efficient as it was in DocumentDB."

**Q: How would you contrast DynamoDB to those two products?**

**A:** "DynamoDB is somewhere in the middle. I mean, it's efficient as well." Acknowledges all three have tradeoffs and you need to "look at the pros and cons and the trade-offs for all."

---

## Questions for Interviewer

**Q: How big is your team that you have now?**

**Q: What is your major tech stack that you're using now?**

---

## Red Flags / Concerns

**1. Fundamental Database Technology Misunderstanding:**
- Recommended DocumentDB (AWS) over MongoDB, claiming DocumentDB has better "lock management" and is "more efficient"
- **Critical issue:** DocumentDB IS MongoDB-compatible - it uses MongoDB's wire protocol. This is a basic fact any MongoDB expert would know.
- Called DynamoDB a "document database" positioned "somewhere in the middle" - DynamoDB is primarily a key-value store
- Shows MongoDB experience is shallow/outdated despite claiming years of use
- For a Principal Data Architecture role, inability to correctly explain database technology tradeoffs is disqualifying

**2. Administration-Heavy Background (Not Application Development):**
- 27 years at Verizon, much of it in operations, dispatch, fleet management, IT support roles
- Interview heavily emphasized administration: Kafka admin, Flink admin, Splunk admin (20 search heads, 80 indexers), system admin, PKI/certificate management
- Interviewer's raw notes explicitly flag: "Heavy on Administration... too admin focus"
- Role requires "strong application development background" - candidate's experience is primarily ops/admin/ETL

**3. Data Platform Operator vs. Application Architect:**
- Experience is in **data platforms** (ETL, streaming, batch processing, log aggregation for network operations)
- Role requires expertise in **application data** (transactional databases, schema design, ORM optimization, query patterns for user-facing products)
- These are fundamentally different problem spaces
- Examples are internal operational tools (Django portals), not customer-facing product applications

**4. Networking/Hardware Focus:**
- Opens career summary with: "I've learned a lot about networking over the years. So obviously, we dealt with mostly network stats and machines, routers, switches, that kind of thing."
- Interviewer's notes flag: "Mentioned networking multiple times... hardware focused??"
- 27 years at Verizon dealing with "network stats and machines, routers, switches"
- GIS databases for cell tower coverage mapping - telecom infrastructure, not application data
- Context is telecom network operations, not software product development

**5. Communication Issues - Verbose and Vague:**
- Struggled to articulate core expertise concisely - took ~200 words and multiple tangents when asked directly
- Uses vague qualifiers throughout: "good working knowledge," "somewhere in the middle," "a little bit faster," "it worked great"
- Could not provide crisp answer to "what are you an expert at?"
- For a Principal role requiring teaching/enabling teams, communication clarity is critical

**6. Shallow Technology Explanations:**
- MongoDB "lock management" critique is outdated (WiredTiger storage engine addressed this years ago)
- Couldn't articulate modern MongoDB use cases (time series collections, aggregation pipelines, Atlas features, change streams)
- Generic descriptions lacking technical depth: "It worked great," "I love Mongo," "Mongod is my favorite part" (referring to command line tool)
- No discussion of: sharding strategies, replica sets, consistency models, transaction isolation levels, compound indexes
- For someone claiming database expertise, explanations were surface-level

**7. Limited Application Architecture Depth:**
- No mention of: API design patterns, microservices architecture, domain-driven design, event sourcing, CQRS
- No discussion of: data modeling for complex business domains, schema evolution strategies, multi-tenancy patterns
- Examples focused on pipelines and infrastructure rather than application-level architecture decisions
- Missing: ORM optimization, N+1 query problems, connection pooling strategies, caching patterns

---

## Interviewer Notes

**Overall Impression:** Candidate has deep operations and data pipeline experience at Verizon scale - legitimate streaming platforms (Kafka, Flink, 5-10TB/day), ETL work, and operational systems. However, this is a **clear pass** for Principal Engineer role focused on enabling application teams to build healthcare software products.

**Critical disqualifiers:**

1. **Fundamental database knowledge gaps** - MongoDB/DocumentDB confusion (DocumentDB IS MongoDB-compatible) shows he cannot reliably evaluate or recommend database technologies. For a role requiring teaching teams, this is disqualifying.

2. **Wrong background context** - 27 years in **telecom network operations**, not product software engineering. Experience is data platform operator/admin, not application architect. Interviewer noted immediately: "Heavy on Administration... too admin focus" and "hardware focused??"

3. **Cannot articulate expertise clearly** - Took 200+ words with tangents to answer "what are you expert at?" For a Principal role requiring communication and enabling others, this is problematic.

4. **Missing application development depth** - Role requires "strong application development background" but candidate's examples are internal ops tools (Django portals for GIS data), not customer-facing product applications.

**What's legitimate:**
- ETL and streaming pipeline architecture (Kafka, Flink) - this discussion had real depth
- Hands-on operational experience at scale (distributed Splunk, 5-10TB/day processing)
- Pragmatic problem-solving (40 hrs/week manual work → automated portal)

**Why it doesn't matter:**
The role needs someone who thinks like an **application architect with deep data expertise** embedded with product teams. This candidate is a **data platform operator with admin focus** from network operations. Different domain, different role context, fundamental knowledge gaps in database technologies.

**Key moments:**
- 9:13: Opens career summary with networking ("network stats and machines, routers, switches") - signals ops/infrastructure orientation
- 24:47: Asked for core expertise - lists administration repeatedly (Kafka admin, Splunk admin, system admin, backend admin)
- 32:15-33:50: DocumentDB/MongoDB discussion - most damaging moment, reveals fundamental misunderstanding
- Throughout: Cannot provide technical depth on application architecture, schema design, data modeling for complex domains
