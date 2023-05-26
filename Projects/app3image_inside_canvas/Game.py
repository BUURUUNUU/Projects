import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion


root = tk.Tk()

root.title('Game')

C = canvas = tk.Canvas(root, width = 1280, height = 720, bg = 'white')
canvas.pack(anchor = tk.CENTER, expand = True)




my_image = tk.PhotoImage(file = 'output.gif')
image_item = canvas.create_image(
    (100, 100),image = my_image)


canvas.tag_bind(
    image_item,
    '<Button-1>',
    lambda e: canvas.delete(image_item))







root.mainloop()

