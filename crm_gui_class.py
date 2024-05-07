from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector


# Main Root
root = Window(themename="superhero")
root.title("Robocore CRM System V1.0")
root.iconbitmap()
root. geometry("1700x800")

def show_create_success_message():
    messagebox.showinfo("Add Success", f"{company_entry} had been added")


def show_edit_error_message():
    messagebox.showerror("Error", "The customer should be selected, pls select customer or double click in tree view")


# Create edit window 
def create_edit_window(title=""):
        
        global top_edit
        top_edit = Toplevel()
        top_edit.title = title

        # Title Label 
        title_label = Label(top_edit, text=title, font="Times 20 bold")
        title_label.pack(padx=10, pady=10, anchor=W)

        # Lead Frame
        lead_frame = Frame(top_edit, relief=FLAT)
        lead_frame.pack(padx=10, pady=10)

        # Sperator
        sep = Separator(top_edit, orient="horizontal",bootstyle="info")
        sep.pack(fill=X, padx=5)

        # Option frame
        option_frame = Frame(top_edit, relief=FLAT)
        option_frame.pack(padx=10, pady=10)

        # Labeles in lead frame
        nation_label = Label(lead_frame, text="Nation: ")
        province_label = Label(lead_frame, text="Province: ") 
        city_label = Label(lead_frame, text="City: ")
        company_label = Label(lead_frame, text="Company: ")
        contact_label = Label(lead_frame, text="Contact: ")
        telephone_label = Label(lead_frame, text="Telephone: ")
        scenario_label = Label(lead_frame, text="Scenario: ")
        cooperation_label = Label(lead_frame, text="Cooperation: ")
        request_label = Label(lead_frame, text="Request: ")
        lead_from_label = Label(lead_frame, text="Lead_From: ")
        lead_channel_label = Label(lead_frame, text="Lead_Channel: ")
        channel_detail_label = Label(lead_frame, text="Channel_Detail: ")
        answer_by_label = Label(lead_frame, text="Answer_By: ")
        customer_ID = Label(lead_frame, text="Customer ID: ")

        # Entries in lead frame
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

        nation_entry = Entry(lead_frame)
        province_entry = Entry(lead_frame)
        city_entry = Entry(lead_frame)
        company_entry = Entry(lead_frame)
        contact_entry = Entry(lead_frame)
        telephone_entry = Entry(lead_frame)
        scenario_entry = Entry(lead_frame)
        cooperation_entry = Entry(lead_frame)
        request_entry = Entry(lead_frame)
        lead_from_entry = Entry(lead_frame)
        lead_channel_entry = Entry(lead_frame)
        channel_detail_entry = Entry(lead_frame)
        answer_by_entry = Entry(lead_frame)
        customer_ID_label = Label(lead_frame, text="")

        # Position of Labeles and Entries in lead frame
        # Row0
        nation_label.grid(row=0, column=0, padx=10, pady=20)
        nation_entry.grid(row=0, column=1)

        province_label.grid(row=0, column=2, padx=10, pady=20)
        province_entry.grid(row=0, column=3)

        city_label.grid(row=0, column=4, padx=10, pady=20)
        city_entry.grid(row=0, column=5)

        # Row1
        company_label.grid(row=1, column=0, padx=10, pady=20)
        company_entry.grid(row=1, column=1)

        contact_label.grid(row=1, column=2, padx=10, pady=20)
        contact_entry.grid(row=1, column=3)

        telephone_label.grid(row=1, column=4, padx=10, pady=20)
        telephone_entry.grid(row=1, column=5)

        # Row2
        scenario_label.grid(row=2, column=0, padx=10, pady=20)
        scenario_entry.grid(row=2, column=1)

        cooperation_label.grid(row=2, column=2, padx=10, pady=20)
        cooperation_entry.grid(row=2, column=3)

        request_label.grid(row=2, column=4, padx=10, pady=20)
        request_entry.grid(row=2, column=5)

        # Row3
        lead_from_label.grid(row=3, column=0, padx=10, pady=20)
        lead_from_entry.grid(row=3, column=1)

        lead_channel_label.grid(row=3, column=2, padx=10, pady=20)
        lead_channel_entry.grid(row=3, column=3)

        channel_detail_label.grid(row=3, column=4, padx=10, pady=20)
        channel_detail_entry.grid(row=3, column=5)

        # Row4
        answer_by_label.grid(row=4, column=0, padx=10, pady=20)
        answer_by_entry.grid(row=4, column=1)

        customer_ID.grid(row=4, column=2, padx=10, pady=20)
        customer_ID_label.grid(row=4, column=3, sticky=W)

        # Option Buttons in Option frame
        save_button = Button(option_frame, text="Save", bootstyle="success", cursor="hand2", command=add_customer)
        save_button.grid(row=0, column=0, padx=20, pady=20)

        clear_button = Button(option_frame, text="Clear", bootstyle="info", cursor="hand2", command=clear_entries)
        clear_button.grid(row=0, column=1, padx=20, pady=20)

        quit_button = Button(option_frame, text="Quit", bootstyle="warning", cursor="hand2", command=top_edit.destroy)
        quit_button.grid(row=0, column=2, padx=20, pady=20)


