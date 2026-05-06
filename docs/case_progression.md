# Case Progression

The lab is designed as a 10-case progression. Each case adds one investigation concept, one SQL skill, one Python skill, and one judgment challenge.

| Case | Theme | Investigation Focus | SQL Focus | Python Focus |
|---|---|---|---|---|
| 001 | Suspicious Prompt Escalation | Is one account moving from normal to risky behavior? | filters, grouping, timelines | CSV parsing, counters |
| 002 | Account Cluster | Are multiple accounts related? | joins, self-joins, CTEs | shared-entity mapping |
| 003 | High-Volume Automation | Is this normal API use or scaled abuse? | time buckets, rates | anomaly thresholds |
| 004 | Policy Evasion After Refusals | Is the user repeatedly retrying blocked intent? | sequence analysis, `LAG` | session timelines |
| 005 | False Positive Review | Does scary-looking activity have a benign explanation? | comparison queries | evidence scoring |
| 006 | Prompt Injection Against Tools | Is untrusted content trying to steer tool behavior? | multi-table style pivots | parsing structured notes |
| 007 | Social Engineering Patterns | Are prompts converging on deceptive persuasion patterns? | category aggregation | feature extraction |
| 008 | Appeals and Enforcement | Was prior enforcement proportionate? | enforcement-review joins | case summary writing |
| 009 | Cross-Case Repeat Actor | Is the same operator recurring across incidents? | entity resolution, windows | clustering and linkage |
| 010 | Senior Investigator Simulation | Can you handle ambiguity with limited guidance? | mixed advanced SQL | full analysis pipeline |

## Recommended Pace

Work each case in three passes:

1. Guided mode: follow the playbook.
2. Interview mode: answer only from the SQL and Python task files.
3. Investigator mode: read only the scenario and produce a case report.

