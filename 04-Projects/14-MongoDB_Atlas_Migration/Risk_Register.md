---
last_updated: 2026-06-01
review_frequency: weekly
owner: Philippe Scoffie
---

# MongoDB to Atlas Migration - Risk Register

## Critical Risks (Occurred)

### RISK-001: Database Naming Conflicts in Multi-Cluster Architecture
**Status**: ⚠️ OCCURRED (May 29, 2026)  
**Severity**: CRITICAL  
**Probability**: N/A (already happened)  
**Impact**: Data visibility failure, rollback required

**Description**: When splitting databases across multiple clusters, identical database names cause application-layer cache collisions due to code that keys datastore cache by database name only.

**Incident**: STG BusinessTransaction migration on May 29, 2026. All 3 clusters configured with `business-transaction` name. Application routed all queries to single cluster, making 2/3 of data invisible.

**Mitigation (Applied)**:
1. ✅ Rename databases to be distinct: `business-transaction`, `business-document`, `business-metric`
2. ✅ Fix application code to key cache on `connection_string + database_name`
3. ✅ Add validation: verify distinct database names across clusters
4. ✅ Enhanced smoke tests: read from ALL clusters, not just one

**Lessons Learned**:
- Environment topology differences (single vs. multi-cluster) mask issues
- Cache keying strategies must account for multi-cluster architectures
- Validation must test actual production topology, not just connectivity

**Residual Risk**: LOW (with both fixes applied)

---

## High Risks (Active)

### RISK-002: Performance Degradation Post-Migration
**Status**: 🔴 ACTIVE  
**Severity**: HIGH  
**Probability**: MEDIUM  
**Impact**: Customer SLA violations, potential rollback

**Description**: Atlas performance characteristics may differ from self-hosted MongoDB, causing query slowdowns, increased latency, or resource exhaustion.

**Indicators to Watch**:
- Query response times > baseline + 10%
- CPU utilization > 80% sustained
- Memory pressure / cache evictions
- Slow query log volume increase
- Connection pool exhaustion

**Mitigation**:
- ✅ Performance testing in PERF environment before PROD
- ✅ Index optimization reviews with MongoDB support
- ✅ TTL index configuration matches self-hosted
- ✅ Connection pool tuning per application
- 🔄 Real-time monitoring during cutover (hourly checks)
- 🔄 Rollback plan ready (< 2 hours)

**Current Status**: 
- AuditDB migration showed minor spikes but within acceptable range
- ILM processing configuration differences identified and fixed
- Ongoing monitoring required for BT/BD migration

**Owner**: Ben Ludkiewicz, Selvakumar Samiappan

---

### RISK-003: Extended Cutover Windows
**Status**: 🔴 ACTIVE  
**Severity**: HIGH  
**Probability**: MEDIUM  
**Impact**: Customer downtime, reputational damage

**Description**: Cutover window exceeds planned maintenance window due to unexpected issues, application startup delays, or data sync lag.

**Historical Data**:
- AuditDB cutover: ~3 hours (within window)
- DEV/ATM: < 1 hour each
- STG May 29: Rollback required (unforeseen issue)

**Mitigation**:
- ✅ Detailed runbooks with timing estimates
- ✅ Parallel execution where possible (ConfigSvc updates, app restarts)
- ✅ Pre-staged MongoMirror sync (catch-up only during cutover)
- ✅ Automated scripts for connection string updates
- 🔄 Communication plan (hourly updates during window)
- 🔄 Escalation path to executive team if window exceeded

**Contingency**:
- Define "abort criteria" before each cutover (e.g., if rollback takes > 1 hour)
- Customer communication templates pre-approved

**Owner**: Philippe Scoffie, Sean Kotze

---

### RISK-004: Kafka Connector Failures
**Status**: 🟡 MODERATE  
**Severity**: HIGH  
**Probability**: LOW  
**Impact**: Data pipeline breaks, dependent systems affected

**Description**: Kafka connectors may fail to reconnect to Atlas after cutover, causing data sync failures to downstream systems (e.g., CDP, Analytics).

**Past Incidents**:
- AuditDB migration: All 22 connectors remained running
- Some AWS-related errors seen in logs but self-recovered

**Mitigation**:
- ✅ Connector health checks in smoke tests
- ✅ Pre-cutover verification of connection strings in connector configs
- ✅ Monitoring: Connector status checks every 15 minutes post-cutover
- 🔄 Runbook: Restart procedure for failed connectors

**Validation**:
```
Summary check:
Connectors: X total | X running | 0 paused | 0 failed
Tasks: Y total | Y running | 0 failed
```

