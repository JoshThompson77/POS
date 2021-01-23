import sqlite3
from tkinter import *
import xlwt as xw

conn = sqlite3.connect('/Volumes/HD/PycharmProjects/POS/inventory_book.db ')

c = conn.cursor()

c.execute("SELECT *, oid FROM inventory")
records = c.fetchall()

wb = xw.Workbook() 

sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(0,1, "name")
sheet1.write(0,2, "cost")
sheet1.write(0,3, "quantity")

counter = 1


for i in range(len(records)):
	sheet1.write(counter, 1, record[i][1])
	sheet1.write(counter, 1, record[i][2])
	sheet1.write(counter, 1, record[i][3])

wb.save('inventory.xls')

conn.commit()
conn.close()

#root.mainloop()