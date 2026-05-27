---
tags:
  - interview-questions
  - principal-engineer
  - data-architecture
candidate: Omprakash Arikeri
date: 2026-05-20
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Questions: Omprakash Arikeri
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-20
**Interviewer:** Marten Engblom
**Stage:** HM Screen (30 min)

---

## Career Overview & Technical Background

**Q: Tell me about yourself, your background, what you work on, and your technical expertise.**

**A:** 23 years in IT across full software development lifecycle. Recent hands-on work with AI tools (Amazon Q, Nova, GitHub Copilot) and agentic AI implementations. Experience spans:
- Cloud services: GCP, AWS, Azure, OpenShift
- Databases: MySQL, Oracle, MongoDB, DynamoDB
- Middleware: Service Bus, SQS, Kafka
- Microservices architecture with Spring framework and Apigee
- Currently at ADP as Principal/Lead Developer handling three integration projects with three different teams
- Previous roles: Pfizer (financial, California state deposits), Bank of New York Mellon (derivatives feeds), ADP healthcare work (Magnitude - legal documents for doctors with Delphi integration), converted MuleSoft ESB to microservices interfacing with Salesforce and Oracle
- Day-to-day: Design, requirements gathering from product owners, writing stories/epics, resource estimation, sprint grooming, code reviews, 30-40% development, 60-70% planning/architecture/design
- Sets up templates for Spring Boot applications, coordinates with third-party services and DevOps for releases across environments

**Q: What's your core skill set - backend, frontend, or data?**

**A:** Started as junior Java developer, progressed to senior developer, now in lead experience. "Strongness is in backend" - microservices in middleware handling backend services. Recently focused on architecture and design work, providing architectural solutions and technical decision-making. Has "little knowledge" of React.js for UI - can understand code and find issues but limited coding experience.

---

## Data Architecture & Database Experience

**Q: This role is very data-focused - dealing with large amounts of data, picking the right products for storage, data modeling, flowing data between applications. Tell me more about your experience with databases and data architecture.**

**A:** At Bank of New York Mellon (financial, derivatives):
- Handled large amounts of data from files in S3 buckets
- **Decision point at project start:** Tool-based approach vs. Spring Boot Batch services
- Analysis showed need for resiliency and backup mechanisms for data failures
- Provided multiple proposals with different scenarios: data exchanges, data mappings, multiple file batch flows
- Considered ETL tools as alternative
- **Factors considered:** "How much data we have, how much is cacheable, how much we need to store, how fast we need to retrieve"
- "All about resiliency - how long we want to store the data"
- Eventually chose Spring Boot Batch microservices due to "advantages and availability of resources"

At Pfizer (deposits project):
- Converting to online system for deposits
- Capturing account details with security focus
- Handling account numbers and assessments with data masking
- Using vaults for secure data storage

At ADP:
- Middleware layer fetching data from monolith systems to provide to UI
- Uses DynamoDB for temporary data storage and reprocessing
- Schema design considerations: columns, indexes for fast fetching, searchable vs. durable data

**Q: What are the different databases or data stores you have experience with?**

**A:** "Working from past 20 years" - experience starts with MySQL, then Oracle database. "Recent past" using MongoDB and DynamoDB. **Note:** 4 total databases mentioned across 23-year career.

**Q: What are some things you have to consider when deciding where to store your data?**

**A:** 
1. **Data size:** How large is the data?
2. **Access patterns:** Frequent access vs. read-only vs. needs edits
3. **Read-only optimization:** Views for easy searches, quick searches
4. **Schema planning:** How to plan data storage - keys are "very important" (primary, secondary, shard keys)
5. **Indexing:** Indexes on keys for search purposes
6. **Views:** Depends on request types being handled
7. **Oracle-specific:** Table spaces, normalization
8. **NoSQL:** Data as JSON objects - how to construct the object. At ADP designed JSON structure for request/response objects
9. **Primary keys:** Important for handling
10. **Complex queries:** Whether PLSQL procedures needed (notes "old way, not hearing much plsql these days")
11. **Legacy systems:** Finding ways to reuse PLSQL queries with criteria
12. **Caching:** "Second thing I need to mention" - caching mechanisms help in retrieval of large amounts of data for searches

**Note:** Answer was high-level and generic - didn't demonstrate deep architectural thinking or trade-off analysis.

**Q: Can you think of a scenario where you would need all three types of databases - relational, NoSQL, and document DB?**

**A:** 
- **Relational for metadata:** "A lot of scenarios where we need to store metadata of files" - saves file metadata, fetches with keys, maps data, constructs file. "Very very helpful" for metadata scenarios. Good for generic columns, normalization, static columns.
- **NoSQL for searches:** "A lot of searches" with no relationships, many inner objects. Read-only databases. "Very faster actually" but with drawback: "Cannot get huge amounts of data" - AWS can only fetch 5MB of data per transaction, making it "hectic to use AWS database when fetching large huge amounts of data"
- **Use relational for large data:** When fetching huge amounts
- **Use NoSQL for light data:** Processing on the fly
- **GraphQL mention:** "One of the thing which helps in searches" in NoSQL scenarios
- **Caching:** Added as additional important mechanism for database retrieval

**Note:** Conflated NoSQL and document databases, showed confusion about database types. GraphQL is a query language, not a database feature. Answer lacked concrete real-world examples from his experience.

---

## Cross-Team Collaboration & Influence

**Q: This role involves working across a dozen or so engineering teams, helping them see what good looks like and executing toward that vision. Tell me about your experience influencing without direct authority.**

