import sqlite3


conn = sqlite3.connect("example.db")

c = conn.cursor()

name = input("名前を入力してください")
age = int(input("年齢を入力してください"))
department = input("所属部署を入力してください")

c.execute("INSERT INTO employees (name, age, department) VALUES (?,?,?)", (name, age, department))

conn.commit()

conn.close()
