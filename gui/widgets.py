from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QCursor
import threading
import time

import sys
sys.path.insert(0, "/home/art/PycharmProjects/prgosay/actions/")
import action

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














class EmptyBoxWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMinimumHeight(65)
        self.setMinimumWidth(300)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('color: #ffffff; border: none; background: #ffffff; padding: 0px')



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
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(310, 70)
        self.setMaximumSize(310, 70)
        self.setContentsMargins(10, 0, 5, 0)
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
        self.logo.setMinimumSize(56, 56)
        self.logo.setMaximumSize(56, 56)
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
        #self.friendLastMessage.setVisible(False)
        self.friendLastMessage.setStyleSheet('border: none; font-size: 12px; color: #696969;')
        self.friendNameAndMessageLayout.addWidget(self.friendNameAndStatus)
        self.friendNameAndMessageLayout.addWidget(self.friendLastMessage)

        self.contentLaout.addWidget(self.friendNameAndMessage)

        self.messageCountWidget = QtGui.QLabel(str(self.messageCount))
        self.messageCountWidget.setVisible(False)
        self.messageCountWidget.setMinimumSize(22, 22)
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

    #def mousePressEvent(self, event):


    def setCountMessage(self, count):
        self.messageCount = self.messageCount + count
        if self.messageCount > 99:
            self.messageCountWidget.setText('99+')
            self.messageCountWidget.setMinimumSize(28, 22)
        else:
            self.messageCountWidget.setText(str(self.messageCount))
            self.messageCountWidget.setMinimumSize(22, 22)

    def getCountMessage(self, count):
        return self.messageCountWidget.text()