**A:** Several examples provided:

**Pfizer - Shared databases:**
- Had incoming data but couldn't have own databases, had to use shared databases
- Set up meetings to explain data schema
- Explained "why we have these keys, why we don't have these keys, how much resilience you want"

**Kafka usage:**
- Cannot have individual standalone systems, must use shared resources
- Provided sample Kafka objects
- Provided stats: "How much KB of data we use per request"
- Interacted with teams to get accounts set up

**ADP - Multi-module integration:**
- Integrating with Workforce software application divided into three modules: clock punching, time periods, time off
- Background processes running across modules
- "How frequently data should be collected, how frequently sent to backend systems"
- Third-party payroll data integration team coordination
- Syncing with resources, determining objects used by both sides
- **Handling disagreements:** "Elongated meetings" with product owners to determine if requirements are necessary, prioritize, create architecture diagrams
- Going back to table to discuss and reach agreement

**Architecture team interaction:**
- Project ready but architecture team wants to implement policies and processes
- Data masking requirements for critical columns (SSN)
- Cannot have account numbers directly - must use vault services for encryption/decryption
- Talking to different groups to ensure project has everything required
- Creating architecture diagrams
- Integrating with different teams for project execution

---

## Closing Questions

**Q: Any questions for me?**

**A: What kind of projects - existing integration or new products needing design?**

Response: Mix of both. Breaking up monolith, dependencies in data layer. Multiple applications sharing databases, not using right products. Blocking and tackling needed, but reason is long backlog of innovation and new product development. Limited by technical debt payback needed first.

**A: Does company allow AI tools or are they restricted?**

Response: Very good situation - zeroed in on Claude and Anthropic tools. Every engineer has unlimited access to Claude Code and Claude Co-work. Working on end-to-end AI-enabled SDLC beyond individual use. Figuring out orchestration layer (combination of GitHub and Claude). Well-resourced, have all tools wanted.

**Q: What's your experience with AI tools?**

**A:** At ADP, developed six or seven microservices using Amazon Q and Nova:
- Two or three microservices "totally out of" AI - provided requirement, got back code and test cases
- "Totally driven by AI"
- Human role: Check if inputs/outputs are good, make changes from business perspective, assess microservice flexibility
- Currently involved in initiative to develop "agentic AI" for ADP Assist (question-answering)
- Using MCP servers to utilize existing API calls
- "Proactively give answers more relative to the question in a faster mode"
- Currently in process of implementing

**A: Tech stack - Java-oriented or flexible with Python?**

Response: Java on backend, TypeScript on frontend currently. Exact technology becoming "less and less important" with agentic assistance - knowing exact language less important. But that's current stack.

---

## Red Flags / Concerns

**1. Communication Issues:**
- Answers were long, rambling, and often tangential
- Struggled to provide concise, direct responses
- Went off-topic frequently - when asked about databases, spent significant time on security, vaults, masking
- Used vague language: "kind of", "you know" repeatedly, "actually" as filler
- Difficulty articulating technical concepts clearly
- For Principal role requiring "educates and empowers," poor communication is disqualifying

**2. Limited Database Depth:**
- Only 4 databases in 23 years: MySQL, Oracle, MongoDB, DynamoDB
- No mention of PostgreSQL, SQL Server (both listed in job requirements)
- No data warehouse experience (Snowflake, Redshift)
- No vector databases or RAG patterns for ML/LLM applications
- Generic, textbook answers lacking real-world architectural depth
- When asked about database selection criteria, gave high-level checklist rather than nuanced trade-off analysis

**3. Incorrect/Confused Technical Terms:**
- Conflated NoSQL and document databases as separate categories
- Mentioned GraphQL as if it were a database feature/type
- Understanding of database taxonomy appears superficial

**4. Software Engineering Manager Background:**
- Interviewer's initial impression: "Seems like more of a software engineering manager than a data engineer/architect"
- 60-70% planning/architecture/design, 30-40% development
- Expertise is in managing teams and microservices integration, not deep data architecture
- Resume shows progression toward management/leadership, not deeper technical specialization in data

**5. Missing Critical Experience:**
- No event-driven architecture discussion (Kafka mentioned only as middleware, not for CDC or data replication)
- No zero-downtime migration examples
- No data modeling depth (temporal models, event sourcing)
- No database performance optimization specifics (query tuning, execution plans, indexing strategies)
- No cloud cost optimization discussion
- No data quality, monitoring, observability practices mentioned

**6. Role Mismatch:**
- Job requires "works side-by-side with application engineers" - this is a hands-on enablement role
- Candidate's recent focus is coordinating multiple teams and 60-70% planning
- Not the "hands-on and takes ownership" profile described in job requirements
- Role needs someone who "can architect complex data systems AND roll up sleeves to optimize them" - candidate leans toward coordination/management

---

## Interviewer Notes

**Overall Impression:** Better than previous candidate but still a pass. Not deep enough experience in data architecture and engineering. Communication is "a bit shaky." Background appears more software engineering management than data engineering/architecture despite "knowledgeable in the data space given his roles."

**Key Disconnect:** Resume shows 23 years of broad experience, but interview revealed:
- Limited database diversity (4 databases)
- Generic understanding of data architecture decisions
- Communication challenges that would impair enablement role
- Management/coordination focus rather than deep technical hands-on data work
- Missing most of the specialized data skills in the scorecard (performance optimization, advanced modeling, cloud data platforms, data warehouses, ML/LLM data architecture)