# Clean entries
def clear_entries(): 
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
    customer_ID_label.configure(text="")


# Query crmdatabase, leads information table and show on the tree view in main page
def query_database():
    """
        first: clear the treeview
        second: connect database table and fetch all data
        third: show on the treeview

    """
    clear_entries()

    for record in tree_view.get_children():
        tree_view.delete(record)

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = "crmdatabase"
        )

    my_cursor = mydb.cursor()

    sql_stuff = "SELECT * FROM leads_information"

    my_cursor.execute(sql_stuff)

    records = my_cursor.fetchall()

    for record in records:
        tree_view.insert(parent="",
                         index="end",
                         text="",
                         values=(record[0], record[1], record[2], record[3], record[4],record[5], record[6],record[7],
                                 record[8], record[9], record[10], record[11], record[12], record[13], record[14]))

    mydb.commit()
    mydb.close()


# Event
def select_record(event):
    # Double click and launch the edit customer window 
    # Grab record number
    selected = tree_view.focus()
    
    # Grab record value 
    values = tree_view.item(selected, "values")
    
    # Create edit window
    create_edit_window(title="Edit Customer")

    # clear entry boxes
    clear_entries()
    
    # Outpus to entry boxes
    nation_entry.insert(0, values[2])
    province_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    company_entry.insert(0, values[5]) 
    contact_entry.insert(0, values[6]) 
    telephone_entry.insert(0, values[7]) 
    scenario_entry.insert(0, values[8]) 
    cooperation_entry.insert(0, values[9]) 
    request_entry.insert(0, values[10]) 
    lead_from_entry.insert(0, values[11]) 
    lead_channel_entry.insert(0, values[12])
    channel_detail_entry.insert(0, values[13])
    answer_by_entry.insert(0, values[14]) 
    customer_ID_label.configure(text=values[0])


# Select record and open edit customer window 
def select_record_edit():
    try:
        # Grab record number
        selected = tree_view.focus()
        
        # Grab record value 
        values = tree_view.item(selected, "values")
        
        # Oepn edit window 
        create_edit_window(title="Edit Customer")

        # clear entry boxes
        clear_entries()
        
        # Output to entry boxes
        nation_entry.insert(0, values[2])
        province_entry.insert(0, values[3])
        city_entry.insert(0, values[4])
        company_entry.insert(0, values[5]) 
        contact_entry.insert(0, values[6]) 
        telephone_entry.insert(0, values[7]) 
        scenario_entry.insert(0, values[8]) 
        cooperation_entry.insert(0, values[9]) 
        request_entry.insert(0, values[10]) 
        lead_from_entry.insert(0, values[11]) 
        lead_channel_entry.insert(0, values[12])
        channel_detail_entry.insert(0, values[13])
        answer_by_entry.insert(0, values[14]) 
        customer_ID_label.configure(text=values[0])

    except:
        top_edit.destroy()
        show_edit_error_message()

# Update customer to database and show on the tree view  
def update_customer_info():
    """update customer info"""
    select_record = tree_view.focus()
    tree_view.item(select_record, text="", values=(nation_entry.get(),
                                                            province_entry.get(),
                                                            city_entry.get(),
                                                            company_entry.get(), 
                                                            contact_entry.get(),
                                                            telephone_entry.get(),
                                                            scenario_entry.get(), 
                                                            cooperation_entry.get(),
                                                            request_entry.get(),
                                                            lead_from_entry.get(),
                                                            lead_channel_entry.get(),
                                                            channel_detail_entry.get(),
                                                            answer_by_entry.get()))



