import login
import index
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox

# theme_names = ["sandstone", "united", "lumen", "solar", "superhero", "darkly"] 
# root = Window(themename=theme_names[4])
# root.title("Robocore CRM System V1.0")
# root.iconbitmap()
# root.geometry("1700x800")


def main_page():
    root = Window(themename="superhero")
    root.title("Robocore CRM System V1.0")
    root.iconbitmap()
    root.geometry("1700x800")
    robocore_index = index.Index_Page(root, user_name="Jason" , user_type="Admin")
    root.mainloop()
    return robocore_index  

def log_page():
    root = Window(themename="superhero")
    root.title("Robocore CRM System Login")
    root.iconbitmap()
    root.geometry("400x400")
    global robocore_log
    robocore_log = login.Login_Page(root)
    robocore_log.login_button.configure(command=lambda:[root.destroy(), main_page()])
    root.mainloop()
    return robocore_log


# def login_btn():    
#     username = "123"
#     password = "123"

#     if robocore_log.username_entry.get() == username and robocore_log.password_entry.get() == password:
#         root.destroy() 
#     else:
#         messagebox.showerror(title="Login Failure", message="Login Failure")

if __name__ == "__main__":
    log_page()

    

    
