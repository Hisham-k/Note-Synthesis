# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 324)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.c4 = QtWidgets.QPushButton(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(20, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c4.sizePolicy().hasHeightForWidth())
        self.c4.setSizePolicy(sizePolicy)
        self.c4.setMinimumSize(QtCore.QSize(20, 20))
        self.c4.setStyleSheet("#c4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#c4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.d4 = QtWidgets.QPushButton(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(60, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d4.sizePolicy().hasHeightForWidth())
        self.d4.setSizePolicy(sizePolicy)
        self.d4.setMinimumSize(QtCore.QSize(20, 20))
        self.d4.setStyleSheet("#d4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#d4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d4.setText("")
        self.d4.setObjectName("d4")
        self.c40 = QtWidgets.QPushButton(self.centralwidget)
        self.c40.setGeometry(QtCore.QRect(40, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c40.sizePolicy().hasHeightForWidth())
        self.c40.setSizePolicy(sizePolicy)
        self.c40.setMinimumSize(QtCore.QSize(20, 20))
        self.c40.setStyleSheet("#c40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#c40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.c40.setText("")
        self.c40.setObjectName("c40")
        self.d40 = QtWidgets.QPushButton(self.centralwidget)
        self.d40.setGeometry(QtCore.QRect(80, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d40.sizePolicy().hasHeightForWidth())
        self.d40.setSizePolicy(sizePolicy)
        self.d40.setMinimumSize(QtCore.QSize(20, 20))
        self.d40.setStyleSheet("#d40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#d40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.d40.setText("")
        self.d40.setObjectName("d40")
        self.e4 = QtWidgets.QPushButton(self.centralwidget)
        self.e4.setGeometry(QtCore.QRect(100, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e4.sizePolicy().hasHeightForWidth())
        self.e4.setSizePolicy(sizePolicy)
        self.e4.setMinimumSize(QtCore.QSize(20, 20))
        self.e4.setStyleSheet("#e4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#e4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e4.setText("")
        self.e4.setObjectName("e4")
        self.f4 = QtWidgets.QPushButton(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(140, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f4.sizePolicy().hasHeightForWidth())
        self.f4.setSizePolicy(sizePolicy)
        self.f4.setMinimumSize(QtCore.QSize(20, 20))
        self.f4.setStyleSheet("#f4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#f4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f4.setText("")
        self.f4.setObjectName("f4")
        self.g4 = QtWidgets.QPushButton(self.centralwidget)
        self.g4.setGeometry(QtCore.QRect(180, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g4.sizePolicy().hasHeightForWidth())
        self.g4.setSizePolicy(sizePolicy)
        self.g4.setMinimumSize(QtCore.QSize(20, 20))
        self.g4.setStyleSheet("#g4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#g4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g4.setText("")
        self.g4.setObjectName("g4")
        self.a4 = QtWidgets.QPushButton(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(220, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a4.sizePolicy().hasHeightForWidth())
        self.a4.setSizePolicy(sizePolicy)
        self.a4.setMinimumSize(QtCore.QSize(20, 20))
        self.a4.setStyleSheet("#a4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#a4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a4.setText("")
        self.a4.setObjectName("a4")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(260, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy)
        self.b4.setMinimumSize(QtCore.QSize(20, 20))
        self.b4.setStyleSheet("#b4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#b4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.c5 = QtWidgets.QPushButton(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(300, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c5.sizePolicy().hasHeightForWidth())
        self.c5.setSizePolicy(sizePolicy)
        self.c5.setMinimumSize(QtCore.QSize(20, 20))
        self.c5.setStyleSheet("#c5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#c5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c5.setText("")
        self.c5.setObjectName("c5")
        self.d5 = QtWidgets.QPushButton(self.centralwidget)
        self.d5.setGeometry(QtCore.QRect(340, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d5.sizePolicy().hasHeightForWidth())
        self.d5.setSizePolicy(sizePolicy)
        self.d5.setMinimumSize(QtCore.QSize(20, 20))
        self.d5.setStyleSheet("#d5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#d5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.d5.setText("")
        self.d5.setObjectName("d5")
        self.a5 = QtWidgets.QPushButton(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(500, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a5.sizePolicy().hasHeightForWidth())
        self.a5.setSizePolicy(sizePolicy)
        self.a5.setMinimumSize(QtCore.QSize(20, 20))
        self.a5.setStyleSheet("#a5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#a5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.a5.setText("")
        self.a5.setObjectName("a5")
        self.e5 = QtWidgets.QPushButton(self.centralwidget)
        self.e5.setGeometry(QtCore.QRect(380, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e5.sizePolicy().hasHeightForWidth())
        self.e5.setSizePolicy(sizePolicy)
        self.e5.setMinimumSize(QtCore.QSize(20, 20))
        self.e5.setStyleSheet("#e5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#e5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.e5.setText("")
        self.e5.setObjectName("e5")
        self.g5 = QtWidgets.QPushButton(self.centralwidget)
        self.g5.setGeometry(QtCore.QRect(460, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5.sizePolicy().hasHeightForWidth())
        self.g5.setSizePolicy(sizePolicy)
        self.g5.setMinimumSize(QtCore.QSize(20, 20))
        self.g5.setStyleSheet("#g5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#g5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.g5.setText("")
        self.g5.setObjectName("g5")
        self.f5 = QtWidgets.QPushButton(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(420, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f5.sizePolicy().hasHeightForWidth())
        self.f5.setSizePolicy(sizePolicy)
        self.f5.setMinimumSize(QtCore.QSize(20, 20))
        self.f5.setStyleSheet("#f5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#f5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.f5.setText("")
        self.f5.setObjectName("f5")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(540, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy)
        self.b5.setMinimumSize(QtCore.QSize(20, 20))
        self.b5.setStyleSheet("#b5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#b5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.c6 = QtWidgets.QPushButton(self.centralwidget)
        self.c6.setGeometry(QtCore.QRect(580, 110, 41, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c6.sizePolicy().hasHeightForWidth())
        self.c6.setSizePolicy(sizePolicy)
        self.c6.setMinimumSize(QtCore.QSize(20, 20))
        self.c6.setStyleSheet("#c6{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#c6:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        self.c6.setText("")
        self.c6.setObjectName("c6")
        self.f40 = QtWidgets.QPushButton(self.centralwidget)
        self.f40.setGeometry(QtCore.QRect(160, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f40.sizePolicy().hasHeightForWidth())
        self.f40.setSizePolicy(sizePolicy)
        self.f40.setMinimumSize(QtCore.QSize(20, 20))
        self.f40.setStyleSheet("#f40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#f40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.f40.setText("")
        self.f40.setObjectName("f40")
        self.g40 = QtWidgets.QPushButton(self.centralwidget)
        self.g40.setGeometry(QtCore.QRect(200, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g40.sizePolicy().hasHeightForWidth())
        self.g40.setSizePolicy(sizePolicy)
        self.g40.setMinimumSize(QtCore.QSize(20, 20))
        self.g40.setStyleSheet("#g40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#g40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.g40.setText("")
        self.g40.setObjectName("g40")
        self.a40 = QtWidgets.QPushButton(self.centralwidget)
        self.a40.setGeometry(QtCore.QRect(240, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a40.sizePolicy().hasHeightForWidth())
        self.a40.setSizePolicy(sizePolicy)
        self.a40.setMinimumSize(QtCore.QSize(20, 20))
        self.a40.setStyleSheet("#a40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#a40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.a40.setText("")
        self.a40.setObjectName("a40")
        self.c50 = QtWidgets.QPushButton(self.centralwidget)
        self.c50.setGeometry(QtCore.QRect(320, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c50.sizePolicy().hasHeightForWidth())
        self.c50.setSizePolicy(sizePolicy)
        self.c50.setMinimumSize(QtCore.QSize(20, 20))
        self.c50.setStyleSheet("#c50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#c50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.c50.setText("")
        self.c50.setObjectName("c50")
        self.d50 = QtWidgets.QPushButton(self.centralwidget)
        self.d50.setGeometry(QtCore.QRect(360, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d50.sizePolicy().hasHeightForWidth())
        self.d50.setSizePolicy(sizePolicy)
        self.d50.setMinimumSize(QtCore.QSize(20, 20))
        self.d50.setStyleSheet("#d50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#d50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.d50.setText("")
        self.d50.setObjectName("d50")
        self.f50 = QtWidgets.QPushButton(self.centralwidget)
        self.f50.setGeometry(QtCore.QRect(440, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f50.sizePolicy().hasHeightForWidth())
        self.f50.setSizePolicy(sizePolicy)
        self.f50.setMinimumSize(QtCore.QSize(20, 20))
        self.f50.setStyleSheet("#f50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#f50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.f50.setText("")
        self.f50.setObjectName("f50")
        self.g50 = QtWidgets.QPushButton(self.centralwidget)
        self.g50.setGeometry(QtCore.QRect(480, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g50.sizePolicy().hasHeightForWidth())
        self.g50.setSizePolicy(sizePolicy)
        self.g50.setMinimumSize(QtCore.QSize(20, 20))
        self.g50.setStyleSheet("#g50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#g50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.g50.setText("")
        self.g50.setObjectName("g50")
        self.a50 = QtWidgets.QPushButton(self.centralwidget)
        self.a50.setGeometry(QtCore.QRect(520, 110, 31, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a50.sizePolicy().hasHeightForWidth())
        self.a50.setSizePolicy(sizePolicy)
        self.a50.setMinimumSize(QtCore.QSize(20, 20))
        self.a50.setStyleSheet("#a50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#a50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
        self.a50.setText("")
        self.a50.setObjectName("a50")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 20, 111, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.c4.raise_()
        self.d4.raise_()
        self.c40.raise_()
        self.e4.raise_()
        self.f4.raise_()
        self.d40.raise_()
        self.g4.raise_()
        self.a4.raise_()
        self.b4.raise_()
        self.c5.raise_()
        self.d5.raise_()
        self.a5.raise_()
        self.e5.raise_()
        self.g5.raise_()
        self.f5.raise_()
        self.b5.raise_()
        self.c6.raise_()
        self.f40.raise_()
        self.g40.raise_()
        self.a40.raise_()
        self.c50.raise_()
        self.d50.raise_()
        self.f50.raise_()
        self.g50.raise_()
        self.a50.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.c4.setShortcut(_translate("MainWindow", "A"))
        self.d4.setShortcut(_translate("MainWindow", "S"))
        self.c40.setShortcut(_translate("MainWindow", "Q"))
        self.d40.setShortcut(_translate("MainWindow", "W"))
        self.e4.setShortcut(_translate("MainWindow", "D"))
        self.f4.setShortcut(_translate("MainWindow", "F"))
        self.g4.setShortcut(_translate("MainWindow", "G"))
        self.a4.setShortcut(_translate("MainWindow", "H"))
        self.b4.setShortcut(_translate("MainWindow", "J"))
        self.c5.setShortcut(_translate("MainWindow", "K"))
        self.d5.setShortcut(_translate("MainWindow", "L"))
        self.a5.setShortcut(_translate("MainWindow", "V"))
        self.e5.setShortcut(_translate("MainWindow", "Z"))
        self.g5.setShortcut(_translate("MainWindow", "C"))
        self.f5.setShortcut(_translate("MainWindow", "X"))
        self.b5.setShortcut(_translate("MainWindow", "B"))
        self.c6.setShortcut(_translate("MainWindow", "N"))
        self.f40.setShortcut(_translate("MainWindow", "E"))
        self.g40.setShortcut(_translate("MainWindow", "R"))
        self.a40.setShortcut(_translate("MainWindow", "T"))
        self.c50.setShortcut(_translate("MainWindow", "Y"))
        self.d50.setShortcut(_translate("MainWindow", "U"))
        self.f50.setShortcut(_translate("MainWindow", "I"))
        self.g50.setShortcut(_translate("MainWindow", "O"))
        self.a50.setShortcut(_translate("MainWindow", "P"))
        self.radioButton.setText(_translate("MainWindow", "Guitar"))
        self.radioButton_2.setText(_translate("MainWindow", "Other instrument"))

