# Likho Kapesi

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mb
from tkinter.ttk import Combobox
from datetime import datetime


import mysql.connector  # mysql connector imported
conn = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
# done with db connection
cursor = conn.cursor(buffered=True)


class LoginApp(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("Life Choices Online")
       self.geometry("900x900")
       self.render = Image.open("LIFE-CHOICES-ICON-ON-GREEN.jpg")
       self.loader = ImageTk.PhotoImage(self.render)
       self.img = tk.Label(self, image=self.loader)
       self.img.place(x=0, y=0)
       self.lblHeading = tk.Label(self, text="Welcome to Login Page", font=("sans-serif", 16), bg="blue", fg="white")
       self.lbluname = tk.Label(self, text="Enter UserName:", font=("sans-serif", 10), bg="blue", fg="white")
       self.lblpsswd = tk.Label(self, text="Enter Password:", font=("sans-serif", 10), bg="blue", fg="white")
       self.txtuname = tk.Entry(self, width=60)
       self.txtpasswd = tk.Entry(self, width=60, show="*")
       self.btn_login = tk.Button(self, text="Login", font=("sans-serif", 11), bg="green", fg="black", command=self.login)
       self.btn_clear= tk.Button(self, text="Clear", font=("sans-serif", 11), bg="green", fg="black", command=self.clear_form)
       self.btn_register = tk.Button(self, text="Not Member ? Register", font=("sans-serif", 11), bg="blue", fg="yellow",  command=self.open_registration_window)
       self.btn_exit = tk.Button(self, text="Exit", font=("sans-serif", 14), bg="red", fg="black", command=self.exit)
       self.admin = tk.Button(self, text="Administrator", font=("sans-serif", 11), bg="blue", fg="white", command=self.admin_management)
       self.lblHeading.place(relx=0.35, rely=0.089, height=50, width=300)
       self.lbluname.place(relx=0.235, rely=0.289, height=21, width=120)
       self.lblpsswd.place(relx=0.242, rely=0.378, height=21, width=120)
       self.txtuname.place(relx=0.417, rely=0.289, height=20, relwidth=0.273)
       self.txtpasswd.place(relx=0.417, rely=0.378, height=20, relwidth=0.273)
       self.btn_login.place(relx=0.45, rely=0.489, height=24, width=52)
       self.btn_clear.place(relx=0.54, rely=0.489, height=24, width=72)
       self.btn_register.place(relx=0.695, rely=0.489, height=24, width=175 )
       self.btn_exit.place(relx=0.75, rely=0.911, height=24, width=61)
       self.admin.place(relx=0.15, rely=0.911, height=34, width=120)

   def open_registration_window(self):
       self.withdraw()
       window = RegisterWindow(self)
       window.grab_set()

   def show(self):
       """"""
       self.update()
       self.deiconify()

   def login(self):
        my_db = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="lifechoicesonline", auth_plugin="mysql_native_password")
        my_cursor = my_db.cursor()
        my_cursor.execute("select * from users")

        for i in my_cursor:
            if self.txtuname.get() == i[0] and self.txtpasswd.get() == i[0]:
                date = datetime.now().date().strftime("%Y-%m-%d")
                time = datetime.now().time().strftime("%H:%M:%S")
                insert = "INSERT INTO login (username, password, login_date, login_time, logout_time) VALUES (%s, %s, %s, %s, %s)"
                entries = (self.txtuname.get(), self.txtpasswd.get(), date, time, time, "")
                my_cursor.execute(insert, entries)
                my_db.commit()
                mb.showinfo("Login Successful", "Enjoy your day")

                break

        if self.txtuname.get() == "" or self.txtpasswd.get() == "":
            mb.showerror("No Entries", "Please enter Username and Password")
        elif self.txtpasswd.get() != [3] or self.txtpasswd.get() != [5]:
            mb.showerror("Access Denied", "Incorrect Username or Password")
            self.txtuname.delete(0, END)
            self.txtpasswd.delete(0, END)

   def clear_form(self):
    self.txtuname.delete(0, tk.END)
    self.txtpasswd.delete(0, tk.END)
    self.txtuname.focus_set()

   def exit(self):
    MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        self.destroy()

   def admin_management(self):
       ask = mb.askquestion("Life Choices Online Administrator", "This is only for Admin, if you're not please be advised to login in utilizing the general page")
       if ask == "yes":
           self.withdraw()
           import admin