**Owner**: Thiyagarajan Murugan, Ben Ludkiewicz

---

### RISK-005: Event Bus / Data Poller Backlog Buildup
**Status**: 🟡 MODERATE  
**Severity**: HIGH  
**Probability**: MEDIUM  
**Impact**: Transaction processing delays, customer complaints

**Description**: During cutover, Event Bus or Data Poller may accumulate backlogs due to connection delays, timeouts, or processing slowdowns.

**Acceptable Thresholds**:
- Data Poller backlog: < 50 events
- Event Bus backlog: < 100 events
- Tracking backlog: < 20 events

**Mitigation**:
- ✅ Hourly monitoring during/after cutover
- ✅ Alert thresholds configured
- ✅ Runbook: Backlog remediation procedures
- 🔄 Pre-cutover: Ensure backlogs are at zero before starting

**Post-Cutover Actions**:
- Monitor for 24 hours (hourly checks)
- Escalate if backlog > 500 events
- Investigate root cause if backlog persists > 4 hours

**Owner**: Arivazhagan Jeganathan, Suresh Kumar

---

## Medium Risks

### RISK-006: Lambda Function Sync Failures (EU/US)
**Status**: 🟡 MODERATE  
**Severity**: MEDIUM  
**Probability**: LOW  
**Impact**: Data inconsistency between EU and US regions

**Description**: Lambda functions syncing data between US and EU (TrackedConfigFile, BT/BD) may fail to connect to Atlas after migration.

**Affected Components**:
- `corex-eu-odin-migration` (TrackedConfigFile sync)
- 14 EU lambda functions requiring connection string updates
- US → EU sync lambdas

**Mitigation**:
- ✅ Code changes deployed to support Atlas connection strings (April 23)
- ✅ Lambda environment variables updated with new connection strings
- 🔄 Post-migration validation: Verify sync is working

**Validation Test**:
- Check last sync timestamp in DynamoDB
- Verify no errors in Lambda CloudWatch logs
- Confirm TrackedConfigFile collection is up-to-date in EU

**Owner**: Thiyagarajan Murugan, Matthew Turner

---

### RISK-007: Code Compatibility Issues
**Status**: 🟡 MODERATE  
**Severity**: MEDIUM  
**Probability**: LOW  
**Impact**: Application errors, feature breakage

**Description**: Application code may have assumptions about self-hosted MongoDB that don't hold in Atlas (e.g., admin commands, replica set configs).

**Known Issues**:
- ✅ MongoClient initialization updated for Atlas connection strings
- ✅ TTL index differences addressed
- ⚠️ Connection pool behavior may differ (needs monitoring)

**Mitigation**:
- ✅ Code reviews for MongoDB-specific assumptions
- ✅ Staging environment testing before PROD
- 🔄 Graylog monitoring for MongoDB-related errors
- 🔄 Quick rollback if critical errors detected

**Owner**: Suresh Kumar, Development Teams

---

### RISK-008: TTL Index Discrepancies
**Status**: 🟡 MODERATE  
**Severity**: MEDIUM  
**Probability**: MEDIUM (occurred in AuditDB)  
**Impact**: Data retention policy violations, storage bloat

**Description**: TTL indexes may not be configured identically on Atlas vs. self-hosted, leading to data retention differences.

**Incident**: AuditDB `mailbox.fileSystemEntry` collection showed 16M record discrepancy (Atlas: 1.3M, Self: 17.6M) due to TTL index timing difference.

**Mitigation**:
- ✅ Pre-migration: Verify TTL indexes match self-hosted
- ✅ Post-migration: Monitor collection counts for unexpected differences
- 🔄 Document expected discrepancies (e.g., TTL cleanup timing)
- 🔄 Engage MongoDB support if large discrepancies found

**Validation**:
- Collection count comparison: Atlas vs. Self-hosted
- Acceptable delta: < 5% or < 1M records (whichever is smaller)
- Document any > 5% differences with explanation

**Owner**: Ben Ludkiewicz, Sean Kotze

---

### RISK-009: Notification System Failures
**Status**: 🟡 MODERATE  
**Severity**: MEDIUM  
**Probability**: LOW  
**Impact**: Users don't receive critical alerts

**Description**: Notification DB split from AuditDB may cause notification delivery failures if application code hasn't been updated.

**Known Issues**:
- Freemarker template errors seen in Graylog (pre-existing issue)
- `Unable to send aggregated message` errors due to null references

**Mitigation**:
- ✅ Notifications split into separate cluster for isolation
- ⚠️ JIRA needed for Freemarker null reference issue (tracked but not fixed)
- 🔄 Post-migration: Monitor notification delivery rates

