---
tags:
  - resume
  - principal-engineer
  - data-architecture
candidate: Jason Craumer
date: 2026-05-29
interviewer: Marten Engblom
stage: hm-screen
location: New Freedom, PA
---

# Resume: Jason Craumer

**Contact:**
- Email: jcraumer@msn.com
- Phone: 717-968-3856
- LinkedIn: linkedin.com/in/jason-craumer
- Location: New Freedom, PA

---

## Summary

Principal Software Engineer with 27 years of experience designing and operating distributed data platforms at enterprise scale. Built and owned streaming architectures (Apache Kafka, Apache Pulsar, Apache Flink) processing 5TB+ of daily events, application services in Python/Django, and AI/LLM-augmented workflows, all in production at Verizon scale. Comfortable owning the full lifecycle: schema design and data access patterns, zero-downtime migrations, code review, CI/CD, and cloud infrastructure across AWS and GCP. Strong communicator who can translate architecture decisions to both engineering teams and executive stakeholders.

---

## Core Technical Competencies

**Streaming & Data Platforms:** Apache Kafka · Apache Pulsar · Apache Flink · Apache Spark · CDC pipelines · ETL/ELT

**Databases & Storage:** MongoDB · PostgreSQL · DocumentDB (AWS) · MySQL · Oracle · Elasticsearch · Parquet/Arrow · vector databases

**Application Engineering:** Python · Django · Java · REST APIs · JavaScript · Bash · SQL

**AI & ML:** LLMs · RAG (Retrieval-Augmented Generation) · embeddings · agentic AI · ML feedback loops · Claude · CoPilot · ChatGPT

**Cloud & Infrastructure:** AWS · GCP · Docker · Kubernetes · Terraform/IaC · CI/CD · NGINX · HAProxy · F5

**Architecture & Governance:** Distributed systems design · data access pattern review · zero-downtime migrations · data lineage · RBAC/IAM · PKI/SSL

---

## Work Experience

### Principal Software Engineer – Platform & Data Architecture | Verizon
**May 2018 – Dec 2025**

**Streaming & Data Platform**
- Architected enterprise-scale event streaming systems using Apache Kafka and Apache Pulsar with CDC-compatible ingestion, canonical data representations, and both real-time and batch processing, handling 5TB+ of daily events across distributed infrastructure.
- Built ETL/ELT pipelines reading from Pulsar and Kafka into Splunk and downstream analytics systems; designed data access patterns optimized for high-throughput ingest and query performance.
- Operated a distributed Splunk environment (20 search heads, 80 indexers) at 99% uptime; owned monitoring, anomaly detection, ML-augmented alerting pipelines, and automated recovery mechanisms.
- Implemented metadata capture, dataset documentation, data lineage tracking, and ownership attribution to support audit readiness, zero-downtime migration planning, and governance maturity.

**Application Engineering & AI**
- Built a self-service internal platform in Python/Django with custom SAML SSO middleware, replacing manual data-access processes for ~150 Network Operations engineers.
- Developed custom REST APIs to receive feedback from external systems and close an ML feedback loop on production ticket handling, saving 40 hours per week in manual triage.
- Integrated LLM-augmented workflows and agentic AI tooling (Claude, CoPilot, ChatGPT) into engineering and analytics processes; evaluated embedding and RAG patterns for internal knowledge retrieval use cases.
- Automated internal dashboards and reporting workflows enabling self-service analytics across engineering and business stakeholders; administered GIS tools (Carto, HeavyAI) and R Studio on Unix/Docker infrastructure.
- Partnered with data scientists as technical lead, conducting code reviews, driving weekly syncs, and clearing blockers to keep work moving.

**Architecture, Cloud & Security**
- Designed and operated distributed platform services across AWS and GCP: API gateway patterns, SSO/LDAP authentication, data ingestion, and observability pipelines.
- Led architecture and code review for data access patterns, enforced engineering standards, and served as Git admin across team repositories; mentored engineers on platform patterns and best practices.
- Managed PKI/x509 and SSL certificate lifecycle (DigiCert) across distributed server infrastructure; administered OS hardening, patch management, Docker containerization, and F5/load balancer configurations.
- Forecasted $500K+ annual licensing and infrastructure budget; handled $5M+ in operational savings through predictive analytics models on network health KPIs.

---

### Engineer IV – Network Engineering & Operations | Verizon
**Apr 2016 – May 2018**

- Built high-throughput streaming and ETL pipelines processing billions of daily events from 1–5TB sources across distributed systems.
- Administered clustered Splunk environments for operational analytics; automated anomaly-triggered ticket generation contributing to $5M+ in annual network savings.
- Configured HEC endpoints and load balancers to maximize Splunk throughput, achieving a 65% improvement in pipeline efficiency.
- Managed PKI/x509 certificate lifecycle for Splunk clusters; built custom TAs/Add-ons for ingestion pipelines and data baselines used in alerting models.

