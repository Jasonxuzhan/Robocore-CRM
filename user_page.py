import tkinter as tk
import ttkbootstrap as ttk
import mysql.connector 

# window
class Create_User(ttk.Window):
    def __init__(self, title, size):
        super().__init__(themename="superhero")
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        self.main_frame = Main_Frame(self)

        self.mainloop()

# frame and widgets
class Main_Frame(ttk.Frame):
     def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.create_widgets()
    
     def clean_entry(self):
        user_name_entry.delete(0, tk.END)
        user_password_entry.delete(0, tk.END)
        user_type_entry.delete(0, tk.END) 
     
     def create_user(self):
         user_name = user_name_entry.get()
         user_password = user_password_entry.get()
         user_type = user_type_entry.get()

         mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "jason121",
            auth_plugin = "mysql_native_password", 
            database = "crmdatabase"
            )

         my_cursor = mydb.cursor()

         sqlstuff = f"""INSERT INTO user_data (
                     User_Name,
                     Password,
                     Type,
                     Generate_Date
                ) VALUES(%s, %s, %s, NOW())"""
    
         record1 = (user_name, user_password, user_type) 
    
         my_cursor.execute(sqlstuff, record1)  
    
         mydb.commit()
         mydb.close()
         
         self.clean_entry()

     def create_widgets(self):
         create_user_frame = ttk.Frame(self)
         create_user_frame.pack(padx=10, pady=10, anchor="nw")

         user_name_label = ttk.Label(create_user_frame, text="User Name: ")
         user_name_label.grid(row=0, column=0, padx=10, pady=10)
         
         global user_name_entry
         user_name_entry = ttk.Entry(create_user_frame)
         user_name_entry.grid(row=0, column=1, padx=10, pady=10)

         user_password_label = ttk.Label(create_user_frame, text="Password: ")
         user_password_label.grid(row=1, column=0, padx=10, pady=10)
         
         global user_password_entry
         user_password_entry = ttk.Entry(create_user_frame)
         user_password_entry.grid(row=1, column=1, padx=10, pady=10)

         user_type_label = ttk.Label(create_user_frame, text="Type: ")
         user_type_label.grid(row=2, column=0, padx=10, pady=10)

         global user_type_entry
         user_type_entry = ttk.Entry(create_user_frame)
         user_type_entry.grid(row=2, column=1, padx=10, pady=10)

         user_create_button = ttk.Button(create_user_frame, text="Create User", command=self.create_user)
         user_create_button.grid(row=3, column=0, padx=10, pady=10)








     

    







































if __name__ == "__main__":
    Create_User("Create user", (600, 600))


