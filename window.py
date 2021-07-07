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
            host="sql4.freesqldatabase.com",
            user="sql4423232",
            password="pCxc9I64Hj",
            database="sql4423232",
            port="3306",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student VALUES('"+id+"', '"+name+"', '"+phone+"')")
        cursor.execute("commit")

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_phone.delete(0, END)

        Messagebox.showinfo("Insert Status", "Inserted Successfully")
        conn.close()


def delete():
    if e_id.get() == " ":
        Messagebox.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        conn = mysql.connect(
            host="sql4.freesqldatabase.com",
            user="sql4423232",
            password="pCxc9I64Hj",
            database="sql4423232",
            port="3306",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id='"+e_id.get()+"'")
        cursor.execute("commit")

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_phone.delete(0, END)

        Messagebox.showinfo("Delete Status", "Delete Successfully")
        conn.close()


def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id == "" or name == "" or phone == ""):
        Messagebox.showinfo("Update  Status", "All Fields are required")
    else:
        conn = mysql.connect(
            host="sql4.freesqldatabase.com",
            user="sql4423232",
            password="pCxc9I64Hj",
            database="sql4423232",
            port="3306",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("Update student set name='"+ name +"', phone='"+phone+"'WHERE id='"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_phone.delete(0, END)

        Messagebox.showinfo("Update Status", "Updated Successfully")
        conn.close()


def get():
    if(id == "" or name == "" or phone == ""):
        Messagebox.showinfo("Fetch Status", "ID is compulsory for delete")
    else:
        conn = mysql.connect(
            host="sql4.freesqldatabase.com",
            user="sql4423232",
            password="pCxc9I64Hj",
            database="sql4423232",
            port="3306",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * FROM student WHERE id='"+e_id.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
        conn.close()




insert = Button(root, text="Insert", font=("Italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="delete", font=("Italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font=("Italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Insert", font=("Italic", 10), bg="white", command=get)
get.place(x=190, y=140)


root.mainloop()
