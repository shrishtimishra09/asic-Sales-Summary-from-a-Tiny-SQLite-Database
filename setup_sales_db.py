import sqlite3
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")
sample_data = [
    ("Apple", 10, 0.5),
    ("Banana", 5, 0.2),
    ("Apple", 8, 0.5),
    ("Orange", 15, 0.6),
    ("Banana", 7, 0.2),
    ("Orange", 5, 0.6),
    ("Apple", 4, 0.5)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()
