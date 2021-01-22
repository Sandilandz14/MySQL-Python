from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    password = "@Lifechoices1234",
    user = "lifechoices",
    database = "students",
    auth_plugin = "mysql_native_password",
)

mycursor = mydb.cursor()

window = Tk()
window.title("Login")
window.geometry("450x450")

#Creating Entries for username and password
label_user = tk.Label(window,text="Enter Username:")
label_user.place(x=25,y=1)
Entry1 = Entry(window)
Entry1.place(x=135,y=1)

password = tk.Label(window,text="Enter Password:")
password.place(x=25,y=29)
Entry2 =Entry(window)
Entry2.place(x=136,y=29)
user = Entry1.get()
passs = Entry2.get()

##I NEED TO GET THIS WORKING NOW
def verify():
    sql = "select * from Login where user = %s and password = %s"
    mycursor.execute(sql,[(user),(passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    if (user==" " and passs==" "):
        messagebox.showinfo("Error message","Please enter the required information")
        # window=None
    else:
        messagebox.showinfo("Successful","Login successful, Enjoy! Enjoy your day. Press ok to proceed")
    # window.destroy()


def failed():
    messagebox.showerror("WARNING","You have entered invalid info. Please try again")

    window.destroy()
def back():
    window.destroy()


mybutton = Button(window,text="Login",command=logged, fg="blue",bg="black")
mybutton.place(x=175,y=60)
mybutton2 = Button(window,text="Go Back",command=back, fg="blue",bg="black")
mybutton2.place(x=165,y=95)


window.mainloop()
# verify()


