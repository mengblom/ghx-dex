# DevSecOps Body of Work Discussion

**Date:** May 6, 2026
**Context:** Email thread about vulnerability remediation approach and complexity analysis
**Key People:** [[CJ_Singh|CJ]], [[Tony_Middleton|Tony]], [[Arshad_Mahammad|Arshad]]

## Background

Tony shared analysis showing 858 vulnerabilities across 12 engineering pods reduce to 98 actual work items (9:1 leverage ratio). CJ asked about efficient execution approach.

## Key Points from Discussion

### AMI Refresh Pipeline (Exchange Team)

Exchange team is building a parallel release and deployment pipeline specifically for gold AMI refreshes:
- Will run weekly or biweekly (vs monthly monolith code release)
- Ensures OS/AMI updates from DevSecOps reach production faster
- More isolated work suitable for the 9:1 leverage ratio

### Code/OSS Vulnerability Complexity

The 858→98 analysis underestimates real-world complexity for larger codebases:
- **Assumption flaw:** Analysis assumes each fix can be done in isolation
- **Reality:** Monolithic codebases have deep dependency chains where:
  - Single library upgrade cascades through multiple layers
  - Testing requirements multiply across dependent services
  - Work becomes much larger than "a story"

### Exchange Monolith as Example

Documented challenge: [Horizontal Dependency Analysis - The Real Complexity](https://prd.hub.ghx.com/wiki/spaces/EX/pages/1258750082/Horizontal+Dependency+Analysis+-+The+Real+Complexity)

**Key insight:** Only realistic path is wholesale upgrade of everything at once
- Monolith too large/intertwined for piece-by-piece approach
- This explains why vulnerability work has been slow historically

### Current Approach

Aaron and Ben working on:
- Separate branch for vulnerability work
- Targeting separate environment
- Using Claude Code to help with complexity
- Stay there until all vulnerabilities fixed and problems solved/tested

## Strategic Implications

1. **AMI refreshes:** Good fit for consolidated/efficient approach
2. **Code/OSS fixes:** Need realistic expectations - not simple punchlist work
3. **Leverage AI:** Using Claude Code to mitigate complexity
4. **Wholesale approach:** Validated by dependency analysis

## Related

- [[Exchange Platform Architecture]] project
- Dependency complexity as blocker for autonomous teams
- Breaking the monolith pillar work
