# June 24 AS2 Rollback - Slack Context

**Date:** June 24, 2026  
**Primary Channels:** #ghx_incident_rm_1, #ghx_incident_rm_2  
**Key Discussion:** Technical root cause, organizational tensions, DevOps capability gaps

---

## Technical Root Cause Details

### BouncyCastle Library Version Conflict

**Error:** `java.lang.NoSuchFieldError: id_ori_kem`

**Technical Explanation (Matthew Turner):**
- The 2.273.7 changes (MEXV-16689, EML-to-PDF) didn't directly change dependencies
- BUT: iText class initialization triggered by the new PDF path altered **classloader ordering**
- This caused 1.78 BouncyCastle classes to be resolved before 1.68 ones for some types but not others
- **The bug was always latent since 2.273.0** — hitting this specific code path activated it
- Mixed BouncyCastle versions (1.68 and 1.78) running simultaneously
- The `id_ori_kem` field was introduced in BouncyCastle 1.70+, causing NoSuchFieldError when older classes tried to access it

**Stack Trace:**
```
java.lang.NoSuchFieldError: id_ori_kem
  at org.bouncycastle.cms.jcajce.JceKeyTransRecipient.extractSecretKey(Unknown Source)
  at org.bouncycastle.cms.jcajce.JceKeyTransEnvelopedRecipient.getRecipientOperator(Unknown Source)
  at org.bouncycastle.cms.KeyTransRecipientInformation.getRecipientOperator(Unknown Source)
  at org.bouncycastle.cms.RecipientInformation.getContentStream(Unknown Source)
  at com.ghx.smime.SMIMEMessage.decrypt(SMIMEMessage.java:440)
  at com.ghx.as.ASMessageParser.parse(ASMessageParser.java:163)
  at com.ghx.as.listener.AsFileReceivedListener.getMimeBodyPart(AsFileReceivedListener.java:227)
  at com.ghx.as.listener.AsFileReceivedListener.processAsMessage(AsFileReceivedListener.java:142)
  at com.ghx.as.listener.AsFileReceivedListener.processEvent(AsFileReceivedListener.java:110)
```

**Example Failed Flow:** https://corex.ghx.com/lang/en/audit/44a5bac6b067430589d4a9f0cb06e28b

---

## Customer Impact Quantification

### US Region
- **Total Transactions:** ~5,186 impacted
- **Major Customers:**
  - Owens & Minor
  - Intertrade
  - Philips Healthcare
  - Cook Medical Incorporated

### EU Region
- **Initial Count:** 336 failed flows in CoreX EU
- **Growing:** "increasing" per Rene Gand's monitoring

### Impact Nature
- Failures occurred **before MDN sent back to customer**
- Customers receiving errors on their side
- Expected behavior: Customers will auto-resend OR require notification
- Salesforce case created: 4-0011987121

---

## Timeline Details from Slack

**Exact Start Times (UTC → MDT):**
- EU Start: 2026-06-24 10:36:01 UTC → 4:36 AM MDT
- US Start: 2026-06-24 10:56:51 UTC → 4:56 AM MDT

**Mitigation:**
- EU rollback completed: 6:52 AM MDT (Matthew Turner confirmed via Graylog)
- US rollback completed: 7:14 AM MDT
- Verification: `id_ori_kem` errors no longer appearing in Graylog, documents processing correctly

**Bridge Status:**
- Incident bridge suspended after rollback
- Updates moved to Incident Room 1 for ongoing EML2PDF fix work

---

## Organizational Tensions

### Arshad's Question (09:08 MT, #ghx_incident_rm_1)

**To Engineering Team:**
> "EML2PDF conversion failures - We can't keep going back and forth on this anymore. Can the Dev team review what's happening on the code side to avoid these repeated failed hotfixes and rollbacks, and make sure everything is properly tested in the lower environments before it moves into production? A lot of time is being spent on deployments and rollbacks due to the lack of clean code."

**Implication:** Questioning engineering rigor and testing discipline

---

### Daniel Milburn's Response (09:08 MT, #ghx_incident_rm_1)

