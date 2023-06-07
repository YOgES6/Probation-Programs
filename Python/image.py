import sqlite3
import pickle

conn=sqlite3.connect('test.db')
row=conn.execute("""SELECT * FROM docs Data""")
f=open("fit1.jpg","wb")
for i in row:
    pickle.dump(i,f)
