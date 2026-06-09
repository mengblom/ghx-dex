# Authoritative Sources: Quick Reference

**Purpose:** Fast citation of industry best practices and research backing for WHAT vs HOW framework

---

## Core Research & Frameworks

### DORA (DevOps Research and Assessment) - Original Creators
**Authority:** The creators of DORA metrics themselves
**Key Point:** DORA metrics are designed for team self-assessment, not external evaluation or team comparison

**Critical Guidance:**
- Quick check tool explicitly designed for "teams wanting to measure your team's software delivery performance"
- Privacy-focused: "We don't store your answers or personal information"
- **No guidance anywhere** on sharing with leadership or using for performance evaluation
- Intended audience: Teams comparing themselves against industry benchmarks to identify improvement priorities

**Implication:** Using DORA for leadership review violates the creators' design intent

---

### Stack Overflow Blog - Official DORA Implementation Guidance
**Authority:** Major engineering platform, official guidance on DORA implementation
**Key Point:** Explicitly warns against using DORA for team comparison and cites Goodhart's Law

**Powerful Quotes:**
> "Don't use [metrics] to rate your teams against each other"

> "The overarching principle: metrics serve discovery and improvement, never punishment or ranking."

**Explicit Warnings:**
- Don't compare teams - each operates in its own context
- Balance all four metrics - focusing on subset risks unintended consequences
- Avoid metric obsession - explicitly cites Goodhart's Law
- Provide context - don't treat as vanity numbers

**Source:** Stack Overflow Blog article on DORA metrics implementation

---

### Goodhart's Law (1975) - Economic Principle
**Authority:** British economist Charles Goodhart, widely cited principle in measurement theory
**Key Point:** When measures become targets, they cease to be good measures

**The Law:**
> "When a measure becomes a target, it ceases to be a good measure."

**Critical Insight:** Metrics function well as descriptive tools but fail when converted into goals. Once systems designed to measure performance become optimization targets, people manipulate behavior to improve the metric rather than achieve the underlying objective.

**Examples of Corruption:**
- Healthcare: Hospitals targeting reduced length of stay discharged patients prematurely, increasing readmissions
- Academia: H-index correlations with scientific achievement weakened after becoming evaluation target
- UK COVID: Counted maximum capacity rather than actual tests, inflating numbers

**Implication:** Not all metrics corrupt equally - outcome metrics (revenue) are harder to game than process metrics (deployment frequency)

---

### Gergely Orosz - The Measurement Hierarchy
**Authority:** Author of "The Software Engineer's Guidebook", former Uber/Microsoft engineering leader
**Key Point:** The earlier in the value chain you measure, the more unintended consequences you create

**Powerful Quote:**
> "The earlier in the cycle you measure, the easier it is to measure. And also the more likely that you introduce unintended consequences."

**Framework:** Effort → Output → Outcome → Impact

**Application:**
- **DORA measures outputs** (how much we deployed) - Early in chain, high corruption risk
- **Sales measures outcomes** (revenue generated) - Later in chain, lower corruption risk
- Earlier measurement = easier to game without creating value
- Leadership should focus on outcomes, let teams optimize outputs

**Source:** "Measuring Developer Productivity" article

---

### Martin Fowler - Cannot Measure Productivity
**Authority:** Chief Scientist at ThoughtWorks, author of seminal software engineering texts
**Key Point:** Cannot adequately measure software development output - true output is business value

**Powerful Quotes:**
> "Cannot adequately measure software development output"

> "True output is business value, not delivered functionality"

**Key Arguments:**
- Lines of Code fail because well-designed code is shorter
- Function Points inconsistent (300% variance between counters)
- Productivity improvements may not manifest for years
- Focus on outcome metrics (business value) not output metrics (code/deployments)

**Implication:** Deployment frequency, lines of code, and similar output metrics don't capture actual value delivered

---

### Google SRE Book - Blameless Postmortem Philosophy
**Authority:** Google's Site Reliability Engineering practices, industry standard
**Key Point:** Postmortems work because they maintain outcome accountability while being process blameless

