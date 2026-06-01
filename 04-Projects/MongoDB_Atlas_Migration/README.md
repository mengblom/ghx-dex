---
project_name: MongoDB to Atlas Migration
status: in_progress
priority: critical
start_date: 2026-02-27
target_completion: 2026-08-29
project_lead: Philippe Scoffie
executive_sponsor: Curtis Nielsen
visibility: executive
tags:
  - infrastructure
  - database
  - migration
  - Atlas
  - MongoDB
  - critical-technical-execution
related_projects:
  - Disaster_Recovery
  - Red_Mythos_Vulnerabilities
---

# MongoDB to Atlas Migration

**One of GHX's "Big 4" strategic technical initiatives alongside Red Mythos, Disaster Recovery, and Breaking the Monolith.**

## Executive Summary

Migrating GHX's self-hosted MongoDB databases to MongoDB Atlas (managed cloud service). This multi-month effort involves migrating multiple database clusters across all environments with zero data loss and minimal downtime.

**Why it matters:**
- **Cost savings**: Significant infrastructure cost reduction through managed services
- **Operational excellence**: Reduce operational burden on DBA team
- **Resilience**: Improved disaster recovery and high availability
- **Performance**: Better monitoring, alerting, and optimization capabilities
- **Security**: Enhanced security features and compliance

## Current Status (As of June 1, 2026)

### Completed ✅
- **AuditDB Migration** (EU & US PROD) - April 19-20, 2026
  - Split from 1 cluster → 4 separate clusters (Audit, Community, Mailbox, Notifications)
  - Successful cutover with minimal issues
  - Post-migration monitoring looks good
- **DEV/ATM environments** - Multiple databases migrated
- **Elastic Search to Elastic Cloud** - DEV environment migrated (April 21)

### In Progress 🔄
- **BusinessTransaction (BT), BusinessDocument (BD), BusinessMetric (BM)** - STG/PERF/PROD
  - **Friday May 29 STG attempt: FAILED & ROLLED BACK** (see Incidents)
  - Root cause identified, fix in progress
  - Retry scheduled for Wednesday, June 3, 2026

### Upcoming 📅
- **Performance (PERF) environment** - Scheduled with STG
- **Production (PROD)** - Final cutover (target Aug 2026)
- **RDS/Aurora migration** - June 3, 2026 in PERF

## Key Stakeholders

### Technical Leadership
- **[[Philippe_Scoffie]]** - Project Lead, Migration Coordinator
- **[[Jeff_Sherard]]** - Principal DBA, Database Architecture
- **[[Suresh_Kumar]]** - Senior IC, Application Architecture & Code Changes
- **[[Daniel_Milburn]]** - Engineering Manager, Oversight & Coordination

### Execution Team
- **[[Thiyagarajan_Murugan]]** - Lead Engineer, Migration Execution
- **[[Ben_Ludkiewicz]]** - DBA, Migration Support & Monitoring
- **[[Sean_Kotze]]** - DBA, Cutover Execution
- **[[Naidu_Dasari_Demudu]]** - DBA, Infrastructure Setup

### Performance & Testing
- **[[Selvakumar_Samiappan]]** - Performance Testing Lead
- **[[Mathivarma_Ganesan]]** - Performance Analysis
- **[[Arivazhagan_Jeganathan]]** - Monitoring & Validation

### Executive Oversight
- **[[Curtis_Nielsen]]** - VP Engineering, Executive Sponsor
- **CJ Singh** - CTO, Strategic Oversight
- **[[Arshad_Mahammad]]** - Infrastructure VP

## Project Scope

### Databases in Scope
1. **AuditDB** ✅ (Complete)
   - Audit
   - Community
   - Mailbox
   - Notifications (split from Audit)

2. **BusinessTransaction (BT)** 🔄 (In Progress)
   - Split into 3 clusters in STG/PERF/PROD
   - BT Cluster (BusinessTransaction collections)
   - BD Cluster (BusinessDocument collections)
   - BM Cluster (BusinessMetric collections)

3. **Elasticsearch** 🔄 (In Progress)
   - ActivityFlow (AF)
   - BusinessTransaction (BT)
   - Combined into 1 cluster in DEV

### Environments (Migration Order)
1. DEV ✅
2. ATM ✅
3. INT 🔄
4. STG 🔄 (retry June 3)
5. PERF 🔄 (scheduled June 3)
6. EU-PROD 📅
7. US-PROD 📅

## Architecture Decisions

### Database Splitting Strategy

**AuditDB** (1 → 4 clusters):
- Reduced blast radius for failures
- Independent scaling per workload
- Separated critical services (Notifications) from general audit logs

