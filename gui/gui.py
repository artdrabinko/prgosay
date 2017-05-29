#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

import time
import threading

import searchMessage

sys.path.insert(0,"/home/art/prgosay/actions/")
import action

style_label_active_friend = '''border-style: solid; border-color: #57dc93; border-width: 1px;
                                  background-color: #75ffb3; color: #555452; font-family: Arial;
                                  border-bottom-right-radius: 10px;border-top-right-radius: 10px;
                                  border-bottom-left-radius: 10px;border-top-left-radius: 10px;'''


style_label_no_active_friend =     '''border-style: solid; border-color: #c3bcb1; border-width: 1px;
                                  background-color: #dbd7d1; color: #555452; font-family: Arial;
                                  border-bottom-right-radius: 10px;border-top-right-radius: 10px;
                                  border-bottom-left-radius: 10px;border-top-left-radius: 10px;'''

style_label_active_press_friend =     '''border-style: solid; border-color: #c3bcb1; border-width: 1px;
                                  background-color: #84edb3; color: #61606b; font-family: Arial;
                                  border-bottom-right-radius: 10px;border-top-right-radius: 10px;
                                  border-bottom-left-radius: 10px;border-top-left-radius: 10px;'''

style_label_active_enterEven_friend = '''border-style: solid; border-color: #c3bcb1; border-width: 1px;
                                  background-color: #a3ffcc; color: #61606b; font-family: Arial;
                                  border-bottom-right-radius: 10px;border-top-right-radius: 10px;
                                  border-bottom-left-radius: 10px;border-top-left-radius: 10px;'''






style_label_received_message = '''border-style: solid; border-color: #57dc93; border-width: 1px;
                                  background-color: #75ffb3; color: #555452; font-family: Arial;
                                  border-bottom-right-radius: 10px;border-top-right-radius: 10px;
                                  border-bottom-left-radius: 10px;'''


style_label_send_message =     '''border-style: solid; border-color: #c3bcb1; border-width: 1px;
                                  background-color: #dbd7d1; color: #555452; font-family: Arial;
                                  border-bottom-left-radius: 10px;border-top-right-radius: 10px;
                                  border-top-left-radius: 10px;'''



#STATUSCONNECTIONgui, SEANSKEYgui = False, ''

STATUSCONNECTIONgui, SEANSKEYgui = False, ''

