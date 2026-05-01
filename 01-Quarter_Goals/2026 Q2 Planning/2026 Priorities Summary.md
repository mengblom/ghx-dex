# 2026 Priorities Summary

Based on Q1 achievements and Q2 planning, your 2026 priorities should focus on three strategic pillars:

## **Organizational Foundation (People & Process)**
**Why**: Can't build autonomous teams or improve DORA metrics without right people, skills, and process discipline. 40% emergent work bleeds capacity. Need upskilling to enable end-to-end ownership—faster deployments, lower lead times, independent delivery.

- **Complete hiring wave**: Fill remaining ~40 open roles and ensure solid onboarding with clear vision/priorities
- **Upskill for autonomy**: Enable teams with GitHub Actions, IaC/Terraform capabilities so they own deployments and infrastructure
- **AI-native SDLC**: Integrate AI throughout development workflow—design, coding, testing, deployment, operations. Scale adoption via training, tooling (Claude, GitHub Copilot), and custom MCP servers for domain context
- **Fix agile mechanics**: Get all work into Jira, improve intake process, establish dashboard visibility with Aha, and protect sprint sanctity against the 40% emergent work pattern

## **Technical Architecture & Vision**
**Why**: "The Monolith" and hard dependencies creates massive blast radius, monthly releases, batched changes. Breaking it unlocks deployment frequency, reduces lead time, enables small independent changes. Clear boundaries eliminate silos and integration friction.

- **Break the monolith** → loosely coupled services, small blast radius, independent deployments (Strangler Pattern, not big-bang)
- **Define domain boundaries** for each team—clear ownership, eliminate coupling points and shared DB dependencies
- **Stop shared database anti-patterns**: teams own their data, right-size storage tech to use case (stop MongoDB-for-everything)
- **Prioritize foundational work**: Events/Messaging/Service Bus strategy, opinionated observability

## **Critical Technical Execution**
**Why**: EOL deadlines, production stability, security vulnerabilities aren't optional—must keep lights on. Quality debt erodes customer trust. AI-native SDLC and IPA LLM are strategic bets for competitive advantage.

- **Complete migrations**: MongoDB→Atlas (continue momentum), Elastic Cloud, finish AWS SDK 2.0 (2 repos remaining)
- **Resilience & stability**: DB stabilization, Disaster Recovery planning, ICS solution RTO testing
- **Chip away at technical debt**: Customer defects, incident remediations, vulnerability backlog—steady progress on quality and security
- **AI-native SDLC**: Deploy AI-assisted development practices (Claude, GitHub Copilot), integrate AI throughout design/coding/testing/deployment/operations
- **Innovation bets**: IPA LLM document understanding project

## **Context**
You delivered 1.03 Say/Do in Q1 while absorbing massive emergent work (40% of total stories). Your priorities reflect learning from that—you need process guardrails (intake, sprint protection) and team empowerment (hiring, upskilling) to sustain delivery while tackling architectural debt and strategic modernization.
