from Driver_login import Driver_login
from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import sqlite3
from Customer_Registration import Customer_Registration
from Customer_login import Customer_login
from Admin_Login import Admin_Login


con = sqlite3. connect(database=r'taxi_booking_data.db')
cur = con.cursor()
# GUI


class Main_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x750+150+0')
        self.root.title(' Taxi Booking Service"')
        self.root.config(bg='white')
# Photos/Icons
        photo_icon = PhotoImage(file='Image/small.png')
        self.root.iconphoto(False, photo_icon)

        self.photo_bg = PhotoImage(file='Image/taxi_back.png')
        self.photo_bg_label = Label(self.root, image=self.photo_bg).place(
            x=550, y=100, width=640, height=600)

# Label
        headline_label = Label(self.root, text='Welcome to our ONLINE TAXI SERVICE', fg='Black', font=(
            "Times New Roman", 40, "bold")).place(x=100, y=10)
        slash_customer = Label(self.root, text="/", font=("Times New Roman", 40),
                               bg="White", fg="Blue").place(x=250, y=140, width=50)

        only_for_customer = Label(self.root, text="For Customer", font=(
            "Times New Roman", 22), bg="White", fg="black").place(x=50, y=100,)
        only_for_admin = Label(self.root, text="For Admin", font=(
            "Times New Roman", 22), bg="White", fg="black").place(x=50, y=220,)
        only_for_driver = Label(self.root, text="For Driver", font=(
            "Times New Roman", 22), bg="White", fg="black").place(x=300, y=220,)
        discription_label = Label(self.root, text='Online Taxi Booking Service', font=(
            "Times New Roman", 20), bg="White", fg="black").place(x=30, y=320)

        point_label = Label(self.root, text="Quick & easy way to book your taxi.",
                            font=("Times New Roman", 20), bg="White", fg="black").place(x=0, y=450)
        point_label1 = Label(self.root, text="Simple application design for easier to use for ",
                             font=("Times New Roman", 20), bg="White", fg="black").place(x=0, y=500)
        point_label2 = Label(self.root, text="our users. ", font=(
            "Times New Roman", 20), bg="White", fg="black").place(x=15, y=550)
        point_label3 = Label(self.root, text="Frequent offers and promotional rides.",
                             font=("Times New Roman", 20), bg="White", fg="black").place(x=0, y=600)
        contact_number_label = Label(self.root, text="Contact us :- 01-xoxoxo, +977 9893909019, TaxiService@gmail.com",
                                     font=("Times New ROman", 15), fg='black').place(x=550, y=700)


# Button
        sing_up_button_for_customer = Button(self.root, text="Login", command=self.customer_login, font=(
            "Times New Roman", 22), bg="White", fg="Blue", cursor='hand2').place(x=30, y=140, width=200)
        sing_in_button_for_customer = Button(self.root, text="Register ", command=self.customer_registration, font=(
            "Times New Roman", 22), bg="White", fg="Blue", cursor='hand2').place(x=300, y=140, width=200)
        sing_up_button_for_admin = Button(self.root, text="Login ", command=self.admin_login, font=(
            "Times New Roman", 22), bg="White", fg="Blue", cursor='hand2').place(x=30, y=260, width=200)
        sing_up_button_for_driver = Button(self.root, text="Login ", command=self.driver_login, font=(
            "Times New Roman", 22), bg="White", fg="Blue", cursor='hand2').place(x=300, y=260, width=200)

 # BUtton Command function
    def customer_registration(self):
        self.customer_registration_window = Toplevel(self.root)
        self.Newobject = Customer_Registration(
            self.customer_registration_window)

    def customer_login(self):
        self.customer_login_window = Toplevel(self.root)
        self.Newobject = Customer_login(self.customer_login_window)

    def admin_login(self):
        self.admin_login_window = Toplevel(self.root)
        self.Newobject = Admin_Login(self.admin_login_window)

    def driver_login(self):
        self.driver_login_window = Toplevel(self.root)
        self.Newobject = Driver_login(self.driver_login_window)


# main
if __name__ == '__main__':
    root = Tk()
    obj = Main_System(root)
    root.mainloop()