**Action Items**:
- [ ] Create JIRA for Freemarker template null handling (Kadhar/Ramasubramanian)
- [ ] Monitor notification delivery rates post-migration

**Owner**: Hari Prasad Narasapu, Visibility Team

---

## Low Risks (Monitoring)

### RISK-010: Disk Space on Notifications DB
**Status**: 🟢 LOW  
**Severity**: LOW  
**Probability**: LOW  
**Impact**: Notification storage full, delivery failures

**Description**: Notifications cluster disk space at 75% after AuditDB migration. Hasn't fluctuated much over 6 months on self-hosted.

**Mitigation**:
- 🔄 Monitor monthly
- 🔄 No immediate resize needed
- 🔄 Alert if > 85%

**Owner**: Ben Ludkiewicz

---

### RISK-011: External System Dependencies
**Status**: 🟢 LOW  
**Severity**: MEDIUM  
**Probability**: LOW  
**Impact**: External integrations break (CDP, Analytics)

**Description**: External systems (CDP load jobs, Analytics pipelines) hitting MongoDB may need connection string updates.

**Known Dependencies**:
- CDP load jobs (read-replica access)
- Analytics pipelines
- MS Portal lambdas

**Mitigation**:
- ✅ Dependency canvas maintained (Philippe)
- ✅ External team coordination (Robert Rudland, Hesheng Li)
- 🔄 Post-cutover validation with external teams

**Owner**: Philippe Scoffie, Gregory Wilson

---

### RISK-012: Read Preference Configuration
**Status**: 🟢 LOW  
**Severity**: LOW  
**Probability**: MEDIUM  
**Impact**: Suboptimal performance, primary overload

**Description**: Read preference not set in connection strings (except Community DB), causing all reads to hit primary instead of distributing to secondaries.

**Observation**: Post-AuditDB migration in PROD, primary nodes handle most traffic, secondaries idle except for replication.

**Mitigation**:
- 📋 Document as potential optimization (not critical for migration)
- 📋 Consider post-migration: Update connection strings with `readPreference=secondary` where appropriate
- ⚠️ Caution: Some queries require strong consistency (ActivityFlow)

**Action**: Post-migration optimization epic (not blocking)

**Owner**: Selvakumar Samiappan, Suresh Kumar

---

## Risk Mitigation Best Practices

### Pre-Migration Checklist
- [ ] Verify database names are distinct across clusters
- [ ] Verify TTL indexes match self-hosted configuration
- [ ] Verify connection strings correct in ConfigSvc
- [ ] Verify MongoMirror sync lag < 1 second
- [ ] Verify backlogs at zero (Event Bus, Data Poller)
- [ ] Verify Kafka connectors all green
- [ ] Verify Lambda environment variables updated
- [ ] Verify smoke test suite includes multi-cluster validation

### During Migration
- [ ] Hourly health checks (Heartbeat, Backlogs, Graylog)
- [ ] Monitor Atlas cluster metrics (CPU, Memory, Disk)
- [ ] Monitor application error rates
- [ ] Track cutover timing against plan
- [ ] Document deviations from runbook

### Post-Migration (24 Hours)
- [ ] Collection count validation
- [ ] Performance baseline comparison
- [ ] Error log analysis (Graylog)
- [ ] Kafka connector health
- [ ] Event Bus backlog trending
- [ ] Customer-reported issues tracking

### Communication Triggers
- **Proactive updates** (every hour during cutover)
- **Immediate escalation** if:
  - Cutover window exceeds plan by > 1 hour
  - Error rate > 5% of baseline
  - Backlog > 500 events and growing
  - Atlas cluster health degraded
  - Rollback required

---

## Risk Trend Analysis

### Risks Realized
1. **Database naming conflict** (RISK-001) - May 29, 2026
   - Trend: Environment differences masking issues
   - Action: Enhanced validation, code architecture fix

### Risks Mitigated
1. **AuditDB performance** - Initially HIGH, now LOW after successful migration
2. **Kafka connector failures** - Initially HIGH, now LOW after AuditDB success

### Emerging Risks
1. **Schedule compression** - Multiple migrations in short windows (STG+PERF+Aurora June 3-4)
2. **Performance testing overlap** - Testing ES Cloud + Atlas simultaneously
3. **Team fatigue** - Multiple aborts, compressed schedule

---

**Last Review**: June 1, 2026  
**Next Review**: June 3, 2026 (post-STG/PERF retry)  
**Risk Owner**: Philippe Scoffie  
**Escalation Path**: Philippe → Daniel Milburn → Curtis Nielsen
