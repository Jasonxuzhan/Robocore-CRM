from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import edit_page
import follow_page
import treeview
import notice
import user_page

# Button functions:
def open_customer_edit_page() -> object:
    customer_edit_page = edit_page.Edit_Page()
    return customer_edit_page

def open_follow_create_page() -> object:
    follow_create_page = treeview.Follow_Info_Input_Page()
    return follow_create_page

def create_user() -> object:
    user_page.Create_User("Create User", (600, 600))
    
# Pages:
def customer_leads_treeview(master) -> object:
    customer_leads_tree = treeview.Leads_Treeview(master)
    customer_leads_tree.query_leads_information_table()
    return customer_leads_tree

def customer_follow_treeview(master: object) -> object:
    customer_follow_tree = treeview.Follow_Treeview(master)
    customer_follow_tree.query_customer_follow_table() 
    return customer_follow_tree

def customer_follow_input(master: object) -> object:
    global customer_follow_input_page
    customer_follow_input_page = follow_page.Follow_Page(master)   
    return customer_follow_input_page

def notice_label(master: object) -> object:
    notice_label_on_top = notice.Notice_Item(master)
    return notice_label_on_top


class Index_Page:
    """Index Page 的页面布局"""
    def __init__(self, master, user_name="" , user_type=""):
        # Main Frame
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.user_name = user_name
        self.user_type = user_type

        # Inner Frames in Mainframe
        self.inner_frame_1 = Frame(self.myFrame)
        self.inner_frame_1.pack(side=LEFT)

        self.seprator = Separator(self.myFrame, orient="vertical")
        self.seprator.pack(fill=Y, side=LEFT, padx=5)

        self.inner_frame_2 = Frame(self.myFrame)
        self.inner_frame_2.pack(side=LEFT)

        # Element in innerframe_1 
        self.crm_label = Label(self.inner_frame_1, text="Robocore CRM", font=("Times", 12))
        self.crm_label.pack(fill=X, padx=5, pady=10, anchor=NW)

        self.seprator = Separator(self.inner_frame_1, orient="horizontal")
        self.seprator.pack(fill=X, pady=20)

        self.user_info_frame = Labelframe(self.inner_frame_1, text="Login Information:", relief=FLAT)
        self.user_info_frame.pack(padx=5, pady=10, anchor=NW)

        self.seprator = Separator(self.inner_frame_1, orient="horizontal")
        self.seprator.pack(fill=X, pady=10)
        
        self.options_frame = Labelframe(self.inner_frame_1, text="Optons:", relief=FLAT)
        self.options_frame.pack(padx=5, pady=10, anchor=NW)

        # Spare frame 备用Frame
        self.spare_frame = Labelframe(self.inner_frame_1, text="Admin Options:", relief=FLAT)
        self.spare_frame.pack(padx=5, pady=10, anchor=NW)
  
        # Elements in user_info_frame
        self.user_name_button = Button(self.user_info_frame, text=self.user_name, bootstyle="info-link", cursor="hand2")
        self.user_name_button.pack(padx=5, pady=10, anchor=W)

        self.user_type_button = Button(self.user_info_frame, text=self.user_type, bootstyle="info-link", cursor="hand2")
        self.user_type_button.pack(padx=5, pady=10, anchor=W)

        # Elements in options_frame
        self.create_customer_button = Button(self.options_frame, text="Create Customer", cursor="hand2", bootstyle="info-link", command=open_customer_edit_page) # command from edit_page.py
        self.create_customer_button.pack(padx=5, pady=10, anchor=W)

        self.create_follow_info_button = Button(self.options_frame, text="Create New Follow", cursor="hand2", bootstyle="info-link", command=open_follow_create_page) # command from follow_page.py
        self.create_follow_info_button.pack(padx=5, pady=10, anchor=W)

        # Elements in spqre frame 备用元素，占位用
        self.create_user_button = Button(self.spare_frame, text="Create User", cursor="hand2", bootstyle="info-link", command=create_user)
        self.create_user_button.pack(padx=5, pady=20)

        self.spare_label = Label(self.spare_frame, text="")
        self.spare_label.pack(padx=5, pady=20)

        self.spare_label = Label(self.spare_frame, text="")
        self.spare_label.pack(padx=5, pady=20)

        self.spare_label = Label(self.spare_frame, text="")
        self.spare_label.pack(padx=20, pady=20)

        # Element is innerframe_2
        notice_label(self.inner_frame_2) # from notice.py
        
        self.leads_treeview_frame = Frame(self.inner_frame_2)
        self.leads_treeview_frame.pack(padx=5, pady=5)

        self.seprator = Separator(self.inner_frame_2, orient="horizontal")
        self.seprator.pack(fill=X, pady=10)

        self.follow_frame = Frame(self.inner_frame_2)
        self.follow_frame.pack(side=LEFT, padx=5,pady=5)

        # Element in leads treeview frame 
        customer_leads_treeview(self.leads_treeview_frame) # from leads_treeview.py

        # Elements in follow frame
        self.follow_treeview_frame = Frame(self.follow_frame)
        self.follow_treeview_frame.pack(side=LEFT, padx=5, pady=5)

        self.follow_input_frame = Frame(self.follow_frame)
        self.follow_input_frame.pack(side=LEFT, padx=5, pady=5)

        # Element in follow treeview frame 
        customer_follow_treeview(self.follow_treeview_frame) # from follow_treeview.py
        
        # Element in follow input labelframe     
        customer_follow_input(self.follow_input_frame) # from follow_page.py

def main_page():
    root = Window(themename="superhero")
    root.title("Robocore CRM System V1.0")
    root.iconbitmap()
    root.geometry("1700x800+100+100")
    robocore_index = Index_Page(root, user_name="Admin" , user_type="Admin")
    root.mainloop()
    return robocore_index  

if __name__ == "__main__":
    main_page()

