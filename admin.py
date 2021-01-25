from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
import os

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    password = "@Lifechoices1234",
    user = "lifechoices",
    database = "students",
    auth_plugin = "mysql_native_password",
)

mycursor = mydb.cursor()

window = Tk()
window.title("Admin Login")
window.geometry("450x450")

user = StringVar
passs = StringVar
#Creating Entries for username and password
label_user = tk.Label(window,text="Enter Fullname:")
label_user.place(x=25,y=1)
Entry1 = Entry(window).place(x=135,y=1)

label_user = tk.Label(window,text="Enter Username:")
label_user.place(x=25,y=30)
Entry2 = Entry(window).place(x=135,y=30)

password = tk.Label(window,text="Enter Password:")
password.place(x=25,y=29)
Entry3 =Entry(window).place(x=136,y=60)

def main_admin():

    user  = Entry1.get()
    password = Entry2.get()
    sql = "select * from Admin where Username = %s and Password = %s"
    mycursor.execute(sql,(user, password))
    results = mycursor.fetchall()

    if results:
        messagebox.showinfo("Successful","Login successful, Enjoy! Enjoy your day. Press ok to proceed")
    else:
        failed()

def failed():
    messagebox.showerror("WARNING","You have entered invalid info. Please try again")
    window.destroy()
def register():
    import adminreg
    adminreg.myregister()

def remove():
    a = Entry1.get()
    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    password = "@Lifechoices1234",
    user = "lifechoices",
    database = "students")

    mycursor = mydb.cursor()
    delete = "delete from Login where Username = '%s'" %(a)
    mycursor.execute(delete)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted")

def update():

    b = Entry1.get()
    c = Entry2.get()
    d = Entry3.get()

    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    password = "@Lifechoices1234",
    user = "lifechoices",
    database = "students")

    mycursor = mydb.cursor()
    my_update = "UPDATE Login SET Fullname = '%s', Username = '%s' WHERE Password = '%s'" %(b,c,d)
    mycursor.execute(my_update)
    mydb.commit()


def back():
    window.destroy()

def logout():
    return os.system("shutdown -l")



# mybutton1 = Button(window,text="Login", fg="green",bg="black", width=20).place(x=135,y=65)
mybutton2 = Button(window,text="Register",command=register, fg="green",bg="black", width=20).place(x=135,y=95)
mybutton3 = Button(window,text="Delete",command=remove, fg="green",bg="black",width=20).place(x=135,y=125)
mybutton5 = Button(window,text="Update",command=update, fg="green",bg="black",width=20).place(x=135,y=155)
mybutton6 = Button(window,text="Go Back",command=back, fg="green",bg="black",width=20).place(x=135,y=185)
mybutton7 = Button(window,text="Logout",command=logout, fg="green",bg="black", width=20).place(x=135,y=215)

window.mainloop()

