# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fatma/dsp_task4/MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SONG1 = QtWidgets.QPushButton(self.centralwidget)
        self.SONG1.setGeometry(QtCore.QRect(20, 20, 121, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/fatma/dsp_task4/../Downloads/Eighth-Note-Double.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SONG1.setIcon(icon)
        self.SONG1.setIconSize(QtCore.QSize(50, 50))
        self.SONG1.setObjectName("SONG1")
        self.SONG2 = QtWidgets.QPushButton(self.centralwidget)
        self.SONG2.setGeometry(QtCore.QRect(20, 110, 121, 71))
        self.SONG2.setIcon(icon)
        self.SONG2.setIconSize(QtCore.QSize(50, 50))
        self.SONG2.setObjectName("SONG2")
        self.MIX_RATIO = QtWidgets.QSlider(self.centralwidget)
        self.MIX_RATIO.setGeometry(QtCore.QRect(170, 80, 401, 51))
        self.MIX_RATIO.setStyleSheet("\n"
"gridline-color: rgb(255, 0, 255);\n"
"selection-color: rgb(255, 0, 255);\n"
"selection-background-color: rgb(170, 0, 127);\n"
"border-color: rgb(255, 85, 127);\n"
"color: rgb(255, 85, 127);")
        self.MIX_RATIO.setMaximum(100)
        self.MIX_RATIO.setOrientation(QtCore.Qt.Horizontal)
        self.MIX_RATIO.setObjectName("MIX_RATIO")
        self.TABLE = QtWidgets.QLabel(self.centralwidget)
        self.TABLE.setGeometry(QtCore.QRect(210, 210, 271, 231))
        self.TABLE.setObjectName("TABLE")
        self.RATIO = QtWidgets.QLabel(self.centralwidget)
        self.RATIO.setGeometry(QtCore.QRect(340, 130, 81, 31))
        self.RATIO.setStyleSheet("font: 75 12pt \"Waree\";")
        self.RATIO.setObjectName("RATIO")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menubrowse = QtWidgets.QMenu(self.menubar)
        self.menubrowse.setObjectName("menubrowse")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_window = QtWidgets.QAction(MainWindow)
        self.actionNew_window.setObjectName("actionNew_window")
        self.actionLoad_song = QtWidgets.QAction(MainWindow)
        self.actionLoad_song.setObjectName("actionLoad_song")
        self.menuFile.addAction(self.actionNew_window)
        self.menubrowse.addAction(self.actionLoad_song)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menubrowse.menuAction())

        self.retranslateUi(MainWindow)
        self.MIX_RATIO.valueChanged['int'].connect(self.RATIO.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SONG1.setText(_translate("MainWindow", "SONG1"))
        self.SONG2.setText(_translate("MainWindow", "SONG2"))
        self.TABLE.setText(_translate("MainWindow", "TextLabel"))
        self.RATIO.setText(_translate("MainWindow", "0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menubrowse.setTitle(_translate("MainWindow", "browse"))
        self.actionNew_window.setText(_translate("MainWindow", "New window"))
        self.actionLoad_song.setText(_translate("MainWindow", "Load song"))