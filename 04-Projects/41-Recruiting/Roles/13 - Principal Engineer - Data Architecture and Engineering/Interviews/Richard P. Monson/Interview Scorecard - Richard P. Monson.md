---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Richard P. Monson
date: 2026-05-18
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Scorecard: Richard P. Monson
**Role:** Principal Engineer - Data Architecture and Engineering
**Date:** 2026-05-18
**Stage:** HM Screen (30 min)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill                                                                       | Score (Interview) | Resume Evidence                                                                       | Interview Evidence                                                                                        |
| --------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | 2                 | Resume: Spring Data JDBC optimization at US Bank (2022-2025), SQL expertise listed    | Interview: Only mentioned local copies at Logi Analytics (10+ years ago), couldn't articulate recent work |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB)           | 1                 | Resume: No MongoDB/NoSQL mentioned                                                    | Interview: Claims MongoDB ~10 years ago, says "now supports SQL" but shows no recent knowledge            |
| Database performance optimization at scale                                  | 2                 | Resume: Credit card spend limit 39 min → 7ms (custom SQL query, Spring Data JDBC)     | Interview: Mentioned this story but explanation lacked credibility/detail                                 |
| Advanced data modeling and schema design                                    | N/A               | Resume: No specific data modeling projects called out                                 | Interview: Not discussed                                                                                  |
| Application development skills                                              | 2                 | Resume: Java/Spring Boot microservices at US Bank (2022-2025), Python at Capital One  | Interview: Didn't discuss recent app dev, only old VB6/C# at Logi Analytics                               |
| Can review application code and architecture                                | 2                 | Resume: ICS/ECIC Architecture Committees, code reviews mentioned                      | Interview: Claimed to review Spring Data JPA but didn't demonstrate depth                                 |
| Experience evaluating and selecting database technologies                   | 2                 | Resume: No specific technology selection examples                                     | Interview: Surface-level criteria (transactional = relational, logs = NoSQL)                              |
| Cloud data platform expertise (AWS, Azure, or GCP)                          | 1                 | Resume: 5 AWS certifications (Dec 2025-Mar 2026), AWS Services listed                 | Interview: **MAJOR DISCONNECT** - said "I haven't done a lot" of managed services despite recent certs    |
| Data warehouse design and implementation                                    | N/A               | Resume: Not mentioned                                                                 | Interview: Brief mention in passing, no details                                                           |
| ETL/ELT pipeline design and data processing architectures                   | 2                 | Resume: ezPie orchestration engine at Fannie Mae (2015-2018)                          | Interview: Focused on 10+ year old Logi Analytics ETL tool                                                |
| Event-driven architectures, CDC, streaming platforms                        | 1                 | Resume: **Event-driven microservice SAGA architecture, Kafka** at US Bank (2022-2025) | Interview: **NOT DISCUSSED** - candidate didn't mention recent Kafka/event-driven work                    |
| Data architecture for ML/LLM applications                                   | 1                 | Resume: TensorFlow/Python ML at Fannie Mae (2015-2018)                                | Interview: Only mentioned vector databases to criticize AI tools                                          |
| Zero-downtime data migration and schema evolution                           | N/A               | Resume: "Migration from monolithic to event-driven microservices"                     | Interview: Not discussed, no depth demonstrated                                                           |
| Data quality, monitoring, and observability practices                       | N/A               | Resume: Not mentioned                                                                 | Interview: Not discussed                                                                                  |
| Aligning data ownership models with domain boundaries                       | N/A               | Resume: Not mentioned                                                                 | Interview: Not discussed                                                                                  |
| Hands-on troubleshooting and optimization                                   | 2                 | Resume: VP Principal Engineer at US Bank suggests hands-on                            | Interview: Limited recent examples, most dated                                                            |
| Proficiency in modern programming languages                                 | 2                 | Resume: Java, Python (Pandas/Boto3), C#.NET                                           | Interview: Only discussed C#, VB6, JDBC - didn't mention Python despite resume                            |

**Critical Disconnect:** Resume shows recent, relevant experience (US Bank 2022-2025: Kafka, Spring Boot, event-driven architecture, microservices) and very recent AWS certifications (2025-2026), but candidate **could not articulate any of this** in the interview. Spent most time on 10+ year old Logi Analytics work instead of showcasing recent accomplishments.

