from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import database_option
import update_page
import follow_page

# Instance of Database_option
robocore_database_option = database_option.Database_Options("localhost", "root", "jason121", "crmdatabase")

 # Event func for double-click in leads treeview
def select_leads_record_oneclick(event):
    selected = leads_treeview.focus()
    values = leads_treeview.item(selected, "values")

    # Clean the follow treeview
    for record in follow_treeview.get_children():
        follow_treeview.delete(record)

    # Option in Database 
    sql_stuff = f"""SELECT * FROM customer_follow WHERE ID = {values[0]}"""
    robocore_database_option.my_cursor.execute(sql_stuff)

    records = robocore_database_option.my_cursor.fetchall()

    for record in records:
        follow_treeview.insert(
                                parent="",
                                index="end",
                                text="",
                                values=(record[0], record[1], record[2], record[3], record[4]))

    robocore_database_option.mydb.commit()

    
def select_leads_record_doubleclick(event):
    # Grab record number
    selected = leads_treeview.focus()
    
    # Grab record value
    values = leads_treeview.item(selected, "values")

    robocore_update_edit_page = update_page.Update_Page()

    # Insert value into edit page entries
    robocore_update_edit_page.nation_entry.insert(0, values[2])
    robocore_update_edit_page.province_entry.insert(0, values[3])
    robocore_update_edit_page.city_entry.insert(0, values[4])
    robocore_update_edit_page.company_entry.insert(0, values[5]) 
    robocore_update_edit_page.contact_entry.insert(0, values[6]) 
    robocore_update_edit_page.telephone_entry.insert(0, values[7]) 
    robocore_update_edit_page.scenario_entry.insert(0, values[8]) 
    robocore_update_edit_page.cooperation_entry.insert(0, values[9]) 
    robocore_update_edit_page.request_entry.insert(0, values[10]) 
    robocore_update_edit_page.lead_from_entry.insert(0, values[11]) 
    robocore_update_edit_page.lead_channel_entry.insert(0, values[12])
    robocore_update_edit_page.channel_detail_entry.insert(0, values[13])
    robocore_update_edit_page.answer_by_entry.insert(0, values[14]) 
    robocore_update_edit_page.customer_ID_label.configure(text=values[0])

def select_follow_record(event):
    # Clean the entries
    follow_page.status_entry.delete(0, END)
    follow_page.follow_by_entry.delete(0, END)
    follow_page.follow_info_text.delete(1.0, END)

    # Grab record number
    selected = follow_treeview.focus()

    # Grab record value
    values = follow_treeview.item(selected, "values")

    # Insert value into entries and text
    follow_page.status_entry.insert(0, values[1])
    follow_page.follow_by_entry.insert(0, values[4])
    follow_page.follow_info_text.insert(END, values[3])

class Leads_Treeview:
    def __init__(self, master):
        # Create leads teeview scroll bar 
        self.leads_treeview_scroll = Scrollbar(master)
        self.leads_treeview_scroll.pack(side=RIGHT, fill=Y)
        
        # Create treeview
        global leads_treeview
        leads_treeview = Treeview(master, bootstyle="primary", yscrollcommand=self.leads_treeview_scroll.set, height=15, selectmode=BROWSE)
        
        # Double click event
        leads_treeview.bind("<Double-1>", select_leads_record_doubleclick)
        leads_treeview.bind("<ButtonRelease-1>", select_leads_record_oneclick)
        
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
     # In database, Query Lead information table and show on the tree view
    def query_leads_information_table(cls):
        # Clean the leads treeview
        for record in leads_treeview.get_children(): # get_children means get iid 
            leads_treeview.delete(record)
        
        # Option in Database 
        sql_stuff = "SELECT * FROM leads_information ORDER BY ID DESC"
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


   
class Follow_Treeview:
    def __init__(self, master):
        # Create follow treeview scrollbar
        self.follow_treeview_scroll = Scrollbar(master)
        self.follow_treeview_scroll.pack(side=RIGHT, fill=Y)
        
        # Create follow treeview
        global follow_treeview
        follow_treeview = Treeview(master, bootstyle="primary", yscrollcommand=self.follow_treeview_scroll.set, height=15)
        
        #Click release event
        follow_treeview.bind("<ButtonRelease-1>", select_follow_record)

        follow_treeview.pack(side=BOTTOM, padx=5, pady=5)

        #Config scroll bar
        self.follow_treeview_scroll.config(command=follow_treeview.yview)

        # Define follow treeview columns
        follow_treeview["columns"] = ("Customer ID",
                                "Follow Status",
                                "Follow Date",
                                "Follow Info",
                                "Follow_By")

        # Format follow treeview columns
        follow_treeview.column("#0", width=0, stretch=NO)
        follow_treeview.column("Customer ID", anchor=W, width=40)
        follow_treeview.column("Follow Status", anchor=W, width=120)
        follow_treeview.column("Follow Date", anchor=W, width=120)
        follow_treeview.column("Follow Info", anchor=W, width=240)
        follow_treeview.column("Follow_By", anchor=W, width=120)
    
        # Creat follow treeview headings
        follow_treeview.heading("#0", text="", anchor=W)
        follow_treeview.heading("Customer ID", text="ID", anchor=W)
        follow_treeview.heading("Follow Status", text="Status", anchor=W)
        follow_treeview.heading("Follow Date", text="Date", anchor=W)
        follow_treeview.heading("Follow Info", text="Follow Info", anchor=W)
        follow_treeview.heading("Follow_By", text="Follow_By", anchor=W)    


    @classmethod
    def query_customer_follow_table(cls):
        # Clean the follow treeview
        for record in follow_treeview.get_children():
            follow_treeview.delete(record)
        
        # Option in Database 
        sql_stuff = "SELECT * FROM customer_follow"
        robocore_database_option.my_cursor.execute(sql_stuff)

        records = robocore_database_option.my_cursor.fetchall()

        for record in records:
            follow_treeview.insert(
                                    parent="",
                                    index="end",
                                    text="",
                                    values=(record[0], record[1], record[2], record[3], record[4]))
        
        robocore_database_option.mydb.commit()

        




















if __name__ == "__main__":
    pass

