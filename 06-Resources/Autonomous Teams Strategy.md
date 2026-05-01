# Autonomous Teams Strategy

*Last Updated: 2026-04-17*
*Status: 🌿 Growing*
*Confidence: ⚠️ Hypothesis*

## Overview

Philosophy and principles for organizing engineering teams around autonomy, domain boundaries, and ownership. Core vision: build autonomous, cross-functional teams that can deliver value independently without dependencies on other teams or centralized bottlenecks. Emphasizes team structure aligned with target architecture using the Reverse Conway Maneuver.

## Core Principles

### Reverse Conway Maneuver

**Conway's Law**: "Organizations design systems that mirror their communication structure"

**The Maneuver**: Organization structure should follow desired architecture, not the other way around. Restructure the organization to match the architecture you want, so that the resulting system architecture naturally follows.

**Why This Matters**:
- If we want decoupled, independently deployable services, we need teams structured to own those services end-to-end
- Current monolithic architecture reflects historical monolithic team structure
- Breaking the monolith requires breaking organizational dependencies first
- Teams organized around technical layers (UI team, API team, DB team) produce layered dependencies
- Teams organized around business capabilities produce decoupled services

**Principle**: Form teams around the target architecture and domain boundaries, not current organizational constraints. Intentionally design team boundaries to enable the desired system design.

### Target Org Topology

**Pod Structure**:
- Each pod contains 2-3 cross-functional teams
- Pod aligned to business capability or product area
- Pod can deliver value independently without cross-pod dependencies

**Team Composition**:
- 5-7 engineers per team (player-coach EM + 4-6 ICs)
- Cross-functional: Full-stack capabilities within team
- Owns end-to-end: UI, APIs, services, data, deployment
- Player-coach Engineering Manager embedded in team

### Leadership Model: Player-Coach EM

**Time Allocation**:
- 60-70% time on individual contribution (coding, architecture)
- 30-40% time on people management and team coordination

**Why This Model**:
- Maintains technical depth and credibility
- Can fill gaps and unblock team directly
- Better technical decisions through hands-on involvement
- Models engineering excellence for the team
- Understands team challenges from direct experience

### Infrastructure and Cloud-Native Ownership

**Principle**: Product teams own their infrastructure and IaC (Infrastructure as Code) in cloud-native architectures.

**Why This Matters**:
- Cloud-native architectures require teams to manage their own infrastructure
- Can't have centralized infrastructure team own everything—creates bottleneck
- Teams need infrastructure skills to be truly autonomous
- IaC should be part of product team competency

**Implications for Hiring**: Look for engineers with cloud and IaC experience. DevOps skills distributed across teams, not centralized. Part of the autonomous team vision.

### Architectural Implications

**To Enable Autonomous Teams**:
- Break database dependencies (biggest blocker to independence)
- Decouple services so teams can deploy independently
- Each team owns its services, APIs, data stores, and deployment pipeline
- Minimize cross-team dependencies and synchronization points
- Teams should be able to deliver value without waiting on other teams

**Deployment Independence**:
- Teams can deploy their services without coordinating with other teams
- Changes in one team's domain don't require changes in other teams
- Reduce blast radius—failure in one service doesn't take down the system
- Enable continuous delivery at the team level

### Work Organization

**Single Source of Truth**: All work across all stakeholders must be in Jira. If it's not in Jira, it's not being worked on. This includes:
- Commercial work
- Customer defects
- Incident root causes
- Vulnerabilities
- Technical work

**Why**: Ensures visibility, accountability, and prevents shadow work streams.

**Autonomy as Core Ask**: The organizational expectation is for teams to work towards autonomy - owning their domain, making their own decisions, and operating independently while maintaining alignment.

## Organizational Maturity Needed

Building autonomous teams requires development across multiple dimensions:

1. **Technical Skills**: Cloud, IaC, full-stack, DevOps capabilities within teams
2. **Process Maturity**: Automated testing, CI/CD, monitoring, incident response owned by teams
3. **Cultural Shifts**: Trust teams to make decisions, accept mistakes as learning, reduce central control
4. **Leadership Model**: Player-coach EMs who lead by doing, not just directing

## Current Challenges

- Monolithic codebase and shared databases prevent team independence
- Centralized infrastructure and deployment processes create bottlenecks
- Cross-team dependencies in every release
- Long testing and deployment cycles force coordination overhead
- Teams organized around technical layers rather than business capabilities

## Path Forward

1. **Restructure Organization**: Align teams to business capabilities, not technical layers
2. **Break Dependencies**: Migrate shared databases, decouple services, remove architectural coupling
3. **Distribute Skills**: Build cloud and IaC capability within product teams
4. **Enable Independence**: Give teams ownership of their full stack, from UI to infrastructure
5. **Measure Autonomy**: Track deployment independence, cross-team dependencies, lead time to production

## When to Use This

- When designing organization structure or team boundaries
- When making decisions about team ownership and domain assignments
- When evaluating team autonomy and decision-making authority
- When establishing work tracking and visibility practices
- When making architectural decisions that affect team independence
- When hiring for team roles (need cloud/IaC skills for autonomy)

## Sources

This article synthesizes insights from:
- [[2026-02-01 10.00 February 2026 MBR Prep|February 2026 MBR Prep]] - Core team structure philosophy, autonomy principles, player-coach model, work organization
- [[04-Projects/Automation Team - Vision and Strategy/Exchange - Building Autonomous Teams.md|Exchange - Building Autonomous Teams]] - Detailed Reverse Conway Maneuver explanation, pod structure, player-coach EM time allocation, infrastructure ownership, architectural implications, deployment independence
- [[04-Projects/Automation Team - Vision and Strategy/Organizational Maturity Observations.md|Organizational Maturity Observations]] - Infrastructure and cloud-native ownership principles, implications for hiring
