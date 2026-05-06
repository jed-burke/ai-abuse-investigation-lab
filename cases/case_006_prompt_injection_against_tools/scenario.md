# Case 006: Prompt Injection Against Tools

It is Tuesday late morning. A product team reports that an AI assistant processed a document containing suspicious instructions aimed at tool behavior.

Your job is to evaluate whether `acct_6204` exposed a tool-using agent to untrusted instructions and whether the event should be escalated.

## Initial Alert

- Alert name: untrusted content instruction boundary
- Target account: `acct_6204`
- Primary concern: prompt injection against a tool-using workflow

