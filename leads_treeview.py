from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import database_option

# Instance of Database_option
robocore_database_option = database_option.Database_Options("localhost", "root", "jason121", "crmdatabase")

class Leads_Treeview:
    def __init__(self, master):
        # Create leads teeview scroll bar 
        self.leads_treeview_scroll = Scrollbar(master)
        self.leads_treeview_scroll.pack(side=RIGHT, fill=Y)

        # Create treeview
        global leads_treeview
        leads_treeview = Treeview(master, bootstyle="primary", yscrollcommand=self.leads_treeview_scroll.set, height=15, selectmode=BROWSE)
        leads_treeview.pack(side=BOTTOM, padx=5, pady=5)

        #Config scroll bar
        self.leads_treeview_scroll.config(command=leads_treeview.yview)

        # Define tree view columns
        leads_treeview["columns"] = ("ID",
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
        leads_treeview.column("#0", width=0, stretch=NO)
        leads_treeview.column("ID", anchor=W, width=40)
        leads_treeview.column("Register Date", anchor=W, width=120)
        leads_treeview.column("Nation", anchor=W, width=100)
        leads_treeview.column("Province", anchor=W, width=100)
        leads_treeview.column("City", anchor=W, width=100)
        leads_treeview.column("Company Name", anchor=W, width=140)
        leads_treeview.column("Contact Name", anchor=W, width=100)
        leads_treeview.column("Telephone", anchor=W, width=140)
        leads_treeview.column("Scenario", anchor=W, width=100)
        leads_treeview.column("Cooperation", anchor=W, width=100)
        leads_treeview.column("Desc of Request", anchor=W, width=140)
        leads_treeview.column("Lead From", anchor=W, width=100)
        leads_treeview.column("Lead Channel", anchor=W, width=60)
        leads_treeview.column("Channel Details", anchor=W, width=60)
        leads_treeview.column("Answer By", anchor=W, width=60)
 
        # Creat headings
        leads_treeview.heading("#0", text="", anchor=W)
        leads_treeview.heading("ID", text="ID", anchor=W)
        leads_treeview.heading("Register Date", text="Reg Date", anchor=W)
        leads_treeview.heading("Nation", text="Nation", anchor=W)
        leads_treeview.heading("Province", text="Province", anchor=W)
        leads_treeview.heading("City", text="City", anchor=W)
        leads_treeview.heading("Company Name", text="Company", anchor=W)
        leads_treeview.heading("Contact Name", text="Contact", anchor=W)
        leads_treeview.heading("Telephone", text=" Telephone", anchor=W)
        leads_treeview.heading("Scenario", text="Scenario", anchor=W)
        leads_treeview.heading("Cooperation", text="Coop", anchor=W)
        leads_treeview.heading("Desc of Request", text="Desc of Request", anchor=W)
        leads_treeview.heading("Lead From", text="Lead From", anchor=W)
        leads_treeview.heading("Lead Channel", text="Lead Channel", anchor=W)
        leads_treeview.heading("Channel Details", text="Channel Detail", anchor=W)
        leads_treeview.heading("Answer By", text="Answer", anchor=W)  

    @classmethod
     # Query Lead information table and show on the tree view
    def query_leads_information_table(cls):
        # Clean the leads treeview
        for record in leads_treeview.get_children(): # get_children means get iid 
            leads_treeview.delete(record)
        
        # Option in Database 
        sql_stuff = "SELECT * FROM leads_information"
        robocore_database_option.my_cursor.execute(sql_stuff)

        records = robocore_database_option.my_cursor.fetchall()

        for record in records:
            leads_treeview.insert(
                         parent="",
                         index="end",
                         text="",
                         values=(record[0], record[1], record[2], record[3], record[4],record[5], record[6],record[7],
                                 record[8], record[9], record[10], record[11], record[12], record[13], record[14]))
        
        robocore_database_option.mydb.commit()
    


        






















        # Double click event
        leads_treeview.bind("<Double-1>", """select_record""")


if __name__ == "__main__":
    pass

