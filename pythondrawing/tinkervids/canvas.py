from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.geometry("400x400")
canvas = Canvas(app, bg='white')
canvas.pack(anchor='nw', fill='both', expand=1)


# create an image and align it to the top left corner of the campus
"""
image = Image.open("/Users/anthonyzhao/Desktop/Career/Headshots/DSCF1858.jpg")
image = image.resize((400, 400), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=image, anchor='nw')
"""

#draw lines
def get_x_and_y(event):
    global lasx,lasy
    lasx, lasy = event.x, event.y

def draw(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='black')
    lasx, lasy = event.x, event.y

# left click
canvas.bind("<Button-1>", get_x_and_y)
# drag while left click
canvas.bind("<B1-Motion>", draw)

app.mainloop()