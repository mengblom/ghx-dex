# What Works: Implementation Strategies

---

## Rollout Approaches

**The evidence strongly supports a phased adoption model rather than a big-bang rollout.** Organizations that see the best outcomes treat AI tooling like a platform launch: get senior developer buy-in first, build internal advocates, then expand.

**Recommended phasing (per Faros.ai and industry best practices):**

1. **Phase 1 — Enthusiastic Early Adopters.** Select volunteers who are already curious about AI tools. Use them to create internal case studies, identify workflow integration points, and develop institutional knowledge. Goal: generate credible internal proof points and surface the real friction points before broad rollout.

2. **Phase 2 — Core Development Teams.** Expand to high-visibility product teams where gains will be measurable and noticed. Update code review guidelines for higher PR volume. Involve QA and security in revised workflows before this phase.

3. **Phase 3 — Extended Teams (QA, DevOps, platform engineering).** These teams use AI differently (infrastructure-as-code, test automation, runbook generation). Requires tailored use cases, not just a copy of developer rollout.

4. **Phase 4 — Cross-Functional Expansion.** Data scientists, product managers, security engineers. Anthropic's 2026 Agentic Coding Trends Report notes that 27% of AI-assisted work is tasks that *wouldn't have been done otherwise* — this phase often unlocks that net-new capacity.

**Critical success factors in rollout:**

- Update code review processes *before* throughput increases. Teams that increase PR volume without scaling review capacity create a bottleneck (Faros.ai data: PR review time increased 91% in high-adoption teams).
- Normalize AI usage culturally. Shopify embedded AI code review ("Roast") into every PR above a size threshold — not optional, not opt-in. This removed social friction around AI use.
- Set expectations honestly. Developers who expect to be 2x more productive and experience 20% gains will be disappointed; calibrate expectations against rigorous data.

---

## Training and Enablement

**Training investment is the single strongest predictor of AI productivity outcomes in the McKinsey data.** Top-performing AI adopters invested in hands-on workshops and coaching at nearly 3x the rate of bottom performers (57% vs. 20%).

**What effective training looks like:**

- **Prompt engineering for developers.** How to write prompts that produce usable output; how to decompose tasks; how to specify constraints and context. This is a genuine skill that improves rapidly with practice.
- **Recognizing AI failure modes.** Teaching developers to identify subtly wrong AI output — the "almost right" problem cited by 66% of Stack Overflow respondents. Pattern recognition for common AI mistakes in your specific tech stack.
- **Security-specific training.** Developers need to understand that AI-generated code has documented higher vulnerability rates (Veracode: 2.74x more vulnerabilities than human-written code). They need to know what to look for and not approve security-sensitive AI suggestions without verification.
- **When NOT to use AI.** For complex legacy system changes, security-critical code, and deeply novel architectural work — experienced developers on these tasks may be faster without AI (see METR findings). Training should include this honest assessment.
- **Hands-on practice time.** Allow developers structured time to experiment without production pressure before they are expected to use tools productively. Forced adoption without practice time creates frustration and low acceptance rates.

**Target adoption rates:** Based on Accenture data, expect adoption to plateau around 60% after 1–2 months without sustained enablement effort. Continued coaching and use-case sharing is needed to push adoption to 80%+.

---

## Measurement Frameworks

**What to measure — and what not to:**

Most easily measured metrics (lines of code written, number of AI suggestions accepted, code generation volume) are poor proxies for productivity. Use a balanced scorecard:

**Throughput metrics** (leading indicators, but can be gamed):
- PR merge rate and velocity
- Task/ticket completion rate
- Time from code complete to deployment
- Test coverage trends

**Quality metrics** (lag indicators, but what actually matters):
- Defect escape rate to production
- Security vulnerability counts per code review (static analysis tooling)
- Time spent in code review (too much increase signals review bottleneck)
- Rework rate / PR rejection rate

**Business outcome metrics** (hardest to attribute, most important):
- Feature delivery velocity (features shipped per sprint)
- Time to market for new capabilities
- Incident rate per feature shipped

**Developer experience metrics** (predictive of sustainability):
- Developer satisfaction scores (NPS or DORA-style survey)
- Time spent on repetitive vs. novel work
- Self-reported frustration with AI tools (track the "almost right" problem)

**DORA's recommended framework** identifies seven organizational capabilities that predict AI ROI: these are available in detail in the [2025 DORA Report](https://dora.dev/dora-report-2025/).

**Measurement timing:** Run baseline measurements for at least 2–3 months before introducing AI tools; measure impact at 3 months and 6 months. One month of data is insufficient to see through the learning curve.

---

## Common Pitfalls

**1. The Review Bottleneck**
Throughput increases without scaling code review create a choke point. Faros.ai documented a 91% increase in PR review time among high-adoption teams. Address this proactively by investing in automated review tooling, reviewer training, and (eventually) AI-assisted code review itself.

**2. Security Regression**
AI-generated code has documented higher vulnerability rates. Without active countermeasures, adopting AI coding assistants will increase your security exposure. Required mitigations: automated SAST/DAST tools in CI/CD pipeline, targeted security review for AI-generated code paths, and developer security awareness training. Sources: Veracode (2.74x vulnerability rate), Apiiro (10x increase in security findings), IEEE study (37.6% increase in critical vulnerabilities after 5 AI iterations).

**3. False Productivity Confidence**
METR's RCT showed a 39-point perception gap — developers believed they were 20% faster while being 19% slower. Management may see high AI adoption rates and assume productivity gains without measuring actual outcomes. Build measurement into the rollout from day one.

**4. Skill Atrophy**
Studies show developers using AI assistants exhibit "false sense of security" about code correctness and may rate insecure AI-generated code as secure. Long-term, this may degrade the review skills needed to catch AI errors. Mitigation: maintain code review standards, require developers to understand (not just accept) AI suggestions, and periodically run exercises without AI tools.

**5. Big-Bang Rollout Without Process Change**
Giving everyone Copilot access on day one without updating code review processes, security workflows, or training programs typically results in 20–30% active usage, limited gains, and frustrated developers. Treat it as a platform launch with change management, not a tool purchase.

**6. Over-reliance in Regulated/Complex Domains**
AI models show 22.7% success rates on complex regulated-industry workflows and misinterpret business requirements in 58.3% of multi-system healthcare/finance cases. Using AI assistants on compliance-critical or complex legacy code without strong human review is high-risk. Start with lower-risk use cases (tests, docs, scripts) and prove quality before expanding to core business logic.

**7. Neglecting the Internal Platform**
The DORA report's clearest finding: the quality of your internal developer platform (build systems, deployment pipelines, developer tooling) is directly correlated with AI ROI. Organizations that invest in AI without first investing in platform maturity consistently underperform. AI amplifies existing developer experience, both good and bad.
