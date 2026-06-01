---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Matt Ford
date: 2026-05-18
interviewer: Marten Engblom
stage: hm-screen
---

# Interview Scorecard: Matt Ford
**Role:** Principal Software Engineer, Data Architecture and Engineering
**Date:** 2026-05-18
**Stage:** HM Screen (30 min)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill                                                                           | Score | Resume Evidence      | Interview Evidence                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------- | ----- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server)     | 4     | Resume: Not provided | Interview: Strong experience with PostgreSQL (created data warehouse/egress database in Azure), SQL Server, Oracle. 20 years of database work at Best Buy and Gemini.                                                                                      |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB)               | 3     | Resume: Not provided | Interview: Has MongoDB experience (partner portal at Gemini), working with CDC data streams and Debezium. Built spark connector as workaround for Microsoft Fabric defect. Experience appears more on read/analytics side than deep operational expertise. |
| Database performance optimization at scale                                      | N/A   | Resume: Not provided | Interview: Not discussed in detail - mentioned query tuning context but no specific examples shared.                                                                                                                                                       |
| Advanced data modeling and schema design                                        | 3     | Resume: Not provided | Interview: Created dimensional models, Medallion architecture (bronze/silver/gold), ontology layers. Strong data warehouse modeling but less evidence of operational/transactional schema design for applications.                                         |
| Application development skills                                                  | 3     | Resume: Not provided | Interview: 60% time on software side at Best Buy (mostly data pipelines). Some front-end work (vanilla JavaScript, CSS, React). Created e-procurement transformations. Secondary to BI/reporting focus.                                                    |
| Can review application code and architecture with focus on data access patterns | 2     | Resume: Not provided | Interview: Experience mostly with BI/reporting infrastructure rather than embedded application architecture review. Mentions being part of software team but focus was data pipelines and reporting.                                                       |
| Experience evaluating and selecting database technologies                       | 4     | Resume: Not provided | Interview: Strong evidence - evaluated Snowflake vs. Fabric, chose Fabric for Gemini. Pragmatic about technology selection (demos, testing, avoiding gotchas). Considers supported patterns vs. anti-patterns.                                             |
| Cloud data platform expertise (AWS, Azure, or GCP)                              | 4     | Resume: Not provided | Interview: Heavy Azure/Microsoft Fabric expertise. Created full Fabric implementation at Gemini (lakehouse, event streams, ontology, pipelines). Brief AWS experience (6 months with S3/Glue). Deep Microsoft ecosystem knowledge.                         |
| Data warehouse design and implementation                                        | 5     | Resume: Not provided | Interview: Excellent evidence - Created data mart at Best Buy, Oracle data warehouse with dimensional modeling. Full Medallion architecture at Gemini (bronze/silver/gold). Clearly a strength.                                                            |
| ETL/ELT pipeline design and data processing architectures                       | 5     | Resume: Not provided | Interview: Strong - SSIS pipelines at Best Buy, Fabric pipelines at Gemini, custom spark connectors. Handles real-time event streams, batch processing, incremental loads (high water marks).                                                              |
| Event-driven architectures, change data capture, and streaming platforms        | 3     | Resume: Not provided | Interview: Working with MongoDB CDC via Fabric event streams (Kafka-like). Built custom Debezium-based spark connector. Experience appears more operational/troubleshooting than architectural design.                                                     |
| Data architecture for ML/LLM applications                                       | 2     | Resume: Not provided | Interview: Mentioned connecting Claude to MCI through Fabric ontology for sales/quotes, helping team build AI models with LLMs. Very early stage exploration, not deep architectural experience.                                                           |
| Zero-downtime data migration and schema evolution strategies                    | N/A   | Resume: Not provided | Interview: Not discussed.                                                                                                                                                                                                                                  |
| Data quality, monitoring, and observability practices                           | N/A   | Resume: Not provided | Interview: Not discussed in detail.                                                                                                                                                                                                                        |
| Aligning data ownership models with domain boundaries                           | 2     | Resume: Not provided | Interview: Focus on centralized BI/reporting models (data marts, data warehouse). Less evidence of distributed domain-driven data ownership patterns.                                                                                                      |
| Hands-on troubleshooting and optimization of production data systems            | 4     | Resume: Not provided | Interview: Strong evidence - Troubleshot Microsoft Fabric/MongoDB CDC defect for 3 months, built workaround. Clearly hands-on with production issues.                                                                                                      |
| Proficiency in modern programming languages                                     | 3     | Resume: Not provided | Interview: JavaScript (vanilla, React), Python (mentioned pyrq/parquet scripts). Primarily data pipeline scripting vs. application development.                                                                                                            |

