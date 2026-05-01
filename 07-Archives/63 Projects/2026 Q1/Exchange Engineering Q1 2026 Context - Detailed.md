---
date: 2026-04-01
content_type: document
destination_category: 60-69 Archive
---
# Exchange Engineering Q1 2026 - Additional Context (Detailed)

## **Q1 Performance & Delivery Metrics**
- Completed 805 stories with a Say/Do ratio of 1.03 (indicating strong delivery against commitments)
- 40.4% (325 stories) were emergent work, reflecting significant unplanned demands
- Monthly performance varied: January impacted by holidays/planning (0.75 ratio), February and March strong (1.15 and 1.12 respectively)
- 12-month trend shows consistent story throughput with peak performance in September (441 stories, 1,136 points)

## **Database Migration & Performance Optimization**
- MongoDB to Atlas migration with custom Kafka-based rollback mechanism; Archive DB fully migrated and decommissioned
- Audit DB migration encountered significant issues requiring incident remediation, rollback, and full schedule replan
- BT/BD optimizations addressing December-January incidents: 9 of 16 business document replacements, 11 of 12 query optimizations completed
- AuditDB improvements: ConfigSVC poll duration reduced from 5 seconds to 1 minute, Activity Flow sharding plan initiated, COLLSCAN fixes implemented

## **New Capabilities & Critical Integrations**
- Feed Processor Observability: Net-new monitoring component with backend APIs and Heimdall UI for queue visibility, in-flight messages, and flow tracking
- Incident MCP: AI-powered PagerDuty incident automation that analyzes heap dumps and auto-resolves alerts without human intervention
- PEPPOL/Tickstar integration: Time-sensitive EU compliance project requiring third-party integration to meet regulatory deadlines
- RegCenter decoupling: Complete separation from monolith with new BFF/Gateway APIs, AuthN/AuthZ implementation, and Core UI migration
- Complex Order Automation (COA): Progress on Re-Park feature for Implants and new EDI actions for lot management

## **Infrastructure Modernization & CI/CD**
- Multiple services migrated to new CI/CD: Bitbucket→GitHub, Bamboo→GitHub Actions, EC2→Containers (Feed Processor, RegCenter)
- AWS SDK upgrade to 2.0: 4 of 6 repos completed (critical as 1.x reached EOL December 31, 2025)
- EC2 Linux 2023 upgrade: 19 repos completed, production release scheduled early April
- AI-assisted development and testing: RegCenter test coverage increased from 25% to 75%
- Additional tooling: Sonarqube integration, feature flag cleanup, Claude AI training and upskilling

## **Security & Technical Debt Resolution**
- Resolved 25 OSS vulnerabilities: 1 KEV (Known Exploited Vulnerability), 11 Critical, 13 High priority
- AWS SDK upgrade project addresses prerequisite for many vulnerability remediations
- QE improvements: 12% progress on Gold Certification Suite migration from Tandoori to Playwright (21 tests completed)
- Infrastructure architectural improvements: IO Guarantee SQS backup for Event Bus failures, DSemaphore migration to Redis to decouple from AuditDB

## **Team Growth & Organizational Investment**
- Significant recruiting effort: 15-20 engineers conducting interviews for ~40 open positions
- 120+ candidates moved through interview process (at minimum through Hiring Manager stage)
- Successfully onboarded 2 Engineering Managers and 2 Individual Contributors
- Customer Visibility UI upgrade to Core UI reached dev complete on Orders, Transactions, Notifications, and Web Direct modules
