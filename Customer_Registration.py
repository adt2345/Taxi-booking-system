from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import sqlite3

# GUI


class Customer_Registration:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x550+50+50')
        self.root.title(' Taxi Booking Service')
        self.root.config(bg='white')

# Icon
        photo_icon = PhotoImage(file='Image/small.png')
        self.root.iconphoto(False, photo_icon)

# Label
        registration_headline_label = Label(self.root, text='REGISTRATION FORM', fg='Black', font=(
            "Times New Roman", 40, "bold")).place(x=300, y=10)
        customer_user_ID = Label(self.root, text='Customer ID :-', fg='Black',
                                 bg='white', font=("Times New Roman", 20,)).place(x=30, y=100)
        Full_name = Label(self.root, text='Full Name :-', fg='Black',
                          bg='white', font=("Times New Roman", 20,)).place(x=30, y=140)
        Address = Label(self.root, text='Address :-', fg='Black',
                        bg='white', font=("Times New Roman", 20,)).place(x=30, y=180)
        Email = Label(self.root, text='Email :-', fg='Black', bg='white',
                      font=("Times New Roman", 20,)).place(x=30, y=220)
        Contact_number = Label(self.root, text='Contact no. :-', fg='Black',
                               bg='white', font=("Times New Roman", 20,)).place(x=30, y=260)
        Card_info = Label(self.root, text='Card Info :-', fg='Black',
                          bg='white', font=("Times New Roman", 20,)).place(x=30, y=300)
        Password = Label(self.root, text='Password :-', fg='Black',
                         bg='white', font=("Times New Roman", 20,)).place(x=30, y=340)
        Gender = Label(self.root, text='Gender :- ', fg='Black',
                       bg='white', font=("Times New Roman", 20,)).place(x=30, y=380)

# Variables
        self.var_customer_user_ID = StringVar()
        self.var_Full_name = StringVar()
        self.var_Address = StringVar()
        self.var_Email = StringVar()
        self.var_Contact_number = StringVar()
        self.var_Card_info = StringVar()
        self.var_Password = StringVar()
        self.var_Gender = StringVar()

# TExt box
        txt_customer_user_ID = Entry(self.root, textvariable=self.var_customer_user_ID, font=(
            "Times New ROman", 20)).place(x=350, y=100)
        txt_Full_name = Entry(self.root, textvariable=self.var_Full_name, font=(
            "Times New ROman", 20)).place(x=350, y=140)
        txt_Address = Entry(self.root, textvariable=self.var_Address, font=(
            "Times New ROman", 20)).place(x=350, y=180)
        txt_Email = Entry(self.root, textvariable=self.var_Email, font=(
            "Times New ROman", 20)).place(x=350, y=220)
        txt_Contact_number = Entry(self.root, textvariable=self.var_Contact_number, font=(
            "Times New ROman", 20)).place(x=350, y=260)
        txt_Card_info = Entry(self.root, textvariable=self.var_Card_info, font=(
            "Times New ROman", 20)).place(x=350, y=300)
        txt_Passowrd = Entry(self.root, textvariable=self.var_Password,
                             show='*', font=("Times New ROman", 20)).place(x=350, y=340)

# Radio button for Gender
        txt_gender = ttk.Combobox(self.root, textvariable=self.var_Gender, values=(
            "Select", "Male", "Female", "Others"), state='readonly', justify=CENTER, font=("Times New Roman", 20))
        txt_gender.place(x=350, y=380, width=150, height=30)
        txt_gender.current(0)
# SEMICOLON LABEL
        '''semicolon0= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=120)
                semicolon1= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=180)
                semicolon2= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=240)
                semicolon3= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=300)
                semicolon4= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=360)
                semicolon5= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=420)
                semicolon6= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=480)
                semicolon7= Label (self.root,text=':-',fg='Black',bg = 'white',font=("Times New Roman",35,"bold")).place(x=300,y=540)'''
# Button
        Save_btn = Button(self.root, text="Save ", command=self.save, bd=5, relief="raised", font=(
            "Times New Roman", 30), bg="Sky Blue", fg="black", cursor='hand2').place(x=600, y=450, width=200, height=50)

    def save(self):
        connection
        if self.var_customer_user_ID.get() == "":
            messagebox.showerror(
                "Error", "Customer ID must be required", parent=self.root)

        else:
            cur.execute("select * from customer where customer_user_ID=?",
                        (self.var_customer_user_ID.get()))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "Customer Id already exists. Try different", parent=self.root)

            else:
                cur.execute("Insert into customer ( customer_user_ID,Full_name,Address, Email, Contact_number, Card_info, Password, Gender) values (?, ?, ?, ?, ? , ? , ? , ?)",
                            (self.var_customer_user_ID.get(), self.var_Full_name.get(), self.var_Address.get(), self.var_Email.get(), self.var_Contact_number.get(), self.var_Card_info.get(),
                             self.var_Password.get(), self.var_Gender.get()))
                con.commit()
                messagebox.showinfo(
                    "Registration", "Successfully Registered", parent=self.root)


con = sqlite3. connect(database=r'taxi_booking_data.db')
cur = con.cursor()


def connection():

    con.commit()


connection()

if __name__ == '__main__':
    root = Tk()
    obj = Customer_Registration(root)
    root.mainloop()