**Skills Summary:**

Matt brings strong traditional BI/data warehousing expertise with deep Microsoft ecosystem knowledge (Fabric, SSIS, SSRS, Azure). His 20-year career shows solid technical execution in building data marts, dimensional models, and reporting infrastructure. He demonstrates hands-on problem-solving ability (e.g., building custom MongoDB spark connector to work around Microsoft defect).

However, his experience profile leans heavily toward analytics and reporting rather than application-embedded data architecture. His software development background exists but appears secondary to his BI focus - he describes spending 60% of time on "software side" at Best Buy but clarifies this was "mostly data pipelines, not front-end." His current role involves training business users on reporting tools and building gold data marts, which differs from the embedded architectural guidance model this position requires.

The role requires a Principal Engineer who works side-by-side with application teams, reviewing code and architecture patterns, making real-time technology decisions, and enabling teams through hands-on collaboration. Matt's experience suggests more of a BI/analytics platform builder who creates infrastructure that application teams consume, rather than embedding within application teams to guide their data decisions.

---

## Personality Traits Assessment

| Trait                                                                | Score | Resume Evidence      | Interview Evidence                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------- | ----- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabling mindset - succeeds by making others successful              | 4     | Resume: Not provided | Interview: Conducts bi-weekly training sessions for operations SMEs at Gemini. Walking team through reports, identifying gaps, building governed models. Helping people who want to become data scientists. Promoted data governance manager and guiding him. Clear enablement focus.                                                                |
| Educates and empowers rather than gatekeeps                          | 4     | Resume: Not provided | Interview: Strong evidence of teaching (training sessions, guiding new governance manager, helping aspiring data scientists). Shares knowledge openly.                                                                                                                                                                                               |
| Hands-on and takes ownership                                         | 5     | Resume: Not provided | Interview: Built custom spark connector when Microsoft tool failed. Spent 3 months battling Microsoft on defect. Solo operator when team funding fluctuated at Best Buy. Clearly takes ownership and doesn't wait for others.                                                                                                                        |
| Can influence without authority                                      | 3     | Resume: Not provided | Interview: "Convinced" Gemini CTO to go with Fabric. Has pushed for automation. Some evidence but limited examples in 30-minute conversation.                                                                                                                                                                                                        |
| Pragmatic judgment - knows when to optimize for speed vs. perfection | 4     | Resume: Not provided | Interview: Chose low-code Fabric approach for "quick turnaround." Built workaround for MongoDB issue that costs more but "at least we're getting our data right now, which is pretty critical." Demonstrates pragmatic trade-offs.                                                                                                                   |
| Comfortable with ambiguity and building from scratch                 | 5     | Resume: Not provided | Interview: Excellent evidence - Walked into "old monolithic systems" at Gemini, built entire Medallion architecture from scratch. At Best Buy: "a lot of report dumps existed, a lot of missed synchronicities, backs, jobs, things that just weren't really normalized or standardized." Clearly comfortable with greenfield/brownfield challenges. |
| Works effectively in modern agile/iterative development processes    | 2     | Resume: Not provided | Interview: Describes Best Buy as "everything was waterfall, no agile, it was insane" - but no evidence he pushed back or brought agile practices. At Gemini appears to be sole technical decision maker (not collaborative agile team environment).                                                                                                  |
| Collaborates effectively across teams                                | 3     | Resume: Not provided | Interview: Works with operations SMEs, data governance manager, aspiring data scientists. But current role appears more hierarchical (training/guiding) than peer collaboration. Was "part of core software team" at Best Buy but limited detail.                                                                                                    |
| Communicates technical concepts effectively                          | 4     | Resume: Not provided | Interview: Clearly explained complex technical concepts in interview (Medallion architecture, CDC, event streams, dimensional modeling). Runs training sessions for non-technical operations staff. Good communicator.                                                                                                                               |

