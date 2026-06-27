---
date: 2026-03-24
participants:
  - Mårten Engblom
companies: []
tags:
  - meeting
meeting_type: general
source: granola
granola_id: 17379bc9-e8a9-4c38-826e-7be581abd0f9
---

# Data architecture and engineering role interview with candidate

### Candidate Background & Experience

- 20 years in data field with major project experience

- Built customer hub for Bank of America
- Fixed BP incident data issues at IBM
- Monetized Schlumberger drilling data platform for oil industry sales
- Career progression: DBA → IBM Global Business Consultant → Data Architect

- Focus on data governance and quality-by-design principles
- Expertise in SQL (primary) and Python (6-7 years proficient)

### Technical Architecture Philosophy

- Semantic layer approach for scalability

- Universal data ingestion layer standardizes all sources
- Output formatting happens from semantic layer (XML, JSON, database sets)
- Operates at “speed of business vs speed of technology”
- Database selection criteria using 3 metrics:

1. Quality - validation rules, data steward accessibility, visualization ease
2. Speed - latency requirements, query patterns, operational complexity
3. Price - TCO including maintenance costs, existing investments

### Database & Performance Experience

- NoSQL experience at First Horizon Bank

- Used MongoDB API with Cosmos DB to avoid vendor lock-in
- Maintained portability while leveraging existing Azure investment
- No performance degradation through connector approach
- Performance tuning approach varies by environment:

- Traditional RDBMS: indexes, execution plans, user query pattern analysis
- Big data: partitioning strategy, sharding, preventing full table scans
- Caching: Redis implementation for similar/repeated queries
- Database type selection factors:

- Structured data + varied queries → traditional RDBMS
- Unstructured + latency concerns → NoSQL
- Extremely large datasets → vector databases
- File format considerations (Parquet, ORC) based on query types

### Cross-Team Influence & Collaboration

- Alignment-focused approach without direct authority

- Understand competing objectives across teams
- Find commonality in manager priorities
- Decision framework presentation:

- Quality vs speed vs price trade-offs
- TCO and operational maintenance impact
- Collaborative rather than dictatorial approach
- Communication strategy:

1. Share motivation behind decisions (not just directives) with peers
2. Align with leadership objectives and priorities
3. Create visual trade-off documentation for informed decisions

### Role Requirements & Company Challenges

- Gap between database administration and application development

- Storage type selection based on use cases
- Data modeling for application vs storage optimization
- Multiple storage needs (querying vs syndication)
- Modernization challenges:

- Break monolithic dependencies for autonomous teams
- Multi-year microservices migration while maintaining operations
- Technical debt vs new architecture balance per project
- Define target state architecture for incremental progress

Chat with meeting transcript: https://notes.granola.ai/t/ec27b6d3-ef4e-4002-b492-eac5d71eb9d2

