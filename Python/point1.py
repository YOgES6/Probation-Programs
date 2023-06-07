import sqlite3
import sys


def writeImage(data):

    fout = None

    try:
        fout = open('fight.jpg','wb')
        fout.write(data)

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fout:
            fout.close()

con = None

try:
    con = sqlite3.connect('test.db')

    cur = con.cursor()
    cur.execute("SELECT data FROM images LIMIT 1")
    con.commit()
    data = cur.fetchone()[1]

    writeImage(data)


except sqlite3.Error as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
