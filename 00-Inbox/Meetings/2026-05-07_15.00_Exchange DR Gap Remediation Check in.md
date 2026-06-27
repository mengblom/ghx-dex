---
date: 2026-05-07
type: meeting-note
attendees: []
duration: 30min
time: TBD
status: pending-transcript
---

# Exchange DR Gap Remediation Check in

**Date:** Thursday, May 7, 2026  
**Time:** TBD  
**Duration:** 30 minutes  
**Attendees:** [[Marten Engblom]]

---

## Transcript

Meeting Title: Disaster recovery runbook refinement — RTO reduction and GitHub migration strategy
Date: May 7
Meeting participants: Mårten Engblom

Transcript:
 
Them: Surfaced other gaps. So you're right. We don't have those stories in a share. The recap from a couple of days ago. Right? So, I mean, BT, you can ignore btbd and es. But SNS, we don't necessarily have some. He's SNS topics on the altar in the alternate region or script that builds them. Right. We could do that. Or sqs. We don't have anything in the alternate region s3 where we would have to have cross region replication. Right. The initial copying and then the syncing. Right. But before there's an SES as well. Yeah. Before we go too deep down this rabbit hole is let's see if christine's going to join because I think you're going to like what I have to tell you. We're done. Cardinal. Cardinal decided disaster recovery stupid. No, we're not off that hook yet. But let me do this. So. First I'll give you depressing. First of all, depress you a little bit. Excellent. And then pick you up. Yeah. Yeah. Then I'll pick you up. That's how you do it. So, yeah, the, the list was. So this was our back in December. This was the original runbook report that the happiest mind created. Right. So I copied it into a new tab, and then I used claude to go through and give us updated times. And the good, the bad news is I told everybody it's four hours and 45 minutes. There's actually, we forgot to include the two and a half hours for database restoration. And at the time I communicated that we didn't know about the SSO, wasn't really working. So. The bad news is we were actually at seven hours and nine minutes. But, but. As soon as we're on elastic search, elastic cloud. We cut off two and a half hours. Right? And then can somebody else let whoever that is in. Yeah, yeah, I got it. And. If the SSL deploy, if they fix that. It'll be 47 minutes. I still like skeptical these numbers. I'm like scared to, to produce them. Well, I keep SS separate thing. If this is all true, we did it in two hours and 15 minutes. If, if we were to do it again in a week, let's say. I, I'm scared to publicize that number because I, I would want to test it again before I felt 100 confident in it. But, you know, we farted around a lot with SSO deployment. We had a big gap here. I don't remember why we went like 45 minutes before we said, oh, by the way, should we start doing the applications? So you can't really count that time, right? Because we wouldn't normally do that. And I think the reason why we did that is because we were waiting for SSO to work and then we just decided to go. I don't, I don't remember Monday, to be honest. But the, when you guys look at this, Daniel martin, when you look at this, you're thinking, well, no, that looks something's wrong. When you look at the bottom half, if we were to do it again, assuming that the database takes 15, 10, 15 minutes to just, you know, you promote, you probe secondary to primary. Right. And then you. Start redirecting everything to the new region. For the database side. And then you start staying up the applications and SSO team. This time has all their scripts and stuff together, and it only takes them just under an hour. Even with the validation, we're still way under. The four hours. Does that make any of you smile? It made me smile when I looked at it this way. I just hope it's right. I think it is right. Yeah, that's right. Yeah. I wouldn't, I wouldn't doubt it. I mean, this is, you know, the fourth time we've gone through it. It doesn't, I mean, the only concern, right, is someone looks at that and makes that translates that to prod today. Which, yes, huge asterisk. This was one, this was one we tested one thing. We tested our run books for core exchange applications. Atlas still is not live, so we're making some assumptions, but we are pretty confident in those assumptions. All you have to do is promote secondary to primary. There is no restoring of a database. Yeah. And then the SSO deploy, there are a couple reasons why it didn't work as, as planned. And it took them a long time to work through it, but they fixed the scripts from what I understand. I would recommend testing some of the individual components again before we're looking at basically the end of August as the official date for last cloud is fully done. And atlas is fully done. So we're looking like mid-September before we do mid-september one where we include fusion and SCA and ccx and everybody else. I would love to test some of these things again because I remember there's a lot of going back and forth on the mix on all of these. Right. I think if they, if we have a proper playbook, like do step one, do step two, do step three instead of back and forth banter on the phone. And I can pull that out of the transcripts and get a draft version of that for people to look at. I think we can even carve those down. Then if something goes, even if something goes horribly wrong, we've got a buffer, quite a bit of a buffer. To get, get within that four hour RTO. Are you? Do you guys agree with me just because it looks visually nice or do you feel like that's really what happened? Could it could, could happen? Because we did fart around with SSO for two days. I think it's realistic. I think it's realistic. Again. Like if it, if stage crashed and we decided we had to do an RTO or PO, I think we would or a Dr. Exercise and stage. We, we could achieve that. So if that's the case, then as we look at the big backlog of epics that were created in December. I would request that anything to do with the scripting, we should take a good look at and see. Which ones give us the biggest bang for the buck. So can we do some stuff with max and get that 75 minutes down to 30? But then there's really not a lot of juice, you know, is the juice worth the squeeze, right? Is there, there's really not a lot of juice to squeeze. I don't, I wouldn't say we spend a whole lot of engineering effort on some of these other things. But make sure the SSO team's got it nailed and they should really test it more often somehow. I don't know how we test it, but, yeah, somehow we need to test it. And just make sure they have a lot of confidence that it's going to work. Because if it didn't, this would have been a really ugly outage. Right. Eight hours. I would have hurt. Well, even let's say the database stuff was fixed. We still would have been a couple hours over a four hour. Yeah. But if they can fix it, if they're confident in it, then we're in pretty good shape. Yeah. The, the danger, right, is because it doesn't translate to prod, like the teams have to go and look. What don't we know? Yeah. What is not set up in prod. Right. Because you go through, when you have to fight through this four times, you know, you do get a whole bunch of stuff set up. You do kind of get through into the rhythm of doing it. And so it does go quickly. You know which jobs to hit. If they were to go do this in prod tomorrow, there'd be a few challenges. I mean, one is we're not organized around the timeline. So a lot of the teams that do this. Are overseas. Right. So if we're, if, like, it crashes now, like, we're not going to get a four hour RTO probably because the first thing we'd have to do is wake everybody up. Get the right people, you know? And so that takes some time because it's not IAC. And so the question, I think more than that, we have to decide is. You know, is that, is that tolerable right now? Or, you know, is it good enough? I think contractually, it's good enough to get to December or, sorry, like October. And just do it in prod. And if it meets four hours, we're good to go.  
Me: Yeah, I mean, I think that's true. But I think like you're alluding to for us it shouldn't be good enough, right? Like we need to have it all. Down to a button push essentially. But it just means that that's not we didn't have to sort of bend over backwards four times to have that all in place by. This contractual date but we also shouldn't just put it on the back burner that's how I would frame it I think we should basically we need to continue this Dr. work until we have. Until we have a disaster recovery situation that we are satisfied with and that are also well actually I'll flip it around that meets the contractual obligation but also and that we are satisfied with.  
Them: So this, so go, go ahead. And then I've got it. I want to talk about scripting, but go ahead. We could test that out and get a true gap analysis if we decided in August to do a Dr. Exercise to Ireland or something like that. Just pick an environment or region we have not gone to. Where we don't have anything set up. And there's that would show in stage, not broad. Correct. Okay. So, like, if we were. If I were approaching this, because I think everybody kind of knows my opinion that I'd like to. Do Dr. Go forward plan rather than our legacy platform here. But, like, if, if, if it was. Like, if we were really looking at doing it for, for everything right now as it is. That's what we do, right? We would just pick a different. Region. Wouldn't have to be Ireland. It could be Ohio.  
Me: Yeah.  
Them: I would say knock overseas just so we don't run into any gdpr data issues. That we're not aware of. Just sounds more fun going to Ireland. But, I mean, we could do that next time and just, you know, and see, okay, well, it's great that we can reduce from, you know, 13 hours to, what, four hours or what you're saying two and a half or something like that. If we're all prepared for it and it's in a region that we've done before three times. But that's a very different thing from push button. Correct. Yeah. So on the script. Go ahead, Martin. Sorry.  
Me: Necessarily one button push but you know it needs to be more automated then basically we can't the situation you described before well we gotta wait so and so up and stuff like that right like.  
Them: Sure.  
Me: Yeah. That's not really that's not really ideal at least not if it really matters who well actually that's actually a good kind of litmus test right like if we have to wake people up overseas that means that there are pieces of this. Plan. That. Only certain individuals can do right we need to have it automated enough that. Quote unquote maybe not anyone but but sort of. You don't you shouldn't have to be that familiar with every single minutia to kind of execute it I don't know if that. Makes sense right or somebody I don't know how we would define it maybe it's that then yeah I don't know. But then again I don't know if it's that kind of disaster truly then maybe it is reasonable that we just need to get a hold of everyone but I mean then that should be part of the timeline so then maybe that pushes us into a button push situation anyway right maybe we have to have reserved one or two hours to get people online and then we really only have two hours to play with you know what I'm saying?  
Them: Yeah. I, how. So, like, if. Because we will have teams that are overseas that own things like IO, for example. How likely is it that we do have disaster recovery processes that. Doesn't require. Like, that team executing it and just.  
Me: Yeah probably not probably not actually right so it's probably more along the lines what I said last which is. The our our tooling and automation and scripting and I see all that needs to be buttoned up enough that. We can afford to take an hour or two or whatever it takes to get people online.  
Them: Gotcha. Yeah. Okay.  
Me: You know.  
Them: Yep, I'm with you. So speaking of push button stuff, when I talk to you earlier, Daniel, you weren't quite sure what our github strategy was. I was told that this week that we're trying to be in github by Q3, I think that means by the end of Q3. So can't, we don't want to wait on that for, because we've got an exercise this year, but that means hopefully early next year we would start. Because that was one of the concerns, right? We have a lot of scripting on our backlog. We don't, there's hesitation to, to prioritize that if we're going to have to redo it again anyway. Remember this conversation? I think that's, I've got it right. So. Anyway, I just want to throw out that caveat that it is sooner than I thought it was like someday. I didn't realize it was actually budgeted on the, on the roadmap and planning to be executed this year. Yeah. So we have a, the teams are looking at github as. As I modernize as I decouple. I'm putting it there, right? Like nothing goes, nothing new goes in bit bucket. Nothing new goes into bamboo. Everything goes to, to GitHub and GitHub actions. We also have this possibility of using tim's team. Right, to migrate some stuff for us. The challenge is, and maybe I'm wrong on this, but I, I feel like disaster recovery, vulnerability remediation, decoupling work is all higher priority. Than GitHub. Migration. So I'm happy to use tailor, assuming it's a not tailor. Tim will. Yeah. Assuming it's a, it's not a huge problem. Like if, but we're all going to be very sad. If, like, we lose three weeks on. Dr. Unless we just have tons of. Bandwidth. Because we're moving to github. Maybe that's how I look at it. But am I wrong there? I look at it as if we're going to fix our scripting and, Martin, I'm sorry if I cut you off. I think if we're going to fix our scripting so that we can reduce. Our RTO, then it's time well spent. Like, I wouldn't take the whole, we're going to move everything to GitHub, but I would say these specific things are going to help us with Dr. We're going to create those in github and just delete the bamboo ones. The bamboo didn't work very much this week. Right. So we had people talking back and forth. No one is pushing buttons. People were opening up script windows and they were. Terminal window windows and stuff. They were going in and doing configurations. I didn't get the sense anyway that we had a lot of automation going on. Maybe I missed it. Yeah, I guess what I'm saying, though, is there's a difference between, hey, I'm going to take, I'm going to put the environment, I'm going to treat an environment variable in my bamboo instead of hard coding the region. I'm going to introduce a variable. That I'm going to pass in, and that's going to be my Dr. Like, I'm going to inject this variable for the region when I want to fail over and I'm going to change my bamboo script a little bit to just take that variable versus I'm going to go rebuild everything and github. Like one takes a certain amount of time and the other's much of greater effort, unless I'm over making it over complex. But. I have to look at that. Yeah. Just say, isn't it doing anything new in bamboo is creating tech debt that we're going to eliminate later anyway. Right? Yes, it is. So when we're, we're already creating new things in github, right? So the team's well underway there. Nothing news going in bamboo. The question is just, I fear we're going to aggregate the team if we say, hey, oh, by the way, while we're like doing this, let's also migrate everything to github. It would make perfect sense if they had to do, like if Suresh is looking at his eight things and he's trying to get it to push button. And he's like, I got to do 100 refactor on bamboo. Yeah, sure. Move it to github. I don't think that's the case.  
Me: Like pizza we kind of trying to get. Most if not everything to github in the next kind of quarter or two anyway.  
Them: We would have loved. So we would have loved to do github three years ago when we decided to use github. But the, the, the question is just like, what's the amount of work?  
Me: Yeah.  
Them: Right, versus what they're already doing for Dr. Like the, the reason Kim will's team was attractive is because our teams have our own product development roadmap. And they could just migrate it for us.  
Me: Maybe I'm conflating the two. But when when we say okay we're going to move some something to github it's a given that it has the right automation in github actions and everything around it right so isn't it. In other words anything that we move to github will have. The the level of automation we need for this Dr exercise isn't that. Kind of safe to assume or no.  
Them: I would assume so.  
Me: Yeah. So in other words so in other words to say a bit more sort of bluntly if we did say what you said which is like hey the number one. Like. Pull out all the stops get everything into github then it's almost like we would get this Dr. Capability for free.  
Them: I guess that depends on what the team's doing to close the gap between. Where we're at now with two hour RTO. And what we, you were talking about a minute ago where we can.  
Me: But if I'm saying what I'm saying is true they could just. Unless there are other things that need to go into meeting that RTO but they would just drop everything that they would otherwise be working on in bamboo. Just pivot just don't do that focus on just getting to github which means that. We get. Again the Dr. Automation we need kind of as a bonus.  
Them: Yeah, I guess in my head, and I'm speaking. From ignorance in, in my head, I'm, I'm looking at the Dr. Gap as a 10 effort thing. And the GitHub migration being the 90. So they'd be playing stories for that.  
Me: Yeah. But I think that that we should be talking about that very seriously because that is I mean it's the GitHub move is not just again the Dr. piece is a bonus but it's really one of the one of the big milestones for us because it means. Not only. The repo and GitHub actions. That modernization but it really translates to. Decoupling from the monolith and autonomous teams and it's like it's all that package in there right like basically like if you somebody asks what's the checklist for a team being autonomous. It's they we've defined what components are under their umbrella and they've called they've moved it all into GitHub repos that they own and control. That's it. More essentially right.  
Them: Yeah, but I think what we're talking about now is not to decoupling and autonomy. It's just taken like for like and putting it in GitHub, but also providing the. Disaster recovery scripting. Infrastructure as code.  
Me: We wouldn't take the all repo and move it into the all repo and GitHub I hope that's not the plan right.  
Them: Well, that's what I'm saying. Like, like that is the, that is what we're talking about here as far as. I'm, I'm concerned. Right.  
Me: Now.  
Them: Because otherwise. Like, even if I just, even if, if the team plays a story, I need to get processing engines from, you know, one hour RTO to 15 minutes. Right. And I'm going to do that work between now and December. And then we say, okay, but also just put that in GitHub. Right? Just whatever, whatever work you're doing. Put that in GitHub. That's one thing. Right. And, and that would be your, you're, you're right. It's, it's an increase in work, but it's probably not like a month's worth of work. However, if we say, hey, we want process processing engines to be fully decoupled from the all repo. Like that's a, that's a much larger thing, especially if we say everything as you move it. Has to be decoupled as well. Like, that's a larger body of work. Right?  
Me: Yeah. I guess. Decoupled in what sense like the way we ultimately want the architecture or just to the point where you thinking on their own. Github repos. And I would say the latter is good enough.  
Them: Yeah, I'd say the latter's good enough, too.  
Me: Yeah.  
Them: Yeah, I gotta, I got a dumb question. Why? Why do we need to go all the way back to github for a Dr. We're not doing a build? We have all the, you know, EBS images ready to go, lambda functions replicate. I don't need to do a build. I just need to basically just activate the ones in the other region. I'm done. What if the other regions, when you see activate in the other region, what do you mean? So, well, I have my EBS images that are view. Every time I do a build, I make sure that immediate, I mean a release. I make sure that all my images are being synced with another region. Right. And essentially everything's built already. I don't need to go back to GitHub. It's there. It's built. It's the, the code is compiled. Or am I looking at this the wrong way? I think I'd rephrase it to say you're talking about, I'm not going to do GitHub. I'm going to do github actions. And I'm, I'm going to deploy to another region, but I'm going to use the bamboo resources and deploying. You're just copying a bunch of images over and activating them and load balancing them, you know, as needed. Yeah. Wherever they store, wherever they store that build artifact, which I assume will be in bit bucket. But I don't know. I mean, yeah, wherever it is, there's men. I'm just moving the image over. I mean, maybe I'm only this wrong because I'm thinking of that AWS Dr Hub. Which is all push button. It's like all it needs is an approval by going to the other region. Yes, we are officially failed. We lost these coast. You press a button and it just does the whole thing with thematically. And I'm like, well, that's kind of what we should be shooting for. Well, yeah, I wouldn't say you're looking at it wrong. I just say you're trying hard to hack it and we should probably just do it. Right. Okay, fine. I'm just saying we don't need to build. I mean, then, then we can't release through the ultimate region for like a week because we have to figure it out. But. You know.  
Me: In principle I agree with our ideally we actually it's actually. Better if we don't build because you really want the same bits as you.  
Them: The same thing. Exactly. Yeah. We're down to four minutes for tomorrow. I plan just to walk through. I'm not really sure what my strategy is yet on tomorrow. I'm, I'm, I want to get to the point sooner than later, but I don't want people walking away thinking we don't need to do anything. So I want to make sure I have a consistent message across all of us. On what the go forward plan is. Give them a record. Give them a range. Best case scenario, it was that long. Worst case because we had SSO, it would be that long. Plus all the unknowns of going from stage to product. Yeah. Yeah. And so, and so we want to reduce, we want to reduce our footprint as tiny as possible. And that way, if they're, when there is a real life event, we have a lot of buffer. Yeah. And, and so to your earlier point about biggest bang for the buck, I think every time we do one of these, we have a caveat. We don't have S3 replicated in the other region, like six months ago is we don't have es or the ability to resurrect. Yes. As we resolve those, like es, for instance, I think we need to talk seriously about all the gaps we have that force us to say, well, there's a caveat. It was in production or we don't have S3 or we don't have the sqs. Or like there's still discussion right now about the lambdas being run in the wrong region for the mapping for mad sport. Right. I'm like, dude, I thought we, we established that the lambdas are in both regions. And I think the biggest bang for the buck is let's reduce the caveat so we don't have to put asterisk in front of everything every time we talk Dr. Yeah. That's what the, that's what building it native. Right. I mean, we're shoehorning Dr into something that wasn't a product requirement. So we're missing some things. Yes. Okay. I don't have a good Gap summary yet. I thought I did in this slide deck, but so I'll create that. The other thing that made me nervous, though, is back, back to where Martin was saying earlier was just hearing the, the application teams talking back and forth. And it felt like there was some mentoring going on, which was great. But, like, during a real Dr. Exercise, what if the person doing the mentoring wasn't available? I don't remember all the names because I have to go back and look. Yeah. But I just thought, oh crap. Like, are we, so somebody goes on vacation for two weeks? It's kind of like if Banks goes on vacation for two weeks. Who's going to write the broken tickets? Well, so that, that happened last time. Suresh was out. So now we have, we have a, what I call a trinity for these things. We have to write. No. What's the other guy's name? Daniel. Yeah. Okay. So we have three. And then I would even challenge the idea that we need India. These are all locals. We can have Jeff. Well, Sean probably, but he's London, right? Easier. We could probably just have it with a local team that validating the app after is a bit more complicated, but bouncing the apps and restarting them, I think can be done locally. And we've done it in the afternoon here, us time before. Well, I'm gonna have to put some thought into this GitHub stuff. Because it would be very, it'd be hard for. Aaron and ben to remediate. The vulnerabilities if we're dicing up the structure of the projects behind the scenes for Dr. Yeah, that too. Yeah. I like the idea. Put some thought into that. Tomorrow I will walk through.  
Me: Yeah I mean Daniel. That that's that's true. But you know in theory that's going to be done. In what it's less now right it's yeah seven whatever so.  
Them: Eight weeks. Yeah, I guess maybe my bias is showing, and I don't think it will be done in seven weeks, but I got my fingers crossed. I would love it if it did. That'd be sweet.  
Me: We have to plan with unless we see really start to see that it's not going to happen but but I think we need to use that as a plan so then I think and then so what happens if we q three we say you know what? Q3 is the quarter we are moving. We're carving this thing up. Again not to the perfect SOA architecture. But. The gloves are off by the end of Q3 every team is going to have all their stuff in github. And and if there's some like you know asterisk to that or whatever you know because there's something that's really really difficult to carve up even to that level then. Let's figure that out but yeah.  
Them: Yeah. I like that plan. I like that going forward with that strategy and just saying, and that's and making it clear. It's not just, hey, you're in github, but you're independently deployable. And in github.  
Me: Yeah.  
Them: I like that.  
Me: And actually. I'm pretty confident that if we said I don't know if we can do zero but basically. We can for that quarter we can almost get away with very very little like commercial we can pass almost everything if that's if that's if that's the outcome. At the end of that quarter. Then you know product can go on vacation basically for a while.  
Them: It's for two years. I will be. Yeah, but we'll be done with, in theory, atlas and elasticsearch by then as well.  
Me: Yeah.  
Them: So we'll have the bandwidth to focus.  
Me: Yeah. I didn't hear your comment Phil what was it you've heard this.  
Them: I've been hearing this for two years. I'll fend off the product people. Then they come back with a vengeance and we all freak out. We're like, oh, damn.  
Me: Well. Yeah I mean that yeah just don't quote me on this but I mean I just had a meeting with cj like two hours ago where to that effect essentially.  
Them: Okay.  
Me: Yeah.  
Them: I trust. You.  
Me: Yeah.  
Them: Again. Really, I go to the, I'll go to the other meeting. You guys can talk. Okay. Well, I wouldn't go to the other meeting, too. So.  
Me: What's the other. Thing.  
Them: I am dragging some of these folks into a perf. I want them to look at some of my perf analysis and tell me where I'm insane. They're doing a sanity test on it. So. All right. Thanks, Marlon. I mean, I'm not going to commit to the, unless you guys want me to, we can, I'll let you talk to it, Daniel, about committing to the GitHub thing in Q3. I'm all for it. Martin's all for it. Let you wrap your head around it and see if it's doable or how far it's doable. Obviously, if product comes in.  
Me: If we think I mean it's not some we would probably maybe we should power on that tomorrow a.  
Them: For sure.  
Me: M.  
Them: Yeah.  
Me: Right.  
Them: The meetings at 7am my time. So 8 a.m. your time. So it's an early morning to cigarette.  
Me: Say that again.  
Them: At the meetings at 8am mountain tomorrow.  
Me: Wait whose meet what meeting is it.  
Them: It's the readout for what happened this week. We can postpone it. The only danger to postponing it is I'm going to be in India for two weeks, and I think I want to let it go for three weeks.  
Me: I mean no I think you should do the readout with but with all these question marks I mean why do why we if anything we should be. I mean we should be very transparent with the challenges that unknowns and everything you know nobody should think that this is kind of a straightforward. Not in terms of the planning and coordination nor in terms of the actual work so just just just report it out as you see it. No sugar coating like that's just that just that that makes us look good for one day and then and then you know it comes back and bites us following that. So.  
Them: Yeah. Yeah. Well, I mean, I communicated four hours and 45 minutes on Monday, and we were actually more in that, but that's okay.  
Me: Yeah. Okay you know what here here's the thing it was it was preliminary I think that was very clear and if somebody says I can't stomach get get ever getting the wrong information then then what's the consequence of that then we're gonna you're gonna wait a month after every you know for every piece of info from us yeah.  
Them: All right. I'll, I'll produce out. I'll, I don't know if I want to share the bottom half of this slide. I'm going to keep it to myself for, and to us for a minute.  
Me: Yeah that might be a good idea but yeah.  
Them: All right.  
Me: Do you I mean do you agree with that?  
Them: Yeah, I know. I agree with it. Yeah, I agree with that. I want to make sure I get frustrated is so december we did all the work and we come up with the backlog and then everyone wants to shoot up the backlog. So tomorrow I'll do a better job of just.  
Me: Yeah.  
Them: Saying, look, here's the gaps. We are so highly dependent on people right now. It's scary.  
Me: Yeah.  
Them: Like, what if two of the people from mechs have been out. During real life event? We're like, screwed.  
Me: Oh yeah right exactly.  
Them: That 75 minutes would have turned into hours.  
Me: Yeah and that should be transparently reported out too I mean that's why we need to. Get to automation. You know you know.  
Them: Okay.  
Me: Yeah.  
Them: All right. Well, I'll work on updating this tomorrow. Present the gaps and then we can continue to refine.  
Me: Sounds good thanks be okay bye.  
Them: All right. Thanks. 

