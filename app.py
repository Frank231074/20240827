import sqlite3


conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute(
    """
CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGERNOT NOT NULL,
department TEXT NOT NULL
)
"""
)


print("テーブルを作成しました")
