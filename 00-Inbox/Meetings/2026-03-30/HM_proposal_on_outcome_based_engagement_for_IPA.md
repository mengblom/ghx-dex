---
date: 2026-03-30
participants:
  - Mårten Engblom
companies: []
tags:
  - meeting
meeting_type: general
source: granola
granola_id: 5e607a30-aaa0-47f4-b186-04044db0e4ef
---

# HM proposal on outcome based engagement for IPA

### Happiest Minds Proposal Overview

- Fixed-fee outcome-based engagement for GHX’s in-house LLM development
- HM will deliver complete solution using Claude and latest AI tools
- GHX retains platform ownership and IP
- Tech guidance from GHX, delivery by HM team
- Production-grade engineering ready for first-time deployment

### Two Development Approaches

- **Approach 1**: Build core IDP capability from ground up

- 8-9 months timeline
- Complete GHX-specific implementation
- **Approach 2**: Leverage existing reusable components

- 6-7 months timeline
- 75-80% component reuse from HM’s existing platform
- Pre-built before GHX POC work

### Technical Architecture

- Three-layer system design:

1. **IDP Component Layer** (80% reusable)

- Document pre-processing and classification
- OCR/ICR extraction engine using hybrid LLM approach
- Multi-step validation framework (7 validation layers)
2. **Exchange System Integration**

- Orchestrates document flow
- Reuses existing adapters and business rules
- Leverages EDI transformation logic
3. **Human-in-the-Loop Interface**

- Visualization for app support team
- Feedback mechanism for continuous improvement

### Existing Capabilities & Accuracy

- Current touchless processing: 60%
- Field-level accuracy: 99.2-99.4%
- Multi-model processing approach
- 4-8 hours for LLM replacement/retraining
- MLOps process for continuous model improvement

### Team & Knowledge Transfer

- Chief architect: Money (familiar to GHX)
- Mix of known team members and new AI specialists
- Transparent development approach with code access
- Demo-driven development throughout project
- Claude Code agent for skill documentation and knowledge retention

### Timeline & Migration Considerations

- 6-7 months to Version 1.0 with 2-3 pilot customers
- Post-development migration timeline depends on:

- Business rules complexity per provider-supplier combination
- Customer document classification and processes
- Sequential UIPath retirement possible to reduce license costs
- Migration planning requires detailed customer complexity analysis

### Next Steps

- GHX internal discussions on approach selection
- HM team (Ramesh, Suresh, Money) to prepare detailed migration timeline
- Decision needed on ground-up vs. component reuse approach

Chat with meeting transcript: https://notes.granola.ai/t/b205e2f0-786b-4cbb-9c88-cd9021956f15