---

### Consultant – Network Operations / Legal | Verizon
**Jun 2012 – Apr 2016**

- Collected, verified, and managed sensitive subscriber data (PII, CPNI) in compliance with privacy and regulatory standards, maintaining less than 1% error rate at 99% accuracy.
- Partnered with legal teams and law enforcement on time-sensitive, high-stakes data requests; processed court orders, search warrants, and National Security Letters in strict compliance with federal/state regulations.
- Designed new procedures for IP and telephone record collection, redaction, and release, improving efficiency and consistency across the team.

---

### Sr. Staff Consultant – Regional Staff | Verizon
**Jun 2011 – Jun 2012**

- Built a centralized data warehouse integrating multiple external data sources to track technician performance and support data-driven decision-making across the Potomac region.
- Delivered executive-level readouts on performance trends; partnered with underperforming managers on targeted improvement plans.

---

### Supervisor – IT / Fleet / Wireless Operations | Results & Analysis | Dispatch Operations | Verizon
**2004 – Jun 2011**

- Progressed through a series of supervisory roles managing dispatch operations, field force analytics, fleet reporting, and IT support across the Potomac region.
- Consistently built centralized data warehouses, automated reporting workflows, and web-based tracking platforms to replace legacy spreadsheet and Access-based systems.
- Developed forecasting models, KPI scorecards, and operational tools providing real-time visibility to Director- and VP-level leadership.

---

### Operations Center Specialist | Verizon Connected Solutions
**Jan 1999 – Mar 2004**

- Managed daily workload tracking for 60–100 field technicians; developed automated macros and reporting tools standardized across the Verizon footprint.

---

## Education

**Bachelor of Science, Computer Information Systems**
Strayer University, Washington DC | GPA: 3.93

---

## Resume vs. Interview Observations

### Strengths on Resume:

**Legitimate streaming and ETL expertise:**
- Apache Kafka, Apache Pulsar, Apache Flink, Spark - processing 5TB+ daily events
- Distributed Splunk environment (20 search heads, 80 indexers) at 99% uptime
- ETL/ELT pipelines with CDC ingestion and data lineage tracking
- **Interview confirmed:** Strong technical discussion of Kafka architecture, fail topics, in-transit data patterns. This expertise is real.

**Hands-on operational experience at scale:**
- ML-based predictive maintenance system (95% confidence laser failure prediction)
- $5M+ operational savings through analytics
- Infrastructure management: PKI/SSL certificates, Docker, load balancers
- **Interview confirmed:** Document portal example (40 hrs/week manual work → automated) shows pragmatic problem-solving

**Senior IC experience:**
- Principal Engineer title (May 2018 - Dec 2025)
- Led 5-person architecture team
- Managed 8 data scientists (code reviews, Git admin, CI/CD)
- **Interview confirmed:** Clear senior technical leadership experience

---

### Major Disconnects in Interview:

**1. Database Technology Understanding - CRITICAL DISCONNECT:**

**Resume claims:**
- "MongoDB · PostgreSQL · DocumentDB (AWS) · MySQL · Oracle · Elasticsearch" in core competencies
- "Databases & Storage" section suggests deep expertise across multiple database technologies
- Summary states: "schema design and data access patterns"

**Interview reality:**
- **Fundamental confusion about MongoDB vs. DocumentDB:** Claimed DocumentDB (AWS) has better "lock management" and is "more efficient" than MongoDB
- **Critical issue:** DocumentDB IS MongoDB-compatible - it uses MongoDB's wire protocol. This is a basic fact that reveals shallow MongoDB knowledge
- **DynamoDB mischaracterization:** Called it a "document database" positioned "somewhere in the middle" - DynamoDB is primarily key-value store
- **Vague technical reasoning:** "Transactions seem faster" without any technical depth on why or in what scenarios
- **No modern MongoDB knowledge:** No mention of WiredTiger, sharding, replica sets, aggregation pipelines, Atlas features, change streams, time series collections

**Assessment:** For a Principal Data Architecture role, inability to correctly explain database technology tradeoffs is disqualifying. Resume lists databases but interview reveals surface-level understanding.

---

**2. Application Development Background - MAJOR DISCONNECT:**

**Resume claims:**
- "Principal Software Engineer" title
- "Application Engineering & AI" section with Python/Django platforms
- "Built a self-service internal platform in Python/Django"
- "Developed custom REST APIs"
- Summary: "Comfortable owning the full lifecycle: schema design and data access patterns"

