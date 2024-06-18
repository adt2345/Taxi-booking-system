
from tkinter import *
from tkinter.font import BOLD
import time
import sys
from tkinter import ttk, messagebox
import time
import sqlite3


class admin_dashboard:

    def __init__(self, root):

        self.root = root
        self.root.geometry('1200x550+50+50')
        self.root.title('Taxi Booking Service -Welcome Admin')
        self.root.config(bg='white')
        self.root.resizable(0, 0)
# Photos/Icons
        photo_icon = PhotoImage(file='Image/small.png')
        self.root.iconphoto(False, photo_icon)

 # headline
        admin_headline_label = Label(self.root, text='Admin Dashboard', fg='Black', bg="Yellow", font=(
            "Times New Roman", 50, BOLD)).place(x=10, y=10, width=1178)
# label
        status_label = Label(self.root, text="Status ", fg='Black', bg="white",
                             font=("Times New Roman", 30, BOLD)).place(x=600, y=100, width=200)

# all variable

        self.var_trip_ID = StringVar()
        self.var_Booking_date = StringVar()
        self.var_Pickup_date = StringVar()
        self.var_Pickup_time = StringVar()
        self.var_Pickup_address = StringVar()
        self.var_Drop_off_address = StringVar()
        self.var_Status = StringVar()
# text box
        status_txt_box = Entry(self.root, textvariable=self.var_Status, bg='white', font=(
            "Times New ROman", 30)).place(x=850, y=100, width=200)

# Button
        update_btn = Button(self.root, text="Halt", command=self.HaltTrip, font=(
            "Times New Roman", 40, 'bold'), bg="black", fg="yellow", cursor='hand2', ).place(x=10, y=100, width=380, height=90)

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

    def HaltTrip(self):

        connection

        if self.var_trip_ID.get() == "":
            messagebox.showerror(
                "Error", "Trip ID must be required", parent=self.root)

        else:
            cur.execute("Select * from trip where trip_ID =?",
                        (self.var_trip_ID.get(), ))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", " There is no trip id u entered", parent=self.root)
            else:
                cur.execute("Update trip set status='Hold' where trip_ID=?", (
                    self.var_trip_ID.get(),
                ))
                con.commit()
                messagebox.showinfo(
                    "Booking", "Successfullly Booking Done", parent=self.root)
                self.clear()
                self.show()


con = sqlite3.connect(database=r'taxi_booking_data.db')
cur = con.cursor()


def connection():
    con.commit


connection

if __name__ == '__main__':
    root = Tk()
    obj = admin_dashboard(root)
    root.mainloop()
