---
title: MongoDB to Atlas Migration - Detailed Schedule
last_updated: 2026-06-01
---

# Migration Schedule & Timeline

## Overview

**Project Duration**: February 27, 2026 - August 29, 2026 (6 months)  
**Current Status**: Phase 2 - AuditDB complete, BT/BD in progress  
**Next Milestone**: June 3, 2026 - STG+PERF BT/BD retry

---

## Migration Phases

### Phase 1: Planning & Preparation (Feb - Mar 2026) ✅

#### Week 1: Feb 27 - Mar 6
**AuditDB Initial Attempt**
- **Feb 26-27**: First AuditDB migration attempt
  - Status: ❌ DOWNGRADED/ROLLED BACK
  - Reason: Performance issues, Event Bus concerns
  - Learning: Need better validation, MongoDB support engagement

**Retrospective & Replanning**
- **Mar 2**: Audit DB Migration Recommendations + Look ahead
- **Mar 4**: 
  - Call with CJ (executive review)
  - Sync with MongoDB Support (technical deep-dive)
- **Mar 6**: 
  - Touchbase on DB Migration (CJ, Curtis, Marten, Arshad)
  - Topics: Testing strategy, communication plan, confidence building

#### Week 2-3: Mar 9 - Mar 25
**Schedule Review & Gap Analysis**
- **Mar 9-10**: Audit DB Migration Recommendations (Follow-up & Finalize)
- **Mar 11**: Audit DB - Atlas Migration Update
- **Mar 12**: Atlas Migration Schedule Review
  - Review Gantt chart from MongoDB
  - Confirm viability of timeline
- **Mar 25**: Accelerate database migration review
  - Agreement: No opportunity to shorten MongoDB timeline
  - Target remains: Aug 29, 2026

**Key Decisions**:
- ✅ Split AuditDB: 1 → 4 clusters
- ✅ Split BusinessTransaction: 1 → 3 clusters  
- ✅ Elastic Search migration can happen in parallel (April/May)
- ✅ PERF testing approach defined

---

### Phase 2: AuditDB Migration (Apr 2026) ✅

#### Week 1: Apr 15-19
**Preparation**
- ConfigSvc connection string preparation
- MongoMirror setup and sync initiation
- Runbook finalization
- Team coordination (DBAs + Engineers + QA)

#### Week 2: Apr 19-20
**PRODUCTION CUTOVER** ✅
- **Apr 19**: EU PROD AuditDB migration
  - Start: Morning MT
  - Status: ✅ SUCCESS
  - Duration: ~3 hours (within window)
  
- **Apr 20**: US PROD AuditDB migration
  - Start: Morning MT
  - Status: ✅ SUCCESS
  - Duration: ~3 hours (within window)

**Post-Migration Monitoring** (Apr 20-26)
- Hourly health checks (24 hours)
- Daily monitoring reports
- Performance baseline comparison
- Issue tracking (minor TTL index discrepancies noted)

**Recognition**: Daniel Milburn's "Frodo to Mount Doom" message (Apr 20)

#### Week 3-4: Apr 21 - Apr 30
**Elastic Search Migration (Parallel Track)**
- **Apr 21**: DEV Elastic Search cutover ✅
  - AF/BT combined into 1 cluster
  - Successfully validated
  
**Lambda Updates (EU/US Sync)**
- **Apr 23**: Lambda connection string updates
  - 14+ lambdas updated with Atlas connection strings
  - Code changes for TrackedConfigFile sync
  - Verified post-migration

---

### Phase 3: Lower Environments - BT/BD (May 2026) ✅

#### Week 1-2: May 12-14
**DEV & ATM Migrations**
- **May 12**: ATM BT cutover ✅
  - Single cluster (DEV/ATM topology)
  - Successful validation
  - No issues noted

- **May 14**: DEV/ATM BT migrations complete ✅
  - Both environments fully migrated
  - MongoDB Atlas operational

---

### Phase 4: STG/PERF - BT/BD (May-June 2026) 🔄

#### Week 3: May 20-26
**Preparation & Code Deployment**
- **May 20**: 
  - Code deployment to STG (BT/BD split support)
  - Schedule coordination for cutover week
  
- **May 21**: Code deployment to PERF confirmed

- **May 25**: Code deployment validation

- **May 26**: 
  - ES (AF/BT) Cutover in PERF scheduled
  - Final STG preparations

**Key Prep Items**:
- MongoMirror sync running (3 clusters: BT, BD, BM)
- ConfigSvc update scripts prepared (~54 properties)
- Validation tests ready
- Communication plan finalized

#### Week 4: May 27-29
**ATTEMPTED CUTOVER** ❌

