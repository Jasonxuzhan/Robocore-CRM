import mysql.connector


# Create database
def create_database(databasename="robocorecrm"):
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


# Create table 1
def create_leadsinfo_table(databasename="robocorecrm", tablename="Leads_information"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    my_cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename} (
                     User_id INT AUTO_INCREMENT PRIMARY KEY,  
                     Register_date DATE,
                     Leads_from VARCHAR(255),
                     Leads_channel VARCHAR(255),
                     Leads_details VARCHAR(255) DEFAULT NULL,
                     Province VARCHAR(255),
                     City VARCHAR(255),
                     Company_name VARCHAR(255) DEFAULT NULL,
                     Contact_person VARCHAR(255),
                     Telephone VARCHAR(255),
                     Scenario VARCHAR(255),
                     Cooperation VARCHAR(255),
                     Request_desc VARCHAR(255),
                     Answer_by VARCHAR(255),
                     Sales_follow VARCHAR(255)
         )""")

    my_cursor.execute("SHOW TABLES")

    for table in my_cursor:
        print(table[0])
    
    mydb.commit()
    mydb.close()


# Create table 2
def create_leads_follow_table(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sqlstuff = f"""CREATE TABLE IF NOT EXISTS {tablename} (
        lead_info_key INT AUTO_INCREMENT PRIMARY KEY, 
        user_id INT NOT NULL,
        follow_by VARCHAR(255),
        follow_time DATETIME,
        follow_info VARCHAR(255),
        how_to_deal VARCHAR(255),
        remark VARCHAR(255),
        FOREIGN KEY(user_id) REFERENCES Leads_information(User_id)
        )"""    
     
    my_cursor.execute(sqlstuff)  
    
    mydb.commit()
    mydb.close()


# Insert info into table - leads_information
def insert_customerinfo(databasename="robocorecrm", tablename="leads_information"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sqlstuff = f"""INSERT INTO {tablename} (  
                     Register_date,
                     Leads_from,
                     Leads_channel,
                     Leads_details,
                     Province,
                     City,
                     Company_name,
                     Contact_person,
                     Telephone,
                     Scenario,
                     Cooperation, 
                     Request_desc,
                     Answer_by, 
                     Sales_follow 
        ) VALUES(NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    record1 = ( 
               "hotline", 
               "baidu search", 
               "introduce by friend", 
               "Guangdong", 
               'Shenzhen', 
               "temi company",
               "Jason",
               "18664301788",
               "Showroom",
               "Distributor",
               "to be distributor",
               "Ella",
               "Jason") 
    
    my_cursor.execute(sqlstuff, record1)  
    
    mydb.commit()
    mydb.close()


# Insert info into table - lead_follow 
def insert_leadinfo(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sqlstuff = f"""INSERT INTO {tablename} (
                     user_id,
                     follow_by,
                     follow_time,
                     follow_info,
                     how_to_deal,
                     remark) VALUES(%s, %s, NOW(), %s, %s, %s)"""
    
    record1 = (1, "jason", "not buy", "give up", "not target customer") 
    
    my_cursor.execute(sqlstuff, record1)  
    
    mydb.commit()
    mydb.close()


# Delete table 
def delete_table(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )

    my_cursor = mydb.cursor()

    sql_query = f"DROP TABLE IF EXISTS {tablename}" 

    my_cursor.execute(sql_query)
    
    mydb.commit()
    mydb.close()


# Modify column 
def modify_column(databasename="robocorecrm", tablename="leads_information"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    sqlstuff = f"ALTER TABLE {tablename} MODIFY COLUMN Telephone VARCHAR(255)" #RENANME COLUMN xxx to xxx 
     
    my_cursor.execute(sqlstuff)  
    
    mydb.commit()
    mydb.close()


# Alter table clomun to default 
def to_default(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    sqlstuff = f"ALTER TABLE {tablename} ALTER Follow_by SET DEFAULT 'jason'"

    my_cursor.execute(sqlstuff)  
    
    mydb.commit()
    mydb.close()


# Alter table add new column 
def add_column(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    sqlstuff = f"ALTER TABLE {tablename} ADD user_id INT FIRST"

    my_cursor.execute(sqlstuff)

    mydb.commit()
    mydb.close()

# Update info 
def update_info(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    sqlstuff = f"UPDATE {tablename} SET user_id = 1 WHERE Follow_by = 'jason'"

    my_cursor.execute(sqlstuff)

    mydb.commit()
    mydb.close()

def delete_row(databasename="robocorecrm", tablename="lead_follow"):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "jason121",
        auth_plugin = "mysql_native_password", 
        database = databasename
        )
    
    my_cursor = mydb.cursor()

    sqlstuff = f"DELETE FROM {tablename} WHERE user_id = 1"

    my_cursor.execute(sqlstuff)

    mydb.commit()
    mydb.close()




if __name__ == "__main__":
   #insert_customerinfo(databasename="robocorecrm", tablename="leads_information")
   #insert_leadinfo(databasename="robocorecrm", tablename="lead_follow")
   #to_default(databasename="robocorecrm", tablename="lead_follow")
   #delete_table(databasename="robocorecrm", tablename="lead_follow")
   #create_leads_follow_table(databasename="robocorecrm", tablename="lead_follow")
   #update_info(databasename="robocorecrm", tablename="lead_follow")
   #add_column(databasename="robocorecrm", tablename="lead_follow")
   #delete_row(databasename="robocorecrm", tablename="lead_follow")
   #insert_leadinfo(databasename="robocorecrm", tablename="lead_follow")
   pass

   


    


