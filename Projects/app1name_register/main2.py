import PySimpleGUI as sg
from random import randint
import back
from tkinter import *
import os.path
import sys
import Log
from tkinter import *


from tkinter import *
sg.theme('random')
def front(): 
    
    ID = ''
    IDD= ''
NAME = back.read_task()     
NAMED = Log.read_task()  

#----------------------------------------
layout = [
        [sg.Text('Nome'), sg.InputText('', key= '-NAME-'), sg.Text('                               Produtos'), sg.InputText('', key= '-LOG-')],
        [sg.Button('Adicionar'),sg.Text('                                                                                                    '), sg.Button('Salvar')],
        
        [sg.Text('')],
        [sg.Text('Funcionarios Cadastrados'),sg.Text('                                                                                                                            ') , sg.Text('Lista de Produtos',justification='right')],
       
        [sg.Listbox(NAME, size=(50, 33), key='-BOX-'), sg.Listbox(NAMED, size=(100,33), key='-BOXX-'), sg.Text('     '), sg.Button('Atualizar')],
        [sg.Button('Deletar'), sg.Text('                                                                      '), sg.Button ('Deletar Log'), sg.Text('                                                                                                                                                                   '),  sg.Button('Sair')]
        
    ]
#---------------------------------------------------------------



front()
#----------------------------------------
window= sg.Window('Cadastro', layout,  size =(1280, 650), element_justification='left')

#----------------------------------------



   
while True:
        button, values = window.read()
        WIN_CLOSED = False
                            
        if button == 'Sair':
            window(exit)
            break
                            
        if button == 'Salvar':
            IDD = randint(1, 999)
            NAMED = values['-LOG-']
            
            
            
                             
            if NAMED != '':
            
                Log.write(IDD, NAMED)
                NAMED = Log.read_task()  
            
                                    

                                    
                window.find_element('-LOG-').Update('')
                window.find_element('-BOXX-').Update(NAMED)
                
                
        if button =='Deletar Log':        
                if NAMED != '':
                    button, values = window.read()                  
                    x= values['-BOXX-'][0]
                    Log.delete(x)
                    NAMED = Log.read_task()          
                    window.find_element('-BOXX-').Update(NAMED)
                         
                    

 #---------------------------------------------------------------------------------------------------                              
                            
        if button == 'Adicionar':
            ID = randint(1, 999)
            NAME = values['-NAME-']
            
            
            
                             
            if NAME != '':
            
                back.write(ID, NAME)
                NAME = back.read_task()  
            
                                    

                                    
                window.find_element('-NAME-').Update('')
                window.find_element('-BOX-').Update(NAME)

        if button =='Atualizar':
            window.find_element('-LOG-').Update('')
            window.find_element('-BOXX-').Update(NAMED)
            window.find_element('-NAME-').Update('')
            window.find_element('-BOX-').Update(NAME)
            
            
                     
        if button == 'Deletar': 
            button, values = window.read()    
            if NAME:
                              
                x= values['-BOX-'][0]
                back.delete(x)
                NAME = back.read_task()          
                window.find_element('-BOX-').Update(NAME)
                


               
                                    


#----------------------------------------
                
                
                
                
             
               