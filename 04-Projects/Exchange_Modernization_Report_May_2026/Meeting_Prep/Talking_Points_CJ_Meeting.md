# CJ Meeting Talking Points - May 29, 2026 (30 min)

## Core Message to Land
"Breaking the monolith in Phase 1 = teams can deploy independently. Not about creating dozens of microservices or perfect architecture. Even with same architecture as today but decoupled teams, we're in much better state."

---

## Opening (2 min)
"Got your questions. Sent email to clarify - I think there's confusion about what we're actually doing. This isn't about creating 40 microservices. It's about breaking teams free from shared deployment pipeline. Let's talk through Q5 - the strategic question."

---

## If He Wants to Discuss Q1-Q4 First (5-8 min)

**Clarify the misconception:**
"I think your questions assume we're designing a target microservices architecture and then building it. That's not what's happening. We're breaking teams free from monolithic deployment, not rewriting the architecture."

**Q1: Service count**  
→ Might be zero new services initially. Goal is team autonomy, not architectural perfection.  
→ Some teams will need to extract services to break coupling, but many just take ownership of what exists.  
→ Architecture might look very similar to today - difference is teams deploy independently.

**Q2 & Q3: Prioritization/Gantt**  
→ Incremental - some teams break free sooner than others based on readiness and coupling.  
→ Teams defining domains now (3-4 weeks). Mid-June we'll have better sequencing visibility.  
→ No service-level Gantt because it's bottom-up, not top-down architectural rewrite.

**Q4: Architecture diagram**  
→ We DO have high-level architecture aligned with teams (reverse Conway maneuver).  
→ Know what needs to change: shared databases, event bus, direct dependencies → events/messaging, EC2 → containers.  
→ But details and sequencing figured out by each team - that's why autonomous teams first.  
→ Even if architecture looks exactly like today but teams can deploy independently = huge win.  
→ Teams will continue making architectural improvements after becoming autonomous.  
→ Difference: trade-offs happen locally per team, at their own pace, balanced with commercial work.

**Key point:** "You're asking architecture questions. I'm solving a team autonomy problem."

---

## Q5: The Real Question (15-18 min)

**His ask:** Can we shift to 50/50 in Q3?

**Short answer:** Most teams won't be autonomous by Q3. If we shift capacity then, we burn it without velocity gains.

### The Reality:
- Some teams will become autonomous sooner (incremental wins)
- But most won't be there by end Q3 for several reasons:
  - **DR work can't be parallelized** - it's IaC/deployments/automation (same things we touch for decoupling)
  - **P0 database issues** - most serious incidents are data layer, need to address before capacity shift
  - Coupling complexity, still hiring (25 open roles)
- Those autonomous teams will move faster immediately - but it's 2-3 teams out of 10
- Shifting 50% capacity when 70-80% of teams still have deployment friction = burning allocation

### What I Recommend:

**Stay at 25/75 through Q4, shift to 50/50 in Q1 2027**  
→ 4-5 teams proven autonomous by then  
→ P0 database issues addressed (doesn't involve all teams - can shift some while database work continues)  
→ Demonstrable velocity improvements  
→ Shift capacity when we have the capability to use it  

**Or if there's pressure: 40/60 in Q4, then 50/50 in Q1**  
→ Shows progress as Red Mythos/DR wrap  
→ Tie capacity shift to team readiness  
→ Lower risk than full shift in Q4  

**What I won't recommend: 50/50 in Q3/Q4**  
→ Only 2-3 teams ready  
→ Risk: allocate capacity, don't see proportional output increase  
→ Then explaining to Steve why velocity didn't improve  

### What I Need from You:
- What's driving the Q3 shift question?
- Board pressure? Steve's vision? Laura needs capacity?
- Help me understand forcing function so I can shape right recommendation

---

## Key Points to Emphasize

**We might not create ANY new services initially**  
→ That's OK - the point is team independence, not microservices perfection

**Architecture will evolve for a long time**  
→ But after teams are autonomous, those decisions happen locally
→ Trade-offs balanced against commercial work per team

**Still building out teams**  
→ 25 open roles (20 in India, 3 managers)
→ Some architectural decisions need teams fully staffed first

**Incremental wins**  
→ Some teams break free sooner, start moving faster immediately
→ Not an all-or-nothing flip

---

## Closing (3 min)

**Decisions:**
1. Which capacity shift timeline (current plan, accelerated, or middle path)?
2. Are you OK with mid-June for domain definition results?

**Next steps:**
- Mid-June: Teams finish domain definitions, we'll have sequencing visibility
- Update capacity roadmap based on decision
- Align with Laura on commercial roadmap sizing if we shift sooner

---

## If He Pushes Back

**"I need to see the architecture diagram"**  
→ "You're thinking architectural rewrite. I'm solving deployment independence. Even if architecture stays exactly the same, decoupled teams = 5x faster."

**"How can you not know service count?"**  
→ "Because service count isn't the goal. Team autonomy is the goal. We might create zero services and still win."

**"This feels vague"**  
→ "It's bottom-up by design. Teams define their domains, we composite. Top-down architecture design doesn't get executed - we've tried that before."

**"Can't we just design it and hand to teams?"**  
→ "That's the old model that doesn't work. Teams need to own their boundaries or they won't execute them. Takes 4 weeks longer upfront but actually gets done."

**"Board needs concrete deliverables"**  
→ "Deliverable is X teams deploying independently by end Q4. That's measurable. Service count is a vanity metric."

**"Why can't DR and decoupling happen in parallel?"**  
→ "They're touching the same infrastructure - IaC, deployment pipelines, automation. DR work will necessitate some decoupling (synergies), but mostly they're sequential not parallel."

**"Why database work before capacity shift?"**  
→ "Most serious incidents are data layer. Don't want to shift to commercial work and then get pulled back for database fires. Database work doesn't involve all teams - can shift capacity on some teams while it continues."

---

## Success Criteria

Walk out with:
1. CJ understands this is team autonomy problem, not architecture rewrite
2. Decision on capacity shift timing (or agreement to decide after mid-June data)
3. Understanding of what's driving urgency (board/Steve/Laura)
4. Aligned on mid-June as checkpoint for domain definition results
