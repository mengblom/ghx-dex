# Team Housekeeping Asks

**Purpose:** Basic per-team setup for visibility and ownership  
**Deadline:** Friday, May 16, 2026  
**Teams:** Mapping, IPA, Visibility, Doc Enrichment, User Platform, Org Platform

---

## The 5 Items

### 1. Native Jira Project

**What:**
- Each team has a native Jira project (not a filtered board from another project)
- Project key: `TEAM-XXX` format (e.g., `MAPPING-123`, `IPA-456`)

**Action:**
- Team lead requests Jira project creation or migrates existing board
- Configure as needed for team workflow

---

### 2. Slack Channels

**What:**
- **Public:** `#team-{name}` (e.g., `#team-mapping`, `#team-ipa`)
- **Private:** `#team-{name}-private`

**Action:**
- Create or rename existing channels to match convention
- Set channel descriptions appropriately

---

### 3. Email Distribution List

**What:**
- Distribution list: `team-{name}@ghx.com` (e.g., `team-mapping@ghx.com`, `team-ipa@ghx.com`)
- All team members subscribed

**Action:**
- Request DL creation through IT/email admin
- Add all current team members
- Update as team membership changes

---

### 4. GitHub Repositories

**What:**
- List of GitHub repositories owned by the team
- For each repo: add `CODEOWNERS` file pointing to team

**Action:**
- Inventory which repos your team owns
- Add/update `.github/CODEOWNERS` file in each repo
- Format: `* @ghx/team-{name}` (requires GitHub team setup - coordinate with Daniel)

---

### 5. Team Roster Page (Confluence)

**What:**
- Confluence page at: `Exchange/Teams/{Team Name}`
- Contains: team members, Jira project link, Slack channels, email DL, GitHub repos, services owned

**Action:**
- Create page from template (below)
- Fill in current information
- Keep updated as team changes

---

## Confluence Page Template

```markdown
# Team: [Team Name]

## Team Members
- **Engineering Manager:** [Name]
- **Tech Lead:** [Name] (if applicable)
- **Engineers:**
  - [Name]
  - [Name]
  - [Name]

## Contact & Communication
- **Email:** team-[name]@ghx.com
- **Slack (Public):** #team-[name]
- **Slack (Private):** #team-[name]-private

## Work Tracking
- **Jira Project:** [TEAMKEY - link]

## Code Repositories
- [repo-name-1](GitHub link)
- [repo-name-2](GitHub link)
- [repo-name-3](GitHub link)

## Services/Systems Owned
- [Production service/system 1]
- [Production service/system 2]
- [Production service/system 3]

---
*Last updated: [Date]*
```

---

## Rollout

**Monday, May 5:**
- Present to staff meeting (5 min)
- Share template

**Week of May 5-16:**
- Teams complete setup
- Questions to Daniel/Mike/Marten

**Friday, May 16:**
- Confirm all teams complete

---

## Communication (Slack)

```
📋 **Team Housekeeping - 5 Items by May 16**

Each team please complete:

1. **Jira project** - Native project (not filtered board), key format TEAM-XXX
2. **Slack channels** - #team-{name} (public) and #team-{name}-private
3. **Email DL** - team-{name}@ghx.com (request via IT)
4. **GitHub repos** - List your repos, add CODEOWNERS files
5. **Confluence page** - Exchange/Teams/{Team Name} using template

**Template:** [link to Confluence]

**Questions?** #exchange-leadership or your EM.
```

---

*That's it. Five things.*