**Powerful Quote:**
> "Without blamelessness, people will not bring issues to light for fear of punishment."

**Core Philosophy:**
- Assumes everyone involved had good intentions
- "You can't 'fix' people, but you can fix systems and processes"
- Focus on systemic causes, not personal fault
- No individual blame - position as learning opportunity

**Why It Matters:**
- Separates outcome accountability (incident happened, we own it) from process blame (who/how)
- Leadership reviews WHAT (incident, impact, system failures) not WHO/HOW (individual actions)
- Proves that outcome accountability + process protection works better than surveillance

**Implication:** Apply the same principle to DORA - review outcomes (features, reliability), not process (deployment mechanics)

---

### Microsoft Research - SPACE Framework
**Authority:** Academic research from Microsoft's engineering productivity team
**Key Point:** Developer productivity is multidimensional and cannot be measured by single metrics

**Powerful Quote:**
> "Developer productivity is about more than an individual's activity levels or the efficiency of the engineering systems relied on to ship software, and it cannot be measured by a single metric or dimension."

**Key Insight:** Framework serves as diagnostic tool for team self-understanding, not performance ranking for external evaluation

**Implication:** Using individual metrics (like DORA) for performance evaluation misses the complexity of productivity

---

### PagerDuty - Incident Review Guidance
**Authority:** Industry leader in incident management
**Key Point:** Mixing incident review with performance management undermines the entire process

**Core Principle:**
- Postmortems are explicitly designed as learning opportunities, not performance reviews
- Focus during incident: restoration
- Focus after incident: reflection in "peacetime"
- Critical: Don't mix with performance management

**Why Blameless Works:**
> "What matters most is the customer impact, and that's what you focus on."

**Rationale:** In complex systems, "there is never a single cause, but a combination of factors that lead to failure"

**Implication:** Same principle applies to process metrics - focus on outcomes (impact), not process details (how)

---

### Amy Edmondson - Psychological Safety Research
**Authority:** Harvard Business School professor, pioneer of psychological safety research
**Key Point:** Teams need psychological safety to report honestly, learn from failures, and perform well

**Powerful Quote:**
> "In psychologically safe environments, people believe that if they make a mistake, others will not penalize or think less of them for it."

