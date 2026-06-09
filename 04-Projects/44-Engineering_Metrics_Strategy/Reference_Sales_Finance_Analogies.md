# Cross-Functional Analogies: WHAT vs HOW

**Purpose:** Quick reference for explaining why DORA metrics shouldn't be reviewed in leadership forums using analogies from Sales and Finance that CJ will immediately understand.

---

## The Core Pattern

**Every function has:**
- **WHAT metrics** - Outcomes/results appropriate for leadership review
- **HOW metrics** - Process mechanics that corrupt under performance pressure

**The principle:** Hold teams accountable for WHAT, empower them to optimize HOW.

---

## Sales Analogies (Most Powerful)

### The Strong Analogy
**"We don't review 'sales calls per day' in leadership forums - we review revenue. For the same reason we shouldn't review deployment frequency - we should review features shipped and customer value."**

### What Gaming Looks Like

**If you review "calls per day" publicly:**
- Sales reps make quick, low-quality calls to hit numbers
- They schedule meetings with unqualified prospects
- Time spent logging activity instead of building relationships
- **Call counts look great, revenue doesn't improve**

**This is exactly what happens with DORA under leadership review:**
- Engineers deploy trivial changes to increase frequency
- Cut corners on code review to reduce lead time
- Declare incidents resolved prematurely to improve MTTR
- **Metrics look great, actual delivery doesn't improve**

### Historical Evidence
Many sales organizations in the 1990s-2000s tried managing by activity metrics. The universal result:
- High activity, low conversion
- CRM dashboards looked impressive
- Revenue didn't improve
- **Modern sales management learned: Hold reps accountable for quota (WHAT), let them optimize their process (HOW)**

### The Table

| Sales | Engineering |
|-------|-------------|
| ✅ Review: Revenue, deals closed, win rate | ✅ Review: Features shipped, reliability, customer value |
| ❌ Don't review: Calls made, emails sent, meetings scheduled | ❌ Don't review: Deployment frequency, lead time, MTTR |
| **Why:** Can't fake revenue; gaming quota means success | **Why:** Can't fake customer value; gaming frequency bypasses value |

---

## Finance Analogies (Strong Authority Signal)

### The Strong Analogy
**"We don't review 'journal entries processed' or compare 'time to close books' across teams - we review EBITDA and accuracy. For the same reason we shouldn't compare DORA metrics - we should review delivery outcomes."**

### What Gaming Looks Like

**If you pressure "time to close" as a competitive metric:**
- Finance teams rush close process
- Defer reconciliations until after close
- Use estimates instead of actuals
- Declare close "complete" while continuing adjustments
- **Close timing looks great, audit findings increase**

**This is exactly what happens with DORA:**
- Teams optimize for metrics instead of quality
- Quick fixes instead of thorough solutions
- Gaming the measurement system
- **Metrics look great, actual outcomes degrade**

### Historical Evidence
When "fast close" became trendy (2000s), companies competed on speed (10 days → 5 days → 3 days):
- Audit findings increased
- Quality degraded
- **Mature finance orgs learned: Accuracy matters more than speed. Close in 7 days accurately beats 3 days with errors.**

### The Table

| Finance | Engineering |
|---------|-------------|
| ✅ Review: EBITDA, accuracy, audit findings | ✅ Review: Features shipped, reliability, incidents |
| ❌ Don't review: Journal entry count, close time (for comparison) | ❌ Don't review: Deployment frequency, lead time (for comparison) |
| **Why:** Can't fake profitability or audit results | **Why:** Can't fake customer value or system reliability |

---

## Customer Success Analogy (Emerging Function)

### The Strong Analogy
**"We don't review 'customer touchpoints logged' or 'email response time' - we review retention and NPS. Same principle for DORA."**

### What Gaming Looks Like
- Log unnecessary touchpoints to hit numbers
- Send quick, unhelpful responses to improve speed metrics
- Close tickets before issues fully resolved
- **Activity looks great, customer satisfaction doesn't improve**

---

## Marketing Analogy (Content/Activity Risk)

### The Strong Analogy
**"We don't review 'blog posts published per month' - we review pipeline generated and conversion rates. Same principle for DORA."**

### What Gaming Looks Like
- Publish low-quality content to hit volume targets
- Blast email lists to hit send counts (hurting deliverability)
- **Activity looks great, pipeline generation doesn't improve**

---

## Quick Response Templates

### When CJ says: "But we review sales pipeline"
**"Exactly - and sales pipeline measures WHAT (deals closed, revenue). We don't review 'calls made per day' because that's HOW they work, and it corrupts behavior. DORA is the engineering equivalent of 'calls per day' - it measures process mechanics, not outcomes. We should review features shipped and system reliability (the engineering equivalent of revenue), not deployment frequency."**

### When CJ says: "We review everything in finance"
**"We review EBITDA and accuracy - the WHAT. We don't compare 'journal entries processed' or pressure 'time to close' as a competitive metric because that led to the fast close disasters of the 2000s where teams rushed close and audit findings increased. DORA metrics are like close timing - useful for teams to track their own improvement, but corrupting when reviewed competitively in leadership forums."**

