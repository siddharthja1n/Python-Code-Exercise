from tkinter import *
from tkinter import messagebox as msg
from PIL import ImageTk, Image
import sqlite3


# establish connection with database
# creates database if not already exist
conn = sqlite3.connect("phone_book.db")

# creating cursor to execute queries
c = conn.cursor()

# create table
# excute just once to create table in the database
# c.execute("""CREATE TABLE contact (
#         first_name text,
#         last_name text,
#         email text,
#         phone integer
#         )
#         """)


# commit the queries into database
conn.commit()

# closes the connection
conn.close()

class Phone:
    def __init__(self, root):    
        root.title("Phone Book")
        root.geometry("350x450+200+150")
        root.resizable(False, False)

        # header frame
        self.frame_header = Frame(root)
        self.frame_header.pack()

        self.logo = ImageTk.PhotoImage((Image.open("phone_book.jpg")).resize((50,50), Image.ANTIALIAS))
        self.logo_label = Label(self.frame_header, image = self.logo)
        self.logo_label.grid(row=0, column=0, sticky=W)

        self.header_label = Label(self.frame_header, text="Welcome to Phone book. Enter your details....")
        self.header_label.grid(row=0, column=1, sticky=E)

        # content frame
        self.frame_content = Frame(root)
        self.frame_content.pack()

        self.f_name_label = Label(self.frame_content, text="First Name")
        self.f_name_label.grid(row=0, column=0, pady=(10, 0), sticky=E)
        self.l_name_label = Label(self.frame_content, text="Last Name")
        self.l_name_label.grid(row=1, column=0, sticky=E)
        self.email_label = Label(self.frame_content, text="Email")
        self.email_label.grid(row=2, column=0, sticky=E)
        self.number_label = Label(self.frame_content, text="Contact")
        self.number_label.grid(row=3, column=0, sticky=E)
        self.id_label = Label(self.frame_content, text="Enter ID")
        self.id_label.grid(row=6, column=0, pady=(10,0), sticky=E)

        self.f_name_entry = Entry(self.frame_content, width = 35)
        self.f_name_entry.grid(row=0, column=1, padx = 10, pady=(10, 0))
        self.l_name_entry = Entry(self.frame_content, width = 35)
        self.l_name_entry.grid(row=1, column=1, padx = 10)
        self.email_entry = Entry(self.frame_content, width = 35)
        self.email_entry.grid(row=2, column=1, padx = 10)
        self.number_entry = Entry(self.frame_content, width = 35)
        self.number_entry.grid(row=3, column=1, padx = 10)
        self.id_entry = Entry(self.frame_content, width = 35)
        self.id_entry.grid(row=6, column=1, padx = 10, pady=(10,0))

        self.query_label = Label(self.frame_content, text = "", font = ('Arial', 16))
        self.query_label.grid(row=9, column=0, columnspan=2, pady = 10)

        self.save_btn = Button(self.frame_content, text = "Save", command = self.save)
        self.save_btn.grid(row=4, column=0, padx=10, ipadx=15, pady=(10, 0))
        self.reset_btn = Button(self.frame_content, text = "Reset", command = self.reset)
        self.reset_btn.grid(row=4, column=1, padx=10, ipadx=13, pady=(10, 0), sticky=W)
        self.view_btn = Button(self.frame_content, text="View Records", command = self.view)
        self.view_btn.grid(row=5, column=0, columnspan=2, pady=(10,0), padx=10, ipadx=110)
        self.edit_btn = Button(self.frame_content, text="Edit Record", command = self.edit)
        self.edit_btn.grid(row=7, column=0, columnspan=2, pady=(10,0), padx=10, ipadx=115)
        self.delete_btn = Button(self.frame_content, text="Delete Record", command = self.delete)
        self.delete_btn.grid(row=8, column=0, columnspan=2, pady=(10,0), padx=10, ipadx=108)


    # function to save new records
    # save button save_btn
    def save(self):
        try:
            if(self.f_name_entry.get() == ''):
                msg.showerror('No first name', "You can't leave first name empty")

            elif(self.number_entry.get() == ''):
                msg.showerror('No contact number', "You can't leave contact number empty")

            else:
                int(self.number_entry.get())
                self.answer = msg.askyesno('Save new contact', 'Do you want to save record?')

                if(self.answer == True):
                    conn = sqlite3.connect("phone_book.db")

                    # creating cursor to execute queries
                    c = conn.cursor()

                    c.execute("INSERT INTO contact VALUES(:fname, :lname, :email, :number)",
                    {
                        'fname' : self.f_name_entry.get(),
                        'lname' : self.l_name_entry.get(),
                        'email' : self.email_entry.get(),
                        'number' : self.number_entry.get(),
                    })

                    # commit the queries into database
                    conn.commit()

                    # closes the connection
                    conn.close()

                    self.f_name_entry.delete(0, END)
                    self.l_name_entry.delete(0, END)
                    self.email_entry.delete(0, END)
                    self.number_entry.delete(0, END)
        except ValueError:
            msg.showerror('Incorrect contact number', "Contact number must contain only digits")

    # function to reset the fields
    # reset button reset_btn
    def reset(self):
        self.f_name_entry.delete(0, END)
        self.l_name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.number_entry.delete(0, END)

    # function to view records
    # view button view_btn
    def view(self):
        conn = sqlite3.connect("phone_book.db")

        # creating cursor to execute queries
        c = conn.cursor()

        c.execute("SELECT *, oid FROM contact")
        records = c.fetchall()

        self.view_format = ''
        for record in records:
            self.view_format += str(record[4]) + ". " + str(record[0]) + " - " + str(record[3]) + "\n"

        self.query_label.config(text=self.view_format)

        # commit the queries into database
        conn.commit()

        # closes the connection
        conn.close()

    # function to delete record
    # delete button delete_btn
    def delete(self):
        self.answer = msg.askokcancel('Delete record', 'Are you sure?\nDeleted record will not be recovered!')

        if self.answer == 1:
            conn = sqlite3.connect("phone_book.db")

            # creating cursor to execute queries
            c = conn.cursor()

            c.execute("DELETE FROM contact WHERE oid = " + self.id_entry.get())

            # commit the queries into database
            conn.commit()

            # closes the connection
            conn.close()

            self.id_entry.delete(0, END)

    # function to edit record
    # edit button edit_btn
    def edit(self):
        global editor
        editor = Tk()
        editor.title("Update Phone Book")
        editor.geometry("350x250+560+150")
        editor.resizable(False, False)

        conn = sqlite3.connect("phone_book.db")

        # creating cursor to execute queries
        c = conn.cursor()

         # header frame
        # self.frame_header = Frame(editor)
        # self.frame_header.pack()

        # self.logo = ImageTk.PhotoImage((Image.open("python_logo.gif")).resize((50,50), Image.ANTIALIAS))
        # self.logo_label = Label(self.frame_header, image = self.logo)
        # self.logo_label.grid(row=0, column=0, sticky=W)

        # self.header_label = Label(self.frame_header, text="Welcome to Phone book. Please enter your details.")
        # self.header_label.grid(row=0, column=1, sticky=E)

        # content frame
        self.frame_content_editor = Frame(editor)
        self.frame_content_editor.pack()

        self.f_name_label_editor = Label(self.frame_content_editor, text="First Name")
        self.f_name_label_editor.grid(row=0, column=0, pady=(10, 0), sticky=E)
        self.l_name_label_editor = Label(self.frame_content_editor, text="Last Name")
        self.l_name_label_editor.grid(row=1, column=0, sticky=E)
        self.email_label_editor = Label(self.frame_content_editor, text="Email")
        self.email_label_editor.grid(row=2, column=0, sticky=E)
        self.number_label_editor = Label(self.frame_content_editor, text="Contact")
        self.number_label_editor.grid(row=3, column=0, sticky=E)

        global f_name_entry_editor
        global l_name_entry_editor
        global email_entry_editor
        global number_entry_editor
        global record_id
        self.record_id = self.id_entry.get()

        self.f_name_entry_editor = Entry(self.frame_content_editor, width = 35)
        self.f_name_entry_editor.grid(row=0, column=1, padx = 10, pady=(10, 0))
        self.l_name_entry_editor = Entry(self.frame_content_editor, width = 35)
        self.l_name_entry_editor.grid(row=1, column=1, padx = 10)
        self.email_entry_editor = Entry(self.frame_content_editor, width = 35)
        self.email_entry_editor.grid(row=2, column=1, padx = 10)
        self.number_entry_editor = Entry(self.frame_content_editor, width = 35)
        self.number_entry_editor.grid(row=3, column=1, padx = 10)

        c.execute("SELECT *, oid FROM contact WHERE oid = " + self.id_entry.get())
        self.records = c.fetchall()

        for record in self.records:
            self.f_name_entry_editor.insert(0, record[0])
            self.l_name_entry_editor.insert(0, record[1])
            self.email_entry_editor.insert(0, record[2])
            self.number_entry_editor.insert(0, record[3])
        
        # commit the queries into database
        conn.commit()

        # closes the connection
        conn.close()

        self.update_btn_editor = Button(self.frame_content_editor, text = "Update", command = self.update)
        self.update_btn_editor.grid(row=4, column=0, padx=10, ipadx=15, pady=(10, 0))
        self.cancel_btn_editor = Button(self.frame_content_editor, text = "Cancel", command = self.cancel)
        self.cancel_btn_editor.grid(row=4, column=1, padx=10, ipadx=15, pady=(10, 0), sticky=W)

    # function to update edited record
    # update button update_btn_editor
    def update(self):
        conn = sqlite3.connect("phone_book.db")

        # creating cursor to execute queries
        c = conn.cursor()
        try:
            if(self.f_name_entry_editor.get() == ''):
                msg.showerror('No first name', "You can't leave first name empty")

            elif(self.number_entry_editor.get() == ''):
                msg.showerror('No contact number', "You can't leave contact number empty")

            else:
                int(self.number_entry_editor.get())
                c.execute("""UPDATE contact SET
                    first_name = :first,
                    last_name = :last,
                    email = :email,
                    phone = :phone

                    WHERE oid = :oid""",
                {
                    'first': self.f_name_entry_editor.get(),
                    'last' : self.l_name_entry_editor.get(),
                    'email' : self.email_entry_editor.get(),
                    'phone' : self.number_entry_editor.get(),
                    'oid' : self.record_id
                }
                )
        
                # commit the queries into database
                conn.commit()

                # closes the connection
                conn.close()

                # close edit page after record is updated
                editor.destroy()
        except ValueError:
            msg.showerror('Incorrect contact number', "Contact number must contain only digits")

    # function to close editor page without editing
    # cancel button cancel_btn_editor
    def cancel(self):
        editor.destroy()

def main():            
    
    master = Tk()
    ph = Phone(master)
    master.mainloop()
    
if __name__ == "__main__": 
    main()
