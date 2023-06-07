import sqlite3

s=400
p="Yogesh"
conn=sqlite3.connect("test.db")
print("Database opened...")
print(conn.total_changes)

cursor=conn.cursor()
cursor.execute("UPDATE MARK SET Mark=? WHERE Name=?",(s,p))
conn.commit()
print("Records added")
conn.close()  
