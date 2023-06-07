import sqlite3
con = sqlite3.connect('test.db')
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())

sql_fetch(con)
