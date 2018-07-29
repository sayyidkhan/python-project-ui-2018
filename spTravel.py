import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
### SQL ###
import sqlite3
import os.path
### SQL ###
### PIL ###
from PIL import Image, ImageTk
### PIL ###

fileName= "sp_Travel_Admin_Database.db"
listOfTourPackages=[]

## Class TourPackage ###
#########################
class TourPackage:
    def __init__(self,name,destination,duration,startDate,endDate,price,image):
        self.__name=name
        self.__destination=destination
        self.__duration=duration
        self.__startDate=startDate
        self.__endDate=endDate
        self.__price=price
        self.__image = image
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
    def getImage_txtFile(self):
        return self.__image
#########################
### Class TourPackage ###

def loadData(fileName):
    db=sqlite3.connect(fileName)
    sql="select * from travel"
    db.row_factory = sqlite3.Row
    rows=db.execute(sql)
    tourLists = []

    for data in rows:
        tourlist = TourPackage(data['name'],data['destination'],data['duration'],data['start_date'],data['end_date'],float(data['price']),data['image_text_file'])
        tourLists.append(tourlist)
    db.close()

    return tourLists

# load image data for validation
def checkData_Withimage_text_file():
    db=sqlite3.connect('sp_Travel_Admin_Database.db')
    sql="select * from travel"
    db.row_factory = sqlite3.Row
    rows=db.execute(sql)
    list_checkData_Withimage_text_file = []
    for data in rows:
        list_checkData_Withimage_text_file.append(data['image_text_file'])
    db.close()
    return list_checkData_Withimage_text_file

#update Tree View of travel package info
def updateTreeView():
	#clear all items in the tree view
	for i in tree1.get_children():
		tree1.delete(i)
	i=0

	for tp in listOfTourPackages:
		#bind the iid with the List item index
		tree1.insert("",i,text=tp.getName(),iid=str(i))
		i+=1

	clearTextBoxes()

def reloadData():
	global listOfTourPackages
	listOfTourPackages=loadData(fileName)
	updateTreeView()
	messagebox.showinfo("Data Load","Data Loaded!")


#search and filter matching tours
def filterTour():

	#clear treeview items
	for i in tree1.get_children():
		tree1.delete(i)

	i=0
	searchStr=txtNameFilter.get().upper()
	#print(searchStr)

	for tp in listOfTourPackages:
		#match substring
		if tp.getName().upper().find(searchStr)>-1:
			#bind the iid with the List item index
			tree1.insert("",i,text=tp.getName(),iid=str(i))
		i+=1
	clearTextBoxes()

def clearTextBoxes():
	#clear text in textboxes
    txtDestination.set("")
    txtDuration.set("")
    txtstartDate.set("")
    txtendDate.set("")
    txtPrice.set("")
    txtImage.set("")
    errorFile_onClick_Change_Pic() # clear image if no txtImage Loaded #displayImage

def selectItem(e):

  curItem = tree1.selection()
  print(curItem[0]) #get the iid
  iid=int(curItem[0])
  print(listOfTourPackages[iid].getName())

  txtDestination.set(listOfTourPackages[iid].getDestination())
  txtDuration.set(listOfTourPackages[iid].getDuration())
  txtstartDate.set(listOfTourPackages[iid].getstartDate())
  txtendDate.set(listOfTourPackages[iid].getendDate())
  txtPrice.set("$"+str(listOfTourPackages[iid].getPriceWithGST()))
  txtImage.set(listOfTourPackages[iid].getImage_txtFile())
  errorFile_onClick_Change_Pic() # display image
### PhotoImage Functions ###
############################

#return the file name
def change_Pic():
    checkimage = checkData_Withimage_text_file()
    image = txtImage.get()
    if image in checkimage:
        value = "images/" + image # returns images/<image name.jpg>
        return value
    else:
        value = "images/no-image-selected.jpg" # returns "images/no-image-selected.jpg"
        return value

