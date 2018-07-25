import tkinter as tk
#installing PIL, https://stackoverflow.com/questions/20060096/installing-pil-with-pip
#pip3 install Pillow
from PIL import Image, ImageTk

window = tk.Tk()

window.title("My First GUI")
window.geometry("500x500")

# Add your code to add widgets and
#bind to events

image = Image.open("images/" + "lenna.jpg")
photo = ImageTk.PhotoImage(image)

label = tk.Label(image=photo)
label.image = photo # keep a reference!
label.pack()


window.mainloop() #main loop to wait for events
