# RCA Planning & Leadership Communication Strategy - June 24, 2026

**Meeting:** Incident RCA, GFAC issues, and CI/CD pipeline standardization  
**Date:** June 24, 2026 (afternoon)  
**Participants:** [[CJ_Singh]], [[Arshad_Mahammad]], [[Marten_Engblom]]

---

## Executive Summary

CJ directed high-quality RCA covering both the June 22-24 incident and recent GFax issues (last month), to be completed Friday/Monday and published EOD Monday. Arshad to lead accelerated CI/CD pipeline standardization plan. Marten to draft comprehensive email to GLT/SLT following specific structure, vetted by Ramesh before sending.

---

## Key Directives from CJ

### 1. Root Cause Analysis

**Scope:**
- This incident (June 22-24, six simultaneous issues + AS2 rollback)
- All recent GFax issues (last month, not just this incident)
- Steve Jackson raised concerns about GFax reliability declining over 4-8 weeks

**Process:**
- High quality, blameless postmortem
- Marten and Arshad to partner and lead
- Everyone has a voice
- Dedicated session (not just Wednesday meeting)
- Timeline: Friday and Monday to prepare
- **Publish by EOD Monday**

**CJ's Framing:**
> "This is a big event, right? This is not a trivial event. Everybody should have a voice. It should be a well run blameless postmortem."

> "Steve said that g fax issues have been lingering for the last several weeks. And having severe impact on customers... Death by a thousand paper cuts, we may be in that situation. Let's get a list of all the G facts issues in the last month or so, so that all the fans are on the table."

---

### 2. CI/CD Pipeline Standardization

**Owner:** Arshad Mahammad

**Context:**
- This incident + last week's API exposure issue increased urgency significantly
- Goal: 100% of teams on standard CI/CD pipelines
- All options on table:
  - More people
  - External help
  - Central tiger team
  - Moving people internally

**CJ's Directive:**
> "Whatever is needed... All options are on the table. We only need to optimize for speed of getting 100% of the teams on standard CI/CD pipelines."

**Collaboration:**
- Arshad owns the plan (one plan, not multiple plans)
- Marten to work closely with Arshad (same partnership model as RCA)
- Arshad to start putting "pen to paper" on plan

---

### 3. Communication to Extended Leadership (GLT/SLT)

**Process:**
1. Marten to write draft following CJ's structure
2. Send draft to Ramesh Donnipadu for review
3. Ramesh and Marten to read through together and align
4. Send to GLT/SLT group

**CJ's Structure (10 Key Points):**

**Point 1:** Currently minimal customer impact (be very precise)

**Point 2:** Minimal impact on internal GHXers

**Point 3:** X incidents closed, one incident open

**Point 4:** For open incident, plan is to do hotfix on [specific date] - "measure thrice before we cut" (instead of rushing)

**Point 5:** Clarify this will be **last deployment before change freeze** (build confidence - historically July 4th period has issues, want to confirm stable state)

**Point 6:** Confirm: "We are in change freeze and we are in a stable state"

**Point 7:** Anticipate Friday/Monday for high quality RCA covering:
- This incident
- All GFax issues from last month

**Point 8:** Anticipate publishing RCA by **EOD Monday**

**Point 9:** While not jumping the gun, **foreshadow** a couple material things that will come out of RCA (build confidence - show we understand what happened)

**Point 10:** Close with: "If there's any change to this, you'll hear from me. Otherwise expect an update from me EOD Monday."

**CJ's Guidance:**
> "I think the first point I would communicate is currently there is minimal customer impact. But be clear what it is. Very precise."

> "You want to build confidence about that because usually, unfortunately, last to july fourth, there have been massive issues."

> "You want to build confidence. It's not like we have no clue what happened."

---

## Context & Rationale

### Historical Pattern (July 4th Period)
CJ noted that "last to july 4th, there have been massive issues" historically. This email needs to build confidence that:
- We're heading into change freeze in stable state
- We understand what happened
- Last deployment before freeze will be measured and careful

### Steve Jackson's Concerns
Steve raised concerns in 1:1 with CJ about GFax reliability declining over 4-8 weeks, not just this incident. RCA must address broader pattern.

### API Exposure Incident
CJ referenced "the issue last week about the API exposure" as compounding the urgency for CI/CD standardization. Combined with this incident, raised sense of urgency "quite a lot."

---

## Marten's Response & Clarifications

### On GFax Issues
Marten acknowledged that smaller GFax issues may not have "bubbled up to a big discussion on my end to be honest" but confirmed he's not discounting Steve's feedback or the email Steve sent.

### On CI/CD Plan
Marten wants to sync with Arshad on pipeline plan to ensure alignment with Exchange team's plans, but CJ clarified: "There's going to be one plan... Arshad is going to own it."

---

## Other Context

### Veritas Sessions (June 2-3)
- Wednesday and half day Thursday
- On-site sessions
- CJ working on agenda
- Wants Marten to "nail" the leadership discussion work before holiday
- Scheduled 1-hour in-person meeting Thursday July 2 at noon

### Friday Meeting with Curtis
- Original meeting on Friday moved (Marten didn't have bandwidth during incident wrap-up)
- Decided to keep Friday meeting as "organic discussion" instead of formal presentation
- Follow-up hour scheduled Thursday July 2 at noon (in-person)

---

## Next Actions

**Marten:**
- [ ] Draft comprehensive email to GLT/SLT following CJ's 10-point structure
- [ ] Send draft to Ramesh for review (CJ will connect via text)
- [ ] Review with Ramesh, align before sending
- [ ] Prepare for Friday RCA kickoff
- [ ] Sync with Arshad on CI/CD pipeline plan
- [ ] Identify 2-3 material RCA findings to foreshadow in email

**Arshad:**
- [ ] Lead CI/CD pipeline standardization plan
- [ ] Partner with Marten on RCA
- [ ] Start drafting pipeline standardization plan

**Ramesh:**
- [ ] Review draft email with Marten before sending
- [ ] Coordinate on communication to extended leadership

---

## Key Quotes

**CJ on RCA Scope:**
> "I want a real high quality RCA and Martin and Arshad, you should partner to lead it. Where everybody has a voice."

**CJ on CI/CD Urgency:**
> "This incident plus the issue last week about the API exposure. I think both of them combined have raised my sense of urgency quite a lot on having a clear documented plan to get 100% of teams on standard CI/CD pipelines."

**CJ on Communication Close:**
> "If there's any change to this, you'll hear from me. Otherwise expect an update from me end of day Monday."

---

## Related Documents

- [TIMELINE.md](TIMELINE.md) - Incident chronology
- [COMMUNICATIONS_INDEX.md](COMMUNICATIONS_INDEX.md) - Previous communications
- [2026-06-22_Production_Incident_Comprehensive_Record.md](2026-06-22_Production_Incident_Comprehensive_Record.md) - Initial root cause analysis

---

**Document Purpose:** Capture CJ's directives for RCA, pipeline standardization, and leadership communication strategy  
**Created:** June 24, 2026  
**Status:** Action items identified, email draft in progress
