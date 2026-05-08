# Exchange Monolith - Technical Complexity Context

**Purpose:** Reference document capturing key insights about Exchange codebase complexity and architectural challenges

## Core Problem: Dependency Chains

The Exchange monolith has deep, horizontal dependency chains that make isolated changes extremely difficult:

- **Single library upgrades cascade** through multiple layers
- **Testing requirements multiply** across dependent services and libraries
- **Coordinated releases required** when shared libraries are involved
- Work that appears simple (e.g., "upgrade library X") becomes much larger than a single story

## Evidence

**Confluence Analysis:** [Horizontal Dependency Analysis - The Real Complexity](https://prd.hub.ghx.com/wiki/spaces/EX/pages/1258750082/Horizontal+Dependency+Analysis+-+The+Real+Complexity)

This analysis documented the extent of horizontal dependencies and validated the wholesale upgrade approach.

## Implications for Work Estimation

### What Doesn't Work
- **Punchlist approach:** Treating vulnerability fixes as independent user stories
- **Piece-by-piece upgrades:** Attempting to upgrade dependencies one at a time
- **Simple work item counting:** External analyses (like vulnerability→work item ratios) that assume isolation

### What Does Work
- **Wholesale upgrades:** Upgrade everything at once in a dedicated branch/environment
- **Dedicated environment strategy:** Separate branch + environment for major upgrade work
- **AI-assisted complexity mitigation:** Tools like Claude Code to help navigate cascading changes
- **Realistic expectations:** Acknowledge complexity upfront rather than discovering it mid-stream

## Historical Context

**Why vulnerability work has been slow:**
- Previous attempts tried piece-by-piece approach
- Didn't account for dependency complexity
- Each "simple" fix revealed cascading requirements

**Current approach (Aaron & Ben):**
- Separate branch for vulnerability work
- Separate deployment environment
- Stay in that branch until all vulnerabilities fixed and tested
- Leverage AI tools for complexity management

## Strategic Connection

This complexity is a primary driver for:
- **Breaking the Monolith pillar** - Enable autonomous teams by reducing dependencies
- **Architecture transformation** - Move toward independent, deployable services
- **AI-native development** - Use AI to mitigate current complexity while working toward simpler architecture

## Related Work

- [[2026-05-06 DevSecOps Body of Work Discussion]] - Example of explaining this complexity to leadership
- [[2026-03-03 10.00 Monolith - SDLC and Delivery Speed Impact]] - Broader delivery impact
