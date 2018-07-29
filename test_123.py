import tkinter as ttk
#installing PIL, https://stackoverflow.com/questions/20060096/installing-pil-with-pip
#pip3 install Pillow
from PIL import Image, ImageTk

class image_test():
    def __init__(self,image):
        self.image = image
    def getImage_txtFile(self):
        return self.image

window = tk.Tk()
window.title("My First GUI")
window.geometry("500x500")

# Add your code to add widgets and
#bind to events
test = "lenna.jpg"
image = Image.open("images/" + image_test(test).getImage_txtFile())
photo = ImageTk.PhotoImage(image)

label1 = ttk.Label(image=photo)
label1.image = photo # keep a reference!
label1.pack()
#label1.place(x=200, y=200)


window.mainloop() #main loop to wait for events
