---
date: 2026-04-02
participants:
  - Mårten Engblom
companies: 
  - Untitled
tags:
  - meeting
meeting_type: general
source: granola
granola_id: a47d607c-b9e6-4e06-b487-28cc066ba666
---

# Untitled Meeting

### IO Team — Disaster Recovery Epics

- Part 1 (XL): Two stories

- Bamboo build plan for new target environment (incl. build parameter changes, AMI coverage)
- SQS migration between regions + S3 connectivity, static content, and DNS/F5 updates for failover cutover
- Part 2 (XL): Two stories — flagged as nice-to-have

- Synthetic heartbeat dashboard — scope unclear (how many adapters to cover; S3 and SQS covered today, full list TBD)
- Deterministic random adapter selection test harness — not built yet; would validate specific customer adapters (e.g. JNJ) during failover
- Confidence: ~80% on both; Part 2 uncertainty driven by unclear adapter list scope

- If adapter list is limited, Part 2 could drop from XL to L

### Org Team — DR Epics

- Part 1 (Medium): Failover for Exchange-specific APIs within shared API Gateway (used across Exchange, Data Connect, SCA, etc.)
- Part 2 (Large): Automate manual service validations (Rich Center, JPI, Org API) + one-click fallback

- Flagged as nice-to-have / not required for MVP DR
- More issues likely to surface once DR runs in stage

### DevOps / Docker Enrichment

- Most DR work sits in DevOps bucket
- Three dev team items identified:

- Line 49: Automate a currently manual process
- Line 51: Automate rollback (currently scripted; goal = one-click)
- Third item: Runbook creation (possibly sample doc push + post-failover validation)
- Matt sliding off to transformation team — impact on resourcing TBD, needs follow-up

### SSO & Network / Config Team

- Part 1 (Small): Fix misconfigured variables and missing parameters (IP addresses, DB hostnames) found during last DR exercise

- Route 53 or equivalent to resolve to active DB instance regardless of region
- Terraform/CloudFormation templates to use dynamic data sources (VPC IDs etc.) instead of static strings
- Checklist needed to validate consistency across all environments
- Part 2 (Small): SSO is a tier-zero service — its failure blocks other teams

- Need deep health check (not just /health) — lightweight DB read internally
- On failure: initiate failover or enter fail-open/cache mode (preserve existing sessions, don’t block new logins)
- Circuit breakers also in scope
- Circuit breaker precedent: new adapter API introduced one recently — not fully shipped yet; Pratik offered to walk team through the code

### Architecture & Strategic Tensions

- Current DR plan is solid but has significant unknown unknowns

- Suresh: last time, most effort was cataloging all AWS resources and determining what had IAC coverage and failover equivalents
- Many resources created manually over 4 years; IAC coverage is incomplete
- Two competing approaches debated:

1. Deep upfront discovery (waterfall) — more certainty, slower start
2. Assign 1–2 people to start discovery now — uncover unknowns while minimally disrupting current roadmap

- Option 2 preferred: use AWS service tags to enumerate SQS, S3, DynamoDB etc.; check IAC coverage and failover region presence
- Team’s preferred path (if unconstrained): finish resiliency/HA + modernize build/deploy pipelines first, then DR falls out naturally

- Conflict: currently building Bamboo plans while also trying to get off Bamboo
- Hard commitment: DR promised to Cardinal Health by end of year (contract-level)

- Scope: all apps, not just document processing
- No schedule cushion in current plan — any slip pushes DR dates
- Tooling: AWS CDK chosen for AWS resources; Terraform viable for non-AWS (e.g. MongoDB/Atlas); Pulumi flagged as more advanced option with full programming language support
- DR posture must be embedded going forward — every new service needs to be DR-ready from the start

### Key Risks & Open Questions

- Atlas migration timeline vs. DR deadline — which wins if they conflict?

- GHX historical pattern: run 12 things in parallel, complete none
- SQS architectural consideration: assume ~15-min max queue depth so failover only loses ~15 min of work (avoids costly cross-region constant sync)
- DR plan will need to be revisited as monolith decoupling progresses — not a final-state design
- Suresh has a prior AWS resource catalog (~4 years old) — may be partially reusable
- Product not yet aligned on DR vs. other Q2 priorities — to be raised in upcoming meetings

### Next Steps

- Mårten Engblom

- Get BI/Easy BI account provisioned (currently hitting access errors on Epic Gantt v2)
- Raise “just get started” approach with Mort and Curtis — argue for DR as prioritized product item to begin discovery immediately
- Discuss with product (tomorrow + Monday) which roadmap items to defer to de-risk DR deadline
- Team / TBD owner

- Assign 1–2 people to begin AWS resource discovery: enumerate all resources via service tags, check IAC coverage, check failover region presence, flag naming convention gaps
- Follow up on Matt’s reduced availability and impact on DR-dependent teams
- Confirm t-shirt size definitions are aligned between engineering and product
- Taylor to add start/end dates to Epic Gantt v2
- Pratik to share circuit breaker code with SSO team
- Forward tomorrow’s “GHX get our stuff together” meeting invite to Mårten if not already included

Chat with meeting transcript: https://notes.granola.ai/t/9e5e2cb3-8746-445b-b650-1c87e0bc0667

