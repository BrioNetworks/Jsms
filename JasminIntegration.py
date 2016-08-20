#!/usr/bin/env python
import sys
import pickle
from twisted.internet import defer, reactor
from jasmin.managers.proxies import SMPPClientManagerPBProxy
from jasmin.routing.proxies import RouterPBProxy
from jasmin.routing.Routes import DefaultRoute
from jasmin.routing.jasminApi import SmppClientConnector, User, Group, MtMessagingCredential, SmppsCredential
from jasmin.protocols.smpp.configs import SMPPClientConfig
from twisted.web.client import getPage
import ast


@defer.inlineCallbacks
def runScenario(Request, method):
    try:
        proxy_router = RouterPBProxy()
        yield proxy_router.connect('127.0.0.1', 8988, 'radmin', 'rpwd')
    
        if method == "POST":
            smppUser = Request['username']
            smppPass = Request['password']
            smppThroughput = Request['tp']
            smppBindSessions = Request['sessions']
            
            if not smppUser:
                raise NameError('user')
                
            if len(smppPass) == 0 or len(smppPass) > 8:
                raise NameError('pass')
                
            if not smppThroughput.isdigit():
                raise NameError('tp')
                
            if not smppBindSessions.isdigit():
                raise NameError('session')
            
            # Provisiong router with users
            smpp_cred = SmppsCredential()
            yield smpp_cred.setQuota('max_bindings',int(smppBindSessions))
            mt_cred = MtMessagingCredential()
            yield mt_cred.setQuota('smpps_throughput' , smppThroughput)
            #yield mt_cred.setQuota('submit_sm_count' , 500)
        
            g1 = Group('clients')
            u1 = User(uid = smppUser, group = g1, username = smppUser, password = smppPass, mt_credential = mt_cred, smpps_credential = smpp_cred)
            yield proxy_router.group_add(g1)
            yield proxy_router.user_add(u1)
            print "Success"
        if method == 'DELETE':
            
            smppUser = Request['username']
            
            if not smppUser:
                raise NameError('user')
                
            yield proxy_router.user_remove(smppUser) 
    except Exception, e:
        print "%s" %str(e)

    finally:
        reactor.stop()

#request = {'username' : 'abc' , 'password':'abc', 'tp':'1', 'sessions':'1', 'method':'POST' }
request = sys.argv[1]
method = sys.argv[2]
request = ast.literal_eval(request)
runScenario(request,method)
reactor.run()