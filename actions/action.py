#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0,"/home/art/Desktop/prgosay/requests/")
import requests

import time
import socket
import hashlib


from Crypto.Cipher import AES
from Crypto import Random

import cPickle as pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#import math
#import threading



class A():
    
    HOST = 'localhost'
    PORT = 8000
    BUFSIZE = 2048
    ADDR = (HOST,PORT)
    

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serverCertificateMessage = '1'

    
    STATUSCONNECTION = False
    ACCEPTEDTMESSAGE = []
    PUBLICKEYFROMSERVER = []
    clientKeyExchangeMessage = []

    sessionkey = ''
    vector = ''


    def getHashMD5(self, text):
        hash_md5 = hashlib.md5()
        hash_md5.update(str(text))
        return hash_md5.hexdigest()
     
    def messageProcessing(self, mess):
        
        print'.......mess ........'
        RESULT = pickle.loads(mess)
    
        return RESULT
       
     
     
    def createClientKeyExchangeMessage(self,publicKeyfromServer,skey):
    
        listMess = []
        listHesh = []
    
        ExchangeMessage = []
    
        listMess.append('2')
        listMess.append(skey)
        listHesh.append(self.getHashMD5(listMess))
        
        ExchangeMessage.append(listMess)
        ExchangeMessage.append(listHesh)
    
        bytesForSend = pickle.dumps(ExchangeMessage,2)
        key = RSA.importKey(publicKeyfromServer)
        cipher = PKCS1_OAEP.new(key)
        clientExchangeMessage = cipher.encrypt(bytesForSend)
        
        return clientExchangeMessage
              
            
    def closeConnect(self):
            self.sock.shutdown()
            print 'conn close!'    
    
    
    def checkServerKeyExchangeMessage(self,data):
        sendMoreClientKeyExchangeMessage = True
        statusConnection = False
        if not data:
            self.closeConnect()
            sendMoreClientKeyExchangeMessage = False
            statusConnection = False
        else:
            clientKeyExchangeMessage = self.messageProcessing(data)
            if(clientKeyExchangeMessage == ['3','key passed to the encrypted mode']):
                sendMoreClientKeyExchangeMessage = False
                statusConnection = True
                print 'server connection estabilished'
            if(clientKeyExchangeMessage == ['3','error encrypted connection']):
                sendMoreClientKeyExchangeMessage = True
                statusConnection = False
                print 'server connection error'
        
        return sendMoreClientKeyExchangeMessage, statusConnection

     
    
    
    

    def estabilishConnection(self):
        #self.sock.settimeout(15)
        self.sock.connect(self.ADDR)
        statusConnection = False
    
        data = self.sock.recv(2048)
    
        Data = self.messageProcessing(data)    
        print 'bery hesh'
        hesh = self.getHashMD5(Data[0])
        if(Data[1][0] == hesh):
            print 'ok!\n'
            
            f = open('/home/art/Documents/alisapublickey.txt','rb')
            publicKeyfromServer = f.read(); f.close()
            print publicKeyfromServer
            
            if(Data[0][1] == publicKeyfromServer):
                print 'pubkey True\n'
                
                self.sessionkey = Random.new().read(32)

                self.sock.send(self.createClientKeyExchangeMessage(publicKeyfromServer,self.sessionkey))
                serverKeyExchangeMessage = self.sock.recv(2048)
                p = []
                p.append(serverKeyExchangeMessage)
                print p
                ExchangeMessage = self.messageProcessing(serverKeyExchangeMessage)
                print ExchangeMessage[0]

                self.vector = (ExchangeMessage[0][0])
                

                obj = AES.new(self.sessionkey, AES.MODE_CFB, self.vector)
                serverMessage = pickle.loads(obj.decrypt(ExchangeMessage[1][0]))

                
                print ExchangeMessage[0]
                print str(ExchangeMessage[1]) + str(serverMessage)
                print ExchangeMessage[2]
                       
                statusConnection = serverMessage[1]
                
                print '....status conn....' + str(statusConnection)            
                
        else:
            print 'tobi pizda'
            statusConnection = False
        if(statusConnection):
            print 'statusConnection true ...... action pacage'
            
            
        print statusConnection   
        return statusConnection

    def loginAction(self, login, password):
        print '.....loginAction.......'
        obj2 = AES.new(self.sessionkey, AES.MODE_CFB, self.vector)
        ExchangeMessage = []
        Message = []

        listMess = []
        listHesh = []
        
        listMess.append('4')
        listMess.append(login)
        listMess.append(password)

        Message.append(obj2.encrypt(pickle.dumps(listMess,2)))
        listHesh.append(self.getHashMD5(Message))
        
        ExchangeMessage.append(Message)
        ExchangeMessage.append(listHesh)
        
        clientLoginMessage = pickle.dumps(ExchangeMessage,2)
        self.sock.send(clientLoginMessage)
        data = self.sock.recv(2048)
        
        serverMessage = pickle.loads(str(data))
        
        obj = AES.new(self.sessionkey, AES.MODE_CFB, self.vector)
        statusLoginMessage = pickle.loads(obj.decrypt(serverMessage[0][0]))
        print statusLoginMessage
        statusLogin = statusLoginMessage[1]
        return statusLogin






