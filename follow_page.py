from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector


class Follow_Page:
    def __init__(self, master):
        # Create entry forms to update follow_tree view and follow database
        self.status_label = Label(master, text="Status: ")
        self.status_label.grid(row=0, column=0, padx=5, pady=5, sticky=NW)

        self.status_entry = Entry(master)
        self.status_entry.grid(row=0, column=1, padx=5, pady=5, sticky=NW)




        