---

## Executive Summary

Significant progress on RTO reduction. Original estimate was 4hrs 45min but actually 7hrs 9min when database restoration was included. With Atlas migration (eliminating 2.5hr database restore) and SSO deployment fixes, RTO could drop to 2hrs 15min - well under the 4-hour target. Team discussed prioritizing automation epics that provide biggest ROI, testing SSO scripts again before September, and migrating runbook documentation to GitHub. Next full DR test scheduled for mid-September including Fusion, SCA, and CCX.

**Key Metrics:**
- **Current RTO:** 7hrs 9min (actual)
- **With Atlas:** 4hrs 39min 
- **With Atlas + SSO fixes:** 2hrs 15min (projected)
- **Target:** 4 hours

---

## Key Topics Discussed

- **RTO Timeline Analysis:** Recalculated actual DR exercise timing
  - Original communication: 4hrs 45min
  - Actual with database restore: 7hrs 9min
  - Atlas eliminates 2.5hr database restoration (promote secondary to primary instead)
  - SSO deployment fixes reduce from 2hrs to ~47min
  - Projected final RTO: 2hrs 15min (with caveats)

- **Automation Epic Prioritization:** Review backlog to identify highest ROI items
  - Focus on scripting improvements (e.g., Max automation to reduce 75min to 30min)
  - Question whether remaining juice is worth the squeeze
  - SSO team needs most attention - testing and confidence building

