import tkinter
from tkinter import *
import tkinter.messagebox
import os
import sys


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("800x480")
        self.bg = PhotoImage(file="bckgrd.png")
        label1 = Label(root, image=self.bg)
        label1.place(x=0, y=0)

        # =======login======
        Frame_login = Frame(self.root, bg="blue")
        Frame_login.place(x=150, y=75, height=340, width=500)

        title = Label(Frame_login, text="SECURITY", font=("Impact", 35, "bold"), fg="white", bg="blue").place(x=190, y=30)
        desc = Label(Frame_login, text="Admin Login", font=("goudy old style", 15), fg="black",
                     bg="blue").place(x=190, y=90)
        desc1 = Label(Frame_login, text="USERNAME", font=("goudy old style", 10), fg="gray", bg="white").place(x=125,
                                                                                                               y=131)
        self.txt_user = Entry(Frame_login, font=("times new roman", 10), fg="gray", bg="white")
        self.txt_user.place(x=200, y=130, width=120, height=23)

        # password
        desc2 = Label(Frame_login, text="PASSWORD", font=("times new roman", 10), fg="gray", bg="white").place(x=125,y=161)
        self.txt_pass = Entry(Frame_login, font=("nymphette", 10), fg="gray", bg="white")
        self.txt_pass.place(x=200, y=160, width=120, height=23)

        forget=tkinter.Button(self.root,command=self.login_function2,text="FORGET PASSWORD ?", bg="white", fg="black",font=("times new roman", 5)).place(x=335, y=265)
        login=tkinter.Button(self.root,command=self.login_function,text="LOGIN", bg="yellow", fg="black",font=("times new roman", 10)).place(x=350, y=285)

    def login_function(self):
        if  self.txt_pass.get()=="" or self.txt_user.get()=="":
            tkinter.messagebox.showerror("Error","Please enter login details",parent=self.root)
        elif self.txt_pass.get()== "cse2021" and self.txt_user.get()=="admin":
                tkinter.messagebox.showinfo("login suscess","continue",parent=self.root)
                os.system('yesno.py')
                
        elif self.txt_pass.get()!= "admin" or self.txt_user.get()!="user":
                tkinter.messagebox.showerror("ERROR", "wrong username/password", parent=self.root)


        
        else:
             tkinter.messagebox.showinfo("login suscess","continue",parent=self.root)
             os.system('yesno.py')
    def login_function2(self):
        if  self.txt_pass.get()=="" or self.txt_user.get()=="":
            tkinter.messagebox.showerror("Error","Entering to recovery login",parent=self.root)
            print('Entering to recovery')
            os.system('rec.py')
            



root = Tk()
obj = login(root)
root.mainloop()
