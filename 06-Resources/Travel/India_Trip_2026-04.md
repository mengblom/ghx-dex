
Dates: 2026-04-13 - 2026-04-21
# Recap#
- Met with the teams
	- Managed Services
	- IPA
	- Visibility
	- Mapping
- Introduced Aaron, spent time introducing AI enablement strategy ([link](https://lucid.app/lucidchart/0590887d-6067-4229-8636-951cd84de215/edit?viewport_loc=-552%2C-7%2C1620%2C829%2CcD.P81UiFREU&invitationId=inv_fdb82d1b-86d1-4c76-b1b2-eacfbee7330e))
- Met with TA team
- Met with Swastik
- Interviewed Staff candidate for ICS team
- Met with Rammi and Managed Services
- Met with Happiest Minds delivery leadership (Sujith Sukumaran, Vignesh Viswanathan)
	- to address concerns about collaboration and capacity/velocity on the Visibility team
# Takeaways #
- AI excitement and readiness better than expected
	- Mapping team has created 2 impressive POCs for new mapping tool - many months of manual work equivalent in < 1 month
- Teams are leaning into becoming autonomous
	- Visibility team has a clear plan, including their areas of ownership, target repo structure - they are actively breaking from the monolith
- Central functions are surfacing as bottlenecks
	- Infrastructure (Github migrations)
		- This is in turn holding back AI adoption, since bitbucket MCPs are poor
	- UI Automated testing
		- Teams feel "obligated" to maintain a very high automated test coverage
- The salary bands continue to surface as an issue with hiring. Feedback is that we are indeed lowering standards in order to fill roles
- There is friction with Happiest Minds contractors. 
# Action Items #
- AI
	- Pivot the AI Native SDLC strategy a bit - broader rollout as opposed to incubate in 1-2 teams
- Need to shift team culture towards full ownership
	- Need to facilitate / accelerate teams need to take ownership of their own repos (including migrations), deployment pipelines (Github Actions)
	- Teams need to be given ownership of the quality of what they release - the team decides how they achieve that, what tests are needed etc.
	- Discuss with Automation leads how we manage the "shared function" of UI Test Automation going forward
	- Need to continue to talk to teams about taking ownership of their data and data stores. This does not receive enough attention right now, despite our data layer arguably being our biggest problem area.
- Need to really doubleclick on the current roadmap for Managed Services
	- The concept of using UIPath automations (i.e. UI bots) on top of our own applications, as opposed to creating API integrations, seems highly inefficient, brittle, and non-scalable.
- 