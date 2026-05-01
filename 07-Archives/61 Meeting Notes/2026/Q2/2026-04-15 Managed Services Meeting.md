---
tags:
  - Managed-Services
  - Engineering
  - India
  - meeting
content_type: meeting_note
meeting_type: staff_meeting
destination_category: 60-69 Archive
kb_insights: false
---
- Quick demo of Managed Services Portal
	- Orders
	- Pricing
- 
- Future Roadmap
	- Exchange Managed Services (EMS)
		- This was "promised" to be finished by December 2026
		- Rammi is concerned that this deadline will not be met
- Technical
	- Managed Services Portal is in its own repo
	- Dependency on BT/BD database
	- Also dependencies on APIs in CCX, CoreX, Reg Center, ...
	- Claude Code adoption is held back by Github migration (Bitbucket MCPs are poor etc.)
	- 90% test coverage by automated Tandoori - currently being migrated to Playwright
		- Talked to the team about the test pyramid, the team owns quality, and it is up to them to decide how - i.e. if they want to decrease automated UI test coverage, that is up to them