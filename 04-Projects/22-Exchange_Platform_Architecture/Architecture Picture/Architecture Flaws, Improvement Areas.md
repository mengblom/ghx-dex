## Monolithic Architecture Impact on SDLC

### The Vicious Cycle

**Root Cause:** Monolithic codebase with tight coupling and extreme dependencies (especially shared databases) forces monolithic deployment where any change deploys the entire application

**Initial Impact:** 
- Massive blast radius and enormous test surface area make trusted automated coverage extremely difficult
- Merge conflicts, hidden dependencies, and steep learning curve create uncertainty about change impacts
- Every deployment affects the entire system, even for small changes

**Defensive Response:** 
- Uncertainty and high rollback risk force extended, careful testing cycles
- Reliance on manual processes since automated coverage is insufficient
- High consequences of failure—rolling back or fixing a monolithic deployment is significantly more difficult than fixing a smaller, isolated service

**The Vicious Cycle:**
1. Long testing cycles → only monthly releases feasible
2. Monthly releases → changes batch into larger deployments
3. Larger deployments → "justify" more extensive testing
4. More extensive testing → longer cycles

**Compounding Effects:**
- Each iteration increases risk awareness, deployment size, and testing requirements
- Team trapped in defensive posture, unable to accelerate without accepting unacceptable risk

### Database Dependencies as Root Cause

**Critical Issue:** Many system components share the same databases, creating extreme coupling
- Forces monolithic deployment patterns
- Creates hidden dependencies that are difficult to track
- Makes it impossible to deploy services independently

**Need to Remove Bad Dependencies (from Audit DB incident):**
- SFTP endpoints should not go down because Audit DB is unresponsive
- Core document processing should not go down because Audit DB is unresponsive
- Question patterns like: Why store 188M ActivityFlow documents/day in MongoDB only to delete and archive to S3 3 days later when we have rehydration mechanisms?

## Operational Issues

- We are batch processing events
	- Examples:
		- Data Poller
	- We are allowing ebbs and flows, surges etc., to propagate through the system
- We don't have good enough log monitoring and alerting
	- Example: 
		- [[BROKEN-606] Exchange - 810 Scheduled Delivery – Batch Failures - Jira](https://prd.workflow.ghx.com/browse/BROKEN-606) 
		- A whole batch of (1000s) invoices failed.
		- We didn't know about it until ***more*** than 7 days later. And only after it was raised by the customer. To make matters worse, the channel for this is through Product
		- Our logs (Graylog) are only retained for 7 days
- Health checks at the service level need improvement

## Crisis as Opportunity

**Philosophy:** "Never let a crisis go to waste"
- When incidents happen, there will be understanding for making large architecture changes
- Need to push for deeper architectural improvements rather than temporary band-aid solutions
- Avoid getting complacent after migrations (e.g., "go to Atlas, shard the crap out of databases, then get complacent")
- Need to improve "headroom" significantly, not just enough to get through immediate problems
- Use crises as openings to move beyond "duct tape and bubblegum" mindset

## Team Friction Points and "Taxes"

*Added: 2026-04-17 from April 2026 automation planning*

**Key Areas Creating Development Friction:**

### Monolith-Related Friction
- Large codebase with extensive coupling makes changes risky
- Difficult to reason about impact of changes
- Slow build and deployment cycles
- High cognitive load for developers
- Changes in one area can break seemingly unrelated features

### Testing Challenges
- **Tandoori** - Legacy testing framework that's difficult to work with
- Steep learning curve for writing and maintaining tests
- Slow test execution times
- Flaky tests reduce confidence
- Manual testing requirements due to insufficient automated coverage

### Homegrown Components
- Custom-built tools and frameworks require specialized knowledge
- Lack of community support and documentation
- Maintenance burden on the team
- Onboarding friction for new engineers
- "Not invented here" syndrome preventing adoption of standard solutions

### Implications
These friction points:
- Slow down feature delivery
- Increase cognitive load on developers
- Create barriers to autonomous team operation
- Make it harder to attract and retain engineers who expect modern tooling
- Compound the monolith deployment challenges described above

**Strategic Direction:** Systematically reduce these "taxes" through architecture improvements, tooling modernization, and selective adoption of industry-standard solutions over homegrown alternatives.