class NikKomarLabel(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        
        
        self.setMouseTracking(True)
        self.setFont(QtGui.QFont("Arial",18))
        self.setStyleSheet(style_label_active_friend)
        
        #self.setStyleSheet("border-color: #404040;border-bottom-right-radius: 15px;border-top-right-radius: 15px;border-bottom-left-radius: 10px;border-style: solid;border-width: 2px;background-color: #f2f1f0;  font-family: Arial; color: rgb(105, 106, 99); ")
        
    def enterEvent(self, event):
        print('enter Event!')
        self.setFont(QtGui.QFont("Arial",18))
        self.setStyleSheet(style_label_active_enterEven_friend)
        #self.setStyleSheet("background-color: #d9e8cb;  font-family: Arial; color: rgb(105, 109, 102); ")
        #self.setText('enter Event!')
    def leaveEvent(self,ev):
        print('leave Event!')
        self.setFont(QtGui.QFont("Arial",18))
        self.setStyleSheet(style_label_active_friend)
        #self.setText('leave Event!')

    def mousePressEvent(self, event):
        #self.setText('Mouse Press')
        self.setStyleSheet(style_label_active_press_friend)
        
    def mouseReleaseEvent(self, event):
        #self.setText('Mouse Drop')
        self.setStyleSheet(style_label_active_enterEven_friend)





    
class TheThreadThatConnectToTheServer(threading.Thread):
    def run(self):
        print' '
        print'................Thread DB on................'
        print 'start ' + time.ctime()
        print' '
        STATUSCONNECTIONgui, SEANSKEYgui, sock = action.estabilishConnection()
        print' '
        print 'stop '  + time.ctime()
        print '...............Thead DB was stoped.............'
        print' '
        return STATUSCONNECTIONgui, SEANSKEYgui
        
	    
def connectToServerStart():
    newThread = TheThreadThatConnectToTheServer()
    newThread.start()
    return True, '......seans key.....'



#STATUSCONNECTIONgui, SEANSKEYgui, sock = action.estabilishConnection()
class loginWindow(QtGui.QWidget):
    
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.STATUSCONNECTIONgui = False        
        
        
        self.pixma = QtGui.QPixmap("connect.png")
        
        mainLayoutm = QtGui.QVBoxLayout()
        
        logoLayoutm = QtGui.QHBoxLayout()
        buttonLayoutm = QtGui.QHBoxLayout()
        mainLayoutm.addLayout(logoLayoutm)
        mainLayoutm.addLayout(buttonLayoutm)
        
        contentLayoutm = QtGui.QVBoxLayout()
        buttonLayoutm.addLayout(contentLayoutm)
        #self.palette = QtGui.QPalette()
        self.setWindowTitle('Welcom to GoSay Client!')
        #self.setStyleSheet("background-color: #37CAA8;")
        self.setAccessibleName('lol')
        self.setWindowIcon(QtGui.QIcon('gosay.png'))
        #self.setStyleSheet("background-color: #9FF4FE; ccolor: #0000ff; ")
        #self.setMaximumSize(265,400)
        #self.setMinimumSize(250,400)
        self.setMaximumSize(600,600)
        self.setMinimumHeight(380)
        #self.setMinimumSize(600,600)
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        #self.logoIcon = QtGui.QLabel('') 
        #self.logoIcon.setMinimumSize(50,50)
        #self.labelNameSelectedFrend = QtGui.QLabel('     Go\n        Say')
        self.labelNameSelectedFrend = QtGui.QLabel('    ')
        self.labelNameSelectedFrend.setFont(QtGui.QFont('Bold', 27))
        self.labelNameSelectedFrend.setMinimumHeight(130)
        self.labelNameSelectedFrend.setMaximumHeight(130)
        self.labelNameSelectedFrend.setMaximumWidth(130)
        self.labelNameSelectedFrend.setStyleSheet("color: rgb(31, 200, 100);")
        #icon = QtGui.QIcon('gosay.png')
        #self.labelNameSelectedFrend.setIcon(icon)
        #self.labelNameSelectedFrend.setIconSize(QtCore.QSize(25,25))
        pixmap = QtGui.QPixmap("gosay.png")
        
        self.labelNameSelectedFrend.setPixmap(pixmap)
        #self.labelNameSelectedFrend.move(qr.topLeft())
        
        self.inputFieldForLoginUser = QtGui.QLineEdit()
        self.inputFieldForLoginUser.setMaximumSize(230,30)
        self.inputFieldForLoginUser.setFont(QtGui.QFont("Arial",11))
        self.inputFieldForLoginUser.setText('Phone or login') 
        self.inputFieldForLoginUser.setStyleSheet("color: rgb(185, 185, 185);")
        self.inputFieldForUserPassword = QtGui.QLineEdit()
        self.inputFieldForUserPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.inputFieldForUserPassword.setMaximumSize(230,30)
        self.inputFieldForUserPassword.setFont(QtGui.QFont("Arial",11))
        self.inputFieldForUserPassword.setText('Password') 
        self.inputFieldForUserPassword.setStyleSheet("color: rgb(130, 130, 130);")
        
        
        self.btnLogin = QtGui.QPushButton("Login")
        #self.btnLogin.setStyleSheet("color: rgb(86, 84, 76);")
        self.btnLogin.setMaximumSize(230,35)
        self.btnLogin.setMinimumSize(230,35)
        
        self.btnTest = QtGui.QPushButton("Test")       
        self.btnTest.setMaximumSize(230,30)
        self.btnTest.setMinimumSize(230,30)
        
        #animation = QtCore.QPropertyAnimation(self.btnTest, "geometry")
        ##animation.setDuration(100000);
        #animation.setStartValue(QtCore.QRect(0, 0, 50, 30));
        #aimation.setEndValue(QtCore.QRect(50, 50, 50, 30));
        
        #pixmap = QtGui.QPixmap('logoIcon.png')
        #self.logoIcon.setPixmap(pixmap)
        #licon = QtGui.QIcon('gosay.png')
        #self.logoIcon.setIcon(licon)
        #self.logoIcon.setIconSize(QtCore.QSize(100,100))
     
        #icon = QtGui.QIcon('gosay.png')
        #self.btnLogin.setIcon(icon)
        #self.btnLogin.setIconSize(QtCore.QSize(25,25))
        #self.printButton.setGeometry(QtCore.QRect(1030, 500, 161, 61))
        
        #mainLayoutm.addWidget(self.logoIcon)
        logoLayoutm.addWidget(self.labelNameSelectedFrend)
        
        contentLayoutm.addWidget(self.inputFieldForLoginUser)
        contentLayoutm.addWidget(self.inputFieldForUserPassword)
        contentLayoutm.addWidget(self.btnLogin)
        contentLayoutm.addWidget(self.btnTest)
        #self.setLayout(logoLayoutm) 
        self.setLayout(mainLayoutm)        
        
        
        
        self.connect(self.btnTest, QtCore.SIGNAL('clicked()'), self.test)
        self.connect(self.btnLogin, QtCore.SIGNAL('clicked()'), self.setVisibleUser)
        #self.connect(self.btnCall, QtCore.SIGNAL('clicked()'), self.set_text_label1)
        #animation.start() 
        #STATUSCONNECTIONgui = False
        if(STATUSCONNECTIONgui == True):
            pixma = QtGui.QPixmap("connect.png")
            self.labelNameSelectedFrend.setPixmap(pixma)
            print 'test lol'
            
        
        
    def test(self):
        if(self.STATUSCONNECTIONgui == False):
            self.STATUSCONNECTIONgui, SEANSKEYgui = connectToServerStart()
        else:
            print '.................block else.....................' 
            if(self.STATUSCONNECTIONgui == True):
                pixma = QtGui.QPixmap("connection_test_true.png")
                self.labelNameSelectedFrend.setPixmap(pixma)
                print 'connection estabilished'
                action.CreateNewThread()
                self.setWindowIcon(QtGui.QIcon('connect.png'))
                self.update()
                action.regestrationAction(self.inputFieldForLoginUser.text(),self.inputFieldForUserPassword.text())
                
                #self.inputFieldForLoginUser.clear
            else:
                pixma = QtGui.QPixmap("connection_test_false.png")
                self.labelNameSelectedFrend.setPixmap(pixma)
                print 'connection not estabilished'
        #STATUSCONNECTIONgu, SEANSKEYgu = ConnectToServerThead()
        #STATUSCONNECTIONgui = STATUSCONNECTIONgu
            
        
    
    def setVisibleUser(self):
        #pixma = QtGui.QPixmap("connect.png")
        self.test()
       #STATUSCONNECTIONgui, SEANSKEYgui, sock = action.estabilishConnection() 
        print 'from gui ' + str(STATUSCONNECTIONgui)
        print 'from gui ' + (SEANSKEYgui)
        mai.show()
        main.setVisible(False)
        print 'was pressed button login'
        #main.close()
        #sock= connServer
        
        



communicationLayout = QtGui.QVBoxLayout()
friendsListLayout = QtGui.QVBoxLayout()


class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        
        self.setWindowTitle('Main window')
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowIcon(QtGui.QIcon('gosay.png'))
        
        #self.ok2.setToolTip('This is a <b>QPushButton</b> widget')
        #self.setStyleSheet("background: #ffffff;")
        
        leftLayout = QtGui.QVBoxLayout() 
        #leftLayout.addStretch(1)
        #leftLayout.addWidget(self.ok1)
        #leftLayout.addWidget(self.label1)
        #leftLayout.addWidget(cancel1)
               
        
        #content for right layout
        selectFrendLayout  = QtGui.QHBoxLayout()
        selectFrendLayoutAction = QtGui.QHBoxLayout()
        selectFrendLayoutName = QtGui.QVBoxLayout()
        
        #first width second hight
        self.btnCall = QtGui.QPushButton("Call")
        self.btnCall.setMaximumSize(50,30)
        self.btnVCall = QtGui.QPushButton("V_Call")
        self.btnVCall.setMaximumSize(60,30)
        self.btnMoreAction = QtGui.QPushButton("...")
        self.btnMoreAction.setMaximumSize(40,30)
        self.labelNameSelectedFrend = NikKomarLabel('Nikolai Komar')
        
        #self.enterEvent(self.labelNameSelectedFrend)
        
        
        
        #self.labelNameSelectedFrend.setVisible(False)
        #self.labelNameSelectedFrend.setFont(QtGui.QFont('Bold', 14))
        #self.labelNameSelectedFrend.setStyleSheet("background-color: #35CAF8; ccolor: #0000ff; font-family: Times;")
        self.labelStatusSelectedFrend = QtGui.QLabel('Online')
        self.labelStatusSelectedFrend.setFont(QtGui.QFont('OldEnglish', 9))
        
        selectFrendLayoutAction.addWidget(self.btnCall)
        selectFrendLayoutAction.addWidget(self.btnVCall)
        selectFrendLayoutAction.addWidget(self.btnMoreAction)
        selectFrendLayoutName.addWidget(self.labelNameSelectedFrend)
        selectFrendLayoutName.addWidget(self.labelStatusSelectedFrend)
        
        selectFrendLayout.addLayout(selectFrendLayoutName)
        selectFrendLayout.addLayout(selectFrendLayoutAction)
        #end content for selectFrendLayout
        
        self.sizepost = 0
        
        #start content communication for right layout
        self.fieldPosts = QtGui.QScrollArea()
        self.fieldPosts.setWidgetResizable(True)
        #self.fieldPosts.setStyleSheet("background-color: #e6e3e0")
        #self.fieldPosts.setStyleSheet('background: #ededed;')
        self.boxlay = QtGui.QVBoxLayout()
        self.boxwid = QtGui.QWidget()
        self.boxwid.setMaximumHeight(self.sizepost)
        self.boxwid.setMinimumHeight(self.sizepost)
        self.boxwid.setLayout(self.boxlay)
        #self.boxwid.setStyleSheet('background: #ededed;')
        self.fieldPosts.setWidget(self.boxwid)
        #self.fieldPosts.setVerticalScrollBar()
        #self.fieldPostsLayout = QtGui.QVBoxLayout()
        #self.fieldPosts.setLayout(self.fieldPostsLayout)
        #self.fieldPosts = QtGui.QTextEdit()
        #self.fieldPosts.append(fieldPostsLayout)
        #lol = action.getConnectStatus()
        #self.fieldPosts.setText('connect to server estabilished')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')
        #self.fieldPosts.append('connect to server estabilished1')

        #self.fieldPosts.append('lol')
        
        
        self.fieldPosts.setMaximumSize(400,700)
        
        #communicationLayout.addStretch(1)
        communicationLayout.addWidget(self.fieldPosts)
        
        #end communication layout
        
        
        #start inputFieldAndSendingLayout
        
        inputFieldAndSendingLayout = QtGui.QHBoxLayout()
        
        self.btnSelectSmile = QtGui.QPushButton("")
        self.btnSelectSmile.setMaximumSize(35,35)
        icons = QtGui.QIcon('smiley_add.png')
        self.btnSelectSmile.setIcon(icons)
        self.btnSelectSmile.setIconSize(QtCore.QSize(23,23))
        self.inputFieldForInputMessage = QtGui.QLineEdit()
        self.inputFieldForInputMessage.setMaximumSize(250,35)
 
        

        #btnSendMessage 'send message'
        self.btnSendMessage = QtGui.QPushButton("")
        self.btnSendMessage.setMaximumSize(35,35)
        icons = QtGui.QIcon('send.png')
        self.btnSendMessage.setIcon(icons)
        self.btnSendMessage.setIconSize(QtCore.QSize(23,23))
        
        
        inputFieldAndSendingLayout.addWidget(self.btnSelectSmile)
        inputFieldAndSendingLayout.addWidget(self.inputFieldForInputMessage)
        inputFieldAndSendingLayout.addWidget(self.btnSendMessage)
        
        #end inputFieldAndSendingLayout
        
        #start friendsList
        
        searchLayout = QtGui.QHBoxLayout()
        searchFrendsListLayout = QtGui.QHBoxLayout()
        
        self.btnSearch = QtGui.QPushButton()
        self.btnSearch.setMaximumSize(35,35)
        self.btnSearch.setMinimumSize(35,35)
        icon = QtGui.QIcon('search.png')
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QtCore.QSize(25,25))
        
        self.inputFieldForSearch = QtGui.QLineEdit()
        self.inputFieldForSearch.setMaximumSize(210,35)

        
        #self.inputFieldForSearch.setEchoMode(QtGui.QLineEdit.Password)        
        self.inputFieldForSearch.setMaxLength(10)
        self.inputFieldForSearch.setFont(QtGui.QFont("Arial",14))
        
        
        self.labelListLayoutFrends = QtGui.QLabel('Friends:')
        self.labelListLayoutFrends.move(0,0)

        self.btnFriend = QtGui.QPushButton("Frend")
        #self.btnFriend.setMaximumSize(200,50)
        
        searchLayout.addWidget(self.btnSearch)
        searchLayout.addWidget(self.inputFieldForSearch)
        searchFrendsListLayout.addWidget(self.labelListLayoutFrends)
        
        
        self.emptyLabel = QtGui.QLabel('empty')
        self.emptyLabel.setMinimumSize(10,10)
        friendsListLayout.addWidget(self.emptyLabel)
        #end friendsList
        
        #leftLayout.setStyleSheet("background: #fffff;")
        leftLayout.addLayout(searchLayout)
        leftLayout.addLayout(searchFrendsListLayout)
        leftLayout.addLayout(friendsListLayout)
        
              
        rightLayout = QtGui.QVBoxLayout()   
        
        #rightLayout.addStretch(1)   
        rightLayout.addLayout(selectFrendLayout)
        rightLayout.addLayout(communicationLayout) 
        rightLayout.addLayout(inputFieldAndSendingLayout)

        #rightLayout.setMargin(30)
        #self.setStyleSheet("QWidget {background-color: #F2F2F2 }")
    
        mainLayout = QtGui.QHBoxLayout() 
        #mainLayout.addStretch(1)
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        #mainLayout.setMargin(10)
        
        self.setLayout(mainLayout)
        self.setMinimumSize(700,600)
        #self.setMinimumSize(250,400)
        self.setMaximumSize(700,700)
        #self.setWindowOpacity(0.98)
        #self.resize(265,400)
        #self.sizepost = 0
        
        #self.connect(self.labelNameSelectedFrend, QtCore.SIGNAL('clicked()'), self.enterLabel)
        
        
        
        
        self.connect(self.btnSendMessage, QtCore.SIGNAL('clicked()'), self.SendMessageAction)
        #self.connect(self.ok2, QtCore.SIGNAL('clicked()'), self.set_text_label2)
        self.connect(self.btnSearch, QtCore.SIGNAL('clicked()'), self.searchUserInDB)
        #self.connect(self.btnCall, QtCore.SIGNAL('clicked()'), self.set_text_label1)        
        
    def closeEvent(self, event):
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                main.setVisible(True)
                main.close()
                #sock.close()
                #time.sleep(3)
                
                
            else:
                event.ignore()
    #def enterEvent(self,ev):
        #self.labelNameSelectedFrend.setText('enter')
        #self.labelNameSelectedFrend.update()
       # print 'label enter'
        #return QtGui.QWidget.enterEvent(self.labelNameSelectedFrend,ev)  
   # def leaveEvent(self,ev):
      #  self.labelNameSelectedFrend.setText('leave')
        #self.labelNameSelectedFrend.update()
        
        #print 'label leave'
        #return QtGui.QWidget.enterEvent(self.labelNameSelectedFrend,ev)          
            
            
    def closeAction(self):
        print 'close'
    
    def SendMessageAction(self):
        message = str(self.inputFieldForInputMessage.text())
        
        #try:
           # message = int(message)
            #print 'int'
        #except:
            #message = str(message)
            #print 'str'
       #print type(message)
        #fieldPostsLayout = QtGui.QVBoxLayout()
        #self.fieldPosts.setLayout(fieldPostsLayout)
        emptyLabe1 = QtGui.QLabel('')
        
        #emptyLabe1.setStyleSheet("background-color: #fcfbf9")
        #emptyLabe1.setFont(QtGui.QFont("Arial",14))
        #emptyLabe1.setStyleSheet("background-color: #fcfbf9;color: #fcfbdd; ")
        #emptyLabe1.setStyleSheet("background-color: #fcfbf9")
        emptyLabe1.setText('   Test Message\n    Hello World: ' + str(self.sizepost))
        emptyLabe1.setStyleSheet(style_label_received_message)
        emptyLabe1.setMinimumSize(40,40)
        emptyLabe1.move(0,0)
        
        self.boxlay.addWidget(emptyLabe1)
        self.sizepost = self.sizepost + 40
        self.boxwid.setMinimumHeight(self.sizepost)
        self.boxwid.setMaximumWidth(350)
        self.boxwid.setMinimumWidth(359)
        
        emptyLabe2 = QtGui.QLabel('')
        emptyLabe2.setMinimumSize(20,20)
        self.boxlay.addWidget(emptyLabe2)
        self.sizepost = self.sizepost + 20
        self.boxwid.setMinimumHeight(self.sizepost)
        
        
        emptyLabe = QtGui.QLabel('')
        emptyLabe.setText('                  My answer: ' + str(self.inputFieldForInputMessage.text()))
        emptyLabe.setStyleSheet(style_label_send_message)
        #emptyLabe.setStyleSheet("color: rgb(31, 200, 100);")
        #emptyLabe.setStyleSheet("border: 2px solid green;border-radius: 10px;")

        emptyLabe.setMinimumSize(40,40)
        #emptyLabe.move(0,0)
        self.inputFieldForInputMessage.clear()
        self.boxlay.addWidget(emptyLabe)
        self.sizepost = self.sizepost + 40
        self.boxwid.setMinimumHeight(self.sizepost)
        self.boxwid.setMaximumWidth(100)
        
        emptyLabe3 = QtGui.QLabel('')
        emptyLabe3.setMinimumSize(20,20)
        self.boxlay.addWidget(emptyLabe3)
        self.sizepost = self.sizepost + 20
        self.boxwid.setMinimumHeight(self.sizepost)        
                
        
        #self.fieldPosts.setWidget(emptyLabe)
        #fieldPostsLayout.addWidget(emptyLabe)
        #sock.send(str(message))
        print 'tyt 430'
        if(message == '') or not message:
            message = 'no data'
        action.sendMess(message)
        

    
    def set_text_label2(self):
        self.label1.setVisible(True)
        
    def searchUserInDB(self):   
        
        while friendsListLayout.count():
            child = friendsListLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        

        textFromInputSearch = self.inputFieldForSearch.text()
        self.inputFieldForSearch.clear()
        print textFromInputSearch
        
        firstname = searchMessage.searchUserByNameOrLogin(textFromInputSearch)     
        print firstname
        
        if firstname != 'There is no such user':
            self.btnFriend = QtGui.QPushButton("Friend")
            friendsListLayout.addWidget(self.btnFriend)
            self.btnFriend.setText(str(firstname[3]) + ' ' + str(firstname[4]) )
            self.btnFriend.setFont(QtGui.QFont('Bold', 12))
            self.labelListLayoutFrends.setText('Users list: ')
            self.labelStatusSelectedFrend.setText(str(firstname[0]) + ' ' + str(firstname[1]))
            
        else:
            self.labelListLayoutFrends.setText('Users with this name\nthere is no(')
            print 'no users'
        
        
#app = QtGui.QApplication(sys.argv)
        
        
app = QtGui.QApplication(sys.argv)
main = loginWindow()

mai = MainWindow()

main.show() 
             

sys.exit(app.exec_())
