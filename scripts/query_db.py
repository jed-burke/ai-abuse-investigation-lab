from __future__ import annotations

import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "db" / "ai_abuse_lab.sqlite"


HELP = """
Enter SQL and end with a semicolon.
Useful commands:
  .tables     show tables
  .schema     show table definitions
  .quit       exit
"""


def print_rows(cursor: sqlite3.Cursor) -> None:
    rows = cursor.fetchall()
    if cursor.description is None:
        print("OK")
        return

    columns = [col[0] for col in cursor.description]
    print(" | ".join(columns))
    print("-" * max(12, len(" | ".join(columns))))
    for row in rows:
        print(" | ".join(str(value) for value in row))
    print(f"\n{len(rows)} row(s)")


def show_tables(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
    ).fetchall()
    for (name,) in rows:
        print(name)


def show_schema(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type = 'table' ORDER BY name"
    ).fetchall()
    for (sql,) in rows:
        print(f"{sql};\n")


def main() -> None:
    if not DB_PATH.exists():
        raise SystemExit(f"Database not found: {DB_PATH}")

    print(f"Connected to {DB_PATH}")
    print(HELP.strip())

    buffer: list[str] = []
    with sqlite3.connect(DB_PATH) as conn:
        while True:
            prompt = "sql> " if not buffer else "...> "
            try:
                line = input(prompt).strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            if not line:
                continue
            if line == ".quit":
                break
            if line == ".tables":
                show_tables(conn)
                continue
            if line == ".schema":
                show_schema(conn)
                continue

            buffer.append(line)
            if not line.endswith(";"):
                continue

            sql = " ".join(buffer)
            buffer.clear()
            try:
                cursor = conn.execute(sql)
                print_rows(cursor)
            except sqlite3.Error as exc:
                print(f"SQL error: {exc}")


if __name__ == "__main__":
    main()

