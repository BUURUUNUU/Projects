import PySimpleGUI as sg
from tkinter import *
import os.path
import hashlib
import getpass

from tkinter import *


from tkinter import *




#----------------------------------------
sg.theme('random')
#----------------------------------------
username = ('-usuario-')
password =( '-password-')




flayout = [
               [sg.Text('Usuario'), sg.InputText('', key = '-NAME-')],
              [sg.Text('Senha'), sg.InputText('', key = '-PASSWORD-')],
               [sg.Button('Login')]
        ]

window= sg.Window('RH App', flayout, element_justification='center')


#----------------------------------------

    
#----------------------------------------

    

while True:
    
    button, values = window.read()
    
    
        
        
        
        
   
    if button == ('Login'):
        NAME = values['-NAME-']
        PASSWORD=values['-PASSWORD-']
        h= hashlib.new('sha256')
        h.update(PASSWORD.encode())
        print(h.hexdigest())
        
        
        
        if NAME == "admin" and PASSWORD == '123':
            exec(open('main2.py').read())
            
            
        else:
                window['-NAME-'].update('')
                window['-PASSWORD-'].update('')
        
        
      
         
        
    

    
     
            
#----------------------------------------

    

#----------------------------------------
