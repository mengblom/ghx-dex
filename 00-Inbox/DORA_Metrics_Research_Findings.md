# DORA Metrics Research - Guidance on Usage and Team Comparisons

**Research Date:** 2026-06-09
**Context:** Finding authoritative sources on proper DORA metrics usage, specifically regarding team comparisons in leadership forums

---

## What I Found

### ✅ Sources Successfully Accessed

#### 1. **Martin Fowler - "Cannot Measure Productivity"**
**URL:** https://martinfowler.com/bliki/CannotMeasureProductivity.html

**Key Quotes:**
- "we can't measure productivity is because we can't measure output"
- On Lines of Code: "code that's well designed and factored will be shorter because it eliminates the duplication"
- On Function Points: "even useful functionality isn't the true measure" - real productivity requires delivered business value
- **On teams:** "You can get a rough sense of a team's output by looking at how many features they deliver per iteration" but emphasizes this is crude
- **Core warning:** "false measures only make things worse. This is somewhere I think we have to admit to our ignorance."

**Main Point:** Productivity cannot be reliably measured because we lack valid ways to quantify output. Attempting to use flawed metrics creates worse problems than admitting ignorance.

---

#### 2. **Gergely Orosz (Pragmatic Engineer) - "Measuring Developer Productivity"**
**URL:** https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity

**Key Quotes:**
- **On measurement timing:** "the earlier in the cycle you measure, the easier it is to measure. And also the more likely that you introduce unintended consequences"
- **On gaming metrics:** Measuring effort and output "will negatively impact the engineering culture" because developers optimize for what gets measured rather than business outcomes
- **Facebook's cautionary tale (via Kent Beck):** Survey scores evolved into performance review components, eventually creating perverse incentives where "managers started negotiating with individual contributors for better survey scores"
- **On McKinsey's approach:** Criticizes frameworks that "measure effort or output," warning this approach ignores that measurement changes behavior, often harmfully

**Main Point:** Metrics that measure effort/output (rather than outcomes) create perverse incentives and damage engineering culture. Orosz advocates measuring outcomes and impact instead.

---

#### 3. **DORA.dev - Generative Organizational Culture**
**URL:** https://dora.dev/devops-capabilities/cultural/generative-organizational-culture/

**Key Quotes:**
- **On culture and metrics:** "a high-trust, generative culture predicts software delivery and organizational performance in technology"
- **On blame:** "Blaming individuals for failures creates a negative culture"
- **On learning:** Organizations should "treat [failures] as opportunities to improve and learn"
- **Cultural shift:** "failure leads to inquiry" rather than scapegoating
- **Psychological safety:** Requires "blameless postmortems" which remove fear so "teams to surface problems and solve them more effectively"
- **Explicit warning:** "Ignoring or punishing bad news" undermines trust
- **On inevitability:** "It's better to understand that failures are inevitable in complex systems"
- **Culture measurement:** DORA provides survey items including "Messengers are not punished when they deliver news of failures or other bad news"

**Main Point:** DORA research explicitly warns against blame culture and emphasizes that metrics used punitively undermine the psychological safety required for genuine improvement.

---

#### 4. **DORA.dev - Quick Check Tool**
**URL:** https://dora.dev/quickcheck/

**Finding:** The quick check tool page contains NO explicit guidance about:
- How metrics should be used
- Warnings about comparing teams
- Performance review concerns
- Proper usage contexts

The page only describes the tool's function: "Measure your team's software delivery performance in less than a minute!"

