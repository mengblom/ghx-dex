---
tags:
  - resume
  - principal-engineer
  - data-architecture
candidate: Chas Narne
date: 2026-05-21
location: Pittsburgh, PA
---

# Resume: Chas Narne

**Contact:**
- Email: chas.narne@gmail.com
- Location: Pittsburgh, PA

---

## Summary

Principal Software Engineer with 13+ years architecting enterprise-scale cloud platforms and leading technical modernization initiatives across healthcare, logistics, and aerospace industries. Proven track record building high-reliability, financially correct distributed systems in regulated environments.

---

## Core Competencies

- Cloud computing
- Distributed architecture
- Microservices – Microlith
- Event-Driven architecture
- Software Integration
- API Development
- Team Management

---

## Skills

**Languages:**
- Java (Spring/Hibernate)
- Groovy
- Kotlin
- TypeScript/JavaScript
- Python
- SQL / PL-SQL

**Cloud & DevOps:**
- AWS (Core Services)
- Azure (AKS/ K8s)
- Docker
- Gitlab CI/CD, Jenkins
- Helm
- Terraform
- Cloud Foundry, VMWare

**Data & Streaming:**
- Kafka / RabbitMQ
- PostgreSQL, Oracle
- MongoDB, CouchDB
- Neo4J
- Elasticsearch / ELK stack
- Redis
- Monstache

**APM:**
- Dynatrace
- AppDynamics
- NewRelic
- Datadog

**Frontend & Viz:**
- Angular
- React

**SDLC Methods:**
- Agile/SCRUM
- Kanban
- LEAN
- SAFe

**AI-Augments:**
- Claude (Code/Cowork)
- Codex
- Cursor
- Gitlab Duo
- OpenClaw

---

## Experience

### Principal Software Engineer | SAE International
**May 2021 - Present** | Warrendale, PA

- Led modernization of a legacy monolith into 40+ cloud-native microservices on AWS using Java 17+, Spring Boot, and event-driven architecture with Kafka and RabbitMQ
- Architected Change Data Capture solutions across NoSQL (MongoDB) and relational databases (PostgreSQL, Oracle), enabling real-time data synchronization across legacy and cloud-native services
- Implemented idempotent event processing patterns ensuring fault-tolerant, zero-duplication message delivery across distributed systems
- Built and maintained CI/CD pipelines using GitLab CI/CD, automating build, test (unit, e2e, smoke), and deployment workflows across cloud environments
- Established unit and integration testing standards across microservices using JUnit and Spring Boot Test, improving test coverage and contributing to a 60% reduction in production support incidents
- Mentored junior and mid-level engineers through code reviews, architectural walkthroughs, and pairing sessions, elevating team-wide proficiency in Spring Boot microservices and cloud-native patterns
- Reduced cloud infrastructure costs by auditing Kubernetes pod utilization across services and rightsizing deployments from 'n' replicas to 1 for low-traffic workloads, cutting compute overhead without impacting availability

### Senior Software Engineer | Philips Respironics
**June 2018 - December 2020** | Murrysville, PA

- Built core ingestion and processing services for the "Care Orchestrator" platform using Java 17+, Spring Boot, and JPA (Hibernate), handling massive streams of IoT telemetry data (EDF files) from 50,000+ patient devices persisting in NoSQL (MongoDB) and relational data stores
- Designed and consumed RESTful APIs to parse, enrich, and deliver proprietary device data with 100% integrity for clinical decision-making
- Worked across NoSQL (MongoDB) and relational data stores, optimizing data access patterns for high-throughput ingestion workloads
- Built HIPAA-compliant Spring Boot and Node JS backend services with strict data security, auditability, and compliance requirements

### Senior Programmer Analyst | FedEx Services
**April 2013 - June 2018** | Moon Twp, PA

