# Confluence Rovo Search Prompts - Thinktiv/Kickdrum Prep

**Purpose:** Find existing documentation for Platform Architecture and Platform-Enabling Services sessions

---

## Comprehensive Search Prompt (Use First)

```
I need to prepare for two consultant deep-dive sessions about GHX Exchange platform. Please search for documentation covering:

1. Exchange Platform Architecture:
   - Logical architecture diagrams showing Exchange components and services
   - Technology stack documentation (languages, frameworks, databases, AWS services)
   - Integration patterns between Exchange and other GHX products
   - Document processing pipeline architecture
   - Monolith vs microservices architecture decisions

2. Identity, SSO, and Authentication:
   - Identity provider configuration (Okta or other IDP)
   - SSO implementation (SAML, OAuth, OIDC)
   - User authentication flows for Exchange and Visibility portal
   - Authorization model (RBAC, claims-based)
   - User and Organization data architecture
   - Multi-tenancy and customer data isolation

3. UI/UX Shared Components:
   - Design system or component library documentation
   - Shared UI components used across Exchange or GHX products
   - Frontend technology stack (Angular, React, Vue)
   - UI governance and maintenance ownership
   - Accessibility standards and compliance

4. Intelligent Process Automation (IPA):
   - IPA technical architecture and capabilities
   - Document digitization pipeline (OCR, classification)
   - Integration with Exchange document processing
   - IPA services and APIs exposed to other teams
   - Automation rates and metrics

Please prioritize architecture diagrams, technical design docs, and API documentation.
```

---

## Targeted Search Prompts (If Comprehensive Search Doesn't Work)

### Search 1: Exchange Architecture
```
Find documentation about Exchange platform architecture including:
- Architecture diagrams showing system components
- Technology stack and deployment architecture
- Integration patterns with other GHX products
- Mapping team Contivo and Smooks documentation
- Document processing pipeline architecture
```

### Search 2: Identity & Authentication
```
Find documentation about identity management and authentication including:
- SSO and identity provider setup (Okta)
- User authentication flows
- Authorization and RBAC implementation
- User Platform and Organization Platform architecture
- Multi-tenancy and data isolation patterns
```

### Search 3: UI Components
```
Find documentation about frontend and UI architecture including:
- Shared component library or design system
- Visibility portal architecture (Angular/Tomcat/SpringBoot)
- Reusable UI components across Exchange
- Frontend technology standards
- UI governance and ownership
```

### Search 4: IPA Capabilities
```
Find documentation about Intelligent Process Automation including:
- IPA technical architecture
- Document digitization capabilities (GFax, Invoice)
- OCR and classification technology
- IPA services and APIs
- Integration with Exchange processing
```

### Search 5: Service Integration Patterns
```
Find documentation about service consumption and integration including:
- API gateway or service mesh architecture
- Service discovery and routing patterns
- Shared service consumption model
- Integration patterns between Exchange teams (Mapping, IPA, Visibility, Doc Enrichment)
```

---

## Alternative Keywords (If Searches Return Nothing)

Try searching for these specific terms:
- "Exchange" + "architecture"
- "Contivo" or "Smooks" (mapping tools)
- "Visibility portal" + "architecture"
- "IPA" or "Intelligent Process Automation"
- "User Platform" or "Organization Platform"
- "SSO" or "Okta" + "Exchange"
- "authentication" + "authorization"
- "design system" or "component library"
- "API documentation" + "Exchange"
- "deployment architecture" + "Exchange"
- "MongoDB" + "Exchange" (database architecture)
- "SFTP" + "document processing"

---

## Follow-Up Questions After Initial Search

If Rovo returns results, ask these follow-up questions to refine:

```
From the results above, which documents contain:
1. High-level architecture diagrams suitable for executive presentation?
2. Technical implementation details for [specific topic]?
3. The most recent/current state documentation (not outdated)?
4. API specifications or service contracts?
5. Known limitations or technical debt in [specific area]?
```

---

## What to Look For in Results

**Priority 1 - Must Find:**
- Architecture diagrams (visual representations)
- SSO/authentication flow diagrams
- IPA technical architecture docs
- Service integration patterns

**Priority 2 - Nice to Have:**
- API documentation
- Technology stack decisions and ADRs (Architecture Decision Records)
- Performance and scalability docs
- Known issues or technical debt registers

**Priority 3 - Background Context:**
- Historical context on architecture decisions
- Migration plans or modernization roadmaps
- Team ownership documentation

---

## Export Instructions

Once you find relevant docs:
1. **Export/download PDFs** of key architecture diagrams
2. **Bookmark** pages you'll reference during the session
3. **Note which docs are outdated** - confirm with Daniel/Mike if still accurate
4. **List gaps** - topics where documentation doesn't exist or is unclear

---

## What to Do If Documentation is Sparse

If Rovo doesn't find much:
1. Note the gaps in your prep session with Daniel and Mike
2. Ask them if docs exist elsewhere (SharePoint, Whiteboard, Google Drive)
3. Focus prep session on getting verbal walkthroughs of missing topics
4. Consider this a signal that documentation needs to be created post-meeting

Remember Curtis's guidance: "Provide if you have it, don't create artifacts" - you're searching for existing docs, not creating new ones.
