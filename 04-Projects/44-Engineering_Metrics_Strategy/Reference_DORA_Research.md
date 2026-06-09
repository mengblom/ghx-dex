# DORA Metrics Public Review: Research Report

## Executive Summary

The debate over whether DORA metrics should be reviewed in senior leadership forums is **not** a slippery slope that applies to all business metrics. The research reveals fundamental distinctions between **process improvement metrics** (like DORA), **outcome metrics** (like sales pipeline), and **learning mechanisms** (like blameless postmortems) that determine when public review helps vs. harms.

**Key finding:** DORA metrics are designed for team self-diagnosis, not external evaluation. When used in leadership forums, they invoke Goodhart's Law and corrupt team behavior without improving actual delivery outcomes.

---

## 1. Goodhart's Law and Metric Corruption

### Definition
**"When a measure becomes a target, it ceases to be a good measure."**
- British economist Charles Goodhart, 1975

### How Metrics Corrupt
Once systems designed to measure performance become optimization targets, people manipulate behavior to improve the metric rather than achieve the underlying objective (Wikipedia article on Goodhart's Law).

### Examples of Corruption
- **Healthcare:** Hospitals targeting reduced length of stay discharged patients prematurely, increasing emergency readmissions
- **UK COVID Testing:** Counted maximum test capacity rather than actual tests, inflating numbers
- **Academia:** H-index correlations with scientific achievement weakened after becoming evaluation target
- **Engineering:** Kent Beck at Facebook observed metrics that provided "valuable feedback about developer sentiment" degrade once they were "rolled up" into scorecards driving organizational cuts (Gergely Orosz analysis)

**Critical insight:** Metrics function well as descriptive tools but fail when converted into goals.

---

## 2. The Measurement Hierarchy (Gergely Orosz Framework)

**Effort → Output → Outcome → Impact**

### Where DORA Sits
DORA metrics measure **output** (how much we deployed, how fast we recovered, how often we deploy).

### The Problem
> "The earlier in the cycle you measure, the easier it is to measure. And also the more likely that you introduce unintended consequences."
> - Gergely Orosz, "Measuring Developer Productivity"

**Why this matters:**
- Effort/output metrics (like DORA) are easiest to measure but incentivize gaming behavior
- Outcome/impact metrics (like revenue, customer value) align incentives but make individual attribution difficult
- Sales and recruitment succeed because they measure outcomes/impact directly
- Engineering often defaults to effort/output metrics, corrupting behavior

### Martin Fowler's Parallel Argument
From "Cannot Measure Productivity":
- Cannot adequately measure software development output
- Lines of Code fail because well-designed code is shorter
- Function Points inconsistent (300% variance between counters)
- **True output is business value, not delivered functionality**
- Productivity improvements may not manifest for years

---

## 3. Official DORA Guidance on Proper Usage

### Stack Overflow Blog Guidance
From their article on DORA metrics:

**Explicit warnings:**
- **Don't compare teams:** "Don't use [metrics] to rate your teams against each other" - each team operates in its own context
- **Balance all four metrics:** Focusing on subset risks unintended consequences (e.g., prioritizing deployment frequency can compromise quality)
- **Avoid metric obsession:** Explicitly cites Goodhart's Law - metrics should reflect progress toward customer value, not become ends in themselves
- **Provide context:** Don't treat as vanity numbers - understand timeframe, trajectory, interconnections

**Proper implementation:**
- Use metrics to help individual teams **continuously improve their delivery processes**
- Focus on outcomes over outputs
- Focus on team performance over individual metrics
- Ensure teams understand what each metric indicates and what actions to take

**Key principle:** "The overarching principle: metrics serve discovery and improvement, never punishment or ranking."

### Google Four Keys Documentation
- Designed for "teams wanting to measure your team's software delivery performance"
- Privacy-focused: Quick check tool explicitly states "We don't store your answers or personal information"
- Intended audience: Teams comparing themselves against industry benchmarks
- Purpose: Identify improvement priorities, not evaluate performance

### DORA Quick Check
- Purpose: "Measure your team's software delivery performance in less than a minute"
- Results should be viewed by "your team"
- Teams should "discover which capabilities you should focus on improving"
- **Note:** No guidance on sharing with leadership or using for evaluation

---

## 4. Distinction: Process Metrics vs. Outcome Metrics

### Process Improvement Metrics (DORA)
- **Measure:** How we work (deployment frequency, lead time, MTTR, change failure rate)
- **Purpose:** Identify bottlenecks and improvement opportunities
- **Audience:** Teams themselves, for self-diagnosis
- **Gaming risk:** HIGH - easy to game by changing practices without improving outcomes
  - Example: Increase deployment frequency by deploying trivial changes
  - Example: Improve lead time by reducing code review rigor
  - Example: Improve MTTR by declaring incidents resolved prematurely
- **Goodhart vulnerability:** EXTREME - becomes target, ceases to be useful measure
- **Attribution:** Unclear - team metrics don't reveal individual contribution
- **Context dependency:** Same metrics mean different things for different teams

### Outcome Metrics (Sales Pipeline, Revenue, EBITDA)
- **Measure:** Business results (closed deals, revenue, profit)
- **Purpose:** Track business health and individual contribution
- **Audience:** Leadership, for resource allocation and accountability
- **Gaming risk:** LOWER - harder to fake actual revenue or closed deals
  - Can manipulate timing, but revenue is revenue
- **Goodhart vulnerability:** MODERATE - can be gamed (timing deals), but fundamentally tied to business value
- **Attribution:** Clear - sales reps directly control customer relationships
- **Context dependency:** Revenue is revenue across teams

**Critical difference:** Gaming an outcome metric (closing more deals) often means achieving the actual goal (revenue). Gaming a process metric (deploying more frequently) can be completely divorced from the actual goal (customer value).

---

## 5. Why Blameless Postmortems Work Publicly

### Google SRE Book Principles
From "Postmortem Culture":

**Core philosophy:** Postmortems are **learning tools, not accountability mechanisms**

**No individual blame:** Focus on systemic causes, not personal fault
- Assumes "everyone involved in an incident had good intentions and did the right thing with the information they had"
- "You can't 'fix' people, but you can fix systems and processes"

**Why blamelessness matters:**
> "Without blamelessness, people will not bring issues to light for fear of punishment."

**Learning over accountability:**
- Position postmortems as "learning opportunity for the entire company"
- Focus shifts from "allocating blame to investigating systematic reasons why an individual or team had incomplete or incorrect information"
- Origins from healthcare and aviation where mistakes can be fatal

### PagerDuty Guidance
**Postmortems are explicitly designed as learning opportunities, not performance reviews.**

Key distinctions:
- During incident: Focus on restoration
- After incident: Separate "peacetime" opportunity to reflect
- **Critical:** Mixing incident review with performance management undermines the entire process

**Why blameless approach is essential:**
> "What matters most is the customer impact, and that's what you focus on."

By shifting focus from *who* made a mistake to *how* it occurred:
- Provides objective accounts without fear of punishment
- Understands systemic failures rather than individual errors
- Extracts actionable improvements

**Rationale:** In complex systems, "there is never a single cause, but a combination of factors that lead to failure."

### Key Differences from DORA Reviews

| Characteristic | Blameless Postmortem | DORA Leadership Review |
|---------------|---------------------|----------------------|
| **Purpose** | Learning from failure | Evaluating performance |
| **Focus** | System improvements | Team comparison |
| **Consequences** | None (explicitly protected) | Resource allocation, perception |
| **Incentives** | Share honestly | Look good |
| **Scope** | Specific incident | Ongoing process |
| **Gaming risk** | Low (no consequences) | High (direct consequences) |

Blameless postmortems work publicly **because they're explicitly protected from accountability consequences.** DORA reviews in leadership forums fail because they create implicit accountability pressures.

---

## 6. Microsoft Research SPACE Framework

From "The SPACE of Developer Productivity":

**Core argument:** 
> "Developer productivity is about more than an individual's activity levels or the efficiency of the engineering systems relied on to ship software, and it cannot be measured by a single metric or dimension."

**Implication:** Organizations should "use it to help teams better understand developer productivity and create better measures to inform their work and teams."

**Key insight:** The framework serves as a diagnostic tool for self-understanding, not a performance ranking system for external evaluation.

---

## 7. Charity Majors on Accountability vs. Improvement Metrics

From articles on metrics:

### The Distinction
- **Accountability metrics:** Binary, backward-looking - "Did you hit the target?"
- **Improvement metrics:** Exploratory, forward-looking - "What patterns emerge? What surprised us?"

### The Trap
When engineers must constantly audit and prune metrics to control expenses, they're spending time managing the measurement system rather than improving the product.

### The Solution
Organizations that treat measurement as compliance get expensive, unhelpful systems. Those treating it as a learning tool get infrastructure that scales with understanding.

**Fundamental tension:** Treating observability/metrics as a checkbox ends badly. Treating it as exploration enables learning.

---

## 8. Countering the Slippery Slope Argument

### The Critique
"I think this logic can be applied to anything and everything in a business… so if we follow this, we should also not do Blameless Postmortem and RCA process in tech; sales teams should not be reviewing sales pipelines; finance should not be reviewing revenue and ebitda tracking… where do we stop?"

### The Response Framework

**You DON'T apply this logic to everything.** The distinction depends on four factors:

#### Factor 1: What Does the Metric Measure?
- **Process (how you work)** → Private team review
- **Outcome (what you deliver)** → Public leadership review
- **Learning (what went wrong)** → Public but explicitly blameless

#### Factor 2: Who Has Attribution?
- **Team diagnosis** → Keep with teams
- **Individual accountability** → Can be reviewed by leadership (with care)
- **System failure** → Share broadly for learning

#### Factor 3: How Easy to Game?
- **Independent of value** → Gaming risk high, keep private
- **Tied to value** → Gaming risk lower, can review publicly
- **No consequences** → No gaming incentive, share freely

#### Factor 4: What's the Intent?
- **Self-improvement** → Teams own their process metrics
- **Accountability** → Leadership reviews outcome metrics
- **Knowledge sharing** → Public with explicit protections

### Applying the Framework

**Sales Pipeline Reviews Work Because:**
1. Outcome-focused (closed deals = money)
2. Clear attribution (sales reps own relationships)
3. Hard to fake (can't game actual revenue)
4. Gaming aligns with goal (closing deals = achieving goal)
5. Intent is accountability (appropriate for outcomes)

**Blameless Postmortems Work Because:**
1. Learning-focused (not for accountability)
2. System-focused (not evaluating people)
3. Public but protected (no performance consequences)
4. Low gaming risk (incentive is to share, not hide)
5. Intent is knowledge sharing (appropriate for learning)

**DORA in Leadership Forums Fails Because:**
1. Process-focused (measures how, not what)
2. Attribution unclear (team metrics ≠ individual contribution)
3. Easy to game (optimize metrics without improving delivery)
4. Gaming misaligns from goal (better metrics ≠ better outcomes)
5. Violates intent (designed for self-diagnosis, not evaluation)

### The Boundary Line

**Metrics appropriate for public/leadership review:**
- Direct business outcomes (revenue, customer acquisition, retention)
- Clear attribution to individuals/teams
- Hard to game without achieving actual goal
- Naturally aligned incentives
- **Examples:** Sales pipeline, revenue, EBITDA, customer retention

**Metrics inappropriate for public/leadership review:**
- Process improvement indicators
- Ambiguous attribution
- Easy to game independently of actual value
- Designed for self-diagnosis
- **Examples:** DORA metrics, velocity, story points, code coverage

**Learning mechanisms appropriate for public review:**
- Explicitly blameless
- System-focused, not people-focused
- No performance consequences
- Goal is knowledge sharing, not evaluation
- **Examples:** Blameless postmortems, retrospectives, incident reviews

---

## 9. Strong Counter-Arguments

### Argument 1: The Measurement Hierarchy
"DORA metrics measure outputs (how much we deployed). Sales metrics measure outcomes (revenue generated). The earlier you measure in the effort→output→outcome→impact chain, the more likely you introduce unintended consequences." (Gergely Orosz)

**Response to critique:** Sales pipeline reviews work because closed deals can't be faked - gaming the metric means achieving the goal. DORA metrics can be gamed without improving actual delivery.

### Argument 2: Goodhart's Law Applies Differently
"When metrics become targets, they cease to be good measures. But not all metrics corrupt equally." (Goodhart's Law)

**Response to critique:** Revenue is hard to fake. Deployment frequency is easy to fake. The corruption potential differs fundamentally.

### Argument 3: Intent Violation
"DORA metrics were designed for team self-diagnosis, not external evaluation. Using them in leadership forums violates their design intent and invalidates their usefulness." (Stack Overflow Blog, DORA documentation)

**Response to critique:** Sales pipelines were designed for accountability. Postmortems were designed for learning. DORA was designed for teams. Using tools for their intended purpose matters.

### Argument 4: Attribution Matters
"You can attribute revenue to a sales rep. You can't meaningfully attribute DORA metrics to individuals in complex engineering organizations." (Microsoft SPACE framework)

**Response to critique:** Sales pipeline reviews work because attribution is clear. DORA reviews fail because team metrics don't reveal who contributed what.

### Argument 5: Blameless ≠ Private
"Blameless postmortems work publicly because they're explicitly protected from accountability consequences. DORA reviews in leadership forums create implicit accountability pressures that corrupt behavior." (Google SRE Book, PagerDuty guidance)

**Response to critique:** The difference isn't public vs. private - it's accountability vs. learning. Postmortems work because no one gets blamed. DORA reviews fail because they create performance pressure.

---

## 10. Authoritative Sources

### Academic/Research
- **Goodhart's Law** (Wikipedia) - Original formulation and corruption examples
- **Martin Fowler** - "Cannot Measure Productivity" - Why software output can't be measured
- **Microsoft Research** - SPACE framework - Multidimensional productivity measurement
- **DORA Research** - Quick check tool designed for team self-assessment

### Practitioner Guidance
- **Stack Overflow Blog** - Explicit warnings: don't compare teams, cites Goodhart's Law
- **Gergely Orosz** - Measurement hierarchy framework (Effort→Output→Outcome→Impact)
- **Google SRE Book** - Blameless postmortem principles and rationale
- **PagerDuty** - Learning vs. accountability distinction in incident reviews
- **Charity Majors** - Accountability metrics vs. improvement metrics

### Industry Standard
- **Google Four Keys** - Documentation emphasizes team usage, not leadership evaluation
- **DORA.dev** - Quick check designed for team self-diagnosis
- **Team Topologies** - Cognitive load and flow focus, not comparative metrics

---

## 11. Recommended Response Strategy

### Opening Statement
"This isn't about applying one rule to everything - it's about recognizing that different metrics serve different purposes and corrupt in different ways."

### Framework Presentation
"There are three types of metrics/reviews, and they work differently:

1. **Outcome metrics** (sales, revenue, EBITDA) - These measure what we deliver to customers and the business. They're appropriate for leadership review because they're hard to fake and directly tied to business value. Gaming a sales metric (closing more deals) usually means achieving the actual goal (revenue).

2. **Learning mechanisms** (blameless postmortems, RCAs) - These work publicly because they're explicitly protected from accountability. No one gets blamed, so people share honestly. The goal is system improvement, not individual evaluation.

3. **Process improvement metrics** (DORA) - These measure how we work, not what we deliver. They're designed for team self-diagnosis, not external evaluation. They're easy to game without improving outcomes - you can increase deployment frequency by deploying trivial changes, improve lead time by cutting corners on code review, or improve MTTR by declaring incidents resolved prematurely."

### Key Distinction
"The difference between sales pipeline and DORA reviews isn't arbitrary - it's based on **what corrupts and what doesn't:**

- **Sales pipeline:** Hard to fake revenue. Gaming the metric = achieving the goal.
- **Blameless postmortems:** No performance consequences. People share because it's safe.
- **DORA in leadership forums:** Easy to game without value. Creates performance pressure that corrupts behavior."

### Evidence Base
"This isn't speculation - it's well-documented in research:
- **Goodhart's Law** shows metrics corrupt when they become targets
- **Gergely Orosz's framework** explains why measuring outputs (DORA) creates more unintended consequences than measuring outcomes (revenue)
- **The DORA creators themselves** designed these metrics for team self-assessment, not executive scorecards
- **Google's postmortem research** shows why blameless learning works publicly while accountability reviews don't"

### Closing
"Where do we stop? **We review outcomes publicly, empower teams to improve their processes privately, and share learnings publicly with explicit blamelessness.** That's the boundary line - not based on comfort, but on what actually works to drive improvement without corruption."

---

## 12. Key Takeaways

1. **DORA metrics are process/output metrics** - They measure how you work (outputs), not what you deliver (outcomes). This makes them vulnerable to gaming.

2. **Goodhart's Law applies differently to different metrics** - Not all metrics corrupt equally. The earlier in the value chain you measure, the easier to game.

3. **Attribution matters** - Sales metrics have clear individual attribution. DORA metrics are team-level diagnostics. This affects where they should be reviewed.

4. **Intent matters** - DORA was designed for team self-diagnosis. Sales pipeline was designed for accountability. Using tools for their intended purpose matters.

5. **Blameless ≠ Private** - Blameless postmortems work publicly because they're explicitly protected from consequences. DORA reviews create implicit accountability that corrupts behavior.

6. **The slippery slope fails** - The distinction isn't arbitrary. It's based on measurable differences in corruption risk, attribution clarity, and design intent.

7. **The boundary line is clear:** Review outcomes publicly (revenue, customer value). Empower teams to improve processes privately (DORA). Share learnings publicly with explicit blamelessness (postmortems).