**Implication:** DORA's public-facing tool doesn't include usage warnings, though their research documentation (see #3 above) emphasizes cultural context.

---

#### 5. **Google SRE Book - "Monitoring Distributed Systems"**
**URL:** https://sre.google/sre-book/monitoring-distributed-systems/

**Key Quotes:**
- **Golden signals focus:** "If you can only measure four metrics of your user-facing system, focus on these four" (latency, traffic, errors, saturation)
- **Symptoms over causes:** Monitor "what's broken" (symptoms) rather than intermediate causes
- **Black-box discipline:** "black-box monitoring has the key benefit of forcing discipline to only nag a human when a problem is both already ongoing and contributing to real symptoms"
- **Alert quality test:** Does this rule detect "an otherwise undetected condition that is urgent, actionable, and actively or imminently user-visible"?
- **Complexity warning:** "data collection, aggregation, and alerting configuration that is rarely exercised...should be up for removal"
- **Anti-magic stance:** Explicitly avoid "magic systems that try to learn thresholds or automatically detect causality"
- **Long-term perspective:** "every page that happens today distracts a human from improving the system for tomorrow"

**Main Point:** Google emphasizes measuring only what's actionable and user-visible. Avoid complexity, focus on symptoms, and recognize that measurement should enable improvement, not create busywork.

---

#### 6. **Google SRE Book - "Postmortem Culture"**
**URL:** https://sre.google/sre-book/postmortem-culture/

**Key Quotes:**
- **Core tenet:** "Blameless postmortems are a tenet of SRE culture"
- **System focus:** A blameless postmortem "must focus on identifying the contributing causes of the incident without indicting any individual or team for bad or inappropriate behavior"
- **Good intentions:** Assume "everyone involved in an incident had good intentions and did the right thing with the information they had"
- **Why blame fails:** "If a culture of finger pointing and shaming individuals or teams for doing the 'wrong' thing prevails, people will not bring issues to light for fear of punishment"
- **Industry origins:** "Blameless culture originated in the healthcare and avionics industries where mistakes can be fatal"
- **System over people:** You can't "fix" people, but you can "fix systems and processes to better support people"
- **Cultural reinforcement:** Google uses senior leadership participation, celebrates well-written postmortems, and normalizes learning from incidents

**Main Point:** Google explicitly adopts blameless culture from high-reliability industries. Blame creates fear, suppresses information, and prevents learning. Fix systems, not people.

---

### ❌ Sources That Were Inaccessible

Many URLs returned 404 errors or were blocked by Cloudflare/authentication:

- Stack Overflow blog posts on DORA metrics
- ACM Queue SPACE framework paper (queue.acm.org/detail.cfm?id=3454124) - blocked by Cloudflare
- Google Cloud blog on Four Keys usage
- GitHub blog on measuring productivity
- Various vendor blog posts (LinearB, Sleuth, Cortex, etc.)
- Nicole Forsgren's blog
- LeadDev articles
- IT Revolution articles

---

## What the Research Actually Says

### The Honest Assessment:

**None of the accessible sources explicitly state "don't review DORA metrics in engineering leadership forums."**

Instead, they say:

1. **Be extremely careful** - metrics change behavior, often in harmful ways (Orosz)
2. **Context matters enormously** - blame culture vs learning culture determines whether metrics help or harm (DORA)
3. **We can't actually measure productivity** - output metrics are fundamentally flawed (Fowler)
4. **Measurement creates unintended consequences** - especially when measuring effort/output rather than outcomes (Orosz)

### The Nuanced Argument:

The research doesn't say "never look at DORA metrics as a leader." It says:

- **Don't use them punitively** - "blaming individuals creates negative culture" (DORA)
- **Don't compare teams without context** - Fowler admits team comparison is "crude," Orosz warns about perverse incentives
- **Focus on learning, not blame** - "failure leads to inquiry" not scapegoating (DORA)
- **Understand they're proxies, not truth** - "false measures only make things worse" (Fowler)

---

## What Would Convince a CTO?

### The Missing Pieces:

1. **SPACE Framework paper** (Nicole Forsgren, Margaret-Anne Storey, et al.) - likely has explicit warnings about cross-team comparison
2. **DORA's full research reports** - probably contain implementation guidance beyond what's on the website
3. **Google's Four Keys documentation** - may have usage guidance
4. **Accelerate book** (Forsgren, Humble, Kim) - chapter on organizational culture likely addresses this
5. **Stack Overflow research** - they've published on developer sentiment and metrics

### The Argument You Can Make:

Even without the explicit "don't do this" quote, the research is clear:

**Metrics in leadership forums create:**
- Psychological unsafety (DORA research on blame culture)
- Gaming behaviors (Orosz on Facebook's experience)
- False precision (Fowler on measurement limitations)
- Focus on output over outcomes (Orosz on McKinsey critique)

**What works instead:**
- Teams use metrics internally for improvement
- Leaders focus on removing blockers revealed by metrics
- Cultural emphasis on learning from failures
- Psychological safety as prerequisite for valid data

---

## Next Steps

To find stronger sources, try:

1. **Access the Accelerate book** - Chapter on measurement and culture
2. **Find the SPACE framework paper** - Search Microsoft Research or author pages directly
3. **DORA's State of DevOps reports** - Full PDFs likely have implementation guidance
4. **Contact Nicole Forsgren directly** - She's been vocal about metrics misuse
5. **Search for "psychological safety" + "metrics"** - Amy Edmondson's work on this

---

## Bottom Line

The research doesn't say "don't review DORA metrics in leadership forums."

It says: **If you review them in a blame-focused culture, you'll damage psychological safety, encourage gaming, and get worse outcomes.**

The question isn't whether to review them. It's:
- **Why are you reviewing them?** (Learning vs performance management)
- **What culture exists?** (Generative vs pathological)
- **What happens after?** (Inquiry vs blame)

That's probably not the smoking gun quote you wanted, but it's what the accessible research actually says.
