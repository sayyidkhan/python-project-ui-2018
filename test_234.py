import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()

def generate_random():
    list_items = ["hongkong.jpg","japan.jpg","lenna.jpg"]
    image_file = random.choice(list_items)
    return image_file

img = ImageTk.PhotoImage(Image.open("images/no-image-selected.jpg"))
panel = tk.Label(root, image=img)
panel.grid(row=1,column=1,columnspan=3,pady=10)

def callback():
    path = "images/" + generate_random()
    img2 = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img2)
    panel.image = img2

### button ###
button5= tk.Button(root,text='change_pic',command= callback)
button5.grid(row=2,column=1,columnspan=3,pady=10)
### button ###
#root.bind("<Return>", callback)
root.mainloop()
