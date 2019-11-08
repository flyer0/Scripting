#!/bin/bash

#Import Source
. /home/hfict/Scripting/Bash/config.sh

#-------------------ROLE---------------------------------------------------------------
#Check if Role is already in DB
for ((i=0;i<${#R_NAME[@]};i++));do

    role=$(mysql -D userreg -u root  -se "select name FROM role WHERE name = '${R_NAME[$i]}'")

if [ -z "$role" ]
then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO role (description,name) VALUE ("${R_DESCRIPTION[$i]}","${R_NAME[$i]}");
EOFMYSQL
  echo "Role ${R_NAME[$i]} added to DB!"
  
else
  echo "Role already in DB...";

fi

done

#-------------------USER---------------------------------------------------------------

for ((i=0;i<${#U_UNAME[@]};i++));do
user=$(mysql -D userreg -u root  -se "select username FROM app_user WHERE username= '${U_UNAME[$i]}'")

#Check if user is already in DB
if [ -z "$user" ]
then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO app_user (account_expired,email,first_name,last_name,password,username) VALUE (${U_EXPIRE[$i]},"${U_EMAIL[$i]}","${U_FIRSTNAME[$i]}","${U_NAME[$i]}","${U_PASS[$i]}","${U_UNAME[$i]}");
EOFMYSQL
  echo "User ${U_FIRSTNAME[$i]} ${U_NAME[$i]} added to DB!"
else
  echo "User already in DB...";
fi

done

#-------------------ADD ROLE TO USER----------------------------------------------------


for ((i=0;i<${#U_UNAME[@]};i++));do
 
roleid=$(mysql -D userreg -u root  -se "select id,name FROM role WHERE name = '${U_ROLE[$i]}'")
uname=$(mysql -D userreg -u root  -se "select id,username FROM app_user WHERE username = '${U_UNAME[$i]}'")

#Query output to Variables
read var1 var2 <<< $uname
read rvar1 rvar2 <<< $roleid


id=$(mysql -D userreg -u root  -se "select user_id,role_id FROM user_role WHERE role_id = '$rvar1' AND user_id='$var1'")


#Check if ID is already taken
if [ -z "$id" ] ; then
mysql -u root<<EOFMYSQL
use userreg;
INSERT INTO user_role (user_id,role_id) VALUE ($var1,$rvar1);
EOFMYSQL
   echo "User $var2 has $rvar2 rights!"
else
   echo "Role-User already associated!";
fi

done


