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


class AESCipher(object):

    def __init__(self, key , iv):
        self.bs = 32
        self.key = key
        self.iv = iv

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]



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
        hash = self.getHashMD5(Data[0])
        if Data[1][0] == hash :
            print 'ok!\n'
            
            f = open('/home/art/Documents/alisapublickey.txt','rb')
            publicKeyFromServer = f.read(); f.close()
            print publicKeyFromServer
            
            if Data[0][1] == publicKeyFromServer:
                print 'pubkey True\n'
                
                self.sessionKey = Random.new().read(32)
                self.sock.send(self.createClientKeyExchangeMessage(publicKeyFromServer,self.sessionKey))
                serverKeyExchangeMessage = self.sock.recv(2048)

                ExchangeMessage = self.messageProcessing(serverKeyExchangeMessage)
                print ExchangeMessage[0]

                self.vector = (ExchangeMessage[0][0])

                self.aesCFB = AES.new(self.sessionKey, AES.MODE_CFB, self.vector)
                serverMessage = pickle.loads(self.aesCFB.decrypt(ExchangeMessage[1][0]))

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
        if statusLogin:
            self.chiper = AESCipher(self.sessionKey, self.vector)
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

    def send_message(self, message):
        self.sock.send(str(message))


    def encriptMessage(self, message):
        ExchangeMessage = []
        encryptMessage = []

        listMessage = message[:]
        hash = []

        encoded = self.chiper.encrypt(pickle.dumps(listMessage, 2))

        encryptMessage.append(encoded)
        hash.append(self.getHashMD5(encryptMessage[0]))

        ExchangeMessage.append(encryptMessage)
        ExchangeMessage.append(hash)

        encryptedAndDumpMessage = pickle.dumps(ExchangeMessage, 2)
        return encryptedAndDumpMessage



    def sendSearchFriendsMessage(self, friendName):
        listMess = []
        listMess.append('8')
        listMess.append(friendName)
        searchFriendsMessage = self.encriptMessage(listMess)
        self.send_message(searchFriendsMessage)
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
            data = self.sock.recv(2048)
            serverMessage = pickle.loads(data)
            print serverMessage
            decoded  = self.chiper.decrypt(str(serverMessage[0][0]).decode('utf-8'))
            encryptMessage = pickle.loads(decoded)
            print encryptMessage

            if encryptMessage[0] == '9':
                return encryptMessage
            else:
                return str(encryptMessage)


    def sendMess(self, message):
        self.sock.send(str(message))

# ..........Test Methods End...............................

    
    
    
    
    
    
    
