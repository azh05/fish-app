from tkinter import *

root = Tk()

def onClick():
    myLabel = Label(root, text = "YUMMY!")
    myLabel.pack()

myButton = Button(root, text = "End World Hunger!", padx=50, command=onClick)
myButton.pack()

root.mainloop()