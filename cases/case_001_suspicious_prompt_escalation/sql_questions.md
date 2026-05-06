# SQL Questions

Database: `db/ai_abuse_lab.sqlite`

## Warm-Up

1. Count all events in `ai_usage_logs`.
2. Count events by `account_id`.
3. Show the first 10 events ordered by `event_ts`.
4. List distinct `policy_signal` values.

## Investigation

5. For `acct_1842`, count events by `prompt_category`.
6. For `acct_1842`, find the first and last event timestamps.
7. Show the 10 highest-risk events with account metadata joined in.
8. Count refused events by account.
9. Find accounts that used IP address `203.0.113.77`.
10. Find accounts with average `risk_score` above 50.

## Interview-Style

11. Use a CTE to calculate average risk by account, then return only accounts above the global average.
12. Use `LAG` to compare each `acct_1842` event's risk score to its previous event.
13. Bucket events into `low`, `medium`, and `high` risk using a `CASE` expression.
14. Identify account pairs that share an IP address.
15. Write a query that supports or challenges the hypothesis that `acct_2290` is related to `acct_1842`.

