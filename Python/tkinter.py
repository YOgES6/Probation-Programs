import tkinter as tk
from tkinter import *

root=Tk()
menubar=tk.Tk()
root.geometry("700x800")
c=Canvas(root,height="100",width=100)

def hello():
    print("Hello!")

name=Label(root,text="Username").place(x=20,y=48)
e1=Entry(root).place(x=100,y=48)
password=Label(root,text="Password").place(x=20,y=98)
e2=Entry(root).place(x=100,y=96)
submit=Button(root,text="SUBMIT",fg="black",activeforeground="blue").place(x=124,y=160)

menubar.add_command(label="Hello!",command=hello)
menubar.add_command(label="Quit!",command=root.quit)

root.config(menu=menubar)
c.pack()
root.mainloop() 
