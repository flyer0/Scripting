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
    value = connect.mysql_query(role)
    msg = value.fetchone()
    #Check if User is already in db
    if not msg:
        query = "INSERT INTO app_user (account_expired,email,first_name,last_name,password,username) VALUE (%s,'%s','%s','%s','%s','%s')" % (U_EXPIRE[idx],U_EMAIL[idx],U_FIRSTNAME[idx],U_NAME[idx],U_PASS[idx],U_UNAME[idx])
        connect.mysql_query(query)
        print("User " + U_FIRSTNAME[idx] + " " + U_NAME[idx] + " added to DB!")
    else:
        print(U_FIRSTNAME[idx] + " " + U_NAME[idx] + " is already in DB...")

#------------------ADD ROLE TO USER-------------------------------------------------------------------
i=0
for idx,line in enumerate(U_UNAME):
    roleid="select id,name FROM role WHERE name = '%s';" % U_ROLE[idx]
    uname="select id,username FROM app_user WHERE username = '%s';" % U_UNAME[idx]
    value = connect.mysql_query(roleid)
    currentrole = value.fetchone()
    value2 = connect.mysql_query(uname)
    currentuser = value2.fetchone()

    idn="select user_id,role_id FROM user_role WHERE role_id = '%s' AND user_id = '%s'" % (currentrole[0],currentuser[0])
    value = connect.mysql_query(idn)
    idcheck = value.fetchone()

    #Check if ID is already taken
    if not idcheck:
        query = "INSERT INTO user_role (user_id,role_id) VALUE (%s,%s);" % (currentuser[0],currentrole[0])
        connect.mysql_query(query)
        print("User " + currentuser[1] + " has " + currentrole[1] + " rights!")
    else:
       print("Role-User already associated!")

#------------------Ausgabe-------------------------------------------------------------------
print("-------------------- AUSGABE ---------------------")
query = "SELECT U.first_name,U.last_name, R.name FROM app_user U INNER JOIN user_role UR ON U.id = UR.user_id INNER JOIN role R ON UR.user_id = role_id;"
msg = connect.mysql_query(query)
print(msg.fetchall())