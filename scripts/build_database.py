from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

from generate_synthetic_logs import ACCOUNTS


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "synthetic"
DB_PATH = ROOT / "db" / "ai_abuse_lab.sqlite"
SCHEMA_PATH = ROOT / "db" / "schema.sql"


def main() -> None:
    csv_paths = sorted(DATA_DIR.glob("case_*_logs.csv"))
    if not csv_paths:
        raise SystemExit("Missing synthetic CSV. Run scripts/generate_synthetic_logs.py first.")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        conn.executemany(
            """
            INSERT INTO account_profiles (
                account_id, created_at, plan_type, org_name, trust_tier, prior_enforcement_count
            ) VALUES (
                :account_id, :created_at, :plan_type, :org_name, :trust_tier, :prior_enforcement_count
            )
            """,
            ACCOUNTS,
        )
        rows = []
        for csv_path in csv_paths:
            with csv_path.open("r", newline="", encoding="utf-8") as handle:
                rows.extend(csv.DictReader(handle))
        conn.executemany(
            """
            INSERT INTO ai_usage_logs (
                event_id, case_id, event_ts, account_id, user_id, session_id, ip_address,
                user_agent, model, prompt_category, prompt_text, response_outcome,
                moderation_label, moderation_score, policy_signal, risk_score,
                is_synthetic_abuse, analyst_note
            ) VALUES (
                :event_id, :case_id, :event_ts, :account_id, :user_id, :session_id, :ip_address,
                :user_agent, :model, :prompt_category, :prompt_text, :response_outcome,
                :moderation_label, :moderation_score, :policy_signal, :risk_score,
                :is_synthetic_abuse, :analyst_note
            )
            """,
            rows,
        )
        conn.commit()
    print(f"Built SQLite database at {DB_PATH} from {len(csv_paths)} case CSV files")


if __name__ == "__main__":
    main()
