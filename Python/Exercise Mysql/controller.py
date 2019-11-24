#!/usr/bin/python
import mysqlconnector

connect = mysqlconnector.MysqlConnection()

result = connect.mysql_query()
for first_name,last_name in result:
    print("First name: {}, Last name: {}".format(first_name,last_name))
    




