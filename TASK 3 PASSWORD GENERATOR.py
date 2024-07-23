import string
import random
from tkinter import *
from tkinter import messagebox
import re
import sqlite3

# Database setup
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
cursor.execute("SELECT * FROM users")
db.commit()
db.close()

class GUI():
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_passwordlen = IntVar()
        
        master.title('Password Generator')
        master.geometry('660x500')
        master.config(bg='#FF8000')
        master.resizable(False, False)

        self.label = Label(text=":PASSWORD GENERATOR:", anchor=N, fg='darkblue', bg='#FF8000', font='arial 20 bold underline')
        self.label.grid(row=0, column=1)

        self.blank_label1 = Label(text="")
        self.blank_label1.grid(row=1, column=0, columnspan=2)
        
        self.blank_label2 = Label(text="")
        self.blank_label2.grid(row=2, column=0, columnspan=2)    

        self.blank_label2 = Label(text="")
        self.blank_label2.grid(row=3, column=0, columnspan=2)    

        self.user = Label(text="Enter User Name: ", font='times 15 bold', bg='#FF8000', fg='darkblue')
        self.user.grid(row=4, column=0)

        self.textfield = Entry(textvariable=self.n_username, font='times 15', bd=6, relief='ridge')
        self.textfield.grid(row=4, column=1)
        self.textfield.focus_set()

        self.blank_label3 = Label(text="")
        self.blank_label3.grid(row=5, column=0)

        self.length = Label(text="Enter Password Length: ", font='times 15 bold', bg='#FF8000', fg='darkblue')
        self.length.grid(row=6, column=0)

        self.length_textfield = Entry(textvariable=self.n_passwordlen, font='times 15', bd=6, relief='ridge')
        self.length_textfield.grid(row=6, column=1)
        
        self.blank_label4 = Label(text="")
        self.blank_label4.grid(row=7, column=0)
 
        self.generated_password = Label(text="Generated Password: ", font='times 15 bold', bg='#FF8000', fg='darkblue')
        self.generated_password.grid(row=8, column=0)

        self.generated_password_textfield = Entry(textvariable=self.n_generatedpassword, font='times 15', bd=6, relief='ridge', fg='#DC143C')
        self.generated_password_textfield.grid(row=8, column=1)
   
        self.blank_label5 = Label(text="")
        self.blank_label5.grid(row=9, column=0)

        self.blank_label6 = Label(text="")
        self.blank_label6.grid(row=10, column=0)

        self.generate = Button(text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1, font='Verdana 15 bold', fg='#68228B', bg='#BCEE68', command=self.generate_pass)
        self.generate.grid(row=11, column=1)

        self.blank_label5 = Label(text="")
        self.blank_label5.grid(row=12, column=0)

        self.accept = Button(text="ACCEPT", bd=3, relief='solid', padx=1, pady=1, font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0', command=self.accept_fields)
        self.accept.grid(row=13, column=1)

        self.blank_label1 = Label(text="")
        self.blank_label1.grid(row=14, column=1)

        self.reset = Button(text="RESET", bd=3, relief='solid', padx=1, pady=1, font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0', command=self.reset_fields)
        self.reset.grid(row=15, column=1)

    def generate_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        numbers = "1234567890"
        all_chars = list(upper + lower + chars + numbers)
        
        name = self.textfield.get()
        leng = self.length_textfield.get()

        if not leng.isdigit() or int(leng) <= 0:
            messagebox.showerror("Invalid Input", "Please enter a valid password length.")
            return

        leng = int(leng)
        password = ''.join(random.choice(all_chars) for _ in range(leng))
        self.n_generatedpassword.set(password)

        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO users(Username, GeneratedPassword) VALUES (?, ?)", (name, password))
            db.commit()

    def accept_fields(self):
        messagebox.showinfo("Accepted", "Username and Password have been saved.")

    def reset_fields(self):
        self.n_username.set("")
        self.n_passwordlen.set(0)
        self.n_generatedpassword.set("")

if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()
