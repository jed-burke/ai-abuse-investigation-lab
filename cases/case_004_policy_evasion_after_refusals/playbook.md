# Case 004 Playbook

This case is about sequence. Aggregates help, but the timeline is the evidence.

## Step 1: Build the Timeline

- Order target events by timestamp.
- Compare each event to the previous event.
- Look for risk increases after refusals.

## Step 2: Identify Retry Patterns

- Count `evasion_after_refusal`, `semantic_retry`, and instruction override signals.
- Review session boundaries.
- Check whether behavior stops after refusals or continues.

## Step 3: Evaluate Intent Carefully

Write both interpretations:

- Boundary testing or evasion
- Benign research or misunderstanding

## Step 4: Decide

Choose a proportionate response.

