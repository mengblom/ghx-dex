# Curtis/Mårten 1-1 - Incident Debrief & Jarvis Rollout Concerns

**Date:** 2026-06-23 (approximate time during ongoing incident)  
**Duration:** ~35 minutes  
**Attendees:** [[Curtis]], [[Marten_Engblom|Marten]]  
**Type:** Unscheduled 1:1 during production incident

---

## Context

Critical discussion during the June 22 production incident (6 simultaneous issues from CoreX-ALL 2.273.x release). This was an unfiltered conversation covering both incident leadership reflections and significant concerns about the Jarvis AI proficiency evaluation rollout.

---

## Key Decisions & Insights

### Incident Response
- ✅ **Key learning:** Should have discussed rollback much sooner in the incident response
- ⚠️ **Risk acknowledgment:** Atlas migration concurrent with releases added significant complexity to rollback decisions
- 📊 **Impact assessment:** Still uncertain about actual customer impact, needs retrospective

### Jarvis Rollout
- ⚠️ **Major messaging problem identified:** "Not a performance review" contradicts evaluation rubrics, action plans, development plans
- 🎯 **Root cause identified:** CJ's board commitment driving artificial urgency (promised 60% AI productivity improvement)
- 💡 **Recommended reframe:** Position as support/skill development opportunity, not evaluation
- ⏰ **Timeline reality check:** August 15 deadline unrealistic for meaningful skill development (~2 months)
- 🤝 **Transparency need:** Should acknowledge board commitment openly to reduce anxiety

---

## Topic 1: Production Incident Reflection

### What Marten Learned

**Rollback Discussion Timing:**
> "A couple of things that I learned in that call is we probably should have talked about rolling back much sooner like way long time ago."

- Waited too long to seriously consider rollback
- Would do this differently in retrospect
- Impact assessment still unclear — needs full retrospective

**Atlas Migration Complexity:**
- Release happened while lower environments on Atlas, production still on MongoDB
- Added significant uncertainty to rollback path
- Trade-off decision: Could have frozen releases for 2 months during migration (team rejected due to velocity concerns)
- Everything comes at a cost: "You assume a little bit more risk"

**Release Complexity:**
- Multiple problems from single big-bang release
- Six different issues simultaneously
- Full day of remediation (minimum)
- Daniel's perspective will be important for post-mortem

### Remediation Timeline
- Already going to be full day before remediation completes
- "That's not great"
- Multi-day resolution expected

---

## Topic 2: Jarvis AI Proficiency Rollout — Honest Feedback

### The Core Problem: Mixed Messaging

**What was said:**
- "This is not a performance conversation"
- "This is not a performance review"
- "We're just interested in how people are doing"

**What was also said:**
- Fill out evaluation spreadsheets
- Here's the rubric to evaluate people against
- People falling behind will have "action plans" or "development plans"
- August 15 deadline for assessment

**Marten's reaction:**
> "We're talking out of both sides of our mouth... I know where this is coming from — CJ promised the board a metric and now we need to figure out how to report on the metric."

### Why Engineers Are Anxious

1. **HR delivery makes it feel like performance management:**
   - Delivered by Sandy (HR)
   - Mentions of "development plans" and "action plans"
   - Evaluation spreadsheets with rubrics

2. **Unrealistic expectations without compensation alignment:**
   > "We want to perform at a level of Anthropic or Google. Well, does that mean we're going to pay people like Anthropic and Google too? Are we going to give them the same incentive package?"
   
   - If people truly level up to those standards, they'd be "fools not to go work at Google"

3. **Impossible timeline:**
   - Less than 2 months to "level up" to level 3
   - Everyone has a day job — only a few hours per day for learning
   - "What do you learn in two months?"
   - Feels like: "In two months you're gonna take the AI final and if you don't score level three... we're not telling you what's gonna happen"

4. **Arbitrary deadline:**
   - August 15 seems totally arbitrary without context
   - People jumping to conclusions about layoffs or performance actions
   - "Why by that time and why so quickly?"

### The Real Story (What People Aren't Being Told)

**Curtis acknowledged:**
- CJ made a commitment to the board about 60% AI productivity improvement
- This is driving the urgency
- Original timeline was even more aggressive (Eric said July 4th, CJ negotiated)
- There's disconnect between board decks (showing Q1 2027 timeline) and the August 15 push

