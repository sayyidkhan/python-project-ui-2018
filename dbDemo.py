import sqlite3
import os.path
def initDatabase():
    db=sqlite3.connect('dbDemo.db')
    sql="create table travel(name text primary key,country text)"
    db.execute(sql)
    sql="insert into travel(name,country) values('Korea Ski-ing Winter Tour','Korea')"
    db.execute(sql)
    db.commit()
    db.close()

def readData():
    db=sqlite3.connect('dbDemo.db')
    sql="select * from travel"
    db.row_factory = sqlite3.Row
    rows=db.execute(sql)
    for data in rows:
        print(data['name']+" -- "+data['country'])
    db.close()


def insertData(name,country):
    db=sqlite3.connect('dbDemo.db')
    sql="insert into travel(name,country) values(?,?)"
    db.execute(sql,(name,country))
    db.commit()
    db.close()

#Exercise...
def deleteData(name):
    print("Delete...")
    db=sqlite3.connect('dbDemo.db')
    sql="delete from travel where name=?"
    db.execute(sql,(name,))
    db.commit()
    db.close()

#create a database when it does not exist
if not os.path.exists("dbDemo.db"): #cannot find file dbDemo.db
    initDatabase()

userInput=""
while userInput!="Q":
    userInput=input("Enter R to display Data or I to insert Data or D to delete Data or Q to quit")

    if userInput=="R":
        readData()

    elif userInput=="I":
        name=input("Enter the name of travel package:")
        country=input("Enter the Country:")
        insertData(name,country)
    
    elif userInput=="D":
        name=input("Enter the name of tour package to Delete")
        deleteData(name)
