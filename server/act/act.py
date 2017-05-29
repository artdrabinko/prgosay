#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from Crypto.Cipher import AES
#import base64
#import os

import sys
sys.path.insert(0,"/home/art/PycharmProjects/prgosay/server/requests/")
import requests

import hashlib
import cPickle as pickle



class A():

    sessionkey = ''
    vector = ''
    

    def getHashMD5(self,text):
        hash_md5 = hashlib.md5()
        hash_md5.update(str(text))
        return hash_md5.hexdigest()
     
    def messageProcessing(self,messToProc):
        
        print'.......mess proc........'
        RESULT = pickle.loads(messToProc)    
    
        return RESULT
       


    
    def sendMess(self, message):
        self.sock.send(str(message))
        
    
    def regestrationAction(self,login,password):
        listForRegestration = []
        listForRegestration.append('10')
        listForRegestration.append(str(login))
        listForRegestration.append(str(password))
        print listForRegestration
        self.sendMess(listForRegestration)
        firstname, statusRegistration = requests.searchUserByNameOrLogin(login)
        print str(firstname) + ' lol ' + str(statusRegistration)
        if(statusRegistration):
            print ' scha bydem regati'
            requests.registrationUserRequest(login)
        else:
            print 'user yge esti'

        
    
    
    
    
    
    
    
    
    
