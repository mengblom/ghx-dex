# Best-in-Class Examples

---

## Accenture (Consulting / Professional Services)

- **Industry:** Technology Consulting / Professional Services
- **Eng Org Size:** Large (hundreds of thousands of employees globally; study covered ~650 developers)
- **Tools Used:** GitHub Copilot
- **Results:**
  - Pull requests per developer: +8.69%
  - PR merge rate: +15%
  - Successful builds: +84%
  - Developer adoption: 80%+ of participants adopted Copilot; 67% used it 5+ days/week
- **Source:** [Research: Quantifying GitHub Copilot's Impact in the Enterprise with Accenture](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/)
- **Key Takeaways:** The 84% increase in successful builds is the most striking result — suggests AI improves not just speed but code quality as it enters review. The training nudge was essential; adoption without it plateaued around 60%. Consulting firm work (project-based, diverse codebases) may limit direct comparability to product-development orgs.

---

## Shopify (E-Commerce SaaS)

- **Industry:** E-Commerce / SaaS
- **Eng Org Size:** ~10,000 total employees; significant engineering organization
- **Tools Used:** Internal AI code review ("Roast" system) + general AI assistants; Cursor and Claude reported among tools used
- **Results:**
  - Estimated **20% productivity gain** (VP & Head of Engineering estimate)
  - "Roast" AI code review runs on every PR above a size threshold — embedded into standard workflow
  - CEO Tobi Lütke declared AI usage a "baseline expectation" for every team in early 2025
- **Source:** [Inside Shopify's AI-First Engineering Playbook — Bessemer Venture Partners](https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook)
- **Key Takeaways:** Shopify's model — mandate AI as default, embed it into mandatory processes (code review), not optional add-ons — is the most aggressive enterprise AI-first posture documented. The 20% gain estimate reflects faster prototyping and higher-quality deliverables across all functions, not just code volume. Cultural normalization (no opt-out) removed friction that kills adoption in other orgs.

---

## Stripe (Payments / Financial Infrastructure)

- **Industry:** Financial Technology
- **Eng Org Size:** ~8,000 employees; substantial engineering organization
- **Tools Used:** Internal "Minions" system (parallel AI agents for code generation and transformation at scale)
- **Results:** Stripe has not published specific productivity metrics; their contribution is architectural — demonstrating that enterprise-grade agentic systems are operationally viable
- **Source:** [What Is an AI Coding Agent Harness? How Stripe, Shopify, and Airbnb Build Reliable AI Workflows — MindStudio](https://www.mindstudio.ai/blog/ai-coding-agent-harness-stripe-shopify-airbnb)
- **Key Takeaways:** Stripe's "Minions" focuses on parallel code generation and transformation — enabling large-scale refactoring and code migration tasks that would be prohibitively expensive manually. The "harness" approach (structured scaffolding around AI models) addresses the consistency and reliability problems that plague raw LLM use in production engineering.

---

## Google (Technology)

- **Industry:** Technology
- **Eng Org Size:** ~30,000+ software engineers globally
- **Tools Used:** Internal AI coding tools; Gemini-based assistants
- **Results:**
  - Internal RCT: developers completed tasks **~21% faster** (96 min vs. 114 min control)
  - AI-generated code share: **"well over 30%"** of new code (Sundar Pichai, 2025)
  - DORA 2025 finding: AI adoption now correlated with higher software delivery throughput at the industry level
- **Source:** [AI in Software Engineering at Google: Progress and the Path Ahead](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/); [AI and Productivity: Year-in-Review — getdx.com](https://getdx.com/blog/year-in-review-with-microsoft-google-and-github-researchers/)
- **Key Takeaways:** Google's ~21% RCT result is more modest than the GitHub benchmark (55%) but involves Google-caliber engineers on real tasks — probably a more realistic proxy for strong engineering orgs. 30%+ AI code share is operationally significant and growing.

---

## Microsoft (Technology)

- **Industry:** Technology / Enterprise Software
- **Eng Org Size:** ~50,000+ engineers
- **Tools Used:** GitHub Copilot; internal tools
- **Results:**
  - AI-generated code share: ~**30%** of new code (executive disclosures, 2025)
  - Part of multi-company study showing **26% productivity increase** across Microsoft, Accenture, and Fortune 100 enterprise
- **Source:** [AI Is Taking Over Coding at Microsoft, Google, and Meta — Entrepreneur](https://www.entrepreneur.com/business-news/ai-is-taking-over-coding-at-microsoft-google-and-meta/490896)
- **Key Takeaways:** Microsoft's position as both a GitHub Copilot vendor and a major consumer creates some conflict of interest in their data, but the 30% code share is corroborated by independent sources. Their internal deployment of Copilot at scale provides the strongest single data point for enterprise-wide rollout feasibility.

---

## Healthcare Organizations (Aggregate, Opsera Research)

- **Industry:** Healthcare
- **Eng Org Size:** Various enterprise healthcare tech orgs
- **Tools Used:** AI coding assistants (tools not specified)
- **Results:**
  - Time to PR: **34–44% faster**
  - Code velocity: **32–42% increase**
  - Features per sprint: **22–32% more**
  - Deployment frequency: **47–57% increase**
- **Source:** [Accelerating Innovation Safely: AI Coding Assistants in Healthcare — Opsera](https://opsera.ai/blog/accelerating-innovation-safely-ai-coding-assistants-in-healthcare/)
- **Key Takeaways:** These are the most optimistic numbers in the research set for a regulated industry. However, the source (Opsera is a DevOps platform vendor) and lack of disclosed methodology make these figures lower-confidence than the RCT-based studies. Treat as an upper-bound estimate rather than a reliable target.
- **⚠️ Use With Caution:** Vendor-published; methodology not disclosed; may represent self-selected high-performing customers.

---

## What Makes Best-in-Class Organizations Different

Synthesizing across all benchmarks, top performers share five characteristics:

1. **Cultural mandate from leadership.** Shopify's "baseline expectation" model — not opt-in, not a pilot, but an organizational commitment — removes the adoption friction that kills most rollouts.

2. **Embedded AI in mandatory workflows.** The most effective implementations don't give developers a new tool to use; they put AI in the path that developers are already walking (code review, CI/CD, PR creation). Shopify's "Roast" system is the clearest example.

3. **Training investment 3x the industry average.** McKinsey's finding that top performers invested in coaching at 3x the rate of bottom performers is the strongest single actionable lever documented in the literature.

4. **Measurement from day one.** Organizations that establish baselines before rollout and measure impact rigorously (not via developer surveys alone) are better positioned to identify what's working, catch regressions, and make the business case for continued investment.

5. **Security as a non-negotiable parallel track.** Best-in-class orgs treat AI-generated code security as a separate, escalated risk stream — not an afterthought. This means automated security scanning in CI/CD and explicit code review requirements for security-sensitive AI-generated code.
