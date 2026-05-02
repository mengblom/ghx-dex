---
tags:
  - executive-update
  - correspondence
  - India-trip
  - Aaron-Srivastava
  - AI-adoption
  - team-autonomy
  - Atlas
content_type: email
destination_category: 60-69 Archive
kb_insights: false
date: 2026-04-21
---

## Executive Update
**April 21, 2026 | For: CJ**

Hello CJ,

### TLDR

- India trip (April 13-21) was productive - the goal was a couple of things:
	- Generally spend time with Ramesh, the teams.
	- Check in on progress towards team autonomy and break-away-from-the-monolith work, make sure the vision is clear.
	- Jumpstart the journey towards a complete AI enabled SDLC - Aaron Srivastava joined me with short notice. 
- Takeaways: 
	- Teams are eager for AI in their workflow, and embracing autonomy faster than anticipated. **We are pivoting from the original approach of single-team AI incubator to broader rollout across the org immediately.** 
	- Some challenges exist; central functions (infrastructure/test automation) are emerging as bottlenecks
	- Hiring constraints; salary bands and TA bandwidth 
- Focus ahead is onboard new hires and support newly forming teams, accelerate shift to autonomous teams and monolith breakup, drive architecture improvements on a broad front (becoming possible with multiple new EMs in seat). **Atlas migrations and DR** are top of mind projects.

### Looking back / India Trip Recap

Met with Managed Services, IPA, Visibility, and Mapping teams to generally spend more time together, build a rapport, check in on challenges etc.

Also met with TA team on hiring challenges; salary bands are limiting access to quality candidates, many are screened out based on compensation. There is a concern that coupled with hiring pressure, we will end up compromising to fill roles. 

Met with Happiest Minds delivery leadership on concerns about both collaboration and velocity based on feedback from our teams. Made expectations clear to HM - when they are playing a staff augmentation role, they report to our EM, attend all sprint rituals, and generally need to function like our FTEs. 

Introduced Aaron and socialized AI strategy. Aaron held multiple sessions on vision/end state, and incremental approach to get there. It was very well received by the teams - there is definitely interest and excitement.

Teams are hitting delivery goals while at the same time making good progress towards autonomy, and are leaning in to AI. The new mapping team built a POC UI equivalent to many months of work in < 1 month using Claude Code. The Visibility team is really moving towards autonomy and breaking away from the monolith with a clear and detailed plan. They are also achieving 80% unit test coverage with AI. A challenge emerging in this area are centralized functions bottlenecking the progress; DevOps (Github migrations) and UI test automation.

Recent sprints strong - see [Exchange update deck](https://ghx365-my.sharepoint.com/:p:/r/personal/cnielsen_ghx_com/Documents/2-Areas/Exchange/Updates/Exchange%20Update%20WIP.pptx?d=wb08c76ab92e247ef895e2a9685c86ecd&csf=1&web=1&e=c0RTd8&nav=eyJzSWQiOjIxNDc0ODMxNjAsImNJZCI6MH0) for velocity growth, RegCenter 2.0, Customer Visibility milestone. Audit DB EU migrated to Atlas successfully.

### Current Focus / Coming Up

**Architecture** - have reached critical mass of technical thought leadership/architects (Directors, EMs, senior ICs) - starting ongoing architecture discussions around backlog of architecture & systemic weaknesses, problems & opportunities. The intent is to steer teams beyond reactive fixes to ongoing incremental improvements - broad and deep. 

**AI Native SDLC** beyond individual coding assistance - Pivoting to broader rollout vs. single-team incubator based on team readiness signal. Aaron taking lead and has gotten far on a strategy and approach.

**Team autonomy** - Driving full-stack ownership including deployment pipelines, quality decisions, repo migrations, data architecture. Teams are excited but need continued encouragement. Central functions (DevOps, test automation) are becoming bottlenecks in some cases - solvable with giving agency and "permission to act". 

**Hiring & onboarding** - Still 20+ open roles. Multiple new managers/ICs joining. Need to make sure they are integrated and become productive quickly.

**Other**
- Exchange Incident Games (DR test) May 4-8
- Audit DB US migration scheduled for 4/25. **Critical milestone** - high stakes given incident history.

### What is on my mind

**Database architecture** - Stability is an ongoing concern, as further highlighted by the EventBus DB incident on Friday. We need to backtrack from the "MongoDB for everything" approach. It is our current **Achilles heel** for stability and scalability of the platform. And it is expensive. 

**Ways of working** - We need to get past the sense that it is hard to know what the teams are working on and accomplishing. We need clearer, higher level, roadmaps, with automated progress rollup, categorization of work etc. Need an Initiatives layer above Epics in Jira, improving Aha-Jira integration for better roadmap visibility. Need to work with Product on this - maybe put in place a small working group.

**Hiring in India** - Salary bands limiting quality of candidates. TA bandwidth.

**Central functions as bottlenecks** - DevOps and test automation slowing down the shift to team autonomy. Need to navigate centralized control and alignment vs. speed.

**Happiest Minds** - Collaboration and knowledge-sharing concerns. Concerned about misaligned incentives and implications for 6-12 month knowledge transfer.

**Planning overhead** - Too much energy on decks, status updates, city maps, "tech debt" inventory, dissecting misses, long-range planning, vs. execution and problem solving.
