from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

mydb = mysql.connector.connect(
    host= "127.0.0.1",
    password= "@Lifechoices1234",
    user= "lifechoices",
    database= "students",
    auth_plugin = "mysql_native_password",
)

mycursor = mydb.cursor()

def verify():
    user = Entry1.get()
    passs = Entry2.get()
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
    messagebox.showinfo("Successful","Login successful, Enjoy! Enjoy your day. Press ok to proceed")

    window.destroy()

def failed():
    messagebox.showerror("WARNING","You have entered invalid info. Please try again")

    window.destroy()



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

mybutton = Button(window,text="Login",command=logged, fg="blue",bg="black")
mybutton.place(x=135,y=60)
mybutton = Button(window,text="Register",fg="blue",bg="black")
mybutton.place(x=200,y=60)




window.mainloop()
verify()

    #
    # labelframe1 = LabelFrame(myWindow,text="Celsius To Fahrenheit", padx=40, pady=40)
    # labelframe1.pack(fill="both")
    # labelframe1.place(x=100,y=10)
    #
    #
    # Celsius_entry=Entry(labelframe1)
    # Celsius_entry.configure(state="disable")
    # Celsius_entry.pack(side=LEFT)
    #
    # labelframe2 = LabelFrame(myWindow,text="Fahrenheit To Celsius", padx=40, pady=40)
    # labelframe2.pack(fill="both")
    # labelframe2.place(x=350,y=10)
    # Fahrenheit_entry = Entry(labelframe2)
    # Fahrenheit_entry.configure(state="disable")
    # Fahrenheit_entry.pack(side=RIGHT)
