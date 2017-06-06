# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:17:27 2017

@author: art
"""
import sys
import cPickle as pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto import Random

import base64
import os
import time
import hashlib

from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic


import requests



def messageProcessing(data):

    RESULT = pickle.loads(data)    
    return RESULT
        
def getHashMD5(text):
    hash_md5 = hashlib.md5()
    hash_md5.update(str(text))
    result = hash_md5.hexdigest()
    return result

def loginActionFromUser(login, heshFromPassword):
        listForRegestration = []
        listForRegestration.append(str(login))
        listForRegestration.append(str(heshFromPassword))
        print listForRegestration
        statusLoginUser = requests.searchUserByLoginAndCheckPassword(login, heshFromPassword)

        return statusLoginUser

def searchActionUserByLoginInDB(login):
    conn = requests.searchConnectionByLogin(login)
    print type(conn)
    print '\n searchActionUserByLoginInDB ' + str(conn) + '\n'
    return conn

def createServerCerificateMessage():
    ServerCerificateMessage = []
    f = open('/home/art/Documents/alisapublickey.txt', 'rb')
    publicKey = f.read();
    f.close()

    listMess = []
    listHesh = []

    listMess.append('1')
    listMess.append(publicKey)
    listMess.append('gosay.net.ru')
    listMess.append('md5')

    listHesh.append(getHashMD5(listMess))

    ServerCerificateMessage.append(listMess)
    ServerCerificateMessage.append(listHesh)

    return ServerCerificateMessage





class Worker:
    def __init__(self,seanceKey, IV):
        self.key = seanceKey
        self.iv = IV
        self.cipher = AES.new(self.key, AES.MODE_CFB, self.iv)

    def getHashMD5(self, text):
        hash_md5 = hashlib.md5()
        hash_md5.update(str(text))
        return hash_md5.hexdigest()

    def decryptMessage(self, data):
        # символ, использующийся для дополнения шифруемых данных
        # до размера, кратного 32 байтам
        print 'decrypt......................'
        PADDING = '{'
        # функция дополнения
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
        clientMessage = pickle.loads(data)

        decoded = DecodeAES(self.cipher, clientMessage[0][0])
        decryptedMessage = pickle.loads(decoded)
        print str(decryptedMessage) + '.......decr message........'
        return decryptedMessage

    def encryptMessage(self, message):
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

        listMess = message[:]
        listHesh = []

        LO = []
        LO.append(pickle.dumps(listMess, 2))

        #cipher = AES.new(self.key)
        encoded = EncodeAES(self.cipher, LO[0])

        encryptMessage.append(encoded)
        listHesh.append(self.getHashMD5(encryptMessage[0]))

        ExchangeMessage.append(encryptMessage)
        ExchangeMessage.append(listHesh)

        print ExchangeMessage, 'exchange.........'
        encryptedAndDumpMessage = pickle.dumps(ExchangeMessage, 2)
        return encryptedAndDumpMessage

    def process_message(self, argument):
        method_name = 'number_' + str(argument[0])
        method = getattr(self, method_name, lambda: "nothing")
        return method(argument)

    def number_8(self, argument):
        respond, status  = requests.searchAllUsersWithName(argument[1])
        print str(respond[2]) + ' ' + str(respond[3])
        print status
        answer = {}
        answer[respond[0]] = respond
        listMess = []

        listMess.append('9')
        listMess.append(answer)
        print listMess
        messageForSend = self.encryptMessage(listMess)

        return messageForSend



class PubProtocol(basic.LineReceiver):

    def __init__(self, factory):
        self.factory = factory
        self.userLogin = ''
        self.seansKey = ''
        self.iv = Random.new().read(16)  # 128 bit

        self.statusConnection = False
        self.encripdetConnection = False
        self.statusAuthorithation = False
        self.UserLoginStatus = False

    def connectionMade(self):
        newUser = self.transport.getPeer()
        self.factory.clients.add(self)
        print "New user conntection: %s" % newUser
        bytesForSend = pickle.dumps(createServerCerificateMessage(),2)
        self.transport.write(bytesForSend)

    def sendServerKeyExchangeMessage(self, statusConnection):
        obj = AES.new(self.seansKey, AES.MODE_CFB, self.iv)
        listIV = []
        Message = []
        listMess = []
        listHesh = []
        ExchangeMessage = []
        listIV.append(self.iv)
        listMess.append('3')
        listMess.append(statusConnection)

        Message.append(obj.encrypt(pickle.dumps(listMess, 2)))
        listHesh.append(getHashMD5(Message))

        ExchangeMessage.append(listIV)
        ExchangeMessage.append(Message)
        ExchangeMessage.append(listHesh)

        serverExchangeMessage = pickle.dumps(ExchangeMessage, 2)
        self.sendLine(serverExchangeMessage)

    def sendServerExchangeMessage(self):
        obj = AES.new(self.seansKey, AES.MODE_CFB, self.iv)
        Message = []
        listMess = []

        listHesh = []

        ExchangeMessage = []

        listMess.append('5')
        listMess.append(self.statusAuthorithation)
        Message.append(obj.encrypt(pickle.dumps(listMess, 2)))
        listHesh.append(getHashMD5(Message))

        ExchangeMessage.append(Message)
        ExchangeMessage.append(listHesh)
        serverExchangeMessage = pickle.dumps(ExchangeMessage, 2)
        self.sendLine(serverExchangeMessage)

    def connectionLost(self, reason):
        print 'connectionLost'
        print self.factory.ListOfUsers
        try:
            requests.logOutRequestUpdateUserStatus(self.userLogin)
            self.factory.ListOfUsers.pop(self.userLogin)
        except:
            print '\n.......................Pop error........................'

        try:
            self.factory.clients.remove(self)
        except:
            print '\n.........self.factory.clients.remove(self)  error........'
        print self.factory.ListOfUsers



    def dataReceived(self, line):

        if self.UserLoginStatus :
            clientMessage = self.worker.decryptMessage(line)

            messageForSend =  self.worker.process_message(clientMessage)
            print messageForSend

            print '\nUser %s wants send message' % self.factory.ListOfUsers
            try:
                if self.userLogin == 'admin':
                    self.factory.ListOfUsers['admin'].sendLine(str(messageForSend))
                    print 'User %s  send message\n' % self.userLogin

                if self.userLogin == '2':
                    self.factory.ListOfUsers['2'].sendLine(str(messageForSend))
                    print 'User %s  send message\n' % self.userLogin
            except:
                print 'error admin'


        if self.statusConnection != True :
            #statusConnection = self.statusConnection
            privatkey = RSA.importKey(open('/home/art/Documents/alisaprivatekey.txt').read())
            cipher = PKCS1_OAEP.new(privatkey)
            try:
                print 'try'
                ReceiveMessage = cipher.decrypt(line)
                listMessage = pickle.loads(ReceiveMessage)
                statusDecrypt = True
                self.statusConnection = True
            except:
                print 'except'
                statusConnection = False
                statusDecrypt = False

            print self.statusConnection
            
            if statusDecrypt and self.statusConnection :
                
                heshFromListMessage = getHashMD5(listMessage[0])
                if heshFromListMessage == listMessage[1][0] :
                    self.seansKey = listMessage[0][1]
                    clientKeyExchangeMessage = True
                    statusConnection = True
                else:
                    clientKeyExchangeMessage = False
                    statusConnection = False
            else:
                clientKeyExchangeMessage = False
                self.factory.statusConnection  = False

            if clientKeyExchangeMessage and statusConnection :
                self.sendServerKeyExchangeMessage(statusConnection)

            self.statusConnection = statusConnection

        else:
            self.encripdetConnection = True
        
        if self.encripdetConnection == True and self.statusAuthorithation == False:

            print '\ nelse status True:\n'
            message= pickle.loads(line)
            obj = AES.new(self.seansKey, AES.MODE_CFB, self.iv)
            clientMessage = pickle.loads(obj.decrypt(message[0][0]))
            self.statusAuthorithation = loginActionFromUser(clientMessage[1], getHashMD5(clientMessage[2]))


            if self.statusAuthorithation:
                self.worker = Worker(self.seansKey, self.iv)
                self.userLogin = clientMessage[1]

                self.factory.ListOfUsers[self.userLogin] = self
                print '..............Start list login User.....................'
                print  self.factory.ListOfUsers
                try:
                    print 'login registred user'
                    print  self.factory.ListOfUsers[self.userLogin]
                except:
                    print '.................ERROR...............'

                print '..............End list login User.....................'

            self.sendServerExchangeMessage()
            self.UserLoginStatus = True




class PubFactory(protocol.Factory):
    print 'Start Factory'
    listConnections = []

    def __init__(self):
        self.clients = set()
        self.ListOfUsers = {}


    def buildProtocol(self, addr):
        return PubProtocol(self)

endpoints.serverFromString(reactor, "tcp:8000").listen(PubFactory())
reactor.run()
