from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import database_option
import follow_page
import notice

# Configure the style 
#style = Style()
#style.configure("object", font=())

# Instance of Database_option
robocore_database_option = database_option.Database_Options("localhost", "root", "jason121", "crmdatabase")

 # Event func for leadstreeview
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

def select_leads_record_oneclick_2(event):
    notice.notice_label_1.configure(text="")
    selected = leads_treeview.focus()
    values = leads_treeview.item(selected, "values")
    notice.notice_label_1.configure(text=f"{values[5]}, {values[6]}, {values[7]}")

def select_leads_event(event):
    select_leads_record_oneclick(event)
    select_leads_record_oneclick_2(event)

def select_leads_record_doubleclick(event):
    # Grab record number
    selected = leads_treeview.focus()
    
    # Grab record value
    values = leads_treeview.item(selected, "values")

    robocore_update_edit_page = Update_Page()

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

# Event func for follow treeview
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
        leads_treeview.bind("<ButtonRelease-1>", select_leads_event)
        
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


class Update_Page:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("Customer info")

        # Edit Frame in top
        self.edit_frame = Frame(self.top)
        self.edit_frame.pack()

        # Elements in edit_frame
        self.nation_label = Label(self.edit_frame, text="Nation: ")
        self.province_label = Label(self.edit_frame, text="Province: ") 
        self.city_label = Label(self.edit_frame, text="City: ")
        self.company_label = Label(self.edit_frame, text="Company: ")
        self.contact_label = Label(self.edit_frame, text="Contact: ")
        self.telephone_label = Label(self.edit_frame, text="Telephone: ")
        self.scenario_label = Label(self.edit_frame, text="Scenario: ")
        self.cooperation_label = Label(self.edit_frame, text="Cooperation: ")
        self.request_label = Label(self.edit_frame, text="Request: ")
        self.lead_from_label = Label(self.edit_frame, text="Lead_From: ")
        self.lead_channel_label = Label(self.edit_frame, text="Lead_Channel: ")
        self.channel_detail_label = Label(self.edit_frame, text="Channel_Detail: ")
        self.answer_by_label = Label(self.edit_frame, text="Answer_By: ")
        self.customer_ID = Label(self.edit_frame, text="Customer ID: ")

        self.nation_entry = Entry(self.edit_frame)
        self.province_entry = Entry(self.edit_frame)
        self.city_entry = Entry(self.edit_frame)
        self.company_entry = Entry(self.edit_frame)
        self.contact_entry = Entry(self.edit_frame)
        self.telephone_entry = Entry(self.edit_frame)
        self.scenario_entry = Entry(self.edit_frame)
        self.cooperation_entry = Entry(self.edit_frame)
        self.request_entry = Entry(self.edit_frame)
        self.lead_from_entry = Entry(self.edit_frame)
        self.lead_channel_entry = Entry(self.edit_frame)
        self.channel_detail_entry = Entry(self.edit_frame)
        self.answer_by_entry = Entry(self.edit_frame)
        self.customer_ID_label = Label(self.edit_frame, text="ID is generated auto")

        # Position of Labeles and Entries in edit frame
        # Row0
        self.nation_label.grid(row=0, column=0, padx=10, pady=20)
        self.nation_entry.grid(row=0, column=1)

        self.province_label.grid(row=0, column=2, padx=10, pady=20)
        self.province_entry.grid(row=0, column=3)

        self.city_label.grid(row=0, column=4, padx=10, pady=20)
        self.city_entry.grid(row=0, column=5, padx=10, pady=20)

        # Row1
        self.company_label.grid(row=1, column=0, padx=10, pady=20)
        self.company_entry.grid(row=1, column=1)

        self.contact_label.grid(row=1, column=2, padx=10, pady=20)
        self.contact_entry.grid(row=1, column=3)

        self.telephone_label.grid(row=1, column=4, padx=10, pady=20)
        self.telephone_entry.grid(row=1, column=5, padx=10, pady=20)

        # Row2
        self.scenario_label.grid(row=2, column=0, padx=10, pady=20)
        self.scenario_entry.grid(row=2, column=1)

        self.cooperation_label.grid(row=2, column=2, padx=10, pady=20)
        self.cooperation_entry.grid(row=2, column=3)

        self.request_label.grid(row=2, column=4, padx=10, pady=20)
        self.request_entry.grid(row=2, column=5, padx=10, pady=20)

        # Row3
        self.lead_from_label.grid(row=3, column=0, padx=10, pady=20)
        self.lead_from_entry.grid(row=3, column=1)

        self.lead_channel_label.grid(row=3, column=2, padx=10, pady=20)
        self.lead_channel_entry.grid(row=3, column=3)

        self.channel_detail_label.grid(row=3, column=4, padx=10, pady=20)
        self.channel_detail_entry.grid(row=3, column=5, padx=10, pady=20)

        # Row4
        self.answer_by_label.grid(row=4, column=0, padx=10, pady=20)
        self.answer_by_entry.grid(row=4, column=1)

        self.customer_ID.grid(row=4, column=2, padx=10, pady=20)
        self.customer_ID_label.grid(row=4, column=3, sticky=W)

        self.update_entries = Button(self.edit_frame, text="Update", bootstyle="success", cursor="hand2", command=self.update_record)
        self.update_entries.grid(row=4, column=4, padx=10, pady=20)

        self.customer_create_button = Button(self.edit_frame, text="Quit", bootstyle="success", cursor="hand2", command=self.top.destroy)
        self.customer_create_button.grid(row=4, column=5, padx=10, pady=20)

    def update_record(self):

        nation = self.nation_entry.get()    
        province = self.province_entry.get()   
        city = self.city_entry.get()    
        company = self.company_entry.get()    
        contact = self.contact_entry.get()    
        telephone = self.telephone_entry.get()   
        scenario = self.scenario_entry.get()    
        cooperation = self.cooperation_entry.get()    
        request = self.request_entry.get()   
        lead_from = self.lead_from_entry.get()   
        lead_channel = self.lead_channel_entry.get()    
        channel_detail = self.channel_detail_entry.get()    
        answer_by = self.answer_by_entry.get()    
        customer_id = self.customer_ID_label.cget("text")

        sqlstuff = f"""UPDATE leads_information SET
                Nation = '{nation}',
                Province = '{province}',
                City = '{city}',  
                Company_Name = '{company}',
                Contact_Name = '{contact}',
                Telephone = '{telephone}',
                Scenario = '{scenario}',
                Cooperation = '{cooperation}',
                Desc_of_Request = '{request}',
                Lead_From = '{lead_from}', 
                Lead_Channel = '{lead_channel}', 
                Channel_Details = '{channel_detail}', 
                Answer_By = '{answer_by}' WHERE ID = {customer_id}"""

        robocore_database_option.my_cursor.execute(sqlstuff)
        robocore_database_option.mydb.commit()

        self.nation_entry.delete(0, END)   
        self.province_entry.delete(0, END)   
        self.city_entry.delete(0, END)    
        self.company_entry.delete(0, END)    
        self.contact_entry.delete(0, END)    
        self.telephone_entry.delete(0, END)   
        self.scenario_entry.delete(0, END)    
        self.cooperation_entry.delete(0, END)    
        self.request_entry.delete(0, END)   
        self.lead_from_entry.delete(0, END)   
        self.lead_channel_entry.delete(0, END)    
        self.channel_detail_entry.delete(0, END)    
        self.answer_by_entry.delete(0, END)    

        Leads_Treeview.query_leads_information_table()
        

