#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0,"/home/art/Desktop/prgosay/requests/")
import requests

import time
import socket
import hashlib
import base64
import os

from Crypto.Cipher import AES
from Crypto import Random


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#import math
#import threading


import cPickle as pickle

class A:
    def __init__(self):
        self.sessionKey = ''
        self.vector = ''

        self.conne = False
        self.HOST = 'localhost'
        self.PORT = 8000
        self.BUFSIZE = 2048
        self.ADDR = (self.HOST,self.PORT)


        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serverCertificateMessage = '1'

    
    STATUSCONNECTION = False
    ACCEPTEDTMESSAGE = []
    PUBLICKEYFROMSERVER = []
    clientKeyExchangeMessage = []


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
                
                self.sessionKey = Random.new().read(32)

                self.sock.send(self.createClientKeyExchangeMessage(publicKeyfromServer,self.sessionKey))
                serverKeyExchangeMessage = self.sock.recv(2048)
                p = []
                p.append(serverKeyExchangeMessage)
                print p
                ExchangeMessage = self.messageProcessing(serverKeyExchangeMessage)
                print ExchangeMessage[0]

                self.vector = (ExchangeMessage[0][0])
                

                obj = AES.new(self.sessionKey, AES.MODE_CFB, self.vector)
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
        obj2 = AES.new(self.sessionKey, AES.MODE_CFB, self.vector)
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
        
        self.mainObj = AES.new(self.sessionKey, AES.MODE_CFB, self.vector)
        statusLoginMessage = pickle.loads(self.mainObj.decrypt(serverMessage[0][0]))
        print statusLoginMessage
        statusLogin = statusLoginMessage[1]
        return statusLogin














    
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
        # размер блока шифрования
        BLOCK_SIZE = 32
        # символ, использующийся для дополнения шифруемых данных
        # до размера, кратного 32 байтам
        PADDING = '{'
        # функция дополнения
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))


        ExchangeMessage = []
        encryptMessage = []

        listMessage = message[:]
        diagest = []

        LO = []
        LO.append(pickle.dumps(listMessage, 2))
        encoded = EncodeAES(self.mainObj, LO[0])


        encryptMessage.append(encoded)
        diagest.append(self.getHashMD5(encryptMessage[0]))

        ExchangeMessage.append(encryptMessage)
        ExchangeMessage.append(diagest)

        encryptedAndDumpMessage = pickle.dumps(ExchangeMessage, 2)
        return encryptedAndDumpMessage



    def sendSearchFriendsMessage(self, friendName):
        listMess = []
        listMess.append('8')
        listMess.append(friendName)

        print listMess

        SearchFriendsMessage = self.encriptMessage(listMess)
        self.sock.send(str(SearchFriendsMessage))
        #self.send_message_action(SearchFriendsMessage)
        #return SearchFriendsMessage


#..........Test Methods...............................


    def process_message(self, argument):
        method_name = 'number_' + str(argument[0])
        method = getattr(self, method_name, lambda: "nothing")
        return method(argument)

    def number_9(self, argument):
        respond, status  = requests.searchAllUsersWithName(argument[1])
        return status



    def whileReceive(self):
        if self.conne == False:
            self.conne = True
        else:
            print '............start rec...........'
            # размер блока шифрования
            BLOCK_SIZE = 32
            # символ, использующийся для дополнения шифруемых данных
            # до размера, кратного 32 байтам
            PADDING = '{'
            # функция дополнения
            DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

            data = self.sock.recv(2048)
            serverMessage = pickle.loads(data)
            print serverMessage

            #cipher = AES.new(self.sessionKey)
            decoded = DecodeAES(self.mainObj, serverMessage[0][0])
            print decoded
            encryptMessage = pickle.loads(decoded)

            print encryptMessage

            return str(encryptMessage)


    def sendMess(self, message):
        self.sock.send(str(message))

# ..........Test Methods End...............................

    
    
    
    
    
    
    
