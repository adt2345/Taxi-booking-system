
from sqlite3.dbapi2 import connect
from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import sqlite3

from Trip_Booking import Trip_Booking


# GUI
class Customer_login:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x550')
        self.root.title('  Taxi Booking Service"')
        self.root.config(bg='white')

# Icon
        photo_icon = PhotoImage(file='Image/small.png')
        self.root.iconphoto(False, photo_icon)


# CUstomer login back ground photo
  #      self.photo_login_bg = PhotoImage(file="Image/taxi_back_login.png")
     #   self.photo_login_bg_label = Label(self.root, image=self.photo_login_bg).place(
     #       x=10, y=0, width=1200, height=550)

# username and password Label
        customer_user_ID_label = Label(self.root, text='Customer ID :- ', fg='Black',
                                       bg='white', font=("Times New Roman", 30,)).place(x=130, y=130)
        Password_label = Label(self.root, text='Password        :-', fg='Black',
                               bg='white', font=("Times New Roman", 30,)).place(x=130, y=210)

# Variables
        self.var_customer_user_ID = StringVar()
        self.var_Password = StringVar()
# Text box
        txt_customer_user_ID = Entry(self.root, textvariable=self.var_customer_user_ID, bg='yellow', font=(
            "Times New ROman", 34)).place(x=450, y=130)
        txt_Passowrd = Entry(self.root, textvariable=self.var_Password, show='*',
                             bg="yellow", font=("Times New ROman", 34)).place(x=450, y=210)

# Login button
        Login_btn = Button(self.root, text="Login ", command=self.customer_login, bd=5, relief="raised", font=(
            "Times New Roman", 40,), bg="black", fg="yellow", cursor='hand2', ).place(x=400, y=340, width=400, height=90)

    def customer_login(self):
        con = sqlite3.connect(database=r'taxi_booking_data.db')
        cur = con.cursor()
        try:
            find_user = (
                "SELECT * from customer where customer_user_ID =? and Password =?")
            cur.execute(
                find_user, [self.var_customer_user_ID.get(), self.var_Password.get()])
            result = cur.fetchall()
        except Exception as ex:
            messagebox.showerror("Error", 'Error due to : ', parent=self.root)

        try:
            cur.execute("Select * from customer")

            if self.var_customer_user_ID.get() == "" or self.var_Password.get() == "":
                messagebox.showerror(
                    "Error", " You must enter the Customer ID and Passowrd", parent=self.root)

            elif result:
                messagebox.showinfo(
                    "Login", "SUccessfully Login", parent=self.root)
                self.var_Password.set("")
                self.var_customer_user_ID.set("")
                self.Booking_page()

            else:
                messagebox.showerror(
                    "Error", " Please Input valid Customer ID or Password", parent=self.root)

        except Exception as ex:
            messagebox.showerror(
                "Error", "Error ddfggue to :", parent=self.root)

    def Booking_page(self):

        self.Trip = Toplevel(self.root)

        self.Newobject = Trip_Booking(self.Trip)
        # Trip_Booking(self.Trip)
        # self.newobj = Testpage()


con = sqlite3.connect(database=r'taxi_booking_data.db')
cur = con.cursor()


def connection():
    con.commit


connection


if __name__ == '__main__':
    root = Tk()
    obj = Customer_login(root)
    root.mainloop()
