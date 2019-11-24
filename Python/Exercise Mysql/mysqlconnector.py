#!/usr/bin/python
import mysql.connector as mariadb

class MysqlConnection():
#Class for Mysql (Mariadb) connection.
    
    def __init__(self):
        self.mariadb_connection = mariadb.connect(user='root', database='userreg')
        self.cursor = self.mariadb_connection.cursor()

        
    def __exit__(self):
        self.mariadb_connection.close()
        self.cursor.close()

    def mysql_query(self):
        """
        Querying the MYSQL (Mariadb) Database.
        Return the Output value.
        """
        try:
            self.cursor.execute("SELECT first_name, last_name FROM app_user;")
        except mariadb.Error as error:
            print("Error: {}".format(error))
        return self.cursor