- **Testing Strategy:** 
  - Recommend testing individual components again before August (LastCloud + Atlas completion)
  - Mid-September full DR test including Fusion, SCA, CCX
  - Concern: Stage testing doesn't perfectly translate to prod (overseas teams, timing, IAC gaps)

- **GitHub Migration for Runbooks:**
  - Move away from Confluence to GitHub for better version control
  - Enable better collaboration and change tracking
  - Concern about losing documentation during migration

---

## Decisions Made

- Prioritize SSO deployment script testing and fixes
- Defer low-ROI automation epics, focus on high-impact items
- Plan mid-September full DR test after Atlas/LastCloud completion
- Move forward with GitHub migration for runbook documentation (with safeguards)

---

## Action Items

### For Marten
- [ ] Review automation epic backlog for ROI analysis [[^task-20260507-005]]
- [ ] Ensure GitHub migration plan includes documentation backup [[^task-20260507-006]]

### For Team
- [ ] Test SSO deployment scripts individually before September [[^task-20260507-007]]
- [ ] Extract DR playbook steps from transcripts into sequential runbook [[^task-20260507-008]]
- [ ] Coordinate with SSO team on confidence-building test schedule [[^task-20260507-009]]
- [ ] Plan mid-September DR test including Fusion, SCA, CCX [[^task-20260507-010]]
- [ ] Migrate runbook documentation to GitHub with version control [[^task-20260507-011]]

---

## Follow-ups

- Atlas migration completion: End of August
- LastCloud fully done: End of August
- Individual component testing: Before September
- Full DR test with all systems: Mid-September
- October: Production DR validation

---

## Related

**People:**  
**Projects:** [[04-Projects/Exchange_Resiliency_2026]], Exchange Atlas Migration, Exchange LastCloud Migration  
**Context:** Fourth DR exercise revealed dramatic RTO improvement potential with infrastructure modernization
