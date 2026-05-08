---
date: 2026-05-07
type: meeting-note
attendees: [Curtis]
duration: 30min
time: 10:00-10:30 AM
status: pending-transcript
---

# Marten / Curtis 1:1

**Date:** Thursday, May 7, 2026  
**Time:** 10:00-10:30 AM  
**Duration:** 30 minutes  
**Attendees:** Curtis, [[Marten Engblom]]

---

## Transcript

Meeting Title: Exchange resiliency roadmap and productivity update with CJ
Date: May 7
Meeting participants: Mårten Engblom

Transcript:
 
Them: Hey, good morning.  
Me: Hey, how are you?  
Them: Oh, you're muted. I can't hear you.  
Me: Doing? Yeah, how's the jet lag?  
Them: Hasn't been too bad yet. So. It's all right. I'm just trying to get my head back on plate of like what's important.  
Me: What time did you actually get home? Like walk through the door?  
Them: It wasn't too bad. It was about 7 p.m. Last night.  
Me: Okay. That's like late enough that it's not a struggle to like just stay awake, right? Like, I don't know. Because then by the time you're settled and maybe eat some, like it's fine to go to bed at nine on a day like that, right? But I feel like when you arrive home. At midday that afternoon is just terrible, you know, you just want to go to bed at three or four, which obviously doesn't work. So yeah.  
Them: Yeah. The particular route I took, I really, really like the route.  
Me: Okay.  
Them: And it was like, I don't know, every piece of it just seemed to work really good. And like the layovers were manageable is like two to three hours. And then, yeah, I'm just like, man, that was pretty dang nice.  
Me: Yeah. One too. And actually I wouldn't mind doing a stay over in Hong Kong and just like, because I've never been there and just check out because I think it's a cool town probably.  
Them: Yeah, it was, I mean, all I saw was from the airplane landing it, but I was like, man, that looks. Cool. They had like misty clouds. And green hills and really, really tall apartment buildings.  
Me: Yeah, no, I've heard it's a little bit I mean in a very broad brushing but it has kind of a New York thing lots of good restaurants and stuff like that except that it's a clean city it's not and you know what I mean it's not. Like yeah.  
Them: Oh. Yeah. Oh, that, yeah, that would be nice.  
Me: Yeah.  
Them: Yeah. The India is just a very dirty city, just less fun.  
Me: And same thing with New York I mean I used to live there obviously so that's a lot it's a lot of you know cool things like that but like but man it's noisy. It's dirty. It's yeah just you know it's not like yeah it has a lot of downsides too. So yeah. Okay. So oh yeah so just really quick the kick drum meeting was fairly. Tame I would say yeah.  
Them: Oh, okay. What was it like?  
Me: I mean. It was let's see so I mean they just asked some. Questions fairly high level I they. Actually I can forward you I mean I'm not saying that as like it was useless that's not what that's not it at all but it wasn't like it wasn't intense or stressful or you know it was just kind of a conversation so. Very little of it was spent on any kind of exchange things it really was the main area where I am Daniel were engaged where around the SSO that solution and they have had sort of already I mean they were leading the witness right they. Basically the same thing I think I asked on day one like why are we why do we have our own IDP and I mean they're like well have you thought about auth zero we're like well as a matter of fact we have talked about.  
Them: Okay.  
Me: Yeah. And then and then that led to actually so the most probably most important takeaway from our us to them me and Daniel to them was that because that led into are there any other areas where you know we should be thinking about build versus buy. And it was more of a round robin so I kind of. Talked a little bit about our homegrown event bus and they that was not they I don't know I guess they're not consuming the documentation we're giving them because that seemed like they hadn't heard about it like and one of the one of the guys J I think his name was seem pretty technical his his eyes were big as saucers when we said that like what do you have a homegrown event bus on mongodb like oh my god so I think I guess that's a good thing that we brought it to their attention that it's on our radar already and you know it's not something that's can that's sustainable in the long run before they come in and think that you know oh these guys think this is a good solution so I think yeah yeah.  
Them: Yeah. Okay. Okay.  
Me: But there so forward you actually so it seems like they have a tool that that's automating meeting notes and then they send it out which was way better than. Actually so we don't have it enabled but the copilot built-in copilot meeting summary thing in teams I don't know why it's not enabled for us but that I've had good experiences with that in the past but this was just as good if not better and I it's it's called.  
Them: Yeah.  
Me: What was it called afforded to you but. The sad thing is. It's like blocked you know how like security they've like blocked access to a bunch of tools so I can't even. It has the transcript and every every sort of point takeaway is a hyperlink that I guess takes you to the tool which gives you a broader context and maybe the full transcript of where they gather that context but that website is blocked so the use is usefulness is limited I guess. But yeah I don't know it seems we should look in if that's maybe something in their their portfolio or whatever I would be very interested in kind of using that because it seemed really good.  
Them: Okay.  
Me: I. Don't know why I can't oh phantom is what it's called phantom. Here I'll send it to you right now. And it actually is a very good summary so you know just you can just skim through that and you'll see what we talked about basically.  
Them: Oh, that's great. Yeah, that's awesome.  
Me: Yeah but try to click on the link and you'll be slapped on the wrist.  
Them: You can't click on this link. Okay. Okay, cool.  
Me: Okay so let so I don't working on some slides but they're all a big mess so I'm just gonna show you this outline that I have that. And just touching a couple of things that I kind of want your feedback on. So okay so. Let's see okay so the three things right that CD okay so actually I know it was on the phone and it was noisy are you clear on what what I'm meeting with him about today was that clear to you.  
Them: I think so. But I mean, I remember thinking it was clear, just go over it because I can't remember.  
Me: Yeah so essentially it's this sort of storyline or the type sort of the. The chain of events go something like this I had lunch with cj. I brought up sort of the whole thing with competing priorities and and so on which led to him he's he you were part of that email he forwarded to us that that where he had sort of pushed back on Christy and Steve and saying like hey we got to stop doing this it's you know it's it's creating a lot of churn I just had a long meeting with Morton and this is you know I think we need to solve this right so then we so then he said he wants me I don't know I'm guessing that you probably should be there too to have a meeting with cj and steve I think that's that's it. To give an update on a couple of things so then the three things are at the top here so one is commentary or like state of the union on. Productivity improvements so far like how are things going what's what's going well what are the challenges and so on.  
Them: Yeah, yeah.  
Me: And then the second thing is. An update on the exchange resiliency work so. Which actually is broken down into really five things if you go back to there's a presentation that you and him put together at the end of last year that has like the 2026 right.  
Them: Yeah. Yeah.  
Me: And four of those things are just really easy to address because it's like database migration it's it's the Dr. The disaster recovery stuff it's vulnerabilities and end of life Technologies and it's the ICS solution okay the fifth one which is by far the murkiest is decoupling the monolith and that's where there's a lot of unclair but not very not very very good understanding of what it means and you know when are we done and it's just this big blob to them basically.  
Them: Yeah.  
Me: Okay and then the third thing is with all that said what's our kind of projection for how the capacity pie chart is going to change when when are we going to start when will we be able to shift some more capacity to. Roadmap commercial work whatever. So does that make this?  
Them: Yep, yep, yep. Now I'm remembering that call. This is when I was in Seattle. Yeah, I gotcha.  
Me: Yeah. Yeah. Things here basically the asks right. Okay so a couple of things. The so actually let me just walk through really quick my kind of plan of attack and then I have some specific things that I would I want your thoughts on so so the so the first thing is okay productivity assessment it's basically going to be there's some positive signs in the data if you look at. Things like storage completed cycle time there's some things if you look the past three months they there are improvements I mean both you and I know that.  
Them: Yep.  
Me: Who knows if this is actual trends that are going to hold or if it's just kind of a bouncy curve but for now it looks good at least right.  
Them: Yep.  
Me: I think I can maybe give a preview of the exchange health score that I and Daniel have been working on because that's also kind of shows the economic trend. Okay so there's that and then some challenges the number one is like the monolith and we're going to get back to that it's it's a challenge in many many ways. I might. I don't know how much of a the kimono we should open here but like. There's some culture things you know fear releasing we sort of had tendency to do large product launches. That's one thing I could kind of mention I think they already know we have a visibility slash reporting problem I think you know if you think about our noisy roadmaps and stuff like that it's not necessarily an impediment to the productivity but it's an impediment to the perception of the productivity.  
Them: Yep. Yep.  
Me: So. And then I don't know if I should bring up the competing priorities again reporting asks I think we do a lot of we do a lot of I mentioned this to you too right like this we we do a lot of reporting that feels like. Feels like very top down performance management in an environment with low trust as opposed to an actual interest in in the progress that that's kind of how I would summarize it. So I don't know I might delete that and because it's probably going to open a can of worms. But I don't know these are my thoughts at least.  
Them: Oh, that's interesting. Yeah. Because, yeah. Because I kind of have the same. Perception, right? It's like everybody gets your OKRs, get those in, get those in. And then it's like never another discussion about it. Right. Or it's like, get the report so I can look good in front of my boss. It's more like that.  
Me: Yeah. Exactly and so it's so exactly so it just feels like.  
Them: Right?  
Me: A bunch of unnecessary work or yeah I don't know. Like yeah we've been joking like if you would anyone know this if we if I wrote lorem ipsum in in the sort of update on the in in the OKR I would love to do it as an experiment sometime and see what happens you know. So anyways okay so that's gonna be summary and then so that where that leaves so in summary we're making incremental we're making incremental productivity improvements and by the way we're also tracking well against all the other four resiliency priorities so again Atlas migration Dr test vulnerabilities in the UL technology so kind of a lot of them are going to be addressed by red mythos.  
Them: Yeah.  
Me: And the ICS solution we're building a team to take it over so I think those are all. Yellow at worst you can say that they're green potentially right like I think it's CJ he didn't seem too interested in these he think he knows. They're on track ish so I think he just wants us to walk through it okay.  
Them: Yeah. Yeah, I think so.  
Me: Okay all right then back to sort of the main the main issue which is the monolith which is both technical and organizational problem so I talked to you about that right it's that vicious cycle of huge releases and blast radius and so on.  
Them: Yep, yep.  
Me: Kind of probably will take just a few minutes. To where to that and where it gets kind of interesting is that you know there's some there's a cost slide that I had in my all hands that talks about what the problems with this is and then it's not only a technical thing right it's also an organization we've had a monolithic organization which you know they go hand in hand I think they feed each other it's the conveys law thing right.  
Them: Yep, yep.  
Me: Okay so now. So then the vish the let's see this is a little bit jumbled. But because I want to get to the questions I have for you. So let's skip that and just say like let's address this like end of resiliency when are we out of the woods and I talked to you about this yesterday I was I was going to like two things right we needed teams to be autonomous and run on their own like and I'll define more precisely what that means. And then I really think we need a first pass at our databases and not just migrating them to atlas I think we need to make some changes and this has a lot to do with. Scalability and resiliency and things like that. Right before we've done those two things I don't want to shift any capacity away from. Technical work to roadmap work when these two things are done then we can start having conversations basically we still will have a long backlog of technical things that we want to do. But they are but they're more they could at that point it becomes a more of a conversation and they're not. They're not. Must haves in the same in the same. Way right.  
Them: Yep. Yep.  
Me: So that's kind of the through line. And I'll let you comment on that but just to put so the couple of things I wanted your input on is what else should I should we talk about in terms of like positive signs and how things are going or challenges or any sort of feedback there. And then the second thing is is there anything else that you think we should put in this must have bucket besides the two things that I highlighted. And then I guess the third ask is what do you think we should say in terms of how the pie chart. Will be shifting and when that's kind of that because that will that's definitely a shot from the hip if you ask me but I also know that if we say it's not going to change till 2029 that's not you know what I mean that's not acceptable. So.  
Them: Not exactly helpful. Yeah. Okay. Can you scroll back up to the top? Because I think.  
Me: Yeah.  
Them: You're, you're touching on the right. Pieces here. The, the other positive signs that I would consider saying is maybe addressed this, but just how you said we went from one director and three managers to essentially three directors and 14 managers. And, and that's just that division of ownership.  
Me: Yeah.  
Them: And then there's a piece in here that. I'm curious if you think it's worth commenting on that. The FTEs just have more ownership than contractors. Contractors are incentivized differently. To, you know. And so I think. I think that's another, I think we'll see more than we expect from that. Or more than the company expects. I think we'll see. Okay, then your next question was, did we, let's see.  
Me: Any challenges any other. Because. He I mean because he said this explicitly like hey I don't want this to be he didn't say dog and pony show but he's like I don't want just like all the positives and wins I want sort of a true. Let's have it let's have an honest conversation what's what's going to be a challenge what's difficult and things like that. So.  
Them: Product? Do you feel like.  
Me: Yeah.  
Them: Because I, I kind of get the sense that it's all project management right now.  
Me: So the way actually I was gonna bring that up is I was gonna put it on the list what it but it what it means for a team to be autonomous. So basically like. Em product owner agile process like that thing and that and that's where that kind of. Light feedback I think. Will. Come up. Because we don't have that now. And I think we're trending in the right direction but I don't know if even with the latest changes. You we can claim that we're gonna get to where we think we should be.  
Them: I agree. And I, okay, so how is like you worked with Laura a little bit now and I know she's done agile in the past and has some opinions about it. How do you feel like. Either you two are aligned or like, is it, is it heading in the right direction? As she's getting everything organized or is there more.  
Me: So CJ said the same thing and he actually shared that he was felt pretty underwhelmed by. Her in those meetings they had with veritas or with there was like. These veritas product meetings that happened I think a week or two ago I'm not sure were you part of those or no. Yeah and he's like yeah he wasn't super impressed he said she kept referring to Josh skiba and just kept I don't know didn't seem like she he said it didn't seem like she had.  
Them: Of those?  
Me: Onboarded very sort of quickly that you know that she hadn't I don't know I wasn't I'm not sure exactly he didn't seem to impress my feedback was. I I think she I mean so far I think that she seems. Like she's no she knows what she's doing. However they have for all the my time here product has been operating in a mode of essentially like you're saying project management they're basically kind of prioritizing a plethora of small to medium size requests from all of the company as opposed to I haven't I haven't seen any sort of product vision type that type of product leadership right but that's but that's. I think that's because they don't have that mandate or that that agency but so basically I haven't seen her work in that mode so that that the jury is still out for me in that case.  
Them: Yeah, and maybe that's just the good way to say it is like. Cause that's the gap that I keep seeing. We don't have the product vision. We just don't know. It's not, we're not hearing it from anywhere.  
Me: Yeah yeah. Yeah.  
Them: And so the role is just playing a project manager role to triage small and medium issues.  
Me: And and and I forget I think that's around the time where CJ shared that basically Steve had said we don't have that anywhere in in his organization he said like. What else is engineering supposed to work on we don't have a vision we don't have a product vision for them to work on so they might as well just do all technical work I mean that's basically what he said.  
Them: Yeah, yeah, this, okay. Yeah. Because there's a part of me that's like, well, if you want a vision, I'll go get you a vision. Like I can do that.  
Me: Yeah. Yeah. So so yeah so I think so I think in in many in in many ways in most ways I think I think we're aligned I think sometimes I've got I've gotten harder push back on things than I would like. When it comes to. Like our expectations on product like what they're supposed to do so things like. They should be present in every agile ceremony they should own the backlog they should make all the prioritization decisions they should write user stories you know so but all of this pushback I think has a lot to do with their the they're not staffed for it or haven't been at least I understand that like all of these things that I'm enumerating has been tough when it's LoRa and two three or four direct reports and we have 12 engineering teams.  
Them: Yeah.  
Me: But you know things are changing a little bit it's not going to be a one to one but I think she's going to have eight or something product people. Now with that said I don't still don't see how she's going to meet our expectations if they keep this like product. Manager product owner delineation because you then you still only have three or four people that would sort of engage. Directly with the engineering teams if you have people like Rada sort of wanting to sit a layer above. And and basically. You know doesn't want to touch Jira in that sense you know at least not. With the fidelity that we want then that's going to be a problem.  
Them: Yeah. Because part of me feels like. I guess I just feel like we should bring that up because, you know, the culture here, like, steve's not going to know that that's how products should be run.  
Me: Yeah.  
Them: Uh, he doesn't have the experience with that. And so it, but if we say, look. It's normally product's job to. Make sure that we understand the needs of the product. And like what the market needs. And then, but they have to interact regularly with the engineering team. So that the engineering team has that shared understanding. If they, if they don't, or if they like meet them once a month or something like it's, it's just, there's too much opportunity for drift.  
Me: Yeah.  
Them: Yeah. Because I even think about this, like, let's say we go a year down the road and the exchange is humming along and they've got no other priorities. Well, this product owner should be able to take a whole different lane. Right? Just, what's the next customer problem we're going to work on and then take that team and, you know, learn a new area. It's not like we just leave them or we cut staff and stuff. That's not how we want to play the game.  
Me: Yeah.  
Them: Okay.  
Me: Yeah so let me. Again part of my I guess I should bring I should bring that up with CJ at least and then he I can get his feedback on. How that's going to land with with Steve.  
Them: Yeah. Yeah. It's, it's just interesting because like. I'm in the place now where when we, we just need to say what the best practices are more often. Because if they don't know, they're not going to know to shift. They're not going to know anything about it. And it takes time for them to, like, assimilate that. And make, make different decisions.  
Me: Yeah. Yeah. All right. So if you think of any more sort of. Either positive things or challenges. Just slack them to me.  
Them: Yeah, you and you've got the one where. Like, let's see, the, the ones that are on my mind are. Data collection in a manual way. Is super annoying. And then you've got this kind of report and status readout from all kinds of different people with their special and secret initiatives. Right. And like, I feel like if those two things went away. Then you're really just focusing on building. And then the product part is building what?  
Me: So. When you said the data collection that's specifically for those for the reporting and things like that's what you meant.  
Them: Yeah, but it's, I guess like over the last little bit when we did the investor due diligence and we collected all that data and now, you know, we're working with veritas or we're prepping for distinctive and kick drum and, you know, feels like there's always some new request for some data that we don't have automated always. And that's the one that I'd like to. Not have. Yeah, there's, there's always that data request. Or it's even. Yeah, and it just feels like it's coming from everywhere.  
Me: Yeah.  
Them: And it's somewhat related to the visibility reporting problem. But, you know. Just like there should be a principle around if it's requested once, you just automate how you get it. So you never have to request it again.  
Me: That's where it belongs.  
Them: And then I guess. That you mentioned the culture, the fear of releasing large product launches. Is there anything that you. That just like. I feel like the newer people you bring in just have a lot better understanding of what's going on in the market. Like what, what good looks like.  
Me: Yeah.  
Them: And so, yeah, go ahead.  
Me: So so these so. These are some of these were actively solving or all have almost solved already right so so that culture is one that I would say is.  
Them: Yeah.  
Me: We're definitely on our way to fixing it one one aspect is what you're saying the the new new people were bringing in that's just knows what what good looks like but I think also with just the change in in asks in marching orders if you will we're seeing I'm seeing changes from the people that were here before too so an extent I mean yeah an example would be like prashant's team are basically asking do we have do we really have to wait around for like pbob and his team to like write new new automated tests? We just want to move forward so that kind of thing right and and then another I don't think I've talked to you about this yet but another recent example is. So you know I think I told you rami was he he he he had put a meeting on the calendar for me and Ramesh on Tuesday or whatever it was. And that the basically the objective was he wanted some sort of. He wanted a roadmap or commitments like quarterly commitment for when we can deliver this managed services portal okay so that request had come in already when I was in India so I'd talk to ramesh about how to approach it so he kind of ate that up and and basically came into the meeting him and and Sunil and and they were like we're not gonna give that to you but what we instead are gonna give you is we're gonna have something deployed to production in a couple of weeks or a couple of sprints and then we're just gonna keep giving you incremental updates as we go along. And we'll keep adjusting the projection for when we're done we actually between you and me you know we think we can be done sooner than what you're asking probably towards the end of the year as opposed to q1 but we're not gonna. Write that in blood anywhere we're gonna sort of like we're gonna just take it as we go and but we're gonna deliver things that that's useful for you along the way. And you could tell that it's like at first it was like at first they just heard we're not gonna give when we're not we're not gonna give a get a commitment from them but then it's like within minutes it started sinking in like okay we're gonna get some we're gonna actually get something useful much quicker. So and that came from a team that's already here you know what I mean? So.  
Them: Yeah. Interesting. That's cool.  
Me: Yeah.  
Them: Good. Good, good. I like that. Good.  
Me: So yeah anyway so that culture is definitely. And it's not it's not changing overnight but we're seeing signs right another another fairly recent example is that that core UI upgrade for my exchange I mean the original plan was literally to plan a product launch with all five modules like some I think it was like July or something.  
Them: Yeah.  
Me: And they were sitting there with like two or three modules that are finished and like why are we not releasing these and this was and and what was his name the product guy that was. He's. Not yeah exactly he was well be very jarring to the customer if the you know the UI is changed in one module and not the other and we have to like rewrite the training manuals and like just okay then put in a toggle in the in the UI so the code and then let the customers know if you're adventurous you can flip over to the new UI and check it out that's what like every modern company does.  
Them: Brian. Granolan:  
Me: And so so then that actually turned into the approach. Which is yeah it's still not like incremental delivery sprint by sprint but it's a lot better than planning the grand product launch you know three quarters from now so yeah we're definitely I mean we're seeing signs. But again none of this is gonna all of this is gonna be incremental until these teams that we're talking about can just move on their own. Everything all of this stuff is kind of held back by the monolith which is kind of the through line in this right so.  
Them: Yeah.  
Me: Yeah.  
Them: Okay, good, good, good man. I love hearing stories like that.  
Me: Yeah.  
Them: Okay. Yeah.  
Me: So there's so there's that and then so any what is was there anything else that you think we should learn in this must have bucket do you think I'm. Too conservative there.  
Them: The thing that's on my mind is like on demand deployment. But I don't, I mean, that can kind of be encapsulated under autonomous teams.  
Me: Yeah. And that's kind of the whole crux there right like that unlocks. So much right because if we anything we want to do before that let's say let's say we said we need to be we need to have what did you call it daily deployments automated what did you say.  
Them: On demand, on demand deployments.  
Me: Just think about how massive of a lift that would be in today's. With today's monolith. Like just like if if we said like hey guys you can drop everything else you just need to get to on demand deployment it would still be a massive project in today's world but in after we've shifted to autonomous teams with.  
Them: Yeah.  
Me: That's not operating on a on a monolith that is a much much much more reasonable ask it's like hey all 12 teams we want you to get to on demand deployments and they're all going to do it at their own pace and at their own way some some team might say you know what like we're so buttoned up with our pipelines we can do that tomorrow some other team might say we're way too busy with like pick your project that's going to happen in Q3 and you know there's some issues with you know the pipeline deploying to you know this whatever AWS product that we're using and you know there's some problems to work through but they're not going to hold up each other because of that so that's kind of the whole and the same thing. Can be said for almost any ask anything we want to do with this this platform or this these teams so that's I mean it's so important.  
Them: Yeah. And I kind of like what you're doing here because you're keeping it simple. It's just autonomous teams. And then data stored in the correct products. You get that. Then you can get this next level of refinement. Those are really the fundamental pieces.  
Me: Yeah.  
Them: Though.  
Me: Yeah.  
Them: Okay.  
Me: And that's that's what I kind of wanted to double check I just want to make sure I'm not forgetting something so we have to sort of come back and shift the goal post later and say like oh you know what I said these two things but by the way we need a third thing before we're done.  
Them: I know, I know. And it's like. It might be good to just call out some of those things, you know. The decoupling really fits under this autonomous teams like the database migrations really fits into this data stored in the correct products. It's just a subset of that. But yeah, no, I, I mean. I mean, the trick for me is I can always see how it works.  
Me: Well and the one thing I was going to throw in there as kind of it's a little sneaky but I think feel like it's a little bit of a hedge or a safety valve basically all these things I'm putting in negotiables. Basically there was still holders back. And then but one thing I'm going to say is I'd be shocked if vertos doesn't call this out it's like you got to fix this like youe know the event busting is a good example like there's no way that that it that a technical assessment is not going to is not going to say. This is not a good architecture. So which then kind of gives us I think in the future the leverage if we need it to say like you know what we actually this needs to also be attacked pretty aggressively here.  
Them: Yeah. And this is the one that, okay. Like if we take a, take a step back, we're talking about resiliency and the stability of the platform. And I don't know, I go down the road of. We did it. We did essentially a lift and shift to the cloud. We got a million and one environments out there. We've, we like HR or disaster recovery is difficult because of all that. And you, you kind of make this comment down below about the cloud native infrastructure. It's where it's literally just a setting. And then if I take a step back, like the whole reason we're doing the continuity assurance is because we haven't done the HADR correctly. Right. Or like in reality, the way that we'd want to do this is something like you have. Multiple exchanges around the country. Will you split the traffic between all of them? And maybe even go multiple clouds, right? You don't need a separate product. If we go down, you just need this to be resilient. And so.  
Me: Yeah.  
Them: So to me, it might be worth. Like, that always ends up being a rabbit hole because everybody goes, oh my gosh, the cost is too high. We don't have to have that. But then you're like, well, you're literally got a team spun out that's building a whole different product in a whole different cloud that you don't even know if it's going to have value. Anyway. I just wonder if there's a need to set that seed a little bit or some value to it. Because they don't know, right? Like this whole product is, was built not in engineering and not in true product management firm. It was built as a side thing. And so it might be worth just saying. I'm just kind of wrestling. Maybe that just falls under the negotiables.  
Me: Well so maybe maybe the thing here is that it's not negotiables that some other maybe that's too soft maybe it's some maybe it's more along the lines.  
Them: And.  
Me: Of these are still things we have to do. But the pace and the order and the priority. You know we can be. It becomes more of a stack ranking with. Commercial objectives or whatever else like we these are not negotiables in the sense that we can do we can choose whether or not to do them it's negotiable in terms of. When and how aggressively.  
Them: Yeah, yeah. Yeah, I think that's it. Because if you said these would still be required, but once we have the other two, we're, we're on the right track.  
Me: Yeah.  
Them: Yeah. Because I. I just, I just keep thinking until we kind of have that auto failover auto disaster recovery fell over. Or that second region or that two or three regions. There's always going to be kind of this. This concern. And, you know, then even from the cost perspective, it's like, can we just get down to two or three? But that's why I don't, it's not like the fire is burning, the house is burning. They're just like really important things to solve.  
Me: Yeah. Yeah.  
Them: So. Yeah. Cool. Yeah, I think this is pretty good. That's pretty good.  
Me: Do you. I don't know if. What. So this this conversation with CJ is at noon my time I don't know if you want to if you want to join it or if that's not his MO he doesn't like people who crashes meetings. Or.  
Them: Um, I would say just go ahead, they'll be fine. Yeah.  
Me: All right. Sounds good.  
Them: Yeah.  
Me: Yeah that's it.  
Them: All right. All right. Cool.  
Me: Now I'm just. Gonna put some bullet points in in slides together I had I had claw generator slide deck but it always it's like overdoes it you always have to pull it back it becomes this like enterprise thing that's like.  
Them: Just give me some talking points on a picture, man. That's it.  
Me: Yeah pretty much.  
Them: Okay.  
Me: Yeah.  
Them: Okay. Cool.  
Me: Thanks.  
Them: Yeah, let me ask you just a real quick question. With Aaron rolling out like some AI stuff. My understanding is he's putting these skills into like plugin and marketplace and people can start downloading them. Are you always seeing that adoption or is there some. Work that Aaron is doing first.  
Me: I. Don't know about the adoption because it was literally shared out I mean it was two days ago or something like yeah it wasn't that long ago so I don't know what the adoption is.  
Them: Or. Okay? Okay.  
Me: But there's definitely engagement in the slack channel immediately. So yeah.  
Them: Okay.  
Me: Yeah.  
Them: Okay.  
Me: Just want to like kind of read on how what the appetite is. Or.  
Them: So I've talked with Eric about what we're what he's doing. And we, he kind of uses a certain flow. And then I talked with Tony Middleton earlier, got a better understanding of what he's doing. And then I'm just, I wanted to just understand what, what Erin's doing because I want to pull it all together so that we're not kind of telling them the company that we have multiple different approaches. I just want to find a way to. To pull it all together.  
Me: Yeah yeah I think that Aaron and Eric are sinking fairly regularly so I hope that they're not drifting too far apart.  
Them: Okay. Okay.  
Me: Not sure about what yeah.  
Them: Okay, that's fine. Yeah. I just, I had, didn't know where Aaron's stuff was at. So.  
Me: Okay all right great yeah talk to you later.  
Them: Okay. Cool. Thanks. Thanks, Martin. Okay, bye. 

