import  sqlite3
from tkinter import messagebox
dbase = sqlite3.connect('Logins.db')

c = dbase.cursor()

dbase.execute(''' CREATE TABLE IF NOT EXISTS Logins(
                             usuario TEXT NOT NULL,
                            senha TEXT NOT NULL)''')



    

dbase.commit()

def write(usuario, senha):
        c.execute(''' INSERT into Logins (usuario, senha) VALUES(?, ?)''', (usuario, senha))
        
        dbase.commit()
        
        
def read(usuario):
        c.execute(''' SELECT * FROM Logins WHERE usuario =?''', (usuario))
        return c.fetchone()
    
dbase.commit()
    
def delete(senha):
        c.execute(''' SELECT * FROM Logins WHERE senha =?''', (senha))
        return c.fetchone()
    
dbase.commit()
    
    
def validate_login(usuario, senha):
    
        c.execute(''' SELECT * FROM Logins WHERE usuario =? AND senha =?''', (usuario, senha))
        return c.fetchone()
    
    
dbase.commit()

def login(self):
            
                    if self.uname.get()=="b-dev" and self.pass_.get()=="123":
                        messagebox.showinfo("Welcome")
                        
