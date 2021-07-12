# Likho Kapesi

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


root = Tk()
root.title("Life Choices Online Administrator Management System")
root.geometry("1550x3518")
root.config(bg="tan")

class Admin:
    def __init__(self, master):
        global mycursor
        # Style For Treeview
        self.tree = ttk.Style()
        self.tree.theme_use('clam')
        self.tree.configure("Treeview", background="black", rowheight=25, fieldbackground="black")
        self.tree.map('Treeview', background=[('selected', 'yellow')])
        # Create Treeview
        self.treeView = ttk.Treeview(master, selectmode='browse')
        # define our columns
        self.treeView["columns"] = ("Name", "Surname", "ID Number", "Phone Number", "Email", "Next of kin", "Next of kin Mobile", "Role", "Password", "Gender")
        # Name and Size Our Columns
        self.treeView.column("#0", width=0, minwidth=100, stretch=NO)

        self.treeView.column("Name", anchor=W, width=100)
        self.treeView.column("Surname", anchor=W, width=100)
        self.treeView.column("ID Number", anchor=W, width=150)  # phantom column
        self.treeView.column("Phone Number", anchor=W, width=150)
        self.treeView.column("Email", anchor=W, width=150)
        self.treeView.column("Next of kin", anchor=W, width=150)
        self.treeView.column("Next of kin Mobile", anchor=W, width=150)
        self.treeView.column("Role", anchor=W, width=150)
        self.treeView.column("Password", anchor=W, width=150)
        self.treeView.column("Gender", anchor=W, width=150)

        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)

        self.treeView.heading("Name", text="Name", anchor=CENTER)
        self.treeView.heading("Surname", text="Surname", anchor=CENTER)
        self.treeView.heading("ID Number", text="ID Number", anchor=CENTER)
        self.treeView.heading("Phone Number", text="Phone Number", anchor=CENTER)
        self.treeView.heading("Email", text="Email", anchor=CENTER)
        self.treeView.heading("Next of kin", text="Next of kin", anchor=CENTER)
        self.treeView.heading("Next of kin Mobile", text="Next of kin Mobile", anchor=CENTER)
        self.treeView.heading("Role", text="Role", anchor=CENTER)
        self.treeView.heading("Password", text="Password", anchor=CENTER)
        self.treeView.heading("Gender", text="Gender", anchor=CENTER)

        self.treeView.place(x=150, y=50)

        # Sript rows into odd and evens
        self.treeView.tag_configure("odd", background="yellow")
        self.treeView.tag_configure("even", background="blue")

        # Frames
        self.frame1 = LabelFrame(master, bg="green")
        self.frame1.place(x=200, y=370, width=1270, height=175)

        # Labels
        self.namelbl = Label(master, text="Name:", bg="green", fg="white", font="sans-serif")
        self.namelbl.place(x=230, y=390)

        self.surnamelbl = Label(master, text="Surname:", bg="green", fg="white", font="sans-serif")
        self.surnamelbl.place(x=210, y=440)

        self.idlbl = Label(master, text="ID Number:", bg="green", fg="white", font="sans-serif")
        self.idlbl.place(x=203, y=490)

        self.phonelbl = Label(master, text="Phone Number:", bg="green", fg="white", font="sans-serif")
        self.phonelbl.place(x=490, y=390)

        self.emaillbl = Label(master, text="Email:", bg="green", fg="white", font="sans-serif")
        self.emaillbl.place(x=555, y=440)

        self.next_of_kin_lbl = Label(master, text="Next of Kin:", bg="green", fg="white", font="sans-serif")
        self.next_of_kin_lbl.place(x=520, y=490)

        self.next_of_kin_mobile_lbl = Label(master, text="Next of Kin Mobile:", bg="green", fg="white", font="sans-serif")
        self.next_of_kin_mobile_lbl.place(x=830, y=390)

        self.rolelbl = Label(master, text="Role:", bg="green", fg="white", font="sans-serif")
        self.rolelbl.place(x=940, y=440)

        self.passwordlbl = Label(master, text="Password:", bg="green", fg="white", font="sans-serif")
        self.passwordlbl.place(x=900, y=492)

        self.genderlbl = Label(master, text="Gender:", bg="green", fg="white", font="sans-serif")
        self.genderlbl.place(x=1180, y=390)

        # Entries
        self.nameEnt = Entry(master)
        self.nameEnt.place(x=300, y=390)

        self.surnameEnt = Entry(master)
        self.surnameEnt.place(x=300, y=440)

        self.id_numberEnt = Entry(master)
        self.id_numberEnt.place(x=300, y=490)

        self.phone_numberEnt = Entry(master)
        self.phone_numberEnt.place(x=630, y=390)

        self.emailEnt = Entry(master)
        self.emailEnt.place(x=630, y=440)

        self.next_of_kin_nameEnt = Entry(master)
        self.next_of_kin_nameEnt.place(x=630, y=490)

        self.next_of_kin_contactEnt = Entry(master)
        self.next_of_kin_contactEnt.place(x=1000, y=390)

        self.roleEnt = Entry(master)
        self.roleEnt.place(x=1000, y=440)

        self.passwordEnt = Entry(master)
        self.passwordEnt.place(x=1000, y=492)

        self.genderEnt = Entry(master)
        self.genderEnt.place(x=1260, y=390)

        # Buttons
        self.addbtn = Button(master, text="Add User", bg="green", fg="white", font="sans-serif", command=self.add)
        self.addbtn.place(x=600, y=600)

        self.deletebtn = Button(master, text="Delete", bg="red", fg="white", font="sans-serif", command=self.delete)
        self.deletebtn.place(x=780, y=600)

        self.exitbtn = Button(master, text="Exit", bg="red", fg="black", font="sans-serif", command=self.exit)
        self.exitbtn.place(x=950, y=600)

        self.conn = mysql.connector.connect(
                    host="localhost",
                    user="lifechoices",
                    password="@Lifechoices1234",
                    database="lifechoicesonline",
                    auth_plugin='mysql_native_password'
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('Select * from users')
        count = 0
        for i in self.cursor:
           # print(i)
           if count % 2 == 0:
               self.treeView.insert("", 'end', iid=count, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]), tags=("even",))
           else:
               self.treeView.insert("", 'end', iid=count, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], [8], i[9]),   tags=("odd",))
           count += 1
        mydb.commit()

    def add(self):
        global mycursor, count
        self.nameEnt.get()
        self.surnameEnt.get()
        self.id_numberEnt.get()
        self.phone_numberEnt.get()
        self.emailEnt.get()
        self.next_of_kin_nameEnt.get()
        self.next_of_kin_contactEnt.get()
        self.roleEnt.get()
        self.passwordEnt.get()
        self.genderEnt.get()

        for i in self.cursor:
            self.treeView.insert("", 'end', iid=count, values=(i[0], self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.emailEnt.get(), self.next_of_kin_nameEnt.get(), self.next_of_kin_contactEnt.get(), self.roleEnt.get(), self.passwordEnt.get(), self.genderEnt.get()))
            count += 1

        if self.nameEnt.get() == '' or self.surnameEnt.get() == '' or self.id_numberEnt.get() == '' or self.phone_numberEnt.get() == '' or self.emailEnt.get() == '' or self.next_of_kin_nameEnt.get() == '' or self.next_of_kin_contactEnt.get() == '' or self.roleEnt.get() == '' or self.passwordEnt.get() == '' or self.genderEnt.get() == '':
            messagebox.showerror("Error", "Please Fill Out All Information")

        else:
            conn = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users VALUES('"+self.nameEnt.get()+"', '"+self.surnameEnt.get()+"', '"+self.id_numberEnt.get()+"', '"+self.phone_numberEnt.get()+"', '"+self.emailEnt.get()+"', '"+self.next_of_kin_nameEnt.get()+"', '"+self.next_of_kin_contactEnt.get()+"', '"+self.roleEnt.get()+"', '"+self.passwordEnt.get()+"', '"+self.genderEnt.get()+"')")
            cursor.execute("commit")

            messagebox.showinfo("Insert Status", "Inserted Successfully")
            conn.close()

        count = []
        for i in self.cursor:
            self.treeView.insert("", 'end', iid=count, values=(i[0], self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.emailEnt.get(), self.next_of_kin_nameEnt.get(), self.next_of_kin_contactEnt.get(),  self.roleEnt.get(), self.passwordEnt.get(), self.genderEnt.get()))
            count += 1

        self.nameEnt.delete(0, END)
        self.surnameEnt.delete(0, END)
        self.id_numberEnt.delete(0, END)
        self.phone_numberEnt.delete(0, END)
        self.emailEnt.delete(0, END)
        self.next_of_kin_nameEnt.delete(0, END)
        self.next_of_kin_contactEnt.delete(0, END)
        self.roleEnt.delete(0, END)
        self.passwordEnt.delete(0, END)
        self.genderEnt.delete(0, END)

    def delete(self):
        ask = messagebox.askquestion("Delete User", "Do you want to delete the user?")
        if ask == "yes":
                conn = mysql.connector.connect(
                        host="localhost",
                        user="lifechoices",
                        password="@Lifechoices1234",
                        database="lifechoicesonline",
                        auth_plugin='mysql_native_password'
    )
                cursor = conn.cursor()
                cursor.execute("DELETE FROM login WHERE username='"+self.id_numberEnt.get()+"'")
                cursor.execute("commit")
                conn.close()
                self.x = self.treeView.selection()
                self.treeView.delete()
                self.id_numberEnt.delete(0, END)

                messagebox.showinfo("Delete Status", "Deleted Successfully")

    def exit(self):
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
        if MsgBox == 'yes':
            root.destroy()


x = Admin(root)
root.mainloop()
