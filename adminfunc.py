from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

root = Tk()
root.title("Lifechoices Management System: Admin")
root.geometry("400x400")

label1 = tk.Label(root,text="Enter Full name:").place(x=15,y=10)
Entry1 = Entry(root).place(x=140,y=10)
label2 = tk.Label(root,text="Enter Username:").place(x=15,y=40)
Entry2 = Entry(root).place(x=140,y=40)
label3 = tk.Label(root,text="Enter Password:").place(x=15,y=70)
Entry3 = Entry(root).place(x=140,y=70)

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



mybutton1 = Button(root,text="Add User",command=my_new_user, fg="green",bg="black", width=15).place(x=150,y=120)
mybutton2 = Button(root,text="Go Back",command=back, fg="green",bg="black", width=15).place(x=150,y=150)
mybutton3 = Button(root,text="Logout",command=logout, fg="green",bg="black", width = 15).place(x=150,y=185)
root.mainloop()