**Personality Traits Summary:**

Matt demonstrates strong hands-on ownership mentality and genuine enablement mindset through teaching and knowledge sharing. He's comfortable with ambiguity and building from scratch (transformed brownfield systems at both Best Buy and Gemini). Shows pragmatic judgment in making technology trade-offs.

Areas of uncertainty: His collaboration experience appears more vertical (training less technical staff) than horizontal (peer collaboration with engineering teams). His agile/iterative process experience is unclear - Best Buy was "waterfall, no agile" and his current role at Gemini sounds like solo technical architecture work rather than collaborative team-based delivery.

For a Principal Engineer role requiring "influence without authority" and "collaborates effectively across teams" in an autonomous team model, his experience pattern suggests he's been more of a solo technical leader or trainer rather than an embedded peer collaborator.

---

## Qualifications Assessment

| Qualification                                                                                 | Score | Resume Evidence      | Interview Evidence                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------- | ----- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 10+ years hands-on experience building software applications with heavy focus on data systems | 3     | Resume: Not provided | Interview: 20 years in "data and analytics" - strong data systems experience. Software application building appears secondary (60% time at Best Buy on "software side" but "mostly data pipelines, not front-end"). More BI infrastructure than application development. |
| Strong application development background (not just database administration)                  | 2     | Resume: Not provided | Interview: Has application development experience (JavaScript, React, e-procurement transformations) but describes it as "filling gaps" and secondary to BI/reporting focus. Not a strong application developer profile.                                                 |
| Track record of establishing data standards and patterns across engineering organizations     | 3     | Resume: Not provided | Interview: Set up data warehouse with dimensional modeling at Best Buy, created standards there. Building governed data models at Gemini with endorsement process. Standards work appears within BI/analytics context rather than application engineering standards.     |
| Experience leading data migrations and infrastructure modernization initiatives               | 5     | Resume: Not provided | Interview: Excellent evidence - Led infrastructure modernization at Gemini (legacy systems to Fabric, MongoDB integration). "Brought them up to qualified tier one systems." Walked into monolithic situation and modernized. This is clearly a strength.                |
| Experience with AI/LLM-assisted development tools and agentic software engineering practices  | 2     | Resume: Not provided | Interview: "Starting to build AI models using LLMs, connected Claude to MCI through Fabric ontology." Very early exploration, not established practice. No mention of AI-assisted development tools (Copilot, Claude Code, etc.) in his own workflow.                    |
| Prior Principal Engineer, Staff Engineer, or senior technical leadership experience           | N/A   | Resume: Not provided | Interview: No explicit title mentioned. At Best Buy, team structure fluctuated - sometimes led team, sometimes solo. At Gemini, brought in by CTO to modernize, appears to be senior technical leader but title not discussed.                                           |
| Bachelor's degree in Computer Science or equivalent practical experience                      | N/A   | Resume: Not provided | Interview: Not discussed. 20 years practical experience evident.                                                                                                                                                                                                         |

**Qualifications Summary:**

Matt has strong infrastructure modernization credentials - successfully led transformation from legacy systems to modern cloud data platform at Gemini. His 20-year career shows deep practical experience in data systems, though more concentrated in BI/analytics than application development.

Key gap: The role requires "strong application development background (not just database administration)" and Matt's profile is essentially the inverse - strong BI/data warehouse background with some application development experience. He describes his software work as "filling gaps" and secondary to his BI focus. His modernization experience is valuable but in a different context (BI platform transformation vs. application data architecture evolution).

The AI/LLM experience requirement is barely addressed - he's starting to explore it at Gemini but has no established practice. No mention of using AI-assisted development tools in his own work.

---

## Other/Details