**Curtis's clarification of actual intent:**
- NOT about layoffs or performance management
- Purpose: Figure out where people are on the journey, focus training accordingly
- Self-evaluation + manager assessment to identify perception gaps
- Enable targeted July/August conversations instead of generic ones
- "Developer experience type feedback, not performance management"

**Executives asking about cost savings:**
- Yes, executives asking "does this mean we can save money?"
- Curtis and CJ positioning it as "creating optionality" — could save money OR invest elsewhere
- Not sharing this widely (Curtis: "that's like between you and me")

### Marten's Recommended Messaging Changes

**1. Frame as Support, Not Evaluation:**
> "I wonder if there's a way to frame it less as an evaluation and more as like an opportunity to ask for help and support."

- Everyone understands where they should be striving towards
- Tell us what's missing
- We're trying to give you the stepping stones
- We're trying to help you out

**2. Acknowledge the Reality Openly:**

Suggested framing:
- "The world is changing, we really want to help you upskill"
- "It's good for GHX, it's good for your career"
- "If you go to any large tech company, AI proficiency is already part of hiring and performance evaluation"
- "This is now one more column in the rubric, just like programming languages, system design, etc."
- "We're doing the same thing at GHX"

**3. Be Transparent About the Urgency:**

What to say:
> "Hey, listen, CJ made a commitment to the board that we're going to increase this by 60% because he wants to show that we're leaning into AI. That's what's driving the urgency. Nothing else."

- Don't throw CTO under the bus, but name the reality
- Acknowledge: "We're probably rushing this a bit"
- "There is a bit of urgency because every company is doing this, the world is changing super fast"
- "As individual professionals we all feel that same urgency"

**4. Remove the Performance Management Language:**
- Stop using terms like "action plans" and "development plans" (has specific HR connotations)
- Emphasize: Targeted support, not consequences
- Example: "Instead of focusing on that part of the problem, bring it back to this part — now you're operating differently"

**5. Timeline Reality Check:**
> "Nobody's gonna care [about the evaluation numbers] in nine months because the numbers [throughput/cycle time] are gonna tell their own story."

- The real goal: Throughput and cycle time improvement
- Six months from now, level 3 assessments won't matter
- The work will speak for itself

### Curtis's Response & Next Steps

**Curtis committed to:**
1. **Messaging adjustment** — Incorporate Marten's framing suggestions
2. **Staff meeting discussion** (next day) — Align leadership on revised approach
3. **Individual team conversations** — Curtis doing rounds with each team
4. **Transparency about board commitment** — Will find way to explain the "why" behind urgency
5. **Reframe the evaluations** — Focus on identifying where targeted help is needed

**Quote from Curtis:**
> "We're going to be making these changes... skills are going to come and go. Obviously. I don't want to say 'you don't have to adapt or change' because you do. At the end of the day, the big numbers we're trying to change is throughput and cycle time."

**What Curtis is wrestling with:**
- Sandy (change management expert) giving one kind of advice
- Engineering leaders giving different feedback
- Trying out structured change management approach (learned from previous chaos)
- But acknowledging the messaging landed wrong

### Risk: People Drawing Wrong Conclusions

**What people might be thinking:**
- Layoffs coming August 15
- Performance improvement plans for low scorers
- Forced out if not level 3
- Job security at risk

**Actual reality (per Curtis):**
- "I may be a pawn in somebody else's game, but that is not on my agenda at all"
- It's about leveling up the org, not cutting people
- Creating optionality for the business
- Helping people not get left behind by industry changes

### The Deeper Context: Change Management Philosophy

**Curtis's challenge:**
> "The stories I've read about change management is usually it just takes a while. It's not like a quick, quick and dirty thing. I think we'll be deep into Q1 next year still working on this change."

**What he's trying to avoid:**
- Previous "One GHX" transformation chaos (Tina announced, no transition plan, everyone confused for years)
- "We tripped and fell and ran into walls and fell into pits"
- Trying structured approach this time with Sandy's change management expertise

**Trade-off he's navigating:**
- Structured = more process, more communication, can feel corporate/HR-y
- Unstructured = chaos, confusion, people floundering
- Still calibrating the right balance

---

## Topic 3: Autonomous Teams & Capacity Shift Work

