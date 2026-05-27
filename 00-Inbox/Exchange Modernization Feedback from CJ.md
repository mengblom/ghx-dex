### Feeback from CJ: ###
- Add a target date for Breaking the Monolith "good enough interim state"
- ICS move to the bottom
- Big tech priorities done by ?
- Capacity pie chart progression
- Specifics of the monolith breakup (ok if it is work in progress)

## Updated Slide Outline (based on the feedback) ##
1. Why are we here - 3 asks from CJ:
	1. Exchange Productivity Commentary - How are things going
	2. Exchange Resiliency
		1. Progress update on the following Exchange Resiliency items from [2026 Tech Org Priorities.pptx](https://ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/Documents/2026/2026%20Tech%20Org%20Priorities.pptx?d=w3d38032c08714d5eb49a0b00d8ecc1ae&csf=1&web=1&e=YA9zG0&nav=eyJzSWQiOjIxNDc0ODM2MjgsImNJZCI6MjEyNjg5NTUyOH0)
	3. Capacity Piechart Forecast
		1. When will we start shifting away from the current capacity allocation (25% commercial / 75% technical) towards a more normal (70% commercial / 30% technical)
2. Productivity Assessment - Positive signs in the data
	1. Stories completed (Jan, Feb, Mar): 207 - 271 - 386 (stories)
	2. Lead time to change (Jan, Feb, Mar):  30 - 33 - 8 (days)
	3. Cycle time  (Jan, Feb, Mar): 44 - 44 - 23 (days)
3. Other Improvements
	1. Org changes / hiring / talent upgrade
4. Update on Exchange Resiliency (from [2026 Tech Org Priorities.pptx](https://ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/Documents/2026/2026%20Tech%20Org%20Priorities.pptx?d=w3d38032c08714d5eb49a0b00d8ecc1ae&csf=1&web=1&e=YA9zG0&nav=eyJzSWQiOjIxNDc0ODM2MjgsImNJZCI6MjEyNjg5NTUyOH0)) - table with 3 columns (Priority, Status, Notes)
	1. DB Migration to managed databases​ | On Track (green) | Atlas Migration completion Aug 19
	2. Disaster Recovery (4h RTO, 2h RPO) | On Track (green) | Lower environment test on May 4: RTO 7h, RPO 0:15h, internal target October, External comms December
	3. All vulnerabilities within SLA / Eliminate EOL technologies | Mixed (yellow) | Red Mythos June 2 date at risk, tracking for July finish
	4. Industry Continuity Solution | On Track (green) | Building GHXi FTE team to own this
	5. Increase Modularity, i.e. continue breaking the monolith | In Progress | "Good enough" stage by end of Q4 - Next slides
5. We are held back by the monolith, improvements will be incremental until we have **Autonomous Teams**
	1. So what does "Autonomous Teams" mean?
	2. Autonomous Teams / Break the Monolith - "good enough" Phase 1 Definition of Done:
		1. Org change - New Team topology, aligned to future decoupled architecture. I.e. "Reverse Conway Maneuver". This has been done.
		2. Teams Correctly Staffed (in progress):
			1. Dedicated Engineering Manager
			2. Dedicated Product Owner
			3. Key Roles Filled
		3. It is 100% clear to everyone what each team owns (mutually exclusive and collectively exhaustive)
		4. Each team can deploy independently, on demand / at will
			1. Their components' code are decoupled, i.e. sits in a stand alone repo (or at least in a "modular monolith")
			2. The team owns and operates the deployment pipelines for their components
			3. They can deploy their components without coordinating with other teams as long as no APIs, contracts or data models are changed
6. Other Technical Work:
	1. MUST DO Technical Work (cannot shift away technical capacity until this is done):
		1. Address the most egregious issues in our data layer (Data stored in the correct "products" - move to cloud native / infinitely scalable (DynamoDB, S3 etc.) where appropriate, read and write patterns considered when choosing where and how to store data, redirect dependencies to Common Data Platform (CDP) where appropriate, be thoughtful and intentional about data retention,...) 
			1. Scalability
			2. Cost
			3. HA / DR is literally a setting
	2. Other Technical Work - Still required and urgent, but timing is negotiable/trade-offs possible (will continue to hold us back, or said differently, I'd be shocked if Veritas / Kickdrum doesn't comment on this)
		1. Event / Messaging system (get rid of the Mongo based "Event Bus")
		2. Infinitely scalable queue processors/event subscribers (lambdas, etc.)
		3. Cloud native infra (move off EC2 to containers and managed services)
		4. Observability
7. Timeline Slide - graphic showing the following 2 things:
	1. Where critical work falls on the timeline:
		1. MongoDB to Atlas | January 2026 - August 2026
		2. Disaster Recovery | April 2026 - December 2026 (tapers off starting in October 2026)
		3. Red Mythos (vulnerabilities/ EOL technologies) | April 2026 - July 2026 (tapers off starting in June 2026)
		4. Autonomous Teams / Break the Monolith | March 2026 - December 2026
		5. P0 Database Improvements | September 2026 - March 2027
		6. Other (Event / Messaging, cloud native infra, ... | January 2027 - ongoing
	2. How the Engineering capacity breakdown (Commercial / Technical) changes over time:
		1. Q1 2026: 25/75
		2. Q2 2026: 25/75
		3. Q3 2026: 25/75
		4. Q4 2026: 25/75
		5. Q1 2027: 50/50
		6. Q2 2027: 50/50
		7. Q3 2027: 70/30
8. Risks (table with 3 columns: Initiative, Risks, Mitigations)
	1. MongoDB to Atlas
		1. Risks: Minimal Risk at this point
		2. Mitigations: No mitigation needed at this point
	2. Disaster Recovery
		1. Risks: Unknown Unknowns, Outside dependencies on Exchange
		2. Mitigations: Discovery and implementation work already started, lower environment dry runs, targeting production failover test for October instead of contracted December date to allow for a buffer, engaging/aligning with teams outside Exchange
	3. Red Mythos
		1. Risks: High level of coupling -> high complexity -> big bang approach is the only path, large upgrades (often jumping many major versions)
		2. Mitigations: Sequestered team working on dedicated and isolated branch and environment, heavy AI use for remediation AND testing/validation, all hands on-deck plan for merging and testing
	4. Autonomous Teams / Break the Monolith
		1. Risks: Impact from Atlas, DR and Red Mythos Projects, Hiring (especially in India), High level of coupling throughout the stack (including shared databases), Unknown unknowns
		2. Mitigations: Fast-tracking DR and Red Mythos projects, India compensation flexibility, giving teams flexibility on how to reach "independent deployments"
	5. COMMON: a common risk throughout is the competing imperial priorities, both as it relates to resources, and the fact that much or all of this work somewhat interferes with each other since it's on the same monolithic code base. The mitigation for this is last focus for Q3 and Q4 - see next slide
9. Q3 - Q4 Technical Laser Focus
	1. My very strict direction to the teams for Q3 and Q4:
		1. Stay true to the current capacity split: 75% of effort should be spent on technical items
		2. Out of the 75% technical work it should all roll up to one of the following three buckets. Anything else needs to be questioned/scrutinized:
			1. Red Mythos
			2. Disaster Recovery
			3. Autonomous Teams / Breaking the Monolith
