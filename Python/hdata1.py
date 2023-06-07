import sqlite3
  
conn=sqlite3.connect("Hotel.db")
conn.execute("""CREATE TABLE HINT(Name TEXT,Mobile CHAR(80),Room CHAR(80));""")
conn.close()

print("Table created...")
