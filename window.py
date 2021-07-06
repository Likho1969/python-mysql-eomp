from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

root = Tk()
root.geometry("600x600")
root.title("Online")

id = Label(root, text="Enter ID", font="bold 10")
id.place(x=20, y=30)

name = Label(root, text="Enter Name", font="bold 10")
name.place(x=20, y=60)

phone = Label(root, text="Enter Phone", font="bold 10")
phone.place(x=20, y=90)

e_id = Entry(root)
e_id.place(x=150, y=30)

e_name = Entry(root)
e_name.place(x=150, y=60)

e_phone = Entry(root)
e_phone.place(x=150, y=90)

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id == "" or name == "" or phone == ""):
        Messagebox.showinfo("Insert Status", "All Fields are required")
    else:
        conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="",
            database='lifechoicesonline',
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ")

insert = Button(root, text="Insert", font=("Italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

insert = Button(root, text="Delete", font=("Italic", 10), bg="white", command=delete)
insert.place(x=70, y=140)

update = Button(root, text="Update", font=("Italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Insert", font=("Italic", 10), bg="white", command=get)
get.place(x=190, y=140)


root.mainloop()
