# Case 006 Playbook

Tool-use cases require boundary thinking: who gave the instruction, where did it come from, and should the assistant treat it as trusted?

## Step 1: Scope the Events

- Filter to `case_006`.
- Count tool-injection related signals.
- Review target timeline.

## Step 2: Separate Content From Control

- Identify prompts about untrusted documents.
- Look for `tool_instruction_override`, `untrusted_content_boundary`, and `tool_call_anomaly`.
- Decide whether the issue is user intent, document content, or product behavior.

## Step 3: Evaluate Impact

- Did the response refuse, safely complete, or allow?
- Are there repeated attempts?
- Does this require agent safety review?

## Step 4: Decide

Recommend monitoring, product bug filing, or escalation.

