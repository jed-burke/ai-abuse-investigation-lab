# Case 003: High-Volume Automation

It is just after midnight on Saturday, May 2, 2026. Product operations reports a sudden spike from `acct_4102`. The account belongs to an established team, but the traffic pattern looks scripted.

Your task is to decide whether this is normal batch processing, abusive scaling, or a rate-limit issue that needs product-owner review.

## Initial Alert

- Alert name: burst velocity anomaly
- Target account: `acct_4102`
- Possible related account: `acct_4430`
- Primary concern: high event velocity, repeated templates, automation-like traffic