# Using Toplevel widget to create a new window named RegisterWindow to register a new user
class RegisterWindow(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("800x700")
         self.title("Register")
         self.geometry("900x900")
         self.render = Image.open("LIFE-CHOICES-ICON-ON-GREEN.jpg")
         self.loader = ImageTk.PhotoImage(self.render)
         self.img = tk.Label(self, image=self.loader)
         self.img.place(x=0, y=0)

         self.Registerlbl = tk.Label(self, text="Register", font=("sans-serif", 16), bg="blue", fg="white")
         self.Fnamelbl = tk.Label(self, text="Enter Name:", font=("sans-serif", 10), bg="blue", fg="white")
         self.Snamelbl = tk.Label(self, text="Enter Surname:", font=("sans-serif", 10), bg="blue", fg="white")
         self.idlbl = tk.Label(self, text="Enter ID Number:", font=("sans-serif", 10), bg="blue", fg="white")
         self.phonelnl = tk.Label(self, text="Enter Phone Number:", font=("sans-serif", 10), bg="blue", fg="white")
         self.emaillbl = tk.Label(self, text="Enter Email:", font=("sans-serif", 10), bg="blue", fg="white")
         self.next_of_kinlbl = tk.Label(self, text="Enter Next of kin:", font=("sans-serif", 10), bg="blue", fg="white")
         self.next_of_kin_celllbl = tk.Label(self, text="Enter Next of Kin Number:", font=("sans-serif", 10), bg="blue", fg="white")
         self.passwdlbl = tk.Label(self, text="Enter Password:", font=("sans-serif", 10), bg="blue", fg="white")

         self.txtFName = tk.Entry(self)
         self.txtLName = tk.Entry(self)
         self.txtUId = tk.Entry(self)
         self.txtphone = tk.Entry(self)
         self.txtemail = tk.Entry(self)
         self.txtgender = tk.Entry(self)
         self.txtNextofkin = tk.Entry(self)
         self.txtNextofkinC = tk.Entry(self)
         self.txtpasswd = tk.Entry(self)

         self.btn_register = tk.Button(self, text="Register", font=("sans-serif", 11), bg="green", fg="white", command=self.register)
         self.back_to_login_btn = tk.Button(self, text="Back To Login", font=("sans-serif", 11), bg="red", fg="white", command=self.onClose)
         self.clear_btn = tk.Button(self, text="Clear", font=("sans-serif", 11), bg="red", fg="white", command=self.clear_form)

         self.Registerlbl.place(relx=0.467, rely=0.111, height=30, width=100)
         self.Fnamelbl.place(relx=0.318, rely=0.2, height=21, width=100)
         self.Snamelbl.place(relx=0.319, rely=0.267, height=21, width=100)
         self.idlbl.place(relx=0.240, rely=0.333, height=21, width=190)
         self.phonelnl.place(relx=0.300, rely=0.4, height=21, width=150)
         self.emaillbl.place(relx=0.310, rely=0.467, height=21, width=105)
         self.next_of_kinlbl.place(relx=0.262, rely=0.533, height=21, width=160)
         self.next_of_kin_celllbl.place(relx=0.212, rely=0.6, height=21, width=170)
         self.passwdlbl.place(relx=0.300, rely=0.740, height=21, width=160)
         self.txtFName.place(relx=0.490, rely=0.2, height=20, relwidth=0.223)
         self.txtLName.place(relx=0.490, rely=0.267, height=20, relwidth=0.223)
         self.txtUId.place(relx=0.490, rely=0.333, height=20, relwidth=0.223)
         self.txtphone.place(relx=0.490, rely=0.4, height=20, relwidth=0.223)
         self.txtemail.place(relx=0.490, rely=0.467, height=20, relwidth=0.223)
         self.txtNextofkin.place(relx=0.490, rely=0.533, height=20, relwidth=0.223)
         self.txtNextofkinC.place(relx=0.490, rely=0.6, height=20, relwidth=0.223)
         self.btn_register.place(relx=0.300, rely=0.880, height=24, width=75)
         self.back_to_login_btn.place(relx=0.405, rely=0.880, height=24, width=160)
         self.clear_btn.place(relx=0.600, rely=0.880, height=24, width=90)
         self.txtpasswd.place(relx=0.490, rely=0.740, height=20, relwidth=0.223)
         self.rolelbl = Label(self, text='Registering As:')
         self.rolelbl.place(relx=0.240, rely=0.664, height=20, relwidth=0.223)
         self.roleset = StringVar(self)
         self.roleset.set("Select your role")
         self.rolecombolist = ['Lecture', 'Staff', 'Student', 'Visitor']
         self.roleselector = Combobox(self, textvariable=self.roleset)
         self.roleselector['values'] = self.rolecombolist
         self.roleselector['state'] = 'readonly'
         self.roleselector.place(relx=0.490, rely=0.664, height=20, relwidth=0.223)

         self.rolelbl2 = Label(self, text='Gender Category :')
         self.rolelbl2.place(relx=0.240, rely=0.800, height=20, relwidth=0.223)
         self.roleset2 = StringVar(self)
         self.roleset2.set("Select your gender")
         self.rolecombolist2 = ['Female', 'Male', 'Other']
         self.roleselector2 = Combobox(self, textvariable=self.roleset2)
         self.roleselector2['values'] = self.rolecombolist2
         self.roleselector2['state'] = 'readonly'
         self.roleselector2.place(relx=0.490, rely=0.800, height=20, relwidth=0.223)

   def register(self):
       self.conn = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)

       fname = self.txtFName.get()  # Retrieving entered first name
       lname = self.txtLName.get()  # Retrieving entered last name
       uid = self.txtUId.get()  # Retrieving entered user id
       phone = self.txtphone.get()  # Retrieving entered password
       email = self.txtemail.get()  # Retrieving entered contact number
       next_of_kin = self.txtNextofkin.get()  # Retrieving entered city name
       next_of_kin_cell = self.txtNextofkinC.get()  # Retrieving entered state name
       role = self.roleset.get()
       passwd = self.txtpasswd.get()
       gender = self.roleset2.get()
       # validating Entry Widgets
       if fname == "":
           mb.showinfo('Information', "Please Enter Firstname")
           self.txtFName.focus_set()
           return
       if lname == "":
           mb.showinfo('Information', "Please Enter Surname")
           self.txtLName.focus_set()
           return
       if uid == "":
           mb.showinfo('Information', "Please Enter User ID Number")
           self.txtUId.focus_set()
           return
       if phone == "":
           mb.showinfo('Information', "Please Enter Phone Number")
           self.txtphone.focus_set()
           return

       if email == "":
           mb.showinfo('Information', "Please Enter Email Address")
           self.txtemail.focus_set()
           return
       if next_of_kin == "":
           mb.showinfo('Information', "Please Enter Next of Kin Name")
           self.txtNextofkin.focus_set()
           return
       if next_of_kin_cell == "":
           mb.showinfo('Information', "Please Enter Next of Kin Mobile Number")
           self.txtNextofkinC.focus_set()
           return

       if role == "Select your role":
           mb.showinfo('Information', "Please Select your Role")
           self.roleset.get()
           return

       if passwd == "":
           mb.showinfo('Information', "Please Enter Password")
           self.txtpasswd.focus_set()
           return

       if gender == "":
           mb.showinfo('Information', "Please Select your Gender")
           self.txtgender.focus_set()
           return

       try:
            # Inserting record into bank table of bank database
            self.cursor = self.conn.cursor()  # Interact with Bank Database
            self.cursor.execute("INSERT INTO users(name, surname, ID_number, phone_number, email, next_of_kin, next_of_kin_mobile, role, password, gender) VALUES ('%s','%s','%s','%s','%s', '%s','%s','%s', '%s', '%s')" %(fname, lname, uid, phone, email, next_of_kin, next_of_kin_cell, role, passwd, gender))
            # implement sql Sentence
            self.cursor.execute("commit")
            # Submit to database for execution
            mb.showinfo('Registration Status', "Registered Successfully, You may now Login Using your ID Number and Password")
            self.conn.close()
       except:
            mb.showinfo('Registration Status', "Registration Failed!!!")
            # Rollback in case there is any error
            self.conn.rollback()
            # Close database connection
            self.conn.close()

   def clear_form(self):
        self.txtFName.delete(0, END)
        self.txtLName.delete(0, END)
        self.txtUId.delete(0, END)
        self.txtphone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtNextofkin.delete(0, END)
        self.txtNextofkinC.delete(0, END)
        self.txtpasswd.delete(0, END)

   def onClose(self):
       """"""
       self.destroy()
       self.original_frame.show()


if __name__ == "__main__":
  app = LoginApp()
  app.mainloop()


