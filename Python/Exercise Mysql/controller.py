#!/usr/bin/python
import mysqlconnector
from user import *

connect = mysqlconnector.MysqlConnection()

#-----------------------ROLE-----------------------------------------------------------------


for idx,line in enumerate(R_NAME):
    role = "select name FROM role WHERE name = '%s'" % line
    value = connect.mysql_query(role)
    msg = value.fetchone()
    #Check if role is already in db
    if not msg:
        query = "INSERT INTO role (description,name) VALUE ('%s','%s')" % (R_DESCRIPTION[idx],line)
        connect.mysql_query(query)
        print("Role %s added to DB!" % line)
    else:
        print(R_DESCRIPTION[idx] + " Role already in DB...")

#---------------------USER-------------------------------------------------------------------

for idx,line in enumerate(U_UNAME):
    role = "select username FROM app_user WHERE username= '%s'" % line
    print(role)
    value = connect.mysql_query(role)
    msg = value.fetchone()
    print(msg)
    #Check if User is already in db
    if not msg:
        query = "INSERT INTO app_user (account_expired,email,first_name,last_name,password,username) VALUE ('%s','%s','%s','%s','%s','%s')" % (U_EXPIRE[idx],U_EMAIL[idx],U_FIRSTNAME[idx],U_NAME[idx],U_PASS[idx],U_UNAME[idx])
        print(query)
    else:
        print(U_FIRSTNAME[idx] + " " + U_NAME[idx] + " is already in DB...")

#------------------ADD ROLE TO USER-------------------------------------------------------------------

"""
query = "SELECT first_name, last_name FROM app_user;"
result = connect.mysql_query(query)
for first_name,last_name in result:
    print("First name: {}, Last name: {}".format(first_name,last_name))
    

for line in R_NAME:
    print(line)
"""




