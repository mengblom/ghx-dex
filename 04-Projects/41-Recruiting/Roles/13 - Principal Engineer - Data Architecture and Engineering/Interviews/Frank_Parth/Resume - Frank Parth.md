---
tags:
  - resume
  - principal-engineer
  - data-architecture
candidate: Frank J. Parth
date: 2026-05-28
location: Lehi, USA
---

# Resume: Frank J. Parth

**Contact:**
- Email: frankparth8@gmail.com
- Phone: (949) 426-2294
- Location: Lehi, UT 84048

---

## Summary

To use my education and experience in the software engineering field to make a difference within the healthcare industry. Specifically, with the intent to help medical vendors integrate and gather/analyze the data they need through highly secure, efficient, and reliable interfaces.

---

## Skills

- API Development
- HL7 Integration
- FHIR Standards
- Machine Learning
- Cloud Architecture
- Kubernetes
- Java Development
- Data Integration

---

## Work Experience

### Baxter Healthcare - Deerfield, IL
**Senior Principal Engineer R&D** | 12/2021 - 04/2026

- Implemented Integration Engine (NextGen) into BDHP platform, enabling Baxter Smartcare Remote Management for seamless device connectivity
- Migrated Azure VM hosting solution to Kubernetes environment developing YAML for pods and services required to host the solution
- Maintained and developed C# microservices for HL7 v2 processing, facilitating outbound IHE alarms to EMRs and creating API endpoints for device management in Kubernetes environment
- Developed interfaces to convert vitals data from MQTT feeds to FHIR resources for CDR and processed FHIR resources from rabbit exchanges to HL7 v2 for outbound transmission to EMRs and Mongo for data analysis

### TAFi/Craneware - Edinburgh, UK
**Software Platform Lead Engineer** | 01/2019 - 01/2021

- Designed architecture for machine learning model utilizing information from supported data types to enhance data analysis capabilities
- Implemented elastic NextGen Connect Azure Scale Set solution for efficient handling of incoming healthcare data feeds
- Developed interfaces for various data types including HL7 v2, HL7 CCDA, HL7 FHIR, NCPDP, EDI/X12, converting them to JSON data models for improved interoperability
- Wrote interfaces to read from Kafka feeds and send data to RabbitMQ/Cosmos DB and validate responses for endpoint application interactions
- Created and configured Azure Cloud servers and services including FHIR and Cosmos with NexGen Connect

### Community Health Systems - Franklin, TN
**Interface Developer III** | 07/2017 - 12/2018

- Developed interfaces using Java and JavaScript to transform HL7 v2 & v3 (CDA) messages for seamless integration with EHR systems including Meditech, Cerner, and Medhost
- Integrated multiple vendor applications with EHR software and medical applications including MPF/HPF, Artifact, Epiphany, HealLogics, MCCM, MIDAS, Pulse, Teletracking, and WoundExpert
- Monitor queues ensure data is sent correctly to destinations (IP/Port configuration), data reprocessing, and error handling
- Implemented MPF to efficiently store documents received in HL7 messages

### NextGen (Mirth) - Costa Mesa, CA
**Software Engineer** | 02/2014 - 12/2016

- Wrote interfaces using both Java and JavaScript transforming and filtering data and medical messaging including HL7 v2, v3(CDA), & FHIR developing channels
- Worked with REST and Soap web services, TCP, Database (Postgres, Oracle, SQL Server, Mongo), File Reader/Writer, HTTP, and SMTP destinations
- Collaborated with clients to gather requirements and create specification documentation, including lucid chart channel diagrams and channel turnover workflow documentation
- Worked with a number of different EHR systems including Epic, Cerner, Meditech, Allscripts as well as HIE software products including Orion, and Relay
- Engaged with various medical device vendors, including Pfizer, CTS, Leica Biosystems, Fresenius, Welch-Allyn, and GE Centricity, to ensure effective integration and support

### UC Irvine - Irvine, CA
**Programmer Analyst II** | 11/2013 - 02/2015

- Developed Java web-based applications interfacing with IBM Tririga via web services on Apache server using Fuse ESB, encompassing analysis, documentation, design, programming, debugging, testing, securing, and implementation of large, complex applications, significantly enhancing campus operational capabilities
- Provided operational support, maintenance, technical documentation, consultation, and end-user support for homegrown and vendor applications, managing tasks, tracking issues, monitoring weekly progress, and facilitating cross-training to improve facility operations
- Evaluated and tested software upgrades, new tools, and techniques, recommending solutions that improved system performance and user satisfaction

