# Road to Autonomy - Github Migrations

**Date:** 2026-05-08
**Time:** 11:00 AM - 12:00 PM
**Location:** Microsoft Teams Meeting

## Attendees
- 

## Context
Github migration planning

## Transcript

**Road to Autonomy - Github Migrations-20260508_110350-Meeting Transcript**

May 8, 2026, 5:03PM

50m 30s

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)**Marten Engblom** started transcription

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   0:09  
If only, Mike, if only.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   0:11  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   0:12  
This.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   0:12  
It's Microsoft, it's Microsoft, like, come on.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   0:14  
At least there's not a double confirmation. Are you sure? OK, so, OK, so the D.R. Disaster Recovery Project, I think of it as two goals, right? One, so one is the contractual obligation to Cardinal specifically, right, which is...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   0:15  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   0:15  
10.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   0:18  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   0:36  
that we have to conduct a...  
DR failover in production, flip and stay before the end of the year.  
And the other one is that I think we need to feel.  
decent, if not good, about our DR situation. So in other words, like if we really got into a situation, do we feel pretty good about our ability to get up and running again in the time frame that's acceptable?  
And they're not necessarily the same thing, right? And they're not necessarily the same time frame. And what do I mean by that? So...  
We just did this DR test in a lower environment earlier this week, and from the early kind of indications, we were pretty close to...  
if not actually meeting the RTO time frames, right? So if, since you guys weren't part of the readout, basically the initial assessment, and help, you gotta help me out here, Daniel, but the initial assessment was 4 hours and 45 minutes.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   1:46  
Yes.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   2:00  
But then that turned out that was not really true. It was actually 7 hours and something because what was it that was forgotten there? There was...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   2:08  
SSO had some challenges they weren't including and then there were some database work previous to the.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   2:14  
Done.  
Okay, so some pre-work and then some work that surfaced like the day after, essentially, right? So that kind of got AP on. However, there were other things that kind of offset that, which is...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   2:16  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   2:17  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   2:17  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   2:20  
Yep, yep.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   2:31  
So once we have migrated the databases to Atlas, the two plus hours that were spent like restoring backups, that more or less goes away from because you know it's already in the cloud and you just like you just point the new the new region to the.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   2:37  
Yes.  
Mm.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   2:49  
To the data, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   2:50  
Who?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   2:52  
Yeah, so that's one thing. What was the other thing that chips away at the time frame, Daniel?  
Or something else.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   3:00  
I don't remember a second thing.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   3:01  
Okay, all right. Philippe, or did they have all this? Yeah, Pete has all this in a kind of a spreadsheet. So, bottom line is, maybe it's slightly optimistic. There's definitely some asterisks or whatever, but if you squint, it seems like we could get to like an under three hour RTO already, basically.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   3:05  
Heat, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   3:21  
However, so that would sort of...  
When we do, that would in theory enable us to do this flip and stay.  
in December kind of already as is, given that we will know it's coming, we're prepping for it or whatever, right? Like, however, does it meet the other goal of us feeling good about where we're at? And I would argue no, because there's just the runbook is just

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   3:50  
Right.  
It's complicated.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   3:54  
Little, little, little with manual steps and this and that and the other, right? OK, OK, so that's why I'm thinking about it as kind of two pieces. OK, so then with that, with that context, basically what we need the work to get to where we book field.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   3:58  
Totally, totally.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   4:14  
Comfortable with this is a lot of automation, right? Like deployment scripts and its infrastructure as code, and it's a bunch of those things, right? Well...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   4:23  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   4:25  
What I just mentioned, that's part of the template, blueprint, pattern, whatever you want to call it, to...  
Decouple the monolith, and because the prescription there is identify your components, carve them off, carve them off from the monolith, move them to GitHub, take ownership of your GitHub actions for deployment, and by the way, make sure all the infra part is like in there as infrastructure as code also, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   4:57  
Suresh.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   4:58  
So then, we continue that line of reasoning, then it's like, well, if we just push the DR piece aside for a moment.  
And just...  
put the pedal to the metal in terms of this decoupling exercise, we would essentially get what we need.  
to feel much, much better, if not feel good about our DR capabilities. We would get it kind of as.  
For free, you're as part of that effort.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   5:32  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   5:33  
Is everyone tracking?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   5:35  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   5:36  
Can we go back for a second? I guess I'm still trying to understand if what we did this week.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   5:38  
Yep.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   5:38  
And.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   5:43  
But.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   5:44  
really could carry traffic and load like in production. I know we flipped everything over and, you know, it took what it took and all the manual steps and the correction. And I know we passed some data, but would it really be production ready? Are we confident of that?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   5:51  
Mhm.  
Mm.  
I don't know. Probably not, right? No.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   6:04  
No.  
No, I mean the environment is very different. There is no infrastructures code. The teams were too small to focus and even create an inventory of the things that they own.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   6:17  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   6:18  
So I think you'd be foolish to think, hey, what we see in stage directly, you know, translates to prod, but I mean, it's not like it's night and day either. There'll be things that are missing.  
But...  
We don't know all those things.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   6:38  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   6:38  
Like I would say, I would say, look, you know, if we did what we just did and we prepared for it and we built all the bamboo jobs for production and we prepped the database, we prepped the buckets, all the things that we know we're going to need, the things that we've been doing in stage the last few times we've done the test.  
You know, we could flip over in three to four hours and have, I don't know, 90% function in production. Like there'd be some things that are missing that we just don't have in stage and no one has a test for it in stage. So you don't see it failing.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   7:12  
Play.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   7:15  
Yeah, that makes sense. I guess I'm just trying to understand if we're fooling ourselves or not, right? One, I mean, we want it to be, right? But is it really that way, that we're at 90 plus percent or not? That's all.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   7:15  
Yeah.  
Yeah, yeah, so all those preparations though, Daniel, that you just talked about, isn't that what, so let's say we, let's say we decided that this is our path, we're doubling down on the play, the runbook that we have created now, over the, you know, that we followed on Monday, that's the game for now.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   7:35  
Maybe 35.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   7:42  
Yeah.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   7:52  
Sure.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   7:54  
Like, that's what we're gonna use. Wouldn't we, wouldn't we do all the things that you just mentioned in? Yeah, okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   8:00  
Exactly.  
Yeah, exactly. So we would basically, the only gap between here and our test in October is we would go create all that stuff for production, get ready, and then do the test in October.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   8:03  
Yeah.  
Yeah, yeah.  
Yeah.  
So...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   8:17  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   8:20  
Yeah, so just for the sake of understanding what kind of our plan B would be, how much work is that, do you think? Is that, did we recently do that for staging to prep for this test, or was it already pre-existing from like months and months and months of effort?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   8:37  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   8:39  
It's been pre-existing. I don't know if I'd call it months and months, but you know, like every time that we do this test, we discover something else that doesn't exist. And so we go build that. And then the next test is easier because of it. So it so somewhere the gap is somewhere between, you know, a sprint.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   8:49  
Mhm.  
Yeah, OK.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   8:52  
Sure.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   8:58  
of work and what they currently had created in that roadmap. Because what we'd want to do now is go back and say, okay, we just did the exercise. Let's go reevaluate that roadmap we created last month. And let's just say the goal is everything that we just did in stage, we need to do in production. So let's go set it all up.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   9:08  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   9:19  
And what does that look like? I don't know that that roadmap that currently exists reflects it. Maybe it's 50% of that roadmap.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   9:24  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   9:25  
When you speak.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   9:27  
Is.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   9:27  
When you say roadmap, Daniel, are you talking about that gaps list? Is that what you're referring to? Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   9:31  
Yeah, the, yeah, all the epics that the teams created for their DR gaps, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   9:35  
Yeah, yeah.  
Yeah, I mean, I know at least a few of them were pretty high level and not a lot of thought went into the details there. It was, we need to do something like this in this area, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   9:43  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   9:50  
O.  
OK.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   10:05  
We just have to get more firm on that.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   10:05  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   10:07  
That was, that was my next question. So, what, what, what is the current current plan?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   10:07  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   10:14  
Is it to create all the IAC and automation for all those missing pieces? Or is it to just kind of repeat what we've done in stage manually-ish for production? Or is it a mix?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   10:29  
I think it's a mix with a lean towards the former, creating some of the IAC and really being able to do it with some automation.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   10:32  
Yeah.  
Yeah, okay, alright.  
Yeah, so then back to the that other.  
Quick question, right? So, okay, so and more more of the context there is that, and I think I'm preaching to the choir here, we have to get to this autonomous state or a good enough autonomous state. It is.  
the price. It's going to, it's such an unlock, it's going to make, I don't think I'm exaggerating when I say it's going to make everything easier. And one sort of analogy I used is...  
Right now, everything is a project because it has to be when you're going to do something, no matter how small, when you're going to do it across 80 Engineers and in the model, it's a project.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   11:29  
Super.  
Yeah, you got all the coordination, right, that you have to do. Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   11:34  
Yeah, yeah, so.  
It it is a it it it's the number one, and I think it's really landing and people are recognizing it. I was obviously Curtis knows CJ is starting, he understands it too, at least at a high level or you know, I don't know if, yeah, but he does.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   11:43  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   12:00  
Me and Daniel just came off our weekly product engineering weekly checkpoint, which...  
with Marlin and Laura. And Laura, I was, were you surprised how on board she was, Daniel? I was a little bit, okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   12:13  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   12:18  
No, no, not at all. I think she's totally on board because we've been talking, building up to this for a while.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   12:22  
Yeah.  
Yeah, she, I mean, she basically said, and I'm not exaggerating, she said.  
I know that's, I want to get there too badly. I will support you in, like, take all the capacity you need, basically. That's more or less what she said, right? And all they want in return is kind of a roadmap, a plan, basically kind of a definition of done. So they have, so it's not.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   12:39  
Yeah, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   12:51  
So it's not like an endless.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   12:53  
To.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   12:55  
project, right? A black hole, which we owe them, right? But I'm really, the more I think about it, I think this is, we need to do this. Everyone is, everyone understands this right now. Like there's a lot of, what's the word I use this?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   13:01  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   13:09  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   13:16  
There's a lot of appetite for it. There's a lot, you know, there's, it's the situation is right, basically. Okay, so that's what we talked about a little bit earlier today. And there's all kinds of ifs and buts and like, you know, you have.  
Banks, doom and gloom, like, you know, it's never gonna work, and we've tried seven times before and whatever, right? I can, and then you have Suresh, you know, he knows all the coupling, it's gonna be, so we have to, you know, do we have to plan it out and whatever. Well, so I'm off.  
Daniel actually kindled this idea. What did you say there? You said something like, well, everyone can, what if everyone can just make their own copy of the monolith, right? Which is actually not an entirely stupid idea. Like that is the most brute force approach, right? But even if...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   14:03  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   14:11  
Even if that's what happened in all of the 12 teams, just make a copy, your own copy of the all repo, and just create pipelines to deploy your pieces. I would argue we're in a better situation than we're in today. And it obviously doesn't have to be that draconian. You can immediately start deleting a bunch of stuff.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   14:15  
I.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   14:16  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   14:33  
stuff that doesn't belong to you. Some teams can take a much more surgical approach because their components are not so intertwined or whatever, right? So it can be a little bit of a mix. But I mean, I'm just kind of illustrating that there is a way to get there. If the only goal is to like...  
By the end of next quarter.  
you should be deploying your things independently. I think it should be achievable. It's, you know, it'll come with a bunch of cost and we'll incur some additional tech debt and we'll have like copies of a bunch of shared libraries that, you know, is, but let's cross those bridges when we get there and say like.  
Hey, this library, oh, seven teams have made a copy of it. You know what? That seems worth it to carve out and put in artifactory or whatever.  
I don't know, I this is what I wanted to float and and talk about and and um see your reactions.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   15:40  
I mean, for me, I would love to get the monolith blown up, right? I would love that. I've been talking about it for, I don't know. Anyway, I don't love the idea of creating copies of the monolith. I'll say that up front.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   15:46  
Yeah.  
Me, me neither, but it again, it's I hopefully right, it doesn't have to be that, but let me let me offer a more more nuanced thing, right? Think of the monolith as a one circle, it's a Venn diagram right right now, and then each team needs to kind of circle what they need for their.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   16:03  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   16:16  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   16:16  
Domain, it's totally fine if there's a bunch of overlap at this point, if some, if some teams...  
make copies of the same shared library or whatever, right? And by the way, we're not saying you need to decouple at the data layer. All those couplings and using each other's databases will still exist in the first pass. It's just to get to you own your repos and you own your deployments.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   16:29  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   16:46  
That's like, that's the price, because now all the other things become easier after that.  
So I don't love it either, Mike. I'm just holding it out. There's like, it's like my sledgehammer blunt tool for the negativity. Yeah. So, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   16:53  
Yeah, yeah.  
Yeah.  
Yeah.  
Yeah.  
Yeah, yeah, yeah, I hear you. I guess I never thought of it as copying the monolith, right?  
I would say another brute force approach is you just copy your code, right? Don't bring all that baggage with you, maybe, right? And yeah, that gets you some code isolation that you can own. I'm not sure, I'm not close enough to it to know about.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   17:15  
Yeah.  
If...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   17:30  
You know, we have so much entanglement on the data that absolutely you can't do the data layer yet, right? No question about it. But my concern is if you have copies and everybody's operating on their own copy and it's not synced, and how that's heading, because lots of writes coming from everywhere.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   17:37  
Nope.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   17:50  
to certain areas, right, of the database. So we'd have to really think about that a little bit and how that could be pulled apart so that you have consistency of the data across, even though you're separated, you've got to have the same data you're working on, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   17:53  
Yeah, a lot.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   18:05  
Yeah, it doesn't, like, it's not an easy button, right? It doesn't just, it's not a silver bullet that you copy the monolith and now your team is fine, doing whatever you want. Yeah, yeah. The nice thing about it is it does reinforce what we're trying to push, which is the autonomous thing. I'd much rather...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   18:05  
Yeah.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   18:11  
Yeah.  
No, no, yeah, far from that, right? Far from that.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   18:15  
Right.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   18:27  
people just copy the code that they need. I think part of the challenge is they don't know.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   18:29  
Yeah.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   18:33  
all of those areas, which is otherwise they would have decoupled it already easily. So our current strategy is domain-driven design. You identify your domain, you identify that code, you pull it out, you modernize it, and it's just a little slower. And that's...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   18:37  
Mm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   18:38  
Yeah, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   18:39  
Good.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   18:49  
Yeah.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   18:52  
But it's a different strategy, so...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   18:55  
It's definitely a different strategy, right? I mean, the aggressive approach of, you know, I don't care if there's duplicate code and copies and whatever, that's fine, right? Because that's a temporary state. I'm still more concerned about, like, even though we separate, quote, separate, we're not really separated because you still have to have an interface into these other areas that are changing.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   19:16  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   19:17  
right? So your copy is out of date pretty quickly. And so you have to be having a, preferably an API that you can get to on these other areas now. That has to be done, otherwise, you know, they won't work together and they'll be out of sync completely.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   19:34  
Yeah, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   19:38  
Right, your your monolith copy becomes out of date immediately, almost.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   19:38  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   19:42  
Yeah, and sometimes it matters that it's out of date, sometimes it doesn't, right? Oh, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   19:43  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   19:44  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   19:49  
Sometimes it doesn't, yeah, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   19:51  
Well, it's not just the monolith though, right? Because like what we're seeing on the red mythos side, and sorry if I drop off camera, ET literally just said.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   19:52  
It's preferable.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   20:15  
No, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   20:16  
the auto all, like auto core, sorry, that's like all these other repos that are added together, which, you know, I'm actually not opposed to the idea of like sub modules, you know, pull them in directly to the copies, right? The tactical way to do this, which we can make it.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   20:24  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   20:32  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   20:37  
Really, you know, put it like still keep the the mono repo, but give everyone their own version of it, more coordination, more hands off, but like that's like a speed, that's a speed to.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   20:47  
Yeah, you're eliminating the common, the common part, right? Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   20:51  
Yeah, yeah, it's I don't know. I honestly I kind of like to take a like take like red center and just make that a template and then.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   20:53  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   21:00  
you know, tell teams to move towards that. But again, it's that domain knowledge, right? It's, I threw a graph. I created a knowledge base, knowledge graph out of our repo. It's, I literally had to run it for like 2 days because it was like, there's too much information, like 20,000 something nodes. I was like.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   21:17  
Yeah, I bet.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   21:19  
That this is ridiculous.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   21:19  
Yeah.  
Yeah, yeah, and that's a.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   21:22  
No.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   21:23  
It took a lot of effort to build that, Aaron. I am glad you recognize that, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   21:25  
Please.  
Yeah, I mean, it's kind of cool. It was just, it was like, okay, that's the complexity.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   21:31  
Access.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   21:32  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   21:33  
Yeah, so the bottom line is, I just I think we have to we have to do something, we have to just kind of do do something a bit differently, go a bit go about it a bit more aggressively, and and and again, if we to get to that.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   21:45  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   21:54  
Even just good enough autonomous states, like the first version of it, is going to be such an unlock because now everything else that needs to happen to get to a better state can now happen in these individual.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   22:02  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   22:13  
Teams.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   22:15  
Yeah, I mean, of course, I love the idea of isolation and being able to execute independently. I'm just not sure if we get enough of it from copying, you know, to get you to that step.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   22:30  
Um, well...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   22:31  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   22:33  
The other part I guess I would bring up is...  
I don't know about the, like, okay, we're in what, mid-May. So the time window that we have is finite.  
because we have to be able to do this DR and we can't mess around and miss that, right? So my question is, do we have enough time to get back to a stable point to be able to run DR without, otherwise DR could be another.  
disaster, right? Chasing them, because it's not how it used to be. It's not how it worked. Everybody's changed how it's going to work and how you're going to do DR now. Should be simpler because you're only worried about your own area, but it is different.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   23:05  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   23:14  
Mhm.  
Mhm.  
Yeah.  
Yeah.  
Yeah, I mean, I think that we would have to think that through, whether we just bank on the fact that we're going to get through that.  
decoupling phase one and end up in a state that's where deployments and IEC is buttoned up enough, right? That we, yeah. Or we have to decide, we don't feel confident with that. So then either first or in parallel or whatever, we need to do.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   23:38  
Thanks.  
Yep, yep.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   23:57  
The things that we talked about earlier, which is a combination of manual work and automation and I see to get production to where staging is now, so that is that would be.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   24:02  
You ought to be in, yeah.  
Yeah.  
Yeah, that's the problem, right? You can't you can't get halfway over the fence with it.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   24:11  
Wait.  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   24:14  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   24:14  
By that point, you either have to pick one or the other, you know.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   24:20  
What for this, like the requirement for doing DR, like, is that do we have to do it in December? Do we have to do it? I've heard rumors that we were going to keep it running in the other region for six months. Like, what's, I guess, like, part of me I'm wondering, like, why don't we just knock out the contractual obligation?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   24:35  
It.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   24:40  
Quickly.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   24:41  
Yeah, we.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   24:42  
And then, and then do...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   24:42  
I agree with that, actually.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   24:43  
We could definitely do that. If we had a way to do it whenever we want to before the end of the year, but it entails more manual work than we are comfortable with, but we, at least officially, we meet the four-hour RTO, then we're clear. We're clear for the year, basically.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   25:01  
The.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   25:02  
Right.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   25:02  
Yeah.  
I like that, especially because you knock it out of the way and now it's not this thing that's a burden over and shortening our time window, right? Oh, we got to take another shortcut because we're almost at this date, right? That's what I'd be concerned about. And we weren't talking about December. We were talking about October 1st.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   25:04  
Yeah.  
But.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   25:17  
Yes.  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   25:23  
Right.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   25:25  
Yeah, I mean, if we can be, I mean, it's like decoupling, doing a mass change, culture change at the same time. It's like.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   25:25  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   25:26  
So...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   25:33  
It would put the contractor side of it at risk, right? Like I just see a lot of, but it seems like we have lessons learned and if we could just pivot to prod as a quick demo and get this out of the way, man, it would probably relieve a lot of burden, just mental overload, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   25:38  
Yeah.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   25:49  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   25:51  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   25:53  
Warren, do you know, is it required to stay? Oh, sorry, go ahead, Aaron.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   25:53  
But.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   25:54  
So...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   25:56  
Amanda.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   25:57  
Oh, is it required to stay six months?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   25:58  
I don't know if they...  
I'm not, I don't think it's a requirement to stay for any amount of time. I think the thinking was that, one, it would be just better for us, like it's, you know, we would feel better internally about the solution, and also that it...  
Easier, because then we would only have to we would only have to do a flip over once.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   26:25  
Stay there. Yeah. Okay. Okay. Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   26:26  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   26:30  
Yeah, I mean, I think that's an interesting idea. Sorry, Marten, I do have to drop to this other call now, unfortunately.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   26:30  
Um...  
I don't know.  
Yeah, that's, yeah. Okay. Thanks.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   26:40  
I like the idea. I like it.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   26:42  
Yeah. So Daniel, do you have a gut feeling for if we were to do that, what Aaron is saying, let's just like force the envelope and do that, do that dumb in air codes, do that stupid production DR thing?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.jpg)**Michael Mitchell**   26:44  
Talk to you as well.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   26:55  
Yeah.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   27:02  
sooner rather than later, like when, how much work, like when could we do it? I think the thing is like we're held up by the, we can't do it before Atlas is my, that, so August 29th is the absolute earliest, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   27:09  
Yeah.  
Atlas Elasticsearch.  
Yeah, the Atlas and the Elasticsearch would be the preconditions that we'd need. We don't have to finish with Aurora, which is nice. But I think if that, I love that idea. I think that's really creative. It's just do it earlier. The question then would be,

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   27:24  
Never.  
Gill.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   27:37  
We go back to the teams and say, all right, what we'd like us to do is build a roadmap that basically says anything you need to do, what you did in stage, has to be able to be done in prod August 1st or whatever. And we just aim for that period. Because then they would, they would like that question you're asking, like, how's the roadmap written?  
We would force the roadmap to be written specifically to it, even if it's manual. Nobody cares. We're getting it out of the way, and then we're going to be done.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   27:58  
Mhm.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   28:08  
Let's just go build it. And then we'll get to the stuff we really, really want to do.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   28:14  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   28:16  
So it's some percentage of that current roadmap. But if we pivot to it now, I mean, that's something that we could accomplish, I'm sure.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   28:30  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   28:32  
And I like that idea.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   28:32  
I mean, it will.  
It'd be kind of fun to see the ISE side because like right now, I think between EA and DevSecOps, I'm just trying to figure out what is our ISE tool for the time being and just being able to go through it because Suresh, it's funny you mentioned Suresh because he and I are trying to figure out like CDK.  
over Terraform. Like, again, like, I'm going to say this so other people can hold me accountable, and because this is how I think about it, I don't care. I just care that we're really good at one or the other. That's it. Just be good at it. I don't, doesn't matter what it is. But we just got to figure that out.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   28:55  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   28:55  
Mhm.  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   29:13  
right for IC because I think right now the way it's running is it's all pipelines. It's all, it's a handful of people to do this work. So.  
I don't know. I think something I'm taking notes on was I might reach out to you, Daniel, and then to Mike also about maybe let's just start building up guilds within exchange. And so people who are good with IAC, people who are good at CICD.  
and just nominate a person from each team and make them just able to be part of this. Because my fear right now is everyone's, each team's going to do their own thing, right? So if we force them together, then I can go through and start documenting setting patterns and practices with them that way.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   30:00  
So, here, here's a question for you: if we say we're gonna do the DR thing requirement first, and let's just pretend it's August 1st and all of other migrations complete by then, do we do we need the right IAC for that exercise or...  
Can we just allow whatever we're doing now, replicate in prod, do it under 3 hours. That's the.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   30:28  
Yeah, no, I think it's just setting the setting the guild format is what's needed, right? It's just getting the group to think together and then we'll figure out the right tool. Like I'm not, I don't think, truthfully, I don't think Exchange will be in the position to just dictate the tool. I think the way like EA and DevSecOps are moving, they want it.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   30:29  
That's the goal.  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   30:50  
dictate tools, which I don't, as long as they build a system to manage it, it doesn't really matter. So that, I think there's time for that conversation to have. So no, I don't think it impacts doing DR early. I just think let's just build up a little, build up that standing bi-weekly meeting and make that a thing where.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   30:51  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   31:11  
that, you know, each team has one person there and it's not the same. Hopefully it's not the same as a lead, right? It has to be someone who we want to build that skill set up on the team.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   31:20  
Sure.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   31:23  
So, so one one thing that...  
One piece that kind of led to this conversation was the...  
insight or realization that  
And with the current DR plan, just, you know, we're going to be syncing a lot of work into changes and whatever in bamboo deployment scripts, which is essentially throwaway work, right?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   31:59  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   32:00  
Is that, would that be part of this approach or would we just, would we just, it would just be the exact manual approach that we're doing now. You see what I'm saying?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   32:12  
Yeah, I mean, from the from the CICD point of view, right, like we're not.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   32:13  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   32:18  
So we should be just adding the GitHub actions as we go or building it. The DevSecOps team is trying to do that. I just don't think we're going to miss out on the D. I think.  
I think we're stuck with bamboo the way we have it. So the quick and easy fix it, let it just use it as is, because it's going to go away. There's no point spending time. Like, I don't see us, based on everyone I've talked to, right? Like, I've been trying to figure out this bamboo piece.  
And there's only a couple of people who really know how to use Bamboo. There's Tim's a great administrator, but he's not managing pipelines. Like everyone wants to get a GitHub actions as soon as possible.  
but they're far away from actually getting it ready, up and running for the teams to use GitHub actions. So let's give them, let's use bamboo because we have to, and take lessons learned, right? It's just notes, just notes on what we've learned, what we had, and let the CICD team or...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   33:12  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   33:26  
shared services or whoever else decides to take over GitHub actions, let them learn from it, or we learn and we write our own, which we're more likely to write our own anyways. I think the IPA team already has like writing GitHub actions on their backlog without any support. So I'm.  
I'd say just, I don't think it would throw those work; I think it is necessary work.  
Longest way of saying that.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   33:53  
Right.  
Yeah.  
And...  
Yeah.  
And what about a third? OK, so what about a third approach where we would?  
Again, just put the pedal to the metal on the...  
Decoupling work.  
Uh...  
And then if we get to, so we do that essentially for.  
Let's say the third quarter.  
And then if we get to end of that and it looks like, you know what, we're not, we're at this rate, we're going to miss the DR deadline.  
then we have to pivot and do the semi-manual, basically pick up the current plan again at that point.  
Or we get to, we get to that point and we say, you know what, this is actually, we're tracking well here. We're going to be in a state where we have.  
We have enough new automation in in the all in these new decoupled repos that it's gonna solve, it's gonna get us to the target for for DR.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   35:28  
Yeah, I like the idea of pivoting is.  
infrequently as we can. Like, since we know that we got to do the DR work, maybe we just prioritize that first, because then we don't have to pivot to it if we don't get as far ahead on the decoupling as we want.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   35:34  
Yeah.  
Yeah, I mean, the one piece of heartburn that I get there is that we're sort of, we can't, we're, like, it's the whole Atlas migration time frame, right? Like, basically, there's no way we can finish it until,  
September at the earliest, right? And this is not one of those, we don't want to try to parallelize these things. I think we just need laser focus on either or, to be honest. And we know, we all know if there's a, if the time frame is that long, that's how long it's going to take, which is probably longer than it needs to take.  
That's kind of, that's my, that's my concern. In other words, if we did have, if we were all migrated to Atlas already, from the sounds of it, it sounds like we would, we would be, we would be doing that production DR exercise.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   36:30  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   36:49  
much sooner than September, but because of that sort of atlas thing, it's going to drag on till then.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   37:00  
Yeah, and...  
That is annoying.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   37:04  
Yeah.  
Exactly.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   37:09  
Uh, sorry then, can we...  
I guess we'd have to ask Sherard, but can he do a four-hour RTO on the current?  
Stack the current config with.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   37:24  
And it certainly didn't seem like it. It seemed like that shave, removing those two whatever plus hours of data backup restores, that was definitely part of the part of the solve.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   37:39  
Four.  
Mm.  
That's too bad.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   37:49  
So I'm going to, I love these DR things because they're fun. But there's so much about it that I don't know. So I'm just asking really dumb questions here. But.  
How much of the DR is actually defined as DR? Like, why do we need the database in another region? Like, is true, like, are we, I mean, I think we talk about true disaster recovery, but I'm looking at the contractual side of this, right? Is the goal for Cardinal to...  
just have them sending data to a new region? Like how much of this do we actually have to go with build a new exchange in another region and all the data and everything behind that?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   38:31  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   38:33  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   38:35  
All right.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   38:36  
It.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   38:38  
Hello.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   38:39  
Yeah, sorry. Go ahead, Marten. I'll jump in.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   38:40  
I, I think, and you might know better than I do, Daniel, but I think that the simulated scenario is that the region that we that we are hosted in gets like...  
Fully white that during the, you know, yeah, it doesn't come back, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   38:57  
Close.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   39:03  
Yeah, the, the, the.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   39:03  
But who specified that like?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   39:06  
What was that?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   39:06  
So we get talked, this is the honest truth, right, about GHX right now. When we get on technical calls with customers, they dictate the terms of those conversations. We are not good at explaining our disaster recovery.  
across availability zones, how the geographical separations availability zones operate, the math on failing over a 99.8 uptime to another region, and how that doesn't work in your favor. So we lost those conversations.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   39:46  
OK.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   39:46  
And they dictated the terms, you will fail over to another region and we signed our name to it.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   39:52  
Okay, okay, so that's, there's no wiggle room on that. I, yeah, yeah, DR exercises are terrible. So yeah, just, I was really hoping we could get away with like an AZ change or just architectural demonstration, but part of this isn't.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   40:09  
Right there with you, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   40:15  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   40:22  
There, there.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   40:23  
and screen reader saw VoiceOver. If you know how to use VoiceOver, press Command and now to turn it on and set up your map. If you would, there we go.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   40:26  
The.  
Ohh, okay.  
They are very concerned that Cardinal will badmouth us to everybody and they'd rather have Cardinal tell everybody how awesome we are. So there's part of that as well.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   40:45  
Okay, so I was going to ask that actually, just for not that it matters, but how big of a customer is Cardinal? But there's more to it than the than the sort of size of that particular contract, obviously. So, yeah, okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   40:59  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   41:00  
OK.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   41:01  
They're one of the big ones, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   41:01  
All right.  
Yeah.  
Yeah, so...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   41:08  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   41:09  
Um...  
So, okay, so where we ended this morning, just for your benefit, Aaron, is basically, we're going to meet again next Friday. We definitely planted the seed hard with everyone. They should go and think about, you know, what this would look like. Matt Turner and Phil Matt Turner,  
He had, I mean, that was a super good point that we need to very better than what we have so far, defining the domain for each team, like down to the component. You know, so everyone, so each team knows what it means when we say you need to decouple your things, right? So that's going to kind of.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   41:41  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   41:50  
That work is going to start happening, and then we're just going to continue riffing on this in a week, and so I hope, I hope people don't forget about it for, you know, for 6 1/2 days, but...  
Yeah, that's kind of the plan, but I, it is really, it is the number one, the decoupling is the number one focus.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   42:08  
Cain.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   42:20  
One, because I firmly believe we need it and it's going to be such an unlock, but the expectation is there also from what I mean, Daniel, you can probably educate us on the past, but we've been talking about it for a long time and basically patience is growing thin with this like...  
resiliency roadmap that we're just like piecemeal chipping away at or whatever, right? So, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   42:46  
Mhm.  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   42:51  
Which is, a lot of that is not really our fault, because you know there's curve ball after curve ball after curve ball, but that tends to be forgotten, but with that said, even without all that, like all that baggage, I'm still maintaining.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   42:52  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   43:02  
Okay.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   43:08  
If we can just get to 12 teams that can execute on their own, regardless of how scruffy that first phase is and how much of A, you know, and again, I know we're not going to do this, but if they just like everyone made had a copy of the freaking monolith, like it's still better than what we're at now. And I mean,

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   43:28  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   43:29  
Yeah, so that's there's there and and then couple that with all this all the appetite and all the understanding for this this posture right now, and we just we need to find a way to do it, so yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   43:46  
Okay. This whole domain breakdown thing, it's, and I know it's been on your list for a couple weeks now. Like, how do you want to, how do you want to see this done? I mean, because I know that's something like, I feel like this is something Ben would really enjoy.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   43:50  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   44:05  
And so would I, like being able to break that kind of stuff down. So we have this rhythm at those project that we're doing at the same time. So I'm trying to be, I'm trying to be balanced, right? Like I don't want to like decoupling is great, IAC is great, but like I want to get this, I'm gonna get these vulnerabilities out. I want to be done with this project. I'm telling you, I don't want to be.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   44:07  
Yeah.  
Yeah, yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   44:21  
Haha.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   44:22  
Yeah.  
Up.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   44:27  
So.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   44:27  
Well, so I don't know what are you saying that you want to be part of those or you don't want to be part of it?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   44:31  
I think, I mean, I think I wanna be able to, I wanna be part of it. I just wanna know how the timing of that will play out in your in your mind and and the teams, right? I think I think that's something where, at least like working with Ben the last two weeks, like he has a wealth of knowledge, like he's paying attention and...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   44:42  
Alright.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   44:50  
has a lot of really good opinions. And so I want to, at the very least, I don't want to, I don't want him to lose out on the chance.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   44:51  
Yeah.  
So...  
Yeah, so maybe, so maybe, maybe it looks like maybe each team does their own pass, basically fills in their section on this confluence page or whatever, and then that leads to kind of check-ins from you and Ben and Daniel, where like...  
And are you sure? Have you thought about this? Like, does this really belong with you? That kind of thing? I don't know.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   45:25  
Yeah, I think that's that we can we can set that up, and Ben has a good Excel sheet that you know we can just start with. I think that'll be huge, honestly. I think that'd be really huge if we if we have that available.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   45:40  
So, maybe, maybe actually that that's kind of a we can.  
communicate that out as a goal. Like, let's say the week of May 18th, we want to be able to book just sessions and...  
Cashly chat through the list that everyone has put together and just sanity check it and, you know, ask questions. I don't know, how does that sound?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   46:13  
Think that, let me talk to Ben.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   46:15  
The, the other, the other, the other piece here is that we're starting sort of pre-Q3 planning activities, right? Like, so this is very good to tee up there. Again, Laura pretty much said, like, you should just take whatever capacity you need if it's for...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   46:16  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   46:34  
If it's for decoupling work.  
But for her to be able to defend that or help us defend it, it needs to be more than just a huge blank placeholder, you know.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   46:48  
Yeah, I mean, I think that's the domains, like getting, I mean, it's not even domains, right? It's actually down to the folder within the repo that matters. Once we get there, then it then it's easy to say, set the like in parallel, I can I can easily write up a definition of done.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   46:57  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   47:08  
For, for the like, what does decoupling looks like, and I think Daniel and I are gonna are write up on the staff page what autonomous teams looks like. I already put some stuff there, but once we set those definitions of done up that way, then it becomes really easy to say, you guys agreed.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   47:08  
Mhm.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   47:27  
to this is your world. Now here's the target.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   47:29  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   47:31  
figure it out, right? Or what would the EMs at least figure it out.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   47:32  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   47:32  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   47:37  
How does that sound?

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   47:37  
Yep.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   47:39  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   47:39  
It's, yeah, it it it is, it sounds good. The where the teams are at right now is they have business value and high level components, but to your point, Aaron, like nobody has gone down to the what folder in the repo does belongs to me.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   47:56  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   47:58  
And how does that work when I pull it out? And how do I define, like, when, like the organization team knows that they should own relationship validation. That's an event right now that does work, that has strategies. How do we contract that between the eventing system and the org team that's doing that? Is that an API call or something else?  
We don't have that.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   48:19  
Yeah, but I think we start with the boundaries and then I think what I really like about the teams a lot is and really impressed with is like this, the structure with the sprinting, it's really, really good. And so part of what could be, we could leverage is.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   48:20  
So.

