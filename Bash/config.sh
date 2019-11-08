#!/bin/bash

#Create Role
R_NAME=("USER" "ADMIN")
R_DESCRIPTION=("User Rights" "Admin Rights")



#Create User
U_FIRSTNAME=("Peter" "Hans")
U_NAME=("Mueller" "Wurschd")
U_UNAME=("PEMUE" "HAWU")
U_EMAIL=("peter.mueller@user.ch" "hans.wurschd@user.ch")
U_EXPIRE=(0 1)
U_PASS=("Welcome01" "Welcome02")
U_ROLE=("USER" "ADMIN")

if [ -n "${U_ROLE[$i]}" ] ; then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO user_role (user_id,role_id) VALUE ("${uname[$i]}","${roleid[$i]}");
EOFMYSQL
   echo "User ${uname[$i+1]} has ${roleid[$i]} rights!"
else
   echo "User or role not found in DB...";
fi