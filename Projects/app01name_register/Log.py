import  sqlite3

dbase = sqlite3.connect('Log.db')

c = dbase.cursor()

dbase.execute(''' CREATE TABLE IF NOT EXISTS Log(
                             IDD INTEGER PRIMARY KEY AUTOINCREMENT,
                             NAMED TEXT NOT NULL
                             )''')
    

dbase.commit()



c = dbase.cursor()

def write(IDD, NAMED):
        
        c.execute('''INSERT into Log (IDD, NAMED) VALUES (?, ?)''', (IDD, NAMED))
        dbase.commit()
        
 
def delete(x):
        
        c.execute('''delete from Log where NAMED =?''', x)
        
        
        dbase.commit()
        
def read_task():
        c = dbase.cursor()
        c.execute('''SELECT NAMED from Log''')
        data = c.fetchall()
        dbase.commit()
        return data