class Follow_Info_Input_Page:
    def __init__(self): 
        self.top = Toplevel()
        self.top.title("Follow Input")

        self.follow_info_input_frame = Frame(self.top)
        self.follow_info_input_frame.pack(padx=5, pady=5)

        self.status_label = Label(self.follow_info_input_frame, text="Status: ")
        self.status_label.grid(row=0, column=0, padx=10, pady=20, sticky=NW)

        self.status_options = ["On Follow", "On Follow", "Give Up", "Transfer to Distributor"]
        self.status_clicked = StringVar()
        self.status_clicked.set(self.status_options[0])
        self.status_entry = OptionMenu(self.follow_info_input_frame, self.status_clicked, *self.status_options)
        self.status_entry.grid(row=0, column=1, padx=10, pady=20, sticky=NW)

        self.follow_by_label = Label(self.follow_info_input_frame, text="Follow By:")
        self.follow_by_label.grid(row=1, column=0, padx=10, pady=20, sticky=NW)

        self.name_options = ["Tony", "Tony", "Jason"]
        self.name_clicked = StringVar()
        self.name_clicked.set(self.name_options[0])
        self.follow_by_entry = OptionMenu(self.follow_info_input_frame, self.name_clicked, *self.name_options)
        self.follow_by_entry.grid(row=1, column=1, padx=10, pady=20, sticky=NW)

        self.follow_info_label = Label(self.follow_info_input_frame, text="Follow Info: ")
        self.follow_info_label.grid(row=2, column=0, padx=10, pady=20, sticky=NW)

        self.follow_info_text = Text(self.follow_info_input_frame, width=40, height=9, font=("Helvetica", 12), undo=True)
        self.follow_info_text.grid(row=2, column=1, padx=10, pady=20, sticky=NW, columnspan=2)

        self.follow_create_button = Button(self.follow_info_input_frame, text="Create Follow", bootstyle="success", cursor="hand2", command=self.create_follow_info)
        self.follow_create_button.grid(row=0, column=2, padx=10, pady=20, sticky=NE)
    
    def create_follow_info(self):
        try:
            selected = leads_treeview.focus()
            values = leads_treeview.item(selected, "values")

            customer_id = values[0]
            status = self.status_clicked.get()
            follow_by = self.name_clicked.get()
            follow_info = self.follow_info_text.get(1.0, END)

            sqlstuff = f"""INSERT INTO customer_follow (
                    ID,
                    Status,
                    Date,  
                    Follow_Info,
                    Follow_By
                ) VALUES(%s, %s, NOW(), %s, %s)"""
            
            new_follow = [customer_id,
                          status,
                          follow_info,
                          follow_by]
            
            robocore_database_option.my_cursor.execute(sqlstuff, new_follow)
            robocore_database_option.mydb.commit()
            
            Follow_Treeview.query_customer_follow_table()
        
        except:
             messagebox.showerror("Error", "One customer should be selected in treeview!")










if __name__ == "__main__":
    pass

