import tkinter as tk

#to test if tkinter is working
#tk._test()

window = tk.Tk()
window.title("My First GUI")
window.geometry("500x500") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction

# Add your code to add widgets and
#bind to events

window.mainloop() #main loop to wait for events
