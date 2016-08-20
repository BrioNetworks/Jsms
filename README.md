# Jsms

Jasmin Webservice URL : http://localhost:7034/jsms/webservice
#########################
#To Create User in SMSC:#
#########################
### REQUEST

Request = POST<br />
Content-Type: application/json<br />
Parameters: {"username":"userToCreate", "password":"PassToSet", "tp":"ThrouputAllowed", "sessions" : "SessionsAllowed"}<br />
username : cid of the user which needs to be create<br />
password : Password of the user should be less than 8 char<br />
tp: Throughput it must be a number<br />
sessions: must be a number. its total number of allowed sessions<br />

### RESPONSES ###
***** In case of Success ***** <br />
HTTP 201 CREATED<br />
{<br />
"Response": "Success"<br />
}<br />

***** Failure *****<br />
HTTP 403 FORBIDEN<br />
{<br />
"Error": "Username Invalid"<br />
}<br />
{<br />
"Error": "Password Invalid"<br />
}<br />
{<br />
"Error": "Throughput Invalid"<br />
}<br />
{<br />
"Error": "Sessions Invalid"<br />
}<br />
###########################
#To delete User from SMSC:#
###########################
### REQUEST ####
Request = DELETE <br />
Content-Type: application/json<br />
Parameters: {"username":"userToCreate"}<br />
username : cid of the user which needs to be deleted<br />

### RESPONSES ###
***** In case of Success ***** <br />
HTTP 200 OK<br />
{<br />
"Response": "Success"<br />
}<br />
***** Failure *****<br />
HTTP 403<br />
{<br />
"Error": "Username Invalid"<br />
}<br />