#..........Test Methods...............................

    conne = False
    count = 0
    def whileReceive(self):
        l = []
        l.append(self.sessionkey)
        l.append(self.vector)
        print l
        if(self.conne == False):
            l1 = []
            l1.append(self.sessionkey)
            l1.append(self.vector)
            print l
            self.conne = True
        else:
            print 'else'
            l3 = []
            l3.append(self.sessionkey)
            l3.append(self.vector)
            print l3
            print 'end else'
            data = self.sock.recv(2048)
            self.count = self.count + 1
            if self.count > 1:
                print  data
                serverMessage = pickle.loads(str(data))
                print 'else'
                l4 = []
                l4.append(self.sessionkey)
                l4.append(self.vector)
                print l3
                print 'end else.........'
                print serverMessage
                print serverMessage[0]
                objdec = AES.new(self.sessionkey, AES.MODE_CFB, self.vector)

                statusLoginMessage = pickle.loads(objdec.decrypt(str(serverMessage[0][0])))
                print statusLoginMessage
                statusLogin = statusLoginMessage[1]

                return str(statusLogin)
            return 'lop'


    def sendMess(self, message):
        self.sock.send(str(message))

# ..........Test Methods End...............................








    
    def regestrationAction(self,login,password):
        listForRegistration = []
        listForRegistration.append('10')
        listForRegistration.append(str(login))
        listForRegistration.append(str(password))
        print listForRegistration
        self.sendMess(listForRegistration)
        firstname, statusRegistration = requests.searchUserByNameOrLogin(login)
        print str(firstname) + ' lol ' + str(statusRegistration)
        if(statusRegistration):
            print ' scha bydem regati'
            requests.registrationUserRequest(login)
        else:
            print 'user yge exist'
        print ''

    def send_message_action(self, message):
        print message
        self.sock.send(str(message))


    def encriptMessage(self, message):
        obj = AES.new(self.sessionkey, AES.MODE_CFB, self.vector)
        ExchangeMessage = []
        encriptMessage = []

        listMess = message
        listHesh = []

        encriptMessage.append(obj.encrypt(pickle.dumps(listMess, 2)))
        listHesh.append(self.getHashMD5(encriptMessage))

        ExchangeMessage.append(encriptMessage)
        ExchangeMessage.append(listHesh)
        print ExchangeMessage
        encriptedAndDumpMessage = pickle.dumps(ExchangeMessage, 2)
        return encriptedAndDumpMessage



    def sendSearchFriendsMessage(self, friendName):
        listMess = []
        listMess.append('8')
        listMess.append(friendName)

        print listMess

        SearchFriendsMessage = self.encriptMessage(listMess)
        self.sock.send(SearchFriendsMessage)




    
    
    
    
    
    
    
