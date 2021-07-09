import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from tkinter.ttk import Combobox
from datetime import datetime
import rsaidnumber


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
       self.geometry("800x600")
       self.configure(bg="#000000")
       self.lblHeading = tk.Label(self,text="Welcome to Login Page", font=("sans-serif", 16),bg="black",fg="white")
       self.lbluname = tk.Label(self,text="Enter UserName:", font=("sans-serif", 10),bg="black",fg="white")
       self.lblpsswd = tk.Label(self,text="Enter Password:", font=("sans-serif", 10),bg="black",fg="white")
       self.txtuname = tk.Entry(self,width=60)
       self.txtpasswd = tk.Entry(self,width=60, show="*")
       self.btn_login = tk.Button(self, text="Login",font=("sans-serif", 11),bg="black",fg="white",command=self.login)
       self.btn_clear= tk.Button(self, text="Clear",font=("sans-serif", 11),bg="black",fg="white",command=self.clear_form)
       self.btn_register = tk.Button(self, text="Not Member ? Register", font=("sans-serif", 11),bg="black",fg="yellow",command=self.open_registration_window)
       self.btn_exit = tk.Button(self, text="Exit",font=("sans-serif", 14),bg="black",fg="red",command=self.exit)
       self.admin = tk.Button(self, text="Administrator",font=("Helvetica", 11),bg="black",fg="white",command=self.admin_management)
       self.lblHeading.place(relx=0.35, rely=0.089, height=50, width=250)
       self.lbluname.place(relx=0.235, rely=0.289, height=21, width=106)
       self.lblpsswd.place(relx=0.242, rely=0.378, height=21, width=102)
       self.txtuname.place(relx=0.417, rely=0.289,height=20, relwidth=0.273)
       self.txtpasswd.place(relx=0.417, rely=0.378,height=20, relwidth=0.273)
       self.btn_login.place(relx=0.45, rely=0.489, height=24, width=52)
       self.btn_clear.place(relx=0.54, rely=0.489, height=24, width=72)
       self.btn_register.place(relx=0.695, rely=0.489, height=24, width=175 )
       self.btn_exit.place(relx=0.75, rely=0.911, height=24, width=61)
       self.admin.place(relx=0.15, rely=0.911, height=34, width=91)

   def open_registration_window(self):
       self.withdraw()
       window = RegisterWindow(self)
       window.grab_set()


   def open_login_success_window(self):
       self.withdraw()
       window = Login_Success_Window(self)
       window.grab_set()


   def show(self):
       """"""
       self.update()
       self.deiconify()

   def login(self):

       try:
           self.conn = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)

           username = self.txtuname.get() # Retrieving entered username
           passwd = self.txtpasswd.get()  # Retrieving entered password
           si_dcurrent = datetime.now().date().strftime("%Y-%m-%d")
           si_tcurrent = datetime.now().time().strftime('%H:%M:%S')

           self.conn.execute("SELECT ID_number, password, role FROM users WHERE ID_number='" + username + "'")
           self.records = self.conn.fetchall()

           loginsql = 'INSERT INTO login (username, password,login_date, login_time) VALUES (%S,%s, %s, %s)'
           loginval = (username, passwd, si_dcurrent, si_tcurrent)
           self.conn.execute(loginsql, loginval)
           self.conn.commit()
           mb.showinfo('Login Status', "Login Successful! Enjoy Your Day")
           self.open_login_success_window()

           conn.close()

       except:
          mb.showinfo('Login Status', "Login Failed!, Contact the Receptionist  ")
          conn.disconnect()


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
           import window

