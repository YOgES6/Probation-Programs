import sqlite3
  
conn=sqlite3.connect("test.db")
print("Database opened...")
print(conn.total_changes)

cursor=conn.cursor()
cursor.execute("""CREATE TABLE images(data BLOB)""")
conn.commit()
print("\nTable created...")
conn.close()               