---

## Executive Summary

Prep discussion for upcoming meeting with CJ and Steve about productivity improvements and exchange resiliency. Kickdrum meeting was productive but tame - consultants asked about build vs buy decisions, were surprised by homegrown event bus on MongoDB. Main focus was on preparing three deliverables for CJ: productivity commentary, exchange resiliency update (5 components), and competing priorities roadmap. CJ has pushed back on Christie and Steve about competing priorities creating churn.

---

## Key Topics Discussed

- **Kickdrum Meeting Debrief:** Mostly focused on SSO/Auth0, consultants were surprised to learn about homegrown event bus on MongoDB - brought it to their attention as unsustainable long-term solution
- **Phantom AI Meeting Notes Tool:** Kickdrum uses this for automated meeting summaries (better than Teams Copilot), but GHX security blocks access to full transcripts
- **CJ Meeting Preparation:** Three main topics:
  1. Productivity improvements update (state of the union, what's working, challenges)
  2. Exchange resiliency work update (5 components from end-of-year presentation)
  3. Competing priorities and roadmap clarity
- **Competing Priorities Issue:** CJ forwarded email pushing back on Christie and Steve about constant priority changes creating churn after long meeting with Marten

---

## Decisions Made

- Need to prepare slides/outline for CJ meeting covering productivity, resiliency, and competing priorities
- Worth investigating Phantom AI tool for meeting notes despite current security blocks

---

## Action Items

### For Marten
- [ ] Prepare presentation for CJ/Steve meeting on productivity improvements [[^task-20260507-001]]
- [ ] Document exchange resiliency status across 5 components [[^task-20260507-002]]
- [ ] Draft competing priorities roadmap clarification [[^task-20260507-003]]
- [ ] Investigate Phantom AI meeting notes tool with IT/security [[^task-20260507-004]]

### For Curtis
- [ ] Review CJ meeting prep materials before meeting

---

## Follow-ups

- CJ meeting with Steve scheduled (topics: productivity, resiliency, competing priorities)
- Follow up on Phantom tool access with security team
- Next Kickdrum session scheduled

---

## Related

**People:** Curtis, [[CJ_Desai|CJ Desai]], Christie, Steve  
**Projects:** [[04-Projects/Thinktiv_Kickdrum_Engagement_May_2026]], Exchange Resiliency  
**Companies:** [[Kickdrum]], [[Thinktiv]]  
**Context:** Pre-meeting coordination for CJ strategic update, competing priorities escalation
