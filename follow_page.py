from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector

def update_follow_info():
    pass



class Follow_Page:
    def __init__(self, master):
        # Create entry forms to update follow_tree view and follow database
        self.status_label = Label(master, text="Status: ")
        self.status_label.grid(row=0, column=0, padx=5, pady=5, sticky=NW)

        self.status_options = ["On Follow", "On Follow", "Give Up", "Transfer to Distributor"]
        self.status_clicked = StringVar()
        self.status_clicked.set(self.status_options[0])
        self.status_entry = OptionMenu(master, self.status_clicked, *self.status_options)
        self.status_entry.grid(row=0, column=1, padx=5, pady=5, sticky=NW)

        self.follow_by_label = Label(master, text="Follow By:")
        self.follow_by_label.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

        self.name_options = ["Tony","Tony", "Jason"]
        self.name_clicked = StringVar()
        self.name_clicked.set(self.name_options[0])
        self.follow_by_entry = OptionMenu(master, self.name_clicked, *self.name_options)
        self.follow_by_entry.grid(row=1, column=1, padx=5, pady=5, sticky=NW)

        self.follow_info_label = Label(master, text="Follow Info: ")
        self.follow_info_label.grid(row=2, column=0, padx=5, pady=5, sticky=NW)

        self.follow_info_text = Text(master, width=40, height=9, font=("Helvetica", 12), undo=True)
        self.follow_info_text.grid(row=2, column=1, padx=5, pady=5, sticky=NW, columnspan=2)

        # When select existing info , the button is "update", default is "Create new info"
        self.follow_update_button = Button(master, text="Update", bootstyle="success", cursor="hand2", command=update_follow_info)
        self.follow_update_button.grid(row=0, column=2, padx=5, pady=5, sticky=NE)



class Follow_Info_Input_Page:
    pass


