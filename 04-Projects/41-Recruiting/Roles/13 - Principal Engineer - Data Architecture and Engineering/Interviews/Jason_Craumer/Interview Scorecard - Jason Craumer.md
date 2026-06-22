---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Jason Craumer
date: 2026-05-29
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Scorecard: Jason Craumer
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-29
**Stage:** HM Screen (36 min)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | 2 | Resume: PostgreSQL, MySQL, Oracle listed in skills | Interview: Only mentioned "relational database" for GIS portal with subqueries - minimal technical depth shown |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB) | 1 | Resume: MongoDB, DocumentDB (AWS) listed | Interview: **MAJOR DISCONNECT** - Claims DocumentDB is faster than MongoDB due to "lock management" but DocumentDB IS MongoDB-compatible. Called DynamoDB a "document database" (it's key-value). Demonstrates fundamental misunderstanding |
| Database performance optimization at scale | 3 | Resume: "data access patterns optimized for high-throughput ingest and query performance" | Interview: Mentioned query tuning and subqueries but didn't demonstrate deep optimization knowledge. More focus on pipeline throughput than database tuning |
| Advanced data modeling and schema design | N/A | Resume: "schema design and data access patterns" mentioned | Interview: Not discussed in detail |
| Application development skills | 2 | Resume: Python/Django, REST APIs, Java | Interview: Built internal portals (Django document server, Flask upload app) but limited evidence of complex application development. More infrastructure-focused |
| Can review application code and architecture | 3 | Resume: "Led architecture and code review for data access patterns" for 8 data scientists | Interview: Confirmed code review role but context was reviewing data scientists' code, not application architecture review |
| Experience evaluating and selecting database technologies | 1 | Resume: Multiple database technologies listed | Interview: **Red flag** - MongoDB/DocumentDB confusion shows weak evaluation framework. "Look at pros and cons" without demonstrating actual evaluation criteria |
| Cloud data platform expertise (AWS, Azure, GCP) | 3 | Resume: AWS, GCP, Docker, Kubernetes, Terraform/IaC | Interview: "Good working knowledge of GCP and AWS" with admin roles. Used GCP Big Data, but depth unclear |
| Data warehouse design and implementation | N/A | Resume: Built "centralized data warehouses" in earlier roles | Interview: Not discussed in technical depth |
| ETL/ELT pipeline design and data processing | 4 | Resume: "Built ETL/ELT pipelines reading from Pulsar and Kafka" | Interview: Strong discussion of pipeline architecture - Kafka ingestion, augmentation, downstream distribution. Cited ETL as core expertise. This aligns |
| Event-driven architectures and streaming platforms (Kafka, Kinesis) | 4 | Resume: Apache Kafka, Apache Pulsar, Apache Flink, CDC pipelines | Interview: Detailed Kafka architecture discussion - topics, fail topics, in-transit patterns. Self-identified as Kafka expert |
| Data architecture for ML/LLM applications | 2 | Resume: "Integrated LLM-augmented workflows" and "evaluated embedding and RAG patterns" | Interview: Not discussed. Resume claims seem recent but no depth shown |
| Zero-downtime data migration | N/A | Resume: "zero-downtime migrations" mentioned twice | Interview: Not discussed |
| Data quality, monitoring, and observability | 3 | Resume: Splunk environment monitoring, anomaly detection, ML-augmented alerting | Interview: Discussed Grafana and Splunk for monitoring Kafka queues and alerting. Legitimate operational experience |
| Aligning data ownership models with domain boundaries | N/A | Not mentioned | Not discussed |
| Hands-on troubleshooting and optimization | 3 | Resume: 99% uptime on distributed Splunk, anomaly detection | Interview: Data type casting troubleshooting examples (helping data scientists). More operational troubleshooting than application-level |
| Programming languages (Python, Java, JavaScript/TypeScript, C#) | 3 | Resume: Python, Django, Java, JavaScript, Bash, SQL | Interview: Heavy Python emphasis ("hundreds of APIs"), Django, Flask, Java mentioned. No TypeScript or modern frontend discussion |

**Critical Disconnect:** Candidate demonstrates fundamental confusion about database technologies central to the role. Claims DocumentDB has better "lock management" than MongoDB - **but DocumentDB IS a MongoDB-compatible database from AWS**. Calls DynamoDB a "document database" when it's primarily key-value. For a Principal Data Architecture role requiring teaching and enabling teams, this level of misunderstanding is disqualifying.

**Skills Summary:**

Jason has legitimate experience in **data pipeline infrastructure** and **streaming platforms** (Kafka, Flink). The ETL work and event-driven architecture discussion showed real depth, and this aligns with his resume. He's clearly been hands-on with operational data systems at scale.

However, the **database technology understanding is concerningly weak**. The MongoDB/DocumentDB confusion is not a minor slip - it reveals he doesn't understand that DocumentDB is AWS's MongoDB-compatible service. For someone claiming database expertise and recommending technology choices, this is a critical gap.

The **application development background is thin**. Most examples are internal operational tools (Django portals, Flask apps for data uploads). Little evidence of designing applications with complex business domains or working embedded with product teams. The resume emphasizes platform and infrastructure work over application architecture.

**Most concerning for this role:** The position requires **enabling application teams** to make good data architecture decisions. If the candidate cannot correctly explain database technology tradeoffs, they cannot effectively teach and enable others. The database confusion combined with heavy ops/admin focus suggests this is a data platform operator role, not a Principal Engineer who guides application teams.

---

## Personality Traits Assessment

| Trait | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Enabling mindset - succeeds by making others successful | 2 | Resume: "mentored engineers on platform patterns and best practices" | Interview: Discussed helping data scientists with data type issues. However, examples lean toward solving problems FOR people rather than teaching them to solve problems |
| Educates and empowers rather than gatekeeps | 2 | Resume: "technical lead, conducting code reviews" | Interview: Limited signal. Built self-service portals (positive) but didn't demonstrate teaching/empowerment approach |
| Hands-on and takes ownership | 4 | Resume: "Built," "Operated," "Administered" throughout | Interview: Clear hands-on orientation. Built systems end-to-end (Django portals, Kafka pipelines). Takes ownership |
| Can influence without authority | N/A | Not clear from resume | Not discussed |
| Pragmatic judgment - speed vs. perfection | 3 | Resume: Self-service platforms replacing manual processes | Interview: Document portal example shows pragmatic solution (turn 40 hrs/week manual work into automated system). Good pragmatism |
| Comfortable with ambiguity and building from scratch | 3 | Resume: Built multiple platforms from scratch | Interview: Examples of building portals from scratch. Comfortable building solutions |
| Works effectively in agile/iterative processes | N/A | Not mentioned | Not discussed |
| Collaborates effectively across teams | 3 | Resume: "Partnered with data scientists as technical lead" | Interview: "Worked with IT" for data pulls. Some collaboration examples but not deeply demonstrated |
| Communicates technical concepts to executives | 2 | Resume: "translate architecture decisions to both engineering teams and executive stakeholders" | Interview: **Question** - Given database technology confusion, ability to translate concepts to executives is doubtful. Did mention "executive-level readouts" in earlier roles |

**Personality Traits Summary:**

Jason is clearly **hands-on** and comfortable building solutions from scratch. The document portal example (converting 40 hrs/week manual work to self-service) shows pragmatic problem-solving.

However, the **enabling mindset** signal is weak. Examples lean toward "I built a solution" or "I helped them fix data types" rather than "I taught the team to evaluate tradeoffs" or "I established patterns the team can apply." For a Principal role in an enabling capacity, this is a gap.

The **communication concern** is significant. The resume claims ability to "translate architecture decisions to executive stakeholders," but the interview revealed confusion on foundational database concepts. You cannot effectively communicate what you don't understand.

---

## Qualifications Assessment

| Qualification | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| 10+ years hands-on experience building software applications | 3 | Resume: 27 years total at Verizon, past ~7 years in Principal role | Interview: **Mixed** - Heavy infrastructure/operations focus. Less "building software applications" and more "building data platforms and internal tools" |
| Strong application development background (not just DBA) | 2 | Resume: Application Engineering section, Python/Django apps | Interview: Built internal portals and tools. Limited complex application development. **More platform operator than application architect** |
| Track record establishing data standards and patterns | 3 | Resume: "enforced engineering standards" and "served as Git admin" | Interview: Established standards for data scientists' code. Scope unclear - team of 8 vs. org-wide |
| Experience leading data migrations and modernization | N/A | Resume: "zero-downtime migrations" mentioned | Interview: Not discussed |
| Experience with AI/LLM-assisted development | 2 | Resume: "Integrated LLM-augmented workflows and agentic AI tooling (Claude, CoPilot, ChatGPT)" | Interview: Not discussed. Resume claims recent but no signal in interview |
| Prior Principal Engineer, Staff Engineer experience | 5 | Resume: "Principal Software Engineer" (May 2018 - Dec 2025) | Interview: Confirmed Principal title, led 5-person architecture team. Clear senior IC experience |
| Bachelor's degree in CS or equivalent | 5 | Resume: Bachelor of Science, Computer Information Systems, Strayer University, GPA 3.93 | Confirmed |

**Qualifications Summary:**

Jason meets the **seniority and years of experience** criteria on paper - 27 years at Verizon with 7+ years as Principal Engineer. He's been a senior IC with appropriate title.

However, the **"strong application development background (not just DBA)"** requirement is not met. The background is actually the inverse: **strong infrastructure/operations background, not application development**. He's more data platform operator than application architect. The interview focused heavily on administration (Kafka admin, Flink admin, Splunk admin, system admin, PKI management).

The **AI/LLM experience** on resume seems recent (mentions Claude, CoPilot, ChatGPT) but wasn't discussed in interview, raising questions about depth.

**Critical gap:** Role requires "embedded with app teams" orientation. Jason's background is **network operations at a telecom company** - very different context than product engineering at a healthcare software company.

---

## Other/Details Assessment

| Criterion | Score | Resume Evidence | Interview Evidence |
|-------|-------|-----------------|-------------------|
| Healthcare or EDI domain knowledge | 1 | None - 27 years at Verizon (telecom) | None - Asked basic questions about GHX. Comment: "I don't know if you do a lot of geospatial" |
| Experience in enabling team or platform team models | 2 | Resume: "mentored engineers" | Interview: Built self-service portals (enabling pattern) but little discussion of enabling team models |
| Experience with autonomous/cross-functional teams | N/A | Not clear | Not discussed |

---

## Overall Assessment

### Key Concerns:

1. **Fundamental database technology confusion:**
   - Claims DocumentDB has better "lock management" than MongoDB, but **DocumentDB IS MongoDB** (AWS's MongoDB-compatible service)
   - Called DynamoDB a "document database" when it's key-value
   - For a **Principal Data Architecture role**, this is disqualifying - cannot teach what you don't understand

2. **Not an application developer - infrastructure/operations background:**
   - Resume shows 27 years at Verizon in network operations context
   - Interview emphasized administration: Kafka admin, Flink admin, Splunk admin, system admin, PKI/certificate management
   - Application examples are internal operational tools (Django portals), not product applications
   - Interviewer's raw notes flag: "Heavy on Administration... too admin focus" and "Mentioned networking multiple times... hardware focused??"

3. **Role requires enabling application teams - misalignment:**
   - Position is about working **embedded with product engineering teams** building healthcare software
   - Jason's background is **data platform operations** for internal network operations at telecom company
   - Different domain (telecom vs. healthcare software), different context (network ops vs. product engineering)
   - Examples lean toward "I built the solution" rather than "I enabled teams to make good decisions"

4. **Limited healthcare/EDI domain knowledge:**
   - No healthcare industry experience
   - Asked basic questions about GHX rather than showing domain curiosity or transfer of similar experience

5. **Resume-interview alignment concerns:**
   - Resume emphasizes recent AI/LLM work ("agentic AI," "RAG patterns") but this wasn't discussed at all
   - Resume claims "translate architecture decisions to executive stakeholders" but interview showed gaps in explaining basic database tradeoffs

### Key Strengths:

- **Legitimate streaming and ETL experience** - Kafka, Flink, pipeline architecture discussion was solid
- **Hands-on and ownership mentality** - Clearly builds and operates systems end-to-end
- **Pragmatic problem-solving** - Document portal example (40 hrs/week → automated) shows good instincts
- **Senior IC experience** - Has held Principal title and led technical teams

### Fit for Role: 1/5 (Definitely Not)

**Reasoning:**

This is a **clear pass** for multiple reinforcing reasons:

**Most disqualifying:** The database technology confusion (MongoDB/DocumentDB, DynamoDB mischaracterization) is a **fundamental knowledge gap** for a Principal Data Architecture role. This role requires teaching and enabling application teams to make good database technology choices. If the candidate cannot correctly explain what DocumentDB is (AWS's MongoDB-compatible service), they cannot effectively guide teams.

**Context mismatch:** The role requires working **embedded with application teams** building healthcare software products. Jason's background is **network operations infrastructure** at a telecom company. He's comfortable as a platform operator and administrator, not as an application architect. The interviewer's notes captured this immediately: "Heavy on Administration... too admin focus."

**Application development gap:** The role explicitly requires "strong application development background (not just database administration)." Jason's background is actually the opposite - strong infrastructure/operations focus with limited complex application development. Examples are internal ops tools, not product applications.

**Cannot teach what you don't understand:** Principal Engineers succeed by enabling others. The database confusion combined with ops-heavy background raises serious doubts about ability to educate and empower application teams on data architecture decisions.

The ETL and streaming experience is legitimate, but it's not enough. This role needs someone who thinks like an **application architect with deep data expertise**, not a **data platform operator with admin skills**.

**Recommendation:** ☒ Do Not Advance

---

## Feedback to Agency

**Critical issue:** This is a **context and role mismatch**, not a capability issue.

**What went wrong:**
- Candidate has 27 years at Verizon in **network operations** context - this is infrastructure/telecom, not product engineering
- Role requires **Principal Engineer embedded with application teams** building healthcare software
- Candidate's background is **data platform operations and administration** - Kafka admin, Splunk admin, system admin, PKI management
- The phrase "Principal Software Engineer" on the resume masked a very different role context

**Specific concerns:**
1. **Database technology confusion** - Fundamental misunderstanding of MongoDB/DocumentDB relationship. For a data architecture role requiring teaching others, this is disqualifying.
2. **Heavy administration focus** - Interview centered on admin work (Kafka, Flink, Splunk, system admin). Role needs application architecture thinking.
3. **Limited application development** - Examples are internal operational tools (Django portals). Need someone who's designed complex product applications.

**What we need:**
- **Strong application development background** - has built complex customer-facing applications, not just internal tools
- **Deep database expertise** - can confidently explain technology tradeoffs and guide teams through evaluation
- **Enabling orientation** - track record of establishing patterns and teaching teams, not just building solutions
- **Product engineering context** - experience building software products, not infrastructure/operations platforms
- **Healthcare software or similar domain** preferred (EDI, data-intensive business applications)

**Please recalibrate:** "Principal Engineer for Data Architecture" in our context means **application architect with deep data expertise** who works embedded with product teams. We're not hiring a data platform operator or infrastructure admin. Look for candidates from **product engineering organizations** (SaaS, enterprise software, healthcare IT) rather than telecom/infrastructure companies.

The title "Principal Engineer" exists in very different contexts - make sure future candidates have **product software engineering** backgrounds, not network operations or infrastructure operations.

---

## Interview Notes

**Interviewer's raw notes:**
- Very long time at Verizon (27 years)
- Mentioned networking multiple times... hardware focused??
- Heavy on Administration... too admin focus

**Key moments that led to decision:**

1. **9:13 - Career overview opens with networking:** "I've learned a lot about networking over the years. So obviously, we dealt with mostly network stats and machines, routers, switches, that kind of thing." This immediately signaled infrastructure/ops orientation rather than application development.

2. **24:47 - Expertise discussion heavy on administration:** When asked what he's "extremely good at," the list included: ETL work, Splunk, Kafka administration, data translation, backend administration, system administration. Pattern is clear - operator/admin mindset.

3. **32:15-33:50 - Database technology confusion (most damaging):**
   - Claimed DocumentDB has better "lock management" than MongoDB
   - **DocumentDB IS MongoDB** (AWS's MongoDB-compatible service)
   - Called DynamoDB a "document database" (it's key-value)
   - For Principal Data Architecture role, this reveals fundamental gap

4. **Throughout - Limited application architecture discussion:** Most technical depth was on pipelines, Kafka topics, alerting, monitoring. Less depth on schema design, data modeling, application-level patterns. Examples were operational tools, not product applications.

The interviewer's instincts were correct from the start - "hardware focused" and "too admin focus" captured the core issue. The database technology confusion confirmed that this is not the right role match.
