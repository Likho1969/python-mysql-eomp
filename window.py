from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

root = Tk()
root.geometry("1500x700")
root.title("Online")

name = Label(root, text="Enter Name", font="bold 10")
name.place(x=20, y=30)

surname = Label(root, text="Enter Surname", font="bold 10")
surname.place(x=20, y=60)

id = Label(root, text="Enter ID", font="bold 10")
id.place(x=20, y=90)

phone = Label(root, text="Enter Phone", font="bold 10")
phone.place(x=20, y=120)

email = Label(root, text="Enter Email", font="bold 10")
email.place(x=20, y=150)

next_of_kin = Label(root, text="Enter Next of Kin", font="bold 10")
next_of_kin.place(x=20, y=180)

next_of_kin_cell = Label(root, text="Enter Next of Kin Mobile", font="bold 10")
next_of_kin_cell.place(x=20, y=210)

role = Label(root, text="Enter Role", font="bold 10")
role.place(x=20, y=240)

gender = Label(root, text="Enter Gender", font="bold 10")
gender.place(x=20, y=270)

e_name = Entry(root)
e_name.place(x=150, y=30)

e_surname = Entry(root)
e_surname.place(x=150, y=60)

e_id = Entry(root)
e_id.place(x=150, y=90)

e_phone = Entry(root)
e_phone.place(x=150, y=120)

e_email = Entry(root)
e_email.place(x=150, y=150)

e_next_of_kin = Entry(root)
e_next_of_kin.place(x=150, y=180)

e_next_of_kin_cell = Entry(root)
e_next_of_kin_cell.place(x=200, y=210)

e_role = Entry(root)
e_role.place(x=150, y=240)

e_gender = Entry(root)
e_gender.place(x=150, y=270)


def insert():
    id = e_id.get()
    name = e_name.get()
    surname = e_surname.get()
    phone = e_phone.get()
    email = e_email.get()
    next_of_kin = e_next_of_kin.get()
    next_of_kin_cell = e_next_of_kin_cell.get()
    role = e_role.get()
    gender = e_gender.get()



    if(id == "" or name == "" or surname == ""):
        Messagebox.showinfo("Insert Status", "All Fields are required")
    else:
        conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(name, surname, ID_number, phone_number, email, next_of_kin, next_of_kin_mobile, role, password, gender) VALUES ('%s','%s','%s','%s','%s', '%s','%s','%s', '%s')" %(name, surname, id, phone, email, next_of_kin, next_of_kin_cell, role, gender))
        cursor.execute("commit")

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_surname.delete(0, END)

        show()

        Messagebox.showinfo("Insert Status", "Inserted Successfully")
        conn.close()


def delete():
    if e_id.get() == " ":
        Messagebox.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE ID_number='"+e_id.get()+"'")
        cursor.execute("commit")

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_surname.delete(0, END)

        show()

        Messagebox.showinfo("Delete Status", "Delete Successfully")
        conn.close()


def update():
    name = e_name.get()
    surname = e_surname.get()
    id = e_id.get()
    phone = e_phone.get()
    email = e_email.get()
    next_of_kin = e_next_of_kin.get()
    next_of_kin_cell = e_next_of_kin_cell.get()
    role = e_role.get()
    gender = e_gender.get()


    if(id == "" or name == "" or phone == ""):
        Messagebox.showinfo("Update  Status", "All Fields are required")
    else:
        conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("Update users set name='"+ name +"', surname='"+surname+"', ID_number='"+id+"', phone_number='"+phone+"', email='"+email+ "', next_of_kin='"+next_of_kin+ "', next_of_kin_mobile='"+next_of_kin_cell+ "', role='"+role+ "', gender='"+gender+ "'WHERE ID_number='"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0, END)
        e_name.delete(0, END)
        e_phone.delete(0, END)

        show()

        Messagebox.showinfo("Update Status", "Updated Successfully")
        conn.close()


def get():
    if(id == "" or name == "" or surname == ""):
        Messagebox.showinfo("Fetch Status", "ID is compulsory for delete")
    else:
        conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE ID_number='"+e_id.get()+"'")
        rows = cursor.fetchall()
        lst.delete(0, lst.size())

        show()

        for row in rows:
            insertData =str(row[0])+ '    ' + row[1] + '    ' + str(row[2]) + '   ' + row[3] + '    ' + str(row[4]) + '   ' + row[5] + '    ' + str(row[6]) + '   ' + row[7] + '    ' + str(row[8]) + '   ' + row[9]
            lst.insert(lst.size()+1, insertData)
            # Printing the outputs to the interface
        conn.close()

def show():
    conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    lst.delete(0, lst.size())

    for row in rows:
        insertData =str(row[0])+ '           ' + row[1]
        lst.insert(lst.size()+1, insertData)

    conn.close()


def logged_in_and_out():
    conn = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="lifechoicesonline",
            auth_plugin='mysql_native_password'
)

insert = Button(root, text="Insert", font=("Italic", 10), bg="white", command=insert)
insert.place(x=20, y=400)

delete = Button(root, text="delete", font=("Italic", 10), bg="white", command=delete)
delete.place(x=110, y=400)

update = Button(root, text="Update", font=("Italic", 10), bg="white", command=update)
update.place(x=200, y=400)

get = Button(root, text="Search", font=("Italic", 10), bg="white", command=get)
get.place(x=300, y=400)

lst = Listbox(root)
lst.place(x=390, y=30, width=900)
show()


root.mainloop()
