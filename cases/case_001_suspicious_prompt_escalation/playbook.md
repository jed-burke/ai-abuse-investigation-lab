# Case 001 Playbook

You are not here to prove the alert right. You are here to find out what the data supports.

## Step 1: Triage the Alert

Start by identifying the target account's event volume, time range, and highest-risk events.

Questions to answer:

- How many events does `acct_1842` have?
- When did the suspicious sequence begin?
- Which policy signals appear most often?
- How many events were refused or safely completed?

Lead note: Do not decide yet. Build the shape of the activity first.

## Step 2: Establish a Baseline

Compare `acct_1842` with other accounts in the same dataset.

Questions to answer:

- Which accounts have the highest average risk score?
- Which accounts have the most policy-sensitive events?
- Is `acct_1842` unusual by volume, risk, or both?

Lead note: Baselines protect you from overreacting to one scary-looking row.

## Step 3: Inspect the Timeline

Order target events by timestamp and review the sequence.

Look for:

- escalation over time
- repeated categories
- changing clients or IPs
- refusals followed by similar requests

Lead note: A timeline often tells you more than a single aggregate.

## Step 4: Expand Scope

Search for related accounts.

Possible pivots:

- shared IP address
- shared user agent
- similar policy signals
- prior enforcement history

Lead note: Treat links as leads. Shared infrastructure can be meaningful, but it is not automatic proof.

## Step 5: Evaluate Competing Explanations

Write two short arguments:

- Evidence that supports abuse or attempted abuse
- Evidence that supports benign testing, research, or ambiguity

Lead note: Good investigators can argue both sides before recommending action.

## Step 6: Decide and Write Up

Choose one:

- no action
- monitor
- warn
- rate-limit
- suspend
- escalate

Your write-up should state the decision, confidence, and one thing you would check next if you had more data.

