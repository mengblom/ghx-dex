Meeting Title: Technical priorities review with focus on productivity and monolith migration
Date: May 1, 2026
Meeting participants: [[CJ_Singh|CJ]], Mårten Engblom

## Context

Discussion about alignment with Steve and Laura, technical priorities, and the path forward for Exchange engineering. CJ outlined two critical deliverables needed and discussed the ideal operating model for product/engineering partnership.

## Transcript

### Two Critical Deliverables

**CJ:** We're working on a stronger and better relationship with Christie. She's not a product person and she doesn't know that yet, but her personality is that she knows what she wants and one way or the other she will get it. I admire that, though it can become unhealthy. I'm confident we'll get all three of us aligned. I'm not concerned about that.

Here is the part I need from you. While we clean up all this alignment mess, I need two things from you.

**First:** Very strong and clear commentary backed by data on how we're improving productivity. Because irrespective of alignment, you're on point to improve productivity. What is working? What are the challenges? I'm not looking for all wins. You've been here four months - how are you improving productivity? I'm not looking for pages, I'm looking for executive level, verifiable, data-backed commentary.

**Second:** Radical clarity on when we're done with this quote-unquote "spike on resiliency." When you look at the top priorities Curtis and I laid out - there were five things, and I'll send you the slide - the most ambiguous one is breaking the monolith.

### The Five Priorities

**CJ:** First is database migration. That's binary and easy to explain - when are we done? It's black and white. 

Second is DR maturity, RTO and RPO goals. That's also clear - when are we done? Non-debatable.

Third is breaking the monolith. That's where there is ambiguity, and lack of clarity raises concerns. We all know we as engineers can break a monolith for the rest of our lives and gold-plate the heck out of it. So the question is: what are the three to five things we need to do? When are we done? How are you ensuring that you're not underdoing it or overdoing it and doing tech for tech's sake?

Fourth is business continuity solution. Fifth - I'll send you the slide when I get back to a computer. But out of these five, the one that is most ambiguous is the monolith.

Those are the two things I need from you. Otherwise, Steve is like "we're 100% aligned, stability is what matters," but CJ, when are we done with this spike?

**Mårten:** Is the idea that when we declare victory, we can radically adjust the percentage of effort that goes towards stability?

**CJ:** We can radically change the pie chart of capacity allocation. I'm glad you brought it up. Currently, Steve and I are aligned - stability matters the most. He said to me one-on-one (I don't think he's gonna say this in front of a group): "Even if you guys are not working on stability, there's nothing else for engineers to work on. There is no clear product direction."

### Steve's Vision for Exchange

**CJ:** He laid out a vision for the first time. I'm glad somebody laid out a vision for Exchange. He said Exchange needs to be close to 100% self-service - EDI should go away. Curtis mentioned that too. I like that vision.

So your goal becomes - with or without Laura, you on your own - your purpose is to change the pie chart so more and more capacity can go towards that product vision.

### The Third Thing: Capacity Planning Narrative

**CJ:** That leads to the third thing you should be communicating: Currently my pie chart looks like this. In Q3, it's gonna look like this. In Q4, it's gonna look like this. That gives Laura the clarity and responsibility to start breaking down the vision Steve has into requirements that engineers can work on.

Otherwise, given we don't have this amount of radical clarity, if I'm in her shoes, I wouldn't even know what to do. Why am I working on vision? There is no capacity, there's no clarity.

**Mårten:** I was having this discussion at lunch. I'm not sure about Laura.

**CJ:** You're like "no, she's great." And she is great. Now she has an opportunity to sit down with Steve and say "what is your vision?" and do a bang-up job turning that into requirements and work with you to figure out how we execute on that.

**Mårten:** Just to be clear, I haven't seen her and her team necessarily work in that mode. At this point, their job is prioritizing a lot of smallish requests against each other. That's the mode I've seen them in. Given the circumstances, I feel like they're doing the best they can. But I haven't seen her and her team work in the capacity you're describing yet.

**CJ:** So there is a concern, right? Between you and me, I see that concern - whether she can do it. But all we can do as leaders is give people the chance. That's what we're gonna do.

### Next Steps & Timeline

**CJ:** Even if it is 60% accurate, 70% accurate, you gotta put something like this out ASAP. I'm gonna talk about this in the staff meeting on Monday. Once I promise that, then I need a date when we can sit down and review this.

I told Curtis that while he's in India, I'll make progress on this with you this next week. Now that you know what I'm looking for, when can we spend 30 minutes and review?

**Mårten:** Let's do it towards end of next week then, because the Summit's coming up. You're busier than I am, so if you want to just pick a time like Friday or Thursday.