| Item | Score | Resume Evidence | Interview Evidence |
|------|-------|-----------------|-------------------|
| Healthcare or EDI domain knowledge | 2 | Resume: Not provided | Interview: Best Buy experience with e-procurement (cXML transformations, catalogs, order placements, EDI documents, FTP/SFTP, XMLs, JSONs, CSVs). Understands B2B document transformation. No healthcare experience mentioned. Some EDI exposure but not deep. |
| Experience in enabling team or platform team models | 3 | Resume: Not provided | Interview: Builds platforms that teams consume (data marts, BI infrastructure). Enables through training and tooling. Less evidence of embedded enabling team model where he works within application teams. |
| Experience with autonomous or cross-functional team environments | 2 | Resume: Not provided | Interview: Best Buy described as waterfall, not agile. Current role appears solo architect building centralized platform. Limited evidence of autonomous team experience. |

---

## Overall Assessment

**Key Concerns:**

1. **BI/Analytics Profile vs. Application-Embedded Architecture Role:**
   - Matt has built an excellent 20-year career in BI and analytics engineering
   - His strength is building centralized data platforms (data warehouses, data marts, reporting infrastructure) that application teams consume
   - The Principal Data Architect role requires embedding with application teams, reviewing their code and architecture, making technology decisions in context of application needs
   - When asked about working with application teams, Matt described being "part of the core software engineer team" at Best Buy but clarified he spent time on "data pipelines, not front-end" and filled gaps with "vanilla JavaScript"
   - His current role involves training business users on reporting tools and building gold data marts - not embedded architecture guidance

2. **Limited Modern Team Collaboration Experience:**
   - Best Buy: "everything was waterfall, no agile, it was insane" - and no evidence he drove agile transformation
   - Current role at Gemini: appears to be solo technical architect making centralized platform decisions
   - Enablement approach is vertical (training less technical staff) rather than horizontal (peer collaboration with engineers)
   - Role requires "influence without authority" and "collaborates effectively across teams" in autonomous team model - his experience suggests hierarchical technical leadership

3. **Software Development as Secondary Skill:**
   - Role requires "strong application development background (not just database administration)"
   - Matt's profile is essentially the inverse: strong data warehouse/BI background with some application development
   - He describes 60% time on "software side" at Best Buy but clarifies this was "mostly data pipelines, not front-end" work
   - Application development appears as gap-filling rather than core competency

4. **Seeking Build Phase vs. Embedded Collaboration:**
   - Main driver for job search: "almost into maintenance mode instead of build mode"
   - Wants to "keep learning, keep evolving instead of 'is that table updated?'"
   - This suggests he's looking for another platform-building greenfield opportunity
   - The role we're hiring for isn't about building a new platform - it's about embedding with teams to guide their data decisions within existing and evolving systems

**Key Strengths:**

- Strong hands-on technical execution (built custom spark connector as workaround, troubleshot production issues)
- Successful infrastructure modernization track record (transformed Gemini from legacy to modern cloud platform)
- Deep Microsoft ecosystem expertise (highly relevant if we expand Azure footprint)
- Genuine teaching and enablement mindset (trains non-technical staff, guides aspiring data scientists)
- Comfortable with ambiguity and brownfield transformation
- Pragmatic judgment in technology trade-offs (speed vs. cost vs. perfection)

**Fit for Role:** 2/5 (No)

**Reasoning:**

This is a classic profile mismatch rather than a capability issue. Matt is an accomplished BI/analytics platform engineer with strong technical execution skills and genuine passion for his work. However, the Principal Data Architect role requires someone who embeds within application teams, reviews application code and architecture, guides data technology decisions in real-time, and enables through hands-on collaboration with engineers.

Matt's career has been built around creating centralized BI infrastructure that application teams consume - data warehouses, data marts, reporting platforms. His enablement approach involves training business users on reporting tools and building governed data models. When describing his software development work, he positions it as secondary to his BI focus and describes it as "filling gaps."

**Most concerning:** The role requires "strong application development background (not just database administration)" and the scorecard emphasizes this is not a DBA role. Matt's profile is the inverse - it's essentially a senior BI/analytics engineer who does some application work. His job search motivation ("build mode vs. maintenance mode") suggests he wants another platform-building greenfield opportunity, which isn't what this embedded architecture role offers.

For a Principal Engineer role that requires working side-by-side with application teams in an autonomous team environment, his experience pattern (solo platform architect, waterfall environment, vertical enablement through training) doesn't align with our needs.

