


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


class Ui_MainWindow4(object):
    def goog(self):
        i=self.textEdit.toPlainText()
        webbrowser.get(chrome_path).open("https://www.google.com/search?q="+i)
    def yt(self):
        i=self.textEdit.toPlainText()
        webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query="+i)
    def dd(self):
        i=self.textEdit.toPlainText()
        webbrowser.get(chrome_path).open(i)
    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(356, 410)
        MainWindow4.setStyleSheet("background-color:navy")
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:green; color:white")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goog)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 320, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:red; color:white;")
        self.pushButton_2.clicked.connect(self.yt)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 320, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:gold;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.dd)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 141, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("sea.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 260, 241, 31))
        self.textEdit.setStyleSheet("background-color:white;")
        self.textEdit.setObjectName("textEdit")
        MainWindow4.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "MainWindow"))
        self.label.setText(_translate("MainWindow4", "search :-"))
        self.pushButton.setText(_translate("MainWindow4", "Google"))
        self.pushButton_2.setText(_translate("MainWindow4", "YouTube"))
        self.pushButton_3.setText(_translate("MainWindow4", "Direct"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow4 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow4)
    MainWindow4.show()
    sys.exit(app.exec_())
