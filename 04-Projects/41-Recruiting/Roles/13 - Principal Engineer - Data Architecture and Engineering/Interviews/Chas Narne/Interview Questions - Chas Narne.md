---
tags:
  - interview-questions
  - principal-engineer
  - data-architecture
candidate: Chas Narne
date: 2026-05-21
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Questions: Chas Narne
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-21
**Interviewer:** Marten Engblom
**Stage:** HM Screen (30 min)

---

## Career Overview

**Q: Tell me about yourself - your background and engineering experiences so far.**

**A:** Started with healthcare domain experience at Philips Respironics, building SaaS platform for medical device data - IoT data streaming from Qualcomm chips, processing EDF files, storing in MongoDB, APIs for clinicians to access patient data with permissions. Currently Principal Engineer at SAE International since 2021, leading monolith-to-microservices migration. Took 30-year-old on-prem monolith, broke it into 50+ microservices pattern, migrated to cloud. Core challenge: thinking about data boundaries, decoupling, choosing right data stores for the problem. Event-driven saga patterns vs eventual consistency decisions. Day-to-day involves code reviews, API versioning (v2, v3, v4), sunsetting legacy APIs, usage analysis. Supports aerospace/defense/manufacturing users - complex business rules, ~75,000 users daily.

---

## Data Architecture & Technology Selection

**Q: Tell me about choosing the right data product for different scenarios - pick an interesting challenge.**

**A:** **Scenario:** Broke down Oracle monolith (300 tables) into MongoDB + Elasticsearch for search functionality. Chose eventual consistency pattern to enable searching across datasets - MongoDB auto-indexes into Elastic. **Challenge:** Lag between write to MongoDB and reflection in Elasticsearch (2 seconds). Users clicked, didn't see updated data immediately. Non-tech-savvy field engineers expected instant feedback. **Solutions attempted:** (1) Reverted some data back to Oracle for critical paths. (2) Used two threads to query Oracle + Elastic simultaneously, compare results. (3) Made writes persistent to MongoDB primary only (faster than waiting for all nodes + Elastic indexing). Improved to ~2 second worst case. Chose dimensional consistency for expanded functionality, but had to pivot and make ongoing changes.

**Q: How did you pick MongoDB as the new data store?**

**A:** Wasn't there for initial stack selection - brought in after decision made. Initially had concerns going from strictly ACID (Oracle) to something partition-tolerant and always-available. MongoDB allows tuning write concern to move between CP and AP (CAP theorem) based on code needs. Good support, good documentation, seamless integration with Elasticsearch. Built-in ETL tools read operational log and auto-write to Elastic. Went with self-managed version for cost savings.