**Skills Summary:** **Major red flag - critical disconnect between resume and interview performance.** Resume shows recent, highly relevant experience:
- US Bank VP Principal Engineer (March 2022 - June 2025) with event-driven microservices, Kafka, Spring Boot, SAGA patterns
- 5 AWS certifications earned Dec 2025 - Mar 2026 (extremely recent)
- Python/Pandas work at Capital One (2018-2022)
- Patent holder with documented innovation

**However, in the interview:**
- Couldn't articulate any of this recent work effectively
- When asked about career, spent most time on 10+ year old Logi Analytics examples
- Said "I haven't done a lot" of managed services **despite 5 recent AWS certifications**
- Never mentioned Kafka or event-driven architecture **despite resume highlighting this**
- Went on tangents about code quality automation (Fannie Mae 2015-2018) instead of recent data architecture
- Used outdated/incorrect terminology ("Azure Tables")
- Surface-level reasoning about technology selection

**Assessment:** Either (1) candidate cannot effectively communicate their own work, (2) resume overstates depth of involvement, or (3) candidate wasn't paying attention to the questions. All three scenarios are disqualifying for a Principal Engineer role requiring team enablement and collaboration.

---

## Personality Traits Assessment

| Trait                                                                | Score | Evidence                                                                                                                                                                                                                       |
| -------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Enabling mindset - succeeds by making others successful              | N/A   | Not enough signal. No stories about enabling teams or empowering others.                                                                                                                                                       |
| Educates and empowers rather than gatekeeps                          | N/A   | Not enough signal from interview.                                                                                                                                                                                              |
| Hands-on and takes ownership                                         | 2     | US Bank story suggests some hands-on work but lacks detail and credibility. Most recent work unclear.                                                                                                                          |
| Can influence without authority                                      | N/A   | Not discussed. Committee work at US Bank mentioned but not elaborated.                                                                                                                                                         |
| Pragmatic judgment - knows when to optimize for speed vs. perfection | N/A   | Not enough signal.                                                                                                                                                                                                             |
| Comfortable with ambiguity and building from scratch                 | N/A   | Not enough signal from interview.                                                                                                                                                                                              |
| Works effectively in modern agile/iterative development processes    | N/A   | Not discussed.                                                                                                                                                                                                                 |
| Collaborates effectively across teams                                | 1     | Goes on tangents frequently. Doesn't listen well to questions. Focuses on his own past rather than understanding current needs.                                                                                                |
| Communicates technical concepts effectively                          | 1     | **Major red flag:** Long rambling answers. Goes off on tangents about microservices, "paved road" concepts, code quality tools. Doesn't stay focused on questions asked. Uses outdated/incorrect terminology ("Azure Tables"). |

**Personality Traits Summary:** Communication is a major concern - candidate goes on tangents, doesn't stay focused, uses outdated vocabulary. Shows poor listening skills and doesn't adapt responses to interviewer's questions. No evidence of collaborative or enabling mindset.

---

## Qualifications Assessment

| Qualification | Score | Evidence |
|---------------|-------|----------|
| 10+ years of hands-on experience building software applications | 2 | Claims many years of experience but most concrete examples are 10+ years old (Logi Analytics, Fannie Mae). Recent work at Capital One/US Bank lacks detail. |
| Strong application development background | 1 | No evidence of application development work. Most experience is old tooling/infrastructure work (Logi Analytics data engine, Fannie Mae code quality automation). |
| Track record of establishing data standards | N/A | Not discussed or demonstrated. |
| Experience leading data migrations | N/A | Mentions US Bank went through platform changes (Microsoft → AWS → on-prem) but doesn't discuss leading migrations. |
| Prior Principal Engineer, Staff Engineer experience | N/A | Not discussed. Resume not reviewed in detail during interview. |
| Bachelor's degree in Computer Science | N/A | Not discussed in interview. |

**Qualifications Summary:** Limited evidence of recent hands-on application development. Most concrete examples are 10+ years old. No demonstrated track record of establishing standards or leading teams. Unclear what candidate has been doing recently.

---

## Other/Details

