1. Tracking Engine Decoupling
	1. Used to be part of Prcoessing Engine
	2. Incidents?
	3. Future: Separate out TE events to a dedicated Event Bus
	4. Moved to separate repo
	5. Separate Bamboo pipeline
2. Notifications Engine Decoupling
	1. Used to be part pf Processing Engine
	2. Incidents?
	3. Moved to separate repo
	4. Separate Bamboo pipeline
3. Atlas Migration (ongoing)
4. ES migraton (ongoing)
5. Aurora (MySql) (ongoing)
6. Decoupling login/auth/auth from TPM
	1. The rest of User data still needs to be done
7. Decoupling SSO from Audit DB
8. IO Guarrantee
	1. SQS backup for Native Comms
8. Mondo DB Cluster Separation 
	1. Mailbox
	2. Statistics
	3. SSO data
	4. ???
9. Redis cache for User Business Rules
	1. TPM contains business rules
	2. User Business Rules still needs to move to a Mongo DB (in progress)
10. Mongo Optimizations
	1. Daniel?
11. Regcenter 2.0 (ongoing)
	1. Decouple RC BFF
	2. Core UI Upgrade
12. Doc IO API Split
	1. But the data is still in TPM
13. Canary (Document Prediction)
	1. Kenisis stream of Exchange Event Bus events
14. 