#!/usr/bin/python
import mysql.connector as mariadb

class MysqlConnection():
#Class for Mysql (Mariadb) connection.
    
    def __init__(self):
        self.mariadb_connection = mariadb.connect(user='root', database='userreg')
        self.cursor = self.mariadb_connection.cursor(buffered=True)

        
    def __exit__(self):
        self.mariadb_connection.close()
        self.cursor.close()

    def mysql_query(self,query):
        """
        Querying the MYSQL (Mariadb) Database.
        Return the Output value.
        """
        try:
            self.cursor.execute(query)
        except mariadb.Error as error:
            print("Error: {}".format(error))
        self.mariadb_connection.commit()
        return self.cursor