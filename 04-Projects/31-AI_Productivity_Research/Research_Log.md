# Research Log

---

## 2026-05-15 — Initial Research Session

- **Searched:**
  - "GitHub Copilot enterprise productivity study metrics 2024 2025"
  - "McKinsey AI coding assistant developer productivity gains 2024 2025"
  - "Stack Overflow developer survey AI tools productivity 2024 2025"
  - "AI coding assistant enterprise rollout implementation best practices case study 2024 2025"
  - "Google Microsoft Meta Shopify AI coding productivity results engineering blog 2024 2025"
  - "DORA report 2025 AI developer productivity metrics findings Google"
  - "AI software engineering agents autonomous coding projections 2026 2027"
  - "Accenture GitHub Copilot randomized controlled trial productivity study methodology results"
  - "AI coding assistant risks security vulnerabilities code quality degradation skill atrophy 2024 2025"
  - "Shopify Stripe Netflix AI coding productivity engineering blog results 2024 2025"
  - "METR study AI experienced developers 19% slower 2025 autonomous tasks methodology"
  - "Anthropic agentic coding trends report 2026 findings"
  - "AI coding productivity enterprise regulated industries healthcare finance legacy systems challenges"

- **Found:**
  - 13+ sources covering current-state gains, future projections, implementation patterns, and company benchmarks
  - Key studies: GitHub/Accenture RCT, multi-company 26% gain study, Google internal RCT, METR RCT (19% SLOWER), McKinsey task-level speedups, DORA 2025, Stack Overflow 2025, Anthropic 2026 Agentic Coding Report, Veracode security findings

- **Added to:**
  - `Current_State_Findings.md` — 9 detailed study entries + patterns synthesis
  - `Future_State_Projections.md` — 7 projection entries + consensus view
  - `Implementation_Patterns.md` — rollout approach, training, measurement, 7 pitfalls
  - `Company_Benchmarks.md` — Accenture, Shopify, Stripe, Google, Microsoft, Healthcare aggregate

- **Quality Assessment:** Medium-High overall; sufficient RCT data for current-state claims; future projections directionally credible but timeline-uncertain

---

## 2026-05-15 — Second Research Session (Recent Data + Expert Opinion)

- **Context:** Expanded scope to include (1) more recent 2025–2026 data and (2) explicitly non-verified expert opinion sources, clearly labeled by reliability level. All entries now carry 🟢/🟡/🟠/🔴 reliability labels.

- **Searched:**
  - "AI coding agent productivity study results 2025 2026 agentic enterprise data"
  - "GitHub Copilot Cursor Claude coding productivity 2025 2026 longitudinal study enterprise results"
  - "software engineering AI productivity 10x claims CTO engineering leader opinion 2025 2026"
  - "AI replace software engineers 2026 2027 predictions thought leaders Sam Altman Dario Amodei"
  - "GitClear code quality churn AI generated code 2025 2026 study"
  - "Addy Osmani engineering manager AI productivity reality 2025 2026 observations"
  - "Pragmatic Engineer Gergely Orosz AI coding productivity impact developer jobs 2025 2026"
  - "AI coding 2026 developer hiring slowdown engineering headcount impact data"
  - "Dario Amodei virtual coworker AI software engineering 2025 prediction"
  - "vibe coding productivity agentic AI 2025 2026 reality versus hype"
  - "Jellyfish DX engineering management AI productivity survey 2025 2026"

- **New data-backed findings:**
  - GitClear 211M-line longitudinal analysis: code churn +44%, duplicates 8×, refactoring −60% (🟡 MEDIUM)
  - Jellyfish 2026 State of Engineering Management (636 leaders): 64% report 25%+ velocity gains, Claude Code now #1 tool (🟡 MEDIUM)
  - METR Feb 2026 follow-up: 19% slowdown reversed to ~18% speedup with newer models (🟢 HIGH)
  - Harvard workforce study: junior developer employment −9–10% within 6 quarters of AI adoption (🟡 MEDIUM)
  - CodeRabbit Dec 2025: AI code 1.7× more major issues, 75% more misconfigs (🟠 LOW)
  - Faros.ai 67,000-developer dataset: 2× incident divergence across organizations (🟠 LOW)

- **Expert opinions documented (all 🔴 OPINION):**
  - Dario Amodei (Davos Jan 2026): 6–12 month replacement prediction; "white collar bloodbath"
  - Sam Altman: 100× cost reduction by 2027; augment not replace
  - Andrej Karpathy: vibe coding → agentic engineering; 80% AI-generated personal code
  - Addy Osmani: 80% problem; orchestrator role; Google observations
  - Gergely Orosz: junior pipeline drought risk; token spend on performance reviews
  - Enterprise governance gap: shadow AI, IP leakage, comprehension debt

- **Added to:**
  - `Current_State_Findings.md` — Added reliability guide, Section A label, 5 new data-backed entries, full Section B (6 expert perspective entries), updated patterns
  - `Future_State_Projections.md` — Added reliability guide, Section A label, full Section B (5 speculative/opinion projections), updated consensus view
  - `Research_Log.md` — this entry

- **Quality assessment:**
  - New data additions: GitClear (🟡), Jellyfish 2026 (🟡), METR follow-up (🟢), Harvard study (🟡 secondhand), CodeRabbit (🟠), Faros.ai (🟠)
  - Expert opinions: all 🔴 — documented as non-verifiable but from credible sources
  - Overall confidence: **Medium-High** for current-state data; **Low-Medium** for forward projections; **qualitative only** for opinion section