### Cerner Corporation - Kansas City, MO
**Software Engineer** | 04/2012 - 04/2013

- Developed front-end application (Millennium) using Java, JS, PHP, and CSS, and corresponding backend using CCL(SQL)
- Reviewed requirements, created user stories, tested and validated features, and released exception and product pipelines while debugging and conducting code reviews
- Applied Agile processes and Unified methodology to deliver iterative improvements every two weeks

---

## Education

**MS: Data Science** | 08/2018
University of California, Riverside - Riverside, CA

**MS: Computer Science** | 08/2013
University of Central Missouri - Warrensburg, MO

**BS: Computer Science & Mathematics** | 05/2012
University of Central Missouri - Warrensburg, MO

---

## Certifications

- Microsoft Certified: Azure Fundamentals, Microsoft, 06/01/21, 991534249
- HL7 FHIR Proficient Certification, Health Level Seven International, 12/01/21
- HL7 V2 Control Specialist Certification, Health Level Seven International, 12/01/18
- Mirth Connect Advanced, NextGen Healthcare, 08/01/16, MC00514
- Mirth Connect and Appliance, QSI | Mirth, 03/01/15
- Network+, CompTIA, 08/01/11, COMP001020311280
- CompTIA A+, CompTIA, 04/01/09, COMP001020311280

---

## Accomplishments

- Baxter BaxStar 2024
- Dean's List

---

## Resume vs. Interview Observations

### Strengths on Resume

**Healthcare Integration Expertise (Exceptional):**
- 14 years of continuous healthcare software experience (NextGen/Mirth 2014-2016, CHS 2017-2018, Craneware 2019-2021, Baxter 2021-2026)
- Deep credentials in medical data standards: HL7 FHIR Proficient, HL7 V2 Control Specialist, Mirth Connect Advanced
- Experience across all major EHR systems (Epic, Cerner, Meditech, Allscripts)
- Built integration solutions for medical device vendors (Pfizer, GE, Fresenius, Welch-Allyn, Leica Biosystems)

**Educational Background:**
- Three graduate degrees: MS Data Science (2018), MS Computer Science (2013), BS Computer Science & Mathematics (2012)
- Shows commitment to continuous learning and technical depth

**Technology Breadth:**
- Multiple cloud platforms: AWS (Baxter), Azure (Craneware)
- NoSQL databases: MongoDB, Cosmos DB, DocumentDB
- Event streaming: Kafka, RabbitMQ
- Kubernetes migration experience
- Multiple programming languages: Java, JavaScript, C#, Python

**Recent Senior Title:**
- "Senior Principal Engineer R&D" at Baxter (2021-2026) suggests principal-level scope

### Major Disconnects in Interview

**1. Role Mismatch - Integration Engineer vs. Data Architect:**

**Resume positioning:** Lists skills like "Cloud Architecture," "Data Integration," "Machine Learning" alongside "API Development" and "HL7 Integration," suggesting broad data architecture capabilities.

**Interview reality:** When asked about core technical expertise, Frank said: **"medical interface engineer and data repository."** This is accurate but fundamentally different from a data architect role. His work involves:
- Building interfaces between medical systems (HL7/FHIR transformations)
- Using databases as storage backends for integration engines
- Implementing predetermined technical solutions within integration platforms

**Not:** Designing data models for business applications, evaluating database technologies based on workload analysis, or establishing data patterns across engineering organizations.

**2. Technology Selection - Passive Role vs. Architectural Leadership:**

**Resume impression:** "Designed architecture for machine learning model" (Craneware), "Created and configured Azure Cloud servers and services" suggests driving architectural decisions.

**Interview reality:** When asked why DocumentDB was chosen over MongoDB:
- Frank: **"They needed a very specific subset... AWS just created a solution and our team decided to go with it."**
- Described business leaders "always looking at costs" - no technical rationale
- Could not articulate workload analysis, performance considerations, or cost modeling

