# Timeline: Engineering Metrics Discussion

**Period:** June 8-9, 2026
**Status:** ✅ Resolved - Positive outcome
**Key Players:** Marten Engblom, CJ (VP Engineering)

---

## Table of Contents

### Timeline
- [Saturday, June 8, 2026 - Initial Concern](#saturday-june-8-2026---initial-concern)
  - [Morning: TLT Meeting](#morning-tlt-meeting)
  - [Afternoon: Marten's Response](#afternoon-martens-response)
  - [Evening: Research & Preparation](#evening-research--preparation)
- [Sunday, June 9, 2026 - The Discussion](#sunday-june-9-2026---the-discussion)
  - [Morning: CJ Responds](#morning-cj-responds)
  - [15-Minute Meeting: Outcome](#15-minute-meeting-outcome)

### Analysis & Context
- [Key Quotes Timeline](#key-quotes-timeline)
- [What Changed Marten's Mind](#what-changed-martens-mind)
- [What Was Preserved from Research](#what-was-preserved-from-research)
- [Lessons Learned](#lessons-learned)
- [Current Status & Next Actions](#current-status--next-actions)
- [Timeline Summary (One Glance)](#timeline-summary-one-glance)
- [People Sidebar Reactions](#people-sidebar-reactions)

---

## Saturday, June 8, 2026 - Initial Concern

### Morning: TLT Meeting
- CJ proposed reviewing DORA metrics in leadership forums using "spin the wheel" approach
- Ramesh presented inventory management metrics
- Mitch showed pages of data, some discussion about missing metrics
- Meeting ran out of time before full discussion

### Afternoon: Marten's Response
**Action:** Drafted email to CJ raising concerns about DORA metrics review

**Core concerns:**
1. Leadership review of process metrics (HOW) corrupts team behavior
2. "Spin the wheel" creates ambient surveillance and gaming behavior
3. Similar to failed Amazon pattern
4. Teams should own process metrics, leadership should review outcomes

**Key argument:** Sales reviews WHAT (revenue), not HOW (calls made). Engineering should follow same principle.

**Sent:** Email to CJ late afternoon

### Evening: Research & Preparation
Marten spent evening building research-backed argument:

1. **Core framework developed:** WHAT vs HOW distinction
   - Outcome metrics (WHAT) vs Process metrics (HOW)
   - Gaming asymmetry: Gaming WHAT = success, Gaming HOW = theater

2. **Research compiled:**
   - DORA creators: Designed for team self-assessment, not comparison
   - Stack Overflow: "Metrics serve improvement, never punishment"
   - Goodhart's Law: When measures become targets, they corrupt
   - Google SRE: Blameless postmortems separate outcome from process
   - Amy Edmondson / Google Aristotle: Psychological safety is #1 factor

3. **Cross-functional analogies developed:**
   - Sales learned not to manage by activity metrics (calls per day) in 1990s-2000s
   - Finance learned not to pressure process speed (fast close) in 2000s
   - Both: Review outcomes, let teams optimize process

4. **Documents created:**
   - Full argument with research backing
   - One-page talking points
   - Citations quick reference
   - Psychological safety deep dive
   - Sales/Finance analogies cheat sheet
   - Artifact-as-forcing-function pattern analysis

**Preparation complete:** ~5-6 hours of research and writing

---

## Sunday, June 9, 2026 - The Discussion

### Morning: CJ Responds
CJ replied to email acknowledging "picking things apart" was wrong phrasing, scheduled 15-minute discussion

### 15-Minute Meeting: Outcome

**CJ's Opening Challenge:**
> "I've heard this so much - people are gonna game it, don't you trust me? Where do we stop? Should we stop looking at revenue, EBITDA, sales pipelines?"

**Marten's Core Argument:**
- Sales analogy: We review revenue (WHAT), not calls made (HOW)
- Engineering should review features shipped (WHAT), not deployment frequency (HOW)
- Gaming asymmetry: Can't fake revenue, can fake deployment frequency

**CJ's Clarification (Key Turning Point):**
- **NOT about comparing teams** - "I don't know why people jump to these conclusions"
- **IS about learning** - Like blameless postmortems, but for metrics
- **Format:** "Here's my data, here's what I learned, here's what I'm improving"
- Amazon "spin the wheel" can be done positively - "How do we do it without being jerks?"

**Marten's Key Insight (What Landed):**
> "It's not about the levels or executive review - it's about the psychological safety existing in that forum. First meeting it won't be there, but over time you and Curtis will demonstrate that's the case."

**CJ's Response:**
> "That's all I care about - that we run a learning meeting. How do we run the complement to blameless postmortems for engineering excellence?"

### What Resonated:
- ✅ Psychological safety framing - CJ agreed this is critical
- ✅ Acknowledging assumptions - Built trust when Marten said "I jumped to conclusions"
- ✅ "Try it and see" approach - Better than preemptive fight
- ✅ Focus on demonstrating safety through behavior over time

### What Didn't Land:
- ❌ "Lots of research says don't do this" - CJ: "Send me research"
- ❌ Gaming concerns alone - Came across as "don't trust me" resistance
- ❌ Assuming Amazon worst-case without evidence

### Agreement Reached:
1. Try the learning meeting approach
2. Focus on "what I learned, what I'm improving" not "why are numbers low"
3. Psychological safety will be demonstrated through CJ/Curtis behavior over multiple meetings
4. Will address unhelpful commentary (if 20% is off-point, will reduce to 10%, then 5%)
5. Need to solve automation gap (six-year problem, now urgent with AI)

### Side Discussion:
- Exchange modernization work: Marten cataloging resiliency items
- Follow-up meeting: End of week after collab week (Marten on PTO next 3 days)

**Meeting tone:** Constructive, not defensive. CJ appreciated the challenge.

---

## Key Quotes Timeline

### Saturday (Email)
**Marten to CJ:**
> "Sales reviews WHAT teams deliver (revenue), not HOW they work (calls made). Engineering should follow the same principle."

### Sunday (Meeting)

**CJ's challenge:**
> "Where do we stop? Should we stop looking at revenue, EBITDA, sales pipelines? Don't we just trust people?"

**Marten's response:**
> "We don't measure how many phone calls they make. We don't measure how they do their work, we measure the outcome."

**CJ's clarification:**
> "We are not comparing teams. There is no comparison. I don't know why people jump to these conclusions."

**Marten's breakthrough insight:**
> "What's needed is not about the levels - it's about the psychological safety existing in that forum."

**CJ's agreement:**
> "That's all I care about - how do we run a learning meeting? Same as blameless postmortems."

**CJ's commitment:**
> "We'll address problems. 20 units of off-point commentary will become 10, then 5."

**CJ's acknowledgment:**
> "I applaud you for raising it. Change is hard - I'd rather talk about my weekend too."

---

## What Changed Marten's Mind

### Before Meeting:
**Position:** Leadership review of DORA metrics will corrupt team behavior, create surveillance culture, destroy psychological safety. Should fight this.

**Assumed:** CJ intends comparison, performance pressure, Amazon-style interrogation

### During Meeting:
**Key realizations:**
1. CJ's intent is genuinely learning-focused, not comparative
2. "Spin the wheel" meant to be positive exploration, not punitive
3. CJ acknowledges psychological safety is critical
4. He's committed to demonstrating safety through behavior
5. Will address unhelpful commentary as it happens

### After Meeting:
**New position:** Try learning approach with explicit psychological safety commitment. If meetings become comparative/critical, address it then.

**Why shift was appropriate:**
- Jumped to conclusions without evidence of CJ's actual intent
- Psychological safety can be built through behavior over time
- Better to try with commitment than fight without data
- CJ heard concerns and acknowledged them explicitly

---

## What Was Preserved from Research

Even though approach shifted, these insights remain valid:

### Core Framework (Still True):
- **WHAT vs HOW distinction** - Outcome accountability vs process autonomy
- **Gaming asymmetry** - Outcome metrics align incentives, process metrics corrupt
- **Psychological safety requirement** - Process metrics need safety to be useful
- **Blameless postmortem parallel** - Outcome accountability + process protection works

### Research Backing (Still Relevant):
- DORA creators designed for team self-assessment
- Stack Overflow warns against team comparison
- Goodhart's Law: Targets corrupt measures
- Amy Edmondson: Psychological safety is #1 factor

### What Changed:
- **Not fighting the meetings** - Trying learning approach instead
- **Not assuming worst case** - CJ's intent is different than feared
- **Focus shifted** - From "don't do this" to "how to do this safely"
- **Trust but verify** - Will monitor psychological safety in practice

---

## Lessons Learned

### What Worked:
1. **Raising concerns directly** - CJ appreciated being challenged
2. **Psychological safety framing** - Resonated more than gaming concerns
3. **Clear principled argument** - WHAT vs HOW framework landed
4. **Acknowledging assumptions** - "I jumped to conclusions" built trust
5. **Proposing "try and see"** - Better than demanding change

### What Didn't Work:
1. **Vague research claims** - "Lots of research" without specifics prompted challenge
2. **Assuming worst case** - Amazon comparison without evidence
3. **Leading with gaming** - Came across as "don't trust me" resistance

### For Next Time:
- Lead with psychological safety, not gaming concerns
- Cite specific research when claiming backing
- Don't assume intent without evidence
- Focus on "how to make it work" vs "why it won't"
- Trust but verify - try with explicit commitments

---

## Current Status & Next Actions

**Status:** ✅ Resolved positively - Agreement to try learning approach

**CJ's Commitments:**
- Run as learning meetings, not performance reviews
- Demonstrate psychological safety through behavior
- Address unhelpful commentary as it happens
- Focus on "what learned, what improving"

**Monitoring:**
- Watch first 2-3 meetings for tone and safety
- Note any comparative or critical commentary
- Speak up if format shifts from learning to evaluation

**Success Criteria:**
- Teams share honestly about challenges
- Discussion focuses on learning, not criticism
- No team comparison or ranking
- Psychological safety evident in forum

**Archive When:**
- After 2-3 successful learning meetings demonstrate approach works
- Or if approach changes and needs re-evaluation

**Last Updated:** June 9, 2026

---

## Timeline Summary (One Glance)

```
Saturday June 8
├─ Morning: TLT meeting, CJ proposes DORA metrics review
├─ Afternoon: Marten sends concern email to CJ
└─ Evening: Marten builds research-backed argument (5-6 hours)

Sunday June 9
├─ Morning: CJ responds, schedules 15-min discussion
├─ Meeting: Discussion reveals CJ's intent (learning not comparison)
├─ Key insight: Psychological safety is what matters, not level of review
├─ Outcome: Agreement to try learning approach with safety commitment
└─ Status: ✅ Positive resolution
```

---

## People Sidebar Reactions

**During meeting, Marten mentioned:**
> "I got pinged by quite a few people on the side, patting me on the back for raising the issue because they didn't feel like they needed to."

**CJ's response:**
> "I'm not surprised. It is not comfortable that now I'll be asked how I'm measuring performance of my team. I've never been asked. It's not the most pleasant thing."

**Context:** Others shared the concern but didn't raise it. Leadership acknowledges the discomfort while still seeing value in metrics discussions.