- **Remaining gaps:**
  - arXiv/ACM peer-reviewed papers on developer productivity
  - ThoughtWorks Technology Radar assessment (not yet searched)
  - ROI/business case frameworks with cost inputs
  - GHX-specific comparables (enterprise B2B healthcare marketplace)
  - Longitudinal technical debt data beyond GitClear
  - QCon/StaffPlus conference presentations

---

*Next suggested search session: arXiv academic papers, ThoughtWorks Radar, and ROI/business case frameworks.*

---

## 2026-05-15 — Third Session: Scope & Measurement Methodology Analysis

- **Context:** No new external sources searched. Analytical session synthesizing existing research to address a key methodological gap: how AI productivity gains vary by scope of measurement (single task → full SDLC → business outcome).

- **Key analysis performed:**
  - Mapped SDLC phase effort allocation (8 phases) against AI gain evidence per phase
  - Calculated weighted SDLC-level productivity estimate (~+14%) vs. typical task-level claims (20–55%)
  - Quantified the "scope attenuation" effect: gains compress from ~35% at task level to ~8% at product/PDL level
  - Documented the "bottleneck shift" mechanism (Faros.ai: +98% PRs, +91% review time) that consumes upstream coding gains
  - Produced scope-level table with confidence assessments for 5 measurement scopes

- **Key finding:** The research corpus almost entirely measures at task or PR level. No peer-reviewed study measures AI productivity gains at the full SDLC or business-outcome level. The "productivity paradox" (high adoption, limited delivery velocity improvement) is consistent with a scope attenuation model where bottleneck shifts absorb coding speedups.

- **Added to:**
  - `Current_State_Findings.md` — New section: "The Scope Problem: Why Study Numbers Don't Translate Directly to Business ROI" (added between Patterns section and Section B). Includes: SDLC phase table, weighted estimate math, scope attenuation table, bottleneck shift analysis, GHX-specific implications.

- **Quality assessment:** Analytical synthesis — not new data. Confidence in the framing is medium-high (consistent with DORA, Faros.ai, and general systems thinking about bottlenecks); the specific phase effort percentages and AI gain estimates per phase are approximations, not measured values.

- **Remaining gaps (updated):**
  - arXiv/ACM peer-reviewed papers on developer productivity (not yet searched)
  - ThoughtWorks Technology Radar (not yet searched)
  - ROI/business case frameworks with cost inputs (license cost, training, time-to-productivity)
  - GHX-specific comparables: enterprise B2B healthcare marketplace, regulated SaaS
  - Longitudinal technical debt data beyond GitClear
  - QCon/StaffPlus conference presentations
  - **NEW GAP identified:** SDLC-level or business-outcome-level productivity studies — virtually none exist; if found, they would be high-priority additions

---

*Next suggested search session: arXiv/ACM academic papers + SDLC-level measurement studies + ROI frameworks.*

---

## 2026-05-19 — Fourth Session: 25x–100x Claim Research

- **Context:** Targeted research to validate or invalidate the executive narrative that AI enables "25x–100x faster product development." Focus on sources of these claims, evidence for/against, and translation problem from task-level to product-level.

- **Searched:**
  - "100x faster software development AI" / "25x AI productivity claims source"
  - "AI 10x software development productivity evidence data"
  - "vibe coding complete product built AI hours"
  - "AI 100x productivity claim false debunked evidence"
  - "AI task speedup vs product delivery speed bottleneck"
  - "a16z Marc Andreessen AI 10x developer"
  - "AI productivity gains 10 percent not 10x enterprise study"

- **Key new findings:**
  - DX 400-company study (135k developers): +7.76% median PR throughput despite +65% AI usage — explicitly titled "10%, not 10x" (🟡 MEDIUM)
  - Uplevel 800-developer study: zero gains + 41% more bugs (🟠 LOW — predates 2025 models)
  - O'Reilly "The Other 80%" — clearest published argument for scope attenuation (🟡 MEDIUM editorial)
  - California Management Review meta-analysis: no robust AI-productivity relationship (🟡 MEDIUM academic)
  - Marc Andreessen claims documented with conflict-of-interest context (a16z portfolio incentive)
  - Vibe coding origin (Karpathy Feb 2025) and limitations documented
  - METR arXiv paper confirmed: arxiv.org/abs/2507.09089

- **The 25x–100x verdict:**
  - At task level (best case): 1.55x–1.8x faster (55% gain = 1.55x)
  - At PR/team level (enterprise): 1.08x–1.26x
  - At SDLC level (estimated): ~1.15x
  - At product level (estimated): ~1.08x
  - **The 25x claim is unsupported by any rigorous study at any scope level.** The gap between claimed (25–100x) and evidenced (1.08–1.55x) is 15–65x. The claim cannot be validated against current evidence.

- **Added to:**
  - `Current_State_Findings.md` — 4 new entries: DX 400-company study, Uplevel study, O'Reilly "Other 80%", CMR Berkeley meta-analysis
  - `The_25x_100x_Question.md` — new dedicated file with full analysis

- **Quality assessment:** New additions range 🟡 MEDIUM to 🟠 LOW; the DX dataset is the most important new addition — largest real-world enterprise sample available.

---

*Research sufficient to build the focused report. Remaining gaps: arXiv peer-reviewed papers, ThoughtWorks Radar, ROI frameworks.*
