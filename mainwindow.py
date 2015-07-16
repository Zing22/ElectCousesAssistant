# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 590)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gongxuanBTN = QtGui.QPushButton(self.centralwidget)
        self.gongxuanBTN.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.gongxuanBTN.setObjectName(_fromUtf8("gongxuanBTN"))
        self.zhuanxuanBTN = QtGui.QPushButton(self.centralwidget)
        self.zhuanxuanBTN.setGeometry(QtCore.QRect(400, 0, 400, 50))
        self.zhuanxuanBTN.setObjectName(_fromUtf8("zhuanxuanBTN"))
        self.DxqBTN = QtGui.QPushButton(self.centralwidget)
        self.DxqBTN.setGeometry(QtCore.QRect(0, 50, 200, 50))
        self.DxqBTN.setObjectName(_fromUtf8("DxqBTN"))
        self.NxqBTN = QtGui.QPushButton(self.centralwidget)
        self.NxqBTN.setGeometry(QtCore.QRect(200, 50, 200, 50))
        self.NxqBTN.setObjectName(_fromUtf8("NxqBTN"))
        self.BxqBTN = QtGui.QPushButton(self.centralwidget)
        self.BxqBTN.setGeometry(QtCore.QRect(400, 50, 200, 50))
        self.BxqBTN.setObjectName(_fromUtf8("BxqBTN"))
        self.ZHxqBTN = QtGui.QPushButton(self.centralwidget)
        self.ZHxqBTN.setGeometry(QtCore.QRect(600, 50, 200, 50))
        self.ZHxqBTN.setObjectName(_fromUtf8("ZHxqBTN"))
        self.tableWidget1 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget1.setGeometry(QtCore.QRect(5, 120, 790, 200))
        self.tableWidget1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget1.setLineWidth(1)
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.listName1 = QtGui.QLabel(self.centralwidget)
        self.listName1.setGeometry(QtCore.QRect(360, 100, 80, 20))
        self.listName1.setAlignment(QtCore.Qt.AlignCenter)
        self.listName1.setObjectName(_fromUtf8("listName1"))
        self.listName2 = QtGui.QLabel(self.centralwidget)
        self.listName2.setGeometry(QtCore.QRect(360, 320, 80, 20))
        self.listName2.setAlignment(QtCore.Qt.AlignCenter)
        self.listName2.setObjectName(_fromUtf8("listName2"))
        self.tableWidget2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(5, 340, 790, 200))
        self.tableWidget2.setObjectName(_fromUtf8("tableWidget2"))
        self.runBTN = QtGui.QPushButton(self.centralwidget)
        self.runBTN.setGeometry(QtCore.QRect(0, 543, 800, 46))
        self.runBTN.setObjectName(_fromUtf8("runBTN"))
        self.runBTN.setDefault(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.gongxuanBTN.setText(_translate("MainWindow", "公选", None))
        self.zhuanxuanBTN.setText(_translate("MainWindow", "专选", None))
        self.DxqBTN.setText(_translate("MainWindow", "东校区", None))
        self.NxqBTN.setText(_translate("MainWindow", "南校区", None))
        self.BxqBTN.setText(_translate("MainWindow", "北校区", None))
        self.ZHxqBTN.setText(_translate("MainWindow", "珠海校区", None))
        self.listName1.setText(_translate("MainWindow", "可选课程", None))
        self.listName2.setText(_translate("MainWindow", "准备选课", None))
        self.runBTN.setText(_translate("MainWindow", "开始选课！", None))
        self.setTables()

    def setTables(self):
        self.tableWidget1.setColumnCount(7)
        self.tableWidget1.setHorizontalHeaderLabels(
            [_translate("MainWindow", "校区", None),
            _translate("MainWindow", "课程名", None),
            _translate("MainWindow", "任课教师", None),
            _translate("MainWindow", "空位", None),
            _translate("MainWindow", "选中率", None),
            _translate("MainWindow", "考试方式", None),
            _translate("MainWindow", "冲突", None),]
            )
        self.tableWidget1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget1.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget1.setColumnWidth(0, 60)
        self.tableWidget1.setColumnWidth(1, 235)
        self.tableWidget1.setColumnWidth(2, 155)
        self.tableWidget1.setColumnWidth(3, 60)
        self.tableWidget1.setColumnWidth(6, 60)
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.verticalHeader().setVisible(False)

        self.tableWidget2.setColumnCount(7)
        self.tableWidget2.setHorizontalHeaderLabels(
            [
            _translate("MainWindow", "校区", None),
            _translate("MainWindow", "课程名", None),
            _translate("MainWindow", "任课教师", None),
            _translate("MainWindow", "空位", None),
            _translate("MainWindow", "选中率", None),
            _translate("MainWindow", "考试方式", None),
            _translate("MainWindow", "冲突", None),]
            )
        self.tableWidget2.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget2.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget2.setColumnWidth(0, 60)
        self.tableWidget2.setColumnWidth(1, 235)
        self.tableWidget2.setColumnWidth(2, 155)
        self.tableWidget2.setColumnWidth(3, 60)
        self.tableWidget2.setColumnWidth(6, 60)
        self.tableWidget2.setAlternatingRowColors(True)
        self.tableWidget2.verticalHeader().setVisible(False)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

