from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox

class Follow_Page:
    def __init__(self, master):
        # Create entry forms to update follow_tree view and follow database
        self.status_label = Label(master, text="Status: ")
        self.status_label.grid(row=0, column=0, padx=5, pady=10, sticky=NW)
        
        global status_entry
        status_entry = Entry(master)
        status_entry.grid(row=0, column=1, padx=5, pady=10, sticky=NW)

        self.follow_by_label = Label(master, text="Follow By:")
        self.follow_by_label.grid(row=1, column=0, padx=5, pady=10, sticky=NW)

        global follow_by_entry
        follow_by_entry = Entry(master)
        follow_by_entry.grid(row=1, column=1, padx=5, pady=10, sticky=NW)

        self.follow_info_label = Label(master, text="Follow Info: ")
        self.follow_info_label.grid(row=2, column=0, padx=5, pady=10, sticky=NW)
        
        global follow_info_text
        follow_info_text = Text(master, width=40, height=9, font=("Helvetica", 12), undo=True)
        follow_info_text.grid(row=2, column=1, padx=5, pady=10, sticky=NW, columnspan=2)






