from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time


class Worker(QObject):
    finished = pyqtSignal()
    message = pyqtSignal(int)

    @pyqtSlot()
    def process(self):
        print 'START'
        for i in range(10):
            print 'sleep', i
            self.message.emit(i)
            time.sleep(0.5)
        print 'FINISHED'
        self.finished.emit()


class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)
        self.start_btn = QPushButton("Start process", self)
        self.start_btn.clicked.connect(self.start)

        self.setContentsMargins(0,0,0,0)
        layout = QVBoxLayout(self)

        layout.addWidget(self.start_btn)
        layout.setContentsMargins(0,0,0,0)

        #self.setMaximumSize(320,300)
        self.setMinimumSize(320,300)

        self.maintabWidget = QTabWidget()
        self.maintabWidget.setTabPosition(1)


        self.tabWidget = QTabWidget()

        self.tabWidget.setTabPosition(2)


        self.window1 = QWidget()
        self.window2 = QWidget()
        self.window3 = QWidget()
        self.window4 = QWidget()

        self.style = """QTabWidget::pane { /* The tab widget frame */
                            border: 1px solid #111111;


                        }
                        QTabBar::tab:selected, QTabBar::tab:hover {
                            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                        stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                                        stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
                        }

                        QTabWidget::tab-bar{
                        alignment: left;
                        padding: 0px;
                        width: 280px;
                        height: 280px;
                        border: 4px solid #444444;
                        position: absolute;
                            bottom: -10em;
                        }
                        """



        self.tabWidget.addTab(self.window1,'1')
        self.tabWidget.addTab(self.window2,'2')
        self.tabWidget.addTab(self.window3,'3')
        self.tabWidget.addTab(self.window4,'4')

        self.w2 = QWidget()

        self.maintabWidget.addTab(self.tabWidget,'ogo')
        self.maintabWidget.addTab(self.w2,'w2')
        self.maintabWidget.setStyleSheet(self.style)





        self.tabWidget.setStyleSheet(self.style)

        layout.addWidget(self.maintabWidget)

        self.inputLine = QLineEdit()
        self.inputLine.setStyleSheet('background: #FBFBFB;')
        self.inputLine.setMinimumSize(200,60)
        self.inputLine.setMaximumWidth(300)
        layout.addWidget(self.inputLine)







    def start(self):
        self.thread = QThread(self)
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.message.connect(self.text)
        self.thread.start()

    def text(self, i):
        self.start_btn.setText('Process ' + str(i))


app = QApplication([])
widget = MyWidget()
widget.show()
app.exec_()