---
date: 2026-04-28
participants:
  - Mårten Engblom
  - Vincent (Observe)
  - Caitlin (Observe)
companies:
  - Observe
tags:
  - observability
  - tools-evaluation
  - vendor-demo
  - infrastructure
meeting_type: vendor-demo
source: granola
granola_id: 9fd1f3be-8e8b-42ae-9838-b47272a12490
---

# Observability Tools Exploration with Observe Platform

## Meeting Context

Exploratory call (no agenda) - Caitlin from Observe reached out. GHX has existing toolchain but interested in hearing about alternatives. No immediate plans to change tools, but always interested in latest technology.

## Observe Platform Overview

AI-powered observability platform addressing modern application monitoring challenges.

### Key Architecture Differentiators
- Built on **Snowflake architecture** with decoupled storage/compute
- **No index-based limitations** like traditional tools (DataDog, New Relic, Splunk)
- Scales without throttling or overages
- **Single query language (OPAL)** with AI natural language interface
- **Knowledge graph** automatically establishes relationships between telemetry data
- 80-90% pre-built connectors for standard infrastructure
- 10-20% customizable for business-specific data (CRM, support tickets, CI/CD)

### Cost Model
- Two SKUs: **ingest** and **compute** (not separate for logs/metrics/traces)
- No overages in billing model
- No concept of "indexed vs ingested" - 100% of ingested data is accessible
- Storage/compute decoupled - retention doesn't drive compute costs
- Example: Capital One moved off ELK + Splunk + DataDog + New Relic → all to Observe

## Current GHX Observability Stack

- **New Relic:** APM, metrics, infrastructure monitoring (single pane of glass)
- **Gray Log:** log management
- **Grafana:** some visualization
- **Migration planned:** New Relic → Prometheus/Grafana stack (org-wide initiative)
- **Retention:** ~30 days
- **Pain point:** Multiple tools create correlation gaps, manual troubleshooting across systems

## Technical Context & Pain Points

### Monolith-to-Microservices Transformation
- Beginning journey to break apart monolithic codebase
- Increased observability demands as architecture breaks apart
- "Getting away with murder" currently due to monolithic structure
- Team has **DataDog experience**, recognizes current tooling gaps

### Snowflake Relationship
- GHX is Snowflake customer but limited ownership
- Systems feed into common data platform
- Don't own infrastructure, just facilitate pipelines

### Bandwidth Constraints
- **Limited bandwidth for major tooling changes currently**
- Need to understand feature parity - can't afford gaps vs DataDog experience
- "We have bigger fish to fry" - if tooling gaps exist, it's a blocker

## Key Technical Questions Raised

1. **Feature parity vs DataDog** - Need clear understanding of:
   - Data stream monitoring
   - Real user monitoring (RUM)
   - Other DataDog features not explicitly listed on Observe website

2. **Filtering/indexing strategy** - How to handle junk logs?
   - Observe approach: Filter at OpenTelemetry collector OR drop filter in Observe
   - Future: AI recommendations on unused/low-value log streams

3. **Query language** - OPAL (Splunk derivative)
   - Builder mode (dropdown-based)
   - AI natural language mode (primary usage)
   - Direct OPAL queries (power users)

## Outcome & Next Steps

- **No immediate timeline** - no New Relic renewal pressure
- **Follow-up in 3-4 weeks** when team has bandwidth for deeper evaluation
- **Vincent to provide:**
  - Feature comparison materials (Observe capabilities vs traditional tools)
  - Cost modeling examples
  - Demo scheduling when ready
- **Internal work needed:**
  - Sort out fundamental pieces and empower teams
  - Define observability journey roadmap
  - Check with "powers that be" on tool direction

## Observability Journey Context

- Need to address tooling **before** microservices complexity increases
- Historical lesson: "went to service-oriented architecture without doing any of this stuff and that becomes very painful very quickly"
- Hard to retrofit after the fact
- Currently "getting away with murder" due to monolith - won't hold long-term

## Links

- [Granola transcript](https://notes.granola.ai/t/7c7658b1-689c-4697-8ea5-5e93997ef7c2)
