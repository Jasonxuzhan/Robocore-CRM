from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector


class Follow_Treeview:
    def __init__(self, master):
        # Create follow treeview scrollbar
        self.follow_treeview_scroll = Scrollbar(master)
        self.follow_treeview_scroll.pack(side=RIGHT, fill=Y)
        
        # Create follow treeview
        self.follow_treeview = Treeview(master, bootstyle="primary", yscrollcommand=self.follow_treeview_scroll.set, height=15)
        self.follow_treeview.pack(side=BOTTOM, padx=5, pady=5)

        #Config scroll bar
        self.follow_treeview_scroll.config(command=self.follow_treeview.yview)

        # Define follow treeview columns
        self.follow_treeview["columns"] = ("Customer ID",
                                "Follow Status",
                                "Follow Date",
                                "Follow Info",
                                "Follow_By")

        # Format follow treeview columns
        self.follow_treeview.column("#0", width=0, stretch=NO)
        self.follow_treeview.column("Customer ID", anchor=W, width=40)
        self.follow_treeview.column("Follow Status", anchor=W, width=120)
        self.follow_treeview.column("Follow Date", anchor=W, width=120)
        self.follow_treeview.column("Follow Info", anchor=W, width=240)
        self.follow_treeview.column("Follow_By", anchor=W, width=120)
    
        # Creat follow treeview headings
        self.follow_treeview.heading("#0", text="", anchor=W)
        self.follow_treeview.heading("Customer ID", text="ID", anchor=W)
        self.follow_treeview.heading("Follow Status", text="Status", anchor=W)
        self.follow_treeview.heading("Follow Date", text="Date", anchor=W)
        self.follow_treeview.heading("Follow Info", text="Follow Info", anchor=W)
        self.follow_treeview.heading("Follow_By", text="Follow_By", anchor=W)