# Add new customer to database and show on the tree view 
def add_customer():
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
    channel = lead_channel_entry.get()
    channel_detail = channel_detail_entry.get()
    answer_by = answer_by_entry.get() 

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = "crmdatabase"
    )

    my_cursor = mydb.cursor()

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
                    channel,
                    channel_detail,
                    answer_by]

    my_cursor.execute(sqlstuff, new_customer)  
    
    mydb.commit()
    mydb.close()
    
    clear_entries()
    
    # Query database in Mainwidnow
    query_database()


# Create follow window
def create_follow_window(title=""):
        top_follow = Toplevel()
        top_follow.title = title

        # Title Label 
        title_label = Label(top_follow, text=title, font="Times 20 bold")
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # Follow Frame
        follow_frame = Labelframe(top_follow, text="Follow Status")
        follow_frame.grid(row=1, column=0, padx=10, pady=10, sticky=SW)

        # Notice Label
        notice_label = Label(follow_frame, text="this is a test notice\nPls update: ", font="Times 10")
        notice_label.pack(padx=10, pady=10, anchor=W)

        # Text
        follow_text = Text(follow_frame, height=5, width=30)
        follow_text.pack(padx=10, pady=10) 

        # Buttons 
        add_button = Button(follow_frame, text="Add", bootstyle="success", cursor="hand2")
        add_button.pack(side=LEFT, padx=10, pady=10)

        # Drop down button 
        options = ["Follow", "Follow", "Give UP", "To Distributor"]
        clicked = StringVar()
        clicked.set(options[0])
        drop = OptionMenu(follow_frame, clicked, *options)
        drop.pack(side=LEFT, padx=10, pady=10)

        quit_button = Button(follow_frame, text="Quit", bootstyle="warning", cursor="hand2", command=top_follow.destroy)
        quit_button.pack(side=LEFT, padx=10, pady=10)


        # Single customer follow tree view 
        # Tree View
        # Create tee view frame
        follow_tree_view_frame = Frame(top_follow)
        follow_tree_view_frame.grid(row=1, column=1, padx=10, pady=10, sticky=N)

        # Create tee view scroll bar 
        follow_tree_view_scroll = Scrollbar(follow_tree_view_frame)
        follow_tree_view_scroll.pack(side=RIGHT, fill=Y)

        # Create tree view 
        global follow_tree_view
        follow_tree_view = Treeview(follow_tree_view_frame, bootstyle="primary", yscrollcommand=follow_tree_view_scroll.set, height=12)
        follow_tree_view.pack()

        #Config scroll bar
        follow_tree_view_scroll.config(command=follow_tree_view.yview)

        # Define tree view columns
        follow_tree_view["columns"] = ("Customer ID",
                                "Follow Status",
                                "Follow Date",
                                "Follow Info",
                                "Follow_By")

        # Format columns
        follow_tree_view.column("#0", width=0, stretch=NO)
        follow_tree_view.column("Customer ID", anchor=CENTER, width=40)
        follow_tree_view.column("Follow Status", anchor=CENTER, width=120)
        follow_tree_view.column("Follow Date", anchor=CENTER, width=120)
        follow_tree_view.column("Follow Info", anchor=CENTER, width=240)
        follow_tree_view.column("Follow_By", anchor=CENTER, width=120)
       

        # Creat headings
        follow_tree_view.heading("#0", text="", anchor=W)
        follow_tree_view.heading("Customer ID", text="ID", anchor=CENTER)
        follow_tree_view.heading("Follow Status", text="Status", anchor=CENTER)
        follow_tree_view.heading("Follow Date", text="Date", anchor=CENTER)
        follow_tree_view.heading("Follow Info", text="Follow Info", anchor=CENTER)
        follow_tree_view.heading("Follow_By", text="Follow_By", anchor=CENTER)


#Query follow crmdatabase and show on the tree view 
def query_follow_database():
    """
    first: clear the treeview
    second: connect database table and fetch all data
    third: show on the treeview

    """
    for record in follow_tree_view.get_children():
        follow_tree_view.delete(record)

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = "crmdatabase"
        )

    my_cursor = mydb.cursor()

    sql_stuff = "SELECT * FROM customer_follow"

    my_cursor.execute(sql_stuff)

    records = my_cursor.fetchall()

    for record in records:
        follow_tree_view.insert(parent="",
                            index="end",
                            text="",
                            values=(record[0], record[1], record[2], record[3], record[4]))

    mydb.commit()
    mydb.close()



