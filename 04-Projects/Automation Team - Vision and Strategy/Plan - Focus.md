- Organization
    - Need 1 player-coach manager for each team
- Databases
    - Need a complete inventory and usage etc.
    - Stabilizing
    - Optimizing
    - No ORMs for bulk operations / set queries / analytics queries etc.
- Monolith
    - Carve out 1 piece and rebuild according to "what good looks like"
- Ways of working
    - Need Initiative level in Jira!
    - Need comprehensive roadmap (Product owns this)
    - Agile Impovements
        - Sprint goals + a few bullets for each sprint… communicated out.
        - Make sprint reviews more fun, more attended, more of an event
- World Class Engineering Team
    - Agile Maturity Model?
- AI Native Development

## Quarterly Planning Process Improvements

**Current Challenge:** "I don't love how we are doing it"
- Quarterly planning to this level of detail in software development is not very valuable
- Too much uncertainty that far out
- Company operates this way, so need to make it less painful

**Improvements Needed:**

1. **Higher Level Planning**
   - Planning at epic level is too granular and detailed
   - Should plan at **initiative level** instead
   - Focus on: what initiatives are we prioritizing to make progress on this quarter
   - Less detail, more strategic direction

2. **Tool Integration**
   - Need to nail down the process around Jira and Aha!
   - Make sure the integration is automated
   - Reduce manual overhead

**Philosophy:** Accept the quarterly cadence but adjust the fidelity to match software development uncertainty

### Specific Anti-Patterns to Avoid

*Added: 2026-04-17 from April 2026 staff meeting planning*

**Don't do deep dive breakdowns of specific epics in quarterly planning:**
- Example: Breaking down Mongo Atlas Migration into specific database-by-database execution plans
- These details belong in sprint planning, not quarterly planning
- Quarterly planning should focus on: "We're going to make progress on the Mongo Atlas Migration initiative"
- Let the teams doing the work plan the tactical details closer to execution

**Architecture discussions should be strategic, not tactical:**
- Don't plan specific code changes or implementation details
- Focus on strategic direction: what architectural initiatives matter this quarter
- Example: "Address coupling and dependencies" vs. detailed refactoring plans

**Why This Matters:**
- Software development has too much uncertainty 3 months out for detailed plans
- Teams closest to the work make better tactical decisions
- Quarterly planning should guide direction, not prescribe execution
- Reduces planning overhead while maintaining strategic alignment