**Recommendation:** ☒ Do Not Advance

**Feedback to Agency:**

**Critical mismatch: BI/Analytics Engineer profile vs. Application-Embedded Architect role.**

Matt Ford is clearly an accomplished professional with 20 years of strong technical execution in BI and analytics engineering. His infrastructure modernization work at Gemini demonstrates hands-on problem-solving and solid technical judgment. However, his experience profile doesn't match what we need for this Principal Data Architect position.

**The mismatch:**
- **What Matt has built his career on:** Centralized BI/analytics platforms - data warehouses, data marts, dimensional models, reporting infrastructure that application teams consume
- **What this role requires:** Embedding within application teams, reviewing application code and architecture, guiding data technology decisions in real-time, enabling through hands-on peer collaboration

**Specific evidence:**
- When asked about working with application teams, Matt described being "part of core software engineer team" at Best Buy but clarified he spent time on "data pipelines, not front-end" and filled gaps with basic JavaScript
- His current role involves training business users on reporting tools and building gold data marts - not embedded architecture guidance
- Job search motivation: "almost into maintenance mode instead of build mode" - suggests he wants another platform-building greenfield opportunity, not embedded team collaboration
- Best Buy environment was "waterfall, no agile" with no evidence he pushed for modern practices; current role appears to be solo architect role

**What we need:**
- "Strong application development background (not just database administration)" - this is called out explicitly in the scorecard because we're not hiring a DBA or BI engineer
- Someone who works side-by-side with application engineering teams in autonomous/cross-functional environments
- Experience in modern agile/iterative processes with peer collaboration (not hierarchical training model)
- Hands-on application code review and architecture guidance embedded within teams
- Understanding of application data patterns (not just analytical/reporting patterns)

**Please recalibrate:** "Principal Data Architect for application teams" means someone whose primary experience is building data-intensive applications or being embedded within application engineering teams to guide data architecture decisions. We need someone from the application engineering world who specializes in data, not someone from the BI/analytics world who does some application work.

**Strong candidates will have:**
- Built or significantly contributed to data-intensive applications (not BI platforms)
- Worked in modern autonomous team environments with agile/iterative practices
- Peer collaboration experience (not training business users on reporting tools)
- Application code review and architecture guidance as core responsibility
- May come with titles like: Principal/Staff Engineer with data focus, application architect with database expertise, or senior backend engineer specializing in data systems

---

## Interview Notes

**Interviewer's raw notes:**
- Experience in ecommerce
- Lots of analytics / reporting related data experience
- Experience with walking into a monolithic situation
- Experience with real time event streams for MongoDB
- Data warehouse experience (mentioned medallion structure)
- Data Store Products: MySQL, Oracle, MS SQL, SSIS, PostgreSQL, Azure Synapse, MongoDB

**Key moments that led to decision:**

1. **Career summary response (lines 61-63):** Matt's own description of his career emphasized "data and analytics" work, creating "data mart," building "reports using SSRS," handling "transformations." The software work was described as secondary: "At best buy, I would say 60% of my time on average throughout that entire time was probably on the software side. Generally with data pipelines, though, not necessarily... there was some front end work here and there, you know, filling gaps for people."

2. **Current role description:** When asked about his team at Gemini, Matt described conducting "bi-weekly training sessions" to build "gold data marts" for operations SMEs who were "used to connecting through ODBC... directly to the transactional database." This is classic BI enablement through training and tooling, not embedded architecture collaboration with application engineers.

3. **Working with application teams (lines 82-84):** When asked directly about dynamics with application teams building on data stores, Matt said he was "part of the core team" but then described working mostly on "data pipelines" and "some front end work here and there, you know, filling gaps" with "vanilla JavaScript." The application development was clearly supplementary to his BI focus.

4. **Job search motivation (lines 99-101):** "At the point where I would like to expand out a little bit more now that we're unfortunately more tightened into fabric. I blew through that. No problem to set up everybody. Pretty solid there. Again, getting into the governance side now at this point. So it's almost into maintenance mode instead of build mode." Seeking another platform-building opportunity, not looking to transition into embedded team collaboration.
