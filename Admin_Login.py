from sqlite3.dbapi2 import connect
from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import sqlite3
from admin_dashboard import admin_dashboard


# GUI
class Admin_Login:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x550+50+50')
        self.root.title(' Taxi Booking Service"')
        self.root.config(bg='white')


# username and password Label
        admin_ID_label = Label(self.root, text='Admin ID :- ', fg='Black',
                               bg='white', font=("Times New Roman", 30, "bold")).place(x=130, y=130)
        Password_label = Label(self.root, text='Password :-', fg='black',
                               bg='white', font=("Times New Roman", 30, "bold")).place(x=130, y=210)

# Variables
        self.var_admin_ID = StringVar()
        self.var_password_admin = StringVar()
# Text box
        txt_admin = Entry(self.root, textvariable=self.var_admin_ID, bg='yellow', font=(
            "Times New ROman", 34)).place(x=450, y=130)
        txt_Passowrd = Entry(self.root, textvariable=self.var_password_admin,
                             show='*', bg="yellow", font=("Times New ROman", 34)).place(x=450, y=210)

# Login button
        Login_btn = Button(self.root, text="Login ", command=self.admin_login, bd=5, relief="raised", font=(
            "Times New Roman", 40, 'bold'), bg="white", fg="black", cursor='hand2', ).place(x=400, y=340, width=400, height=90)

    def admin_login(self):

        con = sqlite3.connect(database=r'taxi_booking_data.db')
        cur = con.cursor()

        find_user = (
            " SELECT * from admin where admin_ID =? and password_admin=?")
        cur.execute(find_user, [self.var_admin_ID.get(),
                    self.var_password_admin.get()])
        result = cur.fetchall()
        if self.var_admin_ID.get() == "" or self.var_password_admin.get() == "":
            messagebox.showerror(
                "Error", " You must enter the Admin ID and Passowrd", parent=self.root)

        elif result:

            messagebox.showinfo(
                "Login", "SUccessfully Login", parent=self.root)
            self.var_admin_ID.set("")
            self.var_password_admin.set("")

            self.Booking_page()

        else:
            messagebox.showerror(
                "Error", " Please Input valid Admin ID or Password", parent=self.root)

    def Booking_page(self):

        self.Trip = Toplevel(self.root)
        self.Newobject = admin_dashboard(self.Trip)


con = sqlite3.connect(database=r'taxi_booking_data.db')
cur = con.cursor()


def connection():
    con.commit


connection
if __name__ == '__main__':
    root = Tk()
    obj = Admin_Login(root)
    root.mainloop()
