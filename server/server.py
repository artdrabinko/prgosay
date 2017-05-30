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


import time
import hashlib

from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic

import sys
sys.path.insert(0,"/home/art/PycharmProjects/prgosay/server/requests")
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



class PubProtocol(basic.LineReceiver):
    
    def __init__(self, factory):
        self.factory = factory
        self.userLogin = ''
        self.recmessok = False
        self.cl = ''
        self.statusConnection = False
        self.encripdetConnection = False
        self.statusAuthorithation = False
        self.seansKey = ''
        self.iv = Random.new().read(16) # 128 bit
        #self.conn = ''

   
    def connectionMade(self):
        #listConnections.append()
        self.factory.clients.add(self)
        self.conn = self.transport.getPeer()
        #print self.conn
        for client in  self.factory.clients:
            #print client
            self.cl = client
            #break
        #print self.cl
        #self.factory.numConnections += 1
        f = open('/home/art/Documents/alisapublickey.txt','rb')
        publicKey = f.read(); f.close()

        self.listMess = []
        self.listHesh = []
        
        self.listMess.append('1')
        self.listMess.append(publicKey)
        self.listMess.append('gosay.net.ru')
        self.listMess.append('md5')

        self.listHesh.append(getHashMD5(self.listMess))
        
        self.factory.ServerCerificateMessage.append(self.listMess)
        self.factory.ServerCerificateMessage.append(self.listHesh)
        #print self.factory.ServerCerificateMessage
        bytesForSend = pickle.dumps(self.factory.ServerCerificateMessage,2)

        self.transport.write(bytesForSend)
        self.factory.ServerCerificateMessage[:] = []

    def connectionLost(self, reason):
        print 'connectionLost'
        try:
            self.factory.listUser.pop(self.userLogin)
            #del self.factory.listUser[self.userLogin]

        except:
            print '\nerror pop....................'
        requests.logOutRequestUpdateUserStatus(self.userLogin)


        self.factory.clients.remove(self)

       
    def dataReceived(self, line):
        if (self.recmessok):
            print line
            #conn = searchActionUserByLoginInDB('admin')
            #conn.sendLine('heeeeeeeeeeeeeeeeeeeeeeeeeeeee')
            print '\nUser %s wants send message' % self.userLogin
            try:
                if(self.userLogin == 'admin'):
                    self.factory.listUser['2'].sendLine(line)
                    print 'User %s  send message\n' % self.userLogin
                if (self.userLogin == '2'):
                    self.factory.listUser['admin'].sendLine(line)
                    print 'User %s  send message\n' % self.userLogin
            except:
                print 'error admin'



        if(self.statusConnection != True):
            #statusConnection = self.statusConnection
            privatkey = RSA.importKey(open('/home/art/Documents/alisaprivatekey.txt').read())
            cipher = PKCS1_OAEP.new(privatkey)
            try:
                print 'try'
                ReceiveMessage = cipher.decrypt(line)
                listMessage = messageProcessing(ReceiveMessage)
                statusDecrypt = True
                statusConnection = True
            except:
                print 'except'
                statusConnection = False 
            print statusConnection
            
            if(statusDecrypt and statusConnection):
                
                heshFromListMessage = getHashMD5(listMessage[0])
                if(heshFromListMessage == listMessage[1][0]):
                    self.seansKey = listMessage[0][1]
                    clientKeyExchangeMessage = True
                    statusConnection = True
                else:
                    clientKeyExchangeMessage = False
                    statusConnection = False
            else:
                clientKeyExchangeMessage = False
                self.factory.statusConnection  = False
            if(clientKeyExchangeMessage and statusConnection):
                obj = AES.new(self.seansKey, AES.MODE_CFB, self.iv)
                listIV = []
                Message = []
                listMess = []                
                listHesh = []
                ExchangeMessage = []
                listIV.append(self.iv)
                listMess.append('3')
                listMess.append(statusConnection)
                
                Message.append(obj.encrypt(pickle.dumps(listMess,2)))
                listHesh.append(getHashMD5(Message))
                
                ExchangeMessage.append(listIV)
                ExchangeMessage.append(Message)
                ExchangeMessage.append(listHesh)
                
                serverExchangeMessage = pickle.dumps(ExchangeMessage,2)
                self.sendLine(serverExchangeMessage)
        
            #print clientKeyExchangeMessage
            #print statusConnection
            self.statusConnection = statusConnection

        else:
            self.encripdetConnection = True
        
        if(self.encripdetConnection == True and self.statusAuthorithation == False):
            print '\ nelse status True:\n'
            message= pickle.loads(line)
            obj = AES.new(self.seansKey, AES.MODE_CFB, self.iv)
            clientMessage = pickle.loads(obj.decrypt(message[0][0]))

            self.statusAuthorithation = loginActionFromUser(clientMessage[1], getHashMD5(clientMessage[2]))

            if(self.statusAuthorithation):
                self.userLogin = clientMessage[1]

                self.factory.listUser[self.userLogin] = self.cl
                print '..............Start list login User.....................'
                print  self.factory.listUser
                try:
                    print 'login registred user'
                    print  self.factory.listUser[self.userLogin]
                except:
                    print 'error admin'

                print '..............End list login User.....................'
            obj = AES.new(self.seansKey, AES.MODE_CFB, self.iv)
            Message = []
            listMess = []
            
            listHesh = []
            
            ExchangeMessage = []
            
            listMess.append('5')
            listMess.append(self.statusAuthorithation)
            #print listMess
            Message.append(obj.encrypt(pickle.dumps(listMess,2)))
            listHesh.append(getHashMD5(Message))
            
            ExchangeMessage.append(Message)
            ExchangeMessage.append(listHesh)
            #print ExchangeMessage
            serverExchangeMessage = pickle.dumps(ExchangeMessage,2)
            self.sendLine(serverExchangeMessage)

            for client in self.factory.clients:
                if(client == self.cl):
                    print  client
                    print  self.cl
                    print 'sovpalo'
                    #client.sendLine('sovpalo')
                else:
                    print '\n' + str(client)
                    print  self.cl
                    print 'nesovpalo'
                    #self.sendLine('eeeeeeeeeees!')
            self.recmessok = True



class PubFactory(protocol.Factory):
    print '........User......'
    listConnections = []    
    ServerCerificateMessage = []
    ServerCerificateMessage[:] = []
    listUser = {}

    def __init__(self):
        print '......new connection....'
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)


endpoints.serverFromString(reactor, "tcp:8000").listen(PubFactory())
reactor.run()