| Item | Score | Evidence |
|------|-------|----------|
| Healthcare or EDI domain knowledge | N/A | Not discussed. |
| Experience in enabling team or platform team models | N/A | US Bank committee work mentioned but not elaborated. No evidence of platform/enabling team experience. |
| Experience with autonomous or cross-functional teams | N/A | Not discussed. |
| Experience with AI/LLM-assisted development tools and agentic software engineering | 1 | Mentions AI coding tools only to criticize them. Shows resistance to modern AI-assisted development. Example: "I asked it to build a one page script and it got to 23 files... Why is it doing this? And I looked at the code and it was horrible." |

---

## Overall Assessment

**Key Concerns:**

**1. CRITICAL: Resume-Interview Disconnect**
- Resume shows recent, relevant work (US Bank 2022-2025: Kafka, event-driven architecture, Spring Boot microservices, SAGA patterns)
- Resume shows 5 AWS certifications earned Dec 2025 - Mar 2026 (extremely recent)
- Candidate **could not articulate any of this** in the interview
- When asked about career, spent time on 10+ year old Logi Analytics work
- Said "I haven't done a lot" of managed services **despite recent AWS certifications**
- Never mentioned Kafka or event-driven work **despite resume highlighting this as primary US Bank accomplishment**

**2. Communication & Professionalism Issues**
- Goes on long tangents (microservices philosophy, "paved road" concepts, code quality automation)
- Doesn't listen to or directly answer questions
- Uses outdated/incorrect terminology ("Azure Tables" - not a product)
- Can't effectively communicate own work history

**3. Missing Critical Context**
- US Bank role ended June 2025 (only 11 months ago) - why not featured prominently?
- Recent AWS certifications (Dec 2025-Mar 2026) - why claim limited managed service experience?
- Patent #11,256,664 - mentioned at end as afterthought, not highlighted

**4. Wrong Approach for Role**
- This role requires **enabling application teams** through clear communication and teaching
- Candidate cannot clearly explain technical concepts
- Demonstrates poor listening and adaptation
- Shows resistance to modern tools (AI-assisted development criticism)

**Key Strengths:**
- Resume looks strong on paper (if accurate)
- Patent holder
- Recent certifications

**Fit for Role:** 1 (Definitely Not)

**Reasoning:** 

Richard is a **definitive pass** for this role. The most concerning issue is not lack of experience (resume suggests relevant experience exists) but rather the **complete inability to articulate that experience:**

1. **Cannot effectively communicate own experience:**
   - Resume shows US Bank work (2022-2025) with Kafka, event-driven architecture, Spring Boot, SAGA patterns
   - In interview, spent most time on 10+ year old Logi Analytics work instead
   - Never mentioned event-driven architecture or Kafka despite being primary resume accomplishment
   - When asked about managed services, said "I haven't done a lot" despite 5 AWS certifications earned Dec 2025-Mar 2026

2. **Critical for Principal role: This position requires enabling application teams through teaching and clear communication**
   - If candidate cannot clearly explain their own recent work, they cannot enable teams
   - Goes on tangents constantly - shows inability to tailor message to audience
   - Uses incorrect terminology ("Azure Tables") - suggests surface-level understanding despite certifications
   - Poor listening skills - doesn't adapt responses to questions asked

3. **Resume-interview disconnect raises credibility concerns:**
   - Three possible explanations, all disqualifying:
     - **(A) Resume overstates involvement** - if so, credibility issue
     - **(B) Cannot articulate own work** - if so, communication/enablement failure for Principal role  
     - **(C) Wasn't paying attention to questions** - if so, professionalism concern
   
4. **Missing depth in critical areas (even with resume context):**
   - Surface-level reasoning about technology selection (transactional = relational, logs = NoSQL)
   - No discussion of: cost optimization, team capabilities, operational overhead, data modeling, governance
   - Can't explain modern patterns: data mesh, domain-driven design, team autonomy implications
   - Negative toward AI-assisted development - suggests resistance to modern practices

5. **Interview approach suggests wrong fit:**
   - Focuses on old tooling/infrastructure work (Logi Analytics data engine, Fannie Mae code quality)
   - Role requires working embedded with application teams
   - Candidate's framing is traditional DBA/platform rather than application-focused

