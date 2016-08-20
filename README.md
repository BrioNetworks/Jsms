# Jsms

This Webservice is written to create/delete user in [Jasmin SMS Gateway] (http://www.jasminsms.com/) from HTTP request with basic options which can be helpful in making web based GUI for SMS gateway. This simple web service can be called to create/delete users in the SMSC.

Before using this webservice you should be familiar of Jasmin SMS Gateway and also should have installed and running. Also Perspective Broker API should be running on port 8988. In this code default username and password is used to connect with PB if you have different credentials you can change in the code.

You also need following python packages to run this web service.
Flask
pickle
twisted python

First you need to run JasminWebservice.py 
```
./JasminWeBservice.py
```
After that you can make a request to create user in JSMSC:

#Create Request
```
curl -i -H "Content-Type: application/json" -X POST -d '{"username":"husnain", "password":"jsmsapi", "tp":"10", "sessions" : "1"}' http://localhost:7034/jsms/webservice

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.9.6 Python/2.7.3
Date: Fri, 19 Aug 2016 18:35:41 GMT

{
  "Response": "Success"
}
```

#Delete Request
```
curl -i -H "Content-Type: application/json" -X DELETE -d '{"username":"abc", "password":"ab123", "tp":"1", "sessions" : "1"}' http://localhost:7034/jsms/webservice

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.9.6 Python/2.7.3
Date: Fri, 19 Aug 2016 18:42:38 GMT

{
  "Response": "Success"
}

```


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
#To Delete User from SMSC:#
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
