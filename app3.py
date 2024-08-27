import sqlite3


conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute("SELECT age, department FROM employees WHERE name = 'John'")

rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
