from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "synthetic" / "case_001_logs.csv"


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = load_rows()

    by_account = Counter(row["account_id"] for row in rows)
    avg_risk: dict[str, list[int]] = defaultdict(list)
    for row in rows:
        avg_risk[row["account_id"]].append(int(row["risk_score"]))

    print("Events by account")
    for account_id, count in by_account.most_common():
        scores = avg_risk[account_id]
        print(f"{account_id}: events={count}, avg_risk={sum(scores) / len(scores):.1f}")


if __name__ == "__main__":
    main()

