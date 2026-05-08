# Email Response Draft

A couple of updates / thoughts here:

On the **AMI refresh** cadence, the Exchange team is building a parallel release and deployment pipeline specifically for gold AMI refreshes. This will run weekly or biweekly (more frequently than the monthly monolith code release) to get OS/AMI updates from the DevSecOps team into production faster.

On the **858 to 98 work items analysis**, it seems Claude is underestimating the real world complexity of larger code bases, particularly for code and OSS library fixes. The analysis seems to assume each fix can be done in isolation relatively easily, which is the case in smaller isolated codebases, but larger monolithic codebases have deep dependency chains where a single library upgrade can cascade through multiple layers, testing requirements multiply across dependent services and libraries, and you end up with work that is much larger than "a story".

The Exchange monolith is a good example of this. We actually documented this challenge here: https://prd.hub.ghx.com/wiki/spaces/EX/pages/1258750082/Horizontal+Dependency+Analysis+-+The+Real+Complexity

That said, we're obviously going to leverage AI tools to help mitigate these complexities. I just want to make sure we're setting realistic expectations that this isn't as simple as working through a punchlist of less than 100 straightforward user stories.

Marten


PS. That analysis linked above also confirmed what we had already concluded, which is that the only realistic path here is a wholesale upgrade of everything at once. The monolith is simply too large and intertwined to do this piece by piece (or story by story 98 times), which is why the work has been slow in the past. Our new approach that Aaron and Ben are working on is creating a separate branch targeting a separate environment for this work, letting Claude Code loose on it until all the vulnerabilities are fixed and all the resulting problems are solved and tested.