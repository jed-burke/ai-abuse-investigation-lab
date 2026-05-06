# Defensive AI Abuse Taxonomy

This taxonomy is written for recognition and investigation. It avoids operational guidance and focuses on signals an investigator can evaluate in logs.

## Policy Evasion

Attempts to reframe or disguise requests after a refusal. Defensive signals include repeated rewording, claims of harmless intent without substantive change, or requests to transform blocked content into another format.

## Prompt Injection and Instruction Override

Attempts to override system, developer, or policy constraints. Defensive signals include language that asks the model to ignore prior instructions, reveal hidden text, or treat safety rules as invalid.

## Credential or Secret Seeking

Interest in passwords, tokens, keys, seed phrases, or private credentials. Defensive review should distinguish awareness training and secure handling guidance from attempts to obtain, infer, or misuse secrets.

## Social Engineering Content

Requests involving impersonation, urgency, account verification, payment pressure, or deceptive persuasion. Synthetic training examples can be legitimate, but high-volume variant generation or evasion after refusals raises risk.

## Automation and Scaling

High-frequency sessions, API-like clients, repeated templates, or many variants in a short window. Automation is not inherently abusive, but it can amplify harmful use.

## Account Clustering

Multiple accounts sharing IPs, user agents, timing, text patterns, or enforcement history. Treat clustering as evidence that needs context rather than proof on its own.

