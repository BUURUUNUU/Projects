from rembg import remove

from PIL import Image

import easygui as eg

import tkinter as tk
import tkinter as ttk

from tkinter import Tk, Text



root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width = 500, height = 10, bg = '#ffffff')
text = Text(root, height=2, width=50)

text.pack()

text.insert('1.0', 'Atenção: É necessário especificar a extensão da imagem ao fazer download! exemplo: imagem1.png')

frame.pack()
canvas.pack()
root.title('Remover background')

def download_clicked():
    
    
    input_path = eg.fileopenbox(title='Select image file')
    output_path = eg.filesavebox(title='Save file to..')
    
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    
download_button = ttk.Button(root, text='Upload', compound=tk.LEFT, command=download_clicked)
download_button.pack(ipadx = 10, ipady=10, expand=True)


#input_path = eg.fileopenbox(title='Select image file')
#output_path = eg.filesavebox(title='Save file to..')

#input = Image.open(input_path)
#output = remove(input)
#output.save(output_path)




root.mainloop()