# Using Toplevel widget to create a new window named Register Successful Window
class Login_Success_Window(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("800x400")
         self.title("You Have Successfully Login -> "+str(username))
         self.configure(background="#000000")
         self.lbl_Login_success = tk.Label(self, text="Hello "+str(username)+" Welcome to Application", font=("sans-serif", 15), bg="black", fg="white")
         self.lbl_Login_success.place(relx=0.150, rely=0.111, height=50, width=300)

         cursor.execute("SELECT * FROM users limit 0,10")
         i=1
         for user in cursor:
            for j in range(len(user)):
                e = Entry(self,bg="black", fg="white")
                e.grid(row=i, column=j)
                e.insert(END, user[j])
            i=i+1
         # create OK button
         self.btn_register = tk.Button(self, text="Logout", font=("sans-serif", 11), bg="black", fg="white",command=self.logout)
         #self.btn_register.pack(side = tk.BOTTOM)
         self.btn_register.place(relx=0.467, rely=0.311, height=21, width=50)

         self.btn_register = tk.Button(self, text="Delete", font=("sans-serif", 11), bg="black", fg="white",command=self.delete)
         #self.btn_register.pack(side = tk.BOTTOM)
         self.btn_register.place(relx=0.467, rely=0.400, height=21, width=50)


   def delete(self):
    self.txtuname = tk.Entry(self,width=60)
    self.txtpasswd = tk.Entry(self,width=60, show="*")
    global username
    username = str(self.txtuname.get())  # Retrieving entered username
    if username == " ":
        mb.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        conn = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username='"+username+"'")
        cursor.execute("commit")


        mb.showinfo("Delete Status", "Delete Successfully")
        conn.close()

   def logout(self):
        mb.showinfo('Information', "You Have Successfully Logout " + str(username))
        self.destroy()
        self.original_frame.show()


# Using Toplevel widget to create a new window named RegisterWindow to register a new user
class RegisterWindow(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("800x700")
         self.title("Register")
         self.configure(background="#000000")

         self.lblRegister = tk.Label(self, text="Register", font=("sans-serif", 16), bg="black", fg="white")
         self.lblFName = tk.Label(self, text="Enter Name:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblLName = tk.Label(self, text="Enter Surname:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblUId = tk.Label(self, text="Enter ID Number:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblphone = tk.Label(self, text="Enter Phone Number:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblemail = tk.Label(self, text="Enter Email:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblNextpfkin = tk.Label(self, text="Enter Next of kin:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblNextpfkinC = tk.Label(self, text="Enter Next of Kin Number:", font=("sans-serif", 10), bg="black", fg="white")
         self.lblpasswd = tk.Label(self, text="Enter Password:", font=("sans-serif", 10), bg="black", fg="white")

         self.txtFName = tk.Entry(self)
         self.txtLName = tk.Entry(self)
         self.txtUId = tk.Entry(self)
         self.txtphone = tk.Entry(self)
         self.txtemail = tk.Entry(self)
         self.txtgender = tk.Entry(self)
         self.txtNextofkin = tk.Entry(self)
         self.txtNextofkinC = tk.Entry(self)
         self.txtpasswd = tk.Entry(self)

         self.btn_register = tk.Button(self, text="Register", font=("sans-serif", 11), bg="black", fg="white", command=self.register)
         self.btn_cancel = tk.Button(self, text="Back To Login", font=("sans-serif", 11), bg="black", fg="white", command=self.onClose)

         self.lblRegister.place(relx=0.467, rely=0.111, height=21, width=100)
         self.lblFName.place(relx=0.318, rely=0.2, height=21, width=100)
         self.lblLName.place(relx=0.319, rely=0.267, height=21, width=100)
         self.lblUId.place(relx=0.240, rely=0.333, height=21, width=190)
         self.lblphone.place(relx=0.300, rely=0.4, height=21, width=150)
         self.lblemail.place(relx=0.310, rely=0.467, height=21, width=105)
         self.lblNextpfkin.place(relx=0.262, rely=0.533, height=21, width=160)
         self.lblNextpfkinC.place(relx=0.212, rely=0.6, height=21, width=170)
         self.lblpasswd.place(relx=0.300, rely=0.740, height=21, width=160)
         self.txtFName.place(relx=0.490, rely=0.2, height=20, relwidth=0.223)
         self.txtLName.place(relx=0.490, rely=0.267, height=20, relwidth=0.223)
         self.txtUId.place(relx=0.490, rely=0.333, height=20, relwidth=0.223)
         self.txtphone.place(relx=0.490, rely=0.4, height=20, relwidth=0.223)
         self.txtemail.place(relx=0.490, rely=0.467, height=20, relwidth=0.223)
         self.txtNextofkin.place(relx=0.490, rely=0.533, height=20, relwidth=0.223)
         self.txtNextofkinC.place(relx=0.490, rely=0.6, height=20, relwidth=0.223)
         self.btn_register.place(relx=0.500, rely=0.880, height=24, width=63)
         self.btn_cancel.place(relx=0.605, rely=0.880, height=24, width=150)
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
            #Close database connection
            self.conn.close()


   def onClose(self):
       """"""
       self.destroy()
       self.original_frame.show()


if __name__ == "__main__":
  app = LoginApp()
  app.mainloop()