![20](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   48:39  
add people into the other team's grooming session if they have work they think they need. Add, you know, do more of a bigger sprint review where everyone can kind of start to talk about the things that they depend or where they're blocked, right? And just, I think just leveraging that, I mean, that's, I...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   48:52  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   48:59  
Cannot say this enough, that is such a huge superpower for an org to have good sprint and agile hygiene that we can leverage it. And it'll go slow. It's not going to be like audit really quick. Like we'll have systems for contract management and stuff, but it will be at least, it'll be the start of it.  
And I think we can iterate through that part quicker than, I don't know, it's a theory though, but I've been impressed with the team, so like really well, so.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   49:25  
Awesome.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   49:26  
I know.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   49:30  
Um...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   49:30  
And.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   49:35  
All right.  
What else?  
Yeah, okay. Well, that's the...  
Those are the.  
Seeds I wanted to plant.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   49:56  
I'll talk to Ben about the about the get the domain stuff together. You and I are gonna talk anyways about run mythos, so...

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   50:04  
Pull Matt Turner into that, if you will, 'cause he's off doing the same type of thing, and so he and he's really interested in it.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   50:04  
Think.  
Yeah.  
Okay.  
Okay, yeah, I'll grab a do a chat with them. Sweet.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   50:15  
Cool.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   50:18  
All right.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   50:19  
I.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   50:21  
Yep.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   50:22  
Thanks, all. All right.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   50:23  
Thanks, guys.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.jpg)**Marten Engblom**   50:24  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)**Aaron Srivastava**   50:24  
Yeah.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)**Daniel Milburn**   50:25  
Like.

