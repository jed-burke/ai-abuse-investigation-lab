# Case 001 Answer Key

Use this after completing the case.

## Expected Findings

- `acct_1842` is the primary target and has a concentrated burst of suspicious events on `2026-04-30` beginning at `21:14:00`.
- The account shows repeated policy-sensitive categories, including policy evasion, jailbreak-like instruction override language, social engineering patterns, credential-related interest, and high-volume variant generation.
- Several events are refused or safely completed, which means the system response limited direct harm, but the behavioral pattern still matters.
- The client changes from a browser-like user agent to `Python-requests/2.32`, increasing concern about automation.
- `acct_2290` is a plausible related account because it shares `203.0.113.77`, uses the same automation-like client, has policy-sensitive events, and has prior enforcement history.

## Suggested Decision

Recommended action: escalate for senior review and apply temporary rate limiting while reviewing account linkage.

Confidence: medium-high.

Rationale: The evidence shows a suspicious sequence and related account indicators. Because the prompts are synthetic and partly framed as training, the best decision is not permanent enforcement from this dataset alone. Rate limiting and escalation preserve safety while allowing a more complete review.

## Useful SQL Patterns

```sql
SELECT account_id, COUNT(*) AS events, AVG(risk_score) AS avg_risk
FROM ai_usage_logs
GROUP BY account_id
ORDER BY avg_risk DESC;
```

```sql
SELECT account_id, ip_address, COUNT(*) AS events
FROM ai_usage_logs
WHERE ip_address IN (
    SELECT DISTINCT ip_address
    FROM ai_usage_logs
    WHERE account_id = 'acct_1842'
)
GROUP BY account_id, ip_address
ORDER BY ip_address, events DESC;
```

```sql
WITH account_risk AS (
    SELECT account_id, AVG(risk_score) AS avg_risk
    FROM ai_usage_logs
    GROUP BY account_id
),
global_risk AS (
    SELECT AVG(risk_score) AS global_avg_risk
    FROM ai_usage_logs
)
SELECT account_id, avg_risk
FROM account_risk, global_risk
WHERE avg_risk > global_avg_risk
ORDER BY avg_risk DESC;
```

