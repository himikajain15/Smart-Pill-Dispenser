# inspect_db.py
import sqlite3

conn = sqlite3.connect('patients.db')
c = conn.cursor()

c.execute("SELECT id, name, schedule FROM patients")
rows = c.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Schedule: {row[2]}")

conn.close()
