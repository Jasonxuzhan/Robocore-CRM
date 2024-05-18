from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector

class Leads_Treeview:
    def __init__(self, master):
        # Create leads teeview scroll bar 
        self.leads_treeview_scroll = Scrollbar(master)
        self.leads_treeview_scroll.pack(side=RIGHT, fill=Y)

        # Create treeview
        self.leads_treeview = Treeview(master, bootstyle="primary", yscrollcommand=self.leads_treeview_scroll.set, height=15, selectmode=BROWSE)
        self.leads_treeview.pack(side=BOTTOM, padx=5, pady=5)

        #Config scroll bar
        self.leads_treeview_scroll.config(command=self.leads_treeview.yview)

        # Define tree view columns
        self.leads_treeview["columns"] = ("ID",
                                        "Register Date",
                                        "Nation",
                                        "Province",
                                        "City",  
                                        "Company Name",
                                        "Contact Name",
                                        "Telephone",
                                        "Scenario",
                                        "Cooperation",
                                        "Desc of Request",
                                        "Lead From", 
                                        "Lead Channel", 
                                        "Channel Details", 
                                        "Answer By") 
        
        # Format columns
        self.leads_treeview.column("#0", width=0, stretch=NO)
        self.leads_treeview.column("ID", anchor=W, width=40)
        self.leads_treeview.column("Register Date", anchor=W, width=120)
        self.leads_treeview.column("Nation", anchor=W, width=100)
        self.leads_treeview.column("Province", anchor=W, width=100)
        self.leads_treeview.column("City", anchor=W, width=100)
        self.leads_treeview.column("Company Name", anchor=W, width=140)
        self.leads_treeview.column("Contact Name", anchor=W, width=100)
        self.leads_treeview.column("Telephone", anchor=W, width=140)
        self.leads_treeview.column("Scenario", anchor=W, width=100)
        self.leads_treeview.column("Cooperation", anchor=W, width=100)
        self.leads_treeview.column("Desc of Request", anchor=W, width=140)
        self.leads_treeview.column("Lead From", anchor=W, width=100)
        self.leads_treeview.column("Lead Channel", anchor=W, width=60)
        self.leads_treeview.column("Channel Details", anchor=W, width=60)
        self.leads_treeview.column("Answer By", anchor=W, width=60)
 
        # Creat headings
        self.leads_treeview.heading("#0", text="", anchor=W)
        self.leads_treeview.heading("ID", text="ID", anchor=W)
        self.leads_treeview.heading("Register Date", text="Reg Date", anchor=W)
        self.leads_treeview.heading("Nation", text="Nation", anchor=W)
        self.leads_treeview.heading("Province", text="Province", anchor=W)
        self.leads_treeview.heading("City", text="City", anchor=W)
        self.leads_treeview.heading("Company Name", text="Company", anchor=W)
        self.leads_treeview.heading("Contact Name", text="Contact", anchor=W)
        self.leads_treeview.heading("Telephone", text=" Telephone", anchor=W)
        self.leads_treeview.heading("Scenario", text="Scenario", anchor=W)
        self.leads_treeview.heading("Cooperation", text="Coop", anchor=W)
        self.leads_treeview.heading("Desc of Request", text="Desc of Request", anchor=W)
        self.leads_treeview.heading("Lead From", text="Lead From", anchor=W)
        self.leads_treeview.heading("Lead Channel", text="Lead Channel", anchor=W)
        self.leads_treeview.heading("Channel Details", text="Channel Detail", anchor=W)
        self.leads_treeview.heading("Answer By", text="Answer", anchor=W)  

        # Query Lead information database and show on the tree view
       
        # Clean the leads treeview
        for record in self.leads_treeview.get_children():
            self.leads_treeview.delete(record)
        





















        # Double click event
        self.leads_treeview.bind("<Double-1>", """select_record""")


if __name__ == "__main__":
    pass

