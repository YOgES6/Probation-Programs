import sqlite3

conn=sqlite3.connect("Hotel.db")
conn.execute("""CREATE TABLE DETAILS(Name TEXT,Mobile REAL,Address CHAR(80),Checkin CHAR(80),Checkout CHAR(80));""")
conn.close()

print("Table created...")
