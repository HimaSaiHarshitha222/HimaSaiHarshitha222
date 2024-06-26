# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 561))
        self.frame.setStyleSheet("background-color: rgb(215, 229, 226);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 30, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.clearB = QtWidgets.QPushButton(self.frame)
        self.clearB.setGeometry(QtCore.QRect(190, 80, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.clearB.setFont(font)
        self.clearB.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.clearB.setObjectName("clearB")
        self.delB = QtWidgets.QPushButton(self.frame)
        self.delB.setGeometry(QtCore.QRect(300, 80, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.delB.setFont(font)
        self.delB.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.delB.setObjectName("delB")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(490, 510, 121, 20))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(60, 140, 481, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 9, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.threeB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.threeB.setFont(font)
        self.threeB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.threeB.setObjectName("threeB")
        self.gridLayout.addWidget(self.threeB, 0, 2, 1, 1)
        self.oneB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.oneB.setFont(font)
        self.oneB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.oneB.setObjectName("oneB")
        self.gridLayout.addWidget(self.oneB, 0, 0, 1, 1)
        self.twoB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.twoB.setFont(font)
        self.twoB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.twoB.setObjectName("twoB")
        self.gridLayout.addWidget(self.twoB, 0, 1, 1, 1)
        self.plusB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.plusB.setFont(font)
        self.plusB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.plusB.setObjectName("plusB")
        self.gridLayout.addWidget(self.plusB, 0, 3, 1, 1)
        self.fourB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fourB.setFont(font)
        self.fourB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.fourB.setObjectName("fourB")
        self.gridLayout.addWidget(self.fourB, 1, 0, 1, 1)
        self.fiveB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fiveB.setFont(font)
        self.fiveB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.fiveB.setObjectName("fiveB")
        self.gridLayout.addWidget(self.fiveB, 1, 1, 1, 1)
        self.sixB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sixB.setFont(font)
        self.sixB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.sixB.setObjectName("sixB")
        self.gridLayout.addWidget(self.sixB, 1, 2, 1, 1)
        self.eqlB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.eqlB.setFont(font)
        self.eqlB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.eqlB.setObjectName("eqlB")
        self.gridLayout.addWidget(self.eqlB, 4, 3, 1, 1)
        self.mulB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mulB.setFont(font)
        self.mulB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.mulB.setObjectName("mulB")
        self.gridLayout.addWidget(self.mulB, 2, 3, 1, 1)
        self.sevenB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sevenB.setFont(font)
        self.sevenB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.sevenB.setObjectName("sevenB")
        self.gridLayout.addWidget(self.sevenB, 2, 0, 1, 1)
        self.perB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.perB.setFont(font)
        self.perB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.perB.setObjectName("perB")
        self.gridLayout.addWidget(self.perB, 4, 2, 1, 1)
        self.byxB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.byxB.setFont(font)
        self.byxB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.byxB.setObjectName("byxB")
        self.gridLayout.addWidget(self.byxB, 3, 2, 1, 1)
        self.nineB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nineB.setFont(font)
        self.nineB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.nineB.setObjectName("nineB")
        self.gridLayout.addWidget(self.nineB, 2, 2, 1, 1)
        self.divB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.divB.setFont(font)
        self.divB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.divB.setObjectName("divB")
        self.gridLayout.addWidget(self.divB, 3, 3, 1, 1)
        self.sqrB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sqrB.setFont(font)
        self.sqrB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.sqrB.setObjectName("sqrB")
        self.gridLayout.addWidget(self.sqrB, 4, 0, 1, 1)
        self.minusB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.minusB.setFont(font)
        self.minusB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.minusB.setObjectName("minusB")
        self.gridLayout.addWidget(self.minusB, 1, 3, 1, 1)
        self.dotB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dotB.setFont(font)
        self.dotB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.dotB.setObjectName("dotB")
        self.gridLayout.addWidget(self.dotB, 3, 0, 1, 1)
        self.zeroB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.zeroB.setFont(font)
        self.zeroB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.zeroB.setObjectName("zeroB")
        self.gridLayout.addWidget(self.zeroB, 3, 1, 1, 1)
        self.eightB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.eightB.setFont(font)
        self.eightB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.eightB.setObjectName("eightB")
        self.gridLayout.addWidget(self.eightB, 2, 1, 1, 1)
        self.sqrtB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sqrtB.setFont(font)
        self.sqrtB.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.sqrtB.setObjectName("sqrtB")
        self.gridLayout.addWidget(self.sqrtB, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearB.setText(_translate("MainWindow", "CE"))
        self.delB.setText(_translate("MainWindow", "del"))
        self.label_2.setText(_translate("MainWindow", "Developed at Digi Brains"))
        self.threeB.setText(_translate("MainWindow", "3"))
        self.oneB.setText(_translate("MainWindow", "1"))
        self.twoB.setText(_translate("MainWindow", "2"))
        self.plusB.setText(_translate("MainWindow", "+"))
        self.fourB.setText(_translate("MainWindow", "4"))
        self.fiveB.setText(_translate("MainWindow", "5"))
        self.sixB.setText(_translate("MainWindow", "6"))
        self.eqlB.setText(_translate("MainWindow", "="))
        self.mulB.setText(_translate("MainWindow", "*"))
        self.sevenB.setText(_translate("MainWindow", "7"))
        self.perB.setText(_translate("MainWindow", "%"))
        self.byxB.setText(_translate("MainWindow", "1/x"))
        self.nineB.setText(_translate("MainWindow", "9"))
        self.divB.setText(_translate("MainWindow", "/"))
        self.sqrB.setText(_translate("MainWindow", "x^2"))
        self.minusB.setText(_translate("MainWindow", "-"))
        self.dotB.setText(_translate("MainWindow", "."))
        self.zeroB.setText(_translate("MainWindow", "0"))
        self.eightB.setText(_translate("MainWindow", "8"))
        self.sqrtB.setText(_translate("MainWindow", "sqrt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
