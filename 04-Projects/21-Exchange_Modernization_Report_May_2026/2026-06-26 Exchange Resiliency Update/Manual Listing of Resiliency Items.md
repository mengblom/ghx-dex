### Items ###
1. **[Board Deck]**: 2025.02 Exchange_Board Deck_Feb.2025.pdf
	1. Page 2 - Exchange Resiliency Executive Summary
		1. DB Stabilization: Audit DB and BT BD 
		2. Release rigor and change management
		3. Performance Environment 
	2. Page 10
		1. DB Stabilization - Atlas Migration
	3. Page 14
		1. Feature Flagging
	4. Page 15
		1. DB and Query Optimization
		2. Visibility Improvement for internal/external tooling
		3. IBR Decoupling
		4. Database syncing, and database optimization
	5. Page 17
		1. Performance Environment
	6. Page 20
		1. Exchange Platform Modularization
			1. SSO Decouple
				1. Separating authentication from AuditDB & MySQL TPM.
		2. User Data Decouple
			1. Migrate IBR data
		3. IO Guarantee
		4. Tracking Engine Decouple
		5. TPM Query Optimization
	7. Page 25
		1. Industry BDP (aka ICS aka Industry Continuity Assure)
	8. Page 28
		1. Disaster Recovery
2. **[Exchange Plan]**: Exchange_Plan_Latest.pptx  
	1. Slide 3
		1. DB spikes
		2. Performance Testing
		3. Alerting and Monitoring
		4. Incident Management
	2. Slide 7
		1. SLA Rebates
	3. Slide 10
		1. AuditDB Improvements
	4. Slide 14-16: Phase 1 Roadmap
		1. Audit
			1. DB Optimization
			2. Data Cleanup
			3. DB Decoupling 
		2. TPM
			1. Registration Query Fixes
			2. MyExchange Query Fixes
			3. Move IBR Data
			4. Replace TPM API
		3. Decoupling
			1. Hash Map Load Balancing
			2. Dead Listener Refactor
			3. SSO Decoupling
			4. Feed Processor Refactor
		4. Processing Engine Issues
			1. Decouple Dead Listener
		5. Testing Maturity
			1. New Performance Environment
			2. Fix Gaps in Monitoring
			3. TPM Database Upgrade
		6. Human Error
			1. CoreX permission audit
			2. Multi-person go-live audit
		7. Communication
			1. Canary Program
		8. Customer Experience
			1. Customer empathy training
	5. Slide 19 - Phase 2 Roadmap
		1. Database
			1. ES to Managed Service
			2. ES depressurization
		2. Decouple Critical Components
			1. Tracking from Event Bus
			2. Tracking refactor
			3. Data Poller overhaul
			4. MEX APIs to Replace Direct DB Calls
			5. Decouple Doc Processing Phase 2
		3. Scheduling Enhancements
			1. Processing Engine Start/Stop Enhancement
			2. Universal Scheduler Migration
			3. Event Bus Next Generation
		4. Database Managed Services
			1. Mongo DB to Atlas
			2. ES to Managed Services
		5. DR
			1. DR Setup
		6. Customer Experience
			1. Communication
				1. ...
	6. Slide 30 (and also Slide 23 - 27) Incident Remdiations
		1. ...
3. **[Product Health]**: 2026 Product Health Portfolio - Copy.pptx (slides 41-49)
	1. Slide 42 - 47 Recommendation Column