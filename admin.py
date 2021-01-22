from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

root = Tk()
root.title("Lifechoices Management System: ")
root.geometry("400x400")

#Creating Entries for name
name = tk.Label(root,text="Enter Name: ")
name.place(x=25, y=1)
Entry1 = Entry(root)
Entry1.place(x=135, y=1)

#Creating Entries for surname
surname = tk.Label(root,text="Enter Surname: ")
surname.place(x=25, y=29)
Entry2 = Entry(root)
Entry2.place(x=135, y=29)


#Creating Entries for cell
mobile = tk.Label(root,text="Enter Cell: ")
mobile.place(x=25, y=60)
Entry3 = Entry(root)
Entry3.place(x=135, y=60)

#Creating Entries for username
username = tk.Label(root,text="Enter Username: ")
username.place(x=25, y=90)
Entry4 =Entry(root)
Entry4.place(x=136, y=90)

#Creating Entries for password
password = tk.Label(root, text="Enter Password: ")
password.place(x=25, y=120)
Entry5 = Entry(root)
Entry5.place(x=135, y=120)

def new_admin():
    pass

def back():
    root.destroy()

mybutton = Button(root, text="Register New Admin", command=new_admin, fg="blue", bg="black", width=15)
mybutton.place(x=145,y=160)
mybutton = Button(root, text="Go Back", command=back, fg="blue", bg="black", width=15)
mybutton.place(x=145,y=190)
root.mainloop()
