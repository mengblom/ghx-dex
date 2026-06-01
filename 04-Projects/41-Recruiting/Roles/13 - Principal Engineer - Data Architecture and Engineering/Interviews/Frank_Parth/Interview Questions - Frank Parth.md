---
tags:
  - interview-questions
  - principal-engineer
  - data-architecture
candidate: Frank J. Parth
date: 2026-05-28
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Questions: Frank J. Parth
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-28
**Interviewer:** Marten Engblom
**Stage:** HM Screen (30 min)

---

## Career Overview & Domain Knowledge

**Q: Give me your executive summary - your expertise and what you've been working on.**

**A:** Started career in medical interfaces at NextGen with Mirth Connect (interfacing engine for medical systems). Learned medical data standards, APIs, HL7/FHIR. Went back for data science degree, then consulted with CHS (couldn't take full-time due to relocation requirement). Started company called TAFi, which got acquired by Craneware. At Craneware, worked on Pricing Transparency Act solution - ingesting EDI files, analyzing charge master tables, running data analysis in Hadoop to display hospital pricing on web pages. After two-year post-acquisition commitment, moved to Baxter where he focused on medical interfaces and vitals monitoring - converted HL7 v2 to FHIR, built clinical data repository (CDR) with RabbitMQ for event distribution, and migrated from Azure VMs to Kubernetes microservices.

**Q: Describe the teams you've been part of at Craneware and Baxter - who was working around you?**

**A:** At Baxter, had different teams working on different devices (beds team, vitals team where he worked). Created clinical data repository that ingested ADT messages, converted to FHIR, tracked patient locations. Used RabbitMQ to send events to teams across enterprise that subscribed to changes. Teams would use events to know when patients changed locations or vitals alerts occurred. Described it as a central repository "where all the other teams across the enterprise would have to connect to us to get their data effectively."

---

## Technical Skills - Data Technologies

**Q: What are the various database products and technologies you've worked with?**

**A:** Used MongoDB (at Baxter as backend for FHIR data, can support FHIR in multiple repository solutions). Worked with relational databases ("where they need data stored very specifically") to NoSQL ("flattening and putting in a NoSQL database"). Most recently used AWS DocumentDB to store JSON transaction data. At Craneware used Azure Cosmos DB for FHIR repository.

**Q: Why did you choose DocumentDB if you already had Mongo in place?**

**A:** "In this case, it was just a matter of they needed a very specific subset. They didn't need everything from Mongo, and so AWS just created a solution and our team decided to go with it." Mentioned it's "built on top of Mongo" and noted business leaders were "always looking at costs."

**Q: How do you handle situations where Mongo needs complementary technologies for specific querying needs (like Elasticsearch or relational databases)?**

**A:** Discussed needing to look at "exactly what data you're going to be needing to get and how quickly" and "what operations are gonna be performed on that," then "configure your database so that it's expecting, and it can return those faster results based on that, and that's just part of the indexing of the database." Did not mention complementary technologies like Elasticsearch or relational databases for complex queries.

**Q: Are you working with self-hosted Mongo or Atlas?**

**A:** "God, no, I haven't worked with self-host in so long. That was Azure or Baxter, and then we're using AWS." (Hasn't done self-hosted in a long time, using managed services.)

---

## Event-Driven Architecture & Messaging

**Q: Can you talk about the queuing and messaging solutions on your resume (Kafka, RabbitMQ) - what was the solution and your involvement?**

**A:** Used RabbitMQ at Baxter in pub-sub model to send out events when data changed in CDR. Used Kafka at Craneware - had to create a plugin in Mirth to read from it because they were interested in events being published to Kafka. Mentioned "queue is another one that goes way back" and said "Rabbit seems to be the best solution today" from what he's used.

**Q: What were the notifications about?**

**A:** At Baxter, used multi-tenancy with facility-based topics. Created topics per facility using "facility ID." Applications would subscribe to facility-specific topics to get all notifications/data coming off that facility-specific RabbitMQ queue. "If your application was part of their solution, then you would get those events based on that tendency."

---

## Red Flags / Concerns

1. **Limited Architecture Depth:**
   - When asked about complementing Mongo with other technologies (Elasticsearch, relational DB) for complex queries, only discussed indexing - didn't demonstrate broader architectural thinking
   - DocumentDB choice explanation was shallow: "they needed a very specific subset" and "business leaders" wanted it - no articulation of technical trade-offs
   - Could not explain multi-technology data architecture beyond "just part of the indexing"

2. **Narrow Focus on Integration/Interfaces:**
   - Core expertise appears to be HL7/FHIR interfaces and medical data transformation, not data architecture
   - Role at Baxter was described as "medical interface engineer" and "data repository"
   - Limited discussion of data modeling, schema design, performance optimization beyond basic indexing

3. **Passive Technology Selection Role:**
   - DocumentDB: "our team decided to go with it"
   - Cosmos DB: appeared to be pre-selected infrastructure
   - No examples of evaluating and recommending database technologies based on workload analysis
   - Business drove technology decisions, not candidate's architectural recommendations

4. **Limited Cloud/Scale Experience:**
   - Acknowledged limited experience with managed services: "I haven't worked with self-host in so long"
   - No discussion of cloud cost optimization, capacity planning, or scaling strategies
   - Recent migration to Kubernetes mentioned but minimal detail on architecture decisions

5. **Communication Style:**
   - Went off-topic when asked technical questions (moving story at beginning, mentioned telescope, cold symptoms)
   - Responses lacked depth when probed on architecture decisions
   - Did not demonstrate ability to articulate complex technical concepts clearly

---

## Closing Questions

**Q: Any questions for me?**

**A:** Asked: "It seems to be more likely it would be going against my data science kind of experience. From my understanding, that's what you need on your team right now."

Then asked: "How many teams do you have that would be using the data store?" (Answered: 4-5 teams)

Then asked: "How are you hosted? Are you using a data advisor [advisor]?" Discussion about AWS, EC2 instances, migration to Atlas, managed services.

---

## Interviewer Notes

**Overall Impression:** Frank has strong domain knowledge in healthcare integration (HL7/FHIR) and medical interfaces, which aligns with the healthcare domain preference. However, his core expertise appears to be as an integration/interface engineer rather than a data architect. His data experience is primarily using databases as storage backends for interface engines, not designing data architectures, modeling complex domains, or making technology selection decisions. When probed on architectural decisions, responses were shallow and didn't demonstrate the depth needed for a Principal Engineer role focused on data architecture. The role requires someone who can evaluate and recommend data technologies, design data models, optimize performance, and guide teams on data decisions - Frank's experience seems more focused on implementing predetermined solutions within integration platforms.
