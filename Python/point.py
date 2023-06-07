import sqlite3
import sys

def readImage():
    fin=None

    try:
       fin=open("fortnite.jpg","rb")
       img=fin.read()
       return img

    except IOError as e:
           print(e)
           sys.exit(1)
    
    finally:
           if fin:
              fin.close()

con=None

try:
   con=sqlite3.connect('new.db') 
   cur=con.cursor()
   data=readImage()
   binary=sqlite3.Binary(data)
   cur.execute("""INSERT INTO images1(data) VALUES ("new.jpg")""") 
   con.commit()

except sqlite3.Error as e:
       if con:
             con.rollback()

       print(e)
       sys.exit(1)

finally:
       if con:
             print("Done...") 
             con.close()
