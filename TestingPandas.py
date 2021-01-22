import sqlite3

conn = sqlite3.connect('inventory_book.db')

c = conn.cursor()

c.execute("SELECT *, oid FROM inventory")
records = c.fetchall()

sumit = 0

for record in records:
    item = 0
    item = record[2] * record[3]
    sumit += item

print(sumit)

conn.commit()
conn.close()