**For comparison:** A data architect would say: "We evaluated DocumentDB vs managed MongoDB based on our query patterns (mostly document lookups vs complex aggregations), transaction volumes (X per second), and cost at scale. DocumentDB's pricing model made sense for our read-heavy workload with limited indexing needs, saving approximately $Y/month compared to Atlas at our scale."

Frank's response suggests he implemented what the team decided, not that he drove the architectural decision.

**3. Performance Optimization - Surface-Level vs. Deep Expertise:**

**Resume impression:** Job descriptions mention "data analysis," "machine learning," "efficient handling of incoming healthcare data feeds" - suggests performance-focused work.

**Interview reality:** When asked about database performance optimization beyond indexing:
- Frank: **"You have to look into exactly what data you're going to be needing to get and how quickly... that's just part of the indexing of the database."**
- Only mentioned indexing - no discussion of query tuning, execution plan analysis, partitioning strategies, materialized views, caching layers, or complementary technologies

**Missing depth:** When asked about using Elasticsearch or relational databases to complement MongoDB for complex queries, Frank only discussed indexing - didn't demonstrate understanding of multi-technology data architectures.

**For comparison:** A Principal Data Architect would discuss: "For complex aggregations across large datasets, we introduced a read model using Elasticsearch with 5-minute refresh from Mongo via change streams. For transactional consistency requirements, we kept relational DB for the canonical model and used Kafka to propagate events to Mongo/Elastic read models."

**4. "Senior Principal Engineer" Title vs. Described Scope:**

**Resume title:** "Senior Principal Engineer R&D" at Baxter (2021-2026) suggests strategic technical leadership.

**Interview scope:** Described work that sounds like senior IC execution:
- "Maintained and developed C# microservices for HL7 v2 processing"
- "Developed interfaces to convert vitals data from MQTT feeds to FHIR resources"
- Built clinical data repository with RabbitMQ event distribution

**No evidence of:**
- Establishing data standards across engineering organization
- Influencing technology decisions across teams
- Reviewing application code/architecture with data focus
- Leading zero-downtime migrations (mentioned migration but not leadership role)
- Educating and enabling other engineers

**Title inflation concern:** The "Senior Principal Engineer" title may not reflect principal-level scope and impact. The work described is technically sophisticated senior-level execution within integration platforms, not architectural leadership across teams.

### Assessment

**What the resume suggests:** Broad data architect with healthcare domain knowledge, cloud architecture experience, machine learning background, and principal-level technical leadership.

**What the interview revealed:** Specialized integration/interface engineer with exceptional healthcare interoperability expertise (HL7/FHIR/EDI), strong implementation skills, and experience using databases within integration platforms - but not a data architect who designs data systems, drives technology selection, or establishes patterns across teams.

**Credibility concerns:** Not a question of resume dishonesty - all listed experience appears accurate. However, the **packaging and positioning** create a misleading impression:

1. Resume emphasizes "Cloud Architecture" and "Data Integration" at same level as "HL7 Integration" - but interview showed HL7/FHIR integration is the core expertise, with database usage being secondary (storage backends for integration engines)

2. "Senior Principal Engineer" title suggests architectural leadership scope, but interview revealed work that's senior IC execution without the "establishing standards across teams" or "driving technology decisions" expected at principal level

3. Resume bullets like "Designed architecture for machine learning model" sound like architectural leadership, but interview showed passive role in technology decisions ("our team decided to go with it")

**The fundamental disconnect:** This resume is for a **Senior Integration/Interoperability Engineer** role focused on healthcare data standards, not a **Principal Data Architect** role focused on application data modeling, database selection, and performance optimization across engineering teams.

**Where Frank would excel:** Healthcare interoperability architect, HL7/FHIR integration specialist, or senior integration engineer at a health tech company, EHR vendor, or HIE (Health Information Exchange). His domain knowledge and integration expertise are genuinely exceptional in that domain.

**Where this creates problems:** For a Principal Data Architect role "working side-by-side with application engineers" on data modeling, query optimization, and technology selection across diverse business domains, Frank's narrow specialization in integration platforms creates a fundamental skills mismatch - regardless of how impressive his integration expertise is.

---

**Recommendation for Agency:** Strong candidate for healthcare integration/interoperability roles. Not a data architect - focus search on architects who have built data-intensive applications, established data patterns across teams, and can articulate technology selection rationale with technical depth. Healthcare domain knowledge is valuable but insufficient without data architecture expertise.
