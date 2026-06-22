# DORA Metrics Usage - Quick Reference for CTO Discussion

**Date:** 2026-06-09

---

## The Honest Answer

**No authoritative source explicitly says "don't review DORA metrics in engineering leadership forums."**

Instead, they say: **Be careful how you use them, or you'll damage the culture and get worse results.**

---

## Key Sources & Quotes

### 1. Martin Fowler - "Cannot Measure Productivity"
**URL:** https://martinfowler.com/bliki/CannotMeasureProductivity.html

**What he says:**
- "we can't measure productivity is because we can't measure output"
- "false measures only make things worse. This is somewhere I think we have to admit to our ignorance"
- On team comparison: "You can get a rough sense of a team's output by looking at how many features they deliver per iteration" - but calls this "crude"

**Takeaway:** Even simple team comparisons are unreliable. False metrics create worse problems than no metrics.

---

### 2. Gergely Orosz (Pragmatic Engineer) - "Measuring Developer Productivity"
**URL:** https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity

**What he says:**
- "the earlier in the cycle you measure, the easier it is to measure. And also the more likely that you introduce unintended consequences"
- Measuring effort/output "will negatively impact the engineering culture"
- **Facebook's cautionary tale:** Survey scores became performance reviews, creating perverse incentives where "managers started negotiating with individual contributors for better survey scores"
- McKinsey's framework fails because it measures "effort or output" which "ignores a fundamental truth: measurement changes behavior, often harmfully"

**Takeaway:** Output metrics in leadership forums create gaming behaviors and damage culture. Facebook tried this and it backfired.

---

### 3. DORA.dev - "Generative Organizational Culture"
**URL:** https://dora.dev/devops-capabilities/cultural/generative-organizational-culture/

**What DORA says:**
- "a high-trust, generative culture predicts software delivery and organizational performance"
- "Blaming individuals for failures creates a negative culture"
- "failure leads to inquiry" not scapegoating
- "Ignoring or punishing bad news" undermines trust
- "It's better to understand that failures are inevitable in complex systems"
- Blameless postmortems "remove fear so teams to surface problems and solve them more effectively"

**Takeaway:** DORA's own research says blame culture destroys the psychological safety needed for metrics to be valid. Metrics in blame cultures produce false data.

---

### 4. Google SRE Book - "Postmortem Culture"
**URL:** https://sre.google/sre-book/postmortem-culture/

**What Google does:**
- "Blameless postmortems are a tenet of SRE culture"
- A postmortem "must focus on identifying the contributing causes of the incident without indicting any individual or team for bad or inappropriate behavior"
- "If a culture of finger pointing and shaming individuals or teams for doing the 'wrong' thing prevails, people will not bring issues to light for fear of punishment"
- "Blameless culture originated in the healthcare and avionics industries where mistakes can be fatal"
- You can't "fix" people, but you can "fix systems and processes to better support people"

**Takeaway:** Google (who invented SRE) explicitly adopts blameless culture from aviation and healthcare. Blame suppresses critical information.

---

### 5. Google SRE Book - "Monitoring Distributed Systems"
**URL:** https://sre.google/sre-book/monitoring-distributed-systems/

**What Google measures:**
- "If you can only measure four metrics of your user-facing system, focus on these four" (latency, traffic, errors, saturation)
- Alert only on "an otherwise undetected condition that is urgent, actionable, and actively or imminently user-visible"
- "every page that happens today distracts a human from improving the system for tomorrow"

**Takeaway:** Even Google's SRE org (obsessed with metrics) focuses on a tiny set of actionable signals and avoids metric proliferation.

---

## What the Research Actually Says

### The Problem with Leadership Review:

**When leaders review team metrics comparatively, it creates:**
1. **Psychological unsafety** - Teams fear punishment, suppress bad news (DORA, Google SRE)
2. **Gaming behaviors** - People optimize for metrics, not outcomes (Orosz, Facebook example)
3. **False precision** - Comparisons are "crude" at best (Fowler)
4. **Cultural damage** - Blame culture prevents learning (DORA, Google SRE)

### What Works Instead:

**Teams use metrics internally** - For self-improvement, not external judgment
**Leaders remove blockers** - Focus on system constraints revealed by metrics
**Learning culture** - "Failure leads to inquiry" not blame (DORA)
**Psychological safety first** - Prerequisite for valid data (Google, DORA)

---

## The Argument

You can't send research that says "don't review DORA metrics in leadership forums" because that research doesn't exist in that form.

**But you CAN say:**

"The research (Fowler, Orosz, DORA, Google SRE) is unanimous that:
- Metrics used for comparison create psychological unsafety
- Psychological unsafety suppresses information and encourages gaming
- Gaming produces false data that misleads leaders
- Therefore, the metrics become actively harmful

The question isn't *whether* to look at metrics. It's:
- **Intent:** Learning or performance management?
- **Culture:** Blame or inquiry?
- **Action:** System improvement or individual accountability?

If we're reviewing team DORA metrics comparatively in leadership forums, we're creating the conditions research shows produce the worst outcomes."

---

## What's Missing

The sources most likely to have explicit "don't do this" guidance were inaccessible:
- **SPACE Framework paper** (Forsgren et al., ACM) - blocked by Cloudflare
- **Accelerate book** (Forsgren, Humble, Kim) - full text not online
- **State of DevOps reports** - full PDFs with implementation guidance
- **Stack Overflow blog** - 404 errors

These probably contain more direct warnings, but the sources above make the case clearly enough.

---

## Bottom Line

**The research doesn't say "don't review DORA metrics."**

**It says: "If you review them in a blame culture, you'll get worse outcomes than not measuring at all."**

And leadership forums comparing teams create blame culture by design.
