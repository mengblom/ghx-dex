### Agenda ###
1. Round Robin
2. Q3 Priority Comms
3. Glint survey

### Notes ###

#### 1. Round Robin Updates

**Marten:**
- **CJ Deck Follow-up:** Sent deck on tech priorities (DR, Red Mythos, breaking the monolith). CJ came back with 5+ follow-up questions:
  - How many new services are we creating?
  - How are we prioritizing them? Tied to incident root causes?
  - Which services can be created in parallel?
  - Is there a logical architecture diagram of end state?
  - What's the trade-off if we stop breaking the monolith by end of Q3?
- **Architecture Clarity:** Don't want overly detailed end-state now (would be waste or lying). High-level architecture follows team formation. Some teams (e.g., Visibility) already have service breakdown mapped out.
- **Action:** Need format to fill in architecture canvas as we go. Michael suggested each team create their own domain view. Aaron noted Matt Turner's domain ownership page needs review.
- **Kick Drum Follow-up:** Easy meeting - they wanted to confirm no hidden tech debt we haven't shared. Michael noted there's likely undocumented tech debt across teams that's not in Jira/Confluence. Daniel confirmed fair amount exists, but org has changed radically since October. Ramesh suggested organizing tech debt by higher-level objectives (e.g., "what prevents you from being autonomous?").
- **Veritas Call:** Monday meeting scheduled to discuss key challenges, Kick Drum feedback, and how to focus engagement going forward. May be related to CJ's frustration about lack of depth from Kick Drum (only 3 weeks in).
- **Q3 Focus:** Thinking about how to get more focused for Q3 and beyond along the technical buckets/team setup.

**Aaron:**
- **Red Mythos Progress:**
  - Ben has work planned in EX OSS board for library/infrastructure/external resource upgrades
  - Christine added to chat for dependency awareness during sprint reviews
  - Team has knocked out package upgrades, Claude skills, refactoring
  - Shared AI plugin repo getting filled out with learnings
  - Infrastructure changes affecting OSS dashboard, concrete differences expected next week
  - Cast tool issues: Analysis shows it's a "dumb tool" that flags potential issues without confirming they exist in actual packages. Considering replacement. Will bring up in Monday meeting after giving Ravi heads-up. Security team now has 3 custom apps built (with Claude) to display data from other open source tools.
  - **Big upcoming work:** OSS branch merge back to develop - will need dedicated PR review time. Thousands of lines of changes, but reviewed incrementally in OSS branch first. Critical for release before July 4th deadline.
- **Team Standard:**
  - Matt Turner's domain ownership page needs eyeballs and feedback
  - Team catalog needs to be filled out
  - JIRA sandbox project created for team project testing
  - Planning to shift travel to Monday-Wednesday to align with office schedules (was Tuesday-Thursday for Palantir)
  - Added link to Turner's page in team standard setup

**Michael:**
- **Native JIRA Spaces Timeline:** 
  - Target: ASAP for creation, Q3 start for transition
  - Some teams like SSO already have boards but need to become full JIRA spaces
  - Need to nail down: template characteristics, statuses, workflow, custom fields
  - Question: What custom fields and workflows should be baseline?
  - Plan: Work with Christine (knows all Jira configs) to set up streamlined bare minimum template, then review together next week
  - Aaron suggested JIRA training for teams on how to manage boards/configure
  - **DevOps dependency:** Still tied to DevOps for merge/build/deploy. They rely on Jira workflow state transitions and CM tickets. Aaron participating in their KT process with Bhavna - will coordinate automation needs.
  - **Team-based vs Company-managed:** Not decided yet. Need to test how Jira Plans works with team-based boards. Can get 30min with Atlassian team if answer isn't obvious.
- **DR Follow-up:**
  - Yesterday's DR discussion was useful
  - Will need more DR epics based on decisions (e.g., transparency to other services)
  - Means changing internal endpoints in API Gateway during failover
  - SSO needs transparency for all users (internal + external)
  - Good to discover difficult pieces now during practice
- **Team Metrics Focus:**
  - Attending sprint reviews, driving teams toward autonomous operation
  - Focusing on data-driven metrics, especially **commit frequency** (not a DORA metric but leads to deploy-often habit)

**Ramesh:**
- **CJ Metrics Mandate:**
  - CJ visited, asked about team metrics. Currently only collecting at pod level, not individual team level (except IPA). CJ not happy.
  - Concern: Blended pod-level metrics can hide slow teams behind high performers
  - **New requirement:** All Hyderabad engineering teams meet weekly to share metrics and learnings. Spin-wheel picks 2-3 teams to present in 30min session. Goal: Improve as a company over time.
  - Each manager chooses their own relevant metrics (e.g., QA manager focuses on test effectiveness, defect escape ratio vs deploy frequency)
  - **Marten's concern:** Too burdensome given current state. Should only do this when metrics are automated and practically free to collect. Currently significant manual effort. Will raise with Curtis and CJ.
  - Ramesh starting with standard list (from Shift team JQLs), but acknowledged:
    - Requires ongoing maintenance
    - Not comparable between teams without clean team boundaries
    - Numbers can become incomparable over time if queries are tweaked
  - **Aaron's suggestion:** Leverage Jira's built-in reporting tabs (Development, Security, Deployment) which collect time-to-resolution, cycle time, PR timelines, deployment frequency - but require instrumentation setup. Will create plan in next 2 weeks.
  - **Key blocker:** Need each team to have their own JIRA space first for well-defined boundaries and comparable metrics.
- **Automation QA Extension Request:**
  - Happiest Minds automation QA contractors rolling off end of June
  - Haven't completed test script migration for orders and invoices yet
  - PBOB estimates 3 more months needed
  - Request: Extend 4-5 automation engineers for another quarter to support Prashanth's team
  - **Concern raised:** These are UI test migrations (legacy Protractor to new framework). Daniel and Marten acknowledged over-reliance on UI tests. Will discuss separately to evaluate if this is the right path.

**Daniel:**
- Nothing that can't be handled in Slack
- Thanked for coordinating next week's office booking and Top Golf event

#### Key Decisions / Action Items:
- [ ] Marten: Follow-up meeting with CJ on architecture questions
- [ ] Marten: Monday call with Veritas about Kick Drum engagement
- [ ] Marten: Raise metrics burden concerns with Curtis and CJ
- [ ] Aaron: Review Matt Turner's domain ownership page
- [ ] Aaron: Create plan for Jira instrumentation for automated metrics (2 weeks)
- [ ] Michael + Christine: Set up baseline JIRA space template for review
- [ ] Aaron: JIRA training for teams on board management
- [ ] Aaron: Coordinate with Bhavna on DevOps automation for new team spaces
- [ ] Teams: Fill out team catalog
- [ ] Ramesh + Marten: Separate discussion on UI test migration investment
- [ ] All: Test JIRA sandbox project and provide feedback 