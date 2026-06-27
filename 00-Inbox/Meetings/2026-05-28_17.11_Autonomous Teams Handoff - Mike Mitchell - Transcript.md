### Granola Transcript ###
 
Me: Okay, so. All right, so we talked about this already that I'm kind of asking for your help to shepherd this.  
Them: Yeah.  
Me: You know, getting to at least these initial stages of getting to autonomous teams, right? So you saw the email I just sent out. I don't know if you did. It was, it wasn't that long ago. It's just clarification on. How that we should. Most of the technical work that we do that we plan. In Q3. And it's probably going to be this hopefully the same story for Q4 is going to needs to be rolling up to. What we actually need to do, right? So it's basically red methods, which hopefully should be. Certainly should be closed somewhere in. I mean, ideally it should be closed very quickly, right? Like almost not spinning even over into Q3. It will probably, but it's going to be. Yeah. And then we have disaster recovery, which is a big one. And but beyond that, it's autonomous teams. Like we just need to get there. Right.  
Them: Yep. Yep.  
Me: Now, I'm hoping that. If you fast forward a few months. That's. The main, if not the only thing we're going to be focusing on. But for now, we have these three kind of competing priorities.  
Them: I agree.  
Me: Yeah. And just the way the chips have fallen, Daniel is running the Dr. thing. Aaron is running the red mythos thing. So I'm asking you for help with this. At least this initial phase of autonomous teams. And again, if you fast forward a few months, we'll probably just all pile onto it. But for now, it's just some blocking and tackling. Right. Yeah. So I think it basically boils down to this, the team standards that we have put in place or start. We need to finish that out. And then. Get teams to just. Get to that starting point. Basically get all the teams to be able to check all the boxes. In that list that we're generating.  
Them: Okay.  
Me: So that's number one. And then kind of closely following, right, we have also talked about each team needs to.  
Them: Okay. Yep.  
Me: Have a very well defined list of what is their domain. Like what is it that they are going to own? And then at that point we will have to do a group type of review exercise where we kind of compare notes and make sure it all makes sense. I would be shocked if each team wrote that list and it's like, it's a perfect, you know, it covers the whole domain. There's no overlap, no disagreements. Like that's not going to happen.  
Them: You're doubtful, huh? You're doubtful.  
Me: Yeah. And but again these things that I'm describing, it's really the teams need to do it. I mean in some places we have gaps, right? So that's where because Daniel hasn't a few teams that are not staffed up. So we have to kind of. It's not a picture perfect scenario in that sense. But for the most part this is really not doing the work. It's like, hey.  
Them: Yeah. Yeah, yeah. I'm with you. I'm with you. Yeah, it sounds good. Sounds good.  
Me: So there's the team standards, the domain ownership. And then with that. This is probably a step after, but then like, okay, now what are the coupling points? What's going to be the. Long pole in the tent for each team to get. To an autonomous situation? And here's where strategy is going to start to differ a bit. Some teams might be like, yeah, you know what? Here's the list of our services.  
Them: Yeah.  
Me: It will only take us two or three months to like move them all to github and whatever. You know, some teams might be like, you know what? That is never happening. We're going to have to. Like, we're just going to create our own monolith for a bit. Or you know what I mean? Like it might be. Yeah. And that. S, but we at least need to get visibility to that. And then. And this is probably the last piece in what I want to talk to you about today. Like we do need to start sketching on kind of a target architecture. And this is probably something we need. I don't know how big of a group exercise it should be. It's. On one hand you want like all the experts and opinions, but you don't want too many cooks in the kitchen. So I don't know, maybe we brainstorm a bit on this. This is kind of after the other things I just talked about.  
Them: Sure.  
Me: Right?  
Them: Yeah. Yeah.  
Me: I don't know what else comes to mind. Like what do you think? So what do you think?  
Them: Yeah.  
Me: That's missing from that like initial playbook here?  
Them: I think one of the things I was going to ask you, like, okay, so as we talk about decoupling. And so what are your thoughts on this path? Right? There's a lot of. Ways you can take and drive this path. You know, I think we all understand the target state, the endpoint. But I was thinking that. You know, maybe there's two phases. I'll break it into two first. And probably a lot more detail inside this. Right. But there's the code part and then there's the data part. You know. And the code separation, not that it's simple. But much simpler than the data part. Right. So when you talk about like domains and architecture. In order to, to make progress and to get everybody on the same page. My thoughts were, okay, let's talk about the code. And let's not worry about we're sharing the data. We're, we're living in that world of sharing the data today so we can live in that, that world a little bit longer. Right. But getting toward code separation starts to feel good for each team then because it's like, ah, now I carve out my boundary points and I can start to see where I'm going. Right. And then we start to separate into the is a phase two, let's call it where we start that messy untangling of the overlapping of data. And they're similar to what you said earlier. There's going to be some teams that are like, good luck guys. That's not my world. I'm clear and free. I can go right. And we can set the path of what that looks like for them. Hey, you're off and running. Go for it. Right. Follow those standards. Talk about do all those things. But there are others. It's going to be a little more, you know, discussion and figuring out exactly where the boundaries are and oh, there's some, there's some data that's just so tight between it. You know, we're going to figure out how do we sync it maybe? Or, you know,  
Me: Remodel it or.  
Them: Right, right, exactly. Exactly. So but if we go down the path of, hey, let's just.  
Me: You know.  
Them: Clear the road and get everybody going one. I think we're going to hit a breaking point where we're like going to stop because we're going to get into this data issue. So what are your thoughts on that?  
Me: Yeah. Well, I think so this initial target state, I think we've been explicit about saying it doesn't have to include it. It probably actually doesn't include the data. Yeah. Because and here's how I kind of justify that and tell me if I'm wrong. I don't think that we make changes to our data that often. So in other words like the fact.  
Them: Schemas?  
Me: Yeah schemas and contracts or whatever. So in other words like the fact that we have shared databases and the fact that we have coupling, let's say in the data layer is not a problem for us that often. That's my impression at least. Now it's a problem in the sense like noisy neighbor and like all this stuff. Right. But as far as like a team being able to just kind of deploy their changes without blowing somebody else up.  
Them: Okay.  
Me: I have the impression that that is not as much of a problem as the code piece.  
Them: I think you're right. But I'll tell you what's simmering for me a bit and I can't, I don't know, is that it's hard for me to imagine with all this overlap and common data that some of these. Weird unknown things that we see happen and we can't explain aren't somehow related to that. You know.  
Me: I agree with you. So it's definitely it's not that we don't want to do it. It will be a very.  
Them: So.  
Me: Quick follow phase too. And listen, if we can get there sooner than later, that's great.  
Them: Yes, yes. I agree. I think the huge victory to get the phase one part done, right? That's a huge victory. And like I was when I was talking with critique about this, I was like, look, let's separate the code. Oh, and I was talking to john. Sorry first actually because he was like, oh, we're going to create all these epics and we're going to do all this. And I'm like, I don't think you need to do all that, you know? And it's more about getting the front end part of it done and then coming back later. Because you just don't know what you're going to run into with all that at this point. It's not worth digging into that. Yet.  
Me: I would almost say also that put that potentially there's even a phase zero let's say before that phase one, which is the code. So the phase zero and I'm I hope we don't have to use phase zero but. If absolutely needed I would say there's maybe a phase zero which is even the code is not completely separated. But at least the deployment is.  
Them: Yeah. Totally. I would love that part. Oh my gosh. Yeah. Yeah.  
Me: So and I don't know if it's if it can could work this cleanly because maybe there's enough there's enough really hard messy coupling in the code that it wouldn't that it basically would be pointless. But in theory at least. You could the code could stay where it is and but each team now has their deployable pipelines that only deploy. To their services basically the infrastructure that they own. You know what I mean?  
Them: Yeah.  
Me: And that's going to have lots of restrictions on it. Because here you can certainly blow somebody else up. Right. So I don't know but it's definitely something to think about.  
Them: Yeah.  
Me: Right.  
Them: No, I totally agree. And the other part of the discussion I was having was that make it, make it about the code first. But if there's data that. Unquestionably you own, no one else is take it with you. Right. And no one's else is peeking at it or, you know, whatever. Take it. Take it now. You know, and get there. But, you know. I think we're just not familiar with. How to deploy on our own. And so getting this separation will be so much better. Right. And. I mean, think about it, not even doing our own merges. It's crazy.  
Me: Yeah I know it's crazy. Yeah so yeah that is definitely that's definitely yeah, I mean that I didn't even think about the merges and stuff so maybe there is a phase zero which is you know it's it's the deployments and the merges and just like own your own stuff in that way right and then.  
Them: Yeah.  
Me: Yeah.  
Them: Totally. I mean, you know, be the be the master of your domain, care for your own path, all that stuff. Right. And I don't, again, I think we probably need to as ridiculous as it may sound, we probably need to lay out that blueprint and say, this is where we're going. And here's the expectations. That you're going to own all these things and you're going to do all these mergers. You're going to. You're going to take it from beginning to end. Right. And that means you don't ask for permissions outside your team. They're all within your team.  
Me: Yeah. Yeah. All right. Yeah so great you sound pretty excited about it.  
Them: I mean, I think this, I think this is going to be such a huge difference maker, you know. And it's going to be, honestly, it's going to be a game changer for if you work on, I don't know how anybody could stay working on the product the way it is today.  
Me: Yeah, I'm not sure.  
Them: I just. I don't know, I feel bad for people that have done it so long. But that's why I think this, this is huge opportunity to make an impact. And it could be, I mean, think about deploying changes in areas every day that you couldn't do for a month before. Now.  
Me: And even if we at the initial stage we're talking about minimonalists like right like oh you have to deploy all of my exchange that is way better than deploying the whole like whole system.  
Them: No kidding. Right, right. So yeah, so that's why I think it's pretty interesting, exciting. I mean, I think there's some challenges in getting everybody on the same page and, and how to move it forward. But I think everybody will be excited about it. I, I don't know how it couldn't be honestly.  
Me: Yeah. Yeah. All right. Okay so then so what maybe you want to do on it for a bit like what the tactics are here but I think it's pretty clear the first we just got to get the team standards knocked out and like get the JR projects created that I'm excited about just that by itself right like fresh JRS and then each team now needs to move. In the the work that's still relevant which also serves as a pruning like okay this stuff is three years old we're not going to.  
Them: Oh man. But. I mean, I agree. And that's. A, I think that's a strong signal of where we're going and how this is going to be a different world. Right. And there's many who are very reluctant to, to prune the backlog. I, I would even call it hatchet, right? Because there's stuff in there. Like if you haven't looked at it and it's been there for that long, just why bother, just toss it.  
Me: Yeah it's like it's I don't know I don't know remember the last time you moved but when you move like your house or you know this shirt or freaking having worn it in one year am I really going to pack it in a box you know.  
Them: You know. Yeah. Oh yeah. Right. Right. Exactly. No, totally exactly. Yeah. And, and so I think that's, you know, there's a reluctance and, you know, you hear all the reasons, oh, it's still a valid problem. Okay, it might be valid, but if we haven't touched it in three years and no one's complaining about it, who cares? Right? I don't know. But so yeah, so I think that's great. I think we need to send that signal of moving. I am still concerned about. Changing the JIRA project IDs and boards and all of that. I just don't know who else is keying in on those values. We're going to have to, we're going to have to find that out before we kick that.  
Me: Change anything right so we're going to create new ones.  
Them: Well, but as soon as you create a new one, you created a new project or space ID that's going to break someone else's set of collecting data from a different space ID.  
Me: Yeah. Yeah well it's not okay so maybe we're saying the same thing but it's not going to break anything it's just going to not be included in in things.  
Them: What does that mean in different like if, if I'm, I don't know, somebody in program management, I don't even know who that is, but, and they're, they're collecting data out of JIRA. It's going to break what they're collecting.  
Me: Well okay so yeah it's okay so yeah we are saying the same thing it's just semantics but no nobody's integration or query or report is going to like not work anymore it's just going to all of a sudden it's going to be incomplete which you could say that it's broken.  
Them: Fair. Enough. Fair enough.  
Me: So but but when you say break that that to me sounds like you get it you know there's a 500 error on this you know what I mean?  
Them: Okay. Okay. Yeah, yeah, yeah. Sure. It'll come back with the 200. It's just you won't have anything to show.  
Me: Yeah sure less and less basically and then people are where's all this stuff well it's in the new project so yeah.  
Them: Right. Exactly. So I think there's going to be surprises there that we don't know who's oh, I didn't even know you were taking data from, you know, that kind of thing. Right.  
Me: But you know what though there's a silver lining with that too because we have way too many sort of like homegrown things that are integrated with the like.  
Them: Oh. Yeah.  
Me: So I would actually I would be I actually want to know all the things that that no longer work correctly. Because half of them the answer is probably well you know what you should just go straight to Jira and get that anyway so yeah.  
Them: Yeah. I'm sure you're right. I'm sure there's countless numbers of those that somebody spun up for some reason.  
Me: Yeah.  
Them: And maybe it's still maintained. Who knows? But.  
Me: Okay. Maybe we can maybe I can schedule do you want me to schedule the next kind of working session and then we'll sort of formally communicate the handoff there?  
Them: Sure. That sounds good.  
Me: Or do you want to just or do you want to find the time?  
Them: Yeah. Anytime, I mean, anytime's fine. Let's go. I don't care.  
Me: With that group that's been working on the team standards? Because I think that that's probably the immediate next step is we close that out right.  
Them: Yeah, I think, I mean, however you want to do is fine with me. If you want me to do it, I can do it. If you want to do it, that's cool. We can do it.  
Me: Okay why don't you do it then I think we we've already at least verbally communicated that you were gonna take point on this so just yeah if you can schedule something that would be great.  
Them: Okay. Yeah, I'll do that. I'll do that. Yeah. And so. Do you have a timeline in your mind of. Of like, hey, we're going to get through this team standard by this. We're going to get down to, you know, domain definitions and, you know, blah, blah, blah.  
Me: Yeah good question. Maybe it's optimistic but I. Don't know do you think we can. At least the jira part that we that can be finished so we can put in tickets to create those spaces before the end of next week.  
Them: Well. I was thinking we can definitely create the spaces, no problem.  
Me: Well I think because there's a few things that maybe is left on that list like what's the workflow statuses like.  
Them: Yeah, that's what I was thinking about.  
Me: Yeah there's a couple of those things.  
Them: Yeah, I really wish that we could get that open so we can just define our own workflows and we wouldn't have. To, wouldn't have to be part of create a space for us. Right. Honestly, we should be able to create our own spaces, but whatever.  
Me: Maybe that's the answer maybe it's just we just need to have it good enough. Which in that case I think we should definitely be able to if we had that if we had another working session tomorrow or monday or something you know actually when we're all together that might be cool Monday.  
Them: That's a good idea.  
Me: Yeah and then and then.  
Them: Yeah.  
Me: Then we those tickets can be open and then I mean I would love to end next week with just the blank Jira space is created and then and then we go from there that would be fantastic.  
Them: I think that's, that's good. I honestly, one of the things that I think is one of the biggest unlockers that I really would hope we'd get to. Let's say by the same time frame by end of next week. If we can get to. A workflow that we're aligned to that is simplified and anything will be simpler than what we've got. Right. But, but if we can get to that simplified workflow. With the understanding that each team can then take that and customize on top. That is, that's huge.  
Me: Yeah. Yeah. So I think so I think kind of goals so if we could have if we could have that by end of next week and then I don't know. What how much what we need to set up for basically so to at least get started on defining everyone's domain so whatever that means like whether that's a confluence page or something where where that happens so I think just kind of the tee it up for for teams.  
Them: Yeah.  
Me: And we have that space actually you know what we have that the thing that Matt created right or did you see that page.  
Them: I haven't, I haven't had a chance to look at it yet.  
Me: Okay I mean that's actually a pretty solid starting point so I think that's probably also not unrealistic to take that either as is or massage it a bit and say like hey everyone here's the starting point we need to get this to the best of your abilities like let's catalog everything that you think you own.  
Them: Okay. Yeah, I haven't looked at it because what I was asking these guys to do was to create a lucid chart page for their domain.  
Me: Yeah yeah that's even better probably.  
Them: And then we can, we can, what I was asking, let's start creating the services you think you're going to have, you know, whether it's one, two, 10, whatever it is. And then, you know, who's connect who you're connecting to, what data you're exchanging and what data you own and really think of it as your domain from there. But obviously we haven't started. So whatever matt has is a good start.  
Me: Yeah. Yeah. So let's shoot for that the jira project and and beta version of of the team domains. That would be amazing.  
Them: I mean, I don't think we're going to get beta version of team domain by next week.  
Me: I mean Matt well it depends how you define beta versions but okay if you take a look at that page I think there's it's a very solid starting point.  
Them: Okay.  
Me: Yeah.  
Them: Okay. Yeah, I haven't. Sorry. So maybe, maybe we can then. Yeah, you're right. Because I was just thinking of the, of the, you know, if we were doing a domain driven design in lucid and, and really thinking this through about how it would be separated, what we're going to provide, that's, that's not going to happen next week.  
Me: I see okay so maybe you're you're you your idea there is the goal in your head is more ambitious than mine I was simply thinking. Out of all the things we have right now like what where does it belong in the future.  
Them: Like a functional, at a functional level.  
Me: Yeah exactly yeah and of course there's this there's an architecture and design thing.  
Them: Yeah, yeah, yeah. I'm with you now. I see, I see, I see.  
Me: Basically. Kind of like okay the current all repo what belongs to which team that that's yeah.  
Them: Yeah. I see what you're saying. Okay. Okay. Yeah, yeah, that's, that's much more. Possible. Okay. Yeah. Okay. Okay, cool. And tell me again, who was on the, who was on that? I guess I could find it. Never mind. I'll find it. Who was on the team standards calls. It changed a couple of times, right?  
Me: You want to use the last one because we we expanded it a bit so it's the one that was on. Did we do it? Wait was it last week already.  
Them: I think so.  
Me: Yeah.  
Them: I don't know. Where. It was.  
Me: It was on Wednesday I think Wednesday at. Four yeah that's the one Wednesday.  
Them: You guys get.  
Me: 17 set up yeah that's the one.  
Them: Okay. So that same group then. Okay, well.  
Me: And you may he was very it was very new at that point but you may want to include a non also.  
Them: Okay. Yeah.  
Me: Yeah.  
Them: I should, I should, you're right. Good, good call out. One question I was going to ask. So obviously we're doing this and it's going to impact Ramesh. Do you want to try to schedule these so he can be included at the time or what do you want to do with that?  
Me: I don't I don't think it's necessary for this for the to just finish that team standard just document if if.  
Them: Okay.  
Me: Try I think it's fairly uncontroversial to be honest. So it's not necessary we can inform him. I think.  
Them: I mean, he could always give feedback that we can answer or change based on. So that's fine.  
Me: Yeah. Yeah.  
Them: Okay. But I will add on and then. Was there anybody else there that was everybody, I guess. Okay. Well. Yeah, if we can do it while we're all together, that's even better actually.  
Me: Yeah.  
Them: I don't, I don't know the setup there. I assume there's whiteboard spaces that we.  
Me: Had. Booked conference rooms.  
Them: Okay, cool.  
Me: In conference room apparently so there's multiple other teams that's getting together there also like in his group. And I was trying to get together like a disaster recovery steer co something like that.  
Them: Okay.  
Me: And but Daniel was first so he had already grabbed himself.  
Them: Sweet. Well, the reason I was asking because like I was talking with Christine yesterday and she was actually in the office. And she said, oh, it's crowded here. And I was like, really? And she's like, well. Crowded. I mean, there's like seven people. I was like, that doesn't sound like.  
Me: They sent out there is a link that shows you.  
Them: A layout or something of it.  
Me: Yeah well there's a confluence page somewhere.  
Them: Yeah.  
Me: And then it has a link to a map. I think.  
Them: Okay. Yeah. As long as Daniel got in first, that's good.  
Me: Yeah so when are you are you traveling on Monday or Sunday or Tuesday or what is it.  
Them: So I'm going to drive up on Saturday.  
Me: Oh. Okay.  
Them: And then I'll, I'll come down in time to be there Monday morning. But I'll be staying in Frisco after that.  
Me: So you'll. Be. Okay wait so you're where you're staying in Frisco. Are staying in a hotel in Denver I assume for yeah okay.  
Them: So. Yeah, yeah, yeah, yeah. Yeah. I don't, I didn't actually. I didn't book anywhere yet, so I've still got to do that.  
Me: So you may want to check with him because he has booked his travel already and you know I don't know. Now I'm thinking okay so we have that. Team event. To stay I don't know maybe we should try to do dinner just the five of us since it's like the first time ever we're all well actually Ramesh is not there but yeah you meet Daniel and Aaron that might be that might be cool.  
Them: Yeah, that sounds good.  
Me: On maybe Monday all right let me let me see if I can pull it off.  
Them: Okay, yeah, that works.  
Me: Yeah okay.  
Them: Sounds good. Okay, cool. So I'll schedule something, I guess everybody will be there. So, but I'll try to block their calendars. For Monday or Tuesday. I don't know which will work.  
Me: Yeah sounds good.  
Them: But. Okay. That sounds good. Anything else here? Oh, did we. I guess we cover that. Yeah, never mind. That works. Okay, cool. Anything else?  
Me: I think that's it.  
Them: All right, sounds good.  
Me: Okay awesome thanks Mike exciting bite.  
Them: All right. Thanks. Talk to you later. 