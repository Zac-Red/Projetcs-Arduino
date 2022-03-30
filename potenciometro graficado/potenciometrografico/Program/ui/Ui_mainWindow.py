# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\myPY\Gauge_test1\ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 302)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Pi4IoT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lbltime = QtWidgets.QLineEdit(self.centralWidget)
        self.lbltime.setGeometry(QtCore.QRect(10, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbltime.setFont(font)
        self.lbltime.setStyleSheet("background-color: rgb(200,200,200);\n"
"")
        self.lbltime.setText("")
        self.lbltime.setFrame(False)
        self.lbltime.setAlignment(QtCore.Qt.AlignCenter)
        self.lbltime.setReadOnly(True)
        self.lbltime.setObjectName("lbltime")
        self.label_20 = QtWidgets.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.btnExit = QtWidgets.QPushButton(self.centralWidget)
        self.btnExit.setGeometry(QtCore.QRect(290, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btnExit.setObjectName("btnExit")
        self.Grafik = QtWidgets.QGraphicsView(self.centralWidget)
        self.Grafik.setGeometry(QtCore.QRect(180, 20, 200, 200))
        self.Grafik.setAutoFillBackground(True)
        self.Grafik.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.Grafik.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Grafik.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Grafik.setLineWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.Grafik.setBackgroundBrush(brush)
        self.Grafik.setObjectName("Grafik")
        self.lblStatusLedUNORS232 = QtWidgets.QLabel(self.centralWidget)
        self.lblStatusLedUNORS232.setGeometry(QtCore.QRect(150, 180, 21, 21))
        self.lblStatusLedUNORS232.setText("")
        self.lblStatusLedUNORS232.setPixmap(QtGui.QPixmap("../../../MyPyProjekte/Gauge/ui/icons/led-red-on.png"))
        self.lblStatusLedUNORS232.setScaledContents(True)
        self.lblStatusLedUNORS232.setObjectName("lblStatusLedUNORS232")
        self.lblRSinfo = QtWidgets.QLabel(self.centralWidget)
        self.lblRSinfo.setGeometry(QtCore.QRect(20, 180, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lblRSinfo.setFont(font)
        self.lblRSinfo.setObjectName("lblRSinfo")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(250, 180, 61, 20))
        self.label.setStyleSheet("color: rgb(244, 244, 244);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lblAnzeige = QtWidgets.QLabel(self.centralWidget)
        self.lblAnzeige.setGeometry(QtCore.QRect(250, 160, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblAnzeige.setFont(font)
        self.lblAnzeige.setStyleSheet("color: rgb(250, 250, 250);")
        self.lblAnzeige.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAnzeige.setObjectName("lblAnzeige")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gauge & Arduino & RS232"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>Time:</p></body></html>"))
        self.btnExit.setText(_translate("MainWindow", "EXIT"))
        self.lblRSinfo.setText(_translate("MainWindow", "Arduino RS232"))
        self.label.setText(_translate("MainWindow", "Poti on A0"))
        self.lblAnzeige.setText(_translate("MainWindow", "1000"))
        self.label_3.setText(_translate("MainWindow", "https://www.youtube.com/pi4iot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

