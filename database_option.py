import mysql.connector

class Database_Options:
    def __init__(self, host, user, passwd, database_name):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.auth_plugin = "mysql_native_password"
        self.database = database_name
        self.mydb = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            auth_plugin = self.auth_plugin, 
            database = self.database)
        self.my_cursor = self.mydb.cursor()
    
    def cursor_excute(self, sqlstuff:str, stuff=None) -> None:
        self.my_cursor.execute(sqlstuff, stuff)
        self.mydb.commit()
        self.mydb.close()





