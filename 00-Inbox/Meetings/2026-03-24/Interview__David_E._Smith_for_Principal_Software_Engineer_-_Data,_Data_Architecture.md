---
date: 2026-03-24
participants:
  - Mårten Engblom
companies: []
tags:
  - meeting
meeting_type: general
source: granola
granola_id: b94f6762-7631-437f-9dbb-f676eb7542ba
---

# Interview: David E. Smith for Principal Software Engineer - Data,  Data Architecture

### Candidate Background & Experience

- Data engineering consultant since 2019, running own company focused on data and AI
- Previous roles: CTO at Reclaim Health, tech lead/management positions
- Healthcare data platform experience (2016+)

- Built platform for pharmaceutical companies like Eli Lilly
- Processed high-velocity sensor data for clinical trials
- Wrapped Apache Spark before Databricks matured
- Major data migrations: legacy warehouses → lakehouse/Databricks

- SRAM bicycle manufacturing: consolidated ad-hoc reports with different “bike” definitions
- Standardized data models across use cases

### Technical Expertise & Database Selection Framework

- Database selection approach:

1. Analytical (OLAP) vs transactional needs
2. Response time requirements
3. Data structure variability
- Relational databases for well-defined business entities with low variability
- NoSQL (DynamoDB, MongoDB) for semi-structured, variable documents
- PostgreSQL preference: open source, AWS support, full SQL standard implementation
- Limited MongoDB experience, primarily uses DynamoDB for performance/auto-scaling

### Recent AI/ML Projects

- Healthcare cost prediction model

- Built feature computer accepting CSV/Excel rules from domain experts
- Scaled from small spreadsheet to ~400 features without workflow changes
- Enabled non-technical stakeholders to contribute without coding
- Multi-agent database interaction system

- Natural language to SQL queries for large schemas (hundreds of tables)
- Self-contained architecture for small educational company
- Built custom tracing/feedback collection (pre-modern orchestration tools)
- Databricks Genie integration with business workflow agents

### Role Discussion & Company Context

- New role filling gap between DBA and application engineering
- Company modernizing: pulling consultants/outsourcing in-house
- Heavy hiring across application teams (mix of new hires and 15-year veterans)
- Data science function exists separately, touches this role for data pipeline optimization
- Current challenges: MongoDB-heavy legacy architecture, Snowflake warehouse integration
- AI investment: unlimited cloud/tool access, multiple product POCs including document understanding

Chat with meeting transcript: https://notes.granola.ai/t/e63e7a84-9b0f-4aff-b065-f616f17dcdd9