**May 27**: 
- ES (AF/BT) Cutover in STG (planned)
- Status: DELAYED to May 29

**May 28**: 
- BT/BD verification in STG/PERF
- Connection string testing
- Final go/no-go

**May 29**: 
- **07:25 AM**: STG BT cutover START
- **08:29 AM**: Initial "success" announcement
- **10:00 AM**: Data visibility issue discovered
  - Historical data missing in UI
  - New data visible (writes going to Atlas)
- **10:01 AM**: Root cause identified
  - All 3 clusters named `business-transaction`
  - Application cache collision
- **10:08 AM**: Decision to rollback
- **10:37-11:58 AM**: Rollback execution
- **11:58 AM**: Rollback complete, STG stable

**Impact**:
- 3 hours degraded service (STG only)
- Zero data loss
- Schedule delay: 5 days

**Analysis** (May 29 - June 1):
- Comprehensive root cause analysis
- Infrastructure fix planned (rename databases)
- Code fix planned (cache keying strategy)
- Enhanced validation suite designed

---

### Phase 4 (Retry): STG/PERF - BT/BD (June 2026) 📅

#### Week 1: June 1-3
**Fix Implementation & Preparation**

**June 1** (Today):
- Root cause documented
- Infrastructure fix: Rename databases to distinct names
  - BT: `business-transaction`
  - BD: `business-document`
  - BM: `business-metric`
- Code fix: Update cache keying strategy
  - Key on `connection_string + database_name`
  - Deploy to ~10 repositories
  - Test in INT environment

**June 2**:
- INT environment validation with code fix
- MongoMirror re-sync with correct database names
- Enhanced smoke tests implemented
- Runbook updated with new validation steps

**June 3** (SCHEDULED):
- **STG BT/BD cutover (retry)** 🎯
  - With both infrastructure + code fixes
  - Enhanced validation (multi-cluster reads)
  - Rollback plan ready
  
- **PERF BT/BD cutover** 🎯
  - Parallel with STG
  - Same fixes applied
  - Performance baseline capture

- **PERF Aurora migration** 🎯
  - RDS to Aurora cutover
  - Separate track, but same day

**June 4**:
- PERF performance testing (Aurora)
- STG/PERF stability monitoring
- Analysis: Did fixes work?

---

### Phase 5: Remaining Environments (June-July 2026) 📅

#### Week 2: June 8-13
**INT Environment** 📅
- BT/BD cutover to Atlas
- Elastic Search cutover to Elastic Cloud
- Validation with external teams

#### Week 3: June 15-20
**Performance Testing & Analysis** 📅
- Compare: ES Cloud vs. Atlas performance
- Decision: Any rollbacks needed?
- Final PROD go/no-go criteria validation

---

### Phase 6: Production Cutover (July-Aug 2026) 📅

#### Tentative Schedule (TBD)

**EU Production**:
- Week: TBD (July)
- Duration: ~3-4 hour maintenance window
- Communication: Customer notifications 1 week prior

**US Production**:
- Week: TBD (July-Aug)
- Duration: ~3-4 hour maintenance window
- Communication: Customer notifications 1 week prior

**Final Validation** (Aug 2026):
- Post-PROD monitoring (2 weeks)
- Performance validation
- Cost analysis (actual vs. projected savings)
- Project closeout: Aug 29, 2026

---

## Coordination With Other Migrations

### Elastic Search to Elastic Cloud
**Parallel Track** - Different databases, similar challenges

| Environment | ES Migration Date | BT/BD Migration Date |
|-------------|-------------------|----------------------|
| DEV | Apr 21, 2026 ✅ | May 12, 2026 ✅ |
| ATM | May 12, 2026 ✅ | May 12, 2026 ✅ |
| STG | May 8, 2026 ✅ | June 3, 2026 📅 |
| PERF | May 26, 2026 ✅ | June 3, 2026 📅 |
| PROD | TBD (June-July) | TBD (July-Aug) |

### RDS to Aurora Migration
**Separate Initiative** - Coordinated timing to avoid overlap

- **PERF**: June 3, 2026 (same day as BT/BD retry)
  - Risk: Multiple migrations in single day
  - Mitigation: Separate teams, clear dependencies
- **PROD**: TBD (post-BT/BD validation)

### Quartz Upgrade
**Dependency**: Deferred pending migration completion
- Original schedule: May 29, 2026 (PERF)
- Decision: Delay to avoid testing overlap
- New schedule: Post-Atlas migration validation

---

## Critical Path & Dependencies

