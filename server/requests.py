import mysql.connector
from mysql.connector import Error
import threading
import time
#DATA = ''
#DATALOGIN = ''
#DATANAME = ''
def connect():
    #""" Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='testDB',
                                       user='root',
                                       password='09081994art')

        if conn.is_connected():
            print('connection to MySQL database estabilished')
            e = ''
    except Error as e:
        print(e)
    
    return conn



def searchAllUsersWithName(Name):
    connDB = connect()
    print  Name
    requestSearchByName = 'select uid, login, firstname, lastname, age, status_conn from users where firstname = \"' + Name + '\"'
    a = connDB.cursor()
    a.execute(requestSearchByName)

    responseSearchByName = a.fetchall()

    if responseSearchByName != []:
        print responseSearchByName
        #responseSearchByName = responseSearchByName[0]
        connDB.close()

        return responseSearchByName, True
    else:
        #print 'There is no such user'
        connDB.close()

        return 'There is no such user with Name', False

















def searchByName(name):
    connDB = connect()
    
    requestSearchByName = 'select * from users where firstname = \"' + name + '\"'
    a = connDB.cursor()
    a.execute(requestSearchByName)
    
    responseSearchByName = a.fetchall()
    
    if (responseSearchByName != []):
        print responseSearchByName
        responseSearchByName = responseSearchByName[0]
        #print responseSearchByName[3] + ' ' + responseSearchByName[4]
        connDB.close()
        #print('connection to MySQL database close!')
        return responseSearchByName, False
    else:
        #print 'There is no such user' 
        connDB.close()
        #print('connection to MySQL database close!')
        return 'There is no such user with Name', True
    


def searchByLogin(login):
    connDB = connect()
    
    requestSearchByLogin = 'select * from users where login = \"' + str(login) + '\"'
    a = connDB.cursor()
    a.execute(requestSearchByLogin)
    
    responseSearchByLogin = a.fetchall()
    print str(responseSearchByLogin)
    
    if (responseSearchByLogin != []):
        responseSearchByLogin = responseSearchByLogin[0]
        #print responseSearchByLogin[3] + ' ' + responseSearchByLogin[4]
        connDB.close()
        #print('connection to MySQL database close!')
        return responseSearchByLogin, False
    else:
        #print 'There is no such user' 
        connDB.close()
        #print('connection to MySQL database close!')
        return 'There is no such user whith login', True


# noinspection PyBroadException
def searchUserByNameOrLogin(DATA):
    try:
        DATA = int(DATA)
        print 'int'
        return searchByLogin(DATA)
    except:
        DATA = str(DATA)
        print 'str'
        return searchByName(DATA)




def logInRequestUpdateUserStatus(login):
    print 'logInRequestUpdateUserStatus in DB'
    connDB = connect()
    request = 'update users set status_conn = \"Online\" where login = \"' + str(login) + '\"'
    a = connDB.cursor()
    print request
    a.execute(request)
    connDB.commit()
    connDB.close()  

def logOutRequestUpdateUserStatus(login):
    print 'logOutRequestUpdateStatus in DB'
    connDB = connect()
    request = 'update users set status_conn = \"Offline\" where login = \"' + str(login) + '\"'
    a = connDB.cursor()
    print request
    a.execute(request)
    connDB.commit()
    connDB.close()  



def searchUserByLoginAndCheckPassword(login, heshFromPassword):
    connDB = connect()
    requestSearchByLogin = 'select login, password from users where login = \"' + str(login) + '\"'
    print '\n' + requestSearchByLogin + '\n'
    a = connDB.cursor()
    a.execute(requestSearchByLogin)
    responseSearchByLogin = a.fetchall()
    print str(responseSearchByLogin)

    if (responseSearchByLogin != []):
        if(heshFromPassword == responseSearchByLogin[0][1]):
            statusLogin = True
            connDB.close()
            logInRequestUpdateUserStatus(login)
        else: 
            statusLogin = False
            connDB.close()
            print 'else'
    else:
        connDB.close()
        print 'There is no such user with login'
        statusLogin = False

    return statusLogin
































def registrationUserRequest(DATA):
    print 'registrationUserRequest to DB'
    connDB = connect()
    reqistrationRequest = 'update users set login = \"' +str(DATA) +'\" where uid = 3' 
    a = connDB.cursor()
    a.execute(reqistrationRequest)
    connDB.commit()
    connDB.close()   




def searchConnectionByLogin(login):
    connDB = connect()

    requestSearchByLogin = 'select conn from users where login = \"' + str(login) + '\"'
    a = connDB.cursor()
    a.execute(requestSearchByLogin)
    responseSearchConnectionByLogin = a.fetchall()
    print responseSearchConnectionByLogin

    connDB.close()
    return responseSearchConnectionByLogin[0][0]









class ThreadDB(threading.Thread):
    def run(self):
        count = 0
        print'............ThreadDB on................'
        while (True):
            print time.ctime()
            time.sleep(0.1)
            count = count + 1
            if (count == 1): break
            # print 'thread was stop.............'

def StartThreadSearchDB():
    newThread = ThreadDB()
    newThread.start()



