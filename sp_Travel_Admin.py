### tkinter ###
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
### tkinter ###
### SQL ###
import sqlite3
import os.path
### SQL ###

### SQL Functions ###
def initDatabase():
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="create table travel(name text primary key,destination text,duration text,period text,price text)"
    db.execute(sql)
    sql="insert into travel(name,destination,duration,period,price) values('Korea Ski-ing Winter Tour','Korea','5D4N','01 January 2017 to 20 May 2018','999')"
    db.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("DataBase Update - Success","Database initialized")

def insertData(name,destination,duration,period,price):
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="insert into travel(name,destination,duration,period,price) values(?,?,?,?,?)"
    db.execute(sql,(name,destination,duration,period,price))
    db.commit()
    db.close()

def deleteData(name):
    print("Delete...")
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="delete from travel where name=?"
    db.execute(sql,(name,))
    db.commit()
    db.close()


#create a database when it does not exist
if not os.path.exists('sp_Travel_Admin_Database.db'): #cannot find file dbDemo.db
    initDatabase()


### GUI Functions ###
#insert_Button_message_box_info
def insert_Button():
    name = txtName.get()
    destination = txtDestination.get()
    duration = txtDuration.get()
    period = txtPeriod.get()
    price = txtPrice.get()
    if name != "" and destination != "" and duration != "" and period != "" and price != "":
      insertData(name,destination,duration,period,price)
      messagebox.showinfo("DataBase Update - Success","Added New Database Entry")
    else:
      messagebox.showinfo("DataBase Update - Failed","Incomplete Entry, Please complete all data entry")

#insert_Button_message_box_info
def delete_Button():
    name = txtName.get()
    txtName.set("")
    txtDestination.set("")
    txtDuration.set("")
    txtPeriod.set("")
    txtPrice.set("")
    if name != "":
        deleteData(name)
        messagebox.showinfo("DataBase Update - Success","Deleted Database Entry")
    elif name == "":
        messagebox.showinfo("DataBase Update - Failed","No data Entry entered, Please complete all data entry")


### GUI ###
window = tk.Tk()
window.title("Sp Travel Admin")
window.geometry("500x500") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction
#
### label App Name ###
labelAppName = ttk.Label(window , text="SP Travel App" ,padding=2)
labelAppName.config(font=("Arial", 40))
labelAppName.grid(row=0,column=1,columnspan=3,pady=10)

#Travel Package Details
### label Name ###
labelName=ttk.Label(window,text="Name",padding=2)
labelName.grid(row=2,column=0,sticky=tk.W)
txtName = StringVar()
textName = ttk.Entry(window,textvariable=txtName)
textName.grid(row=2,column=1,pady=2)

### label Destination ###
labelDestination = ttk.Label(window,text="Destination",padding=2)
labelDestination.grid(row=3,column=0,sticky=tk.W)
txtDestination = StringVar()
textDestination = ttk.Entry(window,textvariable=txtDestination)
textDestination.grid(row=3,column=1,pady=2)

### label Duration ###
labelDuration = ttk.Label(window,text="Duration",padding=2)
labelDuration.grid(row=4,column=0,sticky=tk.W)
txtDuration = StringVar()
textDuration = ttk.Entry(window,textvariable=txtDuration)
textDuration.grid(row=4,column=1,pady=2)

### label Period ###
labelPeriod = ttk.Label(window,text="Period",padding=2)
labelPeriod.grid(row=5,column=0,sticky=tk.W)
txtPeriod = StringVar()
textPeriod = ttk.Entry(window,textvariable=txtPeriod)
textPeriod.grid(row=5,column=1,pady=2)

### label Price ###
labelPrice = ttk.Label(window,text="Price",padding=2)
labelPrice.grid(row=6,column=0,sticky=tk.W)
txtPrice = StringVar()
textPrice = ttk.Entry(window,textvariable=txtPrice)
textPrice.grid(row=6,column=1,pady=2)

### Button insert Data ###
button1=ttk.Button(window,text='Insert',command= insert_Button)
button1.grid(row=7,column=1,columnspan=3,pady=10)
### Button Delete Data ###
button2=ttk.Button(window,text='Delete',command= delete_Button)
button2.grid(row=7,column=2,columnspan=3,pady=10)


window.mainloop() #main loop to wait for events
