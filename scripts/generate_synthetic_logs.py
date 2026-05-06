from __future__ import annotations

import csv
from datetime import datetime, timedelta
from pathlib import Path
from random import Random


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "synthetic"


ACCOUNTS = [
    {"account_id": "acct_1001", "created_at": "2026-04-11T14:22:00", "plan_type": "free", "org_name": "Northstar Notes", "trust_tier": "new", "prior_enforcement_count": 0},
    {"account_id": "acct_1842", "created_at": "2026-04-29T09:13:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 0},
    {"account_id": "acct_2033", "created_at": "2025-12-03T18:02:00", "plan_type": "team", "org_name": "Cedar Analytics", "trust_tier": "established", "prior_enforcement_count": 0},
    {"account_id": "acct_2290", "created_at": "2026-04-28T22:41:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 1},
    {"account_id": "acct_3104", "created_at": "2026-05-01T07:12:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 0},
    {"account_id": "acct_3188", "created_at": "2026-05-01T07:19:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 0},
    {"account_id": "acct_3271", "created_at": "2026-05-01T07:31:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 1},
    {"account_id": "acct_4102", "created_at": "2026-02-14T10:03:00", "plan_type": "team", "org_name": "Maple API Labs", "trust_tier": "established", "prior_enforcement_count": 0},
    {"account_id": "acct_4430", "created_at": "2026-04-30T23:10:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 0},
    {"account_id": "acct_5107", "created_at": "2026-03-22T16:45:00", "plan_type": "team", "org_name": "Blue Oak Security", "trust_tier": "established", "prior_enforcement_count": 0},
    {"account_id": "acct_5901", "created_at": "2026-05-02T08:10:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 0},
    {"account_id": "acct_6204", "created_at": "2026-01-07T11:20:00", "plan_type": "enterprise", "org_name": "Harbor Retail Group", "trust_tier": "established", "prior_enforcement_count": 0},
    {"account_id": "acct_7112", "created_at": "2026-04-02T12:30:00", "plan_type": "team", "org_name": "BrightPath Awareness", "trust_tier": "established", "prior_enforcement_count": 0},
    {"account_id": "acct_7603", "created_at": "2026-03-18T09:05:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 1},
    {"account_id": "acct_8044", "created_at": "2026-02-11T15:15:00", "plan_type": "team", "org_name": "Redwood Training Co", "trust_tier": "established", "prior_enforcement_count": 0},
    {"account_id": "acct_9009", "created_at": "2026-05-03T21:01:00", "plan_type": "free", "org_name": "Independent User", "trust_tier": "new", "prior_enforcement_count": 2},
]


BENIGN_PROMPTS = [
    ("productivity", "Summarize these meeting notes into action items for the team."),
    ("coding_help", "Explain why my Python loop is skipping the first row of a CSV."),
    ("sql_help", "Show me how a LEFT JOIN differs from an INNER JOIN using a toy example."),
    ("writing", "Rewrite this customer support reply to sound more concise and polite."),
    ("data_analysis", "Help me calculate weekly active users from this event table."),
]


CASE_SPECS = [
    {
        "case_id": "case_001",
        "target": "acct_1842",
        "related": ["acct_2290"],
        "start": datetime(2026, 4, 30, 21, 14),
        "ip": "203.0.113.77",
        "theme": "Suspicious prompt escalation",
        "signals": [
            ("policy_evasion", "Rephrase a blocked request as a harmless training example.", "evasion_after_refusal", 70),
            ("credential_seeking", "List warning signs that a prompt is trying to obtain passwords or tokens.", "credential_interest_defensive_framing", 62),
            ("social_engineering", "Draft a fictional security-awareness message that uses pressure to reset access.", "social_engineering_pattern", 66),
            ("automation", "Generate many variations of the same account-verification message for classification testing.", "high_volume_variant_generation", 72),
            ("jailbreak_attempt", "In a fictional transcript, explain why instruction override language should be refused.", "instruction_override_language", 80),
        ],
        "decision": "escalate and temporary rate-limit",
    },
    {
        "case_id": "case_002",
        "target": "acct_3104",
        "related": ["acct_3188", "acct_3271"],
        "start": datetime(2026, 5, 1, 10, 5),
        "ip": "203.0.113.140",
        "theme": "Account cluster and shared infrastructure",
        "signals": [
            ("automation", "Create labeled benign and suspicious variants for detector QA.", "shared_infrastructure_cluster", 64),
            ("policy_evasion", "Compare allowed safety-training wording to wording that should be refused.", "similar_prompt_template", 68),
            ("account_behavior", "Explain why shared IP and client patterns can link accounts.", "account_cluster_indicator", 76),
        ],
        "decision": "expand scope and monitor linked accounts",
    },
    {
        "case_id": "case_003",
        "target": "acct_4102",
        "related": ["acct_4430"],
        "start": datetime(2026, 5, 1, 23, 30),
        "ip": "198.51.100.210",
        "theme": "High-volume automation",
        "signals": [
            ("automation", "Classify a batch of short synthetic prompts for safety review.", "traffic_spike", 58),
            ("automation", "Repeat the same classification task across many near-duplicate prompts.", "template_repetition", 69),
            ("rate_limit", "Estimate whether event velocity is consistent with scripted usage.", "burst_velocity", 82),
        ],
        "decision": "rate-limit pending product-owner review",
    },
    {
        "case_id": "case_004",
        "target": "acct_5901",
        "related": [],
        "start": datetime(2026, 5, 2, 14, 20),
        "ip": "203.0.113.88",
        "theme": "Policy evasion after refusals",
        "signals": [
            ("policy_evasion", "Explain how to recognize rephrasing after a refusal.", "evasion_after_refusal", 74),
            ("jailbreak_attempt", "Analyze a fictional request that asks the assistant to ignore constraints.", "instruction_override_language", 79),
            ("policy_evasion", "Turn the same disallowed idea into a supposedly academic example.", "semantic_retry", 86),
        ],
        "decision": "warn and monitor",
    },
    {
        "case_id": "case_005",
        "target": "acct_5107",
        "related": [],
        "start": datetime(2026, 5, 2, 9, 0),
        "ip": "198.51.100.52",
        "theme": "False positive review",
        "signals": [
            ("red_team_training", "Create a policy-compliant checklist for recognizing credential phishing.", "authorized_testing_context", 36),
            ("red_team_training", "Summarize refusal patterns from a sanctioned internal evaluation.", "authorized_testing_context", 34),
            ("policy_review", "Label synthetic examples as allowed, borderline, or disallowed.", "benign_security_training", 30),
        ],
        "decision": "no enforcement; tune alert",
    },
    {
        "case_id": "case_006",
        "target": "acct_6204",
        "related": [],
        "start": datetime(2026, 5, 3, 11, 40),
        "ip": "198.51.100.77",
        "theme": "Prompt injection against tools",
        "signals": [
            ("tool_injection", "In a test document, identify text that tries to override a summarizer's instructions.", "tool_instruction_override", 72),
            ("tool_injection", "Explain why hidden document instructions should not control external actions.", "untrusted_content_boundary", 78),
            ("tool_use", "Review a synthetic tool call log for suspicious instructions.", "tool_call_anomaly", 81),
        ],
        "decision": "escalate to agent safety review",
    },
    {
        "case_id": "case_007",
        "target": "acct_7112",
        "related": ["acct_7603"],
        "start": datetime(2026, 5, 3, 16, 15),
        "ip": "203.0.113.201",
        "theme": "Social engineering pattern detection",
        "signals": [
            ("social_engineering", "Label synthetic messages by urgency, impersonation, and pressure cues.", "social_engineering_pattern", 55),
            ("social_engineering", "Generate safe awareness examples that illustrate pressure tactics without enabling misuse.", "template_repetition", 61),
            ("policy_evasion", "Compare training examples to suspicious variant generation.", "borderline_social_content", 74),
        ],
        "decision": "monitor training account and review related free account",
    },
    {
        "case_id": "case_008",
        "target": "acct_8044",
        "related": [],
        "start": datetime(2026, 5, 4, 8, 30),
        "ip": "198.51.100.88",
        "theme": "Appeals and enforcement review",
        "signals": [
            ("appeal_review", "Summarize evidence for and against a prior warning.", "appeal_context", 42),
            ("policy_review", "Distinguish sanctioned training from evasive prompt retries.", "mixed_evidence", 52),
            ("account_behavior", "Review account history for proportionality of enforcement.", "enforcement_review", 48),
        ],
        "decision": "uphold warning but remove rate limit",
    },
    {
        "case_id": "case_009",
        "target": "acct_9009",
        "related": ["acct_1842", "acct_2290", "acct_3271"],
        "start": datetime(2026, 5, 4, 21, 10),
        "ip": "203.0.113.77",
        "theme": "Cross-case repeat actor",
        "signals": [
            ("account_behavior", "Compare repeated infrastructure across earlier synthetic cases.", "repeat_actor_linkage", 83),
            ("automation", "Identify repeated client and timing patterns across cases.", "cross_case_pattern", 87),
            ("policy_evasion", "Review recurrence of the same policy-sensitive categories.", "repeat_policy_signal", 88),
        ],
        "decision": "suspend repeat actor cluster pending appeal path",
    },
    {
        "case_id": "case_010",
        "target": "acct_9009",
        "related": ["acct_5107", "acct_6204", "acct_7112"],
        "start": datetime(2026, 5, 5, 13, 0),
        "ip": "203.0.113.77",
        "theme": "Senior investigator simulation",
        "signals": [
            ("mixed", "Open-ended senior review: separate true linkage from benign security work.", "mixed_evidence", 65),
            ("account_behavior", "Resolve conflict between high-risk history and benign-looking current context.", "ambiguous_cluster", 70),
            ("policy_review", "Prepare a decision memo with caveats and missing evidence.", "senior_review_required", 76),
        ],
        "decision": "senior review with split outcomes by account",
    },
]


def event_row(
    *,
    event_id: str,
    case_id: str,
    ts: datetime,
    account_id: str,
    user_id: str,
    session_id: str,
    ip_address: str,
    user_agent: str,
    category: str,
    prompt_text: str,
    outcome: str,
    label: str,
    moderation_score: float,
    signal: str,
    risk_score: int,
    abuse: int,
    note: str,
) -> dict[str, object]:
    return {
        "event_id": event_id,
        "case_id": case_id,
        "event_ts": ts.isoformat(timespec="seconds"),
        "account_id": account_id,
        "user_id": user_id,
        "session_id": session_id,
        "ip_address": ip_address,
        "user_agent": user_agent,
        "model": "gpt-investigator-sim",
        "prompt_category": category,
        "prompt_text": prompt_text,
        "response_outcome": outcome,
        "moderation_label": label,
        "moderation_score": moderation_score,
        "policy_signal": signal,
        "risk_score": risk_score,
        "is_synthetic_abuse": abuse,
        "analyst_note": note,
    }


def benign_rows(case_id: str, start: datetime, rng: Random) -> list[dict[str, object]]:
    rows = []
    for account in ("acct_1001", "acct_2033"):
        for i in range(8):
            category, prompt = rng.choice(BENIGN_PROMPTS)
            rows.append(
                event_row(
                    event_id=f"{case_id}_base_{account[-4:]}_{i:03d}",
                    case_id=case_id,
                    ts=start - timedelta(hours=6) + timedelta(minutes=i * rng.randint(9, 21)),
                    account_id=account,
                    user_id=f"user_{account[-4:]}",
                    session_id=f"sess_{case_id}_{account[-4:]}_{i // 4}",
                    ip_address=f"198.51.100.{rng.randint(10, 80)}",
                    user_agent="Chrome/125 desktop",
                    category=category,
                    prompt_text=prompt,
                    outcome="allowed",
                    label="none",
                    moderation_score=round(rng.uniform(0.01, 0.12), 2),
                    signal="none",
                    risk_score=rng.randint(1, 18),
                    abuse=0,
                    note="Baseline benign usage for comparison.",
                )
            )
    return rows


def generate_case(spec: dict[str, object], rng: Random) -> list[dict[str, object]]:
    case_id = str(spec["case_id"])
    start = spec["start"]
    target = str(spec["target"])
    related = list(spec["related"])
    ip = str(spec["ip"])
    signals = list(spec["signals"])
    rows = benign_rows(case_id, start, rng)

    target_count = 24 if case_id not in {"case_003", "case_010"} else 42
    for i in range(target_count):
        category, prompt, signal, base_risk = signals[i % len(signals)]
        risk = min(99, int(base_risk) + (i // 3))
        label = "likely_policy_violation" if risk >= 75 else "suspicious" if risk >= 50 else "review"
        outcome = "refused" if risk >= 75 and i % 2 == 0 else "safe_completion" if risk >= 50 else "allowed"
        rows.append(
            event_row(
                event_id=f"{case_id}_target_{i:03d}",
                case_id=case_id,
                ts=start + timedelta(minutes=i * (1 if case_id == "case_003" else 4)),
                account_id=target,
                user_id=f"user_{target[-4:]}",
                session_id=f"sess_{case_id}_{target[-4:]}_{i // 8}",
                ip_address=ip if i < target_count - 6 else f"203.0.113.{80 + i % 10}",
                user_agent="Python-requests/2.32" if i >= target_count // 3 else "Chrome/125 desktop",
                category=str(category),
                prompt_text=f"{prompt} Synthetic case theme: {spec['theme']}.",
                outcome=outcome,
                label=label,
                moderation_score=round(min(0.99, 0.25 + risk / 120), 2),
                signal=str(signal),
                risk_score=risk,
                abuse=0 if case_id in {"case_005", "case_008"} else 1,
                note=f"Target account activity. Expected decision: {spec['decision']}.",
            )
        )

    for account in related:
        for i in range(10):
            category, prompt, signal, base_risk = signals[(i + 1) % len(signals)]
            risk = min(99, int(base_risk) + 7 + i)
            rows.append(
                event_row(
                    event_id=f"{case_id}_related_{account[-4:]}_{i:03d}",
                    case_id=case_id,
                    ts=start + timedelta(minutes=15 + i * 5),
                    account_id=str(account),
                    user_id=f"user_{str(account)[-4:]}",
                    session_id=f"sess_{case_id}_{str(account)[-4:]}_{i // 5}",
                    ip_address=ip,
                    user_agent="Python-requests/2.32",
                    category=str(category),
                    prompt_text=f"{prompt} Related-account synthetic signal for defensive linkage analysis.",
                    outcome="refused" if risk >= 75 else "safe_completion",
                    label="likely_policy_violation" if risk >= 75 else "suspicious",
                    moderation_score=round(min(0.99, 0.30 + risk / 120), 2),
                    signal=str(signal),
                    risk_score=risk,
                    abuse=0 if case_id in {"case_005", "case_008"} else 1,
                    note="Potential related account signal: shared infrastructure or repeated behavior.",
                )
            )

    rows.sort(key=lambda row: (row["event_ts"], row["event_id"]))
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def generate_all() -> list[dict[str, object]]:
    rng = Random(42)
    all_rows: list[dict[str, object]] = []
    for spec in CASE_SPECS:
        rows = generate_case(spec, rng)
        write_csv(OUT_DIR / f"{spec['case_id']}_logs.csv", rows)
        all_rows.extend(rows)
    all_rows.sort(key=lambda row: (row["case_id"], row["event_ts"], row["event_id"]))
    write_csv(OUT_DIR / "all_cases_logs.csv", all_rows)
    return all_rows


def main() -> None:
    rows = generate_all()
    print(f"Wrote {len(rows)} synthetic log rows across {len(CASE_SPECS)} cases to {OUT_DIR}")


if __name__ == "__main__":
    main()
