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
    def __init__(self,name,destination,duration,startDate,endDate,price):
        self.__name=name
        self.__destination=destination
        self.__duration=duration
        self.__startDate=startDate
        self.__endDate=endDate
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
    def getstartDate(self):
        return self.__startDate
    def setstartDate(self,startDate):
        self.__startDate = startDate
    def getendDate(self):
        return self.__endDate
    def setendDate(self,period):
        self.__endDate = endDate
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
        startDate = cols[3]
        endDate=cols[4]
        price=cols[5]
        tourlist=TourPackage(name,destination,duration,startDate,endDate,price)
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
    sql="create table travel(name text primary key,destination text,duration text,start_date text,end_date text,price real)"
    db.execute(sql)
    for tp in listOfTourPackages:
        sql="insert into travel(name,destination,duration,start_date,end_date,price) values('"+tp.getName()+"','"+tp.getDestination()+"','"+tp.getDuration()+"','"+tp.getstartDate()+"','"+tp.getendDate()+"','"+tp.getPrice()+"')"
        db.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("DataBase Update - Success","Database initialized")

def insertData(name,destination,duration,startDate,endDate,price):
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="insert into travel(name,destination,duration,start_date,end_date,price) values(?,?,?,?,?,?)"
    db.execute(sql,(name,destination,duration,startDate,endDate,price))
    db.commit()
    db.close()

def updateData(name,destination,duration,startDate,endDate,price):
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="update travel set name=?, destination=?, duration=?, start_date=?, end_date=?, price=? where name=?"
    db.execute(sql,(name,destination,duration,startDate,endDate,price,name))
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

#
def readData_allData():
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="select * from travel"
    db.row_factory = sqlite3.Row
    rows=db.execute(sql)
    list_checkData_WithName = []
    for data in rows:
        attributes = [data['name'],data['destination'],data['duration'],data['start_date'],data['end_date'],data['price']]
        list_checkData_WithName.append(attributes)
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
#validate_number
def is_number(number_float):
  try:
    float(number_float)
    return True
  except ValueError:
    return False
    
#insert_Button_message_box_info
def insert_Button():
    name = txtName.get()
    destination = txtDestination.get()
    duration = txtDuration.get()
    startDate = txtstartDate.get()
    endDate = txtendDate.get()
    price = txtPrice.get()
    if name != "" and destination != "" and duration != "" and startDate != "" and endDate != "" and price != "":
      if is_number(price) == True:
        print("Database Inserted:", name,destination,duration,startDate,endDate,price)
        insertData(name,destination,duration,startDate,endDate,price)
        messagebox.showinfo("DataBase Update - Success","Added New Database Entry")
      else:
        messagebox.showinfo("DataBase Update - Failed","Incomplete Entry, price is not a number")
    else:
      if is_number(price) == False:
        messagebox.showinfo("DataBase Update - Failed","Incomplete Entry, price is not a number")
      else:
        messagebox.showinfo("DataBase Update - Failed","Incomplete Entry, Please complete all data entry")

#delete_Button_message_box_info
def delete_Button():
    name = txtName.get()
    txtName.set("")
    txtDestination.set("")
    txtDuration.set("")
    txtstartDate.set("")
    txtendDate.set("")
    txtPrice.set("")
    my_list = checkData_WithName()
    if name in my_list:
        print("Database Deleted:", name)
        deleteData(name)
        messagebox.showinfo("DataBase Update - Success",  name + ", have been successfully deleted")
    elif name == "":
        messagebox.showinfo("DataBase Update - Null","Incomplete entry, no data entered")
    else:
        print (name,"not in my list")
        messagebox.showinfo("DataBase Update - Failed",  name + ", is not a valid entry in the database.")

#search_Button: search for the package, and prints the package out
def search_Button():
    name = txtName.get()
    my_list = checkData_WithName()
    all_packages = readData_allData()
    ### check if the name is in the database, check against all names ###
    if name in my_list:
        ### run a for loop to isolate the database down to a single array to validate ###
        for package in all_packages:
            ### if name in package, will print out the data ###
            if name in package:
                print("package:", package)
                txtName.set(package[0])
                txtDestination.set(package[1])
                txtDuration.set(package[2])
                txtstartDate.set(package[3])
                txtendDate.set(package[4])
                txtPrice.set(package[5])
        messagebox.showinfo("DataBase Search - Success",  name + ", have been successfully displayed")
    elif name == "":
        messagebox.showinfo("DataBase Search - Null",  "no data selected")
    else:
        messagebox.showinfo("DataBase Search - Failed", name + ", is not available in the database")

#update_Button: update the package, and prints the package out
def update_Button():
    name = txtName.get()
    destination = txtDestination.get()
    duration = txtDuration.get()
    startDate = txtstartDate.get()
    endDate = txtendDate.get()
    price = txtPrice.get()
    if name != "" and destination != "" and duration != "" and startDate != "" and endDate != "" and price != "":
        print("Database Updated:", name,destination,duration,startDate,endDate,price)
        updateData(name,destination,duration,startDate,endDate,price)
        messagebox.showinfo("DataBase Update - Success",  name + ", have been successfully updated")
    else:
        messagebox.showinfo("DataBase Update - Failed",  "One of the fields are empty")

#clear text in textboxes
def clear_Button():
    print("clear")
    txtName.set("")
    txtDestination.set("")
    txtDuration.set("")
    txtstartDate.set("")
    txtendDate.set("")
    txtPrice.set("")
#####################
### GUI Functions ###

### GUI ###
###########
window = tk.Tk()
window.title("Sp Travel Admin")
window.geometry("550x550") #You want the size of the app to be 500x500
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

### start date Period ###
labelstartDate = ttk.Label(window,text="Start Date",padding=2)
labelstartDate.grid(row=5,column=0,sticky=tk.W)
txtstartDate = StringVar()
textstartDate = ttk.Entry(window,textvariable=txtstartDate)
textstartDate.grid(row=5,column=1,pady=2)

### end date Period ###
labelendDate = ttk.Label(window,text="End Date",padding=2)
labelendDate.grid(row=6,column=0,sticky=tk.W)
txtendDate = StringVar()
textendDate = ttk.Entry(window,textvariable=txtendDate)
textendDate.grid(row=6,column=1,pady=2)

### label Price ###
labelPrice = ttk.Label(window,text="Price",padding=2)
labelPrice.grid(row=7,column=0,sticky=tk.W)
txtPrice = StringVar()
textPrice = ttk.Entry(window,textvariable=txtPrice)
textPrice.grid(row=7,column=1,pady=2)

### Button insert Data ###
button1=ttk.Button(window,text='Insert',command= insert_Button)
button1.grid(row=8,column=1,columnspan=3,pady=10)
### Button Delete Data ###
button2=ttk.Button(window,text='Delete',command= delete_Button)
button2.grid(row=8,column=2,columnspan=3,pady=10)
### Button update Data ###
button2=ttk.Button(window,text='Search',command= search_Button)
button2.grid(row=9,column=1,columnspan=3,pady=10)
### Button update Data ###
button2=ttk.Button(window,text='Update',command= update_Button)
button2.grid(row=9,column=2,columnspan=3,pady=10)
### Button clear Data ###
button2=ttk.Button(window,text='Clear',command= clear_Button)
button2.grid(row=10,column=2,columnspan=3,pady=10)
### GUI ###
###########


window.mainloop() #main loop to wait for events
