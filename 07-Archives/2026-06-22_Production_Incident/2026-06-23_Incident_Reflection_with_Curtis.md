# June 22 Incident — Leadership Reflection (Curtis 1-1)

**Date:** 2026-06-23 (day after incident start)  
**Context:** Unfiltered debrief with Curtis during ongoing incident response  
**Participants:** [[Marten_Engblom|Marten]], [[Curtis]]

---

## Key Learnings

### 1. Rollback Discussion Should Have Happened Much Sooner

**Marten's reflection:**
> "A couple of things that I learned in that call is we probably should have talked about rolling back much sooner like way long time ago."

**What this means:**
- Team spent too much time trying to fix forward
- Rollback was viable option earlier than considered
- Decision-making protocol should prioritize rollback discussion upfront

**For next time:**
- Establish rollback decision checkpoint within first 2 hours
- Default assumption: Rollback is the safe path unless strong evidence otherwise
- Don't wait until all options exhausted

### 2. Impact Assessment Was Unclear

**Throughout incident:**
- Uncertain about actual customer impact
- Hard to gauge severity vs. noise
- Made prioritization and decision-making harder

**Quote:**
> "I'm not sure about the impact yet so depending on that I may have... I guess it hasn't seemed to me like there's been that large of an impact but then now I'm not 100% sure anymore."

**Implications:**
- Need better real-time impact visibility
- Customer-facing impact metrics critical for leadership decisions
- Uncertainty prolonged the incident (hesitation on aggressive actions)

### 3. Trade-offs Are Everywhere

**Atlas Migration Context:**
- Release happened while lower environments on Atlas, production on MongoDB
- Created uncertainty about rollback path
- Intertwined complexity

**The trade-off analysis:**
> "If you were to err completely on the safe side then we would have said like well we can't do any releases during the time when lower environments are on Atlas and production is on Mongo — which would have probably been like we're not doing any releases for two months and people were freaked out."

**Key insight:**
> "Everything comes at a cost... Everything is a trade-off... You assume a little bit more risk."

**Lesson:**
- There was no "safe" decision
- Team chose velocity over absolute safety
- That's a legitimate trade-off, not a mistake
- But need to acknowledge the risk explicitly

### 4. Big Bang Release Risk

**Curtis's observation:**
> "That's probably the impact of a big bang release, right? Like you just got lots of parts."

**The reality:**
- CoreX-ALL 2.273.x had multiple changes
- Six simultaneous issues
- Hard to isolate root causes
- Compounded troubleshooting difficulty

**Monolith problem persists:**
- Can't easily isolate changes
- Blast radius is entire system
- Multiple teams affected
- Long remediation cycles

---

## Timeline & Impact

### Duration
- Incident start: 02:00 MT, June 22
- Curtis conversation: June 23 (ongoing)
- Expected resolution: Multi-day

**Marten's assessment:**
> "Yeah I really hope that those fixes... it's been pretty long time anyway I mean it's already going to be the full day basically before we remediate some of these problems and that's not great."

### Full Day of Remediation

- Not acceptable standard
- Multiple fixes required across different areas
- Team exhausted (21+ hour leadership oversight by Marten)

---

## Organizational Context

### Curtis's Immediate Reaction
> "Sounds like you guys are having a fun day... I was like, oh, you got five different problems. Like what happened?"

### Multi-Issue Incident Pattern

This type of incident (many simultaneous issues) reinforces strategic priorities:
1. **Break the monolith** — Reduce blast radius
2. **Autonomous teams** — Clearer ownership
3. **Better testing** — Catch issues before production
4. **Improved observability** — Understand impact faster

---

## Connection to Strategic Work

### Resiliency Narrative

**Context of this incident:**
- Happening same week as Exchange resiliency report for CJ/board
- Crowdsourcing completed work for Friday presentation
- This incident is data point for why that work matters

**Curtis's framing (from later in conversation):**
> "When you look at the surface level RCA, it talks about this problem in the database or data layer. But the real root cause is that there wasn't owners to the work... The underlying root cause was these massive teams and how they're organized and the lack of discipline around it."

**Strategic connection:**
- Incident validates organizational transformation work
- Resiliency isn't just technical fixes
- Team structure and ownership are root causes

---

## Retrospective Actions

### Planned Follow-ups

1. **Full RCA with team** (after incident resolves)
   - Timeline reconstruction
   - Decision point analysis
   - What we'd do differently

2. **Daniel's perspective** (explicitly mentioned)
   > "I'm interested to get Daniel's perspective too when it's just him and I."
   
   - Strategic analysis partner
   - Different lens on what happened
   - Important for complete picture

3. **Rollback protocol review**
   - When to discuss rollback
   - Decision criteria
   - Authority/approval process

4. **Impact assessment tooling**
   - Real-time customer impact visibility
   - Better decision-making data

---

## Emotional Context

### Marten's State

**Uncertain about impact:**
- Not sure if this was truly severe or manageable
- Will depend on retrospective analysis
- Feeling: "Depending on that I may have..."

**Learning mindset:**
- Explicitly identifying lessons mid-incident
- "Couple of things that I learned"
- Already thinking about next time

**Exhaustion:**
- 21 hours of sustained leadership
- Handoff to Ramesh at 23:52 previous night
- Still engaged next day during Curtis call

### Curtis's Response

**Supportive:**
> "Thanks for helping work through it. Appreciate that."

**Pattern recognition:**
- Immediately identified big bang release signature
- Connected to Atlas migration timing
- Framed within broader org challenges

---

## Related Documents

- **[Comprehensive Incident Record](2026-06-22_Production_Incident_Comprehensive_Record.md)** — Full timeline and details
- **[Executive Summary to Curtis/CJ](2026-06-22_Executive_Summary_to_Curtis_and_CJ.md)** — Leadership communication sent during incident
- **[Curtis/Marten 1-1 Full Notes](../../00-Inbox/Meetings/2026-06-23%20Curtis%20Marten%201-1%20-%20Incident%20and%20Jarvis%20Discussion.md)** — Complete meeting context

---

## Key Quotes

**On rollback timing:**
> "We probably should have talked about rolling back much sooner like way long time ago."

**On trade-offs:**
> "Everything comes at a cost... Everything is a trade-off... You assume a little bit more risk."

**On remediation timeline:**
> "It's already going to be the full day basically before we remediate some of these problems and that's not great."

**On Atlas migration risk:**
> "The uncertainty around at least some of the uncertainty around the rollback path has to do with the fact that we're doing this intertwined with the atlas migration."

---

**Created:** 2026-06-23  
**Source:** Curtis/Marten 1-1 conversation during incident recovery  
**Type:** Leadership reflection and learning capture