- Developed Vision-AWAD, a geospatial web platform for real-time package delivery optimization, built on Java and Angular, integrating third-party ArcGIS and Pitney Bowes APIs to process and visualize high-volume logistics data across a national fleet
- Led the technology selection process for the enterprise reporting platform, executing multiple POCs to evaluate scalability, cost, and integration capabilities
- Drove cloud-readiness initiative by re-platforming the application onto an on-prem hypervisor, decoupling it from bare-metal dependencies in preparation for cloud migration
- Integrated multiple third-party APIs for address cleansing and confidence scoring across large-scale transaction datasets

### Junior Engineer | Zycron, Inc. (FedEx Express)
**July 2012 - April 2013** | Memphis, TN

- Maintained the "Customer Impact Analysis" system, a mission-critical Java financial application calculating the monetary impact of weekly fuel price fluctuations on millions of shipping customers – requiring strict data accuracy, auditability, and regulated reporting compliance
- Modernized the application architecture by upgrading the technology stack (WebLogic, Java/Spring) and enforcing security compliance protocols across the codebase
- Streamlined development workflows by automating manual test cases, resulting in a 25% reduction in testing overhead and faster iteration cycles

---

## Education

**Master of Science, Computer Information Science**
University of Alabama - Birmingham | 2009 - 2012 | Birmingham, AL

**Bachelor of Technology, Information Technology**
Jawaharlal Nehru Technological University | 2005 - 2009 | Hyderabad, India

---

## Resume vs. Interview Observations

### Strengths on Resume:

**Exceptional technical depth and breadth:**
- 13+ years continuous software engineering experience with clear progression: Junior Engineer (2012-2013) → Senior Programmer Analyst (2013-2018) → Senior Software Engineer (2018-2020) → Principal Software Engineer (2021-present)
- **Current principal-level role (4 years)** with legitimate scope: 40+ microservices, cross-team standards, mentoring, architecture decisions
- **Healthcare domain experience:** Philips Respironics (2018-2020) with HIPAA compliance, clinical data integrity requirements - directly relevant to GHX
- **Strong modernization track record:** Led monolith → 40+ microservices migration at SAE (exact problem GHX is solving)
- **Event-driven architecture expertise:** Resume highlights Kafka, RabbitMQ, CDC, idempotent processing - all backed up by interview
- **NoSQL depth:** MongoDB across multiple roles (SAE, Philips), not just surface-level usage
- **AI-assisted development:** Lists Claude, Cursor, Gitlab Duo under skills (2024+ addition based on format) - shows staying current
- **Education exceeds requirement:** MS in Computer Information Science (requirement was BS or equivalent)

**Quantified accomplishments:**
- "60% reduction in production support incidents" (testing standards)
- "50,000+ patient devices" (scale at Philips)
- "40+ cloud-native microservices" (scope at SAE)
- Clear cost optimization impact (K8s rightsizing)

**Resume signals enabling mindset:**
- "Mentored junior and mid-level engineers through code reviews, architectural walkthroughs, and pairing sessions, elevating team-wide proficiency"
- "Established unit and integration testing standards across microservices" (cross-team influence)

### Interview Performance - Strong Alignment:

**Core skills demonstrated in depth:**

1. **Data modeling philosophy:** Interview revealed this is THE core competency - "If you come up with a good data model, then it's extremely easy to come up with good APIs." This goes beyond resume bullets to show fundamental thinking approach.

2. **MongoDB expertise validated:** Resume shows MongoDB across roles; interview demonstrated deep internals knowledge (CAP theorem, write concerns CP vs AP, TTL patterns, operational logs, denormalization challenges). Not just used it, understands it.

3. **Event-driven architecture in practice:** Resume mentions Kafka/RabbitMQ; interview provided specific use cases (Kafka for 10-minute audit aggregation window, RabbitMQ for 300-500ms sync, decision framework "Is user waiting?"). Theory → practice validated.

4. **Strangler pattern:** Resume implies modernization work; interviewer noted candidate "naturally mentions strangler pattern" - architectural thinking is second nature, not memorized responses.

