from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
from interwiki import wiki_intermediate
from mailinter import mail_inter
from mal import Ui_MainWindow3
from brou import Ui_MainWindow4
from wea import Ui_MainWindow2
from notesinter import notesinter
from ci import ci
from tinter import tinter
from PyQt5.QtWidgets import QMessageBox

import speech_recognition as sr
from gtts import gTTS
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
    try:
        said = r.recognize_google(audio,language ='en-US')
        print(said)
    except Exception as e:
        return "cant hear you"

    return said
class Ui_MainWindow(object):
    def voicedaww(self):
        ss=get_audio()
        if ss=="Wiki":
            self.open_wiki()
        elif ss=="status":
            self.open_stat()
        elif ss=="translator":
            self.tinter()
        elif ss=="message":
            self.sms()
        elif ss=="notes":
            self.notesinterr()
        elif ss=="search":
            self.op_bro()
        elif ss=="contact":
            self.coi()
        elif ss=="mail":
            self.emai_sen()
        elif ss=="music":
            self.muts()


            

    def pp(self):
        msg = QMessageBox()
        msg.setWindowTitle("credits")
        msg.setText("By B.maneesh kumar \n B.S Maneesh \n K.Uma Sudan")
        x = msg.exec_() 
    def mus(self):
        from mus import muss
        self.window=QtWidgets.QMainWindow()
        self.ui=muss()
        self.ui.setupUi(self.window)
        self.window.show()
    def sms(self):
        from sms import smss
        self.window=QtWidgets.QMainWindow()
        self.ui=smss()
        self.ui.setupUi(self.window)
        self.window.show()
    def tinter(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=tinter()
        self.ui.setupUi(self.window)
        self.window.show()

    def notesinterr(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=notesinter()
        self.ui.setupUi(self.window)
        self.window.show()
    def interbot(self):
        from interbot import cbtxt
        self.window=QtWidgets.QMainWindow()
        self.ui=cbtxt()
        self.ui.setupUi(self.window)
        self.window.show()

    def notesinterr(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=notesinter()
        self.ui.setupUi(self.window)
        self.window.show()
    def coi(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=ci()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_wiki(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=wiki_intermediate()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_stat(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
    def emai_sen(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=mail_inter()
        self.ui.setupUi(self.window)
        self.window.show()
    def op_bro(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow4()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(471, 350)
        MainWindow.setMinimumSize(QtCore.QSize(471, 350))
        MainWindow.setMaximumSize(QtCore.QSize(471, 350))
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#C0C0C0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 101, 81))
        self.pushButton.setStyleSheet("background-color:lightgreen;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Asset_3-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sms)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 101, 151))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: navy;")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("email-western-libraries-12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.emai_sen)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 101, 101))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color:    #F4A460;")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Weather+Targeting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open_stat)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 0, 141, 81))
        self.pushButton_4.setStyleSheet("background-color:\"#9370DB\";")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("search--v2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.op_bro)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 0, 91, 81))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color:white;")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("768px-Wikipedia_Logo_1.0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.open_wiki)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 80, 91, 151))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color:skyblue;")
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Significon-Translation-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.tinter)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 230, 131, 101))
        self.pushButton_7.setAutoFillBackground(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("contacts-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.clicked.connect(self.coi)
        self.pushButton_7.setIconSize(QtCore.QSize(70, 120))
        self.pushButton_7.setStyleSheet("background-color:    #008080;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.clicked.connect(self.pp)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 290, 91, 41))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("background-color:    #FF6347")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 150, 261, 71))
        self.textEdit.setStyleSheet("background-color:white;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 90, 81, 51))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pngtree-vector-microphone-icon-png-image_695750.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.clicked.connect(self.voicedaww)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 0, 141, 81))
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("14134081Untitled-3-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon55)
        self.pushButton_10.clicked.connect(self.interbot)
        self.pushButton_10.setIconSize(QtCore.QSize(70, 120))
        self.pushButton_10.setStyleSheet("background-color: #00FF00   ;")
        self.pushButton_10.setText("")
        
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(230, 230, 151, 101))
        self.pushButton_11.setStyleSheet("background-color: blue;")
        self.pushButton_11.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Student_Notes-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.clicked.connect(self.notesinterr)
        self.pushButton_11.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(380, 230, 91, 61))
        self.pushButton_12.setStyleSheet("background-color: pink;")
        self.pushButton_12.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_12.clicked.connect(self.mus)
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_8.setText(_translate("MainWindow", "Credits"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">VIRTUAL ASSISTANT USING NATURAL LANGUAGE PROCESSING</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
