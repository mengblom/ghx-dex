---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Chas Narne
date: 2026-05-21
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Scorecard: Chas Narne
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-21
**Stage:** HM Screen (30 min)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | 4 | Resume: PostgreSQL, Oracle across SAE (2021-present), Philips (2018-2020), FedEx (2013-2018), Zycron (2012-2013). Oracle listed as primary skill. | Interview: Extensive Oracle discussion (300 tables → MongoDB migration), PostgreSQL mentioned as current option, described data modeling and schema decisions. Strong practical knowledge. |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB) | 5 | Resume: MongoDB, CouchDB listed in skills. SAE: "Architected Change Data Capture solutions across NoSQL (MongoDB)". Philips: IoT data "persisting in NoSQL (MongoDB)". | Interview: Deep MongoDB discussion - CAP theorem, write concerns (CP vs AP), TTL for archiving, operational logs, self-managed vs Atlas, denormalization challenges, collection design. This is clearly a core strength. |
| Database performance optimization at scale (query tuning, indexing, execution plans) | 4 | Resume: Philips role mentions "optimizing data access patterns for high-throughput ingestion workloads". SAE mentions "real-time data synchronization" and CDC. | Interview: Discussed eventual consistency lag optimization (2 second challenge), multi-threaded queries comparing Oracle + Elastic, write concern tuning for performance. Practical optimization experience demonstrated. |
| Advanced data modeling and schema design (temporal models, event sourcing, complex domains) | 5 | Resume: "Architected Change Data Capture solutions", "event-driven architecture with Kafka and RabbitMQ", "Implemented idempotent event processing patterns". | Interview: **Core stated expertise** - "If you come up with a good data model, it's extremely easy to come up with good APIs." Discussed service boundaries, data mutation analysis, denormalization decisions, archive patterns. Strong event-driven thinking. |
| Application development skills (full-stack, backend, or data-intensive applications) | 5 | Resume: 13+ years building applications. Java 17+, Spring Boot, TypeScript/JavaScript, Angular. Built complete platforms at SAE, Philips, FedEx. | Interview: Mentioned doing UI work (Angular, React - "know enough to be dangerous"), primary focus backend and data. Day-to-day includes code reviews. Full-stack capable but backend/data-focused. |
| Can review application code and architecture with focus on data access patterns | 5 | Resume: "Mentored junior and mid-level engineers through code reviews, architectural walkthroughs". Philips: "optimizing data access patterns". | Interview: Day-to-day involves "a lot of code reviews". Explicitly mentioned analyzing how users access data, mutation patterns, effect on existing services/data. This is current daily work. |
| Experience evaluating and selecting database technologies based on workload, cost, and usage patterns | 4 | Resume: FedEx role mentions "Led the technology selection process for the enterprise reporting platform, executing multiple POCs to evaluate scalability, cost, and integration capabilities". | Interview: Wasn't there for MongoDB selection at SAE but evaluated it post-decision. Mentioned choosing between Oracle, PostgreSQL, MongoDB, Redis for new services today based on use case. Has selection framework. |
| Cloud data platform expertise (AWS, Azure, or GCP) with cost optimization focus | 3 | Resume: AWS (Core Services), Azure (AKS/K8s) listed. SAE: "40+ cloud-native microservices on AWS". Mentions "Reduced cloud infrastructure costs by auditing Kubernetes pod utilization...cutting compute overhead". | Interview: Mentioned "very little in AWS realm, just proof of concept" for managed services like DynamoDB. RDS migration from on-prem Oracle. **Mixed signal** - resume shows AWS work, but interview suggests less depth with AWS managed services. |
| Data warehouse design and implementation (Snowflake, Redshift, etc.) | N/A | Resume: No data warehouse or analytics platform experience mentioned. | Interview: Mentioned GHX uses Snowflake for analytics but noted "that's owned by a different team" - not his area. |
| ETL/ELT pipeline design and data processing architectures | 4 | Resume: "Architected Change Data Capture solutions...enabling real-time data synchronization". "Built core ingestion and processing services...handling massive streams of IoT telemetry data". | Interview: Described Oracle triggers → RabbitMQ → service listeners for data sync (300-500ms). Monstache for MongoDB → Elasticsearch ETL. Kafka for batch aggregation (10-minute window). Solid CDC/streaming ETL experience. |
| Event-driven architectures, change data capture, and streaming platforms (Kafka, Kinesis, Pub/Sub) | 5 | Resume: "Event-Driven architecture" as core competency. "Implemented idempotent event processing patterns ensuring fault-tolerant, zero-duplication message delivery". Kafka/RabbitMQ listed. | Interview: **Strong demonstration** - Described Kafka for audit aggregation, RabbitMQ for fast sync, event-driven saga patterns vs eventual consistency decisions. Knows when to use sync vs async ("Is user waiting?"). Dead letter queues, retries, alerting. Deep practical knowledge. |
| Data architecture for ML/LLM applications (vector databases, embeddings, RAG patterns) | N/A | Resume: Lists AI-assisted development tools (Claude, Cursor, etc.) but no ML/LLM data architecture work. | Interview: Discussed AI-assisted development for feature migration automation (PRD generation, code generation) but not data architecture for ML/LLM systems. |
| Zero-downtime data migration and schema evolution strategies | 4 | Resume: Mentions "strangler pattern" implicitly in modernization work. SAE: Led monolith → microservices migration. | Interview: **Strangler pattern explicitly mentioned** by interviewer's notes. Described incremental user migration strategy (5 different apps for user types, all using same backend). This is textbook strangler fig approach. |
| Data quality, monitoring, and observability practices | 4 | Resume: SAE mentions "60% reduction in production support incidents". Lists APM tools (Dynatrace, AppDynamics, NewRelic, Datadog). | Interview: Discussed ops dashboard monitoring usage/requests, alerting on DLQ message counts, Teams hooks for critical queues. Practical observability in place. |
| Aligning data ownership models with domain boundaries | 4 | Resume: "40+ cloud-native microservices" implies service/data boundary work. | Interview: Discussed "coming up with service boundaries" as core skill. Analyzes: How many legacy tables touched? Does it affect existing services? What's the data mutation pattern? Strong domain boundary thinking. |
| Hands-on troubleshooting and optimization of production data systems | 5 | Resume: "Principal Software Engineer" title implies hands-on. Mentions code reviews and direct implementation work throughout. | Interview: "Enjoy getting hands dirty with proof-of-concept work." Day-to-day involves code reviews and implementation. Recent optimization work on eventual consistency lag. Clearly hands-on. |
| Proficiency in modern programming languages (Python, Java, JavaScript/TypeScript, C#) | 5 | Resume: Java (Spring/Hibernate), Groovy, Kotlin, TypeScript/JavaScript, Python, SQL/PL-SQL all listed. 13+ years Java experience. | Interview: Mentioned Java, TypeScript, Angular, React. Primary Java/Spring Boot developer. Strong alignment with GHX stack. |

---

**Skills Summary:**

Chas demonstrates **strong** technical depth in the core areas critical for this role. Standout strengths include:

**Data modeling and event-driven architecture:** This is clearly Chas's strength. The philosophy "If you come up with a good data model, it's extremely easy to come up with good APIs" aligns perfectly with what this role needs - someone who thinks data-first and can guide teams on modeling decisions. The discussion of service boundaries, data mutation analysis, and choosing between saga patterns vs eventual consistency shows sophisticated architectural thinking.

**NoSQL expertise (MongoDB):** Deep, production-grade knowledge of MongoDB internals - CAP theorem tuning, write concerns, TTL patterns, operational logs, denormalization challenges. This is particularly valuable given GHX's heavy MongoDB usage and need to evaluate if it's being used appropriately.

**Event-driven systems:** Strong practical experience with both Kafka and RabbitMQ. Knows when to use each (Kafka for aggregation windows, Rabbit for fast sync). Understands idempotency, dead letter queues, and operational patterns. The decision framework "Is the user waiting?" for sync vs async shows pragmatic thinking.

**Key gap:** Cloud managed data services depth appears lighter than resume initially suggests. Resume shows AWS work and cost optimization, but interview reveals "very little in AWS realm" for managed services (DynamoDB mentioned as "just proof of concept"). This could be a development area, but may not be critical if the role focuses more on data modeling/architecture than infrastructure.

**Minor gap:** No data warehouse or ML/LLM data architecture experience.

**Overall technical assessment:** 4.5/5 - Good fit for the data modeling, architecture, and application development aspects of the role. Some development opportunity around AWS managed services, but core skills are outstanding.

---

## Personality Traits Assessment

| Trait | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Enabling mindset - succeeds by making others successful | 5 | Resume: "Mentored junior and mid-level engineers through code reviews, architectural walkthroughs, and pairing sessions, elevating team-wide proficiency". | Interview: "That's kind of my day job - work across teams, establish standards, align high-level architecture improvements." When asked about role fit, immediately connected to enabling others. |
| Educates and empowers rather than gatekeeps | 5 | Resume: "Mentored...elevating team-wide proficiency". Established standards across teams. | Interview: Discussed creating apps to "make engineers' lives easier." Focus on establishing standards and patterns for others to follow. No gatekeeping signals detected. |
| Hands-on and takes ownership | 5 | Resume: Principal title but still doing code reviews and implementation. "Built", "Architected", "Implemented" throughout (not just "Led"). | Interview: "Enjoy getting hands dirty with proof-of-concept work." "Day-to-day involves a lot of code reviews." Clearly stays hands-on despite principal-level title. |
| Can influence without authority | 4 | Resume: "Established...standards across microservices". Working across 40+ microservices implies influencing multiple teams. | Interview: "Work across teams, establish standards" - present tense, indicating current cross-team influence. Not explicitly discussed but implied by multi-team work. |
| Pragmatic judgment - knows when to optimize for speed vs. perfection | 5 | Resume: "Had very strict time-to-market requirements" leading to MongoDB-first then iterate approach. | Interview: **Strong evidence** - "Had very strict time-to-market requirements for migration - MongoDB was first choice, then circled back and did 50/50 refactoring." The "Is user waiting?" framework for sync vs async shows pragmatic decision-making. Accepts 2-second lag as "good enough" after optimization. |
| Comfortable with ambiguity and building from scratch | 4 | Resume: Led modernization of legacy monolith (inherently ambiguous). FedEx: "Led the technology selection process...executing multiple POCs". | Interview: Described breaking down 30-year-old monolith into microservices (high ambiguity). Building automation for feature migration (greenfield work). |
| Works effectively in modern agile/iterative development processes | 4 | Resume: Lists "Agile/SCRUM, Kanban, LEAN, SAFe" under SDLC Methods. | Interview: Described incremental user migration strategy, iterative optimization of eventual consistency. Not explicitly discussed but implied by work patterns. |
| Collaborates effectively across teams (engineering, product, infrastructure, security) | 5 | Resume: 40+ microservices imply multi-team collaboration. "Established...standards across microservices". | Interview: "Work across teams" mentioned multiple times. Described working with ops team on monitoring/alerts. Cross-functional collaboration is current reality. |
| Communicates technical concepts effectively to executives and non-technical stakeholders | 5 | Interviewer's direct observation. | Interviewer notes: **"Great communicator, effective and to the point."** Explained complex concepts (CAP theorem, eventual consistency, event-driven patterns) clearly during interview. This is first-hand evidence. |

---

**Personality Traits Summary:**

**Strong cultural fit.** Chas embodies the "enabling mindset" that's critical for this principal role. The immediate response to the role description was "That's kind of my day job - work across teams, establish standards" - this person already thinks like an enabler, not a gatekeeper.

**Pragmatic and hands-on:** The philosophy of choosing MongoDB first due to time-to-market pressure, then iterating back to 50/50 with other databases, shows excellent judgment. Doesn't let perfect be the enemy of good, but also doesn't let "good enough" become permanent technical debt.

**Communication strength:** Strong communication skills - "effective and to the point." For a role requiring education and enablement across teams, this is essential. Technical depth without communication ability would be insufficient.

**Hands-on at principal level:** Still doing code reviews daily and building POCs despite principal title. This matches the role's expectation of being hands-on with troubleshooting and optimization, not just providing high-level guidance.

**Minor note:** "Can influence without authority" scored 4 instead of 5 only because it wasn't explicitly tested in this short screen. Multi-team work strongly implies it, but deeper behavioral questions in next rounds could confirm.

**Overall personality assessment:** 5/5 - Outstanding fit. The combination of technical depth + enabling mindset + hands-on approach + strong communication is exactly what this role requires.

---

## Qualifications Assessment

| Qualification | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| 10+ years of hands-on experience building software applications with heavy focus on data systems | 5 | Resume: 13+ years total experience (2012-present). Every role shows heavy data focus - MongoDB, Oracle, PostgreSQL, streaming. | Interview: Confirmed deep data systems focus across all roles. Data modeling is stated core expertise. Clear 10+ years of relevant experience. |
| Strong application development background (not just database administration) | 5 | Resume: "Principal Software Engineer" (not DBA). Built complete applications/platforms at SAE, Philips, FedEx. Java/Spring Boot, APIs, microservices. | Interview: "Day-to-day involves a lot of code reviews." Mentioned doing UI work. API design is core skill. Clearly application developer who specializes in data, not DBA. |
| Track record of establishing data standards and patterns across engineering organizations | 5 | Resume: "Established unit and integration testing standards across microservices". 40+ microservices implies cross-team standardization. | Interview: **Explicit confirmation** - "Work across teams, establish standards, align high-level architecture improvements from data and consistency perspective." This is current job description. |
| Experience leading data migrations and infrastructure modernization initiatives | 5 | Resume: **Headline accomplishment** - "Led modernization of a legacy monolith into 40+ cloud-native microservices". SAE role is entirely about this. | Interview: Described Oracle (300 tables) → MongoDB + Elasticsearch migration. Strangler pattern for incremental user migration. This is literally what the person has been doing for 4 years. |
| Experience with AI/LLM-assisted development tools and agentic software engineering practices | 5 | Resume: Lists Claude (Code/Cowork), Cursor, Gitlab Duo, OpenClaw under "AI-Augments". | Interview: **Enthusiastic depth** - "Last six months = best engineering time of career" using Claude heavily. Building automation for legacy-to-modern feature migration with PRD generation and code generation. Creating apps "faster than can use them." On par with or exceeds GHX's expectations. |
| Prior Principal Engineer, Staff Engineer, or senior technical leadership experience | 5 | Resume: **Principal Software Engineer at SAE (2021-present)** - 4 years at principal level. Senior Software Engineer at Philips (2018-2020). | Interview: Confirmed current Principal Engineer title. Scope includes 40+ microservices, cross-team standards, mentoring. Legitimate principal-level experience. |
| Bachelor's degree in Computer Science or equivalent practical experience | 5 | Resume: Master of Science, Computer Information Science (2009-2012), University of Alabama - Birmingham. Bachelor of Technology, Information Technology (2005-2009), JNTU India. | Interview: Not discussed, but resume shows MS degree exceeds requirement. |

---

**Qualifications Summary:**

**Perfect alignment with role requirements.** Every qualification met at the highest level:

- **Experience:** 13+ years building data-intensive applications (exceeds 10+ requirement)
- **Application development:** Software engineer who specializes in data, not DBA - exactly what the job description emphasizes
- **Standards/enablement:** Already doing this across 40+ microservices at SAE - current job matches future job
- **Migrations:** Led monolith → microservices migration for 4 years - deep, relevant experience
- **AI/LLM tools:** Not just using them, but building automation with them. "Best engineering time of career" in last 6 months shows enthusiasm that matches GHX's aggressive AI adoption
- **Level:** 4 years as Principal Engineer (not just title inflation - scope justifies it)
- **Education:** MS degree exceeds BS requirement

**No gaps in qualifications.** This is a complete package.

---

## Other/Details

| Detail | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Healthcare or EDI (Electronic Data Interchange) domain knowledge | 5 | Resume: **Philips Respironics (2018-2020)** - Built healthcare IoT platform handling EDF data from 50,000+ patient devices. "HIPAA-compliant...with strict data security, auditability, and compliance requirements". | Interview: First experience mentioned was Philips healthcare domain - medical device data, clinical decision-making, permissions for clinicians vs doctors. Understands regulated healthcare environment. |
| Experience in enabling team or platform team models | 5 | Resume: Working across 40+ microservices with established standards implies enabling model. "Mentored junior and mid-level engineers". | Interview: "Work across teams, establish standards" - this IS an enabling team model. Not embedded in single product team. |
| Experience with autonomous or cross-functional team environments | 5 | Resume: 40+ microservices = multiple autonomous teams by definition. Microservices architecture requires team autonomy. | Interview: Described teams making technology choices (Kafka vs Rabbit, which database for new service). His role is to establish standards while teams build. Classic autonomous team setup. |

---

**Other/Details Summary:**

**Perfect bonus alignment.** The healthcare experience at Philips is particularly valuable - not just healthcare domain knowledge, but specifically understanding **regulated data requirements** (HIPAA compliance, auditability, data integrity for clinical decisions). This directly transfers to GHX's healthcare supply chain environment.

The enabling team experience is **current reality**, not aspirational. Already working across many teams to establish standards - exactly the model Marten is building at GHX.

---

## Overall Assessment

**Key Strengths:**

1. **Data modeling expertise is core competency:** "If you come up with a good data model, it's extremely easy to come up with good APIs" - this philosophy and the demonstrated ability to analyze service boundaries, data mutation, and access patterns is **exactly** what the role needs. Someone who can review teams' data models and guide them to better designs.

2. **Deep MongoDB knowledge with critical thinking:** Not just knows MongoDB, but can evaluate where it's appropriate and where it's not. The experience of choosing MongoDB for time-to-market then iterating back to mixed database strategy shows the pragmatic judgment needed to help GHX optimize their MongoDB usage.

3. **Enabling mindset already in practice:** Doesn't need to learn how to enable teams - already doing it across 40+ microservices at SAE. The immediate "That's kind of my day job" response to role description shows this is natural thinking pattern.

4. **Hands-on principal:** Still in code reviews daily, builds POCs, enjoys getting hands dirty. Won't be an ivory tower architect - will roll up sleeves to help teams solve problems.

5. **Strong communicator:** Interviewer directly observed clear, effective communication. For a role requiring education across teams and communication to non-technical stakeholders, this is essential.

6. **Healthcare domain experience:** Philips Respironics work provides direct healthcare context and understanding of regulated data requirements.

7. **AI/LLM enthusiasm matches GHX culture:** "Best engineering time of career" in last 6 months with Claude. Building sophisticated automation. This energy matches GHX's aggressive AI adoption strategy.

**Minor Development Areas:**

1. **AWS managed services depth:** Resume shows AWS work, but interview reveals less depth with managed services than initially apparent ("very little in AWS realm" for services like DynamoDB). However, has strong cloud architecture thinking and should be able to ramp quickly. May not be critical if role focuses more on data modeling than infrastructure.

2. **Data warehouse experience:** No Snowflake/Redshift background, but this wasn't emphasized in job description and may not be needed since Marten mentioned analytics is a different team.

**Resume vs. Interview Alignment:**

**Strong overall alignment** with one small disconnect: Resume lists AWS experience and cloud cost optimization, creating impression of deep AWS managed services expertise. Interview revealed that AWS work was more lift-and-shift (EC2-based) and managed services were "very little...just proof of concept." This isn't disqualifying - the core data modeling, MongoDB, event-driven, and application development skills are all well-demonstrated in both resume and interview. The AWS managed services gap is a development opportunity, not a red flag.

**Fit for Role:** 5/5 (Strong Yes)

**Reasoning:**

This is an **exceptionally strong match** for the role. The combination of technical depth in data architecture + enabling mindset + hands-on approach + strong communication + relevant domain experience checks every critical box.

**Most compelling evidence:** When asked about role fit (working across teams on data strategy, modeling, storage, archiving), Chas's immediate response was "That's kind of my day job." This isn't someone who needs to transition into the role - they're already doing it at SAE. The skills are transferable and the mindset is already there.

**Technical fit:** Core skills (data modeling, MongoDB, event-driven architecture, application development, database selection) are all 4-5/5. The one 3 score (cloud managed services) is a development area but not disqualifying given the role's primary focus on data architecture and application-level data patterns.

**Cultural fit:** The combination of "establish standards across teams" + "enjoy getting hands dirty with POCs" + "great communicator, effective and to the point" is exactly the profile needed. Someone who can both set direction and help teams execute, who enables rather than gatekeeps.

**Healthcare context:** Prior healthcare experience (Philips) provides domain understanding and appreciation for regulated data requirements - valuable for GHX's healthcare supply chain environment.

**AI alignment:** The enthusiasm for AI-assisted development and sophisticated automation work matches GHX's culture perfectly. "Creating apps faster than can use them" shows the kind of productivity multiplier GHX is looking for.

**Risk assessment:** Very low risk hire. 4 years at Principal Engineer level (not title inflation), clear track record of similar work (monolith modernization, establishing standards across teams, data-focused architecture), strong references likely given accomplishments. The "what could go wrong" scenarios are minimal.

**Recommendation:** ☑ **Advance to Full Interview Loop**

Move quickly on this candidate. The combination of technical skills + enabling mindset + relevant experience + cultural fit is rare. Based on this screen, Chas should advance to technical deep-dive interviews focusing on:
- Data modeling exercises (core stated strength - test it)
- Enabling/mentoring scenarios (verify the mindset)
- AWS managed services knowledge (probe the gap)
- Stakeholder communication scenarios (build on observed strength)

---

## Interview Notes

**Interviewer's raw notes:**

- Does have healthcare experiences (Philips Respironics)
- Monolith breakup experience (SAE International)
  - Went from Oracle to MongoDB, indexed into Elasticsearch
  - Naturally mentions strangler pattern etc.
- Very good experience with modern distributed architectures, well versed in microservices, APIs, REST etc.
- Very experienced with Mongo
- Well versed in DB terms (CAP theorem)
- Great communicator, effective to the point
- AI / LLM assisted development is on par or better than what we expect at this point
- Will definitely move Chas on to the full interview loop.

**Key moments that led to decision:**

1. **Data modeling as core philosophy** (line 81): "If you come up with a good data model, then it's extremely easy to come up with good APIs. That's kind of my motto." - This encapsulates the thinking needed for the role.

2. **Role fit confirmation** (line 103): When asked about being data-focused and working across teams, immediate response was "Yeah, I mean that's kind of my day job. I work across teams established standards and align high level architecture improvement on a from a data and consistency perspective. So I'd be very excited to come into the role." - Not learning a new role, already doing it.

3. **CAP theorem discussion** (line 41): Unprompted discussion of MongoDB write concerns, CP vs AP trade-offs shows sophisticated database thinking beyond just "use MongoDB because it's popular."

4. **Pragmatic judgment** (lines 58-61): The story of choosing MongoDB for time-to-market, hitting problems with eventual consistency, then iterating to mixed database strategy shows exactly the judgment needed - optimize for delivery, learn, adapt.

5. **Strangler pattern** (interviewer note, line 5): Natural mention of strangler pattern without prompting shows architectural thinking is second nature, not memorized interview responses.

6. **AI enthusiasm** (lines 96-101): "Last six months...best engineering time of career" and "creating apps faster than I can use them" shows genuine excitement that matches GHX's AI-first culture.
