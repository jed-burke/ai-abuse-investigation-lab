# AI Abuse Investigation Lab

A defensive learning lab for practicing AI abuse investigations with synthetic logs, SQL, and Python.

This project is designed to feel like a day in the life of an AI abuse investigator. Each case gives you a scenario, synthetic product logs, SQL questions, Python tasks, and a case report template. The goal is to learn how to explore data, identify suspicious behavior, evaluate evidence, and make a defensible decision.

## What You Will Practice

- AI abuse tactics and defensive detection concepts
- SQL joins, aggregation, CTEs, window functions, and time-based analysis
- Python data parsing, scoring, summaries, and simple anomaly detection
- Investigation workflows: triage, scoping, evidence review, evaluation, and decisioning
- Familiarity with AI product logs, even though all data here is synthetic

## Quick Start

From this folder:

Windows:

```powershell
py .\scripts\generate_synthetic_logs.py
py .\scripts\build_database.py
```

macOS/Linux:

```bash
python3 scripts/generate_synthetic_logs.py
python3 scripts/build_database.py
```

This creates:

- `data/synthetic/case_001_logs.csv` through `data/synthetic/case_010_logs.csv`
- `data/synthetic/all_cases_logs.csv`
- `db/ai_abuse_lab.sqlite`

Then start with:

1. `cases/case_001_suspicious_prompt_escalation/scenario.md`
2. `cases/case_001_suspicious_prompt_escalation/playbook.md`
3. `cases/case_001_suspicious_prompt_escalation/sql_questions.md`
4. `cases/case_001_suspicious_prompt_escalation/python_tasks.md`
5. `cases/case_001_suspicious_prompt_escalation/report_template.md`

Use `answer_key.md` only after you have worked the case.

To see the full roadmap, open `docs/case_progression.md`.

## Case List

- Case 001: Suspicious Prompt Escalation
- Case 002: Account Cluster and Shared Infrastructure
- Case 003: High-Volume Automation
- Case 004: Policy Evasion After Refusals
- Case 005: False Positive Review
- Case 006: Prompt Injection Against Tools
- Case 007: Social Engineering Pattern Detection
- Case 008: Appeals and Enforcement Review
- Case 009: Cross-Case Repeat Actor
- Case 010: Senior Investigator Simulation

## Case Modes

- Guided mode: follow the playbook step by step.
- Interview mode: answer the SQL and Python prompts without hints.
- Investigator mode: open the scenario, inspect the data, and produce a case report.

## Safety Boundary

This lab teaches recognition, investigation, and mitigation. It does not teach how to successfully abuse AI systems. Synthetic examples are intentionally framed as defensive evidence signals and are written to avoid operational instructions.