### Pre-Requisites (Before Each Environment)
1. ✅ MongoMirror sync lag < 1 second
2. ✅ Code deployed supporting Atlas (if needed)
3. ✅ ConfigSvc connection strings staged
4. ✅ Validation scripts tested
5. ✅ Rollback procedure documented
6. ✅ Communication sent (production environments)

### Success Criteria (Post-Cutover)
1. ✅ All applications connected to Atlas
2. ✅ Zero data loss (collection counts match)
3. ✅ Performance within 10% of baseline
4. ✅ Kafka connectors operational (100% green)
5. ✅ Event Bus backlog < 100
6. ✅ Data Poller backlog < 50
7. ✅ No database errors in Graylog

### Abort Criteria (During Cutover)
- Rollback if cutover exceeds planned window by > 1 hour
- Rollback if error rate > 5% of baseline
- Rollback if backlog > 500 and growing
- Rollback if Atlas cluster health degraded
- Rollback if critical application down

---

## Meeting Cadence

### Weekly (During Active Migration)
- **Monday**: Week planning, go/no-go decisions
- **Wednesday**: Mid-week checkpoint
- **Friday**: Retrospective, lessons learned

### Daily (During Cutover Week)
- **Morning standup**: Status, blockers, prep
- **Evening recap**: What happened, what's next

### Executive Updates
- **Weekly**: Curtis/CJ update (status, risks, decisions needed)
- **Post-milestone**: Environment completion summaries
- **Incident-driven**: Same-day communication for issues

---

## Resource Allocation

### Core Team Availability
- **Philippe Scoffie**: Full-time project lead
- **Jeff Sherard**: Primary DBA, 50% allocation
- **Thiyagarajan Murugan**: Lead engineer, 80% allocation
- **Ben Ludkiewicz**: DBA support, 30% allocation
- **Sean Kotze**: DBA, cutover execution, on-demand

### Team Rotation (Preventing Burnout)
- Primary/secondary on-call rotation
- Knowledge sharing sessions (weekly)
- Post-environment breaks (3-5 days between major cutovers)

### External Dependencies
- **MongoDB Support**: Available for escalations
- **Performance Testing Team**: Selvakumar's team (PERF validation)
- **External Systems**: CDP, Analytics, MS Portal (coordination needed)

---

## Risk Events & Buffer Time

### Known Risk Windows
1. **June 3, 2026**: Triple migration (STG BT, PERF BT, PERF Aurora)
   - Mitigation: Separate teams, clear sequencing
   - Buffer: Can delay Aurora by 1 week if needed

2. **Performance Testing Overlap**: Testing ES + Atlas simultaneously
   - Mitigation: Separate test scenarios, clear baselines
   - Buffer: 2 weeks for analysis before PROD decision

3. **Summer Holidays**: July-August (team capacity reduction)
   - Mitigation: Plan PROD cutovers around core team availability
   - Buffer: 2-week flexibility in PROD dates

---

## Progress Tracking

### Environments Completed: 4/7 (57%)
- ✅ DEV (AuditDB, BT/BD, ES)
- ✅ ATM (AuditDB, BT/BD, ES)
- ✅ EU PROD (AuditDB only)
- ✅ US PROD (AuditDB only)

### Environments Remaining: 3/7 (43%)
- 🔄 STG (BT/BD pending retry, ES done)
- 🔄 PERF (BT/BD pending retry, ES done)
- 📅 PROD (BT/BD, ES pending)

### Database Groups Completed: 1/2 (50%)
- ✅ AuditDB (all environments)
- 🔄 BusinessTransaction/Document/Metric (in progress)

---

## Lessons Learned (Applied to Schedule)

### From May 29 Incident
1. **Buffer time added**: +2 days between environments for analysis
2. **Enhanced validation**: +1 hour per cutover for multi-cluster checks
3. **Rollback testing**: Mandatory in lower environment before PROD
4. **Code+Infra fixes**: Both layers addressed before retry

### From AuditDB Success
1. **Hourly monitoring**: Proven effective, keep for all cutovers
2. **Kafka validation**: Add to standard checklist
3. **TTL index check**: Known issue, document expected deltas
4. **Team collaboration**: Cross-functional war room model works

### From Overall Project
1. **Executive air cover**: Sustained support critical for long-running project
2. **Team morale**: Celebrate milestones, acknowledge setbacks
3. **Knowledge preservation**: Document learnings after each environment
4. **Realistic scheduling**: Don't compress windows to meet arbitrary dates

---

**Last Updated**: June 1, 2026  
**Next Key Dates**:
- **June 2**: INT validation with fixes
- **June 3**: STG+PERF retry (major milestone)
- **June 4**: Performance testing & analysis

**Project Completion Target**: August 29, 2026
