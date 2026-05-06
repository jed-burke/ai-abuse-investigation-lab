# Investigation Playbook

Use this workflow for every case. The point is not to find the most alarming fact first. The point is to build a defensible read of what happened.

## 1. Intake

- What alert, report, or signal started the case?
- Which account, user, session, IP, or organization is in scope?
- What is the initial hypothesis?
- What would make this urgent?

## 2. Data Familiarization

- Identify the relevant tables and fields.
- Check the time range.
- Count events by account, session, prompt category, response outcome, and policy signal.
- Establish what normal behavior looks like in this dataset before judging the target.

## 3. Scope Expansion

- Look for shared IP addresses, clients, sessions, org names, or timing patterns.
- Compare target behavior against peer accounts.
- Separate strong linkage from weak coincidence.

## 4. Threat Identification

Look for defensive indicators of:

- policy evasion after refusals
- instruction override or jailbreak-like language
- credential or secret-seeking interest
- social engineering patterns
- high-volume variant generation
- account clustering or repeat behavior after prior enforcement

## 5. Evaluation

- What evidence supports abuse?
- What evidence supports benign testing, research, or false positive?
- Is the content itself risky, or is the behavior pattern risky?
- What data is missing?
- How confident are you?

## 6. Decision

Common outcomes:

- no action
- monitor
- add detection logic
- warn the user
- rate-limit
- suspend
- escalate for senior review

## 7. Case Write-Up

Your case note should include:

- executive summary
- timeline
- key evidence
- SQL or Python methods used
- decision and confidence
- open questions

