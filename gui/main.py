# -*- coding: utf-8 -*-

import sys

from time import strftime

from widgets import *
import cPickle as pickle

sys.path.insert(0, "/home/art/PycharmProjects/prgosay/actions/")
import action


# .....................Build Application........................................


from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Worker(QObject):
    finished = pyqtSignal()
    message = pyqtSignal(str)
    messageCortage = pyqtSignal(list)
    obj = ''

    @pyqtSlot()
    def process(self):
        while True:
            print 'START'
            mess = self.obj.whileReceive()
            print 'dannie from sock ',mess
            if mess == None:
                print 'none'
            elif type(mess) == list:
                self.messageCortage.emit(mess)
            else:
                self.message.emit(str(mess))

        self.finished.emit()









class MainAuthenticationWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.myFriendsList = {}
        self.friendList = {}
        self.searchedFriendListInformation = {}
        self.searchedFriendListObjects = {}

        self.bGroupMyFriends = QtGui.QButtonGroup()

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

        class buttonAddFriendFromSearchedFriends(AddFriendFromSearchedFriends):
            def mousePressEvent(parent, event):
                self.addNewFriendInFriendsList()

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
        layoutForWidgetsRightHeader.setAlignment(QtCore.Qt.AlignVCenter)
        subLauoytForInformationAboutSelectedFriend = VLayout()
        subLauoytForInformationAboutSelectedFriend.setContentsMargins(15,0,0,0)

        self.subLauoytForSettingsSelectedFriend = HLayout()
        self.subLauoytForSettingsSelectedFriend.setContentsMargins(0, 0, 5, 0)

        self.rightHeader.setLayout(layoutForWidgetsRightHeader)

        self.rightHeader.setMinimumSize(400, 60)
        self.rightHeader.setMaximumSize(1000, 60)
        self.rightHeader.setStyleSheet('border:none; padding: 0px;'
                                       ' border-bottom: 1px solid #D6D6D6; background: #fdfcfc;')


        self.labelNameSelectedUserReightHeader = QtGui.QLabel()
        self.labelNameSelectedUserReightHeader.setAlignment(QtCore.Qt.AlignLeft)
        self.labelNameSelectedUserReightHeader.setContentsMargins(0,0,0,5)
        self.labelNameSelectedUserReightHeader.setStyleSheet('font-size: 18px; color: #282828;'
                                                             'border:none; qproperty-alignment: AlignLeft;')

        self.statusSelectedUser = QtGui.QLabel()
        self.statusSelectedUser.setAlignment(QtCore.Qt.AlignLeft)
        self.statusSelectedUser.setStyleSheet(' border: none; padding: 0px;'
                                      'qproperty-alignment: AlignLeft;'
                                      'font-size: 14px; color: #696969;')

        layoutForWidgetsRightHeader.addLayout(subLauoytForInformationAboutSelectedFriend)
        layoutForWidgetsRightHeader.addLayout(self.subLauoytForSettingsSelectedFriend)
        subLauoytForInformationAboutSelectedFriend.addWidget(self.labelNameSelectedUserReightHeader)
        subLauoytForInformationAboutSelectedFriend.addWidget(self.statusSelectedUser)

        self.btnFriendSettings = FriendSettingsWidget()
        self.subLauoytForSettingsSelectedFriend.addWidget(self.btnFriendSettings)


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
        self.connect(self.buttonAdd, QtCore.SIGNAL('clicked()'), self.addFriendThroughSearchAndVisibleSearchArea)
        #self.connect(self.buttonAdd, QtCore.SIGNAL('clicked()'), self.addNewFriendOnListWidget)
        self.connect(self.searchFriendArea.searchButton, QtCore.SIGNAL('clicked()'), self.searchFriends)

        self.labelNoSuchUser = NoSuchUserWidget('Sorry, no such user.')
        self.searchFriendArea.layoutForSearchedFriends.addWidget(self.labelNoSuchUser, 0, 0)
        self.btnGroupMyFriendsList = QtGui.QButtonGroup()
        self.connect(self.btnGroupMyFriendsList, QtCore.SIGNAL('buttonClicked(int)'),self.mousePressOnFriendFromFriendsList)

        self.btnGroupMyFriendsSettings = QtGui.QButtonGroup()
        self.connect(self.btnGroupMyFriendsSettings, QtCore.SIGNAL('buttonClicked(int)'),self.selectSettingForFriend)
        self.uidDeletingOrClearDialogFriend = 0
        self.uidCurrentFriendForDialogue = 0

        self.connect(self.btnFriendSettings, QtCore.SIGNAL('clicked()'), self.settingsFriend)
        self.statusRestoredData = False


        self.bGroupSearchedFriends = QtGui.QButtonGroup()
        self.connect(self.bGroupSearchedFriends, QtCore.SIGNAL('buttonClicked(int)'), self.addNewFriendInFriendsList)

        # ..........End Button Action.........................
        self.selectedFriendForChatWidget = QtGui.QPushButton()
        self.selectedFriendForChatWidgetInformation = []



    def start_main_user_form(self):
        self.setWindowTitle('GoSay')
        self.setStyleSheet('background: #EBEBEB;')
        self.setMinimumSize(400, 450)
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

        #self.labelNameUserReightHeader.setText(self.inputLineForLoginUser.text())

        self.statres = True
        self.restoreData()

    def start(self):
        self.thread = QThread(self)
        self.worker = Worker()
        self.worker.obj = self.act
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        #self.worker.message.connect(self.addMessageFromFriend)
        self.worker.message.connect(self.processingMessage)
        self.worker.messageCortage.connect(self.processingMessage)
        self.thread.start()




    def addFriendOnMainLeftWidget(self):
        print 'addFriendOnMainLeftWidget'
        self.friend.setParent(None)
        newFriend = LeftFriendWidget('admin', 'Nikolai Komar', 0)
        self.mainLeftWidget.leftArea.addNewFriend(newFriend)
        self.connect(newFriend, QtCore.SIGNAL('clicked()'), self.addFriendOnMainLeftWidget)

        self.friendList[self.countUser] = newFriend
        self.countUser  = self.countUser  + 1
        self.mainLeftWidget.leftArea.addNewFriend(self.friend)
        newFriend.friendLastMessage.setVisible(True)

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




    def addFriendThroughSearchAndVisibleSearchArea(self):
        self.rightWidget.setVisible(False)
        self.searchFriendArea.setVisible(True)

    def searchFriends(self):
        self.act.sendSearchFriendsMessage(str(self.searchFriendArea.searchLine.text()))
        print '..........search action.....................'

    def clearSearchArea(self):
        for uid in self.searchedFriendListObjects:
            searchedFriend = self.searchedFriendListObjects[uid]
            searchedFriend.setVisible(False)
            self.labelNoSuchUser.setVisible(False)
            del searchedFriend

    def displayFoundFriends(self, mess):
        k = 0
        j = 0
        self.clearSearchArea()

        for i in mess:
            print mess[i]
            friend = mess[i]
            uid = int(friend[0])
            searchedFriend = SearchedFriendWidget(str(friend[2]), str(friend[3]),str(friend[5]),str(friend[6]))
            self.searchedFriendListInformation[int(friend[0])] = friend
            self.searchedFriendListObjects[uid] = searchedFriend
            if j != 2:
                self.searchFriendArea.layoutForSearchedFriends.addWidget(searchedFriend, k, j)
                self.bGroupSearchedFriends.addButton(searchedFriend.addFriendButton, uid)
                btnVisible = uid in self.myFriendsList
                if btnVisible == True:
                    btn = self.searchedFriendListObjects[uid]
                    btn.addFriendButton.setVisible(False)
                j = j + 1
            else:
                k = k + 1
                j = 0
                self.searchFriendArea.layoutForSearchedFriends.addWidget(searchedFriend, k, j)
                self.bGroupSearchedFriends.addButton(searchedFriend.addFriendButton, uid)
                btnVisible = uid in self.myFriendsList
                if btnVisible == True:
                    btn = self.searchedFriendListObjects[uid]
                    btn.addFriendButton.setVisible(False)


    def processingMessage(self, mess):
        if mess[0] == '9' and mess[1] != False:
            self.displayFoundFriends(mess[1])
        else:
            print 'no such user'
            self.clearSearchArea()
            self.labelNoSuchUser.setVisible(True)


    def addNewFriendInFriendsList(self, uid):
        infromationAboutFriend = self.searchedFriendListInformation[uid]
        uid = int(infromationAboutFriend[0])

        key_exists = uid in self.myFriendsList
        if key_exists == False:
            self.myFriendsList[uid] = infromationAboutFriend
            friendName = str(infromationAboutFriend[2]) + ' ' + str(infromationAboutFriend[3])
            newFriend = FriendsWidget(uid, friendName)
            self.selectedFriendForChatWidget = newFriend
            if str(infromationAboutFriend[5]) == 'Online':
                newFriend.statusFriendWidget.setVisible(True)

            self.friendsListWidget.leftArea.addNewFriend(newFriend)
            self.btnGroupMyFriendsList.addButton(newFriend, uid)
            self.btnGroupMyFriendsSettings.addButton(newFriend.settingsFriendWidget, uid)
            btn = self.searchedFriendListObjects[uid]
            btn.addFriendButton.setVisible(False)

            self.saveData()
        else:
            print 'this user exist!'
            QtGui.QMessageBox.about(self, "Warning","Friend take exist!")





    def showMessageBox(self, question):
        result = QMessageBox.question(self, 'Warning', question, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            return True
        else:
            return False

    def deleteFriendByUID(self):
        print 'deleteFriendFromMyFriends with uid ', self.uidDeletingOrClearDialogFriend
        if 0 != self.uidCurrentFriendForDialogue or 0 != self.uidDeletingOrClearDialogFriend:
            statusDelete = True
            result = self.showMessageBox('Do you really want to delete this friend?')
        else:
            statusDelete = False


        if statusDelete == False:
            QMessageBox.critical(self, "Message", "Friend was deleted!")

        elif statusDelete == True and result == True:
            btnFriend = self.btnGroupMyFriendsList.button(self.uidDeletingOrClearDialogFriend)
            btnFriendSettings = self.btnGroupMyFriendsSettings.button(self.uidDeletingOrClearDialogFriend)

            self.btnGroupMyFriendsList.removeButton(btnFriend)
            self.btnGroupMyFriendsSettings.removeButton(btnFriendSettings)
            btnFriendSettings.setVisible(False)
            btnFriend.setVisible(False)
            del self.myFriendsList[self.uidDeletingOrClearDialogFriend]
            del btnFriendSettings
            del btnFriend
            self.uidDeletingOrClearDialogFriend = 0
            self.uidCurrentFriendForDialogue = 0

        else:
            print 'Refusal of action'
        self.saveData()

    def clearDialogFriendByUID(self):
        print 'clearDialogFriendByUID', self.uidDeletingOrClearDialogFriend
        result = self.showMessageBox('Do you really want to clear this dialog?')
        if result == True:
            print 'ok'
        else:
            print 'Refusal of action'

    def deleteConversationFriendByUID(self):
        print 'deleteDialogFriendByUID', self.uidDeletingOrClearDialogFriend
        result = self.showMessageBox('Do you really want to delete this dialog?')
        if result == True:
            print 'ok'
        else:
            print 'Refusal of action'

    def settingsFriend(self):
        print self.uidCurrentFriendForDialogue
        self.selectSettingForFriend(self.uidCurrentFriendForDialogue)

    def selectSettingForFriend(self, uid):
        print 'press btn Friend ' , uid
        self.uidDeletingOrClearDialogFriend = uid
        menu = QtGui.QMenu()
        menu.addAction(self.tr('View profile'), self.deleteConversationFriendByUID)
        menu.addAction(self.tr('Clear dialog'), self.clearDialogFriendByUID)
        menu.addAction(self.tr('Delete conversation'), self.deleteConversationFriendByUID)
        menu.addAction(self.tr('Delete friend'), self.deleteFriendByUID)
        menu.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        menu.setStyleSheet('''QMenu {
                                background: #ffffff;
                                font-size: 10px
                                color: #696969
                                border-radius: 10px;}
                              QMenu::item:selected {
                                background-color: #D0DCDC;
                                font-size: 10px
                                color: #696969
                                border-radius: 10px;}''')

        menu.exec_(QtGui.QCursor.pos())



    def mousePressOnFriendFromFriendsList(self, uid):
        print 'press on friend with uid', uid
        print self.myFriendsList[uid]
        self.uidCurrentFriendForDialogue = uid
        self.uidDeletingOrClearDialogFriend = uid
        informationAboutFriend = self.myFriendsList[uid]
        self.rightWidget.setVisible(True)
        self.searchFriendArea.setVisible(False)
        pressButton = self.btnGroupMyFriendsList.button(uid)


        self.labelNameSelectedUserReightHeader.setText(str(informationAboutFriend[2]) + ' ' + str(informationAboutFriend[3]))
        self.statusSelectedUser.setText(str(informationAboutFriend[5]))
        if str(informationAboutFriend[5]) == 'Online':
            self.statusSelectedUser.setStyleSheet('border: none; padding: 0px;'
                                                  'qproperty-alignment: AlignLeft;'
                                                  'font-size: 14px; color: #579E1C;')
        else:
            self.statusSelectedUser.setStyleSheet('border: none; padding: 0px;'
                                                  'qproperty-alignment: AlignLeft;'
                                                  'font-size: 14px; color: #696969;')


        pressedStyleButton = 'background: #EBEDED; border: none;'
        defoltStyleButton = 'background: #ffffff; border: none;'
        hoverStyleButton = 'background: #F3F5F5; border: none;'
        for id in self.myFriendsList:
            if id == uid:
                pressButton.setStyleSheet(pressedStyleButton)
                pressButton.defoltStyle = pressedStyleButton
                pressButton.hoverStyle = pressedStyleButton
            else:
                otherButton = self.btnGroupMyFriendsList.button(id)
                otherButton.setStyleSheet(defoltStyleButton)
                otherButton.defoltStyle = defoltStyleButton
                otherButton.hoverStyle = hoverStyleButton

    def saveData(self):
        print 'save Data ....'
        output = open('data/data.pkl', 'wb')
        pickle.dump(self.myFriendsList, output, 2)
        output.close()


    def restoreData(self):
        self.statusRestoredData = True
        print 'restore Data ....'
        input = open('data/data.pkl', 'rb')
        myFriendsList = pickle.load(input)
        input.close()
        for friend in myFriendsList:
            print friend
            information =  myFriendsList[friend]
            uid = int(information[0])
            friendName = str(information[2]) + ' ' + str(information[3])
            newFriend = FriendsWidget(uid, friendName)
            self.selectedFriendForChatWidget = newFriend
            if str(information[5]) == 'Online':
                newFriend.statusFriendWidget.setVisible(True)

            self.friendsListWidget.leftArea.addNewFriend(newFriend)
            self.btnGroupMyFriendsList.addButton(newFriend, uid)
            self.btnGroupMyFriendsSettings.addButton(newFriend.settingsFriendWidget, uid)



        self.statusRestoredData = False
        self.myFriendsList = myFriendsList
        self.saveData()


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
            self.restoreData()

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