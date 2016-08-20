#!/usr/bin/env python

__author__ = "Husnain Taseer husnain.taseer@gmail.com"

"""
This Webservice is written to create/delete user in Jasmin SMS Gateway from HTTP request with basic options
which can be helpful in making web based GUI for SMS gateway. This simple web service can be called to create/delete
users in the SMSC.
"""

from flask import Flask, jsonify, request, Response, make_response, abort

import os
import subprocess
JasminWebservice = Flask(__name__)

@JasminWebservice.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@JasminWebservice.route('/jsms/webservice', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    try:
        path = os.getcwd()
        print path
        print "python " + path + "/JasminIntegration.py " + """ "%s" """%str(request.json) +  " " + request.method
        ret = subprocess.check_output(["python" , path + "/JasminIntegration.py" , "%s"%str(request.json) , request.method])
        ret = ret.rstrip('\n')
        if ret == 'pass' :
             return make_response(jsonify({'Error': 'Password Invalid'}), 403)
        elif ret == 'user' :
             return make_response(jsonify({'Error': 'Username Invalid'}), 403)
        elif ret == 'tp' :
             return make_response(jsonify({'Error': 'Throughput Invalid'}), 403)
        elif ret == 'session' :
             return make_response(jsonify({'Error': 'Sessions Invalid'}), 403)
        else:
            return jsonify({'Response':'Success'}), 201
    except Exception, e:
        print str(e)
@JasminWebservice.route('/jsms/webservice', methods=['DELETE'])
def delete_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    try:
        path = os.getcwd()
        print path
        print "python " + path + "/JasminIntegration.py " + """ "%s" """%str(request.json) +  " " + request.method
        ret = subprocess.check_output(["python" , path + "/JasminIntegration.py" , "%s"%str(request.json) , request.method])
        ret = ret.rstrip('\n')
        if ret == 'user' :
             return make_response(jsonify({'Error': 'Username Invalid'}), 403)
        else:
            return jsonify({'Response':'Success'})
    except Exception, e:
        print str(e)
    

if __name__ == '__main__':    
    JasminWebservice.run(host="0.0.0.0",port=7034,debug=True)

