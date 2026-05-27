---
tags:
  - interview-questions
  - principal-engineer
  - data-architecture
candidate: Matt Ford
date: 2026-05-18
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Questions: Matt Ford
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-18
**Interviewer:** Marten Engblom
**Stage:** HM Screen (30 min)

---

## Career Overview

**Q: Can you give me a high level summary of yourself and your career?**

**A:** 20 years in data and analytics. Started in small e-commerce shops, moved to Best Buy for 15 years. Created data mart for Best Buy Direct/Business, interfacing with bestbuy.com enterprise data warehouse. Built reports using SSRS, handled transformations and normalization. Also worked on software side handling e-procurement (cXML transformations, catalogs, order placements). Team structure fluctuated based on funding - sometimes solo, sometimes managing team. Set up new data warehouse in Oracle for that org with dimensional modeling, click view sales apps, compensation reports for 300-person sales team. Moved to Gemini (external sign manufacturer, 60 years old) as CTO brought him in to modernize reporting. Convinced them to go with Microsoft Fabric for quick turnaround. Real-time event streams for MongoDB structure (partner portal). Created full Medallion architecture (bronze/silver/gold), ontology on top of gold. Looking at Fabric IQ (MCP layer). Built pipelines, Power BI dashboards, digital signage for contact centers.

---

## Current Role at Gemini

**Q: Describe the team around you at Gemini.**

**A:** Somewhat homegrown company - many operations SMEs started in warehouse or phone support. Conducts bi-weekly training sessions (started as weekly) to build out gold data marts. Users were accustomed to ODBC connections to silver layer (directly to transactional database) - had some SQL skills and relational database concepts. Walks them through existing reports, identifies gaps/missing datasets, shares in governed way (endorsing models). Promoted a data governance manager (33 years at company) who knows business side. Guiding him through governance since he's never done it before. Candidate was heavily involved in data governance at Best Buy (CRM, e-commerce, data archival, sensitivities, PII, PHI from health smart home project). At Gemini: people looking to become data scientists, helping them on that path. Starting to build AI models using LLMs, connected Claude to MCI through Fabric ontology (sales/quotes section). Company doesn't have active inventory but manages raw materials. Every sign is generally custom order (done by hand) - candidate pushing to automate, made strides.

---

## Technology Selection & Experience

**Q: What data store products do you have experience with?**

**A:** 
- **E-commerce tech stack:** PHP with Magento, MySQL database
- **Best Buy:** Oracle for most transactional systems, some Microsoft SQL. Handled ETLs with SSIS using SQL Server. SSRS for reporting front end. Some SSAS (not much need).
- **Current (Gemini):** Microsoft SQL, PostgreSQL (heavy use - created pseudo data warehouse/egress database in Azure before deciding on Fabric). Fabric/lakehouse, some Databricks. Parquet data format, direct lake data format. Azure Synapse (but going away).
- **AWS:** Brief 6 months on project using S3 for storage and Glue (setting up PLC)
- **MongoDB:** Current use for partner portal platform (front-facing interface for companies to create orders/quotes). Interfacing from Fabric using three methodologies: 1) Mongo CDC data streams using Microsoft Fabric event streams (Kafka-like, low code), 2) spark connector handling Debezium metadata himself (due to Microsoft defect)

**Note on MongoDB CDC defect:** Microsoft Fabric event stream keeps losing collection config after 24 hours - hard fails. Been battling Microsoft for 3 months to fix. Created custom spark connector as workaround, but increases billable usage significantly.

---

**Q: How do you decide what type of technology to use?**

**A:** Concepts, demos, testing - actually making it happen. Conscious about not getting too far down a path before discovering a "gotcha" - wants to find critical missing pieces before being too invested. MongoDB/Fabric issue was one of those, but "there's always a workaround for everything." Makes sure it's the right way - following supported patterns, not anti-pattern designs. Questions like "why are you loading all the data and transforming on flight?"

---

## Application Team Collaboration

**Q: How do you work currently with the teams that build applications on top of these data stores?**

**A:** At Best Buy: part of core software engineer team always. 60% of time on average throughout entire tenure was software side, generally with data pipelines (not necessarily front end, though filled gaps). Some front end work - vanilla JavaScript and CSS, some React. Created on-premise cloud service called Mindshift (only part of org using it) which solved CICD problems. 8 years ago CICD wasn't huge at Best Buy - everything was waterfall, no agile. Bestbuy.com running off ATG tech stack. Felt always behind on everything. At current role: has opportunity to "go straight for the candy" (modern approaches). Testing everything. Came close to Snowflake but restricted to Microsoft shop (hiring criteria: Microsoft skill set, contractor relationships). Could convince them to move away if needed for pricing reasons.

---

## GHX BI Infrastructure

**Q: What does your BI layer look like? Sounds like you're trying to bring everything together even though it's monolithic now.**

**A:** (Marten explains) BI data store in Snowflake - syndicate any data anyone wants to look at, stream into Snowflake. Owned by different team. Gap: Snowflake good for analytical workload, not great to serve other systems with low latency requirements. Systems reaching into databases they shouldn't to get dependent data. Monolithic mess being untangled. Analytical workload sits on Snowflake, data should be streamed in (holds true in most/all cases, was later add-on).

**Matt's clarification Q:** Sounds like the gap is latency timing on that data?

**Marten:** Two choices for downstream consumers: 1) Snowflake (fine for analytics/reporting), 2) Direct connection to source of truth (read replicas exist but not perfect). If system is transactional/real-time, Snowflake not suitable. Not everything's replicated.

---

## Closing Questions

**Q: Why are you looking for new roles?**

**A:** Curious. At point where would like to expand more. Now tightened into Fabric, blew through setup solidly, getting into governance side now - "almost into maintenance mode instead of build mode." Main driver: able to keep learning, keep evolving instead of "is that table updated?"

**Q: Any questions for me?**

**A:** Asked about BI layer (covered above).

---

## Interviewer Notes

**Overall Impression:** Strong BI/analytics background with lots of Microsoft Fabric/Azure ecosystem experience. Very focused on reporting, dashboards, data marts - classic BI engineer profile. Has done some application development but mostly data pipelines and reporting infrastructure. Currently at maintenance phase of Fabric implementation and looking for next challenge. Experience seems more BI/analytics focused than the application-embedded data architecture role we're hiring for.

**Key observations:**
- Deep Microsoft ecosystem experience (Fabric, SSIS, SSRS, Power BI)
- Strong in building data warehouses and reporting infrastructure
- Has MongoDB experience but primarily as read-only analytics source
- Software development experience exists but seems secondary to BI focus
- Team enablement mostly through training on reporting tools vs. embedded architecture guidance
- Current role moving to maintenance mode - looking for build mode again
