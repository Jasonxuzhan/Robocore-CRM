from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import database_option
import treeview

# Instance of Database_option
robocore_database_option = database_option.Database_Options("localhost", "root", "jason121", "crmdatabase")


class Edit_Page:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("Customer Edit")

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

        global nation_entry 
        global province_entry 
        global city_entry 
        global company_entry 
        global contact_entry 
        global telephone_entry 
        global scenario_entry 
        global cooperation_entry 
        global request_entry 
        global lead_from_entry 
        global lead_channel_entry 
        global channel_detail_entry 
        global answer_by_entry 
        global customer_ID_label  

        nation_entry = Entry(self.edit_frame)
        province_entry = Entry(self.edit_frame)
        city_entry = Entry(self.edit_frame)
        company_entry = Entry(self.edit_frame)
        contact_entry = Entry(self.edit_frame)
        telephone_entry = Entry(self.edit_frame)
        scenario_entry = Entry(self.edit_frame)
        cooperation_entry = Entry(self.edit_frame)
        request_entry = Entry(self.edit_frame)
        lead_from_entry = Entry(self.edit_frame)
        lead_channel_entry = Entry(self.edit_frame)
        channel_detail_entry = Entry(self.edit_frame)
        answer_by_entry = Entry(self.edit_frame)
        customer_ID_label = Label(self.edit_frame, text="ID is generated auto")

        # Position of Labeles and Entries in edit frame
        # Row0
        self.nation_label.grid(row=0, column=0, padx=10, pady=20)
        nation_entry.grid(row=0, column=1)

        self.province_label.grid(row=0, column=2, padx=10, pady=20)
        province_entry.grid(row=0, column=3)

        self.city_label.grid(row=0, column=4, padx=10, pady=20)
        city_entry.grid(row=0, column=5, padx=10, pady=20)

        # Row1
        self.company_label.grid(row=1, column=0, padx=10, pady=20)
        company_entry.grid(row=1, column=1)

        self.contact_label.grid(row=1, column=2, padx=10, pady=20)
        contact_entry.grid(row=1, column=3)

        self.telephone_label.grid(row=1, column=4, padx=10, pady=20)
        telephone_entry.grid(row=1, column=5, padx=10, pady=20)

        # Row2
        self.scenario_label.grid(row=2, column=0, padx=10, pady=20)
        scenario_entry.grid(row=2, column=1)

        self.cooperation_label.grid(row=2, column=2, padx=10, pady=20)
        cooperation_entry.grid(row=2, column=3)

        self.request_label.grid(row=2, column=4, padx=10, pady=20)
        request_entry.grid(row=2, column=5, padx=10, pady=20)

        # Row3
        self.lead_from_label.grid(row=3, column=0, padx=10, pady=20)
        lead_from_entry.grid(row=3, column=1)

        self.lead_channel_label.grid(row=3, column=2, padx=10, pady=20)
        lead_channel_entry.grid(row=3, column=3)

        self.channel_detail_label.grid(row=3, column=4, padx=10, pady=20)
        channel_detail_entry.grid(row=3, column=5, padx=10, pady=20)

        # Row4
        self.answer_by_label.grid(row=4, column=0, padx=10, pady=20)
        answer_by_entry.grid(row=4, column=1)

        self.customer_ID.grid(row=4, column=2, padx=10, pady=20)
        customer_ID_label.grid(row=4, column=3, sticky=W)

        self.clean_entries = Button(self.edit_frame, text="Clean Entries", bootstyle="warning", cursor="hand2", command=self.clean_entries)
        self.clean_entries.grid(row=4, column=4, padx=10, pady=20)

        self.customer_create_button = Button(self.edit_frame, text="Create Customer", bootstyle="success", cursor="hand2", command=self.create_customer)
        self.customer_create_button.grid(row=4, column=5, padx=10, pady=20)

    # Clean entries for clean entries button
    def clean_entries(self) -> None:
        nation_entry.delete(0, END)
        province_entry.delete(0, END) 
        city_entry.delete(0, END) 
        company_entry.delete(0, END) 
        contact_entry.delete(0, END) 
        telephone_entry.delete(0, END) 
        scenario_entry.delete(0, END) 
        cooperation_entry.delete(0, END) 
        request_entry.delete(0, END) 
        lead_from_entry.delete(0, END) 
        lead_channel_entry.delete(0, END) 
        channel_detail_entry.delete(0, END) 
        answer_by_entry.delete(0, END)
    

    # Create customer and update into database and show on the leads treeview
    def create_customer(self) -> None:
        global nation 
        global province 
        global city 
        global company 
        global contact 
        global telephone
        global scenario 
        global cooperation 
        global request 
        global lead_from  
        global lead_channel 
        global channel_detail 
        global answer_by
        
        nation = nation_entry.get()
        province = province_entry.get() 
        city = city_entry.get() 
        company = company_entry.get() 
        contact = contact_entry.get() 
        telephone = telephone_entry.get() 
        scenario = scenario_entry.get() 
        cooperation = cooperation_entry.get() 
        request = request_entry.get() 
        lead_from = lead_from_entry.get() 
        lead_channel = lead_channel_entry.get() 
        channel_detail = channel_detail_entry.get() 
        answer_by = answer_by_entry.get()

        sqlstuff = f"""INSERT INTO leads_information (
                Register_Date,
                Nation,
                Province,
                City,  
                Company_Name,
                Contact_Name,
                Telephone,
                Scenario,
                Cooperation,
                Desc_of_Request,
                Lead_From, 
                Lead_Channel, 
                Channel_Details, 
                Answer_By
            ) VALUES(NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        new_customer = [nation, 
                        province, 
                        city, 
                        company, 
                        contact, 
                        telephone, 
                        scenario, 
                        cooperation,
                        request,
                        lead_from,
                        lead_channel,
                        channel_detail,
                        answer_by]
        
        robocore_database_option.my_cursor.execute(sqlstuff, new_customer)
        robocore_database_option.mydb.commit()

        nation_entry.delete(0, END)
        province_entry.delete(0, END) 
        city_entry.delete(0, END) 
        company_entry.delete(0, END) 
        contact_entry.delete(0, END) 
        telephone_entry.delete(0, END) 
        scenario_entry.delete(0, END) 
        cooperation_entry.delete(0, END) 
        request_entry.delete(0, END) 
        lead_from_entry.delete(0, END) 
        lead_channel_entry.delete(0, END) 
        channel_detail_entry.delete(0, END) 
        answer_by_entry.delete(0, END)

        treeview.Leads_Treeview.query_leads_information_table() # from leads_treeview.py, class method



        






