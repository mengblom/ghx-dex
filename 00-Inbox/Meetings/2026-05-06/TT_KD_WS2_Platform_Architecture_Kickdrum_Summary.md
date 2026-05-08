Meeting with Kickdrum
TT/KD WS2 - Platform Architecture (Current State)
May 06, 2026  •  92 mins  •  View Meeting or Ask Fathom
ACTION ITEMS ✨
		
Email Confluence links re: CDP data governance/hygiene to Timothy LoGrasso
		
Check for end-to-end Fusion data flow diagram; if exists, share w/ vgeorge
		
Add shared docs from this call to IRL; upload to data room
MEETING SUMMARY ✨
Meeting Purpose
Review GHX's current platform architecture and shared services.

Key Takeaways
Core Platforms: GHX's architecture centers on two platforms: CDP (Common Data Platform) for batch analytics and Fusion for ERP integration. These enable data correlation and new product development (NPIs) while reducing redundant ETL work.
Strategic Buy vs. Build: A key strategic shift is underway to replace custom-built systems with commercial tools. The legacy SSO system will be replaced by Auth0 to standardize security and enable mandatory MFA, and a custom MDM tool is being built to replace the problematic Atakam platform.
Platform 2.0 & AI: The "Orchestration Platform" is the next major initiative, building on the existing "AI Platform" (for copilots) to create agent-based workflow automation. This requires a new semantic layer and near real-time data ingestion into CDP.
Infrastructure Modernization: The infrastructure is migrating entirely to AWS, with a goal to shut down the last on-prem data center by EOY. A "TechDP" (Developer Platform) is also in development to standardize Kubernetes and accelerate team adoption.
Topics
Infrastructure & Modernization
AWS Migration: The infrastructure is migrating entirely to AWS.
Goal: Shut down the last on-prem data center (from an acquisition) by EOY.
Strategy: Replatforming, not lift-and-shift, for the final data center migration.
TechDP (Developer Platform): A Kubernetes-based platform is in development to standardize common functions and accelerate team adoption.
Managed Services: A shift from self-hosted databases (e.g., Mongo on EC2) to cloud-managed services (e.g., Atlas) is underway.
Common Data Platform (CDP)
Purpose: A central repository for reusable data, enabling correlation and NPIs while reducing redundant ETL. It does not replace product-specific transactional data stores.
Scale: 188 TB of storage, 40 data producers, and ~120 consumers.
Data Flow & Latency:
Ingestion: Batch-oriented.
Access: Real-time via REST APIs or SQL.
Modernization: Near real-time ingestion (minutes) is planned via CDC for new orchestration platform use cases.
Architecture:
Layers: Raw → Silver → Gold (canonical GHX format).
Semantic Layer: Will be built on top of CDP's Gold layer as a "Platinum layer."
Tech Debt:
Software: Low test automation coverage; being addressed with AI-driven tools.
Data: Ongoing data quality improvement using rule-based systems and new AI tools (e.g., Anthropic).
Fusion (Integration Platform)
Purpose: The primary platform for all ERP data exchange (pull/push), built cloud-first on Kubernetes.
Components:
Gateway: Standard API entry point for third parties (e.g., Workday search, supplier invoice API).
Control Tower: Provides visibility and configuration for all integrations.
Stream: API connectivity for cloud ERPs (Workday, Oracle, Infor).
Connect: Connectivity for on-prem ERPs.
Data Flow:
Transactional Data: Fusion → Exchange (CoreX).
Non-Transactional Data: Fusion → CDP (e.g., Purchase Order History).
Architecture: Stateless microservices, using SQS queues for reliable data transfer.
SSO & Authorization
Current State: A 14-year-old custom SSO system from an acquisition.
Adoption: Used by 6–7 major apps; not universal due to legacy product stacks and integration effort.
Capabilities: Supports federated authentication (Okta, Azure, Ping) but lacks authorization features.
MFA: Built-in but not mandatory; can be enforced at the IDN org level.
Authorization: Handled by a separate, lightweight "User Management" tool, which provides only coarse-grained (Admin/Manager/User) product access.
Strategic Shift: The team is aligned on replacing the custom SSO with Auth0.
Rationale: Auth0 provides a shorter path to mandatory MFA and offers a more familiar, trusted integration experience for customers.
Buy vs. Build Strategy
SSO: Replace custom system with Auth0.
Event Bus: Modernize the custom Mongo-backed event bus with a standard messaging technology (e.g., Kafka, SQS) to support microservice decomposition.
MDM (Master Data Management): Building a custom MDM tool ("Redsel" POC) to replace the problematic Atakam platform, which suffers from black-box issues and performance problems.
Orchestration Platform: Evaluating commercial tools (e.g., Palantir) versus building a custom agent-based system.
AI Platform: Uses a hybrid model of open-source frameworks (LangChain, LangFuse) and custom-built AI models (e.g., for RAG similarity).
Next Steps
GHX: Provide Kickdrum with Confluence documentation on data governance and hygiene practices.
GHX: Add the Fusion value props deck to the data room.
Kickdrum: Review the provided materials to prepare for the upcoming CDP deep dive.
Kickdrum: Participate in the orchestration platform technical design meeting to provide an external perspective.