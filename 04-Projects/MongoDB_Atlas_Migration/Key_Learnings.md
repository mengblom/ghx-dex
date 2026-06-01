---
title: MongoDB to Atlas Migration - Key Learnings
last_updated: 2026-06-01
---

# Key Learnings from MongoDB to Atlas Migration

## Executive Summary

This document captures critical lessons learned from the MongoDB to Atlas migration project, with particular focus on the May 29, 2026 STG incident. These learnings apply to any large-scale infrastructure migration and highlight the importance of environmental parity, comprehensive validation, and architectural assumptions.

---

## Technical Learnings

### 1. Environment Topology Parity is Critical

**What Happened**: 
- DEV/ATM environments use single MongoDB cluster
- STG/PERF/PROD use 3-cluster split architecture
- Issue only manifested in multi-cluster environment
- Single-cluster testing gave false confidence

**Why It Matters**:
- Lower environment success ≠ production readiness
- Topology differences mask entire classes of bugs
- "Works in DEV" doesn't mean "works in production"

**Lesson**:
> **Test in an environment that mirrors production topology, not just production data.**

**Action Items**:
- [ ] Audit all environment differences between STG and PROD
- [ ] Document which tests MUST run in production-like topology
- [ ] Consider: STG as "production topology test environment"

**Application**: 
- Other multi-cluster/multi-region migrations
- Distributed systems testing
- Load balancer configuration changes

---

### 2. Cache Keying Strategies Must Be Explicit

**What Happened**:
```java
// Implicit assumption: database name is unique across all clusters
Map<String, IMongoDatastore> DATASTORE_BY_DATABASE_NAME;

// Reality: Multiple clusters can have same database name
getDatastore(mongoClient, "business-transaction")
// Which cluster? BT? BD? BM? (Answer: whichever initialized first)
```

**Why It Failed**:
- Code assumed database name uniqueness
- Assumption valid in single-cluster architectures
- Assumption violated in multi-cluster split
- No validation of uniqueness invariant

**Lesson**:
> **Make caching keys explicit and validate invariants. Don't rely on implicit assumptions about global uniqueness.**

**Better Design**:
```java
// Explicit: Key on connection + database
String cacheKey = connectionString + ":" + databaseName;
Map<String, IMongoDatastore> DATASTORE_BY_CONNECTION_AND_DB;
```

**Application**:
- Any caching layer (Redis, in-memory, distributed)
- Service discovery (uniquely identify service instances)
- Configuration management (environment-specific keys)

---

### 3. Validation Must Cover the Success Scenario, Not Just Failure Modes

**What We Tested**:
- ✅ Can we connect to Atlas? YES
- ✅ Can we write to Atlas? YES
- ✅ Do apps start successfully? YES

**What We Didn't Test**:
- ❌ Can we read from ALL clusters? NO (only read from one)
- ❌ Is data distributed across clusters as expected? NO
- ❌ Do collection counts match per-cluster expectations? NO

**Why This Matters**:
- Success looks like failure when data is invisible
- Applications "worked" but showed incomplete data
- Users would see "missing" historical data

**Lesson**:
> **Test the success scenario comprehensively. Verify not just that the system runs, but that it runs CORRECTLY.**

**Enhanced Validation Checklist**:
```
For multi-cluster architecture:
- [ ] Can connect to ALL clusters (not just one)
- [ ] Can read from ALL clusters (verify actual queries succeed)
- [ ] Data distribution matches expectations (counts per cluster)
- [ ] Applications route queries to correct cluster
- [ ] Historical data visible (not just new writes)
```

**Application**:
- Load balancer migrations (verify traffic to ALL backends)
- Database sharding (verify data on correct shards)
- Multi-region deployments (verify routing to all regions)

---

### 4. Infrastructure + Code: Defense in Depth

**Single Point of Failure**:
- Could have prevented with infrastructure fix alone (distinct DB names)
- Could have prevented with code fix alone (smart cache keying)
- We chose to fix BOTH

**Why Both?**:
1. **Redundancy**: If one layer fails, other catches it
2. **Future-proofing**: Architectural improvement beyond immediate issue
3. **Learning**: Validates we understand root cause (not just symptoms)

**Lesson**:
> **When an issue can be fixed at multiple layers, consider fixing all layers. Defense in depth prevents recurrence and validates understanding.**

**Trade-off**:
- More work (10 repos + DB rename)
- More testing surface
- More things that can go wrong
- BUT: Long-term resilience

**Application**:
- Security (network + application + data layer)
- Reliability (redundancy at multiple levels)
- Configuration management (validation at multiple stages)

---

### 5. MongoMirror Limitations Must Be Understood

**Constraint**: MongoMirror cannot write to different database name than source
```
Source: self-hosted "business-transaction"
Target: Atlas "business-document"  ❌ Not supported
Target: Atlas "business-transaction" ✅ Supported
```

**Impact**:
- All 3 clusters synced to `business-transaction` (only valid option with MongoMirror)
- Created naming conflict at application layer

**Lesson**:
> **Understand tool constraints BEFORE designing architecture. Tools may force design decisions.**

