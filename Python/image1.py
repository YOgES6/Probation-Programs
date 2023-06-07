import sqlite3

def readData():
    fl = open('fortnite.jpg', 'rb')
    with fl:
        data = fl.read()
    return data


con = sqlite3.connect('test.db')
with con:
     cur = con.cursor()     
     cur.execute("CREATE TABLE IF NOT EXISTS docs(Data BLOB)")
     data = readData()

     sql = "INSERT INTO docs(Data) VALUES (?)" 
     cur.execute(sql, (sqlite3.Binary(data), ))
