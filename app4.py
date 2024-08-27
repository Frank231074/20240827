import sqlite3


conn = sqlite3.connect("example.db")

c = conn.cursor()

name = "Bob"
old_age = 22

new_age = int(input(f"{name}さんの新しい年齢を入力してください"))

c.execute("UPDATE students SET age =? WHERE name =? AND age =?", (new_age, name, old_age))
conn.commit()

print(f"{name}さんの年齢を更新しました")

conn.close()
