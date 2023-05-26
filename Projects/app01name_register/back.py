import  sqlite3

dbase = sqlite3.connect('Registro.db')

c = dbase.cursor()

dbase.execute(''' CREATE TABLE IF NOT EXISTS Registro(
                             ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             NAME TEXT NOT NULL
                             )''')
    

dbase.commit()


c = dbase.cursor()

def write(ID, NAME):
        
        c.execute('''INSERT into Registro (ID, NAME) VALUES (?, ?)''', (ID, NAME))
        
        
        dbase.commit()
        
 
def delete(x):
        
        c.execute('''delete from Registro where NAME =?''', x)
        
        
        dbase.commit()
        
def read_task():
        c = dbase.cursor()
        c.execute('''SELECT NAME from Registro''')
        data = c.fetchall()
        dbase.commit()
        return data