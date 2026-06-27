1. Objective
	1. Tell the narrative, the story for Exchange. We (including Daniel and the team before I started) have indeed made a lot of progress and improvements, but unfortunately nobody has been telling the story.
	2. What are we doing now, what are the next immediate goals / DODs, what does the roadmap look like, and what are the expected benefits. See [[2026-06-26 CJ Feedback]]
		1. 
		2. 
2. Agenda
	1. Provide an update against the 6 resiliency items identified in '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/2026 Tech Org Priorities - Copy.pptx':
		1. DB Migration to managed databases​ (addressed by the project to migrate MongoDB to Atlas and Elasticsearch to Elastic Cloud)
		2. DR Drills to test RTO (4 hrs) and RPO (2hrs) targets (addressed by the Disaster Recovery project driven by Daniel)
		3. All vulnerabilities addressed within SLA​ (addressed by project Red Mythos Exchange driven by Aaron)
		4. Eliminate EOL technologies in our stack (also addressed by project Red Mythos Exchange driven by Aaron)
		5. Industry Continuity Solution ​(addressed by the current solution developed by contractors, status update provided by Jena Milan in the "ICS Status" email thread on June 15)
		6. Increase Modularity i.e., continue breaking the monolith - progress has been made here in multiple ways, as mentioned in this document:
			1. '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange Resiliency Completed.docx'
	2. Progress with "resiliency work" we originally set out to do:
		1. Review work accomplished over the last 1-2 years to improve resiliency, both generally, but also by tying it back to the plan, i.e. the resiliency items mentioned here: [[Manual Listing of Resiliency Items]] , and the list of incidents and the root causes originally identified in the deck: 
			1. '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange_Plan_Latest.pptx' - i.e. which things in that deck can we say we have done, or made progress towards
		2. A draft list of work completed has been started here: '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange Resiliency Completed.docx' . These need to be mapped to the items in [[Manual Listing of Resiliency Items]]
		3. "What we promised" vs "Work Complted"
	3. Tell the story of the org transformation
		1. We have really transformed the Exchange organization into a world class engineering org
		2. Went from 1 director, 3 managers, 100-ish engineers to a modern engineering org with 4 directors, 12 managers, small teams of 3-5 engineers, all according to how top tier engineering organizations operate (FAANG, Spotify etc.)
			1. Need some examples here to show how those companies operate, for people not in the industry. Links to their blog posts etc., Henrik Knibergs videos about Spotify Engineering culture etc.
	4. What we are doing now, i.e. before shifting capacity in a significant way away from technical work towards commercial work
		1. Reverse Conway Maneuver
			1. "*The teams we are forming are with the specific objective (and frankly only makes sense) if they can each operate independently*"
		2. Autonomous teams
			1. *Much of the resiliency work, decoupling etc., will be much easier, and happen more organically (Conway's Law) with decoupled autonomous teams*
		3. AI Native SDLC
		4. P0 Database items
		5. Continued decoupling
	5. The Details: Autonomous Teams
		1. Product Delivery Process Goals
			1. DOD
		2. The roadmap to get there
		3. Customer / Business Value/Goals
			1. Incident response time
			2. Delivery velocity
			3. Use examples from the last Incident
				1. Rollback 1 part of the system
				2. Could have remediated something like the IBR error message easily and without larger risk (see [Slack messages](https://ghx.slack.com/archives/C0BDE0E26AH/p1782494307691319))
	6. The Details: P0 Database Improvements.
	7. What will be left to do, i.e. continued tech debt roadmap beyond
		1. Continued DB layer improvements
		2. Continued decoupling, towards a true SOA
		3. Get rid of the homegrown Event Bus, build a true Messaging / Event framework 
		4. AI Native SDLC
		5. Get rid of the homegrown IdP, replace with Auth0 implementation
		6. plus much more, needs to be outlined. Need help from my directors here...