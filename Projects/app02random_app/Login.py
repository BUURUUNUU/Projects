from tkinter import *
from functools import partial
import random
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import os



def connection():
    conn = sqlite3.connect('app2db.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS app2login (id INTEGER PRIMARY KEY, usernames TEXT, passwords TEXT)")
    conn.commit()
    conn.close()
    

connection()






#window
tkWindow = Tk()  
tkWindow.geometry('165x120')  
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=1, column= 4)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=2, column=4) 



                    

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=3, column=4)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=4, column=4)  





#login button
loginButton = Button(tkWindow, text="Login").grid(row=6, column=4)  



 

if username.get() == 'admin' and password.get() == 'admin':
    exec(open('main.py').read())
    tkWindow.destroy()
            
            







                    
                    
tkWindow.mainloop()







           




        
        
        
#-----------------------------------------------------------------------------------------------------------------
        
        
        
        
