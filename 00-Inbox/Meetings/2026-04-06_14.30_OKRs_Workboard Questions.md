---
date: 2026-04-06
participants:
  - Mårten Engblom
companies: 
  - Untitled
tags:
  - meeting
meeting_type: general
source: granola
granola_id: b2fd8a18-cd05-4b86-8e68-d370b40a4a14
---

# Untitled Meeting

### OKR Philosophy & Structure

- Goal: align all communication and work to 3 business outcomes (deduced, not handed down)

- Increase revenue
- Reduce costs
- Reduce risk
- Current OKR rollup is broken — groups write “cross-functional OKRs” and ping others, rather than each team owning their portion
- Engineering work types (Roger’s framework): maintenance, tech debt, new features

- Every story/epic should map to both a business outcome and a work type
- Two pie charts as the reporting output
- OKRs will sit at the pod level only — no individual-level OKRs for now

- Rollup to engineering manager level is aspirational but not working yet
- Hiring OKR is appropriate to include (e.g., “15 of 11 roles hired” format worked well last quarter)

### Exchange Resiliency OKRs

- 5 key areas under exchange resiliency — these are full-year KRs, not Q1-only
- Observability:

- Target: define and track 3–5 SLOs this quarter, get them on a status page
- Focus at API/service level only — not internal metrics like query times
- Start small: automate heartbeat reporting, wrap IO engine or notification engine
- Mental model: Obsidian-style status page expanded across exchange services
- “Reduce mean time to detect” KR to be removed — too premature
- Distinct deployments: straightforward KR, no concerns
- Database migration: straightforward KR, no concerns
- Disaster recovery:

- RTO/RPO gap closure KR should be rewritten as an outcome: “reduce recovery time from 13hrs to Xhr”
- Realistic target: Q3 at earliest (databases not yet working correctly)
- DR test: run a lightweight failover test in lower environment — target 4–8 hrs total effort

- Happiest Minds team can run it; no hard dependency on new FTE hire
- Ramesh to reach out to Jenna to scope

### Cybersecurity OKRs

- Artifact repository (JFrog):

- Problem: supply chain attack risk from unscanned open-source packages; also, internal libraries currently copied between repos manually
- JFrog instance exists but barely used
- Better KR: reduce number of repos not pulling from JFrog artifact repository to zero (with quarterly targets)
- Ownership: infrastructure owns the repo, works with security on scanning rules
- Container registry:

- Same concept — zero containers outside of registry
- Currently using ECS; XDP registry exists but maturity unclear
- Likely already compliant — needs a check before writing a KR
- Offshore compliance: removed from Q2 scope

- Can’t comply given current architecture without major re-platforming
- To be raised separately with Tina; other pods (Marketplace, Analysis) have handled it via data anonymization

### Delivery Efficiency OKRs (replacing “Jarvis” framing)

- Reframe as a standing “improve delivery efficiency” objective — not AI-specific

- Applies to every pod area (credentialing, analysis, marketplace, etc.)
- Core KRs: lead time to change + deployment frequency (DORA metrics)
- PR age as a potential third KR — reduce PRs open >30 days

- KPMD dashboard exists (built by Mike Mitchell + India team) but currently tracks time-to-approve, not time-to-deploy
- Data collection may need adjustment before this KR is usable
- Key constraint: deployment frequency is bottlenecked by monthly monolith release cycle, not team throughput

- “Distinct deployments” KR elsewhere already addresses this
- AI productivity measurement: pushing back on AI-specific metrics; normal delivery metrics are sufficient

### Items Deprioritized or Deferred

- Complex order automation: no known engineering backlog; Josh’s team onboarding pilot customers away from engineering

- Watch for reactive defects; Laura’s team may already have this covered
- Reducing customer friction / defect count: framed as a product KR, not an engineering KR

- MTTR here = customer resolution time, not system recovery time
- “Offshore compliance” KR: dropped (see above)

### WorkBoard & OKR Tooling

- WorkBoard is the mandated reporting tool but poorly organized — pod-level pages hard to find
- Automation pod page exists but permissions/visibility issues for Mårten
- Jacqueline and Jamie are the WorkBoard admins for permissions
- Interim plan: enter OKRs on personal page; admins consolidate into pod-level scorecard

### Next Steps

- Mårten

- Sync with Daniel on observability OKR — what 3–5 SLOs are feasible this quarter
- Check with Daniel + Ramesh on JFrog artifact repository usage across teams
- Check container registry status — likely already in ECS, may not need a KR
- Check in on complex order automation — confirm no major engineering backlog
- Ping Daniel re: monthly cyber sync — let Daniel attend and escalate as needed
- Draft OKRs into WorkBoard (personal page as interim); connect with Jacqueline/Jamie on pod-level permissions
- Other party (name unclear — likely Mårten’s manager/CTO)

- Rewrite RTO/RPO KR as outcome-based (“reduce recovery time from 13hrs to Xhr”)
- Edit Jarvis section → rename to “improve delivery efficiency”; remove AI-specific KRs
- Fix cybersecurity OKR wording for consistency across pods
- Move PDF content to Confluence page for collaborative editing
- Have Ramesh reach out to Jenna to scope DR failover test in lower environment
- Ping WorkBoard admins (Jacqueline/Jamie) to locate/fix automation pod page
- Align with Eric on AI/engineering training KRs separately

Chat with meeting transcript: https://notes.granola.ai/t/a72ccf59-79e5-4f6c-9de6-fb8395c698e7

