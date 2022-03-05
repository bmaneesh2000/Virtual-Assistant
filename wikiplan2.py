
from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3 
import playsound
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

import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo



class wiki_spech(object):
    def voiceds(self):
        engine = pyttsx3.init() 
        search=get_audio()
        if search != "cant hear you":
            import requests
            from bs4 import BeautifulSoup
            i=search
            url="https://en.wikipedia.org/wiki/"+i
            r=requests.get(url) 
            c=r.content
            s=BeautifulSoup(c,'html.parser')
            f=s.find("p", class_=False, id=False)
            engine.say(f.text)
        else:
            engine.say(search) 
        engine.runAndWait() 
        engine.stop()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 451)
        MainWindow.setMinimumSize(QtCore.QSize(380, 451))
        MainWindow.setMaximumSize(QtCore.QSize(380, 451))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:silver;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(140, 340, 81, 41))
        self.submit.setStyleSheet("background-color:gold;")
        self.submit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voice-45-470369 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit.setIcon(icon)
        self.submit.setIconSize(QtCore.QSize(45, 45))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.voiceds)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "      WIKI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wiki_spech()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