![](file:////Users/mengblom/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)**Marten Engblom** stopped transcription

---

## Executive Summary

Strategic planning session on monolith decoupling and DR timing. Team debated whether to prioritize GitHub migration/decoupling work versus getting DR contractual obligation done quickly. Recent DR test showed promising 2-3 hour RTO (under 4-hour target) once Atlas migration completes. Key insight: decoupling is the #1 unlock but Atlas migration blocks DR until late August. Emerging consensus: consider doing DR exercise early (August) to clear deadline pressure, then focus fully on decoupling work. Laura (product) fully supportive of taking necessary capacity. Critical next step: define team domains down to folder/component level by May 18th.

**Key Metrics:**
- **Current DR RTO:** ~2-3 hours (projected with Atlas)
- **Target:** 4 hours
- **DR Deadline:** Before end of year (October originally discussed)
- **Atlas Migration Complete:** End of August

---

## Key Topics Discussed

- **DR Timing Strategy - Two Goals:**
  - Contractual obligation to Cardinal (flip and stay before year-end)
  - Internal confidence in DR capabilities (currently manual, needs automation)
  - Recent stage DR test: 7 hours actual, but could be 2-3 hours with Atlas + SSO fixes
  - Question: Do we have 90% production readiness or are we fooling ourselves?

- **Decoupling as #1 Priority:**
  - Unanimous agreement that autonomous teams is the critical unlock
  - Current state: Everything is a project because of monolith coordination overhead
  - Laura (product) explicitly supportive: "Take all the capacity you need"
  - CJ and leadership understand the importance
  - Multiple previous attempts, patience wearing thin

- **Brute Force vs. Elegant Approach:**
  - Daniel's idea: What if teams just copy the monolith?
  - Marten: Even if all 12 teams copied the repo, it's better than current state
  - Reality: Spectrum from surgical decoupling to copy-and-delete approaches
  - Data layer coupling can remain in Phase 1 - focus is on deployment autonomy
  - Mike's concern: Copies get out of sync quickly, need API contracts

- **Three Potential Paths:**
  1. **Decouple now, hope it covers DR:** Risk missing October deadline if decoupling takes longer
  2. **DR first, then decouple:** Manual/semi-automated DR work in bamboo (throwaway effort), but clears deadline
  3. **Hybrid/pivot approach:** Start decoupling, pivot to DR prep if tracking poorly by mid-quarter

- **Blockers & Constraints:**
  - Atlas migration won't complete until end of August (earliest DR date)
  - Can't do 4-hour RTO without Atlas (eliminates 2.5hr database restore)
  - Cardinal contract requirement: full region failover (not just AZ)
  - Customer dictated terms, reputational risk with large customer

- **Domain Definition Work:**
  - Matt Turner's point: Need domains defined down to component/folder level
  - Current state: Teams have business value and high-level components only
  - Don't know: Which folders belong to which team, how to contract between services
  - Example: Org team owns relationship validation event - is that API or event-driven?

- **IAC & CICD Strategy:**
  - Aaron: Don't care if it's CDK or Terraform, just be really good at one
  - Current state: Handful of people doing all IAC work via pipelines
  - Proposal: Guild model - nominate one person per team for IAC guild, one for CICD guild
  - Document patterns and practices collaboratively
  - Let EA and DevSecOps dictate tools as long as they support it
  - Bamboo is temporary - everyone wants GitHub Actions but DevSecOps not ready yet

- **Q3 Planning Context:**
  - Pre-Q3 planning activities starting
  - Laura needs more than blank placeholder to defend capacity allocation
  - Need: Domain definitions + definition of done + roadmap/plan

---

## Decisions Made

- **Decoupling is the #1 organizational priority** - unanimous agreement from leadership
- **Meet again next Friday (May 15th)** to continue planning and review progress
- **Target: May 18th week** for domain review sessions with teams
- **Consider early DR exercise** (August) to clear contractual obligation, then focus on decoupling
- **Not requiring perfect decoupling** - teams can use spectrum of approaches based on their domain complexity
- **Bamboo work is acceptable** for DR even though it's throwaway - GitHub Actions not ready yet

---

## Action Items

### For Aaron
- [ ] Work with Ben on domain breakdown spreadsheet/template [[^task-20260508-001]]
- [ ] Involve Matt Turner in domain definition work [[^task-20260508-002]]
- [ ] Draft definition of done for decoupling work [[^task-20260508-003]]
- [ ] Coordinate with Daniel on definition of autonomous teams [[^task-20260508-004]]
- [ ] Explore guild model formation (IAC guild, CICD guild) [[^task-20260508-005]]

### For Teams
- [ ] Define team domains down to folder/component level in mono repo [[^task-20260508-006]]
- [ ] Complete domain definitions by week of May 18th for review sessions [[^task-20260508-007]]

### For Daniel
- [ ] Work with Aaron on autonomous teams definition [[^task-20260508-008]]
- [ ] Assess if current DR roadmap can be scoped to August timeline [[^task-20260508-009]]

### For Marten
- [ ] Prepare for next Friday's planning session (May 15th) [[^task-20260508-010]]
- [ ] Coordinate Q3 planning with domain definition work [[^task-20260508-011]]

---

## Follow-ups

- Next planning meeting: Friday, May 15th
- Domain review sessions: Week of May 18th
- Q3 planning cycle incorporating decoupling work
- Decision point: Mid-quarter check on decoupling progress vs. DR deadline
- Atlas migration completion: End of August (blocks DR exercise)

---

## Related

**People:** [[Daniel_Milburn|Daniel Milburn]], [[Mike_Mitchell|Mike Mitchell]], [[Aaron_Srivastava|Aaron Srivastava]], Curtis, [[CJ_Singh]], Laura, Matt Turner, Ben, Suresh  
**Projects:** [[04-Projects/Exchange_Resiliency_2026]], Exchange Atlas Migration, Monolith Decoupling  
**Companies:** Cardinal (customer driving DR requirement)  
**Context:** Strategic inflection point - balancing contractual DR obligation with critical architectural transformation. Leadership alignment on decoupling as top priority, but timing and approach still being debated.
