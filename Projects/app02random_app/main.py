from tkinter import *
from functools import partial
import random
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk

def connection():
    conn = sqlite3.connect('app2db.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS app2main (id INTEGER PRIMARY KEY, name TEXT, Log Text)")
    conn.commit()
    conn.close()




tkWindow = Tk()
tkWindow.geometry('1250x720')
tkWindow.title('Aplicativo')

products_label = ttk.Label(tkWindow,text="Products", width=200)
products_label.pack(ipadx=10, ipady=10)
products_Entry = Entry(tkWindow, show = 'name')



  

tkWindow.mainloop()


