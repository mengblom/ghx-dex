# Future State: Credible Projections (12-24 months)

---

## Source Reliability Guide

| Label | Meaning |
|---|---|
| 🟢 **HIGH — Data-Grounded** | Projection backed by longitudinal data, large-scale surveys, or RCT follow-up. Best basis for planning assumptions. |
| 🟡 **MEDIUM — Survey / Trend Extrapolation** | Based on survey data or documented trends, but projecting forward involves assumptions. Reasonable for directional planning. |
| 🟠 **LOW — Vendor / Advocacy Source** | From a company with commercial interest in the projection being true. May directionally reflect reality but treat numbers skeptically. |
| 🔴 **OPINION — Leadership Assertion** | Executive statements, personal predictions, or thought leader forecasts. No underlying data. Useful for understanding the range of credible beliefs; not planning inputs. |

---

## Summary

The shift from AI *assistants* (autocomplete, chat) to AI *agents* (autonomous multi-step task execution) is already underway in 2026 and will accelerate through 2027. Credible industry sources — including Anthropic's own data, Google's DORA research, and major tech company disclosures — project that development cycle times will compress from weeks to days, that AI will handle increasingly large portions of routine implementation work, and that engineer roles will shift from writing code toward orchestrating, reviewing, and directing AI systems. However, significant uncertainty remains about the pace of improvement for complex, legacy-system work in regulated industries, and about whether throughput gains will translate to measurable business outcomes.

---

# SECTION A: Data-Grounded Projections

---

## Projections by Source

### Anthropic: 2026 Agentic Coding Trends Report 🟡 MEDIUM
- **Source:** [2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report)
- **Date:** 2026-Q1
- **Projection:** Eight trends reshaping software engineering in 2026–2027:
  1. Engineer role shifts from *implementer* to *orchestrator*
  2. Development cycles compress from weeks/months to hours/days
  3. Multi-agent systems (parallel agents in coordinated teams) replace single-agent workflows
  4. Long-running agents (task horizons: days to weeks, not minutes)
  5. Agentic coding expands to non-developers (security, design, operations teams)
  6. Legacy language support (COBOL, Fortran) grows — relevant for enterprise
  7. **27% of AI-assisted work consists of tasks that wouldn't have been done otherwise** — net new capacity, not just faster execution
  8. "Delegation gap" as headline metric: engineers use AI in 60% of their work but fully delegate only 0–20%
- **Timeline:** Current through 2027
- **Evidence:** Draws on case studies from Rakuten, CRED, TELUS, Zapier, Legora, Fountain, Augment Code
- **Dependencies:** Organizations need agent governance, review processes for autonomous work, and updated security practices
- **Confidence:** Moderate-high directionally; Anthropic has direct visibility into Claude production usage — but note their commercial incentive to project growth

---

### Google / DORA 2026: Engineering Foundations Drive AI ROI 🟢 HIGH — Data-Grounded
- **Source:** [New DORA Report: Strong Engineering Foundations Drive AI ROI (InfoQ, May 2026)](https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/)
- **Date:** 2026-05
- **Projection:** Organizations with mature engineering foundations — strong internal platforms, good CI/CD, quality practices — will see compounding returns on AI investment. Organizations without these foundations will see AI adoption *increase* workload (more PRs, more review burden) without proportional value.
- **Timeline:** Now through 2027
- **Evidence:** Longitudinal DORA data; seven AI capabilities model shows direct correlation between platform quality and AI ROI
- **Dependencies:** Internal developer platform investment is a prerequisite, not a nice-to-have
- **Confidence:** High; DORA is the most rigorous longitudinal dataset in software delivery performance

---

