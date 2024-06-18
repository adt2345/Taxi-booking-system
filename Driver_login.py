from sqlite3.dbapi2 import connect
from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import sqlite3
from Driver_dashboard import Driver_dashboard


class Driver_login:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x550')
        self.root.title('  Taxi Booking Service"')
        self.root.config(bg='white')


# CUstomer login back ground photo
#        self.photo_login_bg = PhotoImage(file="Image/taxi_back_login.png")
 #       self.photo_login_bg_label = Label(self.root, image=self.photo_login_bg).place(
  #          x=10, y=0, width=1200, height=550)

# username and password Label
        Driver_ID_label = Label(self.root, text='Driver ID :- ', fg='black',
                                bg='white', font=("Times New Roman", 30,)).place(x=130, y=130)
        Password_label = Label(self.root, text='Password :-', fg='black',
                               bg='white', font=("Times New Roman", 30,)).place(x=130, y=210)

# Variables
        self.var_driver_ID = StringVar()
        self.var_password_driver = StringVar()
# Text box
        txt_driver_ID = Entry(self.root, textvariable=self.var_driver_ID, bg='yellow', font=(
            "Times New ROman", 34)).place(x=450, y=130)
        txt_Passowrd = Entry(self.root, textvariable=self.var_password_driver,
                             show='*', bg="yellow", font=("Times New ROman", 34)).place(x=450, y=210)

# Login button
        Login_btn = Button(self.root, text="Login ", command=self.driver_login, bd=5, relief="raised", font=(
            "Times New Roman", 40,), bg="black", fg="white", cursor='hand2', ).place(x=450, y=340, width=300, height=90)

    def driver_login(self):

        con = sqlite3.connect(database=r'taxi_booking_data.db')
        cur = con.cursor()

        find_user = (
            "SELECT * from driver where driver_ID =? and password_driver =?")
        cur.execute(find_user, [self.var_driver_ID.get(),
                    self.var_password_driver.get()])
        result = cur.fetchall()

        if self.var_driver_ID.get() == "" or self.var_password_driver.get() == "":
            messagebox.showerror(
                "Error", " You must enter the Driver ID and Passowrd", parent=self.root)

        elif result:
            messagebox.showinfo(
                "Login", "SUccessfully Login", parent=self.root)
            self.var_password_driver.set("")
            self.var_driver_ID.set("")
            self.Booking_page()

        else:
            messagebox.showerror(
                "Error", " Please Input valid Driver ID or Password", parent=self.root)

    def Booking_page(self):

        self.Trip = Toplevel(self.root)

        self.Newobject = Driver_dashboard(self.Trip)


con = sqlite3.connect(database=r'taxi_booking_data.db')
cur = con.cursor()


def connection():
    con.commit


connection


if __name__ == '__main__':
    root = Tk()
    obj = Driver_login(root)
    root.mainloop()
