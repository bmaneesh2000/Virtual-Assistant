


from PyQt5 import QtCore, QtGui, QtWidgets
from chatbottxt import chatbot_txt
from chatbotvoice import Ui_MainWindow

class cbtxt(object):
    def cbtxt(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=chatbot_txt()
        self.ui.setupUi(self.window)
        self.window.show()
    def cbvoice(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 149)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 171, 151))
        self.pushButton.setStyleSheet("background-color:skyblue;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("29076.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(130, 130))
        self.pushButton.setCheckable(False)
        self.pushButton.clicked.connect(self.cbtxt)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 0, 181, 151))
        self.pushButton_2.setStyleSheet("background-color:lightgreen;")
        self.pushButton_2.setText("")
        self.pushButton_2.clicked.connect(self.cbvoice)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("voice-45-470369 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = cbtxt()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
