from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector
from index import Index_Page

class LoginPage(Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.title("Login Page")
        self.geometry("400x300+200+200")
        self.grab_set()  # Make the login window modal

        # Frame in top
        self.input_frame = Frame(self)
        self.input_frame.pack(pady=20)

        # Element in input frame
        self.login_label = Label(self.input_frame, text="Robocore CRM System", font=("Times", 12))
        self.username_label = Label(self.input_frame, text="username: ")
        self.username_entry = Entry(self.input_frame)
        self.password_label = Label(self.input_frame, text="password: ")
        self.password_entry = Entry(self.input_frame, show="*")
        self.login_button = Button(self.input_frame, text="Login", command=self.login_button)

        self.login_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.username_label.grid(row=1, column=0, padx=10, pady=5)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_label.grid(row=2, column=0, padx=10, pady=5)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)

    def login_button(self):
        username = "123"
        password = "123"
        if self.username_entry.get() == username and self.password_entry.get() == password:
            self.callback()  # Call the callback function to initialize the main page
            self.destroy()  # Close the login window
        else:
            messagebox.showerror(title="Login Failure", message="Login Failure")

class MainPage(Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Robocore CRM System V1.0")
        self.iconbitmap()  # 你可以在这里添加路径到你的图标文件
        self.geometry("1700x800+100+100")
        self.withdraw()  # Hide the main window initially

        # Create and display the login page
        LoginPage(self, self.show_main_page)

    def show_main_page(self):
        self.deiconify()  # Show the main window
        robocore_index = Index_Page(self, user_name="Admin", user_type="Admin")

def main():
    app = MainPage()
    app.mainloop()

# 程序入口
if __name__ == "__main__":
    main()

