## Things to Ask for Help With
- Opinion on how to approach tech vs commercial work
	- Predetermined / sequestered capacity pie chart vs. Product Owns Prioritization
- Opinion on Product / Backlog / Roadmap tool chain
	- Jira Product Discovery
	- Jira Plans
	- Aha
	- Jira Align

## Things to proactively give to Kickdrum
1. High level technical roadmap
	1. Breaking the monolith
	2. DR
	3. Replace the EventBus
	4. Database assessment

## Prep for Thursday 1-1 With Kickdrum
- Org change
	- 
- Monolith
	- The plan for breaking it
- AI SDLC
- MongoDB / Atlas
- Data expertise on the teams
- ...
### Agenda from Kickdrum ###
- **Architectural Strategy & Platform Evolution:** 
  ***Sharing your initial observations on the current platform architecture and your thoughts on how to best balance new technical initiatives with managing existing technical debt.***
	- Observations
		- Monolith
			- Deployment
			- Testing suite
		- Databases
			- Do we need all this data
			- Do we need full snapshots of the document with each change
			- Is it stored in the right product given the write/read patterns
			- ...
		- EventBus
	- Suggested Approach - Spend 2-3 quarters mainly focused on getting in a better technical spot (Autonomous teams, broken monolith, DB risks reduced)
		- Get to Autonomous Teams at all cost
			- Definite team domain boundaries
			- Align teams with Team "template" (Jira Project, Slack channels, repo tags, Confluence page etc.)
			- Ensure the team domain is independently deployable - e.g. move the components into dedicated GH repos, build out GH Actions
		- Ensure we meed the EOY DR target
		- "1st pass" at cleaning up DBs
			- Inventory / Assessment
			- High impact / low-medium effort changes
- SDLC & Developer Experience: 
  *Your perspective on the current delivery processes, testing practices, and the most promising opportunities to enhance developer productivity (e.g., through Project Jarvis and new tooling).*
	- Monolithic deployment -> Autonomous teams
	- Monolithic code base -> smaller code repos, in GitHub, with AI Native SDLC
		- will also alleviate many of the problems with the huge AI testing suite
	- Seed each team with baseline AI-enabled SDLC workflow
- Cross-Functional Collaboration: 
  *Observations on how the Pod and Platform teams interact today, and ideas for optimizing alignment and balancing maintenance (KTLO) with new innovation.*
	- Product / Engineering Relationship
	- Clarity on Priorities
		- Top down priorities need to be aligned between stakeholder / product and engineering arms
	- Reporting / visibility into the work
- Team Dynamics & Knowledge Sharing: 
  *Recognizing the key contributors who are driving success within the engineering organization and discussing areas where the team might benefit from additional support or cross-training.*
	- Daniel - wealth of knowledge, lots of history, knows the business and systems really well
	- Aaron - AI and DevOps SME, a huge level up for the org
	- Ramesh - Key trusted lieutenant for GHXi
	- Michael - Room to grow
	- Happiest Minds knowledge silos
	- New Principal Engineer, Data Architecture & Engineering
- High-Impact Opportunities: 
  *From your relatively fresh vantage point, identifying the top one or two adjustments to process, team structure, or strategy that could most effectively accelerate the team's goals.*
	1. 12 teams, dedicated EM, dedicated PO
	2. Autonomous Teams ()
	3. DR
	4. Databases
	5. 