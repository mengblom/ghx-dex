
### Agenda from Kickdrum ###
> - **Architectural Strategy & Platform Evolution:** 
>   *Sharing your initial observations on the current platform architecture and your thoughts on how to best balance new technical initiatives with managing existing technical debt.*
> 
> - **SDLC & Developer Experience:** 
>   *Your perspective on the current delivery processes, testing practices, and the most promising opportunities to enhance developer productivity (e.g., through Project Jarvis and new tooling).*
> 
> - **Cross-Functional Collaboration:** 
>   *Observations on how the Pod and Platform teams interact today, and ideas for optimizing alignment and balancing maintenance (KTLO) with new innovation.*
> 
> - **Team Dynamics & Knowledge Sharing:** 
>   *Recognizing the key contributors who are driving success within the engineering organization and discussing areas where the team might benefit from additional support or cross-training.*
> 
> **- High-Impact Opportunities:** 
>   *From your relatively fresh vantage point, identifying the top one or two adjustments to process, team structure, or strategy that could most effectively accelerate the team's goals.*
### Areas to make sure to cover ### 
- Org change
	- 
- Monolith
	- The plan for breaking it
- AI SDLC
- MongoDB / Atlas
- Data expertise on the teams
- ...

### Agenda from Kickdrum - My Topics Added ###
- **Architectural Strategy & Platform Evolution:** 
  ***Sharing your initial observations on the current platform architecture and your thoughts on how to best balance new technical initiatives with managing existing technical debt.***
	- Observations
		- Monolith is THE MAIN problem for us
			- Monthly deployments (2-3 weeks working through the UI testing suite)
			- Upside down testing pyramid / UI Testing suite
			- Everything is a project
			- DevOps / Monolithic DEPLOYMENT
			- ...
		- Databases
			- Do we need all this data
			- Do we need full snapshots of the document with each change
			- Is it stored in the right product given the write/read patterns
			- ...
		- Homegrown solutions where commodity products exists:
			- EventBus
			- Identity Provider
			- Observability solution (i.e. Audit DB)
			- CoreUI
			- ICS ("side project"... is this really neccesary?)
	- Suggested Approach
		1. Spend 2-3 quarters mainly focused on getting in a better technical spot (Autonomous teams, broken monolith, DR solution 1.0, DB risks reduced)
			- Get to Autonomous Teams at all cost
				- Definite team domain boundaries
				- Align teams with Team "template" (Jira Project, Slack channels, repo tags, Confluence page etc.)
				- Ensure the team domain is independently deployable - e.g. move the components into dedicated GH repos, build out GH Actions
				- Seed each team with baseline AI-enabled SDLC workflow
			- Ensure we meed the EOY DR target
			- "1st pass" at cleaning up DBs
				- Inventory / Assessment
				- High impact / low-medium effort changes
		2. Now each team can independently start shifting capacity back to commercial - the commercial / tech blend will be different for each team
			1. Tech / Resiliency backlog

- **SDLC & Developer Experience:** 
  ***Your perspective on the current delivery processes, testing practices, and the most promising opportunities to enhance developer productivity (e.g., through Project Jarvis and new tooling).***
	- Monolithic deployment -> Autonomous teams
	- Monolithic code base -> smaller code repos, in GitHub, with AI Native SDLC
		- will also alleviate many of the problems with the huge AI testing suite
	- Seed each team with baseline AI-enabled SDLC workflow, set them up to evolve according to local needs (context, skills, plugins etc.)

- **Cross-Functional Collaboration:** 
  ***Observations on how the Pod and Platform teams interact today, and ideas for optimizing alignment and balancing maintenance (KTLO) with new innovation.***
	- Product / Engineering Relationship
		- Product should be less Project Management - More Product Management
	- Multiple sources of work
		- Example: CX team made board level commitments without talking to PO or Engineering
	- Clarity on Priorities
		- Top down priorities need to be aligned between stakeholder / product and engineering arms
	- Reporting / visibility into the work

- **Team Dynamics & Knowledge Sharing:** 
  ***Recognizing the key contributors who are driving success within the engineering organization and discussing areas where the team might benefit from additional support or cross-training.***
	- Daniel - wealth of knowledge, lots of history, knows the business and systems really well
	- Aaron - AI and DevOps SME, a huge level up for the org
	- Ramesh - Key trusted lieutenant for GHXi
	- Michael - Great technical manager, room to grow
	- A couple of new Engineering Managers, VERY promising
		- Adam Gordon
		- Kooper Frahm
	- Happiest Minds knowledge silos
		- Need KT strategy
	- New Principal Engineer, Data Architecture & Engineering - to be hired

- **High-Impact Opportunities:** 
  ***From your relatively fresh vantage point, identifying the top one or two adjustments to process, team structure, or strategy that could most effectively accelerate the team's goals.***
	1. 12 teams, dedicated EM, dedicated PO
	2. Contractors -> FTEs
	3. Autonomous Teams ()
	4. Monolith
	
	5. DR
	6. Databases
	7. 