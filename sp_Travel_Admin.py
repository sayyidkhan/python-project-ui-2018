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

fileName_txt ="tourlist.txt"

### Class TourPackage ###
#########################
class TourPackage:
    def __init__(self,name,destination,duration,period,price):
        self.__name=name
        self.__destination=destination
        self.__duration=duration
        self.__period=period
        self.__price=price
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getDestination(self):
        return self.__destination
    def setDestination(self,destination):
        self.__destination=destination
    def getDuration(self):
        return self.__duration
    def setDuration(self,duration):
        self.__duration=duration
    def getPeriod(self):
        return self.__period
    def setPeriod(self,period):
        self.__period=period
    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        self.__price = price
    def getPriceWithGST(self):
        return(self.__price * 1.07)
#########################
### Class TourPackage ###

### load text file ###
######################
#load data from some supplied filename
def loadData(fileName):
	#Load Data to GUI
	file=open(fileName_txt,'r')
	lines=file.readlines()
	tourLists=[]
	for eachLine in lines:
		eachLine=eachLine.replace("\n","")
		cols=eachLine.split("|")
		name=cols[0]
		destination=cols[1]
		duration=cols[2]
		period=cols[3]
		price=cols[4]
		tourlist=TourPackage(name,destination,duration,period,price)
		tourLists.append(tourlist)
	file.close()
	return tourLists

#load text file data and get the list Of TourPackages
listOfTourPackages = loadData(fileName_txt)
######################
### load text file ###

### SQL Functions ###
#####################
def initDatabase():
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="create table travel(name text primary key,destination text,duration text,period text,price real)"
    db.execute(sql)
    for tp in listOfTourPackages:
        sql="insert into travel(name,destination,duration,period,price) values('"+tp.getName()+"','"+tp.getDestination()+"','"+tp.getDuration()+"','"+tp.getPeriod()+"','"+tp.getPrice()+"')"
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

#store all "package name" into an array, which will be used later to validate if "package name" contains in an array
def checkData_WithName():
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="select * from travel"
    db.row_factory = sqlite3.Row
    rows=db.execute(sql)
    list_checkData_WithName = []
    for data in rows:
        list_checkData_WithName.append(data['name'])
    db.close()
    return list_checkData_WithName
#####################
### SQL Functions ###

### create a database when it does not exist ###
################################################
if not os.path.exists('sp_Travel_Admin_Database.db'): #cannot find file sp_Travel_Admin_Database.db
    initDatabase()
################################################
### create a database when it does not exist ###

### GUI Functions ###
#####################
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

#delete_Button_message_box_info
def delete_Button():
    name = txtName.get()
    txtName.set("")
    txtDestination.set("")
    txtDuration.set("")
    txtPeriod.set("")
    txtPrice.set("")
    my_list = checkData_WithName()
    if name in my_list:
        deleteData(name)
        messagebox.showinfo("DataBase Update - Success",  name + ", have been successfully deleted")
    elif name == "":
        messagebox.showinfo("DataBase Update - Null","Incomplete entry, no data entered")
    else:
        print (name,"not in my list")
        messagebox.showinfo("DataBase Update - Failed",  name + ", is not a valid entry in the database.")

#####################
### GUI Functions ###

### GUI ###
###########
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
### GUI ###
###########


window.mainloop() #main loop to wait for events
