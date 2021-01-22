from tkinter import *
from tkinter import ttk

import sqlite3


root = Tk()
root.title('Inventory')
root.geometry('400x400')

# Functions for buttons


def nextItem():
    conn = sqlite3.connect('inventory_book.db')
    c = conn.cursor()
    sql = """
            INSERT INTO
            inventory (barcode, name, cost, quantity) 
            VALUES (:barcode, ?, ?, ?)"""


    val = (barcodeE.get(), nameE.get(), costE.get(), quantityE.get())

    c.execute(sql, val)

    conn.commit()
    conn.close()

    barcodeE.delete(0, END)
    nameE.delete(0, END)
    costE.delete(0, END)
    quantityE.delete(0, END)


def viewInven():
    newtop = Toplevel()
    newtop.geometry('625x400')
    mainframe = Frame(newtop)

    mainframe.pack(fill=BOTH, expand=1, pady=10)
    mycanvas = Canvas(mainframe)
    mycanvas.pack(side= LEFT, fill=BOTH, expand=1)
    # myscrollbar = ttk.Scrollbar(mainframe, orient= VERTICAL, command= mycanvas.yview)
    # myscrollbar.pack(side= RIGHT,  fill = Y)
    # mycanvas.configure(yscrollcommand=myscrollbar.set)
    # mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')) )

    # secondframe = Frame(mycanvas)
    # mycanvas.create_window((0,0), window= secondframe, anchor = "n")

    conn = sqlite3.connect('inventory_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM inventory")
    records = c.fetchall()

    # for i in range(len(records)):
    #     Label(secondframe, text=records[i][0]).grid(row=i, column=0)
    #     Label(secondframe, text=records[i][1]).grid(row=i, column=1)
    #     Label(secondframe, text='$' + str(records[i][2])).grid(row=i, column=2)
    #     Label(secondframe, text=records[i][3]).grid(row=i, column=3)
    #     Label(secondframe, text=records[i][4]).grid(row=i, column=4)

    conn.commit()
    conn.close()

    # Placement of Treeview in canvas

    myTree = ttk.Treeview(mycanvas, height=15)

    # Declaring columns in the tree

    myTree['columns'] = ('barcode', 'name', 'cost', 'quantity', 'oid')

    # Determining column sizes and positions

    myTree.column('#0', width=0, stretch=0)
    myTree.column('name', anchor=W, width=240)
    myTree.column('barcode', anchor=W, width=140)
    myTree.column('cost', anchor=E, width=70)
    myTree.column('quantity', anchor=E, width=70)
    myTree.column('oid', anchor=E, width=70)

    myTree.heading('#0', text='')
    myTree.heading('barcode', text='Barcode', anchor=W)
    myTree.heading('name', text='Name', anchor=W)
    myTree.heading('cost', text='Cost', anchor=W)
    myTree.heading('quantity', text='Quantity', anchor=W)
    myTree.heading('oid', text='ID', anchor=W)

    for i in range(len(records)):
        myTree.insert(parent='', index='end', iid=i, text='', values=(records[i][0], records[i][1], records[i][2], records[i][3], records[i][4]))

    style = ttk.Style()

    style.theme_use('default')

    myTree.pack(pady= 10, padx=10)


def removeItem():
    global deleteE
    conn = sqlite3.connect('inventory_book.db')
    c = conn.cursor()
    sql = "DELETE from inventory WHERE oid= " + deleteE.get()
    c.execute(sql)

    conn.commit()
    conn.close()

    deleteE.delete(0, END)



def deleteIven():
    newtop2 = Toplevel()
    newtop2.geometry('400x400')

    # Objects
    global deleteE
    deletel = Label(newtop2, text="Delete ID")
    deleteE = Entry(newtop2, width= 17, borderwidth= 3)
    delbutton = Button(newtop2, text= 'Delete Item', padx= 20, pady= 5,  command= removeItem)


    # Place Objects
    deletel.grid(row= 0, column= 0)
    deleteE.grid(row=0, column= 1)
    delbutton.grid(row=1, column= 1)

    return

# Creating new Table

conn = sqlite3.connect('inventory_book.db')

c = conn.cursor()


c.execute(""" CREATE TABLE IF NOT EXISTS inventory (
        barcode text,
        name text,
        cost integer,
        quantity integer
        )""")



# Creating Labels

barcodel = Label(root, text= "Barcode")
namel = Label(root, text= 'Name')
costl = Label(root, text= 'Cost ')
quantityl = Label(root, text= 'Quantity')

# Creating Entry

barcodeE = Entry(root, width= 17, borderwidth= 3)
nameE = Entry(root, width= 17, borderwidth= 3)
costE = Entry(root, width= 17, borderwidth= 3)
quantityE = Entry(root, width= 17, borderwidth= 3)

#Creating Buttons

nexti = Button(root, text= 'Next Item', padx = 20, pady= 5, command= nextItem)
viewi = Button(root, text= 'View Inventory', padx = 20, pady= 5, command= viewInven)
removei = Button(root, text= 'Remove Item', padx = 20, pady= 5, command= deleteIven)

# Object Placement

barcodel.grid(row= 0, column= 0)
barcodeE.grid(row=0, column= 1)

namel.grid(row= 1, column= 0)
nameE.grid(row=1, column= 1)

costl.grid(row= 2, column= 0)
costE.grid(row= 2, column= 1)

quantityl.grid(row= 3, column= 0)
quantityE.grid(row= 3, column= 1)

nexti.grid(row= 4, column =0)
viewi.grid(row= 4, column =1)
removei.grid(row= 4, column =2)

conn.commit()
conn.close()

root.mainloop()