**CJ:** I'll do that.

### Product vs. Engineering Ownership Discussion

**Mårten:** I wanted to ask your opinion about something related to what we just talked about. My experience and stance so far has been that product owns the roadmap - they're ultimately the decider for priorities. That includes everything: technical work, commercial work, anything. Because they're the only ones who have all the parameters, all the relationships, all the insights to make the trade-offs correctly.

In the prioritization discussion, we as engineers almost become stakeholders too - we argue for paying back tech debt or making upgrades, but ultimately product has to weigh that against everything else.

What we're describing here is that we really need to sequester a portion of that pie chart for technical work. We have something like 35% left over for product to use in their planning. Given our situation, that may be the right move for a while. But I wanted to get your take on it.

### The Ideal Operating Model

**CJ:** Let me talk to you about the ideal operating state - the target operating model. Even though it is laborious and hard to get to, there is no other way. This is how it should ideally work.

First, I'll actually challenge that product owns everything. In my experience, the problem is they are measured on revenue and margin - mostly revenue. In mature orgs, it's only about revenue, actually. Like Exchange, we don't even know the operating margin of Exchange.

**The ideal product role:** Delight customers in hard-to-copy, margin-enhancing ways.

If you break it down - and take notes on this:

**"Delight customers" has four metrics:**
1. Revenue growth
2. Customer retention  
3. NPS
4. Daily average usage and usage metrics

**"Hard to copy"** - a product manager should be able to say "here are the reasons why this product is hard to copy. This is what I'm doing in the roadmap to make it hard to copy."

**"Margin enhancing ways"** - this is where the rub is. You should have clear definition of gross margin and/or net operating margin. Gross includes infrastructure, etc. Net operating includes actual R&D, Christine's team, and all that.

**"Delight customers" should also include:**
- Stability metrics (standard DORA/SRE metrics, incidents)
- Quality metrics  
- Customer service tickets (Christine's stuff goes into delight as well)

### The Partnership Model

**CJ:** Ideally everything is measured, everybody has visibility, and we trust the product manager to make the best decision. In reality, they're only measured on some of those. When a security incident happens, they'll be like "hey Mårten, what happened?" That's why it's always a partnership.

In an ideal scenario, it starts with having these metrics and saying "Mårten, you're on point for these 10 metrics. Laura, you're on point for these other 10." What that means: I'm on point to report them, I'm on point to contribute to the product roadmap to improve them. But there are incentives because if the site is down, I'm gonna call you, not Laura.

That is where you have to say: "Okay, for me to be able to do what I'm accountable for, given the state of our metrics, I think right now for the next 3, 6, 9, 12 months, let's agree on where the product development capacity is going."

That is how it should work ideally. It's a little too idealistic and naive - almost passive aggressive - to say "hey, product knows best."

**Mårten:** I think we're aligned. That's what I was saying. For the time being, we need to operate like you're describing. Whether we ever fully get out of that mode, the future will tell.

**CJ:** Even right now you can get us to the idealistic state if you have all the metrics.

**Mårten:** One more thing that goes in somewhere - maybe in "delighting customer" - is around tech debt because that measures the risk you have.

### Priorities & Execution

**CJ:** I think in parallel, you should do all this work of metrics and breaking down this sentence into metrics and getting us to the ideal state. You can do it, there's nothing stopping you, and you must do that work. But it's a second priority.

**First priority:** Even without all these metrics, just create these three things. Then back into metrics.

I think it'd be good now that you are here - as I was telling you at lunch, Curtis had to do the Exchange engineering job. You're here. You know what good looks like. I actually feel pretty good. All this noise is gonna die down once we lead the way and show how it should be done.

**Mårten:** Yeah, I agree. If you don't deliver well, then you start getting micromanaged. That's kind of part of it.

**CJ:** All right, I'll set up 30 minutes then. Thanks, and have a good weekend.

**Mårten:** You too. Bye.

## Key Takeaways

1. **Two deliverables needed ASAP:**
   - Data-backed productivity improvement commentary (4 months in)
   - Radical clarity on monolith work: what are the 3-5 things, when are we done, how do we avoid gold-plating?

2. **Capacity planning narrative:** Show current pie chart and projected evolution Q3→Q4 to enable product planning

3. **Target operating model:** Partnership where engineering owns stability/quality/tech debt metrics, product owns revenue/retention/NPS, both contribute to roadmap

4. **Next meeting:** End of next week to review deliverables before CJ's staff meeting

5. **Steve's vision:** Exchange should be 100% self-service, EDI should go away 