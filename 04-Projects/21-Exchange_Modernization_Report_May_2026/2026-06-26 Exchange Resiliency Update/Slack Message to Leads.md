# Slack Message - Exchange Resiliency Story

---

**To:** Daniel, Mike, Ramesh, Aaron [+ others as appropriate]

---

Team - need your help with something.

Back in 2024 we had a series of disruptive outages and incidents in Exchange. Following those incidents, there was significant work done to analyze what went wrong - root cause analysis, identifying architectural weaknesses, documenting tech debt that was contributing to instability. This all got documented in several decks that were presented to the board and leadership:

- The Feb 2025 board deck broke down incident root causes by category (design limitations, synchronous dependencies, lack of domain separation, etc.) and showed 13+ incidents across 4 months
- The Exchange Plan deck laid out the technical work needed to address those root causes
- The 2026 Product Health Portfolio identified 6 key resiliency priorities (DB migration to managed services, DR drills, vulnerability SLAs, EOL tech elimination, industry continuity solution, increase modularity)

Since then, we've actually made a lot of progress. We've completed or partially completed work against many of those items. Database stabilization work. Decoupling efforts. Release management improvements. DR capabilities. MongoDB Atlas migration. And more.

The problem? Nobody has told this story. The narrative in the business is still "Exchange has endless tech debt and isn't making progress" and "why plan new features when engineering never has time to build them?" That perception is hurting us.

I'm putting together a presentation for CJ and broader leadership next week to change this narrative - to show the actual progress we've made with data and examples. To do that I need to catalog the work we've completed over the last ~18 months that:
- Maps to the root causes and improvement areas documented in those Feb 2025 board decks
- Has improved resiliency (stability, fewer incidents, better scalability, decoupling work, etc.)
- Has improved engineering efficiency (team autonomy, CI/CD, deployment independence, DORA metrics)
- Addressed security/vulnerabilities/EOL tech

I've started a doc here with some initial items Daniel and Mike helped me brainstorm:
[Exchange Resiliency Completed.docx](https://ghx365-my.sharepoint.com/:w:/r/personal/mengblom_ghx_com/Documents/Documents/Projects/Exchange%20Resiliency/Exchange%20Resiliency%20Completed.docx?d=w0c1816a3b45f4d8b98641b37592b8f8a&csf=1&web=1&e=PestU9)

The doc has instructions at the top explaining the format (just a simple table - What/When/Impact/Root Cause/Jira). Keep it brief, we're not writing comprehensive docs here, just cataloging what's been done.

Reference decks (these show what we originally identified as problems):
- [2025.02 Exchange Board Deck](https://ghx365-my.sharepoint.com/:b:/r/personal/mengblom_ghx_com/Documents/Documents/Projects/Exchange%20Resiliency/2025.02%20Exchange_Board%20Deck_Feb.2025.pdf?csf=1&web=1&e=wgKzKQ)
- [Exchange_Plan_Latest.pptx](https://ghx365-my.sharepoint.com/:p:/r/personal/mengblom_ghx_com/Documents/Documents/Projects/Exchange%20Resiliency/Exchange_Plan_Latest.pptx?d=wcb18e3e1412f4dbbbd3750ebb1e85ea5&csf=1&web=1&e=QdtLLA)
- [2026 Product Health Portfolio](https://ghx365-my.sharepoint.com/:p:/r/personal/mengblom_ghx_com/Documents/Documents/Projects/Exchange%20Resiliency/2026%20Product%20Health%20Portfolio%20-%20Copy.pptx?d=w37fa829cb4154a5689578a1030a2360c&csf=1&web=1&e=4oQOf0) (slides 41-49)

I'm building this presentation next week. Don't let this derail anything critical you're working on - but take some time to review the material and add completed/partially completed work that comes to mind. Pull in whoever from your teams knows the details.

Let me know if questions.
