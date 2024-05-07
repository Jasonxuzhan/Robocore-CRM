import mysql.connector 


# Create crm database
def create_database(databasename="crmdatabase"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        )

    my_cursor = mydb.cursor()
    
    my_cursor.execute(f"CREATE DATABASE {databasename}")

    my_cursor.execute("SHOW DATABASES")
    for db in my_cursor:
        print(db)
    
    mydb.commit()
    mydb.close()


# Create Leads information table 
def create_leadsinfo_table(databasename="crmdatabase", tablename="Leads_information"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    my_cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename} (
                     ID INT AUTO_INCREMENT PRIMARY KEY,
                     Register_Date DATE,
                     Nation VARCHAR(255),
                     Province VARCHAR(255),
                     City VARCHAR(255),  
                     Company_Name VARCHAR(255),
                     Contact_Name VARCHAR(255),
                     Telephone VARCHAR(255),
                     Scenario VARCHAR(255),
                     Cooperation VARCHAR(255),
                     Desc_of_Request VARCHAR(255),
                     Lead_From VARCHAR(255), 
                     Lead_Channel VARCHAR(255), 
                     Channel_Details VARCHAR(255), 
                     Answer_By VARCHAR(255)
                    )""")

    my_cursor.execute("SHOW TABLES")

    for table in my_cursor:
        print(table[0])
    
    mydb.commit()
    mydb.close()


# Insert lead info into leads information table 
def insert_customerinfo(databasename="crmdatabase", tablename="leads_information"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sqlstuff = f"""INSERT INTO {tablename} (
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
    
    record1 = ( 
               "China", 
               "Guangdong", 
               "Shenzhen", 
               "Robocore automation", 
               'Jason', 
               "18664301788",
               "Showroom",
               "Distributor",
               "Will by one temi",
               "Hotline",
               "Baidu",
               "Baidu",
               "Ella") 
    
    my_cursor.execute(sqlstuff, record1)  
    
    mydb.commit()
    mydb.close()


# Create customer follow table 
def create_customerfollow_table(databasename="crmdatabase", tablename="customer_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    my_cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename} (
                     ID INT,
                     Status VARCHAR(255),
                     Date DATE,
                     Follow_Info VARCHAR(255),
                     Follow_By VARCHAR(255))""")
    
    mydb.commit()
    mydb.close()


# Insert follow info into customer follow table 
def insert_customerfollow(databasename="crmdatabase", tablename="customer_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sqlstuff = f"""INSERT INTO {tablename} (
                     ID,
                     Status,
                     Date,
                     Follow_Info,
                     Follow_By
                ) VALUES(%s, %s, NOW(), %s, %s)"""
    
    record1 = (1, "follow", "send the file to customer", "Jason") 
    
    my_cursor.execute(sqlstuff, record1)  
    
    mydb.commit()
    mydb.close()


# Drop table 
def drop_table(databasename="crmdatabase", tablename="leads_information"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sqlstuff = f"""DROP TABLE {tablename}""" 

    my_cursor.execute(sqlstuff)

    mydb.commit()
    mydb.close()








if __name__ == "__main__":
    drop_table(databasename="crmdatabase", tablename="leads_information")
    create_leadsinfo_table(databasename="crmdatabase", tablename="leads_information")




