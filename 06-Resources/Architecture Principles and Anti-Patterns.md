# Architecture Principles and Anti-Patterns

*Last Updated: 2026-04-17*
*Status: 🌿 Growing*
*Confidence: ✓ Validated*

## Overview

Strategic principles for system design and technical decision-making at GHX, including architectural patterns to embrace and anti-patterns to avoid. Emphasizes modernization toward standard formats and self-service capabilities.

## Data Format Strategy

### Canonical Format Philosophy

**Principle**: The canonical document format should be modern, standard, and developer-friendly (e.g., JSON), not legacy formats like EDI.

**Context**: Current mapping solutions rely heavily on EDI as the canonical format, which creates friction for modernization and self-service tooling.

**Current Reality**: X12 is the standard format, with XML as alternative. Canonical format varies based on what both Provider and Supplier use - only when both use non-X12 (e.g., XML) do we deviate from X12.

**Tooling Landscape**: Current mapping tool (Contivo) is outdated (9+ years old). Recommended alternative is IBM Sterling. Cotiviti (in Veritas portfolio) also makes Edifecs as another option.

**Opportunity**: Moving to JSON or other modern formats as canonical representation would:
- Improve developer experience
- Enable better self-service mapping tools
- Align with modern integration patterns
- Reduce complexity in tooling

## Monolithic Architecture Anti-Pattern

### The Vicious Cycle of Monolithic Deployment

**Problem**: Monolithic codebase with tight coupling and extreme dependencies (especially shared databases) forces monolithic deployment where any change deploys the entire application.

**Why This Matters**: This creates a self-reinforcing vicious cycle:

1. **Root Cause**: Single, tightly-coupled codebase with database-level dependencies forces whole-system deployment
2. **Initial Impact**: Massive blast radius and enormous test surface area make trusted automated coverage extremely difficult
3. **Defensive Response**: Uncertainty and high rollback risk force extended, careful testing cycles relying heavily on manual processes
4. **Vicious Cycle**: Long testing → monthly releases → changes batch → larger deployments → more testing → longer cycles
5. **Compounding Effects**: Each iteration increases risk awareness, deployment size, and testing requirements, trapping the team in defensive posture

**Key Insight**: The difficulty of achieving trusted automated test coverage for monolithic systems reinforces reliance on manual, time-intensive testing. High consequences of failure (rolling back or fixing monolithic deployment is much harder than fixing isolated service) lock teams into defensive posture.

**Alternative Approach**: Break coupling through domain-driven boundaries and independent deployment (see [[Autonomous Teams Strategy]] for organizational implications).

### Database Dependencies as Root Cause

**Critical Issue**: Many system components share the same databases, creating extreme coupling that forces monolithic deployment patterns.

**Why This Is The Biggest Problem**:
- Creates hidden dependencies that are difficult to track
- Makes it impossible to deploy services independently
- Single database failure can cascade across unrelated features
- Forces coordination across teams for any database change

**Example of Bad Dependencies**: 
- SFTP endpoints should not go down because Audit DB is unresponsive
- Core document processing should not go down because Audit DB is unresponsive
- Question patterns like: Why store 188M ActivityFlow documents/day in MongoDB only to delete and archive to S3 3 days later when we have rehydration mechanisms?

**Need**: Aggressively remove bad database dependencies to enable service independence.

### Operational Anti-Patterns

**Batch Processing Issues**:
- Processing events in batches rather than streams
- Examples: Data Poller
- Allows ebbs and flows, surges etc., to propagate through the system
- Creates unpredictable load patterns

**Insufficient Observability**:
- Logs retained only 7 days (Graylog limitation)
- No alerting on batch failures
- Example: 1000s of invoices failed, discovered 7+ days later via customer complaint through Product
- Service-level health checks need improvement

## Development Friction Points

### Monolith-Related Friction

**Cognitive Load Issues**:
- Large codebase with extensive coupling makes changes risky
- Difficult to reason about impact of changes
- Slow build and deployment cycles
- High cognitive load for developers
- Changes in one area can break seemingly unrelated features

**Strategic Impact**: This friction slows feature delivery, increases developer cognitive load, creates barriers to autonomous team operation, and makes it harder to attract/retain engineers who expect modern tooling.

### Testing Challenges

**Tandoori Legacy Framework**:
- Legacy testing framework that's difficult to work with
- Steep learning curve for writing and maintaining tests
- Slow test execution times
- Flaky tests reduce confidence
- Manual testing requirements due to insufficient automated coverage

**Impact**: Compounds monolith deployment challenges by making it harder to build trust in automated testing.

### Homegrown Components

**"Not Invented Here" Syndrome**:
- Custom-built tools and frameworks require specialized knowledge
- Lack of community support and documentation
- Maintenance burden on the team
- Onboarding friction for new engineers
- Prevents adoption of standard solutions

**Philosophy**: Systematically reduce these "taxes" through architecture improvements, tooling modernization, and selective adoption of industry-standard solutions over homegrown alternatives.

## Crisis as Opportunity

**Philosophy**: "Never let a crisis go to waste"

**When Incidents Happen**:
- There will be understanding for making large architecture changes
- Push for deeper architectural improvements rather than temporary band-aid solutions
- Avoid getting complacent after migrations (e.g., "go to Atlas, shard the crap out of databases, then get complacent")
- Improve "headroom" significantly, not just enough to get through immediate problems
- Move beyond "duct tape and bubblegum" mindset

**Why This Matters**: Crises create openings for architectural change that would otherwise face resistance.

## When to Use This

- When designing new integration patterns or data exchange systems
- When evaluating mapping tool modernization options
- When making decisions about canonical data formats
- When planning architecture improvements or modernization efforts
- When responding to incidents and considering root cause fixes
- When evaluating build vs buy decisions for tooling
- When justifying architecture changes to leadership
- When prioritizing technical debt and friction reduction

## Sources

This article synthesizes insights from:
- [[07-Archives/61 Meeting Notes/2026/Q1/2026-01-15 08.30 Modernizing Mapping solution.md|Modernizing Mapping Solution Planning]] - Identified opportunity to shift away from EDI as canonical format
- [[07-Archives/61 Meeting Notes/2026/Q1/2026-02-05 09.00 Review Mapping workflow.md|Review Mapping Workflow]] - Current format standards (X12/XML), tooling landscape (Contivo, IBM Sterling, Edifecs)
- [[04-Projects/Exchange Platform Architecture/2026-03-03 10.00 Monolith - SDLC and Delivery Speed Impact.md|Monolith SDLC Analysis]] - Detailed monolithic vicious cycle, defensive posture, testing challenges
- [[04-Projects/Exchange Platform Architecture/Architecture Picture/Architecture Flaws, Improvement Areas.md|Architecture Flaws]] - Database dependencies as root cause, operational issues, crisis as opportunity philosophy, development friction points (Tandoori, homegrown components, monolith friction)
