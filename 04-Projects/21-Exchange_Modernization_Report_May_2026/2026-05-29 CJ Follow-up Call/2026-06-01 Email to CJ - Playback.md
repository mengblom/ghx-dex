# Email to CJ - Resiliency Spike Playback

**Date:** June 1, 2026  
**Subject:** Resiliency Spike - Playing Back What I Heard

---

CJ,

Thank you for your patience. You asked me to echo back what I believe you're asking for in terms of clarity.

As a reminder, here are the two tracks I'm saying we need to accomplish before starting to shift capacity:

- 1: Autonomous Teams** - to set ourselves up to continue to make resiliency improvements more nimbly and incrementally, without it always being a huge Exchange-wide prioritization discussion.
- **2: P0 Database Improvements** - to address the largest threats to stability in our DB layer

I believe you're asking for four things:
1. A definition of done for these tracks broken down to the level of epics or stories
2. A way to track progress against them (milestones, percent complete)
3. How this work improves resilience
4. What decoupling work has already been done

### 1. Definition of Done

We don't have epic/story-level breakdown yet - that will become clear as we engage with the work. In the meantime, the best I can produce is a higher-level checklist:

**Track 1: Autonomous Teams**
- [ ] 12 teams have independent deployment pipelines (each team owns 1+ pipelines)
- [ ] Teams deploy weekly without cross-team coordination
- [ ] GitHub migration complete (100% of Exchange repos)
- [ ] GHX Exchange Team Standards implemented (native Jira projects, standard workflows, ownership metadata)

**Track 2: P0 Database Improvements**
- [ ] Audit DB re-architecture (investigate if Mongo is needed, explore S3-only approach)
- [ ] BT/BD stability and scalability improvements (deep dive to identify root causes)
- [ ] General data layer reliability risk assessment (load analysis, noisy neighbor threats, capacity planning)

### 2. How You'll Track Progress

Over the next few weeks, the details of this work will start to fill in - initiatives, epics underneath them, percent complete, and milestones. You'll be able to see progress as teams engage with the work.

### 3. How This Improves Resilience

**Track 1 (Autonomous Teams):**
- Smaller blast radius when deployments fail (one team, not all of Exchange)
- Faster recovery (team owns entire stack, no coordination overhead)
- Team-level accountability for stability (can measure per-team uptime)
- Creates 12 swim lanes to continuously address resiliency issues at sustainable pace

**Track 2 (P0 Database Improvements):**
- Directly addresses architectural issues causing incidents (Audit DB, BT/BD)
- Removes database-related failure modes
- Risk assessment prevents future capacity/stability issues

### 4. What Decoupling Work Has Already Been Done

I'll follow up with more details on this - I don't want you to have the impression that no progress has been made.

Does this match what you're looking for?

Marten