**Q: Is self-hosted MongoDB working well? (Context: We're migrating to Atlas.)**

**A:** Yes, working well. Implemented TTL (time-to-live) on old documents (20-30 year old standards from Oracle migration that are obsolete). Documents auto-move to archive collection, then to hard disk. TTL feature means set it and forget it.

**Q: What happens when you archive something - ever need to restore?**

**A:** Haven't had need to restore yet. Archive pattern: create separate collection (e.g., `archive_users` matching `users` model). Could write quick query to re-import based on created_date, logoff_date, last_login, etc. if needed. At Philips, had scheme to move to different database entirely (MongoDB databases are just files on server - can export petabyte file and handle as file).

**Q: Who manages databases from performance/tuning perspective - you and your team, or ops?**

**A:** Ops has dashboard monitoring usage percentage, request counts, maintains service accounts. Alert when unusual patterns (e.g., "100 requests/second from this service"). Happens more in test environments - someone does massive update. Challenge with MongoDB and microservices: denormalized data across collections. If user changes name, must touch every collection with audit trail (updated_by, created_by) and update name everywhere. Try to avoid bulk updates, but minor attribute changes cause issues.

**Q: With concerns like that, was going wholesale into MongoDB the right choice? Some of those things are very easy in relational databases.**

**A:** Still use Oracle for some services, also have PostgreSQL and Redis caching. Mostly stick to MongoDB, but have other options. If spawning new service today, would pick and choose between any of these. Had very strict time-to-market requirements for migration - MongoDB was first choice, then circled back and did 50/50 refactoring.

---

## Data Streaming & Event-Driven Architecture

**Q: You mentioned data streaming on your resume - can you talk about that experience?**

**A:** **Context:** Rolled out app divided by user types (auditors, suppliers, subscribers, staff, etc.) - 5 different apps for specific users, all using same backend services. Enables strangling functionality and migrating user sets incrementally to new app. Still references same backend data, so if legacy user updates data, new app user must read same data quickly.

**Kafka use case:** "Audit" process - massive JSON with 75 different attributes from different legacy tables. Any attribute change in one table triggers updates in other tables because user actively working on audit. Wait 10 minutes to compile entire audit before sending to backend (first event triggers 10-minute window to accumulate all changes). User can wait 10 minutes because nobody else accessing same audit simultaneously.

**RabbitMQ use case:** All other changes must be fast. Use Oracle triggers → fires event on Rabbit → service listening to table pulls event → throws on Rabbit → consumers listen on topic. Happens within 300-500ms. SLA is 1 second, most happen <300ms.

**Q: How do most of your 50 microservices communicate - async messaging?**

**A:** Decision criteria: "Is the user waiting on screen for this process to finish?" If yes → synchronous call. If no → async. All APIs go through gateway with hard 5-second timeout (returns 500 if exceeded = bad UX). If can do synchronously and fast, it's an API. If user not waiting, it's event-driven backend.

**Q: That's all on top of RabbitMQ?**

**A:** Yes, all RabbitMQ. Audit process (separate screen, subset of users) is all Kafka.

**Q: How do you deal with edge cases like retries, redrives, dead lettering?**

**A:** Dead letter queues on everything. Alerts on most DLQs (not all). Alert triggers when >1 message in DLQ - can be annoying, spams inbox. Critical DLQs have Teams hooks. When see something, try to reprocess. If special character or unique edge case, change data in backend to fix.

---

## Cloud & Managed Services Experience

**Q: Which managed data stores do you have experience with? (You mentioned DynamoDB at some point maybe.)**

**A:** Used DynamoDB in past - very little in AWS realm, just proof of concept. Migrated everything to RDS from on-prem Oracle - some experience there. Used Cassandra - played around with it. Mostly worked in enterprises where Oracle is the go-to for legacy applications. A lot of Oracle experience.

---

## Core Expertise

**Q: What would you say is your core technical expertise? What topics do people come running to you for?**

**A:** API design for new APIs or services. Architecting data model. Coming up with service boundaries. Gotten really good at looking at usage from end user perspective. Questions: How is user using this data? How does it mutate? Does it affect existing service/data? How many legacy tables does it touch? Use these to come up with good data model. **Motto:** "If you come up with a good data model, then it's extremely easy to come up with good APIs."

---

## GHX Tech Stack Discussion

**Q: Overview of GHX stack?**

**A:** Mostly Java throughout, TypeScript on frontend. Some outdated Angular apps (trying to move away). Data: MongoDB, Elasticsearch, some PostgreSQL - sounds similar to your stack. Part of this role: figuring out if using MongoDB appropriately, identifying areas where it's not the right tool, untangling that. In AWS, lot of lift-and-shift architecture on EC2 instances from data center. Being addressed incrementally - moving to containers or fully managed products (compute or data). Stream data into Snowflake for analytics (different team owns that).

---

## AI-Assisted Development

**Q: Experience with AI-assisted development, agentic tooling?**

**A:** Last six months = best engineering time of career. Use Claude heavily. Coming up with ways to make life better as engineer. Part of another team (50/50 split) - automating feature migration from legacy to new app. Process: mining → PRD generation → UI/backend development → human-in-loop review before PRD generation → resolves open questions. Output: UI code and backend code that should work when run. Takes screen from legacy app, migrates entirely into microservices world. If no service exists, creates another PRD for service creation with suggested data model.

**GHX context:** Leaning in heavily. Everyone has full Anthropic unlimited license. Figuring out orchestration approach. GitHub is code repo, Copilot is great orchestrator. Thinking combination of both. Currently no caps - company wants us to really leverage these tools.

**A (follow-up):** Every other week, create new app making engineers' lives easier. Creating apps faster than can use them. It's fun.

---

## Role Fit & Interest

**Q: You read the job description - the impetus is very data-heavy, but I like teams that are multifaceted and wear a lot of hats. You have full-stack experience. How do you feel about coming into this role where the #1 focus is data for a good while - working across multiple teams, knowing what good looks like, helping them get to better place in how they store/read/write/archive/model data?**

**A:** That's kind of my day job - work across teams, establish standards, align high-level architecture improvements from data and consistency perspective. Would be very excited for the role. Enjoy getting hands dirty with proof-of-concept work - goes a long way in coming up with ideas. Do UI/frontend (Angular, React) a little bit, but not my strong suit. Know enough to be dangerous. Would be very willing and excited for the role.

---

## Closing Questions

**Q: Any questions for me?**

**A:** Just overview of stack and how the middle layer between provider/supplier works - those APIs.

**A (after learning about GHX stack):** No further questions.

---

## Interviewer Notes

**Overall Impression:** 

- Healthcare domain experience (Philips Respironics)
- Monolith breakup experience (SAE International) - Oracle to MongoDB, indexed into Elasticsearch, naturally mentions strangler pattern
- Very good experience with modern distributed architectures, well-versed in microservices, APIs, REST
- Very experienced with MongoDB
- Well-versed in DB terms (CAP theorem)
- Great communicator, effective and to the point
- AI/LLM assisted development is on par or better than expected
- **Will definitely move Chas on to full interview loop**
