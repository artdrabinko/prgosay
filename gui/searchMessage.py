import mysql.connector
from mysql.connector import Error
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



def searchByLogin(DATALOGIN):
    connDB = connect()
    
    requestSearchByLogin = 'select * from users where login = \"' + str(DATALOGIN) + '\"' 
    a = connDB.cursor()
    a.execute(requestSearchByLogin)
    
    responseSearchByLogin = a.fetchall()
    print str(responseSearchByLogin)
    
    if (responseSearchByLogin != []):
        responseSearchByLogin = responseSearchByLogin[0]
        #print responseSearchByLogin[3] + ' ' + responseSearchByLogin[4]
        connDB.close()
        #print('connection to MySQL database close!')
        return responseSearchByLogin
    else:
        #print 'There is no such user' 
        connDB.close()
        #print('connection to MySQL database close!')
        return 'There is no such user'

def searchByName(DATANAME):
    connDB = connect()
    
    requestSearchByName = 'select * from users where firstname = \"' + DATANAME + '\"'
    a = connDB.cursor()
    a.execute(requestSearchByName)
    
    responseSearchByName = a.fetchall()
    
    if (responseSearchByName != []):
        print responseSearchByName
        responseSearchByName = responseSearchByName[0]
        #print responseSearchByName[3] + ' ' + responseSearchByName[4]
        connDB.close()
        #print('connection to MySQL database close!')
        return responseSearchByName
    else:
        #print 'There is no such user' 
        connDB.close()
        #print('connection to MySQL database close!')
        return 'There is no such user'
    


def searchUserByNameOrLogin(DATA):
    try:
        DATA = int(DATA)
        print 'int'
        return searchByLogin(DATA)
    except:
        DATA = str(DATA)
        print 'str'
        return searchByName(DATA)





#while(True):
  #  data = raw_input()
  #  data = searchUserByNameOrLogin(data)
  #  print data[6]
    
    
    
    
    
    