#changes the picture state of PhotoImage
def onClick_Change_Pic():
    path = change_Pic()
    open_path = Image.open(path)
    final_path_resized = open_path.resize((180, 180), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(final_path_resized)
    panel.configure(image = img2)
    panel.image = img2

#catch error for FileNotFoundError
def errorFile_onClick_Change_Pic():
    try:
        onClick_Change_Pic() ### update displayImage file ###
    except (FileNotFoundError):
        print("FileNotFoundError have been triggered by system")
        pass ### update file not found error ###

############################
### PhotoImage Functions ###

#Main GUI
window = tk.Tk()
window.title("SP Travel")
window.geometry("500x700") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction

labelAppName=ttk.Label(window,text="SP Travel App",padding=2)
labelAppName.config(font=("Courier", 20))
labelAppName.grid(row=0,column=1,columnspan=3,pady=10)

txtNameFilter=StringVar()
entry1=ttk.Entry(window,textvariable=txtNameFilter)
entry1.grid(row=1,column=1)
buttonSearch=ttk.Button(window,text='Filter Tour',command=filterTour)
buttonSearch.grid(row=1,column=2)

#treeview
tree1=ttk.Treeview(window)
tree1.heading("#0",text="Tour Package Name")

tree1.grid(row=2,column=0,columnspan=2,pady=15)
tree1.bind('<ButtonRelease-1>', selectItem)

#Travel Package Details
labelDestination=ttk.Label(window,text="Destination",padding=2)
labelDestination.grid(row=3,column=0,sticky=tk.W)
txtDestination=StringVar()
textDestination=ttk.Entry(window,textvariable=txtDestination,state='readonly')
textDestination.grid(row=3,column=1,pady=2)

labelDuration=ttk.Label(window,text="Duration",padding=2)
labelDuration.grid(row=4,column=0,sticky=tk.W)
txtDuration=StringVar()
textDuration=ttk.Entry(window,textvariable=txtDuration,state='readonly')
textDuration.grid(row=4,column=1,pady=2)

labelstartDate=ttk.Label(window,text="Start Date",padding=2)
labelstartDate.grid(row=5,column=0,sticky=tk.W)
txtstartDate=StringVar()
textstartDate=ttk.Entry(window,textvariable=txtstartDate,state='readonly')
textstartDate.grid(row=5,column=1,pady=2)

labelendDate=ttk.Label(window,text="End Date",padding=2)
labelendDate.grid(row=6,column=0,sticky=tk.W)
txtendDate=StringVar()
textendDate=ttk.Entry(window,textvariable=txtendDate,state='readonly')
textendDate.grid(row=6,column=1,pady=2)

labelPrice=ttk.Label(window,text="Price(GST)",padding=2)
labelPrice.grid(row=7,column=0,sticky=tk.W)
txtPrice=StringVar()
textPrice=ttk.Entry(window,textvariable=txtPrice,state='readonly')
textPrice.grid(row=7,column=1,pady=2)

labelImage=ttk.Label(window,text="File Name(Image)",padding=2)
labelImage.grid(row=8,column=0,sticky=tk.W)
txtImage =StringVar()
textImage =ttk.Entry(window,textvariable=txtImage,state='readonly')
textImage.grid(row=8,column=1,pady=2)

### tkinter photo ###
try:
    path = change_Pic()
    open_path = Image.open(path)
    final_path_resized = open_path.resize((180, 180), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(final_path_resized)
    panel = ttk.Label(window, image = img)
    panel.image = img
    panel.place(x = 270, y = 100, height = 180, width = 180)
except:
    pass

### tkinter photo ###

button1=ttk.Button(window,text='Reload Data',command=reloadData)
button1.grid(row=9,column=1,columnspan=3,pady=10)

#load text file data and get the list Of TourPackages
listOfTourPackages=loadData(fileName)

updateTreeView()

window.mainloop() #main loop to wait for events