5. **Enabling mindset confirmed:** When asked about working across teams on data strategy, immediate response: "That's kind of my day job. I work across teams established standards and align high level architecture improvement on a from a data and consistency perspective." Resume claim → interview validation.

6. **Communication strength observed:** Interviewer directly noted "Great communicator, effective to the point." First-hand observation validates resume's implied communication ability.

7. **AI enthusiasm exceeds expectations:** Resume lists AI tools; interview revealed "Last six months = best engineering time of career" with Claude, building feature migration automation with PRD + code generation. "Creating apps faster than can use them." Passion evident, not just checkbox.

### Minor Disconnect (Not Disqualifying):

**Cloud managed services depth:**

- **Resume impression:** Lists "AWS (Core Services)", mentions cloud cost optimization (K8s rightsizing), Azure AKS/K8s. Creates impression of deep AWS managed services expertise.

- **Interview reality:** When asked about managed data stores experience, said "Very little in AWS realm, just as a proof of concept" for DynamoDB. RDS migration from on-prem Oracle mentioned. Explained SAE work was more lift-and-shift architecture (EC2 instances from data center).

- **Assessment:** Resume shows AWS work (accurate), but it's more infrastructure/K8s-focused than managed database services-focused. Interview clarified that AWS experience is real but oriented toward compute (containers, K8s) rather than managed data services (DynamoDB, Aurora, etc.). Still uses PostgreSQL, MongoDB, Oracle - mostly self-managed or RDS.

- **Why it's not a problem:** 
  - Role emphasizes data modeling, application-level data architecture, and guiding teams on storage decisions - not infrastructure/cloud platform expertise
  - Has strong cloud architecture thinking (strangler pattern, event-driven design, cost optimization mindset)
  - Already working with similar tech stack to GHX (MongoDB, PostgreSQL, Java/Spring Boot)
  - Can ramp on AWS managed services if needed - fundamentals are strong
  - Self-managed MongoDB experience is valuable given GHX uses self-hosted MongoDB currently

### No Other Disconnects Detected:

**Every other area showed strong resume-interview alignment:**
- Monolith modernization: Resume claims it, interview described it in detail (Oracle 300 tables → MongoDB + Elasticsearch, incremental user migration)
- Testing standards: Resume mentions establishing them, interview confirmed "day-to-day involves a lot of code reviews" and cross-team standards work
- Healthcare domain: Resume shows Philips role, interview discussed it first (medical device data, clinician permissions, clinical decision-making)
- Pragmatic judgment: Resume shows time-to-market migration, interview explained "MongoDB first choice due to time-to-market, then circled back 50/50"
- Hands-on: Resume shows principal but still implementing, interview confirmed "enjoy getting hands dirty with proof-of-concept work"

### Assessment:

**This is a high-integrity candidate.** The resume accurately represents experience, skills, and accomplishments. The interview validated and deepened understanding of the work, revealing sophisticated thinking (data modeling philosophy, CAP theorem trade-offs, sync vs async decision framework) that goes beyond what any resume can capture.

The one small disconnect (AWS managed services depth vs. resume impression) appears to be more about how the resume is read than what it claims. Resume says "AWS (Core Services)" - technically accurate, just more EC2/K8s than RDS/DynamoDB in practice. Interview clarified the nuance. **This is not a credibility concern** - it's additional context.

**Strong recommendation to advance.** Resume created accurate expectations, interview exceeded them in several areas (communication, AI enthusiasm, data modeling depth). The combination of proven track record + relevant domain experience + enabling mindset + strong technical skills makes this an outstanding candidate for the role.

**Cultural fit indicator:** The resume shows someone who stays current (AI tools listed), takes ownership (built, architected, implemented - not just led), and enables others (mentoring, establishing standards). Interview confirmed this isn't resume polish - it's how the person actually works. "That's kind of my day job" when asked about enabling teams across data architecture decisions - perfect alignment with role requirements.
