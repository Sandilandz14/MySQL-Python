from tkinter import *
import mysql.connector
import mysql.connector as mysql
from tkinter import messagebox
import tkinter as tk
import os

root = Tk()
root.title("Lifechoices Management System: ")
root.geometry("400x400")

#Creating Entries for name
name = tk.Label(root,text="Enter Fullname: ")
name.place(x=25, y=11)
Entry1 = Entry(root)
Entry1.place(x=135, y=11)


#Creating Entries for username
username = tk.Label(root,text="Enter Username: ")
username.place(x=25, y=45)
Entry2 =Entry(root)
Entry2.place(x=136, y=45)

#Creating Entries for password
password = tk.Label(root, text="Enter Password: ")
password.place(x=25, y=75)
Entry3 = Entry(root)
Entry3.place(x=135, y=75)



def myregister():
    fnm = Entry1.get()
    usn = Entry2.get()
    pwd = Entry3.get()

    sql_var = mysql.connect(host="localhost",
    password = "@Lifechoices1234",
    user = "lifechoices",
    database = "students")

    cursor = sql_var.cursor()
    sql = "INSERT INTO Login(Fullname, Username, Password) VALUES (%s, %s, %s)"
    values = (fnm, usn, pwd)
    cursor.execute(sql,values)
    sql_var.commit()

    Entry1.delete(0,END)
    Entry2.delete(0,END)
    Entry3.delete(0,END)

    if (Entry1 != "") and (Entry2 != "") and (Entry3 != ""):
        messagebox.showinfo("Success!","You've registered successfully. Go back to login.")
    elif (Entry1 != "") and (Entry2 != "") and (Entry3 != ""):
        messagebox.showerror("Fatal!","Please enter valid information.")


def myback():
    root.destroy()

mybutton = Button(root, text="Register", command=myregister, fg="blue", bg="black", width=15)
mybutton.place(x=145,y=110)
mybutton = Button(root, text="Back", command=myback, fg="blue", bg="black", width=15)
mybutton.place(x=145,y=140)
root.mainloop()
