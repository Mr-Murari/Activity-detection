import tkinter
from tkinter import *
import tkinter.messagebox
import os
import sys


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("800x500")
        self.bg = PhotoImage(file="bckgrd.png")
        label1 = Label(root, image=self.bg)
        label1.place(x=0, y=0)

        # =======login======
        Frame_login = Frame(self.root, bg="red")
        Frame_login.place(x=150, y=75, height=340, width=500)

        title = Label(Frame_login, text="PASSWORD RECOVERY", font=("Impact", 25, "bold"), fg="white", bg="red").place(x=110, y=30)
        desc = Label(Frame_login, text="USER-LOGIN", font=("goudy old style", 15), fg="black",
                     bg="red").place(x=190, y=90)
        desc1 = Label(Frame_login, text="MOBILE.NO", font=("goudy old style", 10), fg="gray", bg="white").place(x=125,
                                                                                                               y=131)
        self.txt_user = Entry(Frame_login, font=("times new roman", 10), fg="gray", bg="white")
        self.txt_user.place(x=200, y=130, width=120, height=23)

        # password
        desc2 = Label(Frame_login, text="USERID", font=("goudy old style", 10), fg="gray", bg="white").place(x=125,y=161)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 10), fg="gray", bg="white")
        self.txt_pass.place(x=200, y=160, width=120, height=23)
        
        login=tkinter.Button(self.root,command=self.login_function,text="RECOVER", bg="yellow", fg="black",font=("times new roman", 10)).place(x=350, y=285)

    def login_function(self):
        if  self.txt_pass.get()=="" or self.txt_user.get()=="":
            tkinter.messagebox.showerror("Error","Please enter login details",parent=self.root)
        elif self.txt_pass.get()== "admin" and self.txt_user.get()=="9182439144":
            tkinter.messagebox.showinfo("login suscess", "username:user & password:admin", parent=self.root)
            
        elif self.txt_pass.get()!= "MURARI" or self.txt_user.get()!="9652192129":
                tkinter.messagebox.showerror("ERROR", "wrong username/password", parent=self.root)
        else:
            tkinter.messagebox.showinfo("details","username:admin & password:cse2021",parent=self.root)
             
    
root = Tk()
obj = login(root)
root.mainloop()

