# Draft Response to CTO - DORA Metrics Research

**Context:** CTO challenged: "Send me research that says don't review DORA metrics in engineering leadership forums."

---

## Option 1: Direct & Concise

You asked for research saying not to review DORA metrics in leadership forums. The honest answer: **no source says exactly that.**

But the research is clear about what happens when you do:

**1. Psychological unsafety suppresses critical information**
- DORA research: "Blaming individuals for failures creates a negative culture" and "people will not bring issues to light for fear of punishment"
- Google SRE: "If a culture of finger pointing and shaming prevails, people will not bring issues to light"
- Source: https://dora.dev/devops-capabilities/cultural/generative-organizational-culture/
- Source: https://sre.google/sre-book/postmortem-culture/

**2. Metrics used for comparison create gaming behaviors**
- Gergely Orosz (Pragmatic Engineer): Measuring effort/output "will negatively impact the engineering culture" because it creates perverse incentives
- Facebook's experience: Survey scores became performance metrics, resulting in "managers negotiating with individual contributors for better survey scores"
- Source: https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity

**3. Team comparisons are unreliable at best**
- Martin Fowler: Team output comparison is "crude," and "false measures only make things worse"
- "we can't measure productivity because we can't measure output"
- Source: https://martinfowler.com/bliki/CannotMeasureProductivity.html

**The question isn't whether to look at metrics. It's whether we're creating the conditions research shows produce the worst outcomes:**
- Intent: Learning or performance management?
- Culture: Inquiry or blame?
- Action: System improvement or individual accountability?

Happy to discuss what we're actually trying to achieve and alternative approaches.

---

## Option 2: More Diplomatic

You challenged me to find research saying not to review DORA metrics in leadership forums. Fair challenge - I couldn't find a source that says exactly that.

But I found something more interesting: **unanimous research that leadership metric reviews create the conditions that make metrics harmful.**

**Here's what the research actually says:**

**From DORA's own research:**
> "Blaming individuals for failures creates a negative culture"
> "It's better to understand that failures are inevitable in complex systems"
> "failure leads to inquiry" not scapegoating

When metrics become accountability tools, they lose validity because teams optimize for the metric rather than the outcome.
Source: https://dora.dev/devops-capabilities/cultural/generative-organizational-culture/

**From Google's SRE practices:**
> "Blameless postmortems are a tenet of SRE culture"
> "If a culture of finger pointing and shaming prevails, people will not bring issues to light for fear of punishment"

Google (who practically invented modern SRE) explicitly adopts blameless culture because it's the only way to get valid data.
Source: https://sre.google/sre-book/postmortem-culture/

**From The Pragmatic Engineer (Gergely Orosz):**
> "the earlier in the cycle you measure, the easier it is to measure. And also the more likely that you introduce unintended consequences"

Facebook tried using developer surveys in performance reviews. Result: managers and ICs negotiating scores, destroying the validity of the data.
Source: https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity

**From Martin Fowler:**
> "we can't measure productivity because we can't measure output"
> "false measures only make things worse"

Even team-level comparison is "crude" - and that's before we add the pressure of leadership scrutiny.
Source: https://martinfowler.com/bliki/CannotMeasureProductivity.html

**My synthesis:**

The research doesn't say "don't look at DORA metrics." It says: **If you review them in ways that create accountability pressure, you'll:**
1. Suppress critical information (teams hide problems)
2. Encourage gaming (optimize metrics, not outcomes)
3. Damage psychological safety (fear replaces inquiry)
4. Get misleading data (false positives from gaming)

**What I think we should discuss:**
- What problem are we actually trying to solve?
- What decisions would we make differently with this data?
- How do we get valid signals without creating perverse incentives?
- What does "good" look like in our context?

I'm not saying metrics are bad. I'm saying the research shows how easily they become harmful, and I want us to use them in ways that actually help.

---

## Option 3: Collaborative Problem-Solving

You asked me to send research saying not to review DORA metrics in leadership forums. I spent several hours searching and couldn't find a source that says exactly that.

But I found something more useful: **research on when metrics help vs. when they harm.**

