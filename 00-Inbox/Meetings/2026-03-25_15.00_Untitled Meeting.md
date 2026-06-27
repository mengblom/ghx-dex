---
date: 2026-03-25
participants:
  - Mårten Engblom
companies: 
  - Untitled
tags:
  - meeting
meeting_type: general
source: granola
granola_id: 8696d617-c6d3-41d9-bdd1-05bdf4b3a395
---

# Untitled Meeting

### Initial Exchange Impressions

- Three days into new role - processing significant information volume
- Main challenge: understanding how different functions integrate
- CJ’s management style: points people at problems regardless of existing functions
- Strategy: stay focused on Exchange, identify team to embed with

### Team Integration Conversations

- Connected with Daniel and Paul for initial discussions
- Ramesh conversation scheduled for return from time off
- Couldn’t connect with Arshad today - will reconnect upon return
- Taylor meeting completed - gained infrastructure insights

### Infrastructure Concerns

- Current infrastructure described as “old school”
- Tension with desired team autonomy model

- Goal: teams independently own systems with standard practices/tooling
- Reality: centralized approaches creating headwinds

### DevSecOps Challenges

- EA function operates like “software guild” with dedicated lead

- Potential bottleneck for migration/upgrade efforts
- Jarvis encompasses part of EA vision
- Taylor/Arshad planning centralized DevOps model

- Embedded team approach for building workflows/pipelines
- Previous experience suggests this creates friction for all parties

### XDP Platform Analysis

- Built on Kubernetes with Prometheus, Grafana, certificate manager
- Full-fledged container platform requiring everything run in containers
- Concerns about forcing all applications into container model

- Lambda functions wouldn’t benefit from XDP tooling
- Would require separate infrastructure for non-container services
- Platform approach may be too heavy-handed for diverse application needs

### Cost Management Discussion

- Push to move off New Relic and other managed services
- Self-hosting mentality vs. actual cost-benefit analysis
- Question: is this employment-focused rather than value-driven?
- XDP appears more like “resume project” than cloud-native solution

### Organizational Structure Overview

- Daniel: Core pipeline (documents in → documents out)
- Mike: Organizations and Users platforms
- Ramesh: Mapping teams, IPA (document understanding), customer portal, continuity assurance
- Teams sized at critical mass around reverse Conway maneuver strategy

### Three Potential Focus Areas

1. **Orgasaurus team**

- Closest to deliverable state
- Easy win opportunity
- Local team reporting structure
2. **IPA project**

- Exciting greenfield opportunities
- Document understanding capabilities
3. **QA function**

- AI-assisted testing opportunities
- 10-12 day testing cycles need optimization
- Playwright conversion from existing tests
- Eric developing agent for test conversion

### Testing Process Issues

- Inverted testing pyramid - over-indexed on UI tests
- Monolith dependencies make unit/integration testing difficult
- Brittle UI tests cause most of 10-12 day delay
- Breaking out services would enable proper test coverage

### Development Tooling Strategy

- Need to decide: Claude vs GitHub Copilot vs other options
- Current spend: $90K/month on Claude through Bedrock
- GitHub Copilot advantages:

- Model switching capability
- Enterprise/organizational agents
- Integrated workflow automation
- $4/month per user vs. per-token pricing
- Hybrid approach consideration for power users vs. general users

### Next Steps

- Focus on Orgasaurus as first opportunity upon return
- Schedule Eric discussion on AI tooling strategy
- Map out software development lifecycle with agentic components
- Assess headcount needs after month of team embedding
- Customer enablement team transition to Happiest Minds contractors

Chat with meeting transcript: https://notes.granola.ai/t/f4ebc42d-1e0c-4aa9-8a18-b7af1004e0a2