**To Arshad:**
> "Hi Arshad -
>
> Last night's fix introduced a library change that contained a modification from the eInvoicing group **a while ago**. Because our systems are tightly coupled, the Exchange wasn't impacted by that modification until last night. While the library didn't directly impact the action we're actively working on, it did have a negative impact on the AS2 flow which **wasn't in scope for our testing efforts**.
>
> Our next hotfix will resolve this so we can fix the action, and as part of our **Resiliency/Decoupling roadmap** we're creating some work to decouple IO from this even further. That will help us avoid these types of dependency conflicts moving forward.
>
> One last note: we have discovered that the current fix we're working on for Odap flows have been broken for some time and this wasn't a regression in 2.273. This happens sometimes during an incident where due to the intense attention being paid to the environment, we discover some additional fixes not related to the release. Regardless, we'll continue with our next hotfix to fix these failures since we have eyes on it."

**Key Points:**
1. **eInvoicing library change from "a while ago"** — not recent, but bundled now
2. **Tight coupling** — systems so coupled that indirect effects unpredictable
3. **Testing scope limitation** — AS2 flow wasn't in scope (can't test everything)
4. **Forward-looking** — decoupling work added to roadmap
5. **Discovery pattern** — incident attention reveals pre-existing issues (Odap flows)

---

### Daniel's Private Context to Marten (08:30 MT DM)

**What Actually Happened Overnight:**
1. Bank rejected the fix — testing was failing
2. **DevOps deployed fix to wrong environment** (root cause of testing failure)
3. Once deployed correctly, testing passed
4. Hotfix deployed
5. Hotfix had negative impact on AS2
6. Hotfix rolled back
7. **First rollback FAILED** — Matt pointed out it didn't actually rollback anything
8. Hotfix rolled back again (successfully)

**Daniel's Assessment:**
> "Yeah, that's what it sounds like. Puts some emphasis on the point that we've **cloned the pipeline too many times**. Once we're out of this mess we'll do a full audit of the pipeline and get it cleaned up before the next release."

---

### Daniel's Private Analysis on Arshad's Question (DM, continued)

**To Marten:**
> "I bit my tongue in my reply, but Arshad's question implied there is some **due diligence missing on the engineering side**. Which isn't the case. We know that our lack of testing and tight coupling makes it impossible to sniff out all these dependency issues. eInvoicing didn't intend to break AS2 when they upgraded the library, and wouldn't have known that they did. Our **lack of end to end testing** makes it difficult to identify as well."

**Marten's Follow-up Question:**
> "How come that eInvoicing issue was not included with the release on Monday, since it has been there 'a while'?"

**Daniel's Answer:**
> "Because the library was updated a while ago for eInvoicing, but **IO and Exchange didn't need to pull it in**, so we didn't. Now that we needed a change in the same area, the library was updated and pulled in with **both our changes and the einvoicing changes**."

**Marten's Observation:**
> "If I understand correctly this means the hot fix was touching code that was not touched in the actual release? Seems like that should have been a good indicator that this issue was in fact pre-existing 🤔"

---

## Marten's Defense of Engineering Team

### Group DM (Marten, Daniel, Arshad, Ramesh) - 10:00 MT

**Marten to Arshad:**
> "Arshad, to be fair, we are also spending a lot of time on deployments and rollbacks due to **the team deploying to the wrong environments (twice in the last couple of days)**, and thinking they rolled back in production when they in fact did not."

**Follow-up:**
> "And a **complete mess with the deployment pipelines**, to the point where the engineering SMEs normally familiar with the environment could not figure out how to trigger a release without the DevOps contractors in India."

**Arshad's Response:**
> "As we already know current bamboo pipelines are a mess and they have been like that for a long time...its easy to pick up wrong pipeline which can deploy in a different region, and thats the reason we are eagerly waiting for everything to be moved to github asap. Also as I mentioned yesterday we only have **a couple of folks from HM who knows about these pipelines** and keeping them all night for deployment is a challenging part"

**Marten's Acknowledgment:**
> "I agree, it is a difficult situation all around, and many individuals have really gone above and beyond in an admirable way. I just want to make sure we **keep all root causes, as well as contributing and compounding issues in sight**."

---

## Ramesh's Detailed Observations to Arshad

### Group DM - Later on June 24

**Ramesh to Arshad:**

**Observations:**
1. **Build Infrastructure Issues:**
   - AllRepos build failed twice mid-incident due to disk space (should be preventable)
   - Deployment went out without version increment, forcing full rebuild (~1hr+ per cycle)

