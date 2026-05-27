---
tags:
  - interview-questions
  - principal-engineer
  - data-architecture
candidate: Richard P. Monson
date: 2026-05-18
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Questions: Richard P. Monson
**Role:** Principal Engineer - Data Architecture and Engineering
**Date:** 2026-05-18
**Interviewer:** Marten Engblom
**Stage:** HM Screen (30 min)

---

## Career Overview

**Q: Give me a big picture summary of what you've been up to in your career, as it relates to data architecture.**

**A:** Started in telecom data tracking (private lines, user codes). Moved to Logi Analytics where built data engine for business analytics tool. Job was to:
- Hook to any data source (relational, NoSQL, APIs)
- Pull data from Oracle, PostgreSQL, MySQL, SQL Server, MongoDB, Twitter, Google Analytics
- Transform data according to business rules
- Join data across different databases
- Built ETL tool completely
- Wrote SQL Dialect system to support operations across different databases (~4 hours to hook in new database)

Then Fannie Mae - primarily focused on automating code quality process using Cast Software tools. Not data architecture focused.

Then Capital One - worked on models and S3 reader (submitted patent). 

Then US Bank - senior principal on two committees (mainframe architectural changes, modern tech stack). Primary projects:
- Spend limit feature for credit card authorizations (20ms SLA)
- Found team was using Spring Data JPA without understanding what it did under the covers
- Rewrote their code, reduced approval time from 39 minutes to 5 milliseconds

---

## Data Products & Technologies

**Q: What data products do you consider yourself proficient in?**

**A:**
- **Relational:** "Pretty much all the relationals, at least all the majors" - PostgreSQL, Microsoft SQL Server, Oracle, HP Vertica (all local free versions on his machine at Logi)
- **NoSQL:** MongoDB (last used ~2015, "could have been 10 years") - claims "a lot of them have changed and now support SQL"
- **Other:** Wrote SQL Dialect system at Logi to support different database systems
- Says "data is data" and concepts are the same across columnar stores, document stores, standard rows/records
- Mentions vector databases as "new twist with transformers" but focuses on problems with AI coding tools rather than vector database expertise

---

## Managed Data Services

**Q: What managed data services do you have good experience with?**

**A:** "I've only done a few of the AWS and it's the Cloudera and we did a little bit of Cassandra, but I wasn't allowed to do the management I wanted to do."
- US Bank used Cassandra (hosted on their system, not truly managed)
- RDS "you can kind of argue it's managed"
- "I haven't done a lot" of managed services
- US Bank initially wanted Microsoft SQL, then changed to AWS, then changed to on-prem during his project
- Used Microsoft SQL (mandated relational) and Cassandra (document store) with GraphQL

**Key concern:** Very limited managed cloud database service experience.

---

## Technology Selection

**Q: How do you choose between relational, NoSQL, document databases?**

**A:**
- **Relational:** "Highly transactional" - individual record modifications, inserting orders, updating prices/addresses
- **NoSQL:** "More flexible schemas", designed with clusters, scale better, good for logs that you "drop and just leave"
- Document stores: "Perfect for logs" - "whole bunch of orders for tiny things"
- Production databases tuned for throughput vs reporting databases tuned for analytics
- Don't want to run reports on production database - replicate off or use ETL to build data mart/warehouse/lake

**Assessment:** Basic understanding but surface-level reasoning. Didn't discuss:
- Read vs write patterns
- Data modeling complexity
- Query patterns
- Cost considerations
- Team autonomy implications

---

## Red Flags / Concerns

1. **Spent significant time on very old experiences:**
   - Telecom data from early career
   - Logi Analytics work (seems dated)
   - Extensive discussion of Fannie Mae code quality automation (not data architecture)

2. **Outdated/concerning vocabulary:**
   - "Haven't had a chance to use the Azure Tables" (Azure Tables is not a product)
   - MongoDB experience is ~10 years old, claims "now support SQL" but shows no recent experience

3. **Very limited managed service experience:**
   - Explicitly said "I haven't done a lot" when asked about managed data services
   - Most experience with on-prem or self-managed databases

4. **Tangential responses:**
   - Goes on tangents frequently (microservices philosophy, paved road concept, code quality tools)
   - Doesn't stay focused on data architecture topics
   - Long rambling answers that don't directly address questions

5. **Lack of modern data architecture experience:**
   - No discussion of: Data mesh, event sourcing, CDC, streaming architectures, data governance
   - No cloud-native data platform experience (Snowflake, Databricks, etc.)
   - Limited understanding of modern application development with data

---

## Closing Questions

**Q: Any questions for me?**

**A:** Asked about:
- Timeline (applied April 7th)
- Whether I had his latest resume with CISSP
- Mentioned 5 AWS certificates including "the data one"
- Mentioned patent from Fannie Mae
- Asked what's needed for next steps

---

## Interviewer Notes

**Overall Impression:** Clear pass. Candidate is out of touch with modern data architecture, spent most of time on old/irrelevant experiences, shows limited depth in areas critical to the role (managed services, cloud platforms, modern application development). Agency match quality questionable.
