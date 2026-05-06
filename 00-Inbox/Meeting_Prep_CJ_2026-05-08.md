# Meeting Prep: CJ - Resiliency Spike & Capacity Planning

**Date:** Thursday, 2026-05-08
**Meeting Context:** Follow-up to Technical Priorities Review (2026-05-01)

---

## Three Deliverables

1. **Key work remaining in "resiliency spike"** - Define 3-5 specific deliverables with completion criteria (focus on "breaking the monolith")
2. **Capacity pie chart evolution** - Q2 baseline → Q3 → Q4 projections
3. **Productivity gains report** - 4-month tenure, data-backed, concise
4. Org chart

---

## Reference Documents

- **Previous meeting:** [[00-Inbox/Meetings/2026-05-01/Technical_Priorities_Review]]
- **2026 Tech Org Priorities.pptx** (page 2 - Exchange priorities)
- **2026 Product Health Portfolio.pptx** (integrated roadmap)
- **P&T Capacity Pie Chart - 2026 Q2.pptx** (baseline)
- **Resiliency Future Plan** (Gen3 scope boundary)

---

## Ask from Team ##
* What has been "decoupled" over the last 3-6 months?
* The "template" for breaking off the monolith
* Health score??

## Notes

## Agenda / Slides outline: ##
1. The ask from CJ for this meeting:
	1. Commentary / State of the Union on Productivity Improvements
	2. Update on Exchange Resiliency Work
	3. Capacity Planning Forecast
2. Productivity Assessment
	1. There are positives signs in data
		1. Stories completed (Jan, Feb, Mar): 207 - 271 - 386 (stories)
		2. Lead time to change (Jan, Feb, Mar):  30 - 33 - 8 (days)
		3. Cycle time  (Jan, Feb, Mar): 44 - 44 - 23 (days)
		4. Preview of Exchange Health Score?
		5. Latest releases have gone well
		6. AI library
		7. There are some positives, but the reality is that as long as we are operating in a monolithic codebase, deployment footprint, and team structure the improvements will be incremental as opposed to transformational 
	2. Challenges
		1. The monolith (we'll get back to that)
		2. The org, which was also "monolithic" - we are solving that
		3. Culture
			1. Fear of releasing
			2. Large Product Launches
		4. Visibility / reporting problem
			1. Roadmaps at the epic level etc.
		5. Competing priorities, reporting asks, "show your progress"
			1. Large opportunity cost at the leadership level - you need hands-on leadership through change
3. In summary, we are making incremental productivity improvements
4. We are also tracking against the other resiliency priorities (ties this to the priorities in [2026 Tech Org Priorities.pptx](https://ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/Documents/2026/2026%20Tech%20Org%20Priorities.pptx?d=w3d38032c08714d5eb49a0b00d8ecc1ae&csf=1&web=1&e=jwqa7k))
	1. Atlast migration
	2. DR test
	3. Red Mythos
	4. ICS
5. Now on to the monolith
	1. The problem with the monolith
		1. "The monolith" is both a technical and organizational problem
		2. The vicious cycle
		3. The bottleneck is the testing / risk / blast radius
			1. Which will get even worse with AI
		4. At that size, everything needs to be a "project"
		5. The cost (get slides from [Exchange - Building Autonomous Teams.pptx](https://ghx365-my.sharepoint.com/:p:/r/personal/mengblom_ghx_com/Documents/Documents/Projects/Exchange%20Org%20Changes%2025-26/Exchange%20-%20Building%20Autonomous%20Teams.pptx?d=w1fd29fbd375547599f028fe5c73faeca&csf=1&web=1&e=1PIff2))
		6. The monolith is also an organizational problem
			1. Deep changes requires hands-on leadership
			2. Also, it is not how we want to work in the long run, post monolith
	2. The goal / vision
		1. Autonomous teams
			1. The exchange is too big to work on as 1 team, as 1 system
			2. This includes current resiliency work, and future roadmap work
			3. The answer is to empower smaller teams
			4. Things that previously needed to be a project
		2. Reverse Conway Maneuver
		3. Decoupled system
	3. The progress so far
		1. The new org
			1. We are going from 1 director with 3 EMs for 80+ engineers
			2. to 4 directors, 12 EMs (each leading 1 small team)
		2. Hiring
			1. Key roles
			2. EMs
			3. Show org chart here
		3. Technical progress
			1. AI-Native SDLC
				1. Hired Aaron
				2. This transformation (new teams, limited scope, breaking from the Monolith) is a golden opportunity to make sure AI is natively part of the SDLC
		4. Signs of cultural progress
			1. Teams breaking off components
			2. Teams wanting to take over testing responsibilities 
			3. Incremental deliveries - Exchange Managed Services (EMS) delivery of Manages Services Portal - 
				1. request was quarterly commitments to 2027 Q2
				2. agreement
	4. What is happening right now
		1. Each team is defining: 
			- **Your domain** - What's in scope, what's out, where are the boundaries fuzzy?
			- **Coupling points** - How are you tied to the monolith or other services? Shared repos, direct dependencies, shared databases?
			- **Deployment blockers** - What prevents you from deploying independently today?
		2. Template for breaking pieces off the monolith
			1. Move to Github repo
			2. Stand up your
		3. AI-Native SDLC
		4. Teams actually breaking from the monolith
		5. Autonomous teams
			1. Decisions (testing etc.)
			2. Freedom to move forward
		6. Architecture backlog discussions
	5. "End" of resiliency work? / When are we out of the woods?
		1. Must Haves (we will not be stable, or cannot execute properly without these):
			1. Autonomous teams (we just talked about this extensively)
				1. that own and deploy their components independently
				2. own their own application-near infra
				3. own their own deployment pipelines
				4. are sprinting independently
			2. Data stored in the correct "products"
				1. Scalability
				2. Cost
				3. HA / DR is literally a setting
		2. Negotiables (will continue to hold us back, or said differently, I'd be shocked if Veritas / Kickdrum doesn't comment on this)
			1. Event / Messaging system
			2. Infinitely scalable queue/event subscribers (lambdas, etc.)
			3. Cloud native infra
				1. HA / DR is literally a setting
			4. Observability
6. The future
	1. Steve's vision for 100% self serve

