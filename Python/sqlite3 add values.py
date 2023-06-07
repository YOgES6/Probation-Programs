import sqlite3

conn=sqlite3.connect("test.db")
print("Database opened...")
print(conn.total_changes)

cursor=conn.cursor()
cursor.execute("""INSERT INTO MARK VALUES('Yogesh',10,450)""")
cursor.execute("""INSERT INTO MARK VALUES('Deva',10,480)""")
conn.commit()
print("Records added")
conn.close()
