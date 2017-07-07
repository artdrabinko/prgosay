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
        self.setMinimumHeight(65)
        self.setMinimumWidth(300)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('color: #ffffff; border: none; background: #ffffff;')



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
        self.setFocusPolicy(QtCore.Qt.NoFocus)
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
                           ' border: 1px solid #468C0C;  border-radius: 4px;')

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
                           ' border: 1px solid #468C0C;  border-radius: 4px;')


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

        self.setMaximumWidth(380)
        self.setContentsMargins(5, 5, 5, 5)
        self.setStyleSheet(' background: #EFFDDE; color: #555555; padding: 5px;'
                           ' border-radius: 10px;'
                           ' border: none;border-bottom: 1.4px solid #C5E2AD;')

class MessageSendByMeWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.widget = QtGui.QScrollArea()
        self.widget.setVisible(False)


        self.setMaximumWidth(480)
        self.setStyleSheet('border: none; background: transparent; color: #555555;')

        self.containerLayout = HLayout()
        self.containerLayout.setAlignment(QtCore.Qt.AlignRight)
        self.containerLayout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(self.containerLayout)
        # /  left /   top  /   right /  bottom  /

        self.MyLogoLayoutbyMessage = VLayout()
        self.MyLogoLayoutbyMessage.setAlignment(QtCore.Qt.AlignTop)
        self.MyLogoLayoutbyMessage.setContentsMargins(5, 1, 0, 0)


        class MyLogoInMessageWidget(QtGui.QLabel):
            def __init__(self, widget, parent=None):
                QtGui.QLabel.__init__(self, parent)
                self.widget = widget
                self.widget.setVisible(False)

            def mousePressEvent(self, event):
                if self.widget.isVisible():
                    self.widget.setVisible(False)
                else:
                    self.widget.setVisible(True)

        self.MyLogoWidgetbyMessage = MyLogoInMessageWidget(self.widget)
        self.MyLogoWidgetbyMessage.setMinimumSize(36, 36)
        self.MyLogoWidgetbyMessage.setMaximumSize(36, 36)
        self.MyLogoWidgetbyMessage.setStyleSheet('background-image: url(./img/myLogoAboutMessage.png);'
                                                ' border-radius: 18px; border: 1px solid #FFFFFF;')

        self.MyLogoLayoutbyMessage.addWidget(self.MyLogoWidgetbyMessage)

        self.LabelMessageWidget = MessageByMe()
        self.containerLayout.addWidget(self.LabelMessageWidget)
        self.containerLayout.addLayout(self.MyLogoLayoutbyMessage)

    def enterEvent(MyLogoWidgetbyMessage, event):
        MyLogoWidgetbyMessage.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        print 'olopopopopopop'
        if(self.widget.isVisible()):
            self.widget.setVisible(False)
        else:
            self.widget.setVisible(True)


