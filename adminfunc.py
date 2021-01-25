from tkinter import *
import mysql.connector as mysql
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from datetime import *
import datetime as dt


root = Tk()
root.title("Lifechoices Management System: Admin")
root.geometry("400x400")

Entry1 = StringVar()
Entry2 = StringVar()
Entry3 = StringVar()

label1 = tk.Label(root,text="Enter Full name:").place(x=15,y=10)
Entry1 = Entry(root,textvariable = Entry1).place(x=140,y=10)
label2 = tk.Label(root,text="Enter Username:").place(x=15,y=40)
Entry2 = Entry(root,textvariable = Entry2).place(x=140,y=40)
label3 = tk.Label(root,text="Enter Password:").place(x=15,y=70)
Entry3 = Entry(root,textvariable = Entry3).place(x=140,y=70)

# def my_new_user():
#     if (fname == " ") and (uname == " ") and (pword == " "):
#         messagebox.showinfo("Error","Please complete all information")
#     else:
#         messagebox.showinfo("Success!","New user added successfully.")

def my_new_user():
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



def remove():
    pass

def update():
    pass

def back():
    root.destroy()

def logout():
    exit()

def showtime():
    w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="green", bg="black", font=("helvetica", 40))
    messagebox.showinfo("Date and Time",w)


# mybutton1 = Button(root,text="Add New User",command=my_new_user, fg="green",bg="black", width=15).place(x=150,y=120)
# mybutton2 = Button(root,text="Go Back",command=back, fg="green",bg="black", width=15).place(x=150,y=150)
#


mybutton1 = Button(root, text="Add New User", command=my_new_user, fg="green", bg="black", width=20).place(x=140,y=120)
mybutton2 = Button(root, text="Delete User", command=remove, fg="green", bg="black", width=20).place(x=140,y=150)
mybutton3 = Button(root, text="Time Data", command=showtime, fg="green", bg="black", width=20).place(x=140,y=180)
mybutton5 = Button(root,text="Logout",command=logout, fg="green",bg="black", width = 15).place(x=160,y=210)
mybutton5 = Button(root, text="Go Back", command=back, fg="green", bg="black", width=15).place(x=160,y=310)
root.mainloop()
