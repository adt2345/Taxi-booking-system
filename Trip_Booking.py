from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import time
import sqlite3


class Trip_Booking:
    def __init__(self, root):

        self.root = root
        self.root.geometry('1200x550+50+50')
        self.root.title('  Taxi Booking Service11111111"')
        self.root.config(bg='white')
        self.root.resizable(0, 0)

# Photos/Icons
        photo_icon = PhotoImage(file='Image/small.png')
        self.root.iconphoto(False, photo_icon)

 # headline
        Trip_booking_headline_label = Label(self.root, text='TRIP BOOKING PAGE', fg='Black', font=(
            "Times New Roman", 30, BOLD)).place(x=10, y=0, width=1178)

# labels
        trip_ID = Label(self.root, text='Trip ID :-', fg='Black', bg='white',
                        font=("Times New Roman", 15, BOLD)).place(x=30, y=60)
        Booking_date = Label(self.root, text='Booking Date :-', fg='Black',
                             bg='white', font=("Times New Roman", 15, BOLD)).place(x=30, y=100)

        Pickup_date = Label(self.root, text='Pickup Date :-', fg='Black',
                            bg='white', font=("Times New Roman", 15, BOLD)).place(x=30, y=140)
        Pickup_time = Label(self.root, text='Pickup Time :-', fg='Black',
                            bg='white', font=("Times New Roman", 15, BOLD)).place(x=30, y=180)
        Pickup_adderss = Label(self.root, text='Pickup Address :-', fg='Black',
                               bg='white', font=("Times New Roman", 15, BOLD)).place(x=30, y=220)
        Drop_off_address = Label(self.root, text='Drop Off Address :-', fg='Black',
                                 bg='white', font=("Times New Roman", 15, BOLD)).place(x=30, y=260)
        # Status= Label (self.root  ,text='Status :-',fg='Black',bg = 'white',font=("Times New Roman",15,BOLD)).place(x=30,y=300)


# All variable
        self.var_trip_ID = StringVar()

        self.var_Booking_date = StringVar()
        self.var_Pickup_date = StringVar()
        self.var_Pickup_time = StringVar()
        self.var_Pickup_address = StringVar()
        self.var_Drop_off_address = StringVar()
        self.var_Status = StringVar()
# text box
        txt_trip_ID = Entry(self.root, textvariable=self.var_trip_ID, font=(
            "Times New ROman", 15), highlightthickness=2, highlightbackground='Black').place(x=400, y=60)

        txt_Booking_date = Entry(self.root, textvariable=self.var_Booking_date, font=(
            "Times New ROman", 15), highlightthickness=2, highlightbackground='Black').place(x=400, y=100)
        txt_Pickup_date = Entry(self.root, textvariable=self.var_Pickup_date, font=(
            "Times New ROman", 15), highlightthickness=2, highlightbackground='Black').place(x=400, y=140)
        txt_Pickup_time = Entry(self.root, textvariable=self.var_Pickup_time, font=(
            "Times New ROman", 15), highlightthickness=2, highlightbackground='Black').place(x=400, y=180)
        txt_Pickup_address = Entry(self.root, textvariable=self.var_Pickup_address, font=(
            "Times New ROman", 15), highlightthickness=2, highlightbackground='Black').place(x=400, y=220)
        txt_Drop_off_address = Entry(self.root, textvariable=self.var_Drop_off_address, font=(
            "Times New ROman", 15), highlightthickness=2, highlightbackground='Black').place(x=400, y=260)

# Button
        Book_btn = Button(self.root, text="Book", command=self.save, font=(
            "Times New Roman", 20), bg="Sky Blue", fg="black", cursor='hand2').place(x=950, y=80, width=200)
        Delete_btn = Button(self.root, text="Delete ", command=self.delete, font=(
            "Times New Roman", 20), bg="Red", fg="black", cursor='hand2').place(x=950, y=150, width=200)
        Update_btn = Button(self.root, text="Update ", command=self.update, font=(
            "Times New Roman", 20), bg="Yellow", fg="black", cursor='hand2').place(x=950, y=220, width=200)


# frame
        table_frame = Frame(self.root, bd=3, relief=RIDGE)
        table_frame.place(x=5, y=300, width=1189, height=245)


