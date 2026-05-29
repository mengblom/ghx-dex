# Email to CJ - Tonight (May 28)

**Subject:** Your questions on Exchange Modernization deck

---

CJ,

Thanks for the questions. We have a meeting booked for tomorrow, but since we have limited time I wanted to put some things in writing. 

First, let me clarify what we're actually doing here, since I think there's some confusion about what "breaking the monolith" means in this first phase - at first it is more about breaking the monolithic team structure, the monolithic deployment footprint, and the monolithic ways of working - less about the monolithic code base.

**The key insight:** This initial phase is about getting teams to operate autonomously - independent deployment, their own pipelines, their own release schedules. At this stage it is not about creating dozens of new microservices or a perfect architecture diagram. We might not even create that many new services initially.

**Your questions:**

**Q1: How many new services?**  
We might create zero new services initially. The initial goal is to decouple teams, not rewrite the architecture. Over the next few weeks we are going to define the domain of each team in finer detail. Some teams will need to extract services to break coupling, but many might just take ownership of what exists today. The architecture may look very similar to today's footprint initially - the difference is teams can deploy independently.

**Q2 & Q3: Prioritization and sequencing?**  
Yes, if certain areas have proven problematic (incident root causes, high change rate), they'll be prioritized for decoupling and given their own deployment pipeline. But the primary driver is team readiness and coupling complexity. Some teams will break free sooner than others - it'll be incremental. Teams that are ahead can start deploying independently while others are still working through their coupling issues.

We don't have a Gantt chart at the service level because this is a bottom-up process, and architecture changes will be driven by necessity and cost/benefit, much of which will need to be discovered incrementally. 

**Q4: Target architecture diagram?**  
We do have a high-level architecture picture - it's basically aligned with how the teams are formed (the reverse Conway maneuver). But it's at a high level, not individual service level detail.

We know a number of things we'll need to change: eliminate shared databases, replace the event bus, replace direct dependencies with events and messaging, move from EC2 to containers and managed services. But the details and sequencing of these changes will need to be figured out by each team, and it will vary by team. That's why we need autonomous teams first - so this work can happen organically and locally per team, not as a huge coordinated enterprise project.

Here's the important part: even if we have the exact same architecture as today but with decoupled teams, we're in a much better state. The point is breaking free from the shared deployment pipeline and 2-3 week testing cycles, not achieving architectural perfection.

Teams will continue making architectural improvements for a long time after they become autonomous. The difference is those trade-offs happen locally per team, at their own pace, balanced against commercial work.

**Q5: What if we shift to 50/50 in Q3?**  
Most teams won't be autonomous by end of Q3, partially due to competing work (especially DR). The DR work is not just about resource contention - it's largely infrastructure as code, deployments, and automation, which are the same things we need to touch for decoupling. So it's not really possible to parallelize the two efforts. We will get some synergies (some DR work will necessitate decoupling), but they mostly need to happen sequentially.

Additionally, I want to tackle what I'm calling the P0 database issues before shifting capacity - the most egregious problems in our data layer. Most of our serious incidents are database-related. This work doesn't involve all teams (some are more backend/data-oriented than others), so we can shift capacity on some teams while database work continues. But I'd want at least one pass at improving database stability and scalability before the full capacity shift.

Some teams will get to autonomy sooner and will start operating faster immediately. But shifting to 50/50 in Q3 means allocating capacity to commercial work when many teams still have deployment friction. You'll burn the allocation without proportional output increase.

My view: Stay at 25/75 through Q4, shift to 50/50 in Q1 2027 once teams are proven autonomous, and P0 database issues addressed.

**What's happening now:**  
Right now Red Mythos and Disaster Recovery are taking priority over autonomous teams work, especially for individual contributors. This will start shifting as we close out Red Mythos (targeting July), and even more as we get through the DR work, but that's the current reality.

Execution ownership handed to Mike Mitchell this week. Over the next 3-4 weeks:

1. **Infrastructure setup** (parallel work):
   - New JIRA spaces aligned to team domains
   - Simplified workflows teams can customize
   - Finalize team standards

2. **Domain definition sessions** - Mike driving each team through:
   - Map what they own (define boundaries, identify overlaps)
   - Document coupling points (shared repos, databases, dependencies)
   - Start designing target architecture (Lucid charts showing services, connections, data ownership)
   - Plan how they can get to that initial stage of autonomy.

**One more context point:** We're still building out teams (25 open roles, including 3 managers). Some architectural decisions, especially detailed ones, need to wait until teams are fully staffed and can make those calls themselves.

Let's talk tomorrow about Q5 - that's the strategic decision. The rest will clarify as teams complete their domain definitions.

Marten
