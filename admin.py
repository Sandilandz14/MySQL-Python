from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk


root = Tk()
root.title("Lifechoices Management System: ")
root.geometry("400x400")
#
# #Creating Entries for name
# name = tk.Label(root,text="Enter Name: ")
# name.place(x=25, y=1)
# Entry1 = Entry(root)
# Entry1.place(x=135, y=1)
#
# #Creating Entries for surname
# surname = tk.Label(root,text="Enter Surname: ")
# surname.place(x=25, y=29)
# Entry2 = Entry(root)
# Entry2.place(x=135, y=29)
#
#
# #Creating Entries for cell
# mobile = tk.Label(root,text="Enter Cell: ")
# mobile.place(x=25, y=60)
# Entry3 = Entry(root)
# Entry3.place(x=135, y=60)

#Creating Entries for username
username = tk.Label(root,text="Enter Username: ")
username.place(x=25, y=10)
Entry4 =Entry(root)
Entry4.place(x=136, y=10)

#Creating Entries for password
password = tk.Label(root, text="Enter Password: ")
password.place(x=25, y=40)
Entry5 = Entry(root)
Entry5.place(x=135, y=40)

# def logging():
#     import adminfunc
#     adminfunc.
#     pass

def new_user():
    import adminfunc
    adminfunc.my_new_user()

def my_delete():
    import adminfunc
    adminfunc.remove()



#     import adminfunc
#     adminfunc.update()
#
# def insert():
#     import adminfunc
#     adminfunc.my_insert()

def back():
    root.destroy()

mybutton1 = Button(root, text="Login", command=new_user, fg="green", bg="black", width=20).place(x=120,y=80)
# mybutton2 = Button(root, text="Delete User", command=my_delete, fg="green", bg="black", width=20).place(x=120,y=110)
# mybutton3 = Button(root, text="Time Data", command=showtime, fg="green", bg="black", width=20).place(x=120,y=140)
mybutton4 = Button(root, text="Register", command=register, fg="green", bg="black", width=20)
mybutton4.place(x=120,y=140)
mybutton6 = Button(root, text="Go Back", command=back, fg="green", bg="black", width=15)
mybutton6.place(x=139,y=110)
root.mainloop()
