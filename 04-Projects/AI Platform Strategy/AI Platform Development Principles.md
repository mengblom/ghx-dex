# AI Platform Development Principles

*Last Updated: 2026-04-14*

## Avoid Repeating DevOps Centralization Mistakes

**Warning:** Current AI platform approach mirrors early DevOps mistakes

**The Anti-Pattern:**
- Centralized teams stamping out patterns
- Everything goes through central authority
- Misses core point of individual team expertise
- Teams can't just use systems built by others without understanding

**The Better Approach:**
- Teach one tool/platform, let teams customize as needed
- Align on process, not implementation
- Build local orchestration capabilities
- Enable multiple platform initiatives rather than competing with them

**Philosophy:** Like hiring - don't hire Python engineer for Java role unless architectural fit. Teams need to build and understand their own systems.

## Engineer Learning and Reflection (The 20% Rule)

**Problem:** Agentic orchestration speeds up current work but doesn't improve practices
- Will accelerate bad outputs if fundamentals aren't solid
- Engineers need to understand full workflow before adding agents
- Risk of blindly following AI suggestions

**Proposed Solution: 20% Reflection Time**
- One day per week engineers don't code, just reflect
- Analyze Claude's/AI architectural choices and reasoning
- Learn from AI decisions to ask better questions later
- Prevent speed gains without quality improvements

## Database Access and Security

**Critical Concern:** Agents connecting directly to databases is problematic

**Why It's Wrong:**
- Same issues as before, just because it's an agent doesn't make it infallible
- Pattern regression from DBA evolution (machine access → profiling → observability)
- Should connect to observability platforms (New Relic) not direct DB access
- Automate through observability platforms, not direct database connections

**Question to Ask:** Why are orchestration tools accessing databases/AWS directly from machines rather than going through code control?

## Shared Tooling and Permissions

**Standardization Depends on Access Controls:**
- If proper permission matching works → standardization viable
- If not → prefer CLI tools scoped to individual access
- Example: Jira MCP server blocked from some projects in Slack integration

**Package Management:**
- Leverage existing tools better (JFrog skills repository underutilized)
- NPX skills for local downloads/installs
- Agentic package manager available

## Multi-Platform Strategy

**Current Reality:** Multiple teams building platforms
- Jeff, Greg, Arshad, Eric all have initiatives
- Goal: enable their platforms rather than build competing one
- Avoid standardization battles

**For New Teams (India approach):**
- Start from scratch with full lifecycle understanding
- Focus on 24 DORA capabilities for elite performance
- Incorporate dev containers, test data management, observability early
- Target: self-maintaining development team within one month

## Key Principles Summary

1. **Decentralize expertise** - Don't centralize AI patterns
2. **Reflection over speed** - Engineers need learning time, not just productivity gains
3. **Observability over direct access** - Route through proper monitoring
4. **Enable, don't standardize** - Support multiple platform approaches
5. **Understand before automating** - Teams must grasp fundamentals first
