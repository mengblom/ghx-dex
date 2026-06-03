In response to a weekly incident report sent out by DevOps, the following email chain unfolded:

### Email Chain ###

**From:** CJ Singh <csingh@ghx.com>  
**Date:** Friday, May 22, 2026 at 21:01  
**To:** Marten Engblom <mengblom@ghx.com>  
**Subject:** Re: Weekly Incident Update  
  

Thanks. 

  

I just sent you an email and requested an hour next Fri, I would appreciate if you could reserve 10 mins and talk about the standards being put in place and the metrics you track to measure the effectiveness of your team.

  

Regards,

---

**From:** Marten Engblom <mengblom@ghx.com>  
**Date:** Saturday, May 23, 2026 at 2:53 AM  
**To:** Ramesh Rangavithal Donnipadu <rdonnipadu@ghx.com>; CJ Singh <csingh@ghx.com>  
**Cc:** Curtis Nielsen <cnielsen@ghx.com>; Arshad Mahammad <amahammad@ghx.com>; Pete Ferguson <pferguson@ghx.com>  
**Subject:** Re: Weekly Incident Update  
  

Hello CJ,

  

Like Ramesh mentioned, the only metric we have right now are incidents (i.e. BROKEN tickets), and that is not very comprehensive since it doesn’t capture things that doesn’t become an incident. We have the concept of CFR and MTTR in the KMP Dashboard, but it is not wired up correctly, and/or requires Jira ticket labeling discipline that has not been implemented. 

  

As part of getting the Automation teams to operate autonomously, we are in the process of cleaning up a number of things that will make this and other metrics (DORA etc.) much easier to collect straight from Jira and Github:

- Each team will have their own native Jira project (as opposed to just a board pulling tickets from all over the place)
    
- Infrastructure, code repos, and deployment pipelines with clear ownership metadata
    
- Better Jira discipline around using Bug issue type for bugs/defects introduced into PROD via code change/deployment.
    

  

Work in progress document: [Exchange Team Standards.docx](https://ghx365-my.sharepoint.com/:w:/r/personal/mengblom_ghx_com/Documents/Exchange%20Team%20Standards.docx?d=wa931c15d071c4037b6716ba24fc9eb42&csf=1&web=1&e=3Y0ttT&xsdata=MDV8MDJ8bWVuZ2Jsb21AZ2h4LmNvbXwxNTQ1MGRjNGQyZDI0MmU2MjMzOTA4ZGViODc3OWE1ZnwzYzIwODhmZTM5Njk0ODczYWMwZGRjOWYxMjI4NjZiOXwwfDB8NjM5MTUxMDIwOTkzMjQ4NjA2fFVua25vd258VFdGcGJHWnNiM2Q4ZXlKRmJYQjBlVTFoY0draU9uUnlkV1VzSWxZaU9pSXdMakF1TURBd01DSXNJbEFpT2lKWGFXNHpNaUlzSWtGT0lqb2lUV0ZwYkNJc0lsZFVJam95ZlE9PXwwfHx8&sdata=MTU0YTZrWkN3cUVublBuNEJBaEh0WHpZMjhrMnpLbUlQQjIrdEFwdVpjMD0%3d)​ We are putting these changes in place before the start of Q3.


Marten

 --- 

  

![__tpx__](https://tracy.srv.wisestamp.com/px/wsid/4xLGYP11YmPZ.png)

**From:** Ramesh Rangavithal Donnipadu <rdonnipadu@ghx.com>  
**Date:** Thursday, May 21, 2026 at 22:22  
**To:** CJ Singh <csingh@ghx.com>; Marten Engblom <mengblom@ghx.com>  
**Cc:** Curtis Nielsen <cnielsen@ghx.com>; Arshad Mahammad <amahammad@ghx.com>; Pete Ferguson <pferguson@ghx.com>  
**Subject:** Re: Weekly Incident Update  
  

CJ,

  

Currently, I track “Number of incidents” and “Defects Caused by Deployments" as a measure of quality and effectiveness of our quality checks. I would also recommend tracking the total number of defects reported in production, not just those that escalate into incidents.

  

Separately, Swastik and I have already started reviewing all the metrics currently in use across teams and will come back with recommendations where we see gaps or opportunities to improve.

  

Regards

Ramesh

  

**From:** CJ Singh <csingh@ghx.com>  
**Date:** Friday, May 22, 2026 at 7:29 AM  
**To:** Marten Engblom <mengblom@ghx.com>; Ramesh Rangavithal Donnipadu <rdonnipadu@ghx.com>  
**Cc:** Curtis Nielsen <cnielsen@ghx.com>; Arshad Mahammad <amahammad@ghx.com>; Pete Ferguson <pferguson@ghx.com>  
**Subject:** Re: Weekly Incident Update  
  

Marten, regarding "Monday, May 11 – Exchange Emailed PDFs failed to Process – Sev 3”**.** Can you pls share the metrics you have in place for Exchange w.r.t to a) software defects and b) first-pass yield i.e. bugs that leak testing

  

Ramesh, given you are in this time zone and we had a discussion on metrics, adding you for visibility and also curious if you have something in place for your teams.