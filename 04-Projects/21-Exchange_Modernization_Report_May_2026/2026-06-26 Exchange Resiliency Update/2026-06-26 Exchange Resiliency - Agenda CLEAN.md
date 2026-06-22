# Exchange Resiliency Update - CJ Meeting
**Date:** Friday, June 26, 2026 @ 11:00 MT
**Objective:** Tell the Exchange story - significant progress has been made, but nobody has told the narrative

---

## 1. Resiliency Work Completed (Map to Original Incident Root Causes)

**Goal:** Show work accomplished over 18 months tied back to incident root causes from `Exchange_Plan_Latest.pptx`

**Sources:**
- OneDrive: `Exchange Resiliency/Exchange_Plan_Latest.pptx` (Feb 2025 board deck with 13 incidents)
- OneDrive: `Exchange Resiliency/Exchange Resiliency Completed.docx` (draft list, needs detail)

**What I need:**
- Map completed work to specific incident root causes (e.g., "Lack of Domain Separation" → decoupling work completed)
- Add detail: what was done, when, Jira references
- Get help from Daniel, Mike, others to flesh this out

---

## 2. Six Resiliency Priorities Update

**Source:** OneDrive `Exchange Resiliency/2026 Tech Org Priorities - Copy.pptx`

1. **DB Migration to managed databases** - MongoDB → Atlas, Elasticsearch → Elastic Cloud (project status?)
2. **DR Drills (RTO 4hr, RPO 2hr)** - Daniel's DR project (when completed? results?)
3. **Vulnerabilities within SLA** - Red Mythos Exchange (Aaron) - current SLA compliance?
4. **EOL technologies eliminated** - Red Mythos Exchange (Aaron) - what specifically upgraded/replaced?
5. **Industry Continuity Solution** - Contractor solution (Jena Milan's June 15 email has status)
6. **Increase Modularity** - Breaking the monolith (examples in `Exchange Resiliency Completed.docx`)

**What I need:**
- Current status for each (completed? in-progress? metrics?)
- Impact for each (incidents prevented, performance improvements)

---

## 3. Organization Transformation Story

**Goal:** Show how Exchange became a world-class engineering org (CJ's words)

**Transformation:**
- **From:** 1 director, 3 managers, ~100 engineers (monolithic structure)
- **To:** 4 directors, 12 managers, 3-5 person teams (modern structure)
- **Model:** Top-tier orgs (FAANG, Spotify, etc.)

**What I need:**
- Examples/references showing how top companies structure teams (for non-technical audience)
- Henrik Kniberg's Spotify Engineering Culture videos
- Blog posts or case studies from FAANG orgs
- Impact metrics (faster incident response, independent deployment, etc.)

---

## 4. Current Work (Before Q4 Capacity Shift)

**What we're doing now to prepare:**

1. **Reverse Conway Maneuver** - Restructuring teams to match desired architecture
2. **Autonomous teams** - 12 teams with independent deployment pipelines
3. **Continued decoupling** - Ongoing separation of monolithic components
4. **P0 Database items** - Audit DB re-architecture, BT/BD scalability, Event Bus replacement

**What I need:**
- Status on autonomous teams rollout (how many ready? timeline?)
- Specific decoupling examples with deployment independence gained
- Current state on P0 database work

---

## 5. Strategic Roadmap (What's Left)

**Context:** Tina Murphy expects ~2 year roadmap for remaining technical work

**Key themes:**

1. **Continued DB layer improvements** - Scalability, performance, reliability
2. **True SOA architecture** - Continued decoupling toward service-oriented architecture
3. **Replace homegrown Event Bus** - Modern messaging/event framework (Kafka? EventBridge?)
4. **Replace homegrown IdP** - Auth0 implementation for identity/auth
5. **Plus more** - Need input from directors on additional priorities

**What I need:**
- Directors' input on remaining roadmap priorities
- Rough timeline/sequencing
- How this enables future commercial velocity

---

## Action Items

- [ ] Flesh out `Exchange Resiliency Completed.docx` with Daniel, Mike (what, when, impact, Jira refs)
- [ ] Get current status on 6 resiliency priorities (Daniel, Aaron, Jena's email)
- [ ] Find references for org transformation (Spotify videos, FAANG blog posts)
- [ ] Document autonomous teams rollout status
- [ ] Get directors' input on Section 5 roadmap priorities
