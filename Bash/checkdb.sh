#!/bin/bash

#Import Source
. /home/hfict/Scripting/Bash/config.sh

#-------------------ROLE---------------------------------------------------------------
#Check if Role is in DB
role=$(mysql -D userreg -u root  -se "select name FROM role WHERE name = '$R_NAME'")
if [ -z "$role" ]
then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO role (description,name) VALUE ("$R_DESCRIPTION","$R_NAME");
EOFMYSQL
  echo "Role $R_NAME added to DB!"
else
 echo "Role already in DB...";
fi
#-------------------USER---------------------------------------------------------------
user=$(mysql -D userreg -u root  -se "select username FROM app_user WHERE username= '$U_UNAME'")
if [ -z "$user" ]
then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO app_user (account_expired,email,first_name,last_name,password,username) VALUE ($U_EXPIRE,"$U_EMAIL","$U_FIRSTNAME","$U_NAME","$U_PASSWORD","$U_UNAME");
EOFMYSQL
  echo "User $U_FIRSTNAME $U_NAME added to DB!"
else
 echo "User already in DB...";
fi


#-------------------ADD ROLE TO USER----------------------------------------------------


roleid=$(mysql -D userreg -u root  -se "select id FROM role WHERE name = '$U_ROLE'")
unameid=$(mysql -D userreg -u root  -se "select id FROM app_user WHERE username = '$U_UNAME'")

rolename=$(mysql -D userreg -u root  -se "select name FROM role WHERE name = '$U_ROLE'")
uname=$(mysql -D userreg -u root  -se "select last_name FROM app_user WHERE username = '$U_UNAME'")

echo $roleid
echo $unameid

if [[ -n "$roleid" && -n "$unameid" ]] ; then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO user_role (user_id,role_id) VALUE ("$unameid","$roleid");
EOFMYSQL
  echo "User $uname has $rolename rights!"
else
 echo "User or role not found in DB...";
fi
