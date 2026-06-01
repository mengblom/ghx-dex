---
title: MongoDB to Atlas Migration - Architecture & Design Decisions
last_updated: 2026-06-01
---

# Architecture & Design Decisions

## Database Splitting Strategy

### Why Split Databases?

**Original State**: Monolithic database clusters
- Single AuditDB containing all audit, community, mailbox, notification data
- Single BusinessTransaction DB containing all transaction, document, and metric data

**Problems with Monolithic Design**:
1. **Blast radius**: Failure in one workload affects all services
2. **Resource contention**: High-write workloads starve read-heavy workloads
3. **Scaling inefficiency**: Can't independently scale components
4. **Maintenance complexity**: All services down during maintenance
5. **Cost optimization**: Can't right-size clusters per workload

### Split Strategy: AuditDB (1 → 4 Clusters)

```
Before:                          After:
┌─────────────┐                 ┌──────────────┐
│  AuditDB    │                 │   Audit DB   │  (Audit logs, primary workload)
│             │                 └──────────────┘
│ - Audit     │────────────────▶┌──────────────┐
│ - Community │                 │ Community DB │  (User/org data, read-heavy)
│ - Mailbox   │                 └──────────────┘
│ - Notifs    │                 ┌──────────────┐
└─────────────┘                 │  Mailbox DB  │  (File storage, TTL-heavy)
                                └──────────────┘
                                ┌──────────────┐
                                │Notifications │  (Critical path, isolated)
                                └──────────────┘
```

**Rationale**:
- **Audit**: Core audit logging, largest volume
- **Community**: User/organization data, different access pattern
- **Mailbox**: File storage with TTL cleanup, high churn
- **Notifications**: Critical user alerts, needs isolation from audit log spikes

**Results** (Post-Migration, April 2026):
- ✅ Successful cutover with minimal issues
- ✅ Independent scaling per workload
- ✅ Notifications isolated from audit log storms
- ⚠️ TTL index timing differences noted (expected)

---

### Split Strategy: BusinessTransaction (1 → 3 Clusters)

```
Before:                          After:
┌─────────────────┐             ┌─────────────────────┐
│ BusinessTrans.  │             │ BT Cluster          │  (Transaction data)
│                 │             │ business-transaction│
│ - Transaction   │────────────▶└─────────────────────┘
│ - Document      │             ┌─────────────────────┐
│ - Metric        │             │ BD Cluster          │  (Document data)
└─────────────────┘             │ business-document   │
                                └─────────────────────┘
                                ┌─────────────────────┐
                                │ BM Cluster          │  (Metrics/analytics)
                                │ business-metric     │
                                └─────────────────────┘
```

**Workload Characteristics**:

| Cluster | Primary Workload | Collections | Access Pattern | Scaling Need |
|---------|-----------------|-------------|----------------|--------------|
| **BT** | Transaction processing | BusinessTransaction, Worklist, ActivityFlow | High write, time-series | Write-optimized |
| **BD** | Document storage | BusinessDocument, Tracking | High storage, mixed R/W | Storage-optimized |
| **BM** | Metrics & analytics | BusinessMetric, Statistics | Read-heavy, aggregations | Read-optimized |

**Rationale**:
- **Transactions (BT)**: High-volume writes, time-sensitive processing
- **Documents (BD)**: Large storage footprint, mixed access
- **Metrics (BM)**: Analytics queries, reporting workload

**Critical Requirement**: Database names MUST be distinct across clusters to avoid cache collision in application layer.

---

## Environment Topology

### Lower Environments (DEV, ATM, INT)
**Architecture**: Single cluster per database group
- Simpler deployment
- Lower cost
- Adequate for testing/development

**Trade-off**: Doesn't replicate production topology
- ⚠️ May mask issues that only appear in multi-cluster setups (e.g., May 29 incident)

### Production-Like Environments (STG, PERF, PROD)
**Architecture**: Multi-cluster split (matches production)
- STG: 3 clusters (BT, BD, BM)
- PERF: 3 clusters (for load testing)
- PROD: 3 clusters (production workload)

**Why This Matters**:
- STG must match PROD topology to catch production-class issues
- Performance testing requires production-like architecture

---

## Atlas Configuration Decisions

### Cluster Sizing

**Approach**: Right-size based on workload characteristics
- Start with self-hosted baseline performance metrics
- Adjust based on Atlas recommendations
- Monitor and tune post-migration

**Example (AuditDB)**:
- **Audit**: M40 tier (8GB RAM, 40GB storage) - high write volume
- **Community**: M30 tier (4GB RAM, 20GB storage) - read-heavy
- **Mailbox**: M30 tier with TTL optimization
- **Notifications**: M20 tier (isolated, lower volume)

### Replication & Availability

