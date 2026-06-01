---
incident_date: 2026-05-29
incident_type: migration_failure
severity: critical
environment: STG
database: BusinessTransaction
status: resolved_rollback
root_cause_identified: true
resolution_date: 2026-05-29
tags:
  - incident
  - rollback
  - database-naming
  - code-architecture
---

# STG BusinessTransaction Migration Failure - May 29, 2026

## Incident Summary

**What happened**: STG BusinessTransaction database migration to Atlas appeared successful but was rolled back within hours due to data visibility issues in the application UI.

**Impact**: 
- New data written to Atlas was visible
- Historical data from original clusters was NOT visible
- STG environment partially degraded during investigation (2-3 hours)
- Migration schedule delayed by 5 days (May 29 → June 3)

**Resolution**: Complete rollback to self-hosted clusters, identified root cause, planning code + infrastructure fix for June 3 retry.

---

## Timeline

### 07:25 AM MDT - Migration Start
- **Sean Kotze** announced: "Heads up — We are currently in the process of cutting over STG BusinessTransaction (BT) to Atlas"

### 08:29 AM MDT - Initial "Success"
- **Jeff Sherard** announced: "✅ STG BusinessTransaction (BT) cutover to Atlas — Complete"
- Connection strings updated
- Applications restarted
- Initial smoke tests passed

### 10:00-10:01 AM MDT - Problem Discovery
- **Thiyagarajan Murugan** identified issue:
  - MEX Orders page showing incomplete data
  - Transactions page missing historical records
  - Only new writes were visible

### 10:01-10:06 AM MDT - Root Cause Identified
**The smoking gun**: All 3 Atlas clusters were configured with **identical database names**:
- BT Cluster: `business-transaction` ❌
- BD Cluster: `business-transaction` ❌ (should be `business-document`)
- BM Cluster: `business-transaction` ❌ (should be `business-metric`)

**Why it broke**:
```java
// Problematic code in application layer
private static final Map<String, IMongoDatastore> DATASTORE_BY_DATABASE_NAME = Maps.newConcurrentMap();

public static IMongoDatastore getDatastore(final MongoClient mongoClient, final String databaseName) {
    return DATASTORE_BY_DATABASE_NAME.computeIfAbsent(databaseName,
            dbName -> new MongoDatastore(mongoClient, getMapperOptions(), dbName));
}
```

**The failure mode**:
1. Application starts up, initializes database connections
2. **BUSINESS_METRIC_DB** initializes FIRST → caches MongoClient for "business-transaction" (BM cluster)
3. **BUSINESS_DOCUMENT_DB** initializes SECOND → `computeIfAbsent("business-transaction")` returns cached BM client
4. **BUSINESS_TRANSACTION_DB** initializes THIRD → gets cached BM client again
5. **All queries route to BusinessMetric cluster only**
6. New writes go to BM cluster → visible in UI
7. Old data in BT/BD clusters → invisible because application never connects to those clusters

### 10:08-10:37 AM MDT - Decision to Rollback
- **Jeff Sherard**: "let's roll back to old clusters"
- Team discussed alternatives (rename DB, fix code, both)
- Decision: **Rollback immediately, fix both issues for retry**

### 10:37-11:58 AM MDT - Rollback Execution
- **Thiyagarajan Murugan** executed rollback:
  1. Updated ConfigSvc connection strings → point back to self-hosted
  2. Rolling restart of all STG applications
  3. Verified connectivity and data visibility
  4. Confirmed: "Everything is working as expected"

### 11:58 AM MDT - Rollback Complete
- STG fully operational on self-hosted clusters
- No data loss (staging environment)
- Atlas infrastructure left in place (stopped syncing)

---

## Root Cause Analysis

### Why Did This Happen?

**Immediate cause**: Database naming conflict + code assumption violation

**Deeper causes**:
1. **Environment differences masked the issue**:
   - DEV/ATM/INT use **single cluster** → same DB name across logical databases doesn't matter
   - STG/PERF/PROD use **3 clusters** → same DB name creates cache collision
   - Testing in DEV/ATM didn't expose this failure mode

2. **Code architecture assumption**:
   - Datastore cache keyed by database name only
   - Assumes: database name uniquely identifies a datastore
   - Reality: `connection_string + database_name` is the unique identifier
   - Works fine when each logical DB has unique name OR single cluster

3. **Infrastructure misconfiguration**:
   - MongoMirror sync configured with same target DB name on all 3 clusters
   - No validation that logical DB names were distinct across clusters

4. **Validation gap**:
   - Smoke tests checked "can we write?" (YES - to BM cluster)
   - Smoke tests didn't check "can we read from ALL clusters?" (NO - only BM)
   - Missing test: verify data distribution across all 3 target clusters

### Why Wasn't It Caught Earlier?

- **Lower environments work differently**: Single cluster in DEV/ATM
- **No integration test for multi-cluster split**: Never tested the actual production topology
- **Assumption gap**: Team assumed database names would be distinct (as they are in prod-style 3-cluster setups)

---

## Impact Assessment

### Technical Impact
- ✅ **No data loss**: Staging environment, write-heavy workload
- ✅ **Clean rollback**: Complete restoration within 2 hours
- ⚠️ **3 hours partial degradation**: STG mongo calls failing during investigation
- ⚠️ **Schedule slip**: 5-day delay (May 29 → June 3)

