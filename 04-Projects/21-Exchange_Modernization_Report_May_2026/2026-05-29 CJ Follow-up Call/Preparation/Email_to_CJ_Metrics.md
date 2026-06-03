# Email to CJ - Metrics Discussion (May 29)

**Subject:** Quick context before tomorrow's metrics discussion

---

CJ,

I know we are meeting shortly, but thought it might be helpful to put some things around metrics in writing as well.

**Current State:**
Today we track incidents (BROKEN tickets), deployment frequency, and lead time to change in the KMP Dashboard at the pod level. CFR and MTTR exist in the dashboard but aren't correctly reported - requires JIRA labeling discipline we haven't enforced. We're missing comprehensive view of bugs that don't escalate to incidents (the "first-pass yield" gap you asked about) and team-level visibility (current metrics are pod-level, not individual teams). We also don't have a developer platform like Compass or Backstage today.

**What's Being Put in Place:**
We have outlined a detailed implementation plan (attached).

**Phase 1 - Available Now (Bitbucket DC):**
- Deployment Frequency (Jira Deployment Insights)
- Lead Time / Cycle Time (Jira Cycle Time Report)
- Sprint velocity, WIP, Issue cycle time (native Jira reports)
- Security metrics (Wiz/Xray auto-creating tickets in each team's Jira project)

**Phase 2 - After GitHub Migration:**
- Full Compass DevEx dashboard (Deployment Frequency, Build Success Rate, Build Time, PR Cycle Time, Open PRs)
- MTTR via PagerDuty integration
- Change Failure Rate (Compass - configuration in progress)

**Why the split:** Compass is cloud-only and doesn't support Bitbucket DC (no workaround exists). Deployment Insights works with Bitbucket DC, but full DORA suite requires GitHub.

**Requirements (From Exchange Team Standards):**
- Native Jira projects per team (not boards pulling from everywhere) - enables team-level metrics
- CI/CD pipelines sending deployment events to Jira
- Jira issue keys in branch names, commit messages, PR titles (e.g. `ENG-123`)
- 4 weeks of data before rolling averages display


**Worth noting:** several teams are newly formed, some still hiring (25 open roles including 3 managers). Organizational research shows teams go through forming/storming/norming stages before reaching peak performance. Collecting data now establishes baselines, but we should expect metrics to stabilize once teams are fully staffed and have worked together for a few sprints. Measuring a team in flux captures transition state, not steady-state capability.

**Connection to Strategy:**
This maps directly to the Exchange Team Standards and autonomous teams work - native Jira projects per team enable both independent operation AND team-level metrics visibility. Security findings (Wiz/Xray) land in each team's own Jira project alongside delivery work, visible in their native reports. No manual aggregation needed.

Hope that helps.

Marten
