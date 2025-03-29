# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']="../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbtn_Verify = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Verify.setGeometry(QtCore.QRect(360, 340, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbtn_Verify.setFont(font)
        self.pbtn_Verify.setObjectName("pbtn_Verify")
        self.txt_Infomation = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Infomation.setGeometry(QtCore.QRect(130, 150, 301, 61))
        self.txt_Infomation.setObjectName("txt_Infomation")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pbtn_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Sign.setGeometry(QtCore.QRect(130, 340, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbtn_Sign.setFont(font)
        self.pbtn_Sign.setObjectName("pbtn_Sign")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_Signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Signature.setGeometry(QtCore.QRect(130, 240, 301, 71))
        self.txt_Signature.setObjectName("txt_Signature")
        self.pbtn_GenarateKey = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_GenarateKey.setGeometry(QtCore.QRect(130, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbtn_GenarateKey.setFont(font)
        self.pbtn_GenarateKey.setObjectName("pbtn_GenarateKey")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbtn_Verify.setText(_translate("MainWindow", "Verify"))
        self.label_4.setText(_translate("MainWindow", "Signature"))
        self.pbtn_Sign.setText(_translate("MainWindow", "Sign"))
        self.label_5.setText(_translate("MainWindow", "Infomation"))
        self.pbtn_GenarateKey.setText(_translate("MainWindow", "Gen"))
        self.label.setText(_translate("MainWindow", "ECC CYPHER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