### Business Impact
- ✅ **No customer impact**: Staging environment only
- ⚠️ **Team morale**: Another last-minute abort (pattern recognition)
- ⚠️ **Executive confidence**: High-visibility project with repeated delays

### Downstream Impact
- **PERF environment**: Delay from May 28 → June 3
- **Performance testing**: Compressed timeline for validation
- **Aurora migration**: Risk of cascading delays (scheduled June 3)

---

## Resolution Plan (June 3 Retry)

### Two-Part Fix (Both Required)

#### 1. Infrastructure Fix (DBA)
**Owner**: Jeff Sherard, Sean Kotze

- Rename databases in Atlas to be distinct:
  - BT Cluster: `business-transaction` ✅
  - BD Cluster: `business-document` ✅ (change from `business-transaction`)
  - BM Cluster: `business-metric` ✅ (change from `business-transaction`)

- Re-initiate MongoMirror with correct target names
- Verify sync to correct database names before cutover

#### 2. Code Fix (Engineering)
**Owner**: Thiyagarajan Murugan, Suresh Kumar

- Update datastore cache to key on `connection_string + database_name`:
  ```java
  // Proposed fix
  private static final Map<String, IMongoDatastore> DATASTORE_BY_CONNECTION_AND_DB = Maps.newConcurrentMap();
  
  public static IMongoDatastore getDatastore(final MongoClient mongoClient, final String databaseName) {
      String cacheKey = mongoClient.getClusterDescription().getClusterSettings().getHosts() + ":" + databaseName;
      return DATASTORE_BY_CONNECTION_AND_DB.computeIfAbsent(cacheKey,
              key -> new MongoDatastore(mongoClient, getMapperOptions(), databaseName));
  }
  ```

- **Scope**: ~10 repositories require library version update
- **Risk mitigation**: Feature flag for safe rollback
- **Testing**: Verify in INT environment before STG retry

#### 3. Enhanced Validation
**New smoke tests**:
- ✅ Verify connection to ALL 3 clusters (not just one)
- ✅ Verify data distribution (each cluster contains expected collections)
- ✅ Verify read operations from ALL clusters (not just writes)
- ✅ Check collection counts match expectations per cluster

---

## Additional Architectural Improvements (Discussed)

### Connection Pool Optimization
**Problem**: Currently create separate MongoClients per logical database
- Leads to connection storms during DB issues
- Inefficient resource usage

**Proposed**: Single MongoClient per cluster (not per logical DB)
- Requires validation and performance testing
- **Decision**: Defer to post-migration optimization (too risky for migration window)

### Code vs. Infrastructure Trade-offs
**Option 1**: Rename databases only (no code change)
- Pro: Faster, less code risk
- Con: Doesn't fix underlying architectural issue

**Option 2**: Fix code only (keep same names)
- Pro: Fixes root cause
- Con: 10 repos to update, complex rollback

**Option 3**: Both fixes (chosen)
- Pro: Defense in depth, fixes root cause + infrastructure
- Con: More moving parts
- **Rationale**: Future-proofs for other scenarios, prevents recurrence

---

## Key Learnings

### What Went Well ✅
1. **Fast root cause identification** (< 1 hour from problem to RCA)
2. **Clean rollback procedure** (no data loss, quick recovery)
3. **Team collaboration** (cross-functional debugging across Slack)
4. **Post-incident transparency** (immediate analysis, no blame culture)

### What Could Be Improved 🔧
1. **Test environment parity**: STG testing should match PROD topology
2. **Validation coverage**: Need "read from all clusters" test
3. **Assumption documentation**: Document code assumptions about uniqueness
4. **Pre-flight checks**: Verify database names distinct before cutover
5. **Progressive rollout**: Consider single-cluster validation before 3-cluster split

### Process Improvements
- [ ] **Pre-migration checklist**: Add "verify distinct database names across clusters"
- [ ] **Smoke test enhancement**: Add multi-cluster read validation
- [ ] **Documentation**: Update runbooks with environment-specific considerations
- [ ] **Code review**: Flag cache keying strategies for uniqueness validation

---

## Related Incidents & Patterns

### Pattern: Environment Topology Differences
- This is not the first time DEV/STG differences caused production-bound issues
- **Action**: Review other areas where environment topology differs from PROD

### Pattern: Last-Minute Aborts
- Multiple aborts throughout this migration project (see: Event Bus surprises, Feb downgrade)
- Team resilience is high but emotional toll is real
- **Recognition needed**: Team persistence through adversity

---

## Action Items

### Immediate (Before June 3)
- [x] Root cause documented (this document)
- [ ] Code fix implemented and tested in INT
- [ ] Database names updated in Atlas
- [ ] MongoMirror re-sync with correct names
- [ ] Enhanced smoke tests implemented
- [ ] Runbook updated with lessons learned

### Post-Migration (June 3+)
- [ ] Retrospective with full team
- [ ] Share learnings with other migration projects
- [ ] Consider: Connection pool optimization (separate epic)
- [ ] Update migration playbook with environment parity requirements

---

## References

- Slack thread: #atlas_es_migration_coordination (May 29, 2026)
- Code: Search for `DATASTORE_BY_DATABASE_NAME` in CoreX codebase
- Related meetings: `/07-Archives/61 Meeting Notes/2026/Q1/` (Atlas migration planning)

---

**Incident closed**: May 29, 2026 (rollback complete)  
**Remediation in progress**: June 1-3, 2026  
**Retry scheduled**: June 3, 2026 (STG + PERF)
