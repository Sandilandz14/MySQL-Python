from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

def register():

    import register
    register.register()

def admin():

        import admin
        admin.admin()

def logging():
    # messagebox.showinfo("GOOD","You've loged successfully")
    import loginpage
    loginpage.verify()

def landing():

    my_window = Tk()
    my_window.title("Lifechoices Management System: ")
    my_window.geometry("450x450")

    label_heading = tk.Label(my_window,text="Welcome to LifeChoices.")
    label_heading.place(x=115,y=50)

    label_heading = tk.Label(my_window,text="Please select your option:")
    label_heading.place(x=115,y=70)

    mybutton = Button(my_window,text="Login",command=logging,width=15, fg="blue",bg="black")
    mybutton.place(x=50,y=100)
    mybutton2 = Button(my_window,text="Register",command=register,fg="blue",bg="black", width=15)
    mybutton2.place(x=200,y=100)
    mybutton3 = Button(my_window,text="Admin",command=admin,fg="blue",bg="black", width=15)
    mybutton3.place(x=130,y=130)
    mybutton4 = Button(my_window,text="Exit",command=exit,fg="blue",bg="black", width=18)
    mybutton4.place(x=120,y=170)


    my_window.mainloop()
landing()