**Configuration**:
- 3-node replica sets (1 primary, 2 secondaries)
- Multi-region deployment (where applicable)
- Auto-failover enabled

**Read Preference**:
- **Current**: Primary (default for most applications)
- **Optimization opportunity**: Secondary for read-heavy workloads
  - Community DB: Already configured
  - Others: Post-migration optimization

### Backup & Recovery

**Atlas Managed Backups**:
- Continuous backup (point-in-time recovery)
- Daily snapshots retained per policy
- Cross-region backup storage

**Improvement over Self-Hosted**:
- Automated backup management
- Faster recovery (restore from Atlas)
- Better disaster recovery capabilities

---

## Application Architecture Considerations

### Connection Management

**Current Architecture** (Problematic):
```java
// Keys cache by database name only
Map<String, IMongoDatastore> DATASTORE_BY_DATABASE_NAME;

// Problem: Multiple clusters with same DB name collide
getDatastore(mongoClient, "business-transaction") // Which cluster?
```

**Fixed Architecture** (June 3 deployment):
```java
// Keys cache by connection string + database name
Map<String, IMongoDatastore> DATASTORE_BY_CONNECTION_AND_DB;

// Solution: Unique key per cluster + database
String cacheKey = connectionString + ":" + databaseName;
getDatastore(mongoClient, databaseName) // Unique per cluster
```

**Lesson**: Caching strategies must account for multi-cluster architectures.

---

### Connection Pooling

**Current State**: Separate MongoClient per logical database
- Even if on same physical cluster
- Leads to connection multiplication

**Example (Before)**:
```
Cluster: prod-bt-cluster
  ↳ MongoClient for "business-transaction" (pool size: 100)
  ↳ MongoClient for "cache-db" (pool size: 50)
  ↳ MongoClient for "config-db" (pool size: 50)
Total connections: 200 to same cluster
```

**Problem**: Connection storms during cluster issues
- Each client tries to reconnect independently
- Amplifies impact of transient failures

**Proposed Optimization** (Post-Migration):
```
Cluster: prod-bt-cluster
  ↳ Single MongoClient (pool size: 200)
    ↳ Access "business-transaction" database
    ↳ Access "cache-db" database
    ↳ Access "config-db" database
Total connections: 200 to cluster (shared pool)
```

**Benefits**:
- Better resource utilization
- Reduced connection storm impact
- Easier to monitor and tune

**Status**: Deferred to post-migration optimization (requires significant testing)

---

### Connection String Updates

**ConfigSvc Approach**:
- Centralized configuration service
- Connection strings stored as properties
- Applications fetch on startup/refresh

**Migration Process**:
1. Update ConfigSvc properties with Atlas connection strings
2. Execute instance refresh (or rolling restart)
3. Applications reconnect to Atlas
4. Verify connectivity across all services

**Automation**:
- Scripts created for bulk updates (~54 properties for BT/BD)
- Reduces human error and speeds cutover

---

## Migration Tooling

### MongoMirror

**Purpose**: Continuous data sync during cutover window

**How It Works**:
```
Self-Hosted ──────sync────────▶ Atlas
             [MongoMirror]
             
1. Initial bulk load
2. Continuous oplog tailing
3. Minimal lag (< 1 second)
4. Switch reads/writes to Atlas
5. Verify sync lag = 0
6. Disable MongoMirror
```

**Limitations**:
- Can't write to different database name (target must match source)
- ⚠️ This limitation contributed to May 29 incident (all syncs wrote to `business-transaction`)

**Solution for June 3**:
- Rename target databases in Atlas BEFORE starting MongoMirror
- Verify distinct names before sync begins

---

### Atlas Live Migration Service

**Purpose**: Initial bulk data transfer

**Used For**:
- Large database migrations
- Initial seeding before MongoMirror
- Lower environments (DEV, ATM)

**Benefits**:
- Managed by Atlas
- Parallel transfer optimization
- Minimal impact on source cluster

---

### Custom Validation Scripts

**Purpose**: Verify migration success

**Key Checks**:
1. **Collection count comparison** (Atlas vs. Self-Hosted)
   - Acceptable delta: < 5% or < 1M records
   - Document large discrepancies
2. **Index verification** (all indexes present)
3. **TTL index configuration** (matches self-hosted)
4. **Connection string validation** (all apps pointing to Atlas)
5. **Kafka connector health** (all connectors running)
6. **Multi-cluster read validation** (new for June 3)
   - Verify reads from ALL clusters, not just one

---

## Integration Points

### Kafka Connectors

**Purpose**: Stream MongoDB changes to Kafka topics

**Architecture**:
```
MongoDB (Atlas) ──────▶ Kafka Connect ──────▶ Kafka Topics
                    [Change Streams]
                    
- 22 connectors (PROD)
- 99 tasks total
- Real-time data streaming
```