**Brief discussion about Friday meeting with CJ on Exchange resiliency**

**Status:**
- Marten got pulled into incident work, didn't make as much progress as hoped
- Crowdsourcing from team in Slack channel
- Long list of completed work now collected

**Plan:**
- Extract items from old decks
- Map completed work against original gap analysis
- Screenshot old decks with green/yellow checkmarks for what's done
- Time-boxing effort — not building a board presentation, just clear information

**CJ's need:**
- Something he can share directly with Thinktiv and Kickdrum
- Doesn't need to be board-level polish
- Iterated data so he can talk to it

**Key insight from Curtis:**
> "When you look at the surface level RCA, it talks about this problem in the database or data layer. But the real root cause is that there wasn't owners to the work... The underlying root cause was these massive teams and how they're organized and the lack of discipline around it."

**Two-part story:**
1. **Resiliency work completed** — Map against incident root causes from historical decks
2. **Organization transformation** — "World class organization changes" (6 months ago: 1 director, 3 managers, 100 engineers → now: proper team structure with ownership)

**Decoupling work intersection:**
- Some decoupling directly ties to incidents (data layer separation, database splits, noise issues)
- Much decoupling work is about autonomous teams (different but related)
- Can connect via: "Real root cause was lack of ownership in massive teams"

**Timeline:** Review Wednesday before Curtis goes on PTO Thursday

---

## Action Items

### Marten
- [ ] **Finish Exchange resiliency narrative mapping** by Wednesday for review with Curtis ^task-20260623-001
- [ ] **Follow up with Daniel** on incident retrospective perspective ^task-20260623-002
- [ ] **Attend staff meeting discussion** on Jarvis messaging (Tuesday) ^task-20260623-003

### Curtis
- [ ] **Staff meeting agenda Tuesday** — Jarvis messaging, goals, Seth's Marketplace challenges ^task-20260623-004
- [ ] **Schedule team conversations** on Jarvis to address concerns directly ^task-20260623-005
- [ ] **Workshop transparent messaging** about board commitment and urgency ^task-20260623-006
- [ ] **Review Exchange resiliency narrative Wednesday** before PTO Thursday ^task-20260623-007

---

## Key Quotes

**On incident response learning:**
> "A couple of things that I learned in that call is we probably should have talked about rolling back much sooner."

**On mixed messaging:**
> "It doesn't feel like very honest messaging... 'This is not a performance conversation' but then we're talking about filling out a spreadsheet with evaluations... we're talking out of both sides of our mouth."

**On timeline impossibility:**
> "What do you learn in two months? You have a few hours per day, everyone has a day job... It's like half of the next algebra course."

**On the real goal:**
> "Nobody's gonna care [about AI proficiency levels] in six months because the numbers [throughput/cycle time] are gonna tell their own story."

**On reframing:**
> "This is now another new column [in the career ladder]... Most companies are now incorporating AI into hiring and performance... We're just doing the same thing here."

**On the real urgency:**
> "Every company is doing this, the world is changing super fast. And as an individual professional we all feel that same urgency also."

**Curtis on actual intent:**
> "I may be a pawn in somebody else's game, but that is not on my agenda at all [referring to layoffs]."

**On change management challenge:**
> "We tripped and fell and ran into walls and fell into pits [with One GHX transformation]. So I'm trying to figure out if it's a good way to go [with structured change management]."

---

## Related Context

- **Production Incident:** `/07-Archives/2026-06-22_Production_Incident/`
- **Previous Jarvis Discussion:** `/00-Inbox/Meetings/2026-06-04 11.05 Curtis Marten 1-1.md` (Jarvis confirmed as route)
- **Exchange Modernization Work:** `/04-Projects/21-Exchange_Modernization_Report_May_2026/`
- **Board Commitment Context:** CJ promised 60% AI productivity improvement, August 15 checkpoint
- **Staff Meeting Follow-up:** Tuesday discussion on Jarvis, goals, organizational change

---

## Tags

#1-1 #curtis #production-incident #jarvis #ai-proficiency #change-management #organizational-transformation #honest-feedback #messaging-concerns #june-2026-incident

---

## Full Transcript

<details>
<summary>Click to expand full transcript</summary>

[Full transcript preserved as provided by user - available for reference but not duplicated here to avoid length]

</details>
