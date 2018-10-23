# python-project-ui-2018
Back End development Project, Python Backend of Travel website
For python 3.6.5 and above.
___

it is a GUI project with the use of tkinter(python library) to do CRUD(create, read, update, delete) of the travel packages.
The goal for this project is to better understand how to write python programs in a OOP(object oriented programming) manner.
i used the sqlite as a database.there is also an image processing tool where the pogram is able to display images of the 
travel site.

## libraries required:
###### tkinter
* tkinter
* tkinter.ttk
###### sqlite3
* sqlite3
###### pil library
* PIL 

libraries which need to be installed before the program can be run.

## User Interface

There are two programs in this files.

###### The first file, view travel package

**_This first file_** can be started by starting **_"spTravel.py"_**.
This file is to view what are the **_existing travel packages_**.

**Screen 1: Landing page of the Application**

> ![screen shot 2018-10-23 at 10 03 34 pm](https://user-images.githubusercontent.com/22993048/47366105-88899780-d70f-11e8-8e4f-317f085c2fdd.png)

**Screen 2: Loading/refresh the database**
> if the database is being updated/added/removed, we can click reload data to update the database.
![screen shot 2018-10-23 at 10 11 59 pm](https://user-images.githubusercontent.com/22993048/47366653-b7ecd400-d710-11e8-9451-09f64310d810.png)

**Screen 3: Load a travel package**
> select one of the travel package to view the travel package.
![screen shot 2018-10-23 at 10 16 51 pm](https://user-images.githubusercontent.com/22993048/47367126-a3f5a200-d711-11e8-9951-9cac8f900b41.png)

###### The second file, perform CRUD operations to the travel package.

**_This second file_** can be started by starting **_"sp_Travel_Admin.py"_**.
This file is to perform CRUD(create,read,update,delete) on the application.

**Screen 1: Landing page of the Application**
> if there is no data in the database.db what the system will do is it will read from tourlist.txt to create a database from it.
![screen shot 2018-10-23 at 10 25 02 pm](https://user-images.githubusercontent.com/22993048/47367581-8aa12580-d712-11e8-8769-b1b0233203c0.png)

**Screen 2: Create a new travel Package**
> user can add new travel package into the database
![screen shot 2018-10-23 at 10 29 36 pm](https://user-images.githubusercontent.com/22993048/47368009-6eea4f00-d713-11e8-8865-247b12d4f603.png)

**Screen 3: Read an existing travel Package**
> user can search an travel package which is added into the database
![screen shot 2018-10-23 at 10 35 38 pm](https://user-images.githubusercontent.com/22993048/47368329-06e83880-d714-11e8-9270-6ce5643b8a87.png)
![screen shot 2018-10-23 at 10 35 45 pm](https://user-images.githubusercontent.com/22993048/47368330-0780cf00-d714-11e8-83c5-2ca4f6a53f86.png)

**Screen 4: Update an existing travel Package**
