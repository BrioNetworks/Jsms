# Jsms

Jasmin Webservice URL : http://localhost:7034/jsms/webservice
#########################
#To Create User in SMSC:#
#########################
### REQUEST

Request = POST
Content-Type: application/json
Parameters: {"username":"userToCreate", "password":"PassToSet", "tp":"ThrouputAllowed", "sessions" : "SessionsAllowed"}
username : cid of the user which needs to be create
password : Password of the user should be less than 8 char
tp: Throughput it must be a number
sessions: must be a number. its total number of allowed sessions

### RESPONSES ###
***** In case of Success ***** 
HTTP 201 CREATED
{
"Response": "Success"
}

***** Failure *****
HTTP 403 FORBIDEN
{
"Error": "Username Invalid"
}
{
"Error": "Password Invalid"
}
{
"Error": "Throughput Invalid"
}
{
"Error": "Sessions Invalid"
}
###########################
#To delete User from SMSC:#
###########################
### REQUEST ####
Request = DELETE 
Content-Type: application/json
Parameters: {"username":"userToCreate"}
username : cid of the user which needs to be deleted

### RESPONSES ###
***** In case of Success ***** 
HTTP 200 OK
{
"Response": "Success"
}
***** Failure *****
HTTP 403
{
"Error": "Username Invalid"
}