**What makes metrics harmful (unanimous across sources):**
- Using them for accountability instead of learning (DORA, Google SRE)
- Comparing teams without context (Fowler)
- Creating performance pressure (Orosz, Facebook's experience)
- Ignoring cultural prerequisites (DORA, psychological safety research)

**What makes metrics useful:**
- Teams use them for self-improvement
- Leaders remove systemic blockers they reveal
- Inquiry culture ("what can we learn?") not blame culture
- Focus on trends over time, not point-in-time comparisons

**Sources:**
- DORA on organizational culture: https://dora.dev/devops-capabilities/cultural/generative-organizational-culture/
- Google SRE on blameless culture: https://sre.google/sre-book/postmortem-culture/
- Gergely Orosz on measurement pitfalls: https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity
- Martin Fowler on productivity measurement: https://martinfowler.com/bliki/CannotMeasureProductivity.html

**What I'd like to discuss:**
- What problem are we trying to solve with DORA metrics?
- What culture do we have around failure and learning?
- How do we ensure metrics drive improvement rather than gaming?
- What would success look like 6 months from now?

I'm not opposed to using DORA metrics. I want us to use them in ways research shows actually work.

---

## Option 4: Technical/Analytical

You challenged me to find research saying not to review DORA metrics in leadership forums. After searching academic sources, practitioner blogs, and vendor documentation, **I couldn't find explicit guidance that says "don't do this."**

What I found instead: **convergent research showing the conditions under which metrics become harmful.**

**Empirical Evidence:**

**1. Psychological Safety is a Prerequisite (DORA Research)**
- "Blaming individuals for failures creates a negative culture"
- "Ignoring or punishing bad news" undermines the trust required for valid data
- High-trust, generative culture predicts software delivery performance
- Source: https://dora.dev/devops-capabilities/cultural/generative-organizational-culture/

**2. Measurement Changes Behavior, Often Harmfully (Pragmatic Engineer)**
- "the earlier in the cycle you measure, the easier it is to measure. And also the more likely that you introduce unintended consequences"
- Measuring effort/output "will negatively impact the engineering culture"
- Facebook case study: Survey metrics became negotiation points, destroying validity
- Source: https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity

**3. Team Productivity Measurement is Fundamentally Limited (Fowler)**
- "we can't measure productivity because we can't measure output"
- Team comparison is "crude" at best
- "false measures only make things worse. This is somewhere I think we have to admit to our ignorance"
- Source: https://martinfowler.com/bliki/CannotMeasureProductivity.html

**4. Blame Culture Suppresses Critical Information (Google SRE)**
- "Blameless postmortems are a tenet of SRE culture"
- "If a culture of finger pointing and shaming prevails, people will not bring issues to light for fear of punishment"
- Adopted from aviation and healthcare where mistakes are fatal
- You can "fix systems and processes to better support people" but can't "fix" people
- Source: https://sre.google/sre-book/postmortem-culture/

**Synthesis:**

The research doesn't prohibit leadership metric review. It establishes boundary conditions:
- **Valid data requires psychological safety** (DORA)
- **Accountability pressure creates gaming** (Orosz, Facebook)
- **Measurement precision is limited** (Fowler)
- **Blame suppresses information** (Google SRE)

**Hypothesis:** Leadership forums comparing team DORA metrics violate all four conditions.

**Alternative approaches:**
1. Teams self-monitor DORA metrics for continuous improvement
2. Leaders focus on removing systemic constraints revealed by metrics
3. Aggregate trends (not team-by-team) inform resource allocation
4. Cultural investment in psychological safety precedes measurement expansion

**What I propose:**
- Define the decision we're trying to inform
- Identify valid signal for that decision
- Test cultural prerequisites (blameless postmortems working?)
- Pilot with voluntary team participation
- Measure gaming indicators (lead time drops while quality drops?)

I'm not saying we shouldn't use metrics. I'm saying the research is clear about how they fail, and I want us to avoid those failure modes.

---

## Which Tone?

Choose based on your relationship and what you're trying to achieve:

- **Option 1:** Use when you want to be direct and challenge back
- **Option 2:** Use when you want to be diplomatic but still make the point
- **Option 3:** Use when you want to move toward problem-solving
- **Option 4:** Use when your CTO responds to analytical/research-based arguments

All options are honest about what the research actually says while making a clear case for why the practice is problematic.
