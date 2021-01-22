import sqlite3
from tkinter import *
conn = sqlite3.connect('/Users/josh/PycharmProjects/POS/inventory_book.db')

c = conn.cursor()

c.execute("SELECT *, oid FROM inventory")
records = c.fetchall()


# root = Tk()
# root.title('Testing')
# root.geometry('1000x1000')

# for i in range(len(records)):
#     Label(root, text= records[i][0]).grid(row=i, column=0)
#     Label(root, text=records[i][1]).grid(row=i, column=1)
#     Label(root, text=records[i][2]).grid(row=i, column=2)
#     Label(root, text=records[i][3]).grid(row=i, column=3)
#     Label(root, text=records[i][4]).grid(row=i, column=4)

sumit = 0

for record in records:
    item = 0
    item = record[2] * record[3]
    sumit += item
    #print(sumit, record[4])

print(sumit)

conn.commit()
conn.close()

#root.mainloop()