**Migration Considerations**:
- Connection strings embedded in connector configs
- Must update before cutover
- Validate post-migration: All connectors green

**Health Check**:
```bash
Summary:
  Connectors: 22 total | 22 running | 0 paused | 0 failed
  Tasks: 99 total | 99 running | 0 failed
```

---

### Lambda Functions (EU/US Sync)

**Purpose**: Sync data between US and EU regions

**Affected Functions**:
- `corex-eu-odin-migration` (TrackedConfigFile)
- 14+ EU lambdas requiring connection string updates

**Migration Process**:
1. Update Lambda environment variables
2. Deploy updated code (if needed for Atlas connection format)
3. Test sync post-migration

**Validation**:
- Check last sync timestamp in DynamoDB
- Verify no errors in CloudWatch logs

---

### External Systems

**Known Dependencies**:
- **CDP load jobs**: Read-replica access for analytics pipelines
- **MS Portal**: Lambda functions accessing configsvc
- **Analytics**: Direct database queries

**Coordination**:
- Maintained dependency canvas (Philippe Scoffie)
- External team notifications before PROD cutover
- Post-cutover validation with each team

---

## Disaster Recovery Improvements

### Before (Self-Hosted)
- Manual backup scripts
- Recovery time: hours to days
- Limited point-in-time recovery
- Cross-region DR: Manual process

### After (Atlas)
- Continuous backup (automated)
- Point-in-time recovery (to any second)
- Cross-region backup storage (automatic)
- Faster recovery: minutes to hours
- Atlas-managed failover

**Strategic Alignment**: Supports GHX Disaster Recovery initiative

---

## Cost Optimization

### Compute Costs
- **Increase**: Database splitting (1→3, 1→4 clusters)
- **Savings**: Right-sized clusters vs. over-provisioned self-hosted
- **Net**: Positive ROI through managed service benefits

### Operational Savings
- Reduced DBA operational burden
- Automated patching and upgrades
- No hardware management
- Better monitoring/alerting out-of-box

### Storage Optimization
- Tiered storage (hot/cold data)
- Compression (automatic)
- TTL-based cleanup (automated)

---

## Security & Compliance

### Authentication
- Database users per application/service
- Role-based access control (RBAC)
- Connection string secrets management (ConfigSvc)

### Network Security
- VPC peering (Atlas ↔ GHX VPC)
- IP whitelisting
- TLS/SSL encryption in transit

### Audit Logging
- Atlas audit logs (database access)
- Application logs (query patterns)
- Change tracking (configuration changes)

---

## Monitoring & Observability

### Atlas Built-In
- Cluster metrics (CPU, memory, disk, IOPS)
- Slow query logs (automatic)
- Index usage recommendations
- Real-time performance insights

### GHX Monitoring
- **Graylog**: Application error logs
- **Heartbeat**: SLA monitoring
- **Event Bus metrics**: Backlog tracking
- **Custom dashboards**: Per-environment health

### Key Metrics to Watch
- Query response time (p50, p95, p99)
- Connection pool utilization
- Replication lag
- Disk space growth rate
- Backup success rate

---

## Lessons Learned (Architectural)

### 1. Environment Parity Matters
**Issue**: DEV/ATM single-cluster setup didn't reveal multi-cluster issues  
**Solution**: Maintain production-like topology in STG at minimum

### 2. Cache Keying Must Be Cluster-Aware
**Issue**: Database name alone insufficient key in multi-cluster architecture  
**Solution**: Key on `connection_string + database_name`

### 3. Validate the Full Path
**Issue**: Smoke tests checked "can write?" but not "can read from ALL clusters?"  
**Solution**: Enhanced validation covering all clusters

### 4. Document Assumptions
**Issue**: Implicit assumption that database names would be distinct  
**Solution**: Explicit validation + documentation of requirements

### 5. Infrastructure + Code Defense in Depth
**Issue**: Single point of failure (naming OR code caching)  
**Solution**: Fix both layers (distinct names AND smart caching)

---

## Future Optimizations (Post-Migration)

### Connection Pool Consolidation
- Single MongoClient per cluster
- Shared connection pool
- Requires: Performance validation, code refactoring

### Read Preference Optimization
- Route read-heavy queries to secondaries
- Requires: Query categorization, consistency analysis

### Sharding Strategy
- For largest collections (if needed)
- Requires: Workload analysis, shard key selection

### Multi-Region Deployment
- Active-active for global performance
- Requires: Conflict resolution strategy, latency analysis

---

**Last Updated**: June 1, 2026  
**Contributors**: Philippe Scoffie, Jeff Sherard, Suresh Kumar, Marten Engblom
