# Disaster Recovery

**Status:** Active (Q2/Q3 2026)  
**Owner:** [[Daniel_Milburn]] (Senior Director)  
**Executive Sponsor:** Marten Engblom  
**Priority:** P0 - Contractual obligation (December 2026 deadline)

---

## Overview

Disaster Recovery project to achieve multi-region failover capability for Exchange platform. This is one of the "Big 3" technical priorities for Q3 2026, representing 75% of engineering technical capacity alongside Red Mythos and Autonomous Teams.

---

## Strategic Context

**Two Goals:**
1. **Contractual obligation to Cardinal:** Conduct DR failover in production (flip and stay) before end of 2026
2. **Operational confidence:** Feel good about our DR capabilities for real disaster scenarios

**Why This Matters:**
- Cardinal contractual requirement (December 2026 deadline)
- Real operational resilience - confidence we can recover quickly if needed
- RTO (Recovery Time Objective) target: Under 3 hours

**Q3 Planning Guidance:**
All technical work in Q3 should roll up to one of the Big 3:
1. Red Mythos / Vulnerabilities
2. **Disaster Recovery** ← This project
3. Autonomous Teams / Breaking the Monolith

---

## Key Context

### Ownership Model
- **Daniel Milburn:** Execution owner - drives the work, coordinates teams, tracks progress, runs DR steering committee
- **Marten Engblom:** Strategic direction - priority calls, resource allocation, leadership communication

### Recent Progress
- **May 2026 DR Test (lower environment):** 
  - Initial assessment: 4h 45m RTO
  - Revised: 7h+ (SSO challenges, database pre-work discovered post-test)
  - Positive: Atlas migration will eliminate ~2h of database restore time
  - Target: Under 3h RTO achievable

### Connection to Autonomous Teams
**Key Insight:** DR automation requirements overlap heavily with autonomous teams infrastructure:
- Teams need: Infrastructure as Code, automated deployment pipelines, independent deployments
- DR needs: Automated runbooks, infrastructure as code, rapid spin-up capabilities
- **Strategy:** "If we push pedal to metal on decoupling/autonomous teams, we get DR automation for free as part of that effort"

---

## Timeline

**October 2026:** Internal DR capability ready  
**December 2026:** Contractual deadline - production flip and stay with Cardinal  

**Key Dependency:** Atlas database migration removes ~2h from RTO

---

## Related Materials

### Meeting Notes
- [[00-Inbox/Meetings/2026-05-08/Road_to_Autonomy_Github_Migrations]] - Connection between DR, autonomous teams, and GitHub migrations
- Check Daniel's person page for meeting history: [[Daniel_Milburn]]

### Strategic Documents
- [[00-Inbox/Ideas/Q3_Roadmap_Planning_Communications]] - Q3 capacity allocation guidance (Big 3 framework)
- [[00-Inbox/2-Day_Focus_May_28-29]] - Current execution focus
- [[00-Inbox/Weekly_Synthesis_2026-05-24]] - Recent weekly context

### Related Projects
- [[04-Projects/Autonomous_Teams/]] - Overlapping infrastructure requirements
- [[04-Projects/Exchange Platform Architecture/]] - Broader architectural context

---

## Open Questions

- Database migration to Atlas timeline?
- How much DR work is truly independent vs. part of autonomous teams decoupling?
- Who owns runbook automation - DevOps? Teams themselves?

---

*Created: 2026-05-28*  
*Last Updated: 2026-05-28*
