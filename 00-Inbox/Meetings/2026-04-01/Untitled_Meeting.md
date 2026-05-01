---
date: 2026-04-01
participants:
  - Mårten Engblom
companies: 
  - Untitled
tags:
  - meeting
meeting_type: general
source: granola
granola_id: eafae4ce-7dac-4f76-8224-a8b832efb92d
---

# Untitled Meeting

### Team Capability & Staffing Gap

- Current IPA team: mostly pure RPA developers hired for UiPath expertise

- Limited Python, minimal AWS/AI knowledge
- Bi-weekly training sessions underway (LLM basics, tokenization, RAG, agents, prompt engineering)
- Eswar is the only technically strong engineer; everyone else depends on him to build or deploy

- Need to develop a second technical lead to break this dependency
- Mohan identified as best candidate — experienced in UiPath, Python, AWS, still learning

### Staffing Strategy: Internal First, Not Contractors

- Strong preference to keep this project in-house rather than hand it to Happiest Minds

- Core rationale: this is a massive learning opportunity; giving it to contractors wastes that
- If HM is used, they should backfill other teams so internal engineers can move onto IPA 2.0
- CJ has approved an outcome-based engagement model with HM; they’ve submitted a two-option proposal
- Mårten’s challenge: if tasks are “routine,” use AI-assisted development (e.g., Claude Code) instead of contractors
- Action: Ramesh to think broadly — who across all of GHX would be ideal for this project?

- Internal transfers (even from Seth’s org or Daniel’s team) preferred over external contractors
- Spreading learnings by osmosis across GHX seen as a company-level win

### Platform Philosophy: Greenfield, Not Migration

- IPA 2.0 is a full redesign, not a like-for-like replacement of the 10+ year old UiPath system

- “Whatever we did in the last 10 years is gone” — build for the next 10
- Accuracy targets (99.5%+) apply to the final EDI output, not just extraction

- Extraction quality must be near-flawless; business rules output can use confidence scoring + human-in-the-loop as a short-term fallback
- Proposed parallel comparison system: CX agents compare new platform EDI output vs. UiPath/Firstsource output and flag logic flaws in business rules
- Short-term: Firstsource still available as backstop; long-term design must account for a world without it
- Reference model: Mårten’s brother’s team (CTO at Next Story) spent 5 weeks writing detailed markdown requirements, then built a working replacement system in 1 week using AI coding tools

### Next Steps

- Ramesh

- Identify engineers across GHX (including GHX India) who have the skills needed and initiate informal conversations with them or their managers
- Talk to Brian to explore whether his India team has capacity to contribute
- Begin developing Mohan as a second technical lead to reduce Eswar dependency
- Explore outcome-based HM engagement only if internal options fall short
- Mårten

- Connect with Brian if paths cross to ask about India team capacity
- Have conversation with CJ if needed to align on not giving core project work to contractors

Chat with meeting transcript: https://notes.granola.ai/t/9ebc1370-2cd7-4a21-a996-2d28201a8c4e

