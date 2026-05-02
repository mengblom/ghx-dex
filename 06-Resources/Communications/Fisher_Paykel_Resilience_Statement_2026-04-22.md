Ask from Nate Letcher (email on 2026-04-22):
- I am working with supplier sales on a renewal for Fisher & Paykel and they have expressed frustration with GHX major incidents over the last year or so.  Do we have a statement that I can share with Sales indicating steps we have taken and will be taking to address resilience over the last year?

I want to emphasize the following:
- Problems / Background:
	- Legacy infrastructure with limited automatic scalability (Lift and shift AWS footprint, self hosted MongoDB databases etc.)
	- Legacy / Monolithic architecture (high degree of coupling, shared databases, noisy neighbor problem, poor isolation/large blast radius)
	- Insufficient observability
	- Much of this comes back to us having outgrown original systems/architecture, without enough investment in growing and modernizing the architecture along with the growth of the business and volume
- Actions
	- We have recently gone through team transformation to a modern, product focused, engineering org (more nimble teams with clearer, narrower ownership, smaller safer deployments, quicker to react and address defects etc.). We are demonstrating our commitment to fundamental change.
	- We are in the midst of migrating our main databases to managed cloud services (MongoDB to Atlas), and splitting single clusters to multiple clusters for increased scalability and fault isolation
	- On an ongoing journey towards state of the art, loosely coupled micro-service architecture (easier to maintain/upgrade etc., better scalability, smaller blast radius)
	- On an ongoing journey towards cloud-native infrastructure (better scalability, better availability)
	- Current laser focus on drawing down outstanding incident root causes and customer reported defects
	- A renewed focus and commitment to Systematic reduction of technical debt vs. crisis-driven fixes




---

## Draft Response

Nate,

I understand Fisher & Paykel's concerns - they're valid. Here's what's behind the incidents and what we're doing about it.

**The Background**

We have had a number of incidents, each different, but often stemming back to some fundamental limitations:
- Legacy infrastructure with limited automatic scalability (lift-and-shift AWS footprint, self-hosted MongoDB databases etc.)
- Monolithic architecture with tightly coupled services - shared databases, limited fault isolation, large blast radius
- Observability gaps that made it harder to detect and respond before customer impact

Much of this comes back to us having outgrown our original systems, without enough investment in growing and modernizing the architecture along with the growth of the business and transaction volumes.

**What We're Doing**

- **Modernizing our engineering organization**: We have completed a transformation to product-focused, autonomous teams. The goal is narrower ownership and accountability, smaller safer deployments, faster response to defects. We're demonstrating our commitment to fundamental change.

- **Database modernization**: We are in the midst of migrating from self-hosted databases to managed cloud services. We are splitting single database clusters to multiple smaller clusters for increased scalability and fault isolation.

- **System architecture modernization**: We are on a journey toward loosely coupled microservices architecture, hosted on cloud-native infrastructure. Smaller blast radius, independent deployments, better scalability and availability, easier to maintain and upgrade.

- **Ongoing incremental improvements**: We have a significant portion of our roadmap for Q2 and beyond dedicated to systematic reduction both incident root causes and customer reported defects. 

This is a multi-quarter transformation, but we're committed and making tangible progress. Happy to discuss further if helpful.

Mårten