### GitHub: AI Code Share Growing Toward Majority 🟡 MEDIUM
- **Source:** [GitHub Copilot Statistics 2026](https://www.getpanto.ai/blog/github-copilot-statistics)
- **Date:** 2025-2026
- **Projection:** AI-generated code will continue growing from ~46% (2025) toward majority in enterprise settings. Trajectory suggests 50–60%+ by end of 2026 for heavy Copilot users.
- **Timeline:** 12–18 months
- **Evidence:** GitHub telemetry showing 46% of code written with AI assistance; Google and Microsoft both reporting 30%+ of new code is AI-generated
- **Dependencies:** Continued tool improvement; developer trust recovery (currently declining per Stack Overflow)
- **Confidence:** Moderate; adoption trend is clear, but trust issues may create headwinds

---

### Agentic Coding: 30–50% Reduction in Manual Coding Time (Emerging Capability) 🟠 LOW
- **Source:** [The State of AI Coding Agents (2026) — Medium](https://medium.com/@dave-patten/the-state-of-ai-coding-agents-2026-from-pair-programming-to-autonomous-ai-teams-b11f2b39232a); [How Agentic AI Will Reshape Engineering Workflows in 2026 — CIO](https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html)
- **Date:** 2026
- **Projection:** Agentic workflows projected to reduce manual coding time by 30–50% on appropriate task types (bug fixes, test generation, documentation, routine features) on top of current copilot-style gains.
- **Timeline:** 12–24 months for broad enterprise adoption
- **Evidence:** Early deployments at Stripe (Minions) and Shopify (Roast) are operational; task completion quality improving rapidly
- **Dependencies:** Mature codebases with good test coverage; human review of agent output; agent governance frameworks
- **Confidence:** Low-moderate; enterprise-scale agentic deployment is nascent; results extrapolated from limited production data

---

### METR Follow-Up: AI Impact Improving with Newer Models 🟢 HIGH — RCT
- **Source:** [We Are Changing Our Developer Productivity Experiment Design — METR](https://metr.org/blog/2026-02-24-uplift-update/)
- **Date:** 2026-02
- **Projection:** Continued model improvement will shift the productivity curve for experienced developers doing complex work. The METR follow-up reversed the July 2025 slowdown in ~6–9 months, suggesting the ceiling is moving at roughly that pace.
- **Timeline:** Ongoing; reassess every 6 months
- **Evidence:** Repeat RCT with same methodology and developers; shift from 19% slowdown to 18% speedup
- **Dependencies:** Continued model capability improvement; developer skill in working with agents
- **Confidence:** Moderate-high for the direction; small sample limits precision

---

### Regulated Industries: Slower Curve, Different Shape 🟡 MEDIUM
- **Source:** [How Enterprise Teams Evaluate AI Code Assistants for Regulated Environments](https://www.sanciti.ai/blog/how-enterprise-teams-evaluate-an-ai-code-assistant-for-regulated-environments/); [Accenture + Anthropic Partnership for Regulated Industries](https://newsroom.accenture.com/news/2025/accenture-and-anthropic-launch-multi-year-partnership-to-drive-enterprise-ai-innovation-and-value-across-industries)
- **Date:** 2025
- **Projection:** Healthcare and financial services will capture AI productivity gains 12–24 months behind consumer technology companies, constrained by compliance requirements, audit trail needs, and legacy system complexity.
- **Timeline:** 18–36 months for full enterprise-scale deployment in regulated sectors
- **Evidence:** Current AI success rates in regulated workflows: 22.7% on complex multi-system workflows; Copilot misinterprets complex business requirements in 58.3% of cases in regulated contexts
- **Dependencies:** Compliance-aware AI tooling; audit trail capabilities; privacy-preserving model deployment
- **Confidence:** Moderate; directionally clear, timeline uncertain

---

## Consensus View (Data-Grounded Section)

**What most credible sources agree on:**

The direction is unambiguous — AI's role in software development is expanding rapidly, developer roles are shifting toward orchestration, and throughput metrics (code volume, PR velocity) will continue to increase. DORA 2026 confirms the prerequisites: platform maturity, not just AI tool access, is what separates organizations that capture value from those that don't.

**Where opinions diverge:**

The key disagreement is whether throughput gains translate to *business value*. The "productivity paradox" — 90%+ AI adoption but limited improvement in delivery velocity or outcomes — is documented in multiple sources. Outcome variance is increasing, not converging.

**Reasonable planning assumptions for GHX (enterprise healthcare SaaS, regulated, legacy systems):**

- **Near-term (6–12 months):** 15–25% productivity gains on appropriate task types (documentation, greenfield feature work, test generation) with well-trained developers and proper tooling. Lower on legacy system maintenance and compliance-heavy workflows.
- **Medium-term (12–24 months):** Agentic workflows will mature; ability to delegate discrete well-scoped work (bug fixes, routine features, test suites) to AI agents with human review. Potential for 10–20% incremental capacity on top of copilot-style gains.
- **Key prerequisite:** Internal developer platform quality, test coverage maturity, and training investment are stronger predictors of AI ROI than tool selection.
- **Key risk:** Security vulnerability rates will increase without active countermeasures; governance gap is a real compliance exposure.

---

# SECTION B: Speculative & Opinion-Based Projections

*These projections come from executives, prominent practitioners, or analysts whose assertions are not directly supported by disclosed empirical data. They represent the range of credible beliefs among well-informed people — not planning inputs. Read as: "this is what thoughtful people think might happen," not "this is what the evidence says will happen."*

---

### Dario Amodei: Software Engineering Replaced in 6–12 Months 🔴 OPINION
- **Source:** [Anthropic CEO Predicts AI Models Will Replace Software Engineers](https://finance.yahoo.com/news/anthropic-ceo-predicts-ai-models-233113047.html)
- **Stated at:** World Economic Forum, January 2026
- **Claim:** AI models could take over most or all tasks currently performed by software engineers within 6–12 months (i.e., by mid-to-late 2026).
- **Track record:** Similar 2025 prediction ("90% of code within 3–6 months") did not materialize on schedule. IT Pro explicitly documented this gap.
- **Credibility factors FOR:** Amodei has unparalleled visibility into frontier model capability trajectories. The engineers-who-no-longer-write-code anecdote reflects real behavior at AI-native companies.
- **Credibility factors AGAINST:** Strong commercial incentive. Anthropic's engineering culture is an extreme-case context. Enterprise software development (legacy systems, compliance, distributed teams) is structurally different from AI-native greenfield development.
- **Planning implication:** Even at 20% probability, a shift this significant warrants scenario planning. The more conservative planning assumption: *roles will transform substantially* within 2–3 years, not 6 months.

---

### Sam Altman: 100× Reduction in Cost of Intelligence by End of 2027 🔴 OPINION
- **Source:** [OpenAI's Sam Altman Claims AI Will 'Gradually' Replace Software Engineers — Windows Central](https://www.windowscentral.com/software-apps/openai-sam-altman-ai-will-gradually-replace-software-engineers)
- **Claim:** The cost of intelligence will drop by approximately 100× by end of 2027, fundamentally changing the ROI math for AI-assisted development.
- **Credibility factors FOR:** Cost-of-compute has followed rapid decline curves historically; frontier model pricing has already fallen ~30–50× since 2023; trend is real even if the exact multiple is uncertain.
- **Credibility factors AGAINST:** "100×" is a specific and extraordinary claim with no cited methodology. Altman simultaneously argues for augmentation and displacement, introducing interpretive inconsistency.
- **Planning implication:** If cost of AI compute falls even 10–20× (let alone 100×), license costs — currently the primary barrier to broad deployment — become negligible. ROI calculus improves significantly within the planning horizon.

---

### Addy Osmani: The "Orchestrator" Role Becomes the Core Job in 2 Years 🔴 OPINION
- **Source:** [The Next Two Years of Software Engineering — addyosmani.com](https://addyosmani.com/blog/next-two-years/); [The AI-Native Software Engineer](https://addyo.substack.com/p/the-ai-native-software-engineer)
- **Claim:** Within two years (~2027–2028), the dominant mode of software engineering will be orchestration — defining intent, evaluating AI output, and maintaining architectural coherence — rather than line-by-line implementation. Developers who can "think in systems" will be more valuable than those with narrow implementation skills.
- **Credibility factors FOR:** Consistent with DORA amplification data; Anthropic agentic trends report; Osmani observes this across Google's large engineering org.
- **Credibility factors AGAINST:** Timeline is speculative — this is a direction of travel, not a measured rate of change. The transition could take 5 years, not 2.
- **Planning implication:** Hiring and training should already be shifting toward systems thinking, AI prompt engineering, and code review depth — reweighting toward judgment over production, without abandoning coding skill entirely.

---

### Gergely Orosz: Junior Developer Drought in 2028–2030 🔴 OPINION
- **Source:** [When AI Writes Almost All Code, What Happens to Software Engineering?](https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what)
- **Claim:** Organizations quietly cutting junior developer hiring today will face a supply crisis of experienced mid-level engineers in 3–5 years. AI cannot replace the apprenticeship pipeline that turns juniors into seniors.
- **Credibility factors FOR:** The Harvard workforce data (9–10% junior employment drop within six quarters of AI adoption) provides empirical backing for the first step of this argument. The logic of the pipeline consequence is structurally sound.
- **Credibility factors AGAINST:** Assumes AI won't substantially accelerate the time to develop senior-level judgment. If AI tools help juniors develop expertise faster, the pipeline problem is smaller.
- **Planning implication:** If GHX maintains or grows junior developer hiring while peers cut it, there is a potential 3–5 year competitive advantage in having an experienced mid-level cohort when the market faces a shortage.

---

### Engineering Community Synthesis: The "Plateau + Infrastructure" Thesis 🔴 OPINION
- **Synthesis of:** Pragmatic Engineer, Addy Osmani, DORA findings, and practitioner discourse through 2025–2026
- **Claim:** There is a productivity plateau approaching for copilot-style tools, reachable within 12–18 months. The next step-change requires agentic deployment, which requires significantly more organizational infrastructure (governance, test coverage, review processes, security tooling) than most enterprises currently have. Organizations that invest in that infrastructure now will see a second productivity step-change; those that don't will plateau.
- **Credibility:** Consistent with DORA "amplification" data and Faros.ai high-variance data. Treat as a plausible hypothesis to monitor, not a settled fact.
- **Planning implication:** The infrastructure investment needed to unlock agentic gains should begin now, ahead of when agentic tools are enterprise-ready. Platform maturity, test coverage, and security tooling are the long lead-time items.

---

## Updated Consensus View (incorporating both sections)

The range of credible expert opinion spans from "software engineering roles substantially automated within 12 months" (Amodei, aggressive end) to "meaningful but incremental gains over 3–5 years" (Orosz, conservative end). The data-grounded view sits between these: a transition already underway, accelerating, but with significant organizational prerequisites that will rate-limit enterprise adoption — especially in regulated industries.

For GHX planning purposes, the most defensible stance is:

**Claim the near-term gains now.** The 15–25% productivity gains available from well-implemented copilot-style tooling are data-backed and achievable within 12 months with proper rollout and training investment.

**Invest in the infrastructure for agentic gains.** Test coverage, platform quality, security tooling, and governance are the unlock for the next tier of productivity. These are 12–24 month investments.

**Maintain the junior developer pipeline.** The 3–5 year risk (Orosz, Harvard data) is real and asymmetric. The cost of maintaining junior hiring is low relative to the cost of a senior shortage in 2029.

**Track model improvement rates.** METR's 6-month reversal is the clearest signal that the productivity ceiling is not fixed. Tools available in Q1 2027 will be meaningfully more capable than today's — reassess assumptions every 6 months, not annually.

**Plan for governance before it's needed.** The shadow AI and IP leakage risks (governance gap observation) are compliance exposures for GHX specifically. Get ahead of them before agentic tools become standard team practice.