**Key Research Finding:**
- Teams with high psychological safety report MORE errors (not fewer - they're more honest)
- Learn faster from mistakes
- Perform better on complex tasks
- Innovate more effectively

**What Destroys Psychological Safety:**
- Performance evaluation pressure
- Public comparison between teams
- Using learning metrics for accountability
- Surveillance of process details

**Implication:** Leadership review of DORA metrics destroys the psychological safety required for honest process measurement. Teams game metrics to look good instead of reporting honestly.

---

### Google Project Aristotle
**Authority:** Google's multi-year research on team effectiveness (2012-2014)
**Key Point:** Psychological safety was the #1 predictor of team performance

**Critical Finding:**
- Not about who is on the team (individual talent)
- Not about team structure or processes
- **About how team members interact**
- Psychological safety enabled all other factors

**Implication:** Teams need to feel safe to share honest data about their processes. Leadership review of process metrics creates the opposite environment - surveillance and performance pressure that destroys safety and corrupts metrics.

---

### Charity Majors (Honeycomb) - Accountability vs Improvement Metrics
**Authority:** CTO of Honeycomb, industry leader in observability
**Key Point:** Distinction between accountability metrics (backward-looking) and improvement metrics (forward-looking)

**The Distinction:**
- **Accountability metrics:** Binary, backward-looking - "Did you hit the target?"
- **Improvement metrics:** Exploratory, forward-looking - "What patterns emerge?"

**The Trap:** When engineers must constantly audit metrics to control expenses/appearance, they spend time managing the measurement system rather than improving the product

**Fundamental Tension:** Treating measurement as compliance gets expensive, unhelpful systems. Treating it as learning enables infrastructure that scales with understanding.

**Implication:** DORA should be improvement metrics (team-owned exploration), not accountability metrics (leadership scorecards)

---

## Quick Citation Guide

### When you need to cite industry standard:
**"According to Stack Overflow's official guidance on DORA: 'The overarching principle: metrics serve discovery and improvement, never punishment or ranking.' They explicitly warn: 'Don't use metrics to rate teams against each other.'"**

### When you need academic backing:
**"Goodhart's Law, established in 1975: 'When a measure becomes a target, it ceases to be a good measure.' This isn't speculation - it's economic principle proven across healthcare, academia, and business."**

### When you need engineering authority:
**"Martin Fowler, Chief Scientist at ThoughtWorks: 'Cannot adequately measure software development output... True output is business value, not delivered functionality.' Even the creator of many software practices we use can't find a way to measure productivity with simple metrics."**

### When you need measurement hierarchy backing:
**"Gergely Orosz's framework shows why: 'The earlier in the cycle you measure, the more likely you introduce unintended consequences.' DORA measures outputs (early), sales measures outcomes (later). That's why one corrupts and the other doesn't."**

### When you need Google's credibility:
**"Google's SRE Book, the industry standard: 'Without blamelessness, people will not bring issues to light for fear of punishment.' They learned to separate outcome accountability from process blame. We should apply the same principle to DORA."**

### When someone says "but DORA creators think it's fine":
**"Actually, DORA's own quick check tool is designed for 'teams wanting to measure your team's software delivery performance' - not leadership scorecards. There's zero guidance in their official documentation on using DORA for team comparison or leadership review."**

---

## The Evidence Stack (Use When Challenged)

**1. The creators say so:**
- DORA: Designed for team self-assessment
- Stack Overflow: Explicitly warns against team comparison

**2. The research backs it:**
- Goodhart's Law: Targets corrupt measures
- Orosz: Earlier measurement = more corruption
- Microsoft SPACE: Can't measure productivity with single metrics

**3. We've learned this lesson elsewhere:**
- Google SRE: Blameless postmortems separate outcome from process
- Sales: Learned not to manage by activity metrics (calls per day)
- Finance: Learned not to pressure process speed (fast close)

**4. Industry leaders agree:**
- Martin Fowler: Can't measure output, only value
- Charity Majors: Improvement metrics ≠ accountability metrics
- PagerDuty: Don't mix learning with performance management

**This isn't opinion - this is established best practice backed by decades of research and real-world evidence.**

---

## Counter to "Show Me Where It Says Not To"

**The absence of guidance is itself telling:**

1. **DORA documentation** - Zero mention of leadership review, team comparison, or performance evaluation
2. **Stack Overflow guidance** - Explicitly says DON'T use for team comparison
3. **Google SRE Book** - Designed blameless approach specifically to avoid performance pressure
4. **Every practitioner guide** - Focuses on team self-improvement, not external evaluation

**The pattern is clear:** When experts discuss DORA, it's always for team self-diagnosis, never for leadership scorecards.

**If leadership review was appropriate, why would:**
- Stack Overflow explicitly warn against it?
- DORA's own tool emphasize privacy ("we don't store your answers")?
- Every implementation guide focus on team autonomy?
- Google design "blameless" specifically to remove performance pressure?

**The absence of endorsement + explicit warnings = clear guidance against leadership review.**

---

## One-Sentence Summaries (For Quick Dropping)

- **DORA creators:** "Designed for teams to measure their own performance, not for leadership comparison"
- **Stack Overflow:** "Metrics serve discovery and improvement, never punishment or ranking"  
- **Goodhart's Law:** "When measures become targets, they cease to be good measures"
- **Gergely Orosz:** "Earlier measurement creates more unintended consequences"
- **Martin Fowler:** "True output is business value, not delivered functionality"
- **Google SRE:** "Without blamelessness, people won't bring issues to light"
- **Microsoft Research:** "Can't measure productivity with single metrics"
- **Amy Edmondson:** "Psychological safety is required for teams to report honestly and learn from failures"
- **Google Project Aristotle:** "Psychological safety was the #1 predictor of team performance"

**Pattern:** Every authoritative source points away from using process metrics for external evaluation.
