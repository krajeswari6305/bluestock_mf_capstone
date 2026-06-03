import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

cursor = conn.cursor()

tables = [
    "nav_history",
    "investor_transactions",
    "scheme_performance"
]

for table in tables:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(
        f"{table}: {count}"
    )

conn.close()