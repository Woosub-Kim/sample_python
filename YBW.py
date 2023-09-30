# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day05ex09.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from time import time

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    money = 10000
    bet = 1000

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #금액표시
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 20, 230, 40))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(self.money)

        #라벨1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 110, 40))
        self.label.setObjectName("label")

        #라벨2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 60, 15))
        self.label_2.setObjectName("label_2")

        #베팅금액
        self.plusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(280, 300, 15, 15))
        self.plusButton.setObjectName("pushButton+")
        self.plusButton.clicked.connect(self.betUp)
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(280, 325, 15, 15))
        self.minusButton.setObjectName("pushButton-")
        self.minusButton.clicked.connect(self.betDown)
        self.allInBtn = QtWidgets.QPushButton(self.centralwidget)
        self.allInBtn.setGeometry(QtCore.QRect(300,300,40,40))
        self.allInBtn.setObjectName('allInBtn')
        self.lcdNumber2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber2.setGeometry(QtCore.QRect(70, 300, 200, 40))
        self.lcdNumber2.setObjectName("lcdNumber2")
        self.lcdNumber2.display(self.bet)
        self.allInBtn.clicked.connect(self.allIn)

        #이미지
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 80, 340, 140))
        self.image.setObjectName("image")
        self.image.setPixmap(QPixmap('./YBW.jpg'))

        #베팅선택
        self.bet1 = QtWidgets.QPushButton(self.centralwidget)
        self.bet1.setGeometry(QtCore.QRect(20, 250, 90, 20))
        self.bet1.setObjectName("radioButton")
        self.bet2 = QtWidgets.QPushButton(self.centralwidget)
        self.bet2.setGeometry(QtCore.QRect(140, 250, 90, 20))
        self.bet2.setObjectName("radioButton_2")
        self.bet3 =QtWidgets.QPushButton(self.centralwidget)
        self.bet3.setGeometry(QtCore.QRect(260, 250, 90, 20))
        self.bet3.setObjectName("radioButton_3")
        self.bet1.clicked.connect(self.choice1)
        self.bet2.clicked.connect(self.choice2)
        self.bet3.clicked.connect(self.choice3)

        ##
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
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
        self.label.setText(_translate("MainWindow", "가진 돈"))
        self.label_2.setText(_translate("MainWindow", "배팅금액"))
        self.bet1.setText(_translate("MainWindow", "1에 베팅"))
        self.bet2.setText(_translate("MainWindow", "2에 베팅"))
        self.bet3.setText(_translate("MainWindow", "3에 베팅"))
        self.plusButton.setText(_translate('MainWindow', '+'))
        self.minusButton.setText(_translate('MainWindow', '-'))
        self.allInBtn.setText(_translate('MainWindow', 'All In'))

    def betUp(self):
        self.bet += 1000
        if self.bet > self.money:
            self.bet = self.money
        self.lcdNumber2.display(self.bet)

    def betDown(self):
        self.bet -= 1000
        if self.bet < 0:
            self.bet = 0
        self.lcdNumber2.display(self.bet)

    def allIn(self):
        self.bet = self.money
        print(self.bet)
        self.lcdNumber2.display(self.bet)
        print(self.bet)

    def betting(self, ybw, user):
        self.money = self.money - self.bet
        if user == ybw:
            self.money += 2 * self.bet
        print('당신의 잔액', self.money)
        if self.money <= 0:
            self.money = 0
            self.gameover()
            print('잔액이 0이 되어 야바위판에서 쫓겨났습니다')
        self.bet = 1000
        self.lcdNumber.display(self.money)
        self.lcdNumber2.display(self.bet)
    def gameover(self):
        msg = QMessageBox(self.centralwidget)
        print('.')
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('개털ㅋㅋ')
        print('..')
        msg.setText('돈을 모두잃어 야바위판에서 쫓겨났습니다')
        msg.exec_()
        self.sheepOut()
    def sheepOut(self):
        print('??')
        sys.exit()

    def choice1(self):
        ybw = np.random.choice([1,2,3])
        user = 1
        self.betting(ybw, user)
    def choice2(self):
        ybw = np.random.choice([1,2,3])
        user=2
        self.betting(ybw, user)
    def choice3(self):
        ybw = np.random.choice([1,2,3])
        user=3
        self.betting(ybw, user)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
