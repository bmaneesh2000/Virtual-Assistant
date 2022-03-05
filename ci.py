


from PyQt5 import QtCore, QtGui, QtWidgets
from contact import Ui_MainWindow
from contactent import Ui_MainWindow2


class ci(object):
    def conta(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def contx(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 142)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 191, 141))
        self.pushButton.setStyleSheet("background-color:blue")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("contacts-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.clicked.connect(self.conta)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 0, 181, 141))
        self.pushButton_2.setStyleSheet("background-color:green")
        self.pushButton_2.setText("")
        self.pushButton_2.clicked.connect(self.contx)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Student_Notes-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(120, 120))
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
    ui = ci()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
