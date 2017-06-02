# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore, Qt
import time
import threading
from time import strftime
from PyQt4.QtGui import QCursor

sys.path.insert(0, "/home/art/PycharmProjects/prgosay/actions/")
import action
import datetime
#from simple_thread import SimpleThread



class QTheThreadThatConnectToTheServer(threading.Thread):
    def run(self):
        print' '
        print'................Thread DB on................'
        time.sleep(2)
        print 'start ' + time.ctime()
        print' '
        stat = action.estabilishConnection()
        print stat
        print' '
        print 'stop ' + time.ctime()
        time.sleep(2)
        print '...............Thead DB was stoped.............'
        print' '
        return stat


def QconnectToServerStart():
    newThread = QTheThreadThatConnectToTheServer()
    newThread.start()
    # return True, '......seans key.....'
    return 'Connect !'


def connectToServerStart():
    print' '
    print'................Thread DB on................'
    time.sleep(0.5)
    print 'start ' + time.ctime()
    print' '
    stat = action.estabilishConnection()
    print stat
    print' '
    print 'stop ' + time.ctime()
    time.sleep(0.5)
    print '...............Thead DB was stoped.............'
    print' '
    return stat


class VLayout(QtGui.QVBoxLayout):
    def __init__(self, parent=None):
        QtGui.QVBoxLayout.__init__(self, parent)
        self.setMargin(0)
        self.setSpacing(0)


class HLayout(QtGui.QHBoxLayout):
    def __init__(self, parent=None):
        QtGui.QHBoxLayout.__init__(self, parent)
        self.setMargin(0)
        self.setSpacing(0)


class EmptyBoxWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMinimumSize(450, 65)
        self.setMaximumSize(450, 65)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('color: #ffffff; border: none;')



class ButtonBackRegistrationWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(40, 40)
        self.setMinimumSize(40, 40)
        icon = QtGui.QIcon('back_button.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(30, 40))
        self.setStyleSheet('background: #5181b8;')

    def mousePressEvent(self, event):
        icons = QtGui.QIcon('button_back_hover.png')
        self.setIcon(icons)
        self.setIconSize(QtCore.QSize(40, 40))
        self.setStyleSheet('background: #5181b8;')
        print'press 1'

    def mouseReleaseEvent(self, event):
        icons = QtGui.QIcon('button_back_hover.png')
        self.setIcon(icons)
        self.setIconSize(QtCore.QSize(45, 45))
        self.setStyleSheet('background: #5181b8;')

    def enterEvent(self, event):
        # self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        icons = QtGui.QIcon('button_back_hover.png')
        self.setIcon(icons)
        self.setIconSize(QtCore.QSize(45, 45))
        self.setStyleSheet('background: #5181b8;')
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # print 'enterEvent press'

    def leaveEvent(self, event):
        icon = QtGui.QIcon('back_button.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(30, 40))
        self.setStyleSheet('background: #5181b8;')
        # self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')



class ButtonAttachFile(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(46, 46)
        self.setMinimumSize(46, 46)
        self.setStyleSheet('border: none;margin: 0px 0px 0px 0px;  background-image: url(./img/button_attach_in.png); background-repeat: no-repeat ;')

    def mousePressEvent(self, event):
        self.setStyleSheet('border: none;margin: 0px 10px 0px 0px; background-image: url(./img/button_attach_in.png); background-repeat: no-repeat ;')

    def mouseReleaseEvent(self, event):
        self.setStyleSheet('border: none;margin: 0px 10px 0px 0px; background-image: url(./img/button_attach_in.png); background-repeat: no-repeat ;')

    def enterEvent(self, event):
        self.setStyleSheet('border: none;margin: 0px 10px 0px 0px; background-image: url(./img/button_attach_in.png); background-repeat: no-repeat ;')
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def leaveEvent(self, event):
        self.setStyleSheet('border: none; margin: 0px 10px 0px 0px; background-image: url(./img/button_attach_in.png); background-repeat: no-repeat ;')






class ButtonSendMessage(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(46, 46)
        self.setMinimumSize(46, 46)
        self.setStyleSheet('border: none;margin: 0px 10px 0px 0px;  background-image: url(./img/button_send_out.png); background-repeat: no-repeat ;')

    def mousePressEvent(self, event):
        self.setStyleSheet('border: none;margin: 0px 5px 0px 0px; background-image: url(./img/button_send_in.png); background-repeat: no-repeat ;')

    def mouseReleaseEvent(self, event):
        self.setStyleSheet('border: none;margin: 0px 10px 0px 0px; background-image: url(./img/button_send_in.png); background-repeat: no-repeat ;')

    def enterEvent(self, event):
        self.setStyleSheet('border: none;margin: 0px 10px 0px 0px; background-image: url(./img/button_send_in.png); background-repeat: no-repeat ;')
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def leaveEvent(self, event):
        self.setStyleSheet('border: none; margin: 0px 10px 0px 0px; background-image: url(./img/button_send_out.png); background-repeat: no-repeat ;')


class ButtonMenuWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(52, 53)
        self.setMinimumSize(52, 53)
        icon = QtGui.QIcon('menu.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 40))
        self.setStyleSheet('background: #ffffff; border:none;')

    def mousePressEvent(self, event):
        icon = QtGui.QIcon('menu.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 40))
        self.setStyleSheet('background: #ffffff; border:none;')
        self.setFocusPolicy(False)
        print'press 1'

    def mouseReleaseEvent(self, event):
        icon = QtGui.QIcon('menu_hover.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 40))
        self.setStyleSheet('background: #ffffff; border:none;')

    def enterEvent(self, event):
        # self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        icon = QtGui.QIcon('menu_hover.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 45))
        self.setStyleSheet('background: #ffffff; border:none;')
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # print 'enterEvent press'

    def leaveEvent(self, event):
        icon = QtGui.QIcon('menu.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 40))
        self.setStyleSheet('background: #ffffff; border:none;')
        # self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')








class inputSearchWidget(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMinimumSize(290, 33)
        self.setMaximumSize(340, 33)
        self.setStyleSheet('background-color: #f1f1f3; font-size: 14px;'
                           ' padding-left: 10px; margin-right: 50px; color: #b4a3b3;'
                           ' border: none; border-radius: 3.5px;')
        self.setText('Search')
        # self.setCursorPosition(0)
        # self.setFocusPolicy(True)
        # def mousePressEvent(self, event):
        # self.clear()
        # print 'mouse press'

    def focusOutEvent(self, event):
        if (len(self.text()) == 0):
            self.setStyleSheet('background-color: #f1f1f3; font-size: 14px;'
                               ' padding-left: 10px; color: #b4a3b3; margin-right: 50px;'
                               ' border: none; border-radius: 3.5px;')
            self.setText('Search')
            self.setCursorPosition(0)
        else:
            self.setStyleSheet('background-color: #ffffff; font-size: 14px;'
                               ' padding-left: 10px; color: #7C849D; margin-right: 50px;'
                               ' border: none;  border-radius: 3.5px; border: 1.6px  solid #54C3F2;')

    def focusInEvent(self, event):
        if (self.text() == 'Search'):
            self.clear()
        self.setStyleSheet('background-color: #ffffff; font-size: 14px;'
                           ' padding-left: 10px; color: #3A3131; margin-right: 50px;'
                           ' border: none;  border-radius: 3.5px; border: 1.6px  solid #54C3F2;')


class inputSendMessageWidget(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMinimumSize(60, 48)
        self.setMaximumHeight(48)
        self.setStyleSheet('margin: 0px 10px 0px 10px; background-color: #ffffff;'
                           ' font-size: 16px; padding-left: 10px; color: #b4a3b3;'
                           ' border: 1px solid #E0E0E0; border-radius: 4px;')
        self.setText('Write a message...')

    def mousePressEvent(self, event):
        self.setStyleSheet('margin: 1px 10px 1px 10px;background-color: #ffffff;'
                           ' font-size: 16px; padding-left: 10px; color: #3A3131;'
                           ' border: 1px solid #B3E08E;  border-radius: 4px;')

    def focusOutEvent(self, event):
        if (len(self.text()) == 0):
            self.setStyleSheet('margin: 1px 10px 1px 10px; background-color: #ffffff; '
                               'font-size: 16px; padding-left: 10px; color: #b4a3b3; '
                               ' border: 1px solid #E0E0E0; border-radius: 4px;')
            self.setText('Write a message...')
            self.setCursorPosition(0)
        else:
            self.setStyleSheet(
                            'margin: 1px 10px 1px 10px; background-color: #ffffff; '
                            'font-size: 16px;'
                            'padding-left: 10px; color: #3A3131; border: 1px solid #E0E0E0;'
                            ' border-radius: 4px;')

    def focusInEvent(self, event):
        if (self.text() == 'Write a message...'):
            self.clear()
        self.setStyleSheet('margin: 1px 10px 1px 10px;background-color: #ffffff;'
                           ' font-size: 16px; padding-left: 10px; color: #3A3131;'
                           ' border: 1px solid #B3E08E;  border-radius: 4px;')


class HeaderRegistrationWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMinimumSize(270, 40)
        self.setMaximumSize(270, 40)
        self.setStyleSheet('background: #5181b8; border: none;')

        LayoutH = QtGui.QHBoxLayout()
        self.setLayout(LayoutH)

        # self.buttonBack.setStyleSheet('margin-bottom: 20px;')
        self.buttonBack = ButtonBackRegistrationWidget()
        self.registrationLabel = QtGui.QLabel('Registration:')
        self.registrationLabel.setMaximumSize(240, 30)
        self.registrationLabel.setMinimumSize(240, 30)
        self.registrationLabel.setStyleSheet('padding-top:1px;border: none;font: Arial; '
                                             'font-size: 18px; background: #5181b8;'
                                             'color: #ffffff;')

        LayoutH.addWidget(self.buttonBack)
        LayoutH.addWidget(self.registrationLabel)


class ThreadDB(threading.Thread):
    def run(self):
        cout = 0
        print'............Thread was active................'
        while (True):
            print time.ctime()
            # time.sleep(2)
            cout = cout + 1
            if (cout == 2): break
        print '...........Thread was stoped...............'


class logoLabelWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMaximumSize(165, 70)
        self.setMinimumSize(165, 70)
        self.setText("GoSay")
        self.setStyleSheet('border: none; background-color: #5181b8; color : #edf2f8;'
                           ' font: bold  Arial; font-size: 53px;')


class logoWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMaximumSize(290, 120)
        self.setMinimumSize(250, 120)
        self.setStyleSheet('border: none; background-color: #5181b8;')
        logoLayout = HLayout()
        self.setLayout(logoLayout)
        self.logoLabel = logoLabelWidget()
        logoLayout.addWidget(self.logoLabel)


class inputLineLogin(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMaximumSize(250, 30)
        self.setMinimumSize(250, 30)
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px;'
                           ' border: none; border-bottom: 1px solid #7ca0ca;')
        self.setText('Login or phone')

    def focusOutEvent(self, event):
        if (len(self.text()) == 0 or 'Login or phone' == self.text()):
            self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; '
                               'margin : 0px;border: none; border-bottom: 1px solid #7ca0ca;')
            self.setText('Login or phone')

    def focusInEvent(self, event):
        if (len(self.text()) == 0 or 'Login or phone' == self.text()):
            self.clear()
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; '
                           'margin : 0px; border: none; border-bottom: 1.6px  solid #edf2f8;')


class inputLinePassword(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMaximumSize(250, 40)
        self.setMinimumSize(250, 40)
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc;'
                           ' border: none; border-bottom: 1px solid #7ca0ca;')
        self.setText('Password                                    Forgot?')

    def focusOutEvent(self, event):
        if (len(self.text()) == 0):
            self.clear()
            self.setEchoMode(QtGui.QLineEdit.Normal)
            self.setText('Password                                    Forgot?')
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin :'
                           ' 0px;border: none; border-bottom: 1px solid #7ca0ca;')

    def focusInEvent(self, event):
        if (len(self.text()) == 0 or 'Password                                    Forgot?' == self.text()):
            self.clear()
            self.setEchoMode(QtGui.QLineEdit.Password)
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; '
                           'margin : 0px; border: none; border-bottom: 1.6px solid #edf2f8;')


class emtyBlockAfterEdit(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMinimumSize(100, 0)
        self.setMaximumSize(100, 0)


class buttonLogin0(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMaximumSize(250, 38)
        self.setMinimumSize(250, 38)
        self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
        self.setText('                              Login')

    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: #5f90c8; color: #ffffff; border: none;')
        # print 'mousePressEvent press'

    def mouseReleaseEvent(self, event):
        self.setStyleSheet('background-color: #6698cf; color: #ffffff; border: none;')
        # print 'mouseReleaseEvent press'

    def enterEvent(self, event):
        self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # print 'enterEvent press'

    def leaveEvent(self, event):
        self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
        # print 'leaveEvent press'


class emptyBlock(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMaximumSize(250, 85)
        self.setMinimumSize(250, 85)
        self.setStyleSheet('border: solid;')


class ButtonRegistrationWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMouseTracking(True)
        self.setMaximumSize(250, 30)
        self.setMinimumSize(250, 30)
        self.setStyleSheet(' color: #ffffff; border:none;')
        self.setText('Registration')

    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: #5f90c8; color: #ffffff; border: none;')

    def mouseReleaseEvent(self, event):
        self.setStyleSheet('background-color: #6698cf; color: #ffffff; border: none;')
        # print 'mouseReleaseEvent press'

    def enterEvent(self, event):
        self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # print 'enterEvent press'

    def leaveEvent(self, event):
        self.setStyleSheet(' color: #ffffff; border: none;')
        # print 'leaveEvent press'





# .....................Build Application........................................





from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Worker(QObject):
    finished = pyqtSignal()
    message = pyqtSignal(str)
    obj = ''

    @pyqtSlot()
    def process(self):
        while True:
            print 'START'
            mess = self.obj.whileReceive()
            print 'dannie from sock ',mess
            if mess == None:
                print 'none'
            else:
                self.message.emit(str(mess))

        self.finished.emit()

        # ...............Create Pattern Message......................
class MessageByMe(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setWordWrap(True)
        self.setMinimumSize(90, 40)
        # self.setContentsMargins(5, 5, 5, 5)
        self.setStyleSheet(' background: #EFFDDE; color: #555555;'
                           ' border-radius: 10px;'
                           ' border: none;border-bottom: 1.4px solid #C5E2AD;')

class MessageSendByMeWidget(QtGui.QLabel):

    def __init__(self, parent=None):
        self.meth = QtGui.QScrollArea()
        self.meth.setVisible(False)
        QtGui.QLabel.__init__(self, parent)
        # self.setContentsMargins(5, 5, 5, 5)
        self.setMinimumSize(300, 40)
        # self.setMaximumWidth(600)
        self.setWordWrap(True)
        self.adjustSize()
        self.setStyleSheet('border: none; background: transparent; color: #555555;')

        self.containerLayout = HLayout()
        self.containerLayout.setAlignment(QtCore.Qt.AlignRight)
        self.containerLayout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(self.containerLayout)
        # /  left /   top  /   right /  bottom  /

        self.MyLogoLayoutbyMessage = VLayout()
        self.MyLogoLayoutbyMessage.setAlignment(QtCore.Qt.AlignTop)
        self.MyLogoLayoutbyMessage.setContentsMargins(5, 1, 0, 0)

        MyLogoWidgetbyMessage = QtGui.QLabel()
        MyLogoWidgetbyMessage.setMinimumSize(36, 36)
        MyLogoWidgetbyMessage.setMaximumSize(36, 36)
        MyLogoWidgetbyMessage.setStyleSheet('background-image: url(./img/myLogoAboutMessage.png);'
                                            ' border-radius: 18px; border: 1px solid #FFFFFF;')
        self.MyLogoLayoutbyMessage.addWidget(MyLogoWidgetbyMessage)

        self.LabelMessageWidget = MessageByMe()
        self.containerLayout.addWidget(self.LabelMessageWidget)
        self.containerLayout.addLayout(self.MyLogoLayoutbyMessage)

    def enterEvent(MyLogoWidgetbyMessage, event):
        MyLogoWidgetbyMessage.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        print 'olopopopopopop'
        if(self.meth.isVisible()):
            self.meth.setVisible(False)
        else:
            self.meth.setVisible(True)


class MessageFromFriend(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setWordWrap(True)
        self.setMinimumSize(90, 20)
        self.setStyleSheet(' background: #FBFAF9; color: #555555;'
                           ' border-radius: 10px;'
                           ' border: none;border-bottom: 1.4px solid #E2E4E3')

class MessageFromFriendWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        # self.setContentsMargins(5, 5, 5, 5)
        self.setMinimumSize(600, 40)
        # self.setMaximumWidth(600)
        # self.adjustSize()
        self.setStyleSheet('border: none; background: transparent; color: #555555;')

        self.containerLayout = HLayout()
        self.containerLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.containerLayout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(self.containerLayout)
        # /  left /   top  /   right /  bottom  /

        self.FriendLogoLayoutbyMessage = VLayout()
        self.FriendLogoLayoutbyMessage.setAlignment(QtCore.Qt.AlignTop)
        self.FriendLogoLayoutbyMessage.setContentsMargins(0, 1, 5, 0)
        self.containerLayout.addLayout(self.FriendLogoLayoutbyMessage)

        self.FriendLogoWidgetbyMessage = QtGui.QLabel()
        self.FriendLogoWidgetbyMessage.setMinimumSize(36, 36)
        self.FriendLogoWidgetbyMessage.setMaximumSize(36, 36)
        self.FriendLogoWidgetbyMessage.setStyleSheet('background-image: url(./img/logoFriendaboutMessage.jpg);'
                                                     ' border-radius: 18px; border: 1px solid #FFFFFF;')
        self.FriendLogoLayoutbyMessage.addWidget(self.FriendLogoWidgetbyMessage)

        self.LabelMessageWidget = MessageFromFriend()
        self.containerLayout.addWidget(self.LabelMessageWidget)

# ...............End  create Pattern Message.................









class LeaftAreaWidget(QtGui.QScrollArea):
    def __init__(self, parent=None):
        QtGui.QScrollArea.__init__(self, parent)
        self.setWidgetResizable(True)
        self.setMinimumWidth(310)
        self.setMaximumWidth(310)
        self.setStyleSheet('border: none; subcontrol-position: left;')
        self.setContentsMargins(0, 0, 0, 0)

        self.container = QtGui.QWidget()
        self.container.setContentsMargins(0, 0, 0, 0)
        self.setWidget(self.container)
        self.layoutForleftArea = VLayout()
        self.layoutForleftArea.setAlignment(QtCore.Qt.AlignTop)
        self.container.setLayout(self.layoutForleftArea)
        self.container.setStyleSheet('border: none;')


    def addNewFriend(self, newFriend):
        self.layoutForleftArea.addWidget(newFriend)



class LeftFriendWidget(QtGui.QLabel):
    def __init__(self, friendLogin, friendName, messageCount, parent=None, ):
        QtGui.QLabel.__init__(self, parent )
        self.setMinimumSize(310, 70)
        self.setMaximumSize(310, 70)
        self.setContentsMargins(10,0,5,0)
        # /  left /   top  /   right /  bottom  /
        self.defoltStyle = '''background: #ffffff; border: none;
                              border-bottom: 1px solid #cacfd2;'''
        self.setStyleSheet(self.defoltStyle)
        self.contentLaout = HLayout()
        self.contentLaout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.contentLaout)

        self.friendLogin = friendLogin
        self.friendName = friendName
        self.messageCount = messageCount

        self.logo = QtGui.QLabel()
        self.logo.setMinimumSize(56,56)
        self.logo.setMaximumSize(56,56)
        self.logo.setStyleSheet('background: url(./img/logoFriendLeftArea/admin.png);'
                                ' border: none;'
                                'border-radius: 28px;')
        self.contentLaout.addWidget(self.logo)

        self.friendNameAndMessage = QtGui.QLabel()
        self.friendNameAndMessage.setMinimumSize(200, 65)
        self.friendNameAndMessageLayout = VLayout()
        self.friendNameAndMessage.setStyleSheet('margin-left: 1px; border: none;')
        self.friendNameAndMessage.setLayout(self.friendNameAndMessageLayout)


        self.friendNameWidget = QtGui.QLabel(self.friendName)
        self.friendNameWidget.setStyleSheet('border: none; font-size: 22px; color: #282828;')
        self.friendNameLastMessage = QtGui.QLabel('Hello how are\n you?')
        self.friendNameLastMessage.setVisible(False)
        self.friendNameLastMessage.setStyleSheet('border: none; font-size: 12px; color: #696969;')
        self.friendNameAndMessageLayout.addWidget(self.friendNameWidget)
        self.friendNameAndMessageLayout.addWidget(self.friendNameLastMessage)

        self.contentLaout.addWidget(self.friendNameAndMessage)


        self.messageCountWidget = QtGui.QLabel(str(self.messageCount))
        self.messageCountWidget.setMinimumSize(24,24)
        self.messageCountWidget.setMaximumHeight(24)
        self.messageCountWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.messageCountWidget.setStyleSheet('background: #579E1C; font-size: 14px;'
                                              'border-radius: 10px; color: #ffffff;')

        self.contentLaout.addWidget(self.messageCountWidget)

    def enterEvent(self, event):
        self.setStyleSheet('background: #EBEDED; border: none;'
                           'border-bottom: 1px solid #cacfd2;')
    def mousePressEvent(self, event):
        self.setStyleSheet('background: #DFE5E6; border: none;'
                           'border-bottom: 1px solid #cacfd2;')
        self.messageCountWidget.setText('0')
    def leaveEvent(self, event):
        self.setStyleSheet(self.defoltStyle)



    def setCountMessage(self, count):
        self.messageCount = self.messageCount + count
        self.messageCountWidget.setText(str(self.messageCount))

    def getCountMessage(self, count):
        return self.messageCountWidget.text()




class LeftFooterWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMinimumSize(310,60)
        self.setMaximumSize(310,60)
        self.setStyleSheet('background: #EBEBEB;border: none; '
                           'border-top: 1px solid #cacfd2;')



class MainLeftWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMinimumWidth(310)
        self.setMaximumWidth(310)
        self.setStyleSheet('border:none; background: #ffffff;')
        self.setContentsMargins(0, 0, 0, 0)
        self.setVisible(False)
        self.layoutForMainLeftWidget = VLayout()
        self.layoutForMainLeftWidget.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layoutForMainLeftWidget)

        self.leftHeader = QtGui.QWidget()
        self.buttonMenu = ButtonMenuWidget()
        self.inputSearch = inputSearchWidget()

        self.buildLeftHeader()

        self.leftArea = LeaftAreaWidget()
        self.layoutForMainLeftWidget.addWidget(self.leftArea)





        self.leftFoooter = LeftFooterWidget()
        self.layoutForMainLeftWidget.addWidget(self.leftFoooter)


    def buildLeftHeader(self):
        self.layoutForWidgetsLeftHeader = HLayout()
        self.layoutForWidgetsLeftHeader.setAlignment(QtCore.Qt.AlignLeft)
        self.leftHeader.setLayout(self.layoutForWidgetsLeftHeader)
        self.leftHeader.setMinimumSize(310, 60)
        self.leftHeader.setMaximumSize(310, 60)
        self.leftHeader.setStyleSheet('border: none; border-bottom: 1px solid #cacfd2;')

        self.layoutForWidgetsLeftHeader.addWidget(self.buttonMenu)
        self.layoutForWidgetsLeftHeader.addWidget(self.inputSearch)

        self.layoutForMainLeftWidget.addWidget(self.leftHeader)

    def addWidgetInLeftArea(self, logoImg, friendName, login ):

        self.leftArea.addNewFriend(self.but)
        print 'add'


























class MainAuthenticationWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Authentication Window')
        self.setWindowIcon(QtGui.QIcon('connect.png'))
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setContentsMargins(0, 0, 0, 0)
        # first width second hight
        # 290 460  #410 460
        self.setMinimumSize(300, 480)
        self.setMaximumSize(310, 480)

        self.setStyleSheet('background-color: #5181b8; border: none;')

        self.statusConnection = False
        self.statusAuthorization = False
        self.statres = False
        self.act = action.A()
        self.localTime = strftime("%I:%M", time.localtime())


        class buttonSendMessage(ButtonSendMessage):
            def mousePressEvent(parent, event):
                #print'\nWas be send buttonSendMessage:\n'
                self.send_message()
                self.friend.messageCountWidget.setText('0')

        class buttonAttachFile(ButtonAttachFile):
            def mousePressEvent(parent, event):
                print 'open directory'
                self.showAttachDialog()

        class buttonLogin(buttonLogin0):
            def mousePressEvent(parent, event):
                print '370'
                self.pressLoginAction()

                #reactor.connectTCP("localhost", 8000, EchoFactory())
                #reactor.run()

        class ButtonRegistration(ButtonRegistrationWidget):
            def mousePressEvent(parent, event):
                print 'line 375'
                self.pressRegistrationAction()

        class ButtonBackRegistration(ButtonBackRegistrationWidget):
            def mousePressEvent(parent, event):
                print'line 380'
                self.pressBackAction()

        class InputLineForSendMessage(inputSendMessageWidget):
            def focusInEvent(parent, event):
                if (parent.text() == 'Write a message...'):
                    parent.clear()
                    parent.setStyleSheet('margin: 1px 10px 1px 10px;'
                                       ' background-color: #ffffff; '
                                       'font-size: 16px; padding-left: 10px;'
                                       ' color: #3A3131; border: 1px solid #B3E08E;'
                                       '  border-radius: 4px;')

        class HeaderRegistration(HeaderRegistrationWidget):
            def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.setMaximumSize(290, 40)
                self.setMinimumSize(290, 40)
                LayoutH = QtGui.QHBoxLayout()
                LayoutH.setMargin(0)
                self.setStyleSheet('background: #5181b8;')
                self.buttonBack = ButtonBackRegistration()
                # self.buttonBack.setStyleSheet('margin-bottom: 20px;')
                self.setLayout(LayoutH)

                self.registrationLabel = QtGui.QLabel('Registration:')
                self.registrationLabel.setMaximumSize(240, 40)
                self.registrationLabel.setMinimumSize(240, 40)
                self.registrationLabel.setStyleSheet('padding-top:1px;font: Arial; font-size: 18px;'
                                                     ' background: #5181b8;color: #ffffff;')

                LayoutH.addWidget(self.buttonBack)
                LayoutH.addWidget(self.registrationLabel)





        mainAuthenticationWindowLayout = HLayout()
        self.setLayout(mainAuthenticationWindowLayout)

        layoutForWidgetAuthenticationWindow = VLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetAuthenticationWindow)

        layoutForWidgetRegestrationWindow = VLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetRegestrationWindow)

        # ...................Start content Registration Form.............................
        self.RegistrationHeader = HeaderRegistration()
        self.RegistrationHeader.setContentsMargins(0, 0, 0, 0)
        self.RegistrationHeader.setStyleSheet('border: none;')

        self.emptyLabel0 = QtGui.QLabel('      Registration Form')
        self.emptyLabel0.setStyleSheet(' text-align:right;')
        self.emptyLabel0.setMinimumSize(200, 420)
        self.emptyLabel0.setMaximumSize(200, 420)

        self.RegistrationHeader.setVisible(False)
        self.emptyLabel0.setVisible(False)

        layoutForWidgetRegestrationWindow.addWidget(self.RegistrationHeader)
        layoutForWidgetRegestrationWindow.addWidget(self.emptyLabel0)
        # ...................End content Registration Form.............................



        # ...................Start content authentification.............................
        self.logoWidget = logoWidget()  # first width second hight

        self.inputLineForLoginUser = inputLineLogin()
        self.inputLineForPasswordUser = inputLinePassword()
        self.emtyBlockAfterEdit = emtyBlockAfterEdit()

        self.btnLogin = buttonLogin()
        self.emptyBlock = emptyBlock()

        self.btnRegistration = ButtonRegistration()

        layoutForWidgetAuthenticationWindow.addWidget(self.logoWidget)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForLoginUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForPasswordUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.emtyBlockAfterEdit)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnLogin)
        layoutForWidgetAuthenticationWindow.addWidget(self.emptyBlock)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnRegistration)

        # ...................End content authentification.............................



        # ...................Start content Main User Form.............................
        MainUserWindow = HLayout()
        mainAuthenticationWindowLayout.addLayout(MainUserWindow)

        leftLayoutMainuserWindow = VLayout()
        MainUserWindow.addLayout(leftLayoutMainuserWindow)

        rightLayoutMainuserWindow = HLayout()
        MainUserWindow.addLayout(rightLayoutMainuserWindow)

        self.leftWidget = QtGui.QWidget()
        self.leftWidget.setMinimumSize(300, 470)
        self.leftWidget.setMaximumSize(300, 900)
        self.leftWidget.setStyleSheet('border:1px solid; background: #ffffff; border: none;')
        self.leftWidget.setContentsMargins(0, 0, 0, 0)
        self.leftWidget.setVisible(False)



        # ...................Start content self.leftWidget.............................
        leftWidgetlayout = VLayout()
        self.leftWidget.setLayout(leftWidgetlayout)

        self.leftHeader = QtGui.QWidget()
        layoutForWidgetsLeftHeader = HLayout()
        layoutForWidgetsLeftHeader.setAlignment(QtCore.Qt.AlignLeft)

        self.leftHeader.setLayout(layoutForWidgetsLeftHeader)
        self.leftHeader.setMinimumSize(300, 60)
        self.leftHeader.setMaximumSize(300, 60)
        self.leftHeader.setStyleSheet('border: none; border-bottom: 1px solid #cacfd2;')

        self.buttonMenu = ButtonMenuWidget()
        self.inputSearch = inputSearchWidget()
        layoutForWidgetsLeftHeader.addWidget(self.buttonMenu)
        layoutForWidgetsLeftHeader.addWidget(self.inputSearch)

        self.leftArea = QtGui.QScrollArea()
        self.leftArea.setWidgetResizable(True)
        self.leftArea.setMinimumSize(300, 425)
        self.leftArea.setMaximumSize(300, 900)
        self.leftArea.setStyleSheet('border: none; subcontrol-position: left;')
        self.leftArea.setContentsMargins(0, 0, 0, 0)

        self.boxwid = QtGui.QWidget()
        self.leftArea.setWidget(self.boxwid)
        self.layoutForleftArea = VLayout()
        self.layoutForleftArea.setAlignment(QtCore.Qt.AlignTop)
        self.boxwid.setLayout(self.layoutForleftArea)
        self.boxwid.setStyleSheet('border: none;')




        leftWidgetlayout.addWidget(self.leftHeader)
        leftWidgetlayout.addWidget(self.leftArea)

        # ...................End content self.leftWidget.............................




        # ...................Start content self.rightWidget.............................
        self.rightWidget = QtGui.QLabel()
        self.rightWidget.setMinimumSize(300, 470)
        self.rightWidget.adjustSize()
        #self.rightWidget.setMaximumSize(1000, 1000)
        self.rightWidget.setContentsMargins(0, 0, 0, 0)
        self.rightWidget.setStyleSheet(' border: none; background-image: url(./img/fon3.png);'
                                       'border-left: 1px solid #cacfd2;')
        rightWidgetlayout = VLayout()
        rightWidgetlayout.setAlignment(QtCore.Qt.AlignTop)
        self.rightWidget.setLayout(rightWidgetlayout)
        self.rightWidget.setVisible(False)

#background: url(./fon3.png);

        self.rightHeader = EmptyBoxWidget()
        layoutForWidgetsRightHeader = HLayout()
        self.rightHeader.setLayout(layoutForWidgetsRightHeader)

        self.rightHeader.setMinimumSize(280, 60)
        self.rightHeader.setMaximumSize(1000, 60)
        self.rightHeader.setStyleSheet('border:none;'
                                       ' border-bottom: 1px solid #D6D6D6; background: #fdfcfc;')

        #self.labelNameUserReightHeader = QtGui.QLabel('Nicolai Komar')
        self.labelNameUserReightHeader = QtGui.QLabel()
        self.labelNameUserReightHeader.setStyleSheet('color : #5d5d5d; font:  Arial;'
                                                     'font-size: 25px;border:none;')
        self.labelNameUserReightHeader.setMinimumSize(170, 50)
        self.labelNameUserReightHeader.setMaximumSize(170, 50)
        self.labelNameUserReightHeader.setAlignment(QtCore.Qt.AlignCenter)

        layoutForWidgetsRightHeader.addWidget(self.labelNameUserReightHeader)
        layoutForWidgetsRightHeader.setAlignment(QtCore.Qt.AlignCenter)



        self.rightArea = QtGui.QScrollArea()
        self.rightArea.setWidgetResizable(True)
        self.rightArea.setMinimumSize(100, 400)
        self.rightArea.setContentsMargins(0, 0, 0, 0)
        self.rightArea.adjustSize()
        self.rightArea.verticalScrollBar().rangeChanged.connect(self.ResizeScroll)
        self.rightArea.setStyleSheet("""QScrollArea{
                                            border-right:3px solid #111;
                                            background: transparent;
                                            border: none;
                                            
                                        }
                                        QStatusBar {
                                            border-left: 4px solid red;
                                            
                                        }
                                        QScrollBar{
                                             background: transparent;
                                             border: none;
                                             
                                         }
                                        QScrollBar:vertical {
                                             background: #E5E5E2;
                                             width: 10px;
                                             margin: 0px 5px 0px 0px;
                                             border: none;
                                         }
                                         QScrollBar::handle:vertical {
                                             border: none;
                                             background: #A9A9A9;
                                             min-height: 20px;
                                             
                                         }
                                         QScrollBar::add-line:vertical {
                                             border: none;
                                             background: transparent;
                                             height: 0px;
                                             subcontrol-position: bottom;
                                             subcontrol-origin: margin;
                                         }
                                        
                                         QScrollBar::sub-line:vertical {
                                             border: none;
                                             background: transparent;
                                             height: 0px;
                                             subcontrol-position: top;
                                             subcontrol-origin: margin;
                                         }
                                        
                                        
                                         QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                             background: transparent;
                                             border: none;
                                         }
                                                                               
                                          """)

        self.rightArea.setStyleSheet('border:none; background: transparent;')


        self.rightArea.setAlignment(QtCore.Qt.AlignCenter)
        self.rightWidgetForSendMessage = EmptyBoxWidget()
        self.rightWidgetForSendMessage.setMinimumSize(300, 60)
        self.rightWidgetForSendMessage.setMaximumSize(1000, 60)
        self.rightWidgetForSendMessage.setStyleSheet('background: #EBEBEB; border: none;'
                                                     ' border-left: 1px solid #D6D6D6;'
                                                     ' border-top: 1px solid #D6D6D6;'
                                                     'border-bottom: 1px solid #D6D6D6;')

        layoutForRightWidgetSendMessage = HLayout()
        self.rightWidgetForSendMessage.setLayout(layoutForRightWidgetSendMessage)



        self.buttonAttachFile = buttonAttachFile()
        self.inputWidgetForSendMessage = InputLineForSendMessage()
        self.buttonSendMessage = buttonSendMessage()



        layoutForRightWidgetSendMessage.addWidget(self.buttonAttachFile)
        layoutForRightWidgetSendMessage.addWidget(self.inputWidgetForSendMessage)
        layoutForRightWidgetSendMessage.addWidget(self.buttonSendMessage)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.boxwidr = QtGui.QLabel()
        self.boxwidr.setMaximumWidth(480)
        #self.boxwidr.adjustSize()
        self.rightArea.setWidget(self.boxwidr)
        self.layoutForRightArea = VLayout()
        self.layoutForRightArea.setAlignment(QtCore.Qt.AlignTop)
        self.boxwidr.setLayout(self.layoutForRightArea)

        self.boxwidr.setContentsMargins(0, 0, 0, 0)
        self.boxwidr.setStyleSheet(' background: transparent;')


        rightWidgetlayout.addWidget(self.rightHeader)

        self.layoutForRightAreaAndInformationAboutUser = HLayout()
        self.layoutForRightAreaAndInformationAboutUser.setAlignment(QtCore.Qt.AlignTop)
        self.layoutForRightAreaAndSendMessageWidgets = VLayout()
        self.layoutForRightAreaAndSendMessageWidgets.setAlignment(QtCore.Qt.AlignTop)
        self.layoutForInformationAboutUserWidgets = VLayout()
        self.layoutForInformationAboutUserWidgets.setAlignment(QtCore.Qt.AlignTop)
        self.layoutForRightAreaAndInformationAboutUser.addLayout(self.layoutForRightAreaAndSendMessageWidgets)
        self.layoutForRightAreaAndInformationAboutUser.addLayout(self.layoutForInformationAboutUserWidgets)
        self.rightWidgetForRightAreaAndInformationAboutUser = QtGui.QWidget()
        self.rightWidgetForRightAreaAndInformationAboutUser.setContentsMargins(0, 0, 0, 0)
        self.rightWidgetForRightAreaAndInformationAboutUser.setLayout(self.layoutForRightAreaAndInformationAboutUser)
        self.rightWidgetForRightAreaAndInformationAboutUser.setStyleSheet('border: none;')
        self.rightWidgetForRightAreaAndInformationAboutUser.setMinimumSize(480,480)


            #User information


        self.rightAreaForUserInformation = QtGui.QScrollArea()
        self.rightAreaForUserInformation.setWidgetResizable(True)
        self.rightAreaForUserInformation.setMinimumSize(250, 700)
        self.rightAreaForUserInformation.setMaximumWidth(250)
        self.rightAreaForUserInformation.adjustSize()
        self.rightAreaForUserInformation.setContentsMargins(0, 0, 0, 0)
        #self.rightAreaForUserInformation.verticalScrollBar().rangeChanged.connect(self.ResizeScroll)


        self.rightAreaForUserInformation.setStyleSheet('border:none; background: #654789;')

        self.boxUserInformation = QtGui.QLabel()
        self.boxUserInformation.setMinimumSize(250, 400)
        self.rightAreaForUserInformation.setMaximumWidth(250)
        self.boxUserInformation.adjustSize()
        self.rightAreaForUserInformation.setWidget(self.boxUserInformation)
        self.layoutForRightAreaUserInformation = VLayout()
        self.layoutForRightAreaUserInformation.setAlignment(QtCore.Qt.AlignTop)
        self.layoutForRightAreaUserInformation.setContentsMargins(10,10,10,10)
        self.boxUserInformation.setLayout(self.layoutForRightAreaUserInformation)

        self.boxUserInformation.setContentsMargins(0, 0, 0, 0)
        self.boxUserInformation.setStyleSheet(' background: #ffffff; border: 1px solid #d6d6d6;')

        self.buttonBackInUserInfo = QtGui.QPushButton('<')
        self.buttonBackInUserInfo.setMaximumWidth(32)
        self.buttonBackInUserInfo.setMinimumHeight(32)
        self.buttonBackInUserInfo.setStyleSheet('background: #ffffff; border: 1px solid #666666;'
                                                ' border-radius: 16px; font-size: 26px; color:#666666;')
        self.layoutForRightAreaUserInformation.addWidget(self.buttonBackInUserInfo)
        self.rightAreaForUserInformation.setVisible(False)

        self.connect(self.buttonBackInUserInfo, QtCore.SIGNAL('clicked()'), self.peressB)





        rightWidgetlayout.addWidget(self.rightWidgetForRightAreaAndInformationAboutUser)
        self.layoutForRightAreaAndSendMessageWidgets.addWidget(self.rightArea)
        self.layoutForRightAreaAndSendMessageWidgets.addWidget(self.rightWidgetForSendMessage)
        self.layoutForInformationAboutUserWidgets.addWidget(self.rightAreaForUserInformation)





        #rightWidgetlayout.addWidget(self.rightArea)
        #rightWidgetlayout.addWidget(self.rightWidgetForSendMessage)

        # ...................End content self.rightWidget.............................



        leftLayoutMainuserWindow.addWidget(self.leftWidget)
        self.mainLeftWidget = MainLeftWidget()
        self.mainLeftWidget.setVisible(False)
        leftLayoutMainuserWindow.addWidget(self.mainLeftWidget)

        self.friend = LeftFriendWidget('admin', 'Artur Drabinko', 0)
        self.mainLeftWidget.leftArea.addNewFriend(self.friend )





















        rightLayoutMainuserWindow.addWidget(self.rightWidget)
        #rightLayoutMainuserWindow.addWidget(self.rightWidgetUserInformation)




    def start_main_user_form(self):


        print 'True login'
        self.setWindowTitle('GoSay')
        self.setMinimumSize(380, 450)
        self.setMaximumSize(1500, 1000)
        self.resize(910, 540)
        self.logoWidget.setVisible(False)
        self.inputLineForLoginUser.setVisible(False)
        self.inputLineForPasswordUser.setVisible(False)
        self.emtyBlockAfterEdit.setVisible(False)
        self.btnLogin.setVisible(False)
        self.emptyBlock.setVisible(False)
        self.btnRegistration.setVisible(False)

        self.Friend13 = QtGui.QLabel('   Nikolai Komar\n   You: Hi!')
        self.Friend13.setMinimumSize(300, 62)
        self.Friend13.setMaximumSize(320, 62)
        self.Friend13.setStyleSheet('background: #f1f1f1; color: #171515;'
                                    ' border: none; border-bottom: 1px solid #cacfd2')



        self.layoutForleftArea.addWidget(self.Friend13)


        #self.leftWidget.setVisible(self.statusConnection)
        self.mainLeftWidget.setVisible(self.statusConnection)
        self.rightWidget.setVisible(self.statusConnection)

        self.labelNameUserReightHeader.setText(self.inputLineForLoginUser.text())

        self.statres = True

    def start(self):
        self.thread = QThread(self)
        self.worker = Worker()
        self.worker.obj = self.act
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.message.connect(self.addMessageFromFriend)
        self.thread.start()





    def peressB(self):
        #self.rightAreaForUserInformation.setParent(None)
        self.rightAreaForUserInformation.setVisible(False)
        #self.layoutForInformationAboutUserWidgets.removeWidget(self.rightAreaForUserInformation)

    def ResizeScroll(self, min, maxi):
        self.rightArea.verticalScrollBar().setValue(maxi)

    def pressRegistrationAction(self):
        print 'press ...........start pressRegistrationAction........'
        self.logoWidget.setVisible(False)
        self.inputLineForLoginUser.setVisible(False)
        self.inputLineForPasswordUser.setVisible(False)
        self.emtyBlockAfterEdit.setVisible(False)
        self.btnLogin.setVisible(False)
        self.emptyBlock.setVisible(False)
        self.btnRegistration.setVisible(False)

        self.RegistrationHeader.setVisible(True)
        self.emptyLabel0.setVisible(True)
        newThread = ThreadDB()
        newThread.start()
        self.setMinimumSize(290, 460)
        self.setMaximumSize(600, 460)
        self.resize(290, 460)
        print 'press ...........end pressRegistrationAction...........'

    def pressBackAction(self):
        print 'press ...........start pressBackAction........'
        self.logoWidget.setVisible(True)
        self.inputLineForLoginUser.setVisible(True)
        self.inputLineForPasswordUser.setVisible(True)
        self.emtyBlockAfterEdit.setVisible(True)
        self.btnLogin.setVisible(True)
        self.emptyBlock.setVisible(True)
        self.btnRegistration.setVisible(True)

        self.RegistrationHeader.setVisible(False)
        self.emptyLabel0.setVisible(False)
        newThread = ThreadDB()
        newThread.start()

        self.setMinimumSize(290, 460)
        self.setMaximumSize(290, 460)
        self.resize(290, 460)
        # workPlace.show()
        print 'press ...........end pressBackAction...........'

    def pressLoginAction(self):
        # r = MainAuthenticationWindow(self)
        # t1 = threading.Thread(target= r.lisenS(), args=())
        # t1.start()
        self.btnLogin.setCursor(QCursor(QtCore.Qt.WaitCursor))
        if (self.statusConnection == False):
            self.statusConnection = self.act.estabilishConnection()
            self.btnLogin.setCursor(QCursor(QtCore.Qt.ArrowCursor))

        if (self.statusConnection == True and self.statusAuthorization == False):
            self.statusAuthorization = self.act.loginAction(str(self.inputLineForLoginUser.text()),
                                                            str(self.inputLineForPasswordUser.text()))

        if (self.statusAuthorization == True):
            self.start_main_user_form()
            self.start()
        else:
            self.inputLineForPasswordUser.setText('incorrect Pasword')






    def send_message(self):
        if self.inputWidgetForSendMessage.text() == 'Write a message...' or self.inputWidgetForSendMessage.text() == '':
            self.inputWidgetForSendMessage.clear()
            self.buttonSendMessage.setFocus(False)
            self.inputWidgetForSendMessage.setFocus(True)
        else:
            self.act.send_message_action(str(self.inputWidgetForSendMessage.text()))

            self.messageByMeWidget = MessageSendByMeWidget()
            self.messageByMeWidget.LabelMessageWidget.setText(str(self.inputWidgetForSendMessage.text())+ '___' +self.localTime)
            self.layoutForRightArea.addWidget(self.messageByMeWidget)


            self.empt = QtGui.QWidget()
            self.empt.setMinimumSize(200,14)
            self.empt.setStyleSheet('border: none')
            self.layoutForRightArea.addWidget(self.empt)
            self.inputWidgetForSendMessage.clear()

            self.buttonSendMessage.setFocus(False)
            self.inputWidgetForSendMessage.setFocus(True)

            self.messageByMeWidget.meth = self.rightAreaForUserInformation
    def showAttachDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/art/Desktop/')
        print fname
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.prin = data
            f.close()


        di = open('/home/art/Documents/test.png', 'wb')
        di.write(bytes(self.prin))
        di.close()


        self.testWidge = MessageFromFriendWidget()
        self.testWidge.setStyleSheet('background: transparent; border: none;')
        self.testWidge.setMaximumHeight(200)
        self.testWidge.LabelMessageWidget.setStyleSheet(' background-image: url(/home/art/Documents/test.png); background-repeat: no-repeat;')
        self.testWidge.LabelMessageWidget.setMaximumHeight(200)
        self.layoutForRightArea.addWidget(self.testWidge)
        self.buttonAttachFile.setFocus(False)
        self.inputWidgetForSendMessage.setFocus(True)

    def addMessageFromFriend(self,i):
        print  i
        print type(i)
        if(str(i)== "mess"):
            print 'oppopopopopopooop'
        self.testWidget = MessageFromFriendWidget()

        self.testWidget.LabelMessageWidget.setText('Process_' + str(i)+ '__' +self.localTime)
        self.layoutForRightArea.addWidget(self.testWidget)

        self.emptF = QtGui.QWidget()
        self.emptF.setMinimumSize(200, 14)
        self.emptF.setStyleSheet('border: none')
        self.layoutForRightArea.addWidget(self.emptF)

        self.friend.setCountMessage(1)




    def resizeEvent(self, event):
        if(self.width() < 600):
            #self.leftWidget.setVisible(False)
            self.mainLeftWidget.setVisible(False)
        if(self.width() > 600):
            #self.leftWidget.setVisible(True)
            self.mainLeftWidget.setVisible(True)
        if (self.width() < 900 and self.statres == True):
            print 'False..............'
        if (self.width() > 900 and self.statres == True):
            print 'True.............'

    #def closeEvent(self, event):
        #messbox =QtGui.QMessageBox()
        #messbox.setStyleSheet('background: #111111;border: none;')

        #reply = messbox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes,
         #                                 QtGui.QMessageBox.No)

        #if reply == QtGui.QMessageBox.Yes:
         #   main.setVisible(True)
         #   main.close()
        #else:
        #    event.ignore()


# if __name__ == '__gui2.py__':

app = QtGui.QApplication(sys.argv)

main = MainAuthenticationWindow()

main.show()

sys.exit(app.exec_())









# background: url(./lmess.png) no-repeat;
# background:transparent;