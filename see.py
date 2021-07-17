
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Combobox, Treeview
from datetime import datetime
import rsaidnumber


root = Tk()
root.geometry("400x400")
root.title('Life Choices Online')
root.resizable(0, 0)
titlefont = Font(family='Helvetica', size=25)

mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="lifechoicesonline", auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
si_dcurrent = datetime.now().date().strftime("%Y-%m-%d")
si_tcurrent = datetime.now().time().strftime('%H:%M:%S')

"""
Main window
"""

class Login:
    def __init__(self, master):
        self.mcanvas = Canvas(master, width=500, height=600, highlightbackground='#aaa')
        self.mcanvas.place(x=-10, y=-10)
        self.mimg = PhotoImage(file="./images/andrew-ridley-jR4Zf-riEjI-unsplash.png")
        self.mimg = self.mimg.subsample(1)
        self.mcanvas.create_image(230, 250, image=self.mimg)
        self.title = Label(master, text='Welcome to Life Choices', font=titlefont, bg='#83E6DC')
        self.title.place(x=18, y=20)
        self.idlbl = Label(master, text='Enter ID', bg='#83E6DC')
        self.idlbl.place(x=135, y=90)
        self.ident = Entry(master)
        self.ident.place(x=135, y=120)
        self.passlbl = Label(master, text='Enter password', bg='#83E6DC')
        self.passlbl.place(x=135, y=150)
        self.passent = Entry(master)
        self.passent.place(x=135, y=180)


        # Function to sign in user
        def Signin():
            mycursor.execute("SELECT password, role FROM users WHERE ID_number='" + self.ident.get() + "'")
            records = mycursor.fetchall()
            if records == []:
                messagebox.showerror("Invalid Credentials", "User does not exist.")
                self.ident.delete(0, END)
                self.passent.delete(0, END)
            else:
                if self.passent.get() == records[0][0] and records[0][1] != 'ADMIN':
                    mycursor.execute(
                        "SELECT * FROM login WHERE ID_number='" + self.ident.get() + "' AND login_date=curdate() "
                                                                               "AND logout_time is NOT NULL")
                    check = mycursor.fetchall()
                    if len(check) > 0:
                        messagebox.showinfo("Login Successful", "Enter to the next screen.")
                        root.withdraw()
                        self.signedinscreen()
                    else:
                        signinsql = 'INSERT INTO login (ID_number, login_time, logout_time) VALUES (%s, %s, %s)'
                        signinval = (self.ident.get(), si_dcurrent, si_tcurrent)
                        mycursor.execute(signinsql, signinval)
                        mydb.commit()
                        messagebox.showinfo("Login Successful", "Enter to the next screen.")
                        root.withdraw()
                        self.signedinscreen()
                elif self.passent.get() == records[0][0] and records[0][1] == 'ADMIN':
                    messagebox.showwarning('Use Admin Login', 'Admin users must log in through the Admin screen.')
                else:
                    messagebox.showerror("Login Unsuccessful", "Username and password do not correspond")
                    self.ident.delete(0, END)
                    self.passent.delete(0, END)

        self.signinbtn = Button(master, text='Sign In', width=15, command=Signin)
        self.signinbtn.place(x=140, y=220)
        self.registerlbl = Label(master, text='If you do not have an account, please register:', bg='#83E6DC')
        self.registerlbl.place(x=75, y=310)

        # Function that opens the register window
        def Register():
            window = Toplevel()
            window.geometry('300x400')
            window.resizable(0, 0)
            window.config(bg='')

            idlabel = Label(window, text='ID Number')
            idlabel.place(x=20, y=20)
            identry = Entry(window)
            identry.place(x=130, y=20)
            namelabel = Label(window, text='Name')
            namelabel.place(x=20, y=40)
            nameentry = Entry(window)
            nameentry.place(x=130, y=40)
            surnamelabel = Label(window, text='Surname')
            surnamelabel.place(x=20, y=60)
            surnameentry = Entry(window)
            surnameentry.place(x=130, y=60)
            phonelabel = Label(window, text='Contact No.')
            phonelabel.place(x=20, y=80)
            phoneentry = Entry(window)
            phoneentry.place(x=130, y=80)
            passwordlabel = Label(window, text='Password')
            passwordlabel.place(x=20, y=100)
            passentry = Entry(window)
            passentry.place(x=130, y=100)
            kinlbl = Label(window, text='Next of Kin details:')
            kinlbl.place(x=20, y=190)
            kinnamelbl = Label(window, text='Name')
            kinnamelbl.place(x=20, y=220)
            kinnameentry = Entry(window)
            kinnameentry.place(x=130, y=220)
            kin_nolbl = Label(window, text='Phone Number')
            kin_nolbl.place(x=20, y=240)
            kin_noentry = Entry(window)
            kin_noentry.place(x=130, y=240)

            rolelbl = Label(window, text='Registering As:')
            rolelbl.place(x=20, y=130)
            roleset = StringVar(window)
            roleset.set("Select your role")
            rolecombolist = ['STUDENT', 'LECTURER', 'GUEST']
            roleselector = Combobox(window, textvariable=roleset)
            roleselector['values'] = rolecombolist
            roleselector['state'] = 'readonly'
            roleselector.place(x=130, y=130)

            # Function for registering user to the database
            def SignUp():
                if (identry.get() == '' or nameentry.get() == '' or surnameentry.get() == ''
                        or phoneentry.get() == '' or passentry.get() == '' or roleset.get() == 'Select your role'
                        or kinnameentry.get() == '' or kin_noentry.get() == ''):
                    messagebox.showerror('Entries Unfilled', 'Please fill out all entries before signing up.')
                else:
                    try:
                        phonevalid = int(phoneentry.get())
                        kphonevalid = int(kin_noentry.get())
                        if len(phoneentry.get()) != 10 and len(kin_noentry.get()) != 10:
                            messagebox.showerror('Invalid Contact Number',
                                                 'Length of contact number must be 10 digits.')
                        else:
                            idno = rsaidnumber.parse(identry.get())
                            if idno.valid is False:
                                messagebox.showerror('Invalid ID', 'Please enter a valid SA ID.')
                            else:
                                if str.isalpha(nameentry.get()) is False or str.isalpha(kinnameentry.get()) is False\
                                        or str.isalpha(surnameentry.get()) is False:
                                    messagebox.showerror('Invalid Name/Surname',
                                                         'Please enter only alphabetic characters for name')
                                else:
                                    sql1 = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
                                    val1 = (identry.get(), nameentry.get(), surnameentry.get(), phoneentry.get(),
                                            passentry.get(), roleset.get())
                                    sql2 = "INSERT INTO next_of_kin (ID, Name, Phone_number) VALUES (%s, %s, %s)"
                                    val2 = (identry.get(), kinnameentry.get(), kin_noentry.get())
                                    mycursor.execute(sql1, val1)
                                    mycursor.execute(sql2, val2)
                                    mydb.commit()
                                    messagebox.showinfo("Successful", "Your account is registered. "
                                                                      "You may now sign in.")
                                    window.destroy()
                    except ValueError:
                       messagebox.showerror('Invalid details', 'Phone number must be in digits only.')

            registeruserbtn = Button(window, text='Sign Up', command=SignUp)
            registeruserbtn.place(x=20, y=300)

        self.registerbtn = Button(master, text='Register', width=15, command=Register)
        self.registerbtn.place(x=140, y=340)

        # Function to open the admin sign in window after control-a keys have been pressed
        def AdminSignIn(event=None):
            master.withdraw()
            ascreen = Toplevel()
            ascreen.geometry('400x500')
            ascreen.resizable(0, 0)
            acanvas = Canvas(ascreen, width=500, height=600, highlightbackground='#aaa')
            acanvas.place(x=-10, y=-10)
            aimg = PhotoImage(file="./images/jean-philippe-delberghe-75xPHEQBmvA-unsplash.png")
            aimg = aimg.subsample(4)
            acanvas.create_image(230, 290, image=aimg)
            signintitle = Label(ascreen, text='Admin Sign In', font=titlefont, bg="#999")
            signintitle.place(x=100, y=20)
            aframe = Frame(ascreen, width=300, height=200, bg='#999')
            aframe.place(x=50, y=200)
            aidlbl = Label(aframe, text='Your ID', bg='#999')
            aidlbl.place(x=20, y=20)
            aidentry = Entry(aframe)
            aidentry.place(x=140, y=20)
            apasslbl = Label(aframe, text='Your Password', bg='#999')
            apasslbl.place(x=20, y=60)
            apassentry = Entry(aframe)
            apassentry.place(x=140, y=60)

            # Function to sign in admin to the admin log in screen
            def Asignin():
                mycursor.execute("SELECT Password, Role FROM users WHERE ID='" + aidentry.get() + "'")
                records = mycursor.fetchall()
                if records == []:
                    messagebox.showerror("Invalid Credentials", "User does not exist.")
                    aidentry.delete(0, END)
                    apassentry.delete(0, END)
                else:
                    if apassentry.get() == records[0][0] and records[0][1] == 'ADMIN':
                        mycursor.execute(
                            "SELECT * FROM Signin WHERE ID='" + aidentry.get() +
                            "' AND Sign_in_date=curdate() AND Sign_out_time is NULL")
                        check = mycursor.fetchall()
                        if len(check) > 0:
                            messagebox.showinfo("Login Successful", "Enter to the next screen.")
                            ascreen.withdraw()
                            self.adminscreen()
                        else:
                            signinsql = 'INSERT INTO signin (ID, Sign_in_date, Sign_in_time) VALUES (%s, %s, %s)'
                            signinval = (aidentry.get(), si_dcurrent, si_tcurrent)
                            mycursor.execute(signinsql, signinval)
                            mydb.commit()
                            messagebox.showinfo("Login Successful", "Enter to the next screen.")
                            ascreen.withdraw()
                            self.adminscreen()

                    elif apassentry.get() == records[0][0] and records[0][1] != 'ADMIN':
                        messagebox.showwarning('Unauthorized',
                                               'Only admin users may log in through the Admin screen.')
                    else:
                        messagebox.showerror("Login Unsuccessful", "Username and password do not correspond")
                        self.ident.delete(0, END)
                        self.passent.delete(0, END)

            asigninbtn = Button(aframe, text='Sign In', width=15, command=Asignin)
            asigninbtn.place(x=90, y=160)

            ascreen.mainloop()

        # Bind that opens the admin signin screen
        master.bind('<Control-a>', AdminSignIn)

        master.mainloop()

    # Sign in screen for normal users
    def signedinscreen(self):
        mycursor.execute("SELECT Name, Surname, Role FROM users WHERE ID='" + self.ident.get() + "'")
        data = mycursor.fetchall()
        sscreen = Toplevel()
        sscreen.geometry('400x500')
        scanvas = Canvas(sscreen, width=500, height=600, highlightbackground='yellow')
        scanvas.place(x=-10, y=-10)
        simg = PhotoImage(file="./images/ben-neale-sQQf8Ao3dpk-unsplash (1).png")
        simg = simg.subsample(4)
        scanvas.create_image(230, 290, image=simg)

        signedinlbl = Label(sscreen, text='Signed In', font=titlefont, bg='#aaa')
        signedinlbl.place(x=130, y=20)
        frame = Frame(sscreen, width=300, height=200, bg='#aaa')
        frame.place(x=50, y=250)

        rolelbl = Label(frame, text='Role: ' + data[0][2], bg='#aaa')
        rolelbl.place(x=20, y=20)

        # function to sign out normal users
        def signout():
            so_tcurrent = datetime.now().time().strftime('%H:%M:%S')
            so_dcurrent = datetime.now().date().strftime('%Y-%m-%d')
            signoutsql = "UPDATE signin SET Sign_out_date=%s, Sign_out_time=%s WHERE ID='" \
                         + self.ident.get() + "' AND Sign_in_date='" + si_dcurrent + "'"
            signoutval = (so_dcurrent, so_tcurrent)
            mycursor.execute(signoutsql, signoutval)
            mydb.commit()
            messagebox.showinfo('Sign Out successful', 'Enjoy the rest of your day!')
            sscreen.destroy()
            root.destroy()

        signoutbtn = Button(frame, text='Sign Out', command=signout)
        signoutbtn.place(x=130, y=100)

        sscreen.mainloop()

    # Admin screen where the admin can edit and sign out users
    def adminscreen(self):
        asiscreen = Toplevel()
        asiscreen.geometry('400x500')
        asicanvas = Canvas(asiscreen, width=700, height=700, highlightbackground='yellow')
        asicanvas.place(x=-10, y=-10)
        asiimg = PhotoImage(file="./images/scott-webb-OxHPDs4WV8Y-unsplash (1).png")
        asiimg = asiimg.subsample(1)
        asicanvas.create_image(230, 290, image=asiimg)

        mycursor.execute("SELECT * FROM Signin WHERE Sign_in_date=curdate() AND Sign_out_date IS NULL")
        countusers = mycursor.fetchall()
        usersin = len(countusers)

        userssignedin = Label(asiscreen, text="Users Currently Logged In: " + str(usersin), bg='#aaa')
        userssignedin.place(x=50, y=190)

        signedinlbl = Label(asiscreen, text='Signed In', font=titlefont, bg='#aaa')
        signedinlbl.place(x=130, y=20)
        aframe = Frame(asiscreen, width=300, height=200, bg='#aaa')
        aframe.place(x=50, y=250)

        # function to count how many people are currently signed in
        def count():
            mycursor.execute("SELECT * FROM Signin WHERE Sign_in_date=curdate() AND Sign_out_time is NULL")
            records=mycursor.fetchall()
            n_usersin = len(records)
            print(records)
            userssignedin.config(text="Users Currently Logged In: " + str(n_usersin))

        refreshbtn = Button(asiscreen, text='Refresh Users', command=count)
        refreshbtn.place(x=50, y=220)

        # function to sign out admin user
        def asignout():
            so_tcurrent = datetime.now().time().strftime('%H:%M:%S')
            so_dcurrent = datetime.now().date().strftime('%Y-%m-%d')
            signoutsql = "UPDATE signin SET Sign_out_date=%s, Sign_out_time=%s WHERE ID='" \
                         + self.ident.get() + "' AND Sign_in_date='" + si_dcurrent + "'" \
                         "AND Sign_out_time is NULL"
            signoutval = (so_dcurrent, so_tcurrent)
            mycursor.execute(signoutsql, signoutval)
            mydb.commit()
            messagebox.showinfo('Sign Out successful', 'Enjoy the rest of your day!')
            asiscreen.destroy()
            root.destroy()

        signoutbtn = Button(aframe, text='Sign Out', command=asignout)
        signoutbtn.place(x=120, y=100)

        # function that calls the screen where the admin can add, edit or delete users from database
        def editusers():
            escreen = Toplevel()
            escreen.geometry('940x600')
            escreen.resizable(0, 0)

            # function to take data from row in treeview and display it in the user details editor
            def dataselect(event=None):
                if users.selection() == ():
                    pass
                else:
                    edata = users.focus()
                    items = users.item(edata)
                    items = items['values']
                    enameentry.delete(0, END)
                    esurnameentry.delete(0, END)
                    enumberentry.delete(0, END)
                    epasswordentry.delete(0, END)
                    enextofkinnameentry.delete(0, END)
                    enextofkinnoentry.delete(0, END)
                    enameentry.insert(0, items[1])
                    esurnameentry.insert(0, items[2])
                    enumberentry.insert(0, str(items[3]))
                    epasswordentry.insert(0, items[4])
                    eroleset.set(items[5])
                    enextofkinnameentry.insert(0, items[6])
                    enextofkinnoentry.insert(0, str(items[7]))

            users = Treeview(escreen)
            users['columns'] = (1, 2, 3, 4, 5, 6, 7, 8)
            users.column('#0', width=0, stretch=NO)
            users.column(2, anchor=CENTER, width=100)
            users.column(3, anchor=CENTER, width=100)
            users.column(1, anchor=CENTER, width=100)
            users.column(4, anchor=CENTER, width=100)
            users.column(5, anchor=CENTER, width=100)
            users.column(6, anchor=CENTER, width=100)
            users.column(7, anchor=CENTER, width=100)
            users.column(8, anchor=CENTER, width=100)

            users.heading('#0', text='', anchor=CENTER)
            users.heading(1, text='ID', anchor=CENTER)
            users.heading(2, text='Name', anchor=CENTER)
            users.heading(3, text='Surname', anchor=CENTER)
            users.heading(4, text='Contact No.', anchor=CENTER)
            users.heading(5, text='Password', anchor=CENTER)
            users.heading(6, text='Role', anchor=CENTER)
            users.heading(7, text='Next Of Kin Name', anchor=CENTER)
            users.heading(8, text='Next Of Kin No.', anchor=CENTER)

            # function to fill treeview with database data
            def tvinsert():
                mycursor.execute('SELECT users.*, next_of_kin.Name, next_of_kin.Phone_number FROM users '
                                 'INNER JOIN next_of_kin ON users.ID = next_of_kin.ID')
                records = mycursor.fetchall()
                for i in range(len(records)):
                    users.insert(parent='', index=i, iid=i, text='', values=records[i])

            users.bind('<ButtonRelease>', dataselect)

            tvinsert()

            users.place(x=25, y=50)

            addframe = Frame(escreen, width=400, height=300, bg='white', highlightbackground="black", highlightthickness=1)
            addframe.place(x=1000, y=1000)
            addheading = Label(addframe, text='---ADD A USER---', bg='white')
            addheading.place(x=15, y=17)
            yourdetails = Label(addframe, text='_Your Details:_', bg='white')
            yourdetails.place(x=20, y=40)
            aidlabel = Label(addframe, text='ID', bg='white')
            aidlabel.place(x=20, y=70)
            aidentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            aidentry.place(x=20, y=90)
            anamelabel = Label(addframe, text='Name', bg='white')
            anamelabel.place(x=150, y=70)
            anameentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            anameentry.place(x=150, y=90)
            asurnamelabel = Label(addframe, text='Surname', bg='white')
            asurnamelabel.place(x=280, y=70)
            asurnameentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            asurnameentry.place(x=280, y=90)
            anumberlabel = Label(addframe, text='Contact Number', bg='white')
            anumberlabel.place(x=20, y=130)
            anumberentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            anumberentry.place(x=20, y=150)
            apasswordlabel = Label(addframe, text='Password', bg='white')
            apasswordlabel.place(x=150, y=130)
            apasswordentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            apasswordentry.place(x=150, y=150)
            arolelabel = Label(addframe, text='Role', bg='white')
            arolelabel.place(x=280, y=130)
            aroleset = StringVar(escreen)
            aroleset.set("Select your role")
            arolecombolist = ['ADMIN', 'STUDENT', 'LECTURER', 'GUEST']
            aroleselector = Combobox(addframe, textvariable=aroleset, width=14)
            aroleselector['values'] = arolecombolist
            aroleselector['state'] = 'readonly'
            aroleselector.place(x=280, y=150)
            akindetails = Label(addframe, text='_Next Of Kin Details:_', bg='white')
            akindetails.place(x=20, y=190)
            anextofkinnamelabel = Label(addframe, text='Name', bg='white')
            anextofkinnamelabel.place(x=20, y=220)
            anextofkinnameentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            anextofkinnameentry.place(x=20, y=240)
            anextofkinnolabel = Label(addframe, text='Contact Number', bg='white')
            anextofkinnolabel.place(x=150, y=220)
            anextofkinnoentry = Entry(addframe, highlightbackground='black', highlightthickness=1, width=14)
            anextofkinnoentry.place(x=150, y=240)

            # function that allows the admin to add users to the database
            def adduser():
                if (aidentry.get() == '' or anameentry.get() == '' or asurnameentry.get() == ''
                        or anumberentry.get() == '' or apasswordentry.get() == '' or aroleset.get() == 'Select your role'
                        or anextofkinnameentry.get() == '' or anextofkinnoentry.get() == ''):
                    messagebox.showerror('Entries Unfilled', 'Please fill out all entries before registering user.')
                else:
                    try:
                        phonevalid = int(anumberentry.get())
                        kphonevalid = int(anextofkinnoentry.get())
                        if len(anumberentry.get()) != 10 and len(anextofkinnoentry.get()) != 10:
                            messagebox.showerror('Invalid Contact Number',
                                                 'Length of contact number must be 10 digits.')
                        else:
                            idno = rsaidnumber.parse(aidentry.get())
                            if idno.valid is False:
                                messagebox.showerror('Invalid ID', 'Please enter a valid SA ID.')
                            else:
                                if str.isalpha(anameentry.get()) is False or str.isalpha(anextofkinnameentry.get()) is False \
                                        or str.isalpha(asurnameentry.get()) is False:
                                    messagebox.showerror('Invalid Name/Surname',
                                                         'Please enter only alphabetic characters for name')
                                else:
                                    sql1 = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
                                    val1 = (aidentry.get(), anameentry.get(), asurnameentry.get(), anumberentry.get(),
                                            apasswordentry.get(), aroleset.get())
                                    sql2 = "INSERT INTO next_of_kin (ID, Name, Phone_number) VALUES (%s, %s, %s)"
                                    val2 = (aidentry.get(), anextofkinnameentry.get(), anextofkinnoentry.get())
                                    mycursor.execute(sql1, val1)
                                    mycursor.execute(sql2, val2)
                                    mydb.commit()
                                    messagebox.showinfo("Successful", "Account is registered.")

                                    users.delete(*users.get_children())
                                    tvinsert()
                    except ValueError:
                        messagebox.showerror('Invalid details', 'Phone number must be in digits only.')

            adduserbtn = Button(addframe, text='Commit', command=adduser)
            adduserbtn.place(x=280, y=235)

            editframe = Frame(escreen, width=400, height=300, bg='white', highlightbackground="black", highlightthickness=1)
            editframe.place(x=1000, y=1000)
            editheading = Label(editframe, text='---EDIT A USER---', bg='white')
            editheading.place(x=15, y=17)
            eyourdetails = Label(editframe, text='_Your Details:_', bg='white')
            eyourdetails.place(x=20, y=40)
            enamelabel = Label(editframe, text='Name', bg='white')
            enamelabel.place(x=20, y=70)
            enameentry = Entry(editframe, highlightbackground='black', highlightthickness=1, width=14)
            enameentry.place(x=20, y=90)
            esurnamelabel = Label(editframe, text='Surname', bg='white')
            esurnamelabel.place(x=150, y=70)
            esurnameentry = Entry(editframe, highlightbackground='black', highlightthickness=1, width=14)
            esurnameentry.place(x=150, y=90)
            enumberlabel = Label(editframe, text='Contact Number', bg='white')
            enumberlabel.place(x=280, y=70)
            enumberentry = Entry(editframe, highlightbackground='black', highlightthickness=1, width=14)
            enumberentry.place(x=280, y=90)
            epasswordlabel = Label(editframe, text='Password', bg='white')
            epasswordlabel.place(x=20, y=130)
            epasswordentry = Entry(editframe, highlightbackground='black', highlightthickness=1, width=14)
            epasswordentry.place(x=20, y=150)
            erolelabel = Label(editframe, text='Role', bg='white')
            erolelabel.place(x=150, y=130)
            eroleset = StringVar(escreen)
            eroleset.set("")
            erolecombolist = ['ADMIN', 'STUDENT', 'LECTURER', 'GUEST']
            eroleselector = Combobox(editframe, textvariable=eroleset, width=14)
            eroleselector['values'] = erolecombolist
            eroleselector['state'] = 'readonly'
            eroleselector.place(x=150, y=150)
            ekindetails = Label(editframe, text='_Next Of Kin Details:_', bg='white')
            ekindetails.place(x=20, y=190)
            enextofkinnamelabel = Label(editframe, text='Name', bg='white')
            enextofkinnamelabel.place(x=20, y=220)
            enextofkinnameentry = Entry(editframe, highlightbackground='black', highlightthickness=1, width=14)
            enextofkinnameentry.place(x=20, y=240)
            enextofkinnolabel = Label(editframe, text='Contact Number', bg='white')
            enextofkinnolabel.place(x=150, y=220)
            enextofkinnoentry = Entry(editframe, highlightbackground='black', highlightthickness=1, width=14)
            enextofkinnoentry.place(x=150, y=240)

            # function that allows the admin to edit the details of a user in the database
            def edituser():
                edata = users.focus()
                items = users.item(edata)
                items = items['values']
                if (enameentry.get() == '' or esurnameentry.get() == ''
                        or enumberentry.get() == '' or epasswordentry.get() == '' or eroleset.get() == ''
                        or enextofkinnameentry.get() == '' or enextofkinnoentry.get() == ''):
                    messagebox.showerror('Entries Unfilled', 'Please fill out all entries before registering user.')
                else:
                    try:
                        phonevalid = int(enumberentry.get())
                        kphonevalid = int(enextofkinnoentry.get())
                        if len(enumberentry.get()) != 10 and len(enextofkinnoentry.get()) != 10:
                            messagebox.showerror('Invalid Contact Number',
                                                 'Length of contact number must be 10 digits.')
                        else:
                            if str.isalpha(enameentry.get()) is False or str.isalpha(enextofkinnameentry.get()) is False \
                                    or str.isalpha(esurnameentry.get()) is False:
                                messagebox.showerror('Invalid Name/Surname',
                                                     'Please enter only alphabetic characters for name')
                            else:
                                sql1 = "UPDATE users SET Name=%s, Surname=%s, Phone_number=%s" \
                                       "Password=%s, Role=%s WHERE ID='" + str(items[0]) + "'"
                                val1 = (enameentry.get(), esurnameentry.get(), enumberentry.get(),
                                        epasswordentry.get(), eroleset.get())
                                sql2 = "UPDATE next_of_kin SET Name=%s, Phone_number=%s" \
                                       "WHERE ID='" + str(items[0]) + "'"
                                val2 = (enextofkinnameentry.get(), enextofkinnoentry.get())
                                mycursor.execute(sql1, val1)
                                mycursor.execute(sql2, val2)
                                mydb.commit()
                                messagebox.showinfo("Successful", "Account details updated.")

                                users.delete(*users.get_children())
                                tvinsert()
                    except ValueError:
                        messagebox.showerror('Invalid details', 'Phone number must be in digits only.')

            edituserbtn = Button(editframe, text='Commit', command=edituser)
            edituserbtn.place(x=280, y=235)
            """
            id, name, surname, contactno, password, role, nextokin name, nextokin contactno
            """

            # function that brings the add user frame into view
            def adduserfunc():
                editframe.place(x=1000, y=1000)
                addframe.place(x=200, y=290)

            addbtn = Button(escreen, text='Add user', command=adduserfunc)
            addbtn.place(x=50, y=350)

            # function that brings the edit user frame into view
            def edituserfunc():
                addframe.place(x=1000, y=1000)
                editframe.place(x=200, y=290)

            edbtn = Button(escreen, text='Edit user', command=edituserfunc)
            edbtn.place(x=50, y=400)

            # function to delete user from database
            def deleteuser():
                editframe.place(x=1000, y=1000)
                edata = users.focus()
                items = users.item(edata)
                items = items['values']
                mycursor.execute("DELETE FROM next_of_kin WHERE ID='" + str(items[0]) + "'")
                mycursor.execute("DELETE FROM users WHERE ID='" + str(items[0]) + "'")
                mydb.commit()
                users.delete(*users.get_children())
                tvinsert()

            delbtn = Button(escreen, text='Delete user', command=deleteuser)
            delbtn.place(x=50, y=450)

            escreen.mainloop()

        modifybtn = Button(aframe, text='Edit database', command=editusers)
        modifybtn.place(x=60, y=50)

        # function that calls window where the admin can sign out users
        def logprivilege():
            lscreen = Toplevel()
            lscreen.geometry('560x500')
            lscreen.resizable(0, 0)

            si_users = Treeview(lscreen)
            si_users['columns'] = (1, 2, 3, 4, 5, 6)
            si_users.column('#0', width=0, stretch=NO)
            si_users.column(2, anchor=CENTER, width=80)
            si_users.column(3, anchor=CENTER, width=80)
            si_users.column(1, anchor=CENTER, width=80)
            si_users.column(4, anchor=CENTER, width=80)
            si_users.column(5, anchor=CENTER, width=80)
            si_users.column(6, anchor=CENTER, width=80)

            si_users.heading('#0', text='', anchor=CENTER)
            si_users.heading(1, text='Signed In', anchor=CENTER)
            si_users.heading(2, text='ID', anchor=CENTER)
            si_users.heading(3, text='Sign in date', anchor=CENTER)
            si_users.heading(4, text='Sign in time', anchor=CENTER)
            si_users.heading(5, text='Sign out date', anchor=CENTER)
            si_users.heading(6, text='Sign out time', anchor=CENTER)

            # function to fill the treeview with data from the database
            def tvinsert():
                mycursor.execute('SELECT * FROM Signin')
                records = mycursor.fetchall()
                for i in range(len(records)):
                    si_users.insert(parent='', index=i, iid=i, text='', values=records[i])

            tvinsert()
            si_users.place(x=25, y=50)

            # function that allows the admin user to sign out other users
            def loguserout():
                if si_users.selection() == ():
                    messagebox.showerror("Error", "Please select user to log out")
                else:
                    ldata = si_users.focus()
                    litems = si_users.item(ldata)
                    litems = litems['values']
                    select = str(int(si_users.selection()[0]) + 1)
                    so_tcurrent = datetime.now().time().strftime('%H:%M:%S')
                    so_dcurrent = datetime.now().date().strftime('%Y-%m-%d')
                    lsql = "UPDATE signin SET Sign_out_date=%s, Sign_out_time=%s WHERE SignedIn='" \
                                 + select + "' AND Sign_in_date='" + litems[2] + "'"
                    lval = (so_dcurrent, so_tcurrent)
                    mycursor.execute(lsql, lval)
                    mydb.commit()
                    si_users.delete(*si_users.get_children())
                    mycursor.execute('SELECT * FROM Signin')
                    records = mycursor.fetchall()
                    for i in range(len(records)):
                        si_users.insert(parent='', index=i, iid=i, text='', values=records[i])

            logoutbtn = Button(lscreen, text='Log user out', command=loguserout)
            logoutbtn.place(x=130, y=300)

            lscreen.mainloop()

        logbtn = Button(aframe, text='Log users out', command=logprivilege)
        logbtn.place(x=150, y=50)

        asiscreen.mainloop()
