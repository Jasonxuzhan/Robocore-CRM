from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector



class Login_Page:
    def __init__(self, master):
        self.top = master
        self.top.title("Login Page")

        # Frame in top
        self.input_frame = Frame(self.top)
        self.input_frame.pack()

        # Element in input frame
        global username_entry
        global password_entry

        self.login_label = Label(self.input_frame, text="Robocore CRM System", font=("Times", 12)) 
        self.username_label = Label(self.input_frame, text="username: ")
        self.username_entry = Entry(self.input_frame)
        self.password_label = Label(self.input_frame, text="password: ")
        self.password_entry = Entry(self.input_frame, show="*")
        self.login_button = Button(self.input_frame, text="Login", command=None)

        self.login_label.grid(row=0, column=0, columnspan=2,pady=30) 
        self.username_label.grid(row=1, column=0, padx=20, pady=10)
        self.username_entry.grid(row=1, column=1, padx=20, pady=10)
        self.password_label.grid(row=2, column=0, padx=20, pady=10)
        self.password_entry.grid(row=2, column=1, padx=20, pady=10)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)
    

    


if __name__ == "__main__":
    pass







