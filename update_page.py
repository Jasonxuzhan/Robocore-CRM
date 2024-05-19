from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox

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

        #self.clean_entries = Button(self.edit_frame, text="Delete", bootstyle="warning", cursor="hand2", command=self.delete_record)
        #self.clean_entries.grid(row=4, column=4, padx=10, pady=20)

        self.customer_create_button = Button(self.edit_frame, text="Quit", bootstyle="success", cursor="hand2", command=self.top.destroy)
        self.customer_create_button.grid(row=4, column=5, padx=10, pady=20)

    
    
    
   
        

        


        






