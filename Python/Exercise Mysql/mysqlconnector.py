#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', database='userreg')
cursor = mariadb_connection.cursor()

try:
    cursor.execute("SELECT first_name, last_name FROM app_user;")
except mariadb.Error as error:
    print("Error: {}".format(error))

for first_name,last_name in cursor:
    print("First name: {}, Last name: {}".format(first_name,last_name))