**BusinessTransaction** (1 → 3 clusters):
- Transaction data (BT) - high write volume
- Document data (BD) - high storage needs
- Metrics data (BM) - analytics workload

### Migration Tooling
- **MongoDB Atlas Live Migration** - For initial bulk data sync
- **MongoMirror** - For continuous replication during cutover window
- **Custom scripts** - ConfigSvc updates, connection string changes, validation

## Timeline & Milestones

### Q1 2026 - Planning & Prep
- **Feb 26-27**: Audit DB initial attempt (downgraded/rolled back)
- **Mar 2-12**: Schedule review, gap analysis, MongoDB support engagement
- **Mar 25**: Executive review with Curtis/CJ - confirmed no opportunity to shorten timeline

### Q2 2026 - Execution Phase 1
- **Apr 19-20**: ✅ AuditDB EU & US PROD cutover (SUCCESS)
- **Apr 21**: ✅ DEV Elastic Search to Elastic Cloud
- **Apr 23**: Lambda updates for EU/US sync
- **May 12**: ✅ ATM BT cutover
- **May 14**: ✅ DEV/ATM BT Atlas migration complete
- **May 20-29**: STG/PERF prep, code deployment, MongoMirror sync
- **May 29**: ❌ STG BT cutover attempt (FAILED - see Incidents)
- **Jun 1**: Root cause analysis, fix planning

### Q2 2026 - Execution Phase 2 (Upcoming)
- **Jun 3**: STG + PERF BT/BD cutover (retry)
- **Jun 3**: PERF Aurora migration
- **Jun 4**: PERF testing for Aurora
- **June-July**: Remaining environments
- **Aug 29**: Target completion (all environments)

## Communication & Coordination

### Slack Channels
- **#atlas_es_migration_coordination** (C096QQS0JUV) - Primary coordination channel
- **#help-database** - User-facing support

### Status Updates
- **Hourly monitoring** during cutover windows
- **Daily standups** during active migration periods
- **Executive updates** to Curtis/CJ weekly
- **Customer communications** for production cutovers

### Meeting Cadence
- Migration planning sessions (ad-hoc)
- Performance testing reviews
- Post-migration retrospectives

## Technical Details

See:
- [Architecture & Database Split Strategy](Architecture.md)
- [Migration Runbooks](Runbooks/)
- [Incidents & Learnings](Incidents/)
- [Risk Register](Risk_Register.md)

## Success Metrics

### Migration Success Criteria
- ✅ Zero data loss
- ✅ Downtime < planned maintenance window
- ✅ All applications connecting to Atlas post-cutover
- ✅ Performance within acceptable thresholds
- ✅ Kafka connectors operational
- ✅ Event bus/data poller backlogs normal

### Post-Migration Health Indicators
- Heartbeat SLA compliance
- Event bus backlog < 100 events
- Data poller backlog < 50 events
- No database-related errors in Graylog
- Kafka connector success rate > 99%
- Query performance within 10% of baseline

## Budget & Cost
- **Cost savings target**: Significant reduction vs. self-hosted infrastructure
- **Additional compute costs**: From database splitting (1→3 clusters, 1→4 clusters)
- **Migration costs**: MongoDB Atlas Professional Services, temporary parallel infrastructure

## Risks & Mitigation

See [Risk Register](Risk_Register.md) for detailed analysis.

**Top Risks:**
1. **Database naming conflicts** - CRITICAL (occurred on May 29)
2. **Performance degradation** post-migration
3. **Extended cutover windows** affecting customer SLAs
4. **Code compatibility** issues with Atlas-specific features
5. **Data sync lag** during high-volume periods

## Related Documentation

- [May 29 STG Incident - Database Naming Conflict](Incidents/2026-05-29_STG_BT_Migration_Failure.md)
- [Post-Incident Analysis](Incidents/2026-05-29_Post_Incident_Analysis.md)
- Meeting notes in `/07-Archives/61 Meeting Notes/2026/Q1/` (search: Atlas, MongoDB, Migration)
- Executive updates in `/07-Archives/64 Correspondence/2026/`

## Project Team Recognition

Special recognition to the team for **persistence through multiple challenges**:
- Multiple leadership changes
- Last-minute aborts and schedule changes  
- Event Bus surprises
- Complex technical challenges (12th hour debugging)

*"This project has been a lot like Frodo journeying to Mount Doom to destroy the one ring"* - Daniel Milburn

---

**Last Updated**: June 1, 2026
**Next Review**: June 3, 2026 (post-retry)
