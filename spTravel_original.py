import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox

fileName="tourlist.txt"
listOfTourPackages=[]

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
        self.__price=price
    def getPriceWithGST(self):
        return(self.__price*1.07)

#load data from some supplied filename
def loadData(fileName):
	#Load Data to GUI
	file=open(fileName,'r')
	lines=file.readlines()
	tourLists=[]

	for eachLine in lines:
		eachLine=eachLine.replace("\n","")
		cols=eachLine.split("|")
		name=cols[0]
		destination=cols[1]
		duration=cols[2]
		period=cols[3]
		price=float(cols[4])
		tourlist=TourPackage(name,destination,duration,period,price)
		tourLists.append(tourlist)
	
	file.close()


	return tourLists

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
	txtPeriod.set("")
	txtPrice.set("")

def selectItem(e):
	
	curItem = tree1.selection()
	print(curItem[0]) #get the iid 
	iid=int(curItem[0])
	print(listOfTourPackages[iid].getName())

	txtDestination.set(listOfTourPackages[iid].getDestination())
	txtDuration.set(listOfTourPackages[iid].getDuration())
	txtPeriod.set(listOfTourPackages[iid].getPeriod())
	txtPrice.set("$"+str(listOfTourPackages[iid].getPriceWithGST()))


#Main GUI	
window = tk.Tk() 
window.title("SP Travel")
window.geometry("340x500") #You want the size of the app to be 500x500
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

tree1.grid(row=2,column=1,columnspan=2,pady=15)
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

labelDescription=ttk.Label(window,text="Period",padding=2)
labelDescription.grid(row=5,column=0,sticky=tk.W)
txtPeriod=StringVar()
textPeriod=ttk.Entry(window,textvariable=txtPeriod,state='readonly',width=34)
textPeriod.grid(row=5,column=1,columnspan=2,pady=2)

labelPrice=ttk.Label(window,text="Price(GST)",padding=2)
labelPrice.grid(row=6,column=0,sticky=tk.W)
txtPrice=StringVar()
textPrice=ttk.Entry(window,textvariable=txtPrice,state='readonly')
textPrice.grid(row=6,column=1,pady=2)

button1=ttk.Button(window,text='Reload Data',command=reloadData)
button1.grid(row=7,column=0,columnspan=3,pady=10)

#load text file data and get the list Of TourPackages
listOfTourPackages=loadData(fileName)
updateTreeView()

window.mainloop() #main loop to wait for events
