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



class Worker:
    def __init__(self, key, iv, login):
        self.secretInformationAboutFriend = []
        self.key = key
        self.iv = iv
        self.chiper = AESCipher(self.key, self.iv)
        self.userLogin = str(login)

    def getHashMD5(self, text):
        hash_md5 = hashlib.md5()
        hash_md5.update(str(text))
        return hash_md5.hexdigest()

    def decryptMessage(self, data):
        clientMessage = pickle.loads(data)
        decoded = self.chiper.decrypt(clientMessage[0][0])
        decryptedMessage = pickle.loads(decoded)
        print str(decryptedMessage) + '.......decr message........'
        return decryptedMessage

    def encryptMessage(self, message):
        ExchangeMessage = []
        encryptMessage = []
        listMess = message[:]
        listHash = []
        encoded = self.chiper.encrypt(pickle.dumps(listMess, 2))

        encryptMessage.append(encoded)
        listHash.append(self.getHashMD5(encryptMessage[0]))

        ExchangeMessage.append(encryptMessage)
        ExchangeMessage.append(listHash)

        encryptedAndDumpMessage = pickle.dumps(ExchangeMessage, 2)
        return encryptedAndDumpMessage

    def process_message(self, argument):
        method_name = 'number_' + str(argument[0])
        method = getattr(self, method_name, lambda: "nothing")
        return method(argument)

    def number_8(self, argument):
        respond, status  = requests.searchAllUsersWithName(argument[1])

        print status
        answer = {}

        if status:
            for res in respond:
                answer[res[0]] = res
        else:
            answer = False
        listMess = []
        listMess.append('9')
        listMess.append(answer)
        print listMess
        messageForSend = self.encryptMessage(listMess)
        return self.userLogin, messageForSend

    def number_10(self, argument):
        #add! pull in DB
        listMess = []
        listMess.append('11')
        listMess.append(argument[1])
        listMess.append(argument[2])
        listMess.append(argument[3])
        destination = argument[2]
        print listMess


        statusForSend = argument[2] in self.secretInformationAboutFriend
        if statusForSend == True:
            ExchangeMessage = []
            encryptMessage = []
            listHash = []

            information = self.secretInformationAboutFriend[argument[2]]
            print information
            chiper = AESCipher(information[0], information[1])
            encoded = chiper.encrypt(pickle.dumps(listMess, 2))

            encryptMessage.append(encoded)
            listHash.append(self.getHashMD5(encryptMessage[0]))

            ExchangeMessage.append(encryptMessage)
            ExchangeMessage.append(listHash)

            encryptedAndDumpMessage = pickle.dumps(ExchangeMessage, 2)
        else:
            print 'error'
            destination = argument[1]
            listMess[3] = 'user Offline!'
            encryptedAndDumpMessage = self.encryptMessage(listMess)

        return destination, encryptedAndDumpMessage



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
        del self.factory.secretUsersInformation[self.userLogin]
        try:
            del self.factory.secretUsersInformation[self.userLogin]
            self.factory.clients.remove(self)
        except:
            print '\n.........self.factory.clients.remove(self)  error........',self.factory.secretUsersInformation
        print self.factory.ListOfUsers



    def dataReceived(self, line):

        if self.UserLoginStatus :
            clientMessage = self.worker.decryptMessage(line)

            destination ,messageForSend =  self.worker.process_message(clientMessage)
            print messageForSend

            statusForSend = destination in self.factory.ListOfUsers
            if statusForSend == True:
                print '\nUser %s wants send message' % self.userLogin
                print '\nUsery %s ' % destination
                self.factory.ListOfUsers[destination].sendLine(str(messageForSend))
                print 'User %s  send message\n' % self.userLogin
            else:
                print 'no such user or this user offline.'




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
                self.userLogin = clientMessage[1]
                self.worker = Worker(self.seansKey, self.iv, self.userLogin)

                print clientMessage[0]

                self.factory.ListOfUsers[self.userLogin] = self
                listSecretInformation = []
                listSecretInformation.append(self.seansKey)
                listSecretInformation.append(self.iv)
                self.factory.secretUsersInformation[self.userLogin] = listSecretInformation
                self.worker.secretInformationAboutFriend = self.factory.secretUsersInformation
                del listSecretInformation
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
        self.secretUsersInformation = {}


    def buildProtocol(self, addr):
        return PubProtocol(self)

endpoints.serverFromString(reactor, "tcp:8000").listen(PubFactory())
reactor.run()
