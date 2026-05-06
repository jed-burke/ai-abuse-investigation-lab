# Python Tasks

Starter file: `scripts/case_001_python_starter.py`

## Warm-Up

1. Load `data/synthetic/case_001_logs.csv`.
2. Count events by account.
3. Calculate average risk by account.
4. Print the top five highest-risk events.

## Investigation

5. Build a timeline for `acct_1842`.
6. Count policy signals for `acct_1842`.
7. Find all accounts that share an IP with `acct_1842`.
8. Create a simple account risk summary with:
   - event count
   - average risk score
   - max risk score
   - refused event count
   - number of distinct policy signals

## Interview-Style

9. Write a function `group_by(rows, key)` that returns a dictionary of grouped rows.
10. Write a function `average(values)` that handles empty lists safely.
11. Write a function `related_accounts(rows, target_account_id)` that returns accounts sharing IPs with the target.
12. Write a function `risk_bucket(score)` that returns `low`, `medium`, or `high`.
13. Write a short text summary for the top-risk account using computed evidence.