# Scrool bar
        scrolly = Scrollbar(table_frame, orient=VERTICAL)
        scrollx = Scrollbar(table_frame, orient=HORIZONTAL)

        self.detailTable = ttk.Treeview(table_frame, columns=("trip_ID", "Booking_date", "Pickup_date", "Pickup_time",
                                        "Pickup_address", "Drop_off_address", "Status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.detailTable.xview)
        scrolly.config(command=self.detailTable.yview)

        self.detailTable.heading("trip_ID", text='Trip ID')
        self.detailTable.heading("Booking_date", text='Booking Date')
        self.detailTable.heading("Pickup_date", text='Pickup date')
        self.detailTable.heading("Pickup_time", text='Pickup time')
        self.detailTable.heading("Pickup_address", text='Pickup Address')
        self.detailTable.heading("Drop_off_address", text='Drop off address')
        self.detailTable.heading("Status", text='Status')

        self.detailTable["show"] = "headings"
        self.detailTable.column("trip_ID", width=150)
        self.detailTable.column("Booking_date", width=150)
        self.detailTable.column("Pickup_date", width=150)
        self.detailTable.column("Pickup_time", width=150)
        self.detailTable.column("Pickup_address", width=150)
        self.detailTable.column("Drop_off_address", width=150)
        self.detailTable.column("Status", width=150)

        self.detailTable.pack(fill=BOTH, expand=1)
        self.detailTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def clear(self):
        self.var_trip_ID.set(""),
        self.var_Booking_date.set(""),
        self.var_Pickup_date.set(""),
        self.var_Pickup_time.set(""),
        self.var_Pickup_address.set(""),
        self.var_Drop_off_address.set(""),
        self.var_Status.set(""),

        self.show()

    def show(self):
        try:

            cur.execute("select * from trip")

            rows = cur.fetchall()
            self.detailTable.delete(*self.detailTable.get_children())
            for row in rows:
                self.detailTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error ", f"Save error: {str(ex)}", parent=self.root)

    def get_data(self, ev):

        f = self.detailTable.focus()
        content = (self.detailTable.item(f))
        row = content['values']

        self.var_trip_ID.set(row[0])
        self.var_Booking_date.set(row[1])
        self.var_Pickup_date.set(row[2])
        self.var_Pickup_time.set(row[3])
        self.var_Pickup_address.set(row[4])
        self.var_Drop_off_address.set(row[5])
        self.var_Status.set(row[6])

    def save(self):

        connection

        if self.var_trip_ID.get() == "":
            messagebox.showerror(
                "Error", "Trip ID must be required", parent=self.root)

        else:
            cur.execute("Select * from trip where trip_ID =?",
                        (self.var_trip_ID.get(), ))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", " Trip ID already exists. Type another one", parent=self.root)
            else:
                cur.execute("Insert into trip (trip_ID,Booking_date,Pickup_date,Pickup_time,Pickup_address,Drop_off_address,Status) values (?,?,?,?,?,?,'Pending')", (self.var_trip_ID.get(
                ), self.var_Booking_date.get(), self.var_Pickup_date.get(), self.var_Pickup_time.get(), self.var_Pickup_address.get(), self.var_Drop_off_address.get()))
                con.commit()
                messagebox.showinfo(
                    "Booking", "Successfullly Booking Done", parent=self.root)
                self.clear()
                self.show()

    def delete(self):
        if self.var_trip_ID.get() == "":
            messagebox.showerror(
                "Error", "ID must be required", parent=self.root)

        else:
            cur.execute("Select * from trip where trip_ID=?",
                        (self.var_trip_ID.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid ID", parent=self.root)
            else:
                cosM = messagebox.askyesno(
                    'Confirm', "Do you want to delete?", parent=self.root)
                if cosM == True:
                    cur.execute("delete from trip where trip_ID=?",
                                (self.var_trip_ID.get()))
                    con.commit()
                    messagebox.showinfo(
                        "Delete", "User Delete Successfully", parent=self.root)
                    self.clear()
                    self.show()

    def update(self):

        connection
        if self.var_trip_ID.get() == "":
            messagebox.showerror(
                "Error", "Trip ID must be required", parent=self.root)
        else:
            cur.execute("Select * from trip where trip_ID =?",
                        (self.var_trip_ID.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid ID", parent=self.root)

            else:
                cur.execute("Update trip set  Booking_date=?, Pickup_date=?, Pickup_time=?,Pickup_address = ?, Drop_off_address=?,Status='Pending' where trip_ID=?", (
                    self.var_Booking_date.get(),
                    self.var_Pickup_date.get(),
                    self.var_Pickup_time.get(),

                    self.var_Pickup_address.get(),
                    self.var_Drop_off_address.get(),
                    self.var_trip_ID.get()
                ))
                con.commit()
                messagebox.showinfo(
                    "Error", "Successfully Update", parent=self.root)
                self.clear()
                self.show()


con = sqlite3.connect(database=r'taxi_booking_data.db')
cur = con.cursor()


def connection():

    con.commit()


connection

if __name__ == '__main__':
    root = Tk()
    obj = Trip_Booking(root)
    root.mainloop()
