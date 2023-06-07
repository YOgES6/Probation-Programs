import sys
import sqlite3

connection=sqlite3.connect("hotel.db")

cursor=connection.cursor()
row=cursor.execute("SELECT * FROM HINT").fetchall()
print(row)
