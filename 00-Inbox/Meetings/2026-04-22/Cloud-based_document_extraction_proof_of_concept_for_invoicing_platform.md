---
date: 2026-04-22
participants:
  - Mårten Engblom
companies: 
  - Cloud
tags:
  - meeting
meeting_type: general
source: granola
granola_id: bfc3d25d-fb6e-4d46-8af1-26fec3dca3ac
---

# Cloud-based document extraction proof of concept for invoicing platform

### POC Results & System Architecture

- Cloud-based LLM solution completed in 2 weeks vs 4-5 months for previous systems
- Architecture uses AWS S3, Haiku model for classification, Sonnet for extraction
- Success metrics achieved:

- Classification accuracy >90%
- Extraction touchless rate >50%
- Mandatory field accuracy 98%, other fields 95%
- Processing time <15 seconds classification, <30 seconds extraction
- Manual validation on 26-30 documents showed 100% accuracy

- No human corrections needed during testing
- Sample size may have been limited to system-generated PDFs

### Technical Implementation Details

- Extracts 50+ fields from purchase orders and invoices
- Confidence scoring system built into API responses

- 0.95-0.99 for clearly visible fields
- Color coding: red <70%, orange 70-90%, green >90%
- Human-in-the-loop interface for corrections and retraining

- Visual highlighting shows extraction source locations
- Manual corrections feed back into learning database
- Basic validation includes math checks and mandatory field verification

### Current Limitations & Scope Gaps

- POC excluded scanned PDF documents (only system-generated)
- No post-processing logic (account lookup, invoice smoothing)
- No data feed handling or process automation
- Customer Requirements Documents (CRDs) not integrated

- Currently stored in spreadsheets, need database migration
- Per-customer extraction rules not applied
- Volume testing limited to small hardware setup

### Post-Processing Requirements Discussion

- CRDs contain customer-specific extraction and processing rules

- Different customers require different field mappings
- Rules change monthly, need dynamic reference system
- Current UI Path system has extraction/post-processing tightly coupled
- Need separation of extraction engine from business rules application
- Proposed solution: Move CRD rules from spreadsheets to queryable database

- Enable API-based rule retrieval
- Support deterministic processing vs non-deterministic LLM approach

### Next Steps

- Expanded POC requirements from invoicing team:

- Test larger volume (targeting 10% of monthly 500K documents)
- Cross-section of 50+ document types across customer base
- Include handwritten invoices and non-standard formats
- Compare extraction output to current system results
- Technical architecture planning needed:

- Separate extraction from post-processing systems
- Design CRD database structure and APIs
- Plan incremental migration approach
- Schedule follow-up meeting to discuss CRD workaround implementation

- Focus on creating structured database from current spreadsheets
- Define scope for reference table creation and testing approach

Chat with meeting transcript: https://notes.granola.ai/t/2e49e577-4fc7-450a-a5c8-e7846b278598

