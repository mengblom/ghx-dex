The background to this meeting was the conversation with the Visibility team last week, where they had some complaints about the Happiest Minds contractors:
- The HM engineers are operating on their own to a certain extent:
	- not attending standups or other sprint rituals etc.
	- logging bugs in a separate spreadsheet, as opposed to Jira
	- are not very forthcoming with information in general
- The completion of the automated UI tests is the only thing that is preventing us from releasing otherwise completed modules:
	- Notifications
	- Transactions

# Notes from the meeting#
- Multiple modules completed - held up by Tandoori to Playwright conversion
	- 5 UI Automation engineers fully engaged with the Visibility team
- The Happiest Minds test engineers are not joining the standups
	- HM leadership contends they don't know why, they claim this is the norm on all other teams
- Feedback from HM is that the some modules are done, including the tests, just waiting for the user manuals to get updated
	- Modules that are ready:
		- Notifications
		- Transactions
	- My opinion is that we should release these to production - this is the reason we have a toggle between the old and new UI. We should be able to release to production, keep the toggle hidden (except for internally to the engineering team etc.)
	- On the same toke - why are we doing UAT in the INT environment - we should be able to do it in prod