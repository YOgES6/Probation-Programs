import sys
import random,sqlite3
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  
conn=sqlite3.connect("Hotel.db")
num=random.randint(200,500)
print("\n1.Booking\n2.Rooms info\n3.Room Service(Menu card)\n4.Payment\n5.Record\n6.Check Room\n7.Cancel request\n\n0 For EXIT\n")

p=input("\nSELECT__")

if p=='1':
   cursor=conn.cursor()
   row=cursor.execute("SELECT Checkin,Checkout FROM DETAILS").fetchall()
   print("\n")
   for i in row:
       print(i[0])
       print(i[1])
   print("Above listed dates are already booked...")
   print("Booking___\n")
   p1=input("Name: ")
   p2=input("Mobile:")
   p3=input("Address:")
   p4=input("Check-IN:")
   p5=input("Check-OUT:")
  
   if ((i[0]==p4) and (i[1]==p5)):
      print("Sorry,given dates are already booked")
      exit()
   conn.execute("""INSERT INTO DETAILS(Name,Mobile,Address,Checkin,Checkout) VALUES (?,?,?,?,?)""",(p1,p2,p3,p4,p5))
   conn.commit()
   print("Details added successfully...") 
   print("\n\nSelect room type--\n")
   print("\n1.Standard Non-AC\n\n2.Standard AC\n\n3.3-Bed Non-AC\n\n4.3-Bed AC\n\n0 for Room Prices...\n\n($)To generate room number:")

   print("\nDate and time:",dt_string)  
   s=input("SELECT: ")
   if s=='0':
      print("\n1.Standard Non-AC=3000/day\n\n2.Standard AC=4000/day\n\n3.3-Bed Non-AC=6000/day\n\n4.3-Bed AC=8000/day\n\n")
   if s=='$':
      print("Your room number:",num)
      print("Welcome...")
      conn.execute("""INSERT INTO HINT(Name,Mobile,Room) VALUES (?,?,?)""",(p1,p2,num))
      conn.commit()
if p=='2':
   print("\nRooms info...\n")
   print("\n1.Standard Non-AC=3000/day.(Balcony with accent table,1 Television,1 Telephone,1 sofa,1 bedroom)\n\n2.Standard AC=4000/day(Balcony,1 Television,1 Telephone,2 sofa(in hall),1 bedroom)\n\n3.3-Bed Non-AC=6000/day(Balcony,2 Television(in hall,left bedroom),2 Telephone(in hall,bedroom),2 sofa,1 double bed + single bed)\n\n4.3-Bed AC=8000/day(Balcony,2 Television(in hall,left bedroom),2 Telephone(in hall,bedroom),2 sofa,1 double bed + single bed\n\n")


if p=='4':
   print("\n1.Standard Non-AC\n2.Standard AC\n3.3-Bed Non-AC\n4.3-Bed AC\n")
   s1=input("Select room type:")
   s2=input("Enter number of days:")
   if s1=='1':  
      s3=int(s2)*3000
      print("\ntotal amount Rs:",s3)
      print("\nThank you...visit again")
   if s1=='2':
      s3=int(s2)*4000
      print("\nTotal amount Rs:",s3)
      print("\nThank you...visit again")
   if s1=='3':
      s3=int(s2)*6000
      print("\nTotal amount Rs:",s3)
      print("\nThank you...visit again")
   if s1=='4':
      s3=int(s2)*8000
      print("\nTotal amount Rs:",s3)
      print("\nThank you...visit again")

if p=='5':
   p20=input("Enter your name given while booking:")
   try:
      r_set=row=conn.execute("SELECT * FROM DETAILS WHERE Name=?",(p20,)).fetchall()
      for i in row:
          print(i)
          print("\n")
   except sqlite3.OPerationalError:
                                  exists=false

if p=='6':
   y=input("\nEnter Name:")
   cursor=conn.cursor()
   row=cursor.execute("SELECT * FROM HINT WHERE Name=?",(y,)).fetchall()
   for i in row:
       print(i)
   print("\n",dt_string)

if p=='7':
   y1=input("Enter your name:")
   y2=input("Enter your mobile number:")
   y3=input("Reason...:") 
   try: 
      r_set=conn.execute("DELETE FROM DETAILS WHERE Name=? AND Mobile=?",(y1,y2))  
      conn.commit() 
      print("Your booking get canceled...")

   except TypeError:
                   print("No such data exist") 
if p=='0':
   exit()
