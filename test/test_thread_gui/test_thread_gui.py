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

        layout = QVBoxLayout(self)
        layout.addWidget(self.start_btn)
        self.resize(250, 150)

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