The interviewer's immediate assessment remains accurate: "This is a clear pass. Makes me wonder why the agency thought he was a good fit."

**Most concerning:** For a Principal Engineer role requiring team enablement, the inability to clearly communicate recent, relevant experience is **disqualifying regardless of what's on the resume.**

**Recommendation:** ☒ Do Not Advance

**Feedback to Agency:** 

Critical issue: **Resume-interview disconnect.** Candidate's resume shows relevant recent experience (US Bank 2022-2025: Kafka, event-driven architecture, Spring Boot) and recent AWS certifications (Dec 2025-Mar 2026), but **could not articulate any of this** in the interview.

**Specific concerns:**
1. When asked about career, spent time on 10+ year old work (Logi Analytics) instead of recent US Bank accomplishments
2. Said "I haven't done a lot" of managed services despite 5 recent AWS certifications
3. Never mentioned Kafka or event-driven architecture despite this being primary resume accomplishment
4. Poor communication - long tangents, doesn't listen, uses incorrect terminology
5. Cannot effectively explain own recent work

**For Principal Engineer role requiring team enablement:** Communication ability is **as critical as technical skills.** If a candidate cannot clearly articulate their own recent experience, they cannot enable application teams.

**What we need:**
- **Candidates who can clearly communicate technical concepts** (this is a teaching/enabling role)
- Strong application development background with data focus (embedded with app teams, not isolated)
- Modern data architecture experience they can **articulate clearly** (streaming, event-driven, cloud-native)
- Demonstrated collaboration and listening skills
- Recent hands-on work they can discuss in depth

**Please recalibrate:** "Principal Data Architect for application teams" means working side-by-side with engineers, not traditional DBA or infrastructure tooling. Communication and teaching ability are as important as technical depth.

---

## Interview Notes

**Interviewer's raw notes:**
- "Spend a lot of time on very old experiences... a little out of touch/missing the mark"
- "Bullshit detector is going off here..."
- "Goes on tangents all the time..."
- "This is a clear pass. Makes me wonder why the agency thought he was a good fit."

**Post-Interview Resume Review:**

After reviewing the actual resume, the pass decision stands but with additional context:

**Resume shows:**
- US Bank VP Principal Engineer (March 2022 - June 2025) - ended just 11 months ago
- Event-driven microservice SAGA architecture with Kafka and Spring Framework
- Credit card spend limit optimization (39 min → 7ms using custom SQL and Spring Data JDBC)
- ICS/ECIC Architecture Committee voting member
- 5 AWS certifications: Data Engineer (Dec 2025), ML Associate (Oct 2025), Solutions Architect (Sep 2025), AI Practitioner (Sep 2025), Cloud Practitioner (May 2025)
- Patent #11,256,664 for memory management system
- Python/Pandas/Boto3 work at Capital One (2018-2022)

**But in 30-minute interview:**
- Never mentioned Kafka or event-driven architecture
- When asked about career, focused on Logi Analytics (2007-2015) 
- When asked about managed services: "I haven't done a lot" (despite 5 recent AWS certs)
- US Bank work mentioned only briefly with unconvincing explanation
- Patent only mentioned at end when prompted

**Critical concern:** Resume looks much stronger than interview performance. This disconnect is **more disqualifying** than lacking experience entirely because:
1. If resume is accurate → candidate cannot communicate own work (fatal for Principal/enabling role)
2. If resume is inflated → credibility issue
3. Either way → cannot enable application teams through teaching/communication

**Key moments that led to pass decision:**
1. When asked about managed data services: "I haven't done a lot" - contradicts 5 recent AWS certifications (Dec 2025-Mar 2026)
2. References "Azure Tables" as a product (it's not) - despite recent certifications showing outdated knowledge
3. MongoDB experience "could have been 10 years ago" - not even mentioned on resume
4. Spends 10+ minutes on Fannie Mae code quality automation (2015-2018) instead of recent US Bank data architecture (2022-2025)
5. Never mentions Kafka, event-driven architecture, or SAGA patterns despite being primary US Bank accomplishment on resume
6. Can't articulate clear criteria for technology selection - surface-level reasoning despite Architecture Committee experience on resume
7. Poor communication throughout - tangents, doesn't listen, can't adapt message to audience