**Better Approach**:
1. Research tool limitations first
2. Design architecture within those constraints
3. OR: Choose different tool if constraints unacceptable

**Application**:
- Migration tool selection (evaluate constraints early)
- Data pipeline design (understand source/sink limitations)
- Integration patterns (know what your tools can/can't do)

---

## Process Learnings

### 6. Pre-Flight Checklists Catch Human Error

**What We Missed**:
- No explicit check: "Are database names distinct across clusters?"
- Assumed (incorrectly) that naming would be correct

**Lesson**:
> **Checklists prevent assumption-based errors. If an assumption is critical, validate it explicitly.**

**Enhanced Pre-Migration Checklist**:
```markdown
Database Configuration:
- [ ] Database names are distinct across all clusters
- [ ] Connection strings point to correct cluster
- [ ] Database names match application configuration
- [ ] No naming conflicts in application cache layer

Validation:
- [ ] Can connect to each cluster independently
- [ ] Can read from each cluster independently  
- [ ] Data distribution matches expectations
- [ ] Collection counts correct per cluster
```

**Application**:
- Production deployments (verify assumptions)
- Configuration changes (check for conflicts)
- Infrastructure changes (validate prerequisites)

---

### 7. Fast Rollback is a Superpower

**What Went Well**:
- Root cause identified: 1 hour from symptom to diagnosis
- Rollback decision: < 30 minutes debate
- Rollback execution: < 2 hours complete
- Total downtime: ~3 hours (STG only)
- Zero data loss

**Why Fast Rollback Matters**:
- Limits blast radius (time-bound impact)
- Reduces customer exposure (if production)
- Preserves team morale (quick recovery)
- Enables aggressive innovation (safety net exists)

**Lesson**:
> **Invest in rollback procedures as much as forward migration. Fast rollback is risk mitigation.**

**Rollback Best Practices**:
- Document rollback procedure BEFORE migration
- Test rollback in lower environment
- Keep old infrastructure running (don't decommission immediately)
- Automate rollback steps (scripts, not manual)
- Define "abort criteria" before starting

**Application**:
- Feature flags (instant rollback)
- Blue/green deployments (switch back)
- Database migrations (rollback scripts)

---

### 8. Team Collaboration Under Pressure

**What Worked**:
- Cross-functional debugging (DBAs + Engineers + Architects)
- Slack-based coordination (async + real-time)
- No blame culture (focused on problem, not person)
- Transparent post-incident analysis

**Why It Matters**:
- Complex issues require multiple perspectives
- Psychological safety enables honest debugging
- Fast incident response requires trust

**Lesson**:
> **Build high-trust teams before incidents happen. Trust accelerates incident response.**

**Team Practices**:
- Regular cross-functional reviews
- Blameless post-mortems
- Celebrate learning (not just success)
- Document near-misses (learning opportunities)

---

### 9. Schedule Pressure is a Risk Multiplier

**Context**:
- Multiple migrations in short window (STG, PERF, Aurora)
- Compressed performance testing timeline
- External pressures (executive visibility)

**Risk**:
- Pressure to "just make it work" (skip validation)
- Fatigue leads to mistakes (reduced vigilance)
- Less time for retrospection (skip learning)

**Lesson**:
> **Schedule pressure amplifies all other risks. Build buffer time into critical migrations.**

**Mitigation**:
- Explicit "abort criteria" (don't push past limits)
- Mandatory retrospectives (even when successful)
- Team rotation (prevent burnout)
- Executive communication (manage expectations)

**Red Flags**:
- "We'll figure it out during the cutover"
- "No time for full testing"
- "Let's just try it and see"
- Multiple people working 60+ hour weeks

---

### 10. Pattern Recognition: Repeated Aborts Signal Deeper Issues

**History**:
- Feb 26-27: AuditDB initial attempt (downgraded/rolled back)
- May 29: BT/BD attempt (rolled back)
- Multiple "last minute aborts" throughout project

**Pattern**:
- High-pressure migrations
- Unexpected issues at cutover time
- Team frustration ("here we go again")

**Lesson**:
> **Repeated failures in similar contexts signal systemic issues, not bad luck.**

**Root Causes (Likely)**:
- Insufficient production-like testing
- Incomplete runbooks (missing edge cases)
- Schedule pressure (rushing validation)
- Complexity underestimation

**Action**:
- [ ] Retrospective on entire project (not just incidents)
- [ ] Identify systemic improvements (process, tooling, testing)
- [ ] Build confidence through smaller, more frequent migrations
- [ ] Consider: Pause and improve process before continuing

---

## Communication Learnings

### 11. Proactive Status Updates Reduce Anxiety

**What Worked**:
- Hourly updates during cutover window
- Clear "START" and "COMPLETE" announcements
- Transparent when issues occurred
- Fast communication of rollback decision

**Why It Matters**:
- Stakeholders can plan around known issues
- Reduces "what's happening?" questions
- Builds trust through transparency

**Lesson**:
> **Overcommunicate during high-risk operations. Silence creates anxiety.**

---

### 12. Executive Framing: Persistence, Not Failure

**Daniel Milburn's Recognition**:
> "This project has been a lot like Frodo journeying to Mount Doom... No matter what challenge that's been thrown your way, you all keep plugging away and putting one foot in front of the other."

**Why This Matters**:
- Reframes "failure" as "learning"
- Acknowledges team resilience
- Maintains morale through difficulty

**Lesson**:
> **Complex migrations are marathons, not sprints. Celebrate persistence, not just success.**

---

## Strategic Learnings

### 13. Technical Debt Pays Interest During Migrations

**Examples**:
- Connection pool architecture (per-DB clients, not per-cluster)
- Cache keying strategy (implicit assumptions)
- Notification template errors (pre-existing Freemarker issues)

**Impact**:
- Pre-existing issues surface during migration
- Migration becomes opportunity to fix technical debt
- But: Increases migration complexity

**Lesson**:
> **Migrations expose technical debt. Budget time to address debt or accept increased risk.**

**Decision Framework**:
- **Fix now**: If it blocks migration or increases risk significantly
- **Fix after**: If it's independent and migration can proceed safely
- **Document**: If you defer, add to technical debt backlog

---

### 14. Multi-Month Migrations Need Momentum Management

**Challenge**:
- Project duration: Feb - Aug (6+ months)
- Multiple leadership changes
- Team fatigue
- Competing priorities

**Risks**:
- Loss of context (people change roles)
- Motivation decline (long slogs)
- Skill atrophy (between environments)

**Lesson**:
> **Long-running migrations need deliberate momentum management and knowledge preservation.**

**Practices**:
- Regular retrospectives (every 2-3 environments)
- Documentation (runbooks evolve based on learnings)
- Team rotation (prevent burnout, distribute knowledge)
- Celebrate milestones (each environment is a win)

---

### 15. "Big 4" Initiatives Need Sustained Executive Support

**Context**:
- MongoDB to Atlas = 1 of 4 strategic technical initiatives
- High visibility (Curtis, CJ, executives)
- Competes with feature delivery

**Challenge**:
- Engineering capacity
- Stakeholder patience
- Sustained prioritization

**Lesson**:
> **Strategic initiatives require sustained executive air cover, not just initial approval.**

**Success Factors**:
- Regular executive updates (weekly)
- Tie to business outcomes (cost savings, resilience)
- Communicate learnings (not just status)
- Acknowledge team effort publicly

---

## Application to Other Projects

### Disaster Recovery
- **Relevance**: Multi-region architecture, failover testing
- **Lesson Applied**: Test actual DR scenarios in production-like topology
- **Lesson Applied**: Validate ALL regions can serve traffic, not just primary

### Breaking the Monolith
- **Relevance**: Multi-service architecture, distributed caching
- **Lesson Applied**: Cache keys must be service-aware
- **Lesson Applied**: Test service interactions in multi-service topology

### Red Mythos / Vulnerabilities
- **Relevance**: Patching across environments, rollback procedures
- **Lesson Applied**: Fast rollback capability for failed patches
- **Lesson Applied**: Environment parity for security testing

---

## Recommendations for Future Migrations

### Before Starting
1. **Document all environment differences** (topology, configuration, scale)
2. **Identify production-like test environment** (where MUST we test?)
3. **Research tool limitations** (what constraints do our tools impose?)
4. **Build rollback procedures first** (test rollback before forward migration)
5. **Define abort criteria** (when do we stop and rollback?)

### During Planning
1. **Map architectural assumptions** (what must be true for this to work?)
2. **Validate assumptions explicitly** (turn implicit into explicit checks)
3. **Design defense in depth** (fix at multiple layers when possible)
4. **Build comprehensive validation** (test success, not just failure)
5. **Schedule buffer time** (expect the unexpected)

### During Execution
1. **Use checklists** (prevent assumption-based errors)
2. **Communicate proactively** (hourly updates during high-risk windows)
3. **Monitor multiple signals** (not just "is it running?")
4. **Document deviations** (what differed from runbook?)
5. **Decide fast on rollback** (don't fight uphill battles)

### After Completion
1. **Retrospective every 2-3 environments** (capture learnings while fresh)
2. **Update runbooks** (incorporate learnings)
3. **Share learnings widely** (other teams benefit)
4. **Celebrate milestones** (maintain momentum)
5. **Address technical debt exposed** (don't just paper over)

---

## Conclusion

The May 29 incident was a **high-value learning opportunity disguised as a failure**. The team:
- Identified root cause in < 1 hour
- Rolled back cleanly in < 2 hours
- Developed comprehensive fix for both layers (infrastructure + code)
- Documented learnings for future migrations

**This is how high-performing teams operate**: Fast diagnosis, clean rollback, thorough analysis, improved process.

The MongoDB to Atlas migration is on track despite setbacks. Each environment teaches us something new. Each incident makes us stronger. This is the nature of complex technical work.

---

**Contributors**: Marten Engblom, Philippe Scoffie, Jeff Sherard, Suresh Kumar, Daniel Milburn  
**Last Updated**: June 1, 2026  
**Next Review**: Post-June 3 retry (capture additional learnings)
