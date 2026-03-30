import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    region TEXT,
    revenue INTEGER,
    date TEXT
)
""")

sample_data = [
    ("A", "North", 1000, "2024-01-01"),
    ("B", "South", 1500, "2024-02-01"),
    ("A", "North", 2000, "2024-03-01"),
    ("C", "West", 1200, "2024-04-01")
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", sample_data)

conn.commit()
conn.close()