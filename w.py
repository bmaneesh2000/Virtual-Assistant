from PyQt5 import QtCore, QtGui, QtWidgets
import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
from PyQt5.QtWidgets import QMessageBox
class Ui_MainWindow1(object):


    def search_wiki(self):
        try:
            search=self.textEdit.toPlainText()
            answer=wikipedia.summary(search)
            msg = QMessageBox()
            msg.setWindowTitle("wiki daww")
            msg.setText(answer)
            x = msg.exec_() 
        except:
            msg = QMessageBox()
            msg.setWindowTitle("wiki daww")
            msg.setText('error')
            x = msg.exec_() 

    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow")
        MainWindow1.resize(380, 451)
        MainWindow1.setMinimumSize(QtCore.QSize(380, 451))
        MainWindow1.setMaximumSize(QtCore.QSize(380, 451))
        MainWindow1.setAutoFillBackground(False)
        MainWindow1.setStyleSheet("background-color:silver;")
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 310, 261, 41))
        self.textEdit.setStyleSheet("background-color:white;")
        self.textEdit.setObjectName("textEdit")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(280, 310, 75, 41))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.search_wiki)
        
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 100, 191, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("768px-Wikipedia_Logo_1.0.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit.setText(_translate("MainWindow", "submit"))
        self.label_2.setText(_translate("MainWindow", "      WIKI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