class MessageFromFriend(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setWordWrap(True)

        self.setMaximumWidth(380)
        self.setStyleSheet(' background: #FBFAF9; color: #555555; padding: 5px;'
                           ' border-radius: 10px;'
                           ' border: none;border-bottom: 1.4px solid #E2E4E3')

class MessageFromFriendWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMaximumWidth(480)
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









class LeftAreaWidget(QtGui.QScrollArea):
    def __init__(self, parent=None):
        QtGui.QScrollArea.__init__(self, parent)
        self.setWidgetResizable(True)
        self.setMinimumWidth(310)
        self.setMaximumWidth(310)
        self.setStyleSheet("""QScrollArea{
                                border-right:1px solid #111111;
                                border: none;
    
                            }
                            QStatusBar {
                                border-left: 1px solid red;
    
                            }
                            QScrollBar{
                                 background: transparent;
                                 border: none;
    
                             }
                            QScrollBar:vertical {
                                 background: #E5E5E2;
                                 width: 8px;
                                 margin: 0px 4px 0px 0px;
                                 border: none;
                             }
                             QScrollBar:vertical:hover {
                                 background: #E5E5E2;
                                 width: 10px;
                                 margin: 0px 0px 0px 0px;
                                 border: none;
                             }
                             QScrollBar::handle:vertical {
                                 border: none;
                                 background: #A9A9A9;
                                 min-height: 20px;
                                 width: 5px;
                             }QScrollBar::handle:vertical:hover {
                                 border: none;
                                 background:#787676;
                                 min-height: 20px;
                                 width: 5px;
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

class LeftFriendWidget(QtGui.QPushButton):
    def __init__(self, friendLogin, friendName, messageCount, parent=None, ):
        QtGui.QPushButton.__init__(self, parent )
        self.setMinimumSize(310, 70)
        self.setMaximumSize(310, 70)
        self.setContentsMargins(10,0,5,0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        # /  left /   top  /   right /  bottom  /
        self.defoltStyle = '''background: #ffffff; border: none;'''
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

        self.friendNameAndMessage = QtGui.QWidget()
        self.friendNameAndMessage.setMinimumSize(200, 65)
        self.friendNameAndMessage.setContentsMargins(7, 8, 0, 0)
        self.friendNameAndMessageLayout = VLayout()
        self.friendNameAndMessageLayout.setAlignment(QtCore.Qt.AlignTop)
        self.friendNameAndMessage.setStyleSheet('border: none;')
        self.friendNameAndMessage.setLayout(self.friendNameAndMessageLayout)




        self.friendNameAndStatus = QtGui.QWidget()
        self.friendNameAndStatus.setContentsMargins(0, 0, 0, 0)
        self.friendNameAndStatusLayout = HLayout()
        self.friendNameAndStatus.setLayout(self.friendNameAndStatusLayout)


        self.friendNameWidget = QtGui.QLabel(self.friendName)
        self.friendNameWidget.setContentsMargins(0, 0, 0, 0)
        self.friendNameWidget.setStyleSheet('border: none; font-size: 20px;'
                                            'color: #282828; padding-left: 1px;')

        self.statusFriendWidget = QtGui.QWidget()
        self.statusFriendWidget.setVisible(False)
        self.statusFriendWidget.setMinimumSize(8, 8)
        self.statusFriendWidget.setMaximumSize(8, 8)
        self.statusFriendWidget.setStyleSheet('background: #579E1C;'
                                              'border-radius: 4px;'
                                              'border: none;')

        self.friendNameAndStatusLayout.addWidget(self.statusFriendWidget)
        self.friendNameAndStatusLayout.addWidget(self.friendNameWidget)


        self.friendLastMessage = QtGui.QLabel()
        self.friendLastMessage.setMaximumWidth(180)
        self.friendLastMessage.setWordWrap(True)
        self.friendLastMessage.setVisible(False)
        self.friendLastMessage.setStyleSheet('border: none; font-size: 12px; color: #696969;')
        self.friendNameAndMessageLayout.addWidget(self.friendNameAndStatus)
        self.friendNameAndMessageLayout.addWidget(self.friendLastMessage)

        self.contentLaout.addWidget(self.friendNameAndMessage)


        self.messageCountWidget = QtGui.QLabel(str(self.messageCount))
        self.messageCountWidget.setVisible(False)
        self.messageCountWidget.setMinimumSize(22,22)
        self.messageCountWidget.setMaximumHeight(22)
        self.messageCountWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.messageCountWidget.setStyleSheet('background: #579E1C; font-size: 13px;'
                                              'border-radius: 11px; color: #ffffff;')

        self.contentLaout.addWidget(self.messageCountWidget)

    def enterEvent(self, event):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('background: #EBEDED; border: none;')


    def leaveEvent(self, event):
        self.setStyleSheet(self.defoltStyle)

    def mousePressEvent(self, event):
        self.setStyleSheet('background: #DFE5E6; border: none;')
        self.messageCountWidget.setVisible(False)
        self.messageCount = 0


    def setCountMessage(self, count):
        self.messageCount = self.messageCount + count
        self.messageCountWidget.setText(str(self.messageCount))

    def getCountMessage(self, count):
        return self.messageCountWidget.text()

class FriendsWidget(QtGui.QPushButton):
    def __init__(self, friendLogin, friendName, parent=None, ):
        QtGui.QPushButton.__init__(self, parent )
        self.setMinimumSize(310, 50)
        self.setMaximumSize(310, 50)
        self.setContentsMargins(8,0,8,0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        # /  left /   top  /   right /  bottom  /
        self.defoltStyle = '''background: #ffffff; border: none;'''
        self.setStyleSheet(self.defoltStyle)
        self.contentLayout = QtGui.QHBoxLayout()
        self.contentLayout.setAlignment(QtCore.Qt.AlignVCenter)
        self.contentLayout.setMargin(0)
        self.contentLayout.setSpacing(0)
        self.setLayout(self.contentLayout)
        self.leftLayout = HLayout()
        self.leftLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.rightLayout = HLayout()
        self.rightLayout.setAlignment(QtCore.Qt.AlignRight)
        self.contentLayout.addLayout(self.leftLayout)
        self.contentLayout.addLayout(self.rightLayout)


        self.friendLogin = friendLogin
        self.friendName = friendName
        self.friendID = '1'


        self.logo = QtGui.QLabel()
        self.logo.setMinimumSize(40,40)
        self.logo.setMaximumSize(40,40)
        self.logo.setStyleSheet('background: url(./img/logoFriendLeftArea/admin.png);'
                                ' border: none;'
                                'border-radius: 20px;')
        self.leftLayout.addWidget(self.logo)


        self.friendNameWidget = QtGui.QLabel(self.friendName)
        self.friendNameWidget.setMinimumWidth(50)
        self.friendNameWidget.setStyleSheet('border: none; padding-left: 5px;'
                                            'padding-bottom: 2px; '
                                            'font-size: 18px; color: #282828;')
        self.leftLayout.addWidget(self.friendNameWidget)



        self.statusFriendWidget = QtGui.QWidget()
        self.statusFriendWidget.setVisible(False)
        self.statusFriendWidget.setMinimumSize(8, 8)
        self.statusFriendWidget.setMaximumSize(8, 8)
        self.statusFriendWidget.setStyleSheet('background: #579E1C;'
                                                'border-radius: 4px; color: #ffffff;'
                                                'border: none;')
        self.leftLayout.addWidget(self.statusFriendWidget)


        self.settingsFriendWidget = QtGui.QPushButton()
        self.settingsFriendWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settingsFriendWidget.setMinimumSize(30, 30)
        self.settingsFriendWidget.setMaximumSize(30, 30)
        self.settingsFriendWidget.setStyleSheet("""QPushButton:hover {
                                                 background: url(./img/button_more_hover.png);
                                                 padding: 0px;
                                                }
                                                
                                                QPushButton {
                                                background: url(./img/button_more.png);
                                                color: #ffffff;
                                                border: none;
                                                }""")
        self.rightLayout.addWidget(self.settingsFriendWidget)



    def enterEvent(self, event):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('background: #EBEDED; border: none;')


    def leaveEvent(self, event):
        self.setStyleSheet(self.defoltStyle)

    def mousePressEvent(self, event):
        self.setStyleSheet('background: #DFE5E6; border: none;')




class AddFriendWidget(QtGui.QPushButton):
    def __init__(self, parent=None, ):
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(310, 45)
        self.setMaximumSize(310, 45)
        self.setContentsMargins(10, 0, 8, 0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        # /  left /   top  /   right /  bottom  /
        self.defoltStyle = '''background: #ffffff; border: none;'''
        self.setStyleSheet(self.defoltStyle)
        self.container = HLayout()
        self.container.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.container)


        self.icon = QtGui.QLabel('+')
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setMinimumSize(32, 32)
        self.icon.setMaximumSize(32, 32)
        self.icon.setStyleSheet(' font-size: 24px; color: #548B28;'
                                'border: 1px solid #548B28;padding-bottom: 2px;padding-left: 1px;'
                                'border-radius: 16px;')
        self.container.addWidget(self.icon)

        self.text = QtGui.QLabel('Add contact')
        self.text.setMinimumWidth(50)
        self.text.setStyleSheet('border: none; padding-left: 5px;'
                                'padding-bottom: 2px;'
                                'font-size: 17px; color: #509319;')
        self.container.addWidget(self.text)


    def enterEvent(self, event):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('background: #EBEDED; border: none;')

    def leaveEvent(self, event):
        self.setStyleSheet(self.defoltStyle)

class AreaWidget(QtGui.QScrollArea):
    def __init__(self, parent=None):
        QtGui.QScrollArea.__init__(self, parent)
        self.setWidgetResizable(True)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setMinimumSize(100, 400)
        self.setStyleSheet("""QScrollArea{
                                border: none;
                                border-left:1px solid #D6D6D6;
                            }
                            QScrollBar{
                                 background: transparent;
                                 border: none;
                             }
                            QScrollBar:vertical {
                                 background: #E5E5E2;
                                 width: 8px;
                                 margin: 0px 4px 0px 0px;
                                 border: none;
                             }
                             QScrollBar:vertical:hover {
                                 background: #E5E5E2;
                                 width: 10px;
                                 margin: 0px 0px 0px 0px;
                                 border: none;
                             }
                             QScrollBar::handle:vertical {
                                 border: none;
                                 background: #A9A9A9;
                                 min-height: 20px;
                                 width: 5px;
                             }QScrollBar::handle:vertical:hover {
                                 border: none;
                                 background:#787676;
                                 min-height: 20px;
                                 width: 5px;
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
        self.setContentsMargins(0, 0, 0, 0)

        self.mainContainer = QtGui.QWidget()
        self.mainContainer.setContentsMargins(40, 15, 40, 0)
        self.setWidget(self.mainContainer)
        self.layoutForMainContainer= VLayout()
        self.layoutForMainContainer.setAlignment(QtCore.Qt.AlignTop)
        self.mainContainer.setLayout(self.layoutForMainContainer)
        self.mainContainer.setStyleSheet('border:none; background: #ffffff;')

        self.header = QtGui.QWidget()
        self.header.setStyleSheet('border:none;')
        self.header.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = VLayout()
        self.header.setLayout(self.headerContainer)

        self.label = QtGui.QLabel('Add contact')
        self.label.setStyleSheet('font-size: 29px;')
        self.label.setContentsMargins(0, 0, 0, 0)
        self.headerContainer.addWidget(self.label)


        self.searchWidget = QtGui.QWidget()
        self.searchWidget.setContentsMargins(0, 26, 20, 0)
        self.searchWidgetContainer = HLayout()
        self.searchWidget.setLayout(self.searchWidgetContainer)
        self.headerContainer.addWidget(self.searchWidget)


        self.searchLine = QtGui.QLineEdit()
        self.searchLine.setMinimumSize(120,42)
        self.searchLine.setStyleSheet('background: #ffffff; border:none; font-size: 17px; color: #222222;'
                                      'margin-right: 12px; border-bottom: 1px solid #cacfd2;')
        self.searchWidgetContainer.addWidget(self.searchLine)

        self.searchButton = QtGui.QPushButton('Search')
        self.searchButton.setMinimumSize(130, 33)
        self.searchButton.setMaximumSize(130, 33)
        self.searchButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.searchButton.setStyleSheet('background: #579E1C; border:none;'
                                        'font-size: 16px; color: #ffffff;')
        self.searchWidgetContainer.addWidget(self.searchButton )

        self.layoutForMainContainer.addWidget(self.header)




class LeftButtonMyFriends(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(60,40)
        self.setMaximumSize(60,40)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('background: #EBEBEB; border: none;')


class LeftButtonAddFriend(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(60,40)
        self.setMaximumSize(60,40)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('background: #EBEBEB; border: none;')


class MainLeftWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
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

        self.leftArea = LeftAreaWidget()
        self.layoutForMainLeftWidget.addWidget(self.leftArea)



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


class LeftTabWidget(QtGui.QTabWidget):
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)
        self.setVisible(False)
        self.setMinimumWidth(310)
        self.setMaximumWidth(310)
        self.setTabPosition(1)

        self.style = """
                        QTabWidget::pane{
                        border: none;
                        padding: 0px;
                        width: 310px;
                        border-bottom: 1px solid #cacfd2;
                        alignment: center;
                        }
                        
                        QTabBar::tab{
                        height: 59px;
                        width: 77px;
                        background: #EBEBEB;
                        border: none;
                        alignment: center;
                        }
                        QTabBar::tab:hover {
                        background: #EBEBEB;
                        padding: 0px;
                        
                        }

                        QTabWidget::tab-bar{
                        alignment: center;
                        width: 310px;
                        }
                        """

        self.setStyleSheet(self.style)

        self.setContentsMargins(0,0,0,0)
        self.setUsesScrollButtons(False)












class MainAuthenticationWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.friendList = {}
        self.setWindowTitle('Authentication Window')
        self.setWindowIcon(QtGui.QIcon('connect.png'))
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setContentsMargins(0, 0, 0, 0)
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
                self.send_message()


        class LeftFriendInList(LeftFriendWidget):
            def mousePressEvent(parent, event):
                self.addFriendOnMainLeftWidget()

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
                                       ' color: #3A3131; border: 1px solid #468C0C;'
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


        # ...................End content self.leftWidget.............................




        # ...................Start content self.rightWidget.............................
        self.rightWidget = QtGui.QWidget()
        self.rightWidget.setMinimumSize(100, 470)


        self.rightWidget.setContentsMargins(1, 0, 0, 0)
        self.rightWidget.setStyleSheet(' border: none; background-image: url(./img/fon3.png);'
                                       'border-left: 4px solid #cacfd2;')
        rightWidgetlayout = VLayout()
        rightWidgetlayout.setAlignment(QtCore.Qt.AlignTop)
        self.rightWidget.setLayout(rightWidgetlayout)
        self.rightWidget.setVisible(False)

#background: url(./fon3.png);

        self.rightHeader = EmptyBoxWidget()
        layoutForWidgetsRightHeader = HLayout()
        self.rightHeader.setLayout(layoutForWidgetsRightHeader)

        self.rightHeader.setMinimumSize(400, 60)
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
        self.rightArea.setAlignment(QtCore.Qt.AlignCenter)
        self.rightArea.setMinimumSize(100, 400)
        self.rightArea.setContentsMargins(0, 0, 0, 0)
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

        #self.rightArea.setStyleSheet('border:none; background: transparent;')


        self.rightWidgetForSendMessage = EmptyBoxWidget()
        self.rightWidgetForSendMessage.setMinimumSize(300, 60)
        self.rightWidgetForSendMessage.setMaximumSize(1000, 60)
        self.rightWidgetForSendMessage.setStyleSheet('background: #EBEBEB; border: none;'
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
        self.boxwidr = QtGui.QWidget()
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
        #self.layoutForInformationAboutUserWidgets.addWidget(self.rightAreaForUserInformation)





        #rightWidgetlayout.addWidget(self.rightArea)
        #rightWidgetlayout.addWidget(self.rightWidgetForSendMessage)

        # ...................End content self.rightWidget.............................



        #leftLayoutMainuserWindow.addWidget(self.leftWidget)

        self.countUser = 0

        self.mainLeftWidget = MainLeftWidget()


        self.friend = LeftFriendInList('admin', 'Artur Drabinko', 0)
        self.mainLeftWidget.leftArea.addNewFriend(self.friend)

        self.friendList[self.countUser] = self.friend
        self.countUser = self.countUser + 1
        self.leftTabWidget = LeftTabWidget()

        self.friendsListWidget = MainLeftWidget()


        self.buttonAdd = AddFriendWidget()
        self.friendsListWidget.leftArea.addNewFriend(self.buttonAdd)

        self.friend1 = FriendsWidget('2','Nikolai Komar')
        self.friendsListWidget.leftArea.addNewFriend(self.friend1)



        dialogs = QtGui.QIcon('img/dialog.png')
        friends = QtGui.QIcon('img/friends.png')
        settings = QtGui.QIcon('img/settings.png')


        self.leftTabWidget.addTab(self.mainLeftWidget, '')
        self.leftTabWidget.setTabIcon(0, dialogs)
        self.leftTabWidget.addTab(self.friendsListWidget, '')
        self.leftTabWidget.setTabIcon(1, friends)
        self.leftTabWidget.addTab(MainLeftWidget(), '')
        self.leftTabWidget.addTab(MainLeftWidget(), '')
        self.leftTabWidget.setTabIcon(3, settings)

        self.leftTabWidget.setIconSize(QSize(150,90))

        leftLayoutMainuserWindow.addWidget(self.leftTabWidget)

        self.searchFriendArea = AreaWidget()
        self.searchFriendArea.setVisible(False)
        rightLayoutMainuserWindow.addWidget(self.searchFriendArea)
        rightLayoutMainuserWindow.addWidget(self.rightWidget)
        #rightLayoutMainuserWindow.addWidget(self.rightWidgetUserInformation)






        #..........Start Button Action.........................
        self.connect(self.buttonAdd, QtCore.SIGNAL('clicked()'), self.addFriendOnListWidget)
        self.connect(self.searchFriendArea.searchButton, QtCore.SIGNAL('clicked()'), self.searchFriends)


        # ..........End Button Action.........................




    def start_main_user_form(self):
        self.setWindowTitle('GoSay')
        self.setStyleSheet('background: #EBEBEB;')
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


        #self.leftWidget.setVisible(self.statusConnection)
        self.leftTabWidget.setVisible(self.statusConnection)
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


    def searchFriends(self):
        self.act.sendSearchFriendsMessage(str(self.searchFriendArea.searchLine.text()))
        print 'search ction.....................'





    def addFriendOnListWidget(self):
        friend = FriendsWidget('2', 'Nikolai Komar')
        self.friendsListWidget.leftArea.addNewFriend(friend)
        self.rightWidget.setVisible(False)
        self.searchFriendArea.setVisible(True)

    def addFriendOnMainLeftWidget(self):
        print 'addFriendOnMainLeftWidget'
        self.friend.setParent(None)
        nweFriend = LeftFriendWidget('admin', 'Nikolai Komar', 0)
        self.mainLeftWidget.leftArea.addNewFriend(nweFriend)
        self.connect(nweFriend, QtCore.SIGNAL('clicked()'), self.addFriendOnMainLeftWidget)

        self.friendList[self.countUser] = nweFriend
        self.countUser  = self.countUser  + 1
        self.mainLeftWidget.leftArea.addNewFriend(self.friend)
        nweFriend.friendLastMessage.setVisible(True)

        self.rightWidget.setVisible(True)
        self.searchFriendArea.setVisible(False)


        print self.friendList

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
            self.inputWidgetForSendMessage.setFocus(True)
        else:
            self.act.send_message(self.inputWidgetForSendMessage.text())

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

            self.messageByMeWidget.widget = self.rightAreaForUserInformation


            self.friendList[self.countUser - 1].messageCountWidget.setVisible(False)
            self.friendList[self.countUser - 1].messageCount = 0


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
        self.testWidge.setMinimumSize(100,100)
        self.testWidge.setMinimumWidth(100)
        self.testWidge.LabelMessageWidget.setStyleSheet(' background-image: url(/home/art/Documents/test.png); background-repeat: no-repeat;')
        #self.testWidge.LabelMessageWidget.setMaximumHeight(200)
        self.layoutForRightArea.addWidget(self.testWidge)
        self.buttonAttachFile.setFocus(False)
        self.inputWidgetForSendMessage.setFocus(True)

    def addMessageFromFriend(self,i):

        self.testWidget = MessageFromFriendWidget()

        self.testWidget.LabelMessageWidget.setText('Process_' + str(i)+ '__' +self.localTime)
        self.layoutForRightArea.addWidget(self.testWidget)

        self.emptF = QtGui.QWidget()
        self.emptF.setMinimumSize(200, 14)
        self.emptF.setStyleSheet('border: none')
        self.layoutForRightArea.addWidget(self.emptF)

        self.friendList[self.countUser-1].setCountMessage(1)

        self.friendList[self.countUser - 1].messageCountWidget.setVisible(True)
        self.friendList[self.countUser - 1].friendLastMessage.setText( str(i)[0:45]+'...')
        self.friendList[self.countUser - 1].statusFriendWidget.setVisible(True)



    def resizeEvent(self, event):
        if(self.width() < 600):
            #self.leftWidget.setVisible(False)
            self.leftTabWidget.setVisible(False)
        if(self.width() > 600):
            #self.leftWidget.setVisible(True)
            self.leftTabWidget.setVisible(True)
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


#if __name__ == '__main.py__':

app = QtGui.QApplication(sys.argv)

main = MainAuthenticationWindow()

main.show()

sys.exit(app.exec_())









# background: url(./lmess.png) no-repeat;
# background:transparent;