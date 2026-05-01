1. Current State - The Vicious Cycle
	1. Monolithic Code Base
	2. Massive Blast Radius
	3. Extended Testing Cycles
	4. Monthly Releases Only
	5. Changes Batch Up
	6. Even More Testing Required
2. The Cost of our current state
	1. For Product, Stakeholders & Customers
	2. For Engineering Teams
3. The Vision
	1. How we operate
		1. We can release small parts of the system independently, with little or no coordination
		2. We can release very often with very low risk
	2. How the system looks
		1. Small encapsulated services
		2. Loosely coupled services
		3. Fault tolerant services - small blast radius
		4. No shared release dependenceies
	3. The teams???
		1. Can make decisions on their own and operate autonomously
			1. Built It
			2. Test It
			3. Deploy It
			4. Operate It
			5. Evolve It
		2. Autonomy, Mastery & Purpose
4. How we get there
	1. Reverse Conway maneuver 
		1. Form teams and give them ownership of parts of the system
	2. Team Goals
		1. Decouple
		2. Encapsulate (compute, storage, infra)
		3. Take ownership of their testing
		4. Take ownership of their releases
	3. Team Strategies
		1. Use the Strangler Pattern as opposed to big-bang rewrites
		2. Take ownership of your data
		3. Do not start with the hardest or most central part just because it is important.
			1. It is like untying a know
5. How do we measure progress
	1. Deployment frequency
	2. Lead time for changes

## Q2 2026 Implementation Focus

**Objective:** Making tangible progress on decoupling, clear ownership boundaries, and standalone deployments

### Team-Level Work (Next 2-3 weeks)
Each team must define:

1. **Your domain** 
   - What's in scope, what's out
   - Where are the boundaries fuzzy?
   - Document this clearly

2. **Coupling points**
   - How are you tied to the monolith or other services?
   - Shared repos
   - Direct dependencies  
   - Shared databases

3. **Deployment blockers**
   - What prevents you from deploying independently today?
   - What needs to change?

### Q2 End State Goal
Every team should have:
- Documented domain boundary
- Plan to break free of the monolith
- Clear direction and momentum (doesn't have to be done, but path must be clear)

### Ongoing Process
- Flag ambiguity or cross-team ownership questions as they come up
- Work through boundary issues together
- Focus on progress over perfection 



