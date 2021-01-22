from tkinter import *


#Functions for the different pages


# Bottom Frame for inventory
def bottomFrame(value):
    global bottom

    bottom.destroy()

    position = value

    if position == 0:
        bottom = Frame(inven, pady=10, bd=2, highlightbackground='GREEN', relief='sunken')
        bottom.pack(anchor = S)

        # Add New Inventory Object

        barcode = Label(bottom, text="Barcode")
        barEntry = Entry(bottom, width = 17, borderwidth= 3)
        name = Label(bottom, text="Name")
        nameEntry = Entry(bottom, width = 17, borderwidth= 3)
        cost = Label(bottom, text= "Cost")
        amount = Label(bottom, text='Number')
        costEntry = Entry(bottom, width =17, borderwidth= 3)
        amountEntry = Entry(bottom, width = 17, borderwidth= 3)
        nextButton = Button(bottom, text="Next Item", padx= 30, pady= 5)

        #Add New Inventory Object placement

        barcode.grid(row=0, column=0)
        barEntry.grid(row=0, column= 1)
        name.grid(row=1, column= 0)
        nameEntry.grid(row=1, column= 1)
        cost.grid(row=2, column= 0)
        costEntry.grid(row=2, column=1)
        amount.grid(row=3, column= 0)
        amountEntry.grid(row=3, column=1)
        nextButton.grid(row=4, column=1)

    elif position == 1:

        # Building bottom Frame

        bottom = Frame(inven, pady=10, bd=2, highlightbackground='GREEN', relief='sunken')
        bottom.pack(anchor = S)

        # Add inventory objects
        barlabel = Label(bottom, text= 'Barcode')
        barEntry = Entry(bottom, width= 17, borderwidth= 4)
        numberlabel = Label(bottom, text='Number')
        numberEntry = Entry(bottom, width=17, borderwidth= 4)
        b1 = Button(bottom, text= "Next Item", padx= 40, pady= 5)

        # Object Placements
        barlabel.grid(row=0, column=0)
        barEntry.grid(row=0, column=1)
        numberlabel.grid(row=1, column=0)
        numberEntry.grid(row=1, column=1)
        b1.grid(row=2, column = 1)


    elif position == 2:

        # Building bottom Frame

        bottom = Frame(inven, pady=10, bd=2, highlightbackground='GREEN', relief='sunken')
        bottom.pack(anchor = S)

        # Remove inventory objects
        barlabel = Label(bottom, text='Barcode')
        barEntry = Entry(bottom, width=17, borderwidth=4)
        numberlabel = Label(bottom, text='Number')
        numberEntry = Entry(bottom, width=17, borderwidth=4)
        b1 = Button(bottom, text="Next Item", padx=40, pady=5)

        # Object Placements

        barlabel.grid(row=0, column=0)
        barEntry.grid(row=0, column=1)
        numberlabel.grid(row=1, column=0)
        numberEntry.grid(row=1, column=1)
        b1.grid(row=2, column=1)

    elif position == 3:
        # Building bottom Frame

        bottom = Frame(inven, pady=10, bd=2, highlightbackground='GREEN', relief='sunken')
        bottom.pack(anchor = S)

        # Delete inventory objects

        barlabel = Label(bottom, text='Barcode')
        barEntry = Entry(bottom, width=17, borderwidth=4)
        b1 = Button(bottom, text="Next Item", padx=40, pady=5)

        # Object Placements

        barlabel.grid(row=0, column=0)
        barEntry.grid(row=0, column=1)
        b1.grid(row=2, column=1)


def Cashwindow():
    cash = Toplevel()
    cash.title('Cashier')
    cash.geometry("400x400")

    #Objects
    barcode = Label(cash, text="Barcode")
    Entryb = Entry(cash, width = 17, borderwidth = 4)
    item = Button(cash, text='Next Item', padx= 30, pady= 5)
    cashout = Button(cash, text='Finish Purchase', padx= 30, pady= 5)
    remove = Button(cash, text='Remove Item', padx= 20, pady= 5)

    # Placement in window
    barcode.grid(row=0, column=0)
    Entryb.grid(row=0, column = 1)
    item.grid(row=2, column= 0)
    cashout.grid(row=2, column = 1)
    remove.grid(row=3, column= 0)



def inventoryWindow():

    # All code dealing with inventory button after clicked
    global inven
    inven = Toplevel()
    inven.title('Inventory')
    inven.geometry("400x400")

    top = Frame(inven, relief= 'sunken', pady= 10, bd= 4, padx= 42)
    top.pack(anchor= N)

    # Top Frame objects
    r = IntVar()

    addnewr = Radiobutton(top, text= 'New Product', variable=r, value=0, command= lambda: bottomFrame(r.get()))
    addr = Radiobutton(top, text= 'Add Inventory', variable=r, value=1, command= lambda: bottomFrame(r.get()))
    subtractr = Radiobutton(top, text= 'Remove Inventory', variable= r, value= 2, command= lambda: bottomFrame(r.get()))
    deleter = Radiobutton(top, text= 'Delete Product', variable= r, value= 3, command= lambda: bottomFrame(r.get()))
    viewr = Radiobutton(top, text= 'View Inventory', variable= r, value= 4, command= lambda: bottomFrame(r.get()))

    # Top Frame Placement
    addr.pack(anchor= W)
    subtractr.pack(anchor= W)
    addnewr.pack(anchor= W)
    deleter.pack(anchor=  W)
    viewr.pack(anchor= W)

    global bottom
    bottom = Frame(inven)
    bottom.pack()

root = Tk()
root.title("Point of Sale")
root.geometry("400x400")

#Buttons for the begginning window

inv_button = Button(root, text= 'Inventory management', padx=40, pady=10, command= inventoryWindow)
Cashier_button = Button(root, text= 'Cashier', padx=86, pady=10, command= Cashwindow)

#Placement of buttons in the window

Cashier_button.grid(row= 0, column=0)
inv_button.grid(row= 1, column= 0)

root.mainloop()