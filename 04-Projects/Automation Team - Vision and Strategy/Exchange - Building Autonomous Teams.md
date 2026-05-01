# Exchange - Building Autonomous Teams

*Last Updated: 2026-04-17*

## Vision

Build autonomous, cross-functional teams that can deliver value independently without dependencies on other teams or centralized bottlenecks.

## Core Principles

### Reverse Conway Maneuver

*Added: 2026-04-17 from February 2026 MBR prep*

**Principle:** Organization structure should follow desired architecture, not the other way around.

**Conway's Law:** "Organizations design systems that mirror their communication structure"

**Reverse Conway Maneuver:** Restructure the organization to match the architecture you want, so that the resulting system architecture naturally follows.

**Why This Matters:**
- If we want decoupled, independently deployable services, we need teams structured to own those services end-to-end
- Current monolithic architecture reflects historical monolithic team structure
- Breaking the monolith requires breaking organizational dependencies first
- Teams organized around technical layers (UI team, API team, DB team) produce layered dependencies
- Teams organized around business capabilities produce decoupled services

### Org Topology for Autonomous Teams

*Added: 2026-04-17 from February 2026 MBR prep*

**Target Structure:**

**Pod Structure:**
- Each pod contains 2-3 cross-functional teams
- Pod aligned to business capability or product area
- Pod can deliver value independently without cross-pod dependencies

**Team Composition:**
- 5-7 engineers per team (player-coach EM + 4-6 ICs)
- Cross-functional: Full-stack capabilities within team
- Owns end-to-end: UI, APIs, services, data, deployment
- Player-coach Engineering Manager embedded in team

**Player-Coach EM Model:**
- EM spends 60-70% time on individual contribution (coding, architecture)
- 30-40% time on people management and team coordination
- Maintains technical depth and credibility
- Can fill gaps and unblock team directly
- Better technical decisions through hands-on involvement
- Models engineering excellence for the team

### Infrastructure and Cloud Native Ownership

*Added: 2026-04-17 from organizational maturity discussions*

**Principle:** Product teams own their infrastructure and IaC (Infrastructure as Code) in cloud-native architectures.

**Why This Matters:**
- Cloud-native architectures require teams to manage their own infrastructure
- Can't have centralized infrastructure team own everything—creates bottleneck
- Teams need infrastructure skills to be truly autonomous
- IaC should be part of product team competency

**Implications for Hiring:**
- Look for engineers with cloud and IaC experience
- Product teams need infrastructure capability
- DevOps skills distributed across teams, not centralized
- Part of the autonomous team vision

### Implications for Architecture

**To enable autonomous teams:**
- Break database dependencies (biggest blocker to independence)
- Decouple services so teams can deploy independently
- Each team owns its services, APIs, data stores, and deployment pipeline
- Minimize cross-team dependencies and synchronization points
- Teams should be able to deliver value without waiting on other teams

**Deployment Independence:**
- Teams can deploy their services without coordinating with other teams
- Changes in one team's domain don't require changes in other teams
- Reduce blast radius—failure in one service doesn't take down the system
- Enable continuous delivery at the team level

## Organizational Maturity Needed

Building autonomous teams requires:
1. **Technical Skills:** Cloud, IaC, full-stack, DevOps capabilities within teams
2. **Process Maturity:** Automated testing, CI/CD, monitoring, incident response owned by teams
3. **Cultural Shifts:** Trust teams to make decisions, accept mistakes as learning, reduce central control
4. **Leadership Model:** Player-coach EMs who lead by doing, not just directing

## Current Challenges

- Monolithic codebase and shared databases prevent team independence
- Centralized infrastructure and deployment processes create bottlenecks
- Cross-team dependencies in every release
- Long testing and deployment cycles force coordination overhead
- Teams organized around technical layers rather than business capabilities

## Path Forward

1. **Restructure Organization:** Align teams to business capabilities, not technical layers
2. **Break Dependencies:** Migrate shared databases, decouple services, remove architectural coupling
3. **Distribute Skills:** Build cloud and IaC capability within product teams
4. **Enable Independence:** Give teams ownership of their full stack, from UI to infrastructure
5. **Measure Autonomy:** Track deployment independence, cross-team dependencies, lead time to production