# Create Main Window         
# Frame and Label 
title_label = Label(root, text="Robocore CRM System", font="Times 20 bold")
title_label.grid(row=0, column=0, padx=10, pady=20, sticky=NW, columnspan=2)

customer_option_frame = Labelframe(root, text="Customer Options", relief=FLAT)
customer_option_frame.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

# Buttons
create_customer_button = Button(customer_option_frame, text="Create Customer", bootstyle="success-link", cursor="hand2", command=add_customer) 
create_customer_button.grid(row=0, column=0, padx=10, pady=10, sticky=W) 

edit_customer_button = Button(customer_option_frame, text="Edit Customer", bootstyle="success-link", cursor="hand2", command=select_record_edit) 
edit_customer_button.grid(row=1, column=0, padx=10, pady=10, sticky=W) 

follow_customer_button = Button(customer_option_frame, text="Follow Customer", bootstyle="success-link", cursor="hand2")
follow_customer_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)    

# Tree View
# Create tee view frame
tree_view_frame = Frame(root)
tree_view_frame.grid(row=1, column=1, padx=15, pady=10, sticky=N)

# Create tee view scroll bar 
tree_view_scroll = Scrollbar(tree_view_frame)
tree_view_scroll.pack(side=RIGHT, fill=Y)

# Create tree view 
tree_view = Treeview(tree_view_frame, bootstyle="primary", yscrollcommand=tree_view_scroll.set, height=20, selectmode="extended")
tree_view.pack()

# Double click event
tree_view.bind("<Double-1>", select_record)

#Config scroll bar
tree_view_scroll.config(command=tree_view.yview)

# Define tree view columns
tree_view["columns"] = ("ID",
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
tree_view.column("#0", width=0, stretch=NO)
tree_view.column("ID", anchor=CENTER, width=40)
tree_view.column("Register Date", anchor=CENTER, width=120)
tree_view.column("Nation", anchor=CENTER, width=100)
tree_view.column("Province", anchor=CENTER, width=100)
tree_view.column("City", anchor=CENTER, width=100)
tree_view.column("Company Name", anchor=CENTER, width=140)
tree_view.column("Contact Name", anchor=CENTER, width=100)
tree_view.column("Telephone", anchor=CENTER, width=140)
tree_view.column("Scenario", anchor=CENTER, width=100)
tree_view.column("Cooperation", anchor=CENTER, width=100)
tree_view.column("Desc of Request", anchor=CENTER, width=140)
tree_view.column("Lead From", anchor=CENTER, width=100)
tree_view.column("Lead Channel", anchor=CENTER, width=60)
tree_view.column("Channel Details", anchor=CENTER, width=60)
tree_view.column("Answer By", anchor=CENTER, width=60)

# Creat headings
tree_view.heading("#0", text="", anchor=W)
tree_view.heading("ID", text="ID", anchor=CENTER)
tree_view.heading("Register Date", text="Reg Date", anchor=CENTER)
tree_view.heading("Nation", text="Nation", anchor=CENTER)
tree_view.heading("Province", text="Province", anchor=CENTER)
tree_view.heading("City", text="City", anchor=CENTER)
tree_view.heading("Company Name", text="Company", anchor=CENTER)
tree_view.heading("Contact Name", text="Contact", anchor=CENTER)
tree_view.heading("Telephone", text=" Telephone", anchor=CENTER)
tree_view.heading("Scenario", text="Scenario", anchor=CENTER)
tree_view.heading("Cooperation", text="Coop", anchor=CENTER)
tree_view.heading("Desc of Request", text="Desc of Request", anchor=CENTER)
tree_view.heading("Lead From", text="Lead From", anchor=CENTER)
tree_view.heading("Lead Channel", text="Lead Channel", anchor=CENTER)
tree_view.heading("Channel Details", text="Channel Detail", anchor=CENTER)
tree_view.heading("Answer By", text="Answer", anchor=CENTER)       






if __name__ == "__main__":
    query_database()
    root.mainloop()



