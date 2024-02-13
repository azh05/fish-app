import tkinter as tk
from tkinter import filedialog
import PIL.Image as Image
import os

def save_canvas_as_image(root, canvas):
    current_dir = os.getcwd()

    save_dir = os.path.join(current_dir, "saveddoodles")

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    

    file_path = filedialog.asksaveasfilename(defaultextension=".ps", initialdir=save_dir)
    print(file_path)
    if file_path:
        canvas.postscript(file = file_path) 
        # use PIL to convert to PNG 
        img = Image.open(file_path) 
        img.save(file_path[:-3] + '.png', 'png') 

        # remove postscript file
        os.remove(file_path)


#draw lines
def get_x_and_y(event):
    global lasx,lasy
    lasx, lasy = event.x, event.y

def draw(event, canvas):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='black')
    lasx, lasy = event.x, event.y

def main():
    # Create the main window
    root = tk.Tk()
    root.geometry("400x400")

    # Create a canvas
    canvas = tk.Canvas(root, bg="white", width=300, height=300)
    canvas.pack()

    # Draw something on the canvas (e.g., a rectangle)
    canvas.bind("<Button-1>", get_x_and_y)
    canvas.bind("<B1-Motion>", lambda event: draw(event, canvas))

    # Create a button to save the canvas as an image
    save_button = tk.Button(root, text="Save Canvas", command=lambda: save_canvas_as_image(root, canvas))
    save_button.pack()

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()