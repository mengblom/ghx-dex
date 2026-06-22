1. The overarching objective of this meeting is to tell the narrative, the story for Exchange. We (including Daniel and the team before I started) have indeed made a lot of progress and improvements, but unfortunately nobody has been telling the story.
2. Agenda
	1. Progress with "resiliency work" we originally set out to do:
		1. Review work accomplished over the last 1-2 years to improve resiliency, both generally, but also by tying it back to the plan and the list of incidents and the root causes originally identified in the deck: 
			1. '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange_Plan_Latest.pptx' - i.e. which things in that deck can we say we have done, or made progress towards
		2. A draft list of work completed has been started here: '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange Resiliency Completed.docx' . These items needs a lot more detail - what was done, when, perhaps tied back to Jira items etc. Need to have Daniel, Mike and others help me with this.
	2. Provide an update against the 6 resiliency items identified in '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/2026 Tech Org Priorities - Copy.pptx':
		1. DB Migration to managed databases​ (addressed by the project to migrate MongoDB to Atlas and Elasticsearch to Elastic Cloud)
		2. DR Drills to test RTO (4 hrs) and RPO (2hrs) targets (addressed by the Disaster Recovery project driven by Daniel)
		3. All vulnerabilities addressed within SLA​ (addressed by project Red Mythos Exchange driven by Aaron)
		4. Eliminate EOL technologies in our stack (also addressed by project Red Mythos Exchange driven by Aaron)
		5. Industry Continuity Solution ​(addressed by the current solution developed by contractors, status update provided by Jena Milan in the "ICS Status" email thread on June 15)
		6. Increase Modularity i.e., continuebreaking the monolith - progress has been made here in multiple ways, as mentioned in this document:
			1. '/Users/mengblom/Library/CloudStorage/OneDrive-GlobalHealthcareExchange/Documents/Projects/Exchange Resiliency/Exchange Resiliency Completed.docx'
	3. Tell the story of the org transformation
		1. We have really transformed the Exchange organization into a world class engineering org
		2. Went from 1 director, 3 managers, 100-ish engineers to a modern engineering org with 4 directors, 12 managers, small teams of 3-5 engineers, all according to how top tier engineering organizations operate (FAANG, Spotify etc.)
			1. Need some examples here to show how those companies operate, for people not in the industry. Links to their blog posts etc., Henrik Knibergs videos about Spotify Engineering culture etc.
	4. What we are doing now, i.e. before shifting capacity in a significant way away from technical work towards commercial work
		1. Reverse Conway Maneuver
		2. Autonomous teams
		3. Continued decoupling
		4. P0 Database items
	5. What will be left to do, i.e. continued tech debt roadmap beyond
		1. Continued DB layer improvements
		2. Continued decoupling, towards a true SOA
		3. Get rid of the homegrown Event Bus, build a true Messaging / Event framework 
		4. Get rid of the homegrown IdP, replace with Auth0 implementation
		5. plus much more, needs to be outlined. Need help from my directors here...