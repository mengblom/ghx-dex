---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Omprakash Arikeri
date: 2026-05-20
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Scorecard: Omprakash Arikeri
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-20
**Stage:** HM Screen (30 min)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | 2 | Resume: Oracle 9i/10g/11g/19c, MySQL, DB2, Postgres listed | Interview: Only mentioned Oracle and MySQL from experience. Postgres listed on resume but never discussed. No SQL Server mentioned. Limited to 4 databases across 23 years. |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB) | 2 | Resume: MongoDB Atlas, DynamoDB listed | Interview: Only MongoDB and DynamoDB discussed. Conflated NoSQL and document DB as separate categories. No depth demonstrated - just "used them recently." |
| Database performance optimization at scale (query tuning, indexing, execution plans) | 2 | Resume: No specific performance optimization mentioned | Interview: Mentioned indexes and views generically. No query tuning specifics, no execution plan analysis, no real-world optimization examples. Generic textbook-level knowledge. |
| Advanced data modeling and schema design (temporal models, event sourcing, complex domains) | 1 | Resume: No advanced modeling mentioned | Interview: Basic schema discussion - keys, normalization. No temporal models, event sourcing, or complex domain modeling discussed. Very surface-level. |
| Application development skills (full-stack, backend, or data-intensive applications) | 4 | Resume: 23+ years SDLC, Spring Boot microservices, full tech stack listed | Interview: Strong backend focus. 30-40% development currently. Confirmed hands-on Spring Boot, microservices. "Little knowledge" of React. Backend-focused application developer. |
| Can review application code and architecture with focus on data access patterns | 3 | Resume: Code reviews mentioned, architecture diagrams | Interview: Does code reviews. Mentioned data access patterns at high level but didn't demonstrate deep pattern analysis. More coordination than deep technical review. |
| Experience evaluating and selecting database technologies based on workload, cost, and usage patterns | 2 | Resume: No technology selection examples | Interview: Bank of NY Mellon example: chose Spring Batch over ETL tools "due to advantages and availability of resources" - not a sophisticated workload/cost analysis. Generic checklist of factors (data size, access patterns) without nuanced trade-off thinking. |
| Cloud data platform expertise (AWS, Azure, or GCP) with cost optimization focus | 2 | Resume: AWS (ECS, CF, Lambda, S3, SQS), GCP, Azure, OCP4 listed | Interview: Mentioned S3 for files, DynamoDB for temp storage. No depth on AWS data services (RDS, Aurora, Redshift). No cost optimization discussion. No GCP or Azure data platform details. Surface-level cloud knowledge. |
| Data warehouse design and implementation (Snowflake, Redshift, etc.) | 1 | Resume: No data warehouse experience mentioned | Interview: Not discussed. No data warehouse experience evident. |
| ETL/ELT pipeline design and data processing architectures | 2 | Resume: DPX-ETL Trade project, Spring Batch, Apache Airflow, Spark | Interview: Mentioned considering ETL tools vs. Spring Batch. Chose Spring Batch. No pipeline architecture depth, no Airflow/Spark discussion despite being on resume. |
| Event-driven architectures, change data capture, and streaming platforms (Kafka, Kinesis, Pub/Sub) | 2 | Resume: Apache Kafka, AWS SQS, enterprise service bus | Interview: Kafka mentioned only as shared resource for coordination. No CDC, no event-driven architecture depth, no streaming platform design. Middleware usage, not architecture. |
| Data architecture for ML/LLM applications (vector databases, embeddings, RAG patterns) | N/A | Resume: Agentic AI, Amazon Q, Nova, GitHub Copilot. Master's in CS (DA, ML, AI) ongoing. | Interview: AI tool usage for code generation. Agentic AI work using MCP servers for API calls. No vector databases, embeddings, or RAG patterns discussed. AI tool consumer, not ML/LLM data architect. |
| Zero-downtime data migration and schema evolution strategies | N/A | Resume: No migrations mentioned | Interview: Not discussed. |
| Data quality, monitoring, and observability practices | N/A | Resume: AppDynamics, Dynatrace, New Relic, Grafana listed as tools | Interview: Not discussed. Tools listed but no practices demonstrated. |
| Aligning data ownership models with domain boundaries | N/A | Resume: No mention | Interview: Not discussed. |
| Hands-on troubleshooting and optimization of production data systems | 3 | Resume: Production support mentioned across roles | Interview: "Support and coordinate during releases and deployments." Troubleshooting mentioned but no deep optimization examples. Support role, not optimization focus. |
| Proficiency in modern programming languages (Python, Java, JavaScript/TypeScript, C#) | 4 | Resume: Java 17/21, Python 3.x, JavaScript, NodeJs, NextJs | Interview: Confirmed Java expertise. "Little bit experience on Python" and "little knowledge of React" - so Java strong, others limited. TypeScript not discussed. |

**Critical Disconnect:** Resume shows broad technology exposure (multiple databases, cloud platforms, AI tools, data processing tools) but interview revealed **limited depth and inability to articulate technical concepts clearly**. 23 years of experience but only 4 databases used, no data warehouse work, no advanced modeling, and generic understanding of database selection trade-offs.

**Skills Summary:**

Candidate presents as a **software engineering manager with generalist backend development experience**, not a data architecture specialist. While the resume lists extensive technologies, the interview exposed significant gaps:

**Missing depth:** Only worked with 4 databases in 23 years (MySQL, Oracle, MongoDB, DynamoDB) - no PostgreSQL in practice, no SQL Server, no data warehouses. When discussing database selection, provided textbook checklists rather than nuanced architectural trade-off analysis. No query optimization examples, no execution plan analysis, no performance tuning depth.

**Communication concerns:** For a Principal role requiring "educates and empowers," communication was problematic. Answers were long, rambling, and tangential. Used excessive filler words ("kind of," "you know," "actually"). Struggled to articulate technical concepts concisely. When asked about data architecture, went off-topic discussing security and vaults. This communication style would impair the enablement aspect of the role.

**Management trajectory:** Currently 60-70% planning/architecture/design, 30-40% development. Focus is on coordinating multiple teams, sprint grooming, resource allocation - software engineering management activities. Not the "hands-on and takes ownership" profile needed for this data architecture enablement role.

**Technology confusion:** Conflated NoSQL and document databases as separate categories. Mentioned GraphQL as if it were a database feature. Understanding of database taxonomy appears superficial.

**Resume-interview gaps:** Resume lists Apache Airflow, Spark, multiple cloud platforms - none discussed in interview. Lists data warehousing project (DPX-ETL) but couldn't articulate pipeline architecture. AI tools listed prominently but only as code generation consumer, not for ML/LLM data architecture.

The role requires someone who can "work side-by-side with application engineers, review their code, understand their challenges, and guide them to better data solutions." This candidate's trajectory is toward team coordination and management, not the deep hands-on data architecture work this role demands.

---

## Personality Traits Assessment

| Trait | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Enabling mindset - succeeds by making others successful | 3 | Resume: "Lead and mentor teams," "code reviews," "helping architecture diagrams" | Interview: Examples of coordinating with teams and setting up shared resources. More transactional (getting accounts set up) than true enablement. Focus on coordination rather than education. |
| Educates and empowers rather than gatekeeps | 2 | Resume: No specific evidence | Interview: **CRITICAL CONCERN** - Communication issues would severely impair ability to educate. Rambling, tangential answers. Cannot explain technical concepts concisely. Gatekeeping not evident, but education ability questionable. |
| Hands-on and takes ownership | 3 | Resume: "Hands-on" mentioned with AI tools, 30-40% development | Interview: Currently 30-40% development, 60-70% planning/coordination. Trending away from hands-on toward management. Does code reviews and some development but increasingly coordination-focused. |
| Can influence without authority | 4 | Resume: Cross-team work mentioned across projects | Interview: Good examples: Pfizer shared databases, Kafka coordination, ADP multi-module integration. Knows how to navigate organizational politics and get agreement through "elongated meetings" with product owners. |
| Pragmatic judgment - knows when to optimize for speed vs. perfection | N/A | Resume: No specific evidence | Interview: Bank of NY Mellon decision (Spring Batch vs ETL) but reasoning was "availability of resources" not speed vs. perfection trade-off. Insufficient signal. |
| Comfortable with ambiguity and building from scratch | N/A | Resume: Some new project mentions | Interview: Not discussed. Most examples were integration work, not greenfield. |
| Works effectively in modern agile/iterative development processes | 5 | Resume: "Agile, Scrum, Sprint grooming, planning, retrospective" throughout | Interview: Strong evidence - sprint grooming, planning, retrospectives across all recent roles. Very comfortable with agile processes. |
| Collaborates effectively across teams (engineering, product, infrastructure, security) | 4 | Resume: Cross-team coordination mentioned | Interview: Multiple examples of working with different teams (databases, Kafka, payroll integration, architecture team, DevOps). Good collaborator. |
| Communicates technical concepts effectively to executives and non-technical stakeholders | 1 | Resume: "Talking with product owners business associates" | Interview: **DISQUALIFYING** - Cannot communicate technical concepts effectively. Rambling, tangential answers even to technical interviewer. Used incorrect terminology. Went off-topic frequently. If struggling to be concise with technical interviewer, communication with non-technical stakeholders would be very poor. |

**Personality Traits Summary:**

Strong agile process experience and cross-team collaboration skills. Can navigate organizational dynamics and get alignment across teams. However, **critical communication deficiency** for a Principal role requiring education and enablement.

**Most concerning:** The job description states this person "educates and empowers" and "communicates technical concepts effectively to executives and non-technical stakeholders." The interview demonstrated the opposite - rambling answers, tangential discussions, difficulty articulating concepts concisely. When asked about database experience, spent significant time discussing security vaults and data masking instead. Used excessive filler language ("kind of," "you know," "actually") throughout.

For a hands-on technical contributor, communication issues might be manageable. For a **Principal Engineer whose primary value is enabling multiple application teams**, poor communication is disqualifying. The role explicitly requires "speaks the language of application engineers and can review their code, understand their challenges, and guide them to better data solutions." This requires clear, concise technical communication - the opposite of what was demonstrated.

The candidate is also trending toward management (60-70% planning/coordination) rather than the hands-on technical ownership this role requires. Good at process and coordination, but the role needs someone who "can architect complex data systems AND roll up sleeves to optimize them" while teaching others.

---

## Qualifications Assessment

| Qualification | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| 10+ years of hands-on experience building software applications with heavy focus on data systems | 3 | Resume: 23+ years SDLC experience | Interview: 23 years confirmed but "heavy focus on data systems" is questionable. Backend microservices development, yes. Data systems specialist, no. Recent work is middleware integration, not data architecture. |
| Strong application development background (not just database administration) | 4 | Resume: Full development stack, microservices, Spring Boot throughout | Interview: Confirmed - strong backend application development background. Started as Java developer, progressed through senior roles. Not a DBA. |
| Track record of establishing data standards and patterns across engineering organizations | 1 | Resume: No standards/patterns work mentioned | Interview: No examples provided. Work was within teams or coordinating with other teams, not establishing organization-wide standards. |
| Experience leading data migrations and infrastructure modernization initiatives | N/A | Resume: No migrations mentioned | Interview: Not discussed. No evidence. |
| Experience with AI/LLM-assisted development tools and agentic software engineering practices | 4 | Resume: Amazon Q, Nova, GitHub Copilot, Agentic AI | Interview: Strong recent experience. Used AI to generate 2-3 full microservices. Currently working on agentic AI initiative using MCP servers for ADP Assist. Up-to-date with AI tooling. |
| Prior Principal Engineer, Staff Engineer, or senior technical leadership experience | 4 | Resume: Principal Software Engineer (current), Lead roles | Interview: Currently Principal/Lead at ADP, previous Lead roles at Fiserv and BNY Mellon. Has the title and team leadership experience. |
| Bachelor's degree in Computer Science or equivalent practical experience | 5 | Resume: B.Tech in CS from JNT University, MS in CS (ongoing) at Georgia Tech | Interview: Not discussed but resume shows both BS and MS (in progress) in CS. |

**Qualifications Summary:**

Meets years of experience (23 years) and has application development background. Current Principal Engineer title and leads teams. Strong on AI tool usage. Pursuing MS in CS from Georgia Tech (Data Analytics, ML, AI focus).

**However, critical qualifications are missing:**
- No track record of establishing data standards across organizations
- No data migration leadership
- Limited data systems depth despite long career

The resume shows progression from developer → senior developer → lead → principal, but the trajectory is toward **software engineering management** (team coordination, sprint planning, resource allocation) rather than deepening technical expertise in data architecture.

"Heavy focus on data systems" is not supported by the evidence. Focus has been backend microservices development with databases as components, not data architecture as the primary discipline. The role requires someone who has specialized in data systems over their career - this candidate has remained a generalist backend developer who progressed into management.

---

## Other/Details Assessment

| Item | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Healthcare or EDI (Electronic Data Interchange) domain knowledge | 3 | Resume: ADP projects, MagMutual (healthcare), Magnitude (doctors' legal documents) | Interview: Mentioned Magnitude healthcare work briefly (Delphi documents for doctors). Not a domain expert but has some exposure. |
| Experience in enabling team or platform team models | 2 | Resume: Lead/mentor teams mentioned | Interview: Team coordination examples but not enabling team models. More traditional project team structure. |
| Experience with autonomous or cross-functional team environments | 3 | Resume: Multiple teams across projects | Interview: Cross-team coordination evident. Autonomous team experience not clear - seems more traditional structure with his coordination role. |

---

## Overall Assessment

**Key Concerns:**

1. **Cannot communicate technical concepts effectively - DISQUALIFYING for Principal role:**
   - Rambling, tangential answers throughout interview
   - Excessive filler words: "kind of," "you know," "actually"
   - Went off-topic when asked about databases (spent time on security, vaults, masking)
   - Used incorrect terminology (GraphQL as database feature, conflated NoSQL and document DB)
   - If struggling to communicate concisely with technical interviewer, cannot effectively educate application engineers
   - **Role requires "educates and empowers" and "communicates technical concepts effectively to executives and non-technical stakeholders"** - this is the opposite of what was demonstrated
   - Interviewer noted: "Communication is a bit shaky"

2. **Limited data architecture depth despite 23 years of experience:**
   - Only 4 databases across 23-year career (MySQL, Oracle, MongoDB, DynamoDB)
   - No PostgreSQL in practice, no SQL Server (both in job requirements)
   - No data warehouse experience (Snowflake, Redshift, etc.)
   - No vector databases or ML/LLM data architecture
   - No zero-downtime migrations
   - No advanced data modeling (temporal models, event sourcing)
   - Database selection reasoning was generic: "availability of resources" not sophisticated trade-off analysis
   - Interviewer noted: "Not deep enough experience in data architecture and engineering"

3. **Role mismatch - trending toward management, not hands-on technical depth:**
   - Currently 60-70% planning/architecture/design, 30-40% development
   - Focus: coordinating multiple teams, sprint grooming, resource allocation, "elongated meetings"
   - This is **software engineering management**, not the hands-on data architecture work the role requires
   - Role needs: "hands-on and takes ownership" and "can architect complex data systems AND roll up sleeves to optimize them"
   - Candidate is moving away from hands-on toward coordination/management
   - Interviewer's initial impression: "Seems like more of a software engineering manager than a data engineer/architect"

4. **Missing critical technical skills:**
   - No database performance optimization depth (no query tuning examples, execution plans, indexing strategies)
   - No event-driven architecture experience (Kafka mentioned only as middleware to coordinate)
   - No data warehouse work
   - No cloud data platform depth (mentioned S3 and DynamoDB only, no RDS, Aurora, Redshift)
   - No data quality, monitoring, observability practices discussed
   - Resume lists technologies (Airflow, Spark, multiple clouds) never discussed in interview

5. **Resume-interview disconnect indicates breadth without depth:**
   - Resume lists extensive technologies but interview couldn't articulate depth in any
   - Listed Postgres but only mentioned Oracle and MySQL from experience
   - Listed data warehousing project (DPX-ETL) but couldn't discuss pipeline architecture
   - Listed Airflow and Spark - never mentioned
   - Listed multiple cloud platforms - only discussed S3 and DynamoDB at surface level
   - **Pattern:** Resume shows technology exposure through employment, not specialization

**Key Strengths:**
- Strong agile process experience and cross-team collaboration
- Recent AI tool experience (Amazon Q, Nova, agentic AI work)
- Can navigate organizational dynamics and achieve alignment across teams
- 23 years of backend development experience with Spring Boot and microservices

**Fit for Role:** 1/5 (Definitely Not)

**Reasoning:**

This is a clear pass for three disqualifying reasons:

**Most critical:** Communication deficiency. The role's primary purpose is **enabling application teams** - the job description states you "work side-by-side with application engineers," "educate and empower," and "communicate technical concepts effectively to executives and non-technical stakeholders." This is fundamentally a **teaching role** wrapped in a technical contribution role. The candidate cannot communicate technical concepts concisely or clearly. Rambling, tangential answers with incorrect terminology and excessive filler language make this person unable to fulfill the core enabling mission. If he struggles to be concise with a technical peer interviewer, he cannot effectively educate and guide application engineers or explain decisions to executives.

**Second concern:** Limited data architecture depth. In 23 years, only worked with 4 databases, no data warehouse experience, no advanced modeling, no migration leadership, no cloud data platform depth. When asked about database selection criteria, gave generic textbook checklists rather than nuanced architectural thinking. The role needs "deep expertise in NoSQL databases" and "deep hands-on experience with relational databases" plus data warehouses, event-driven architectures, ML/LLM data architecture, zero-downtime migrations. Candidate has surface-level exposure to some technologies but no depth in the specialized skills this role demands.

**Third concern:** Role mismatch in trajectory. Candidate is 60-70% coordination/planning (sprint grooming, resource allocation, coordinating teams, "elongated meetings") and 30-40% development. He's trending toward software engineering management, not deepening technical expertise. The role explicitly needs someone "hands-on and takes ownership" who "can architect complex data systems AND roll up sleeves to optimize them" **while enabling others to do the same**. This trajectory mismatch means even if communication improved and he focused on learning data technologies, he's moving in the opposite direction from where the role needs someone.

Interviewer's assessment was correct: "Better than previous candidate, but still a pass. Not deep enough experience in data architecture and engineering."

**Recommendation:** ☒ Do Not Advance

**Feedback to Agency:**

Thank you for submitting Omprakash Arikeri. After a thorough interview, we're passing on this candidate for three critical mismatches:

**Critical issue #1 - Communication:** This Principal Engineer role is fundamentally an **enabling role** - working side-by-side with application engineers to educate and guide them toward better data solutions. The job description explicitly requires "communicates technical concepts effectively to executives and non-technical stakeholders" and "educates and empowers rather than gatekeeps." In the interview, the candidate struggled to communicate technical concepts concisely. Answers were rambling and tangential, with excessive filler words and difficulty staying on topic. When asked about database experience, spent significant time discussing security and vaults instead. For a role where the primary value is teaching and guiding others, clear technical communication is non-negotiable.

**Critical issue #2 - Limited data architecture depth:** Despite 23 years of experience, the candidate has worked with only 4 databases (MySQL, Oracle, MongoDB, DynamoDB) and has no data warehouse experience, no advanced data modeling work, no zero-downtime migrations, and no deep cloud data platform expertise. When discussing database selection criteria, provided generic textbook answers rather than nuanced architectural trade-off analysis. We need "deep expertise in NoSQL databases," "deep hands-on experience with relational databases," plus data warehouses (Snowflake/Redshift), event-driven architectures, ML/LLM data platforms, and performance optimization depth (query tuning, execution plans, indexing strategies). This candidate is a generalist backend developer, not a data architecture specialist.

**Critical issue #3 - Role trajectory mismatch:** The candidate is currently 60-70% planning/coordination (sprint grooming, resource allocation, cross-team meetings) and 30-40% development - trending toward software engineering management. We need someone who is **deepening hands-on technical expertise** and can "architect complex data systems AND roll up sleeves to optimize them." The role requires "hands-on and takes ownership" - someone moving toward more hands-on technical work, not less. This candidate's career trajectory is toward team coordination and management, which is valuable but not what we need here.

**What we need for future submissions:**
- **Data architecture specialist** - someone whose career has specialized in data systems, not a generalist who uses databases as one component among many
- **Strong technical communicator** - can explain complex concepts concisely to both engineers and non-technical stakeholders (this is a teaching/enabling role)
- **Deep hands-on experience** with multiple database technologies, data warehouses, cloud data platforms, and performance optimization
- **Track record of establishing data standards and patterns** across engineering organizations
- **Recent focus on deepening technical expertise** rather than moving toward management/coordination

**Recalibrate around:** "Principal Data Architect **for application teams**" means someone who works embedded with engineers, reviews their code, understands their challenges, and guides them to better solutions while remaining deeply hands-on themselves. It's 70% hands-on technical work, 30% teaching/enabling - not the reverse.

Please reach out if you'd like to discuss the role requirements in more detail to help calibrate future candidates.

---

## Interview Notes

**Interviewer's raw notes:**

- Stated Experiences (mentioned high level as part of intro):
  - GCP, AWS, Azure
  - Distributed systems
  - Multiple Databases
  - Service bus, SQS, Kafka etc.
  - Microservices
- Seems like more of a software engineering manager than a data engineer / architect...
- ... albeit very knowledgeable in the data space given his roles
- Databases / Data stores:
  - MySQL
  - Oracle
  - MongoDB
  - DynamoDB
- Communication is a bit shaky...
- This is better than previous candidate, but still a pass. Not deep enough experience in data architecture and engineering.

**Key moments that led to decision:**

**Moment 1 - Limited database experience (Lines 35-36):**
> Me: "What are the different databases or data stores that you have experience with?"
> 
> Them: "I've been working from past 20 years my experience starts with mysql and I used Oracle database recent past I had been using mongo DB and dynamo DB actually so those are the couple of two nice fields I have a little bit hands on experience."

**Context:** After 23 years in software development, candidate has only worked with 4 databases. No PostgreSQL in practice (despite being on resume), no SQL Server, no data warehouses. For a Principal Data Architect role requiring deep database expertise, this is far too limited.

**Moment 2 - Generic database selection reasoning (Lines 37-38):**
> Me: "What are some things you have to consider when you pick, when you decide where to store your data?"
> 
> Them: [Long answer covering]: "How large your data is," "frequent access or read only," keys (primary, secondary, shard), indexes, views, normalization, JSON objects, PLSQL procedures, caching...

**Context:** Answer was a textbook checklist of considerations, not nuanced architectural thinking about trade-offs. Lacked depth and real-world decision-making examples. For someone with 23 years of experience, expected sophisticated analysis of workload patterns, cost optimization, performance trade-offs - not a generic list.

**Moment 3 - Confused database taxonomy (Lines 39-40):**
> Me: "Can you think of a scenario where you would need all three types of databases - relational, NoSQL, and document DB?"
> 
> Them: [Discusses relational for metadata, NoSQL for searches, mentions GraphQL, discusses AWS 5MB limit, caching...]

**Context:** Conflated NoSQL and document databases as if they're separate categories. Mentioned GraphQL as if it's a database feature. Shows superficial understanding of database taxonomy. Used generic scenarios ("a lot of scenarios where we need to store metadata") rather than concrete examples from his own experience.

**Moment 4 - Communication challenges throughout:**
Throughout interview, answers were rambling with excessive filler words ("kind of," "you know," "actually"). When asked about data architecture, went off-topic discussing security, vaults, and data masking. Struggled to provide concise, direct responses to technical questions.

**Context:** For a Principal role requiring "educates and empowers" and "communicates technical concepts effectively," this communication style is disqualifying. Cannot effectively enable application teams if unable to explain concepts concisely.

**Moment 5 - Career trajectory toward management (Lines 27-28):**
> Them: "...my day-to-day actives involve design like you know talking with the product owners business associates get the requirements converting them into technical documents like you know writing stories for the epics and eventually talking to different teams... estimating the resources of work how much you need to be doing... spring groomings I do code reviews I've been hands-on with the code to like 30 to 40% development 60 to 70% planning architecture design..."

**Context:** Currently 60-70% planning/coordination, 30-40% development. This is software engineering management trajectory, not deepening technical expertise. Role needs someone moving toward more hands-on work, not less. Mismatch with "hands-on and takes ownership" requirement.
