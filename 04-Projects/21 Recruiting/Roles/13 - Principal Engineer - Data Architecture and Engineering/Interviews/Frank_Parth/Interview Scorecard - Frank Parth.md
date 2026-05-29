---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Frank J. Parth
date: 2026-05-28
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Scorecard: Frank J. Parth
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-28
**Stage:** HM Screen (30 min)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | N/A | Resume: Mentions Oracle, SQL Server, Postgres in job history (NextGen 2014-2016) | Interview: Not discussed |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB) | 2 | Resume: Mongo mentioned (Baxter, NextGen roles), Cosmos DB (Craneware) | Interview: Used Mongo as storage backend for FHIR data. DocumentDB choice explained as "they needed a very specific subset" - no architectural depth. Only discussed indexing for performance. |
| Database performance optimization at scale (query tuning, indexing, execution plans) | 2 | Resume: No specific performance optimization mentioned | Interview: When asked about query optimization, only mentioned "indexing of the database" - no discussion of query tuning, execution plans, or performance analysis |
| Advanced data modeling and schema design (temporal models, event sourcing, complex domains) | N/A | Resume: No evidence | Interview: Not discussed |
| Application development skills (full-stack, backend, or data-intensive applications) | 3 | Resume: Java, JavaScript, C# development, API endpoints, microservices | Interview: Described C# microservices at Baxter, API development, but focused heavily on integration/interface work rather than full application development |
| Can review application code and architecture with focus on data access patterns | N/A | Resume: No evidence of code review or architecture review | Interview: Not discussed |
| Experience evaluating and selecting database technologies based on workload, cost, and usage patterns | 1 | Resume: Multiple databases used across roles | Interview: **MAJOR DISCONNECT** - When asked why DocumentDB was chosen, said "our team decided to go with it" and business leaders "always looking at costs." No articulation of workload analysis, technology trade-offs, or architectural decision-making. Passive role in technology selection. |
| Cloud data platform expertise (AWS, Azure, or GCP) with cost optimization focus | 2 | Resume: Azure Cloud servers (Craneware), AWS (Baxter), Kubernetes migration | Interview: Used AWS DocumentDB and Azure Cosmos DB but couldn't discuss cost optimization. When asked about self-hosted vs managed: "God, no, I haven't worked with self-host in so long" - limited depth on cloud platform decisions |
| Data warehouse design and implementation (Snowflake, Redshift, etc.) | N/A | Resume: Hadoop mentioned at Craneware for data analysis | Interview: Not discussed |
| ETL/ELT pipeline design and data processing architectures | 2 | Resume: Data integration, processing HL7/FHIR data, Hadoop | Interview: Described data transformation (HL7 to FHIR) but focused on interface-level transformations, not broader pipeline architecture |
| Event-driven architectures, change data capture, and streaming platforms (Kafka, Kinesis, Pub/Sub) | 3 | Resume: Kafka feeds, RabbitMQ/Cosmos DB, MQTT feeds | Interview: Used RabbitMQ at Baxter for pub-sub model (CDR event distribution). Created Mirth plugin to read from Kafka at Craneware. Described facility-based topics for multi-tenancy. Demonstrated usage but not deep architectural design. |
| Data architecture for ML/LLM applications (vector databases, embeddings, RAG patterns) | N/A | Resume: Master's in Data Science (2018), machine learning model design at Craneware | Interview: Not discussed |
| Zero-downtime data migration and schema evolution strategies | N/A | Resume: Migration from Azure VM to Kubernetes mentioned | Interview: Mentioned migration but no discussion of zero-downtime strategies or schema evolution |
| Data quality, monitoring, and observability practices | N/A | Resume: Monitor queues, error handling | Interview: Not discussed in depth |
| Aligning data ownership models with domain boundaries | N/A | Resume: No evidence | Interview: Not discussed |
| Hands-on troubleshooting and optimization of production data systems | N/A | Resume: Error handling, debugging | Interview: Not discussed |
| Proficiency in modern programming languages (Python, Java, JavaScript/TypeScript, C#) | 4 | Resume: Java, JavaScript, C# (extensive), Python (data science degree) | Interview: Mentioned C# microservices, Java development - credible programming background |

**Critical Disconnect:** Resume shows diverse database experience (Mongo, DocumentDB, Cosmos DB, relational) across recent roles, but interview revealed **passive role in technology selection** ("our team decided") and **shallow architectural thinking** (only mentioned indexing for performance optimization, couldn't articulate why DocumentDB vs Mongo beyond "specific subset"). This suggests experience *using* predetermined database solutions within integration platforms, not *architecting* data systems or driving technology decisions.

**Skills Summary:**

Frank's technical background is primarily as an **integration/interface engineer** specializing in healthcare data standards (HL7/FHIR), not a data architect. His database experience consists of using NoSQL databases (Mongo, DocumentDB, Cosmos DB) as storage backends for integration engines and FHIR repositories, but he demonstrated limited depth in:

- **Database selection rationale**: Could not articulate workload analysis, technology trade-offs, or cost considerations. Described technology decisions as team-driven or business-driven, not architect-driven.
- **Performance optimization**: When asked about query optimization beyond indexing, did not mention execution plans, query tuning, materialized views, partitioning strategies, or complementary technologies (Elasticsearch for search, relational DB for complex queries).
- **Architectural breadth**: No discussion of data modeling complexity, schema design, data ownership boundaries, or evolving data architectures over time.

His strongest area is **event-driven integration** using RabbitMQ/Kafka within the context of medical interface engines, but this is a narrow slice of the data architecture expertise needed for this Principal role. The role requires someone who can evaluate data technologies, design data models, optimize performance at scale, and guide teams on data decisions - Frank's experience is more focused on implementing interfaces and transformations within existing platform architectures.

Most concerning: when asked "what's your core technical expertise," Frank answered "medical interface engineer and data repository" - not data architecture. This is an accurate self-assessment.

---

## Personality Traits Assessment

| Trait | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Enabling mindset - succeeds by making others successful | N/A | Resume: No evidence of enabling/teaching others | Interview: Not discussed |
| Educates and empowers rather than gatekeeps | N/A | Resume: No evidence | Interview: Not discussed |
| Hands-on and takes ownership | 4 | Resume: "A stickler for finishing things. I always did not finish things, you know. So I wanted to finish my solution" | Interview: Stayed months longer at Craneware to finish solution. Described hands-on implementation work. |
| Can influence without authority | N/A | Resume: No evidence | Interview: Not discussed |
| Pragmatic judgment - knows when to optimize for speed vs. perfection | N/A | Resume: No evidence | Interview: Not discussed |
| Comfortable with ambiguity and building from scratch | N/A | Resume: Startup experience (TAFi) | Interview: Not discussed |
| Works effectively in modern agile/iterative development processes | 3 | Resume: Agile processes at Cerner, iterative improvements | Interview: Not discussed in detail |
| Collaborates effectively across teams (engineering, product, infrastructure, security) | 3 | Resume: Multiple team environments, interfacing with vendors | Interview: Described working with different device teams at Baxter, creating central CDR that other teams connected to |
| Communicates technical concepts effectively to executives and non-technical stakeholders | 2 | Resume: No evidence | Interview: **Communication concerns** - responses lacked depth when probed, went off-topic at times (moving story, telescope, cold symptoms), could not clearly articulate architectural decisions or trade-offs |

**Personality Traits Summary:**

Limited signal on most traits due to short 30-minute screen focused on technical skills. Key observation: **communication effectiveness is a concern**. When asked technical architecture questions, Frank provided surface-level responses and couldn't articulate the "why" behind technology decisions. For a Principal role requiring influence without authority and education of team members, the ability to clearly explain complex technical concepts is critical. Frank's responses suggested difficulty communicating at the architectural level - more comfortable describing implementation details than strategic rationale.

---

## Qualifications Assessment

| Qualification | Score | Resume Evidence | Interview Evidence |
|---------------|-------|-----------------|-------------------|
| 10+ years of hands-on experience building software applications with heavy focus on data systems | 3 | Resume: 2012-2026 (14 years) in software engineering, multiple data-related roles | Interview: **14 years of experience, but focused on integration/interfaces, not data architecture.** Built interfaces and transformations, not data-intensive applications. |
| Strong application development background (not just database administration) | 3 | Resume: Java, C#, JavaScript development across multiple roles | Interview: C# microservices, API development mentioned, but **primary focus is integration/interface engineering, not full application development** |
| Track record of establishing data standards and patterns across engineering organizations | 1 | Resume: No evidence of establishing standards across organizations | Interview: No discussion of establishing standards, patterns, or influencing organization-wide data practices. Worked within existing platforms (Mirth, Kubernetes). |
| Experience leading data migrations and infrastructure modernization initiatives | 2 | Resume: "Migrated Azure VM hosting solution to Kubernetes environment" | Interview: Mentioned migration briefly but **no discussion of leadership role, migration strategy, or zero-downtime approaches** - appeared to be implementation-level involvement |
| Experience with AI/LLM-assisted development tools and agentic software engineering practices | N/A | Resume: No mention | Interview: Not discussed |
| Prior Principal Engineer, Staff Engineer, or senior technical leadership experience | 3 | Resume: "Senior Principal Engineer R&D" at Baxter (2021-2026) | Interview: Title suggests principal level, but **described work scope and decision-making authority seems more senior IC than principal** (didn't drive technology decisions, worked within team decisions) |
| Bachelor's degree in Computer Science or equivalent practical experience | 5 | Resume: BS Computer Science & Mathematics (2012), MS Computer Science (2013), MS Data Science (2018) | Interview: Credible educational background |

**Qualifications Summary:**

Frank has the tenure (14 years) and educational credentials (BS/MS Computer Science, MS Data Science) for a principal-level role, but his **experience scope and impact level don't match the Principal Engineer expectations** for this data architecture role.

**Critical gap:** No evidence of establishing data standards, influencing engineering organizations, or driving architectural decisions. When asked about technology selection, he described passive roles ("our team decided," "business leaders were pushing"). The role requires someone who can lead data strategy across 4-5 application teams - Frank's experience is implementing within teams, not leading across teams.

The "Senior Principal Engineer" title at Baxter may be inflated relative to scope - the work described (building interfaces, converting HL7 to FHIR, creating CDR with RabbitMQ) sounds like strong senior-level execution, not principal-level architecture and influence.

---

## Other/Details

| Criterion | Score | Resume Evidence | Interview Evidence |
|-----------|-------|-----------------|-------------------|
| Healthcare or EDI domain knowledge | 5 | Resume: NextGen (Mirth Connect), CHS, Craneware, Baxter - all healthcare | Interview: Strong healthcare domain knowledge - discussed HL7, FHIR, EDI, medical interfaces, ADT messages, EHR systems. Mentioned GHX competitor (Craneware). This is Frank's strongest area. |
| Experience in enabling team or platform team models | N/A | Resume: No clear evidence | Interview: Built CDR that other teams connected to, but not discussed as enabling/platform team model |
| Experience with autonomous or cross-functional team environments | N/A | Resume: No evidence | Interview: Not discussed |

---

## Overall Assessment

### Key Concerns

1. **Wrong Role Match - Integration Engineer, Not Data Architect:**
   - Resume shows healthcare integration/interface engineer with strong HL7/FHIR expertise
   - Interview confirmed: when asked about core expertise, Frank said "medical interface engineer and data repository"
   - His database experience is using databases as storage backends within integration platforms (Mirth, Kubernetes), not architecting data systems
   - This is a **fundamental role mismatch** - the position requires a data architect who can guide teams on data modeling, technology selection, and performance optimization across diverse application domains

2. **Passive Role in Technology Decisions:**
   - DocumentDB: "our team decided to go with it" - no articulation of why
   - Could not explain architectural trade-offs or technology evaluation process
   - Described business leaders driving decisions ("always looking at costs") rather than architectural recommendations
   - For a Principal role requiring "influence without authority" and guiding teams on data decisions, this is disqualifying

3. **Shallow Architectural Depth:**
   - Performance optimization: only mentioned "indexing" - no discussion of query tuning, execution plans, partitioning, complementary technologies
   - Multi-database architecture: when asked about complementing Mongo with Elasticsearch/relational for complex queries, only discussed indexing
   - No discussion of data modeling patterns, schema evolution, zero-downtime migrations, data ownership boundaries
   - Responses lacked the depth and breadth expected for a Principal Engineer focused on data architecture

4. **Communication Effectiveness Concerns:**
   - Could not clearly articulate architectural decisions or trade-offs when probed
   - Responses were surface-level and lacked the "why" behind technology choices
   - For a role requiring "communicating technical concepts effectively to executives and non-technical stakeholders" and "educating and empowering" teams, this is a critical gap
   - Went off-topic at times (moving story, telescope, cold symptoms)

5. **Narrow Domain Focus:**
   - Extremely strong in healthcare integration (HL7/FHIR/EDI) - this is valuable
   - However, data architecture for GHX spans beyond integration: application databases, data modeling for diverse business domains, warehouse/analytics, ML/AI patterns
   - Frank's experience is deep but narrow - integration platforms, not diverse data architecture challenges

### Key Strengths

- **Strong healthcare domain knowledge** - HL7, FHIR, EDI, medical interfaces, EHR systems, healthcare workflows
- **Hands-on and persistent** - stayed months longer at Craneware to finish solution, demonstrated ownership
- **Programming proficiency** - Java, C#, JavaScript, Python (data science degree)
- **Event-driven integration experience** - RabbitMQ pub-sub, Kafka, multi-tenancy patterns
- **Educational background** - BS/MS Computer Science, MS Data Science

### Fit for Role: 1/5 (Definitely Not)

### Reasoning

This is a **clear pass** due to fundamental role mismatch. Frank is a strong integration/interface engineer with deep healthcare domain knowledge, but this is not a data architecture role. The position requires:

- **Evaluating and selecting database technologies** based on workload, cost, usage patterns → Frank described passive role in technology decisions ("our team decided")
- **Designing data models and architectures** for diverse application domains → Frank's experience is using databases within integration platforms, not designing data models for business applications
- **Optimizing database performance at scale** (query tuning, indexing, execution plans) → Frank only mentioned indexing, no depth on optimization strategies
- **Guiding teams on data decisions** and establishing standards across engineering organizations → No evidence of establishing patterns or influencing across teams
- **Communicating technical concepts effectively** to educate and empower teams → Communication was surface-level and lacked architectural depth when probed

**Most concerning:** Frank accurately self-described his expertise as "medical interface engineer and data repository," not data architect. When asked about architectural decisions, he could not articulate the rationale or trade-offs. For a Principal Engineer role requiring autonomous teams to make sound data decisions with this person's guidance, the ability to explain the "why" and evaluate alternatives is essential.

**What Frank is excellent at:** Building healthcare data integration solutions using integration engines (Mirth/NextGen), converting between medical data standards (HL7/FHIR/EDI), implementing event-driven interfaces with RabbitMQ/Kafka, and understanding healthcare workflows. He would be a strong candidate for a **Senior Integration Engineer** or **Healthcare Interoperability Architect** role focused on interface engines and medical data standards.

**What this role needs:** A data architect who has built data-intensive applications, designed data models for complex business domains, evaluated and selected database technologies based on technical analysis, optimized query performance at scale, and established data patterns across engineering teams. The role works "side-by-side with application engineers" on data architecture for their applications - not building integration platforms.

**Recommendation:** ☒ Do Not Advance

---

## Feedback to Agency

**Critical issue:** This candidate is an **integration/interface engineer specializing in healthcare data standards (HL7/FHIR/EDI)**, not a data architect. While he has strong domain knowledge in healthcare and experience using databases within integration platforms, the role requires different expertise.

**Role mismatch specifics:**

1. **Technology selection:** When asked why DocumentDB was chosen over Mongo, candidate said "our team decided to go with it" with no articulation of workload analysis, cost considerations, or architectural trade-offs. The role requires evaluating and recommending database technologies - candidate has been implementing team decisions, not driving them.

2. **Performance optimization depth:** When asked about database optimization beyond indexing, candidate only mentioned "indexing of the database." The role requires query tuning, execution plan analysis, partitioning strategies, understanding when to use complementary technologies (Elasticsearch for search, relational DB for complex queries). Candidate demonstrated surface-level understanding.

3. **Architectural scope:** Candidate's data experience is primarily using NoSQL databases (Mongo/DocumentDB/Cosmos) as storage backends for integration engines (Mirth, Kubernetes-based FHIR repositories). The role requires designing data architectures for diverse business applications, not configuring storage for integration platforms.

4. **Communication at architectural level:** For a Principal role requiring "communicates technical concepts effectively to executives and non-technical stakeholders" and "educates and empowers rather than gatekeeps," the candidate struggled to articulate architectural decisions and trade-offs when probed. This is critical for a role focused on enabling teams.

**What we need:**

- **Application development background** with deep data focus - someone who has built data-intensive applications (not just integration platforms), understands how data fits into broader application architecture
- **Proven track record of evaluating and selecting database technologies** - can articulate "we chose X over Y because of workload pattern Z, cost considerations, and access patterns" with technical depth
- **Advanced data modeling and optimization** - schema design for complex business domains, query performance tuning, understanding multi-database architectures (when to use relational vs NoSQL vs search vs warehouse)
- **Establishing data patterns across teams** - prior experience setting data standards, reviewing application code with focus on data access patterns, guiding teams on data decisions
- **Principal-level communication** - can clearly explain complex technical concepts and architectural trade-offs to both technical and non-technical stakeholders

**Please recalibrate:** "Principal Data Architect for application teams" means someone who can review application code, understand business domain complexity, design data models, optimize query performance, and guide technology selection with clear rationale. Healthcare domain knowledge is valuable but not sufficient - we need someone who can architect data systems across diverse application domains, not implement interfaces within integration platforms.

**Where this candidate would excel:** Healthcare interoperability architect role focused on HL7/FHIR/EDI integration, interface engine platforms (Mirth/NextGen), or senior integration engineer position. His domain knowledge and integration expertise are genuinely strong - just not the right fit for this data architecture role.

---

## Interview Notes

**Transcript processed:** 2026-05-28 Granola transcript (33 min 36 sec)

**Key moments that led to decision:**

1. **Self-described expertise (12:50):** When asked for executive summary, Frank said he's been "working with a lot of medical data standards and APIs and all the rest and how medical data is exchanged." Described as "medical interface engineer and data repository" - not data architect.

2. **Technology selection passivity (23:15):** When asked why DocumentDB over Mongo:
   - Frank: "In this case, it was just a matter of they needed a very specific subset. They didn't need everything from Mongo, and so AWS just created a solution and our team decided to go with it."
   - Could not articulate architectural reasoning beyond "business leaders were always looking at costs"
   - No discussion of workload analysis or technical trade-offs

3. **Performance optimization depth (24:45):** When asked about query optimization and complementary technologies:
   - Frank: "You have to look into exactly what data you're going to be needing to get and how quickly. And what operations are gonna be performed on that, and then configure your database so that it's expecting, and it can return those faster results based on that, and that's just part of the indexing of the database."
   - Only mentioned indexing - no discussion of query tuning, execution plans, partitioning, or complementary technologies
   - When probed further, didn't demonstrate broader architectural thinking

4. **Role scope clarity (29:30):** When Marten explained the role gap between DBA and application teams, Frank asked:
   - "Okay, so and you mentioned that, I mean, like you wanted it, how many teams do you have that are that would be using the data store?"
   - This question suggests Frank sees the role as "providing a data store to teams" rather than "guiding teams on data architecture for their applications"

5. **Career trajectory observation:** Resume shows "Senior Principal Engineer R&D" title at Baxter, but described work (building interfaces, C# microservices, CDR with RabbitMQ) sounds more like senior IC execution than principal-level architecture and influence. When asked about technology decisions, consistently described passive role rather than leadership/architecture role.
