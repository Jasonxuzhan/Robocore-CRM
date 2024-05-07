from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector


class Edit_Page:
    def __init__(self):
        self.top = Toplevel()

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
        customer_ID_label = Label(self.edit_frame, text="ID is auto generated")

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