### When CJ says: "This seems like engineering is special"
**"It's the opposite - engineering should follow the same principle that makes sales and finance management successful. Every function has WHAT metrics (outcomes appropriate for leadership) and HOW metrics (process mechanics that corrupt under pressure). The boundary is the same everywhere:
- Sales: Review revenue ✅, not calls made ❌
- Finance: Review EBITDA ✅, not journal entries ❌  
- Engineering: Review features shipped ✅, not deployment frequency ❌

This principle makes engineering management consistent with how we manage other functions, not different."**

### When CJ says: "But postmortems DO have accountability"
**"You're absolutely right - and this actually strengthens the WHAT vs HOW framework. Blameless postmortems have accountability for WHAT (outcomes) while being blameless for HOW (process/individuals):**

**We're accountable for:**
- ✅ The incident occurring (WHAT outcome)
- ✅ Customer impact and downtime (WHAT business result)  
- ✅ Fixing system weaknesses (WHAT organizational responsibility)

**We're explicitly NOT examining:**
- ❌ Who made the mistake (HOW individual action)
- ❌ What they were doing wrong (HOW process detail)
- ❌ Should anyone be disciplined (HOW performance evaluation)

**The word 'blameless' exists to maintain outcome accountability while removing process blame. That's the WHAT vs HOW distinction in action.**

**Leadership reviews WHAT happened (incident, impact, system failures) but not HOW/WHO caused it (individual actions, process details for blame). This is exactly what we should do with DORA:**
- Review WHAT: Features shipped, system reliability, incidents
- Don't review HOW: Deployment mechanics, cycle time, process details

**Blameless postmortems prove that outcome accountability + process protection works better than surveillance. Apply the same principle to DORA."**

### When CJ says: "We need to know what's happening" or "How else do we ensure accountability?"
**"There's a critical research-backed insight here: process metrics require psychological safety to be useful, and leadership review destroys that safety.**

**Amy Edmondson at Harvard and Google's Project Aristotle both found psychological safety is the #1 predictor of team performance. To use DORA honestly, teams must admit when deployments fail, report when incidents take longer, and surface systemic problems.**

**But when leadership reviews these metrics, even with good intentions, the implicit performance pressure destroys the safety required for honest reporting. Teams game metrics to look good instead of being honest. You can't have both leadership review of process metrics AND psychological safety for honest measurement - pick one.**

**This is especially true with 'spin the wheel' random reviews - creates ambient surveillance where teams constantly manage metrics for presentation readiness instead of actual improvement.**

**We can ensure accountability through outcomes:**
- ✅ Review WHAT: Features shipped, system reliability, customer impact
- ✅ Hold teams accountable for business results
- ❌ Don't surveil HOW: Deployment mechanics, process details
- ❌ Protect safety for teams to experiment and improve

**Blameless postmortems prove this works: Outcome accountability (incident happened, we own it) + Process protection (no blame for who/how) = Better results than surveillance."**

---

## The Universal Table (Use This)

| Function | WHAT (Review Publicly) | HOW (Teams Own) | Gaming Example |
|----------|----------------------|-----------------|----------------|
| **Sales** | Revenue, deals closed, retention | Calls made, emails sent | Low-quality calls to hit count |
| **Finance** | EBITDA, accuracy, audit results | Journal entries, close time | Rush close, skip reconciliations |
| **Engineering** | Features shipped, reliability | Deployment freq, lead time | Deploy trivial changes |
| **CS** | Retention, NPS, expansion | Touchpoints, response time | Log fake touchpoints |
| **Marketing** | Pipeline, conversion, ROI | Posts published, emails sent | Low-quality content for volume |

**Pattern:** Gaming WHAT usually requires achieving goal. Gaming HOW bypasses goal entirely.

---

## Strongest Closing Statement

**"This isn't about engineering being special or avoiding accountability. It's about applying the same principle consistently that makes sales and finance management successful:**

- **Sales learned** not to manage by activity metrics (calls per day) because it corrupted behavior
- **Finance learned** not to pressure process speed (fast close) because it degraded quality
- **We learned with postmortems** to maintain outcome accountability (incident happened, we own it) while being blameless about process/individuals (who/how it happened, explicitly protected)
- **Engineering should learn** not to review process metrics (DORA) in leadership forums for the same reasons

**The boundary is the same everywhere: Hold teams accountable for outcomes (WHAT they deliver), empower them to optimize their processes (HOW they deliver).**

**Blameless postmortems prove this works: Outcome accountability + process protection beats surveillance.**

**Where do we stop? At the same place in every function - at the line between outcome accountability and process surveillance."**

---

## Key Advantages of These Analogies

1. **Familiar territory** - CJ understands sales and finance deeply
2. **Historical evidence** - These aren't hypotheticals, they're proven patterns
3. **Shows consistency** - Not special pleading for engineering
4. **Demonstrates maturity** - "We learned this lesson in sales/finance, apply it here"
5. **Provides framework** - Gives him a consistent principle to apply across org
6. **Defuses "slippery slope"** - Shows where boundary actually is

---

## When to Use Which Analogy

- **CJ has sales background** → Lead with sales "calls per day" analogy
- **CJ is metrics-focused/financial** → Lead with finance "fast close" analogy
- **CJ challenges consistency** → Use the universal table
- **CJ says "but we review X"** → Distinguish WHAT (yes) from HOW (no) in that domain
- **CJ dismisses as engineering special case** → "Same principle that works in sales/finance"
