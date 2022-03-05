import datetime

x = datetime.datetime.now()
print(x)
import requests, json 
  

api_key = "b6907d289e10d714a6e88b30761fae22"
  
 
base_url = "https://samples.openweathermap.org/data/2.5/weather?q="
  

city_name = "chennai"

  

complete_url = base_url + city_name  +"&appid=b6907d289e10d714a6e88b30761fae22"
  
response = requests.get(complete_url) 
  

x = response.json() 
  

if x["cod"] != "404": 
  

    y = x["main"] 
  
  
    current_temperature = y["temp"] 

    current_pressure = y["pressure"] 
  
   
    current_humidiy = y["humidity"] 
  
    
    z = x["weather"] 
  
  
    weather_description = z[0]["description"] 
  
    
  
else: 
    print(" City Not Found ")

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 355)
        MainWindow.setStyleSheet("background-color:pink")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 10, 321, 191))
        self.calendarWidget.setStyleSheet("background-color:silver")
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 220, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 250, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "current temprature is :-"+str(current_temperature)))
        self.label_2.setText(_translate("MainWindow", "atmospheric pressure :-"+str(current_pressure)))
        self.label_3.setText(_translate("MainWindow", "current humidiy :-"+str(current_humidiy)))
        self.label_4.setText(_translate("MainWindow", "weather description:-"+str(weather_description)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
