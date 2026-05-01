---
date: 2026-04-09
participants:
  - Mårten Engblom
companies: 
  - Untitled
tags:
  - meeting
meeting_type: general
source: granola
granola_id: efb79ba1-4560-4763-9c98-cdcd3d51bf41
---

# Untitled Meeting

### Nanoclaw Development & Orchestration Strategy

- Building orchestration layer for nanoclaw (simplified OpenClaw alternative)

- Single file architecture vs giant binary with unknown code
- Uses enterprise communication for everything
- Spins up containers, runs in sandbox by default
- Making it run on ECS with ephemeral tasks instead of VMs
- Personal AI system concept

- Has own identity, doesn’t use user credentials
- Handles news aggregation, calendar invites, recurring tasks
- Isolated to individual instances
- Users can modify/update codebase directly

### AI Platform Development Challenges

- Current approach mirrors early DevOps mistakes

- Centralized teams stamping out patterns
- Everything goes through central authority
- Misses core point of individual team expertise
- Teams need to build and understand their own systems

- Can’t just use systems built by others
- Like hiring - don’t hire Python engineer for Java role unless architectural
- Proposed solution: teach one tool/platform, let teams customize as needed

- Align on process, not implementation
- Build local orchestration using user credentials (compliance concern)

### Database Access & Security Concerns

- Current orchestration tools accessing databases/AWS directly from machines

- Why not going through code control?
- Pattern regression from DBA evolution (machine access → profiling → observability)
- Agents connecting directly to databases problematic

- Same issues as before, just because it’s an agent doesn’t make it infallible
- Should connect to New Relic for database performance monitoring
- Automate through observability platforms, not direct DB access

### Shared Tooling & Package Management

- Standardization depends on permissions and access controls

- Jira MCP server example: some projects blocked from Slack integration
- If proper permission matching worked, standardization viable
- Otherwise prefer CLI tools scoped to individual access
- Package management solutions

- NPX skills for downloading/installing skills locally
- Agentic package manager available
- JFrog has skills repository (underutilized)
- Need to leverage existing tools better

### Engineering Learning & Reflection

- Agentic orchestration speeds up current work but doesn’t improve practices

- Will accelerate bad outputs if fundamentals aren’t solid
- Need engineers to understand full workflow before adding agents
- Proposed 20% rule concept

- One day per week engineers don’t code, just reflect
- Analyze Claude’s architectural choices and reasoning
- Learn from AI decisions to ask better questions later
- Prevent blind following of AI suggestions

### Team Platform Initiatives

- Multiple parallel platform efforts ongoing

- Jeff, Greg, Arshad, Eric all building separate platforms
- Goal: enable their platforms rather than build competing one
- India team project approach

- Start from scratch with full lifecycle understanding
- Focus on 24 DORA capabilities for elite performance
- Incorporate dev containers, test data management, observability early
- Target: self-maintaining development team within one month

Chat with meeting transcript: https://notes.granola.ai/t/a27cd37d-9e20-40d1-85c0-92733f9f96e0

