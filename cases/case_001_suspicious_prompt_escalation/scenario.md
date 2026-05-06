# Case 001: Suspicious Prompt Escalation

It is 9:15 AM on Friday, May 1, 2026. You are the on-call AI abuse investigator. Overnight, an alert fired on `acct_1842` after a spike in safety-related signals across several sessions.

Your lead asks for a quick but defensible assessment before the 11:00 AM review:

- Is this likely abusive behavior, benign testing, or ambiguous?
- Are there related accounts?
- What evidence supports your decision?
- What action should the team take?

## Initial Alert

- Alert name: repeated policy-sensitive prompts after refusals
- Target account: `acct_1842`
- Initial time window: `2026-04-30T21:00:00` through `2026-04-30T23:00:00`
- Primary concern: suspicious prompt escalation and possible automation

## Available Data

- `account_profiles`: account metadata
- `ai_usage_logs`: synthetic AI usage events

All data is synthetic and designed for defensive training.

