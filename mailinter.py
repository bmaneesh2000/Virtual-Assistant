

from PyQt5 import QtCore, QtGui, QtWidgets
from mal import Ui_MainWindow3
from specmail import Ui_mailspeech

class mail_inter(object):
    def emai_sen(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()
    def emai_voi(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_mailspeech()
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.emai_sen)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 0, 181, 151))
        self.pushButton_2.setStyleSheet("background-color:lightgreen;")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("voice-45-470369 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.clicked.connect(self.emai_voi)
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
    ui = mail_inter()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