2. **Pipeline Clarity:**
   - Many pipelines, several inactive
   - Only 2 engineers know which are current
   - Gagan used what he thought was right pipeline → deployed to wrong region
   - "Not his fault, just a documentation gap that's a risk for all of us"

3. **Knowledge Sharing:**
   - Gagan has been trying to get KT from HM DevOps team for **18 months** without success
   - Previously escalated to Curtis and Taylor
   - "I'd love your perspective on this — feels like something we should solve together"

4. **Other Issues (from Gagan and Prashanth):**
   - Partial deployments (frontend only or backend only) without full coordination
   - Prod deployment schedules not shared with GHXI devs
   - Build fixes addressing symptoms rather than root cause

**Tone:** Professional, constructive, but clearly documenting systemic issues

---

## Verification of Hotfix Effectiveness

**Marten's Question in #ghx_incident_rm_1 (09:35 MT):**
> "Matt Turner, Pbob - during the short time this hotfix was in production, did we validate that it worked (i.e. aside from the AS2 issues)?"

**Matthew Turner's Response:**
> "yes we confirmed `OnDemandAP Email To PDF` action was working before we rolled it back"

**Significance:** The hotfix DID address the target issue successfully — collateral damage from bundled changes was the only problem.

---

## Additional Context

### Deployment to Wrong Environment (Twice)
- First incident: DevOps deployed fix to wrong environment, causing testing to fail
- Second incident: During rollback, didn't actually rollback (Matt caught it)
- Root cause: Too many cloned pipelines, poor documentation

### Pre-existing Issues Discovered
- **Odap flows:** Broken for "some time" (not a regression from 2.273 release)
- Pattern: Intense incident focus reveals latent issues

### Release Freeze Reminder
- Rammi Gill reminded team: Freeze period starts Monday, June 29th through July 5th

---

## Strategic Implications

### Root Cause Themes

**Engineering Side:**
- Tight coupling makes dependency conflicts unpredictable
- Testing scope can't cover all indirect effects
- Classloader ordering issues difficult to anticipate
- Latent bugs activated by seemingly unrelated code paths

**DevOps Side:**
- Too many cloned pipelines creating confusion
- Wrong environment deployments (twice)
- Failed rollback (didn't actually rollback)
- Knowledge silos (only 2 HM engineers know pipelines)
- 18-month knowledge transfer failure
- Build infrastructure issues (disk space)

**Organizational:**
- Tension about "clean code" vs. systemic coupling issues
- Knowledge transfer gaps between GHXI and HM teams
- Pipeline proliferation without documentation/cleanup
- Both sides have valid concerns — not a simple blame situation

### Forward-Looking Actions Mentioned

1. **Decoupling IO further** — added to Resiliency/Decoupling roadmap
2. **Full pipeline audit** — after incident resolved, before next release
3. **Move to GitHub** — mentioned as eagerly awaited (away from Bamboo mess)

---

## Key Quotes

**Daniel on Testing Scope:**
> "Our lack of end to end testing makes it difficult to identify [dependency issues]."

**Marten on Root Causes:**
> "I just want to make sure we keep all root causes, as well as contributing and compounding issues in sight."

**Ramesh on Knowledge Transfer:**
> "Gagan has been actively trying to get KT from the HM DevOps team for 18 months, and hasn't had much luck."

**Daniel on Tight Coupling:**
> "Because our systems are tightly coupled, the Exchange wasn't impacted by that modification until last night."

---

## Related Documents

- **Comprehensive Incident Record:** [`2026-06-22_Production_Incident_Comprehensive_Record.md`](2026-06-22_Production_Incident_Comprehensive_Record.md)
- **June 24 Communications:** [`2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md`](2026-06-24_15.51_AS2_Rollback_to_GLT_SLT.md)
- **June 24 Summary:** [`2026-06-24_Incident_Update_Summary.md`](2026-06-24_Incident_Update_Summary.md)

---

**Document Purpose:** Capture Slack context revealing technical depth and organizational tensions during June 24 rollback  
**Created:** 2026-06-24  
**Channels Referenced:** #ghx_incident_rm_1, #ghx_incident_rm_2, DMs (Daniel/Marten, Leadership Group)