class FriendsWidget(QtGui.QPushButton):
    def __init__(self, friendUID, friendName, login,parent=None, ):
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(310, 50)
        self.setMaximumSize(310, 50)
        self.setContentsMargins(8, 0, 8, 0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        # /  left /   top  /   right /  bottom  /
        self.defoltStyle = '''background: #ffffff; border: none;'''
        self.hoverStyle = '''background: #F3F5F5; border: none;'''
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

        self.friendUID = friendUID
        self.friendName = friendName
        self.login = login
        self.friendID = '1'

        self.logo = QtGui.QLabel()
        self.logo.setMinimumSize(40, 40)
        self.logo.setMaximumSize(40, 40)
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
        self.settingsFriendWidget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
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
        self.setStyleSheet(self.hoverStyle)

    def leaveEvent(self, event):
        self.setStyleSheet(self.defoltStyle)



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
        self.setStyleSheet('background: #F3F5F5; border: none;')

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
        self.layoutForMainContainer = VLayout()
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
        self.searchWidgetContainer.setAlignment(QtCore.Qt.AlignLeft)
        self.searchWidget.setLayout(self.searchWidgetContainer)
        self.headerContainer.addWidget(self.searchWidget)

        self.searchLine = QtGui.QLineEdit()
        self.searchLine.setMinimumSize(120, 42)
        self.searchLine.setMaximumSize(380, 42)
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
        self.searchWidgetContainer.addWidget(self.searchButton)

        self.layoutForMainContainer.addWidget(self.header)

        self.widgetForSearchedFriends = QtGui.QWidget()
        self.layoutForSearchedFriends = QtGui.QGridLayout()
        self.layoutForSearchedFriends.setSpacing(10)

        self.widgetForSearchedFriends.setLayout(self.layoutForSearchedFriends)
        self.layoutForMainContainer.addWidget(self.widgetForSearchedFriends)


class LeftButtonMyFriends(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(60, 40)
        self.setMaximumSize(60, 40)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('background: #EBEBEB; border: none;')


class LeftButtonAddFriend(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMinimumSize(60, 40)
        self.setMaximumSize(60, 40)
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

    def addWidgetInLeftArea(self, logoImg, friendName, login):
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

        self.setContentsMargins(0, 0, 0, 0)
        self.setUsesScrollButtons(False)


class AddFriendFromSearchedFriends(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setMinimumSize(32, 32)
        self.setMaximumSize(32, 32)
        self.defoltStyle = '''font-size: 24px; color: #548B28;
                           border: 1px solid #548B28; padding: 0px;
                           border-radius: 16px;'''
        self.setStyleSheet(self.defoltStyle)

    def enterEvent(self, event):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('font-size: 24px; color: #548B28;'
                           'border: 2px solid #548B28; padding: 0px;'
                           'border-radius: 16px;')

    def leaveEvent(self, event):
        self.setStyleSheet(self.defoltStyle)



class SearchedFriendWidget(QtGui.QWidget):
    def __init__(self, firstName, lastName, status, city, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMinimumSize(100, 110)
        # self.setMaximumSize(70, 70)
        self.setContentsMargins(0, 0, 0, 0)
        # self.setFocusPolicy(QtCore.Qt.NoFocus)
        # /  left /   top  /   right /  bottom  /

        self.firstName = firstName
        self.lastName = lastName
        self.status = status
        self.city = city

        self.defoltStyle = '''background: #ffffff; border: none; padding: 0px;'''
        self.setStyleSheet(self.defoltStyle)
        self.mainContainer = HLayout()
        self.mainContainer.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.mainContainer)

        self.avatarUserWidget = QtGui.QLabel(firstName[0])
        self.avatarUserWidget.setMinimumSize(98, 98)
        self.avatarUserWidget.setMaximumSize(98, 98)
        self.avatarUserWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.avatarUserWidget.setStyleSheet('background: #0092D0; font-size: 63px;color: #ffffff; '
                                            'border-radius: 49px;')

        self.subContainerForInfAboutUserAndButtonAdd = VLayout()
        self.subContainerForInfAboutUserAndButtonAdd.setAlignment(QtCore.Qt.AlignTop)
        self.informationAboutUserWidget = QtGui.QLabel()
        self.informationAboutUserWidget.setStyleSheet('padding-left: 10px;')
        self.informationAboutUserWidget.setAlignment(QtCore.Qt.AlignLeft)
        self.informationAboutUserWidget.setMinimumSize(170, 98)
        self.informationAboutUserWidget.setMaximumSize(170, 98)
        self.informationAboutUserWidget.setLayout(self.subContainerForInfAboutUserAndButtonAdd)

        self.mainContainer.addWidget(self.avatarUserWidget)
        self.mainContainer.addWidget(self.informationAboutUserWidget)

        self.userName = QtGui.QLabel(self.lastName + ' ' + self.firstName)
        self.userName.setStyleSheet('border: 0px solid #222222; border: none; padding: 0px;'
                                    'font-size: 18px; color: #282828;')

        self.statusUser = QtGui.QLabel(self.status)
        self.statusUser.setAlignment(QtCore.Qt.AlignTop)

        if self.status == 'Online':
            self.statusUser.setStyleSheet('padding: 0px;'
                                          'qproperty-alignment: AlignLeft;'
                                          'font-size: 13px; color: #579E1C;')
        else:
            self.statusUser.setStyleSheet('padding: 0px; '
                                          'qproperty-alignment: AlignLeft;'
                                          'font-size: 13px; color: #696969;')

        self.userCity = QtGui.QLabel(self.city)
        self.userCity.setAlignment(QtCore.Qt.AlignVCenter)
        self.userCity.setMinimumHeight(30)
        self.userCity.setStyleSheet('padding: 0px; '
                                    'font-size: 14px; color: #3c3c3c;')

        self.addFriendButton = AddFriendFromSearchedFriends('+')

        self.subContainerForInfAboutUserAndButtonAdd.addWidget(self.userName)
        self.subContainerForInfAboutUserAndButtonAdd.addWidget(self.statusUser)
        self.subContainerForInfAboutUserAndButtonAdd.addWidget(self.userCity)
        self.subContainerForInfAboutUserAndButtonAdd.addWidget(self.addFriendButton)

class NoSuchUserWidget(QtGui.QLabel):
    def __init__(self, parent = None):
        QtGui.QLabel.__init__(self, parent)
        self.setVisible(False)
        self.setMinimumHeight(120)
        self.setStyleSheet('font-size: 18px; color: #282828;'
                           'padding: 0px;')


class FriendSettingsWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setMinimumSize(30, 30)
        self.setMaximumSize(30, 30)
        self.setStyleSheet("""QPushButton:hover {
                             background: url(./img/button_more_hover.png);
                             padding: 0px;
                            }

                            QPushButton {
                            background: url(./img/button_more.png);
                            color: #ffffff;
                            border: none;
                            }""")