**Interview reality:**
- Opens career summary with: "I've learned a lot about networking over the years. So obviously, we dealt with mostly network stats and machines, routers, switches"
- Interviewer's raw notes: "Mentioned networking multiple times... hardware focused??" and "Heavy on Administration... too admin focus"
- Application examples are **internal operational tools** (Django portal for GIS data downloads, Flask upload app), not customer-facing product applications
- Heavy focus on **administration:** Kafka admin, Flink admin, Splunk admin, system admin, PKI/certificate management
- No discussion of: API design patterns, microservices architecture, domain modeling, schema evolution, ORM optimization
- Context is **telecom network operations**, not software product development

**Assessment:** Title says "Software Engineer" but background is **data platform operator and administrator** for network operations. Role requires "strong application development background (not just DBA)" - candidate's background is the inverse: strong operations/admin, limited application development.

---

**3. AI/LLM Experience - NO SIGNAL IN INTERVIEW:**

**Resume claims:**
- "AI & ML" entire section in core competencies: "LLMs · RAG (Retrieval-Augmented Generation) · embeddings · agentic AI · ML feedback loops · Claude · CoPilot · ChatGPT"
- "Integrated LLM-augmented workflows and agentic AI tooling (Claude, CoPilot, ChatGPT) into engineering and analytics processes"
- "Evaluated embedding and RAG patterns for internal knowledge retrieval use cases"

**Interview reality:**
- **AI/LLM work was not discussed at all** in the interview
- Only ML discussion was the predictive maintenance system for fiber lasers (traditional ML, not LLMs)
- When asked for core expertise, didn't mention AI/LLM work
- No discussion of vector databases, embeddings, RAG architecture, prompt engineering, LLM integration patterns

**Assessment:** Resume emphasizes recent AI/LLM work prominently, but candidate didn't bring it up when discussing expertise or recent projects. Suggests this experience may be shallow or very recent (tool usage rather than architecture/implementation).

---

**4. Communication Ability - DISCONNECT:**

**Resume claims:**
- "Strong communicator who can translate architecture decisions to both engineering teams and executive stakeholders"
- Summary positions communication as a key strength

**Interview reality:**
- **Struggled to articulate core expertise** - took ~200 words with tangents when asked directly "what are you extremely good at?"
- Uses vague language: "good working knowledge," "somewhere in the middle," "a little bit faster," "it worked great"
- Long, rambling responses without clear structure
- Could not explain database technology tradeoffs clearly (MongoDB/DocumentDB confusion)
- **Cannot translate what you don't understand** - the database confusion undermines claimed ability to "translate architecture decisions to executive stakeholders"

**Assessment:** Communication in interview was verbose and unclear. For a Principal role requiring teaching and enabling teams, this is problematic.

---

### Critical Context Gap:

**Resume context:** "Principal Software Engineer" at Verizon suggests product software engineering role

**Actual context:** 27 years in **telecom network operations** - building data platforms for monitoring routers, switches, cell towers, network health. This is infrastructure operations, not product software development.

**Role requirement:** Principal Engineer embedded with **product engineering teams** building **healthcare software applications**

**Mismatch:** Telecom infrastructure operations vs. healthcare product engineering. Data platform operator vs. application architect. Network operations context vs. software product development context.

---

## Overall Assessment

**What's Real:**
- ETL and streaming platform expertise (Kafka, Flink, Spark) - interview confirmed this
- Operational experience at Verizon scale (Splunk, 5TB/day processing)
- Senior IC experience with technical leadership
- Hands-on problem-solving (document portal automation)
- Pragmatic engineering mindset

**What's Concerning:**
- **Fundamental database knowledge gaps** - MongoDB/DocumentDB confusion reveals shallow understanding despite resume claims
- **Wrong role context** - resume says "Software Engineer" but background is network operations infrastructure admin
- **Application development is thin** - internal ops tools, not product applications
- **AI/LLM claims not supported** in interview - no discussion despite prominent resume positioning
- **Communication unclear** - cannot articulate expertise concisely, uses vague language

**Critical Disconnect:**
The resume presents a "Principal Software Engineer" with modern tech stack (streaming, MongoDB, AI/LLMs, cloud). The interview reveals a **data platform operator and administrator** from **telecom network operations** with limited application development depth and fundamental database technology gaps.

For a role requiring **enabling application teams** to make sound data architecture decisions, the candidate cannot reliably evaluate or explain database tradeoffs. The DocumentDB confusion (not understanding it's MongoDB-compatible) is disqualifying for a Principal Data Architecture position.

**Resume credibility concern:** The disconnect between resume claims (modern AI/LLM work, database expertise, strong communication) and interview performance (no AI discussion, database confusion, unclear communication) raises questions about resume accuracy or candidate's ability to articulate their own experience.
