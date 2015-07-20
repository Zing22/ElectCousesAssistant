# -*- coding: utf-8 -*-

##############################################
# Filename: showHad_ui.py
# Mtime: 2015/7/20 16:21
# Description:
#    本文件由 Qt designer 生成的ui文件转换而来
#    因为只有一个功能，就是显示已有课程列表
#    所以在构造函数里就填好了两个列表
#    或者是显示“没有该类课程” png图片
#    继承QWidget类是为了控制窗口大小和右上角按钮
# Author: Zing
##############################################

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

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

class HadWidget(QWidget):
    def __init__(self, datas, parent=None):
        super(HadWidget, self).__init__(parent)
        self.setupUi(self)
        self.maxRows_1 = 0
        self.maxRows_2 = 0
        self.fillTables(datas)

    def setupUi(self, HadWidget):
        HadWidget.setObjectName(_fromUtf8("HadWidget"))
        HadWidget.resize(500, 430)
        self.label = QtGui.QLabel(HadWidget)
        self.label.setGeometry(QtCore.QRect(215, 10, 70, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(HadWidget)
        self.label_2.setGeometry(QtCore.QRect(215, 215, 70, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget1 = QtGui.QTableWidget(HadWidget)
        self.tableWidget1.setGeometry(QtCore.QRect(10, 35, 480, 170))
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        self.tableWidget2 = QtGui.QTableWidget(HadWidget)
        self.tableWidget2.setGeometry(QtCore.QRect(10, 240, 480, 170))
        self.tableWidget2.setObjectName(_fromUtf8("tableWidget2"))
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)

        self.List_1_lable = QtGui.QLabel(HadWidget)
        self.List_1_lable.setGeometry(QtCore.QRect(10, 35, 480, 170))
        self.List_1_lable.setObjectName(_fromUtf8("List_1_lable"))
        self.List_1_lable.setPixmap(QPixmap("./image/s_nodata.png"))
        self.List_2_lable = QtGui.QLabel(HadWidget)
        self.List_2_lable.setGeometry(QtCore.QRect(10, 240, 480, 170))
        self.List_2_lable.setObjectName(_fromUtf8("List_2_lable"))
        self.List_2_lable.setPixmap(QPixmap("./image/s_nodata.png"))

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint|Qt.WindowCloseButtonHint)

        self.retranslateUi(HadWidget)
        QtCore.QMetaObject.connectSlotsByName(HadWidget)

    def retranslateUi(self, HadWidget):
        HadWidget.setWindowTitle(_translate("HadWidget", "已选课程一览", None))
        self.label.setText(_translate("HadWidget", "已选公选", None))
        self.label_2.setText(_translate("HadWidget", "已选专选", None))
        self.setTables()

    def setTables(self):
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setHorizontalHeaderLabels(
            [_translate("HadWidget", "校区", None),
            _translate("HadWidget", "课程名", None),
            _translate("HadWidget", "任课教师", None),
            _translate("HadWidget", "考试方式", None),]
            )
        self.tableWidget1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget1.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget1.setColumnWidth(0, 60)
        self.tableWidget1.setColumnWidth(1, 180)
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.verticalHeader().setVisible(False)

        self.tableWidget2.setColumnCount(4)
        self.tableWidget2.setHorizontalHeaderLabels(
            [_translate("HadWidget", "校区", None),
            _translate("HadWidget", "课程名", None),
            _translate("HadWidget", "任课教师", None),
            _translate("HadWidget", "考试方式", None),]
            )
        self.tableWidget2.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget2.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget2.setColumnWidth(0, 60)
        self.tableWidget2.setColumnWidth(1, 180)
        self.tableWidget2.setAlternatingRowColors(True)
        self.tableWidget2.verticalHeader().setVisible(False)

    def Mytranslate(self,str):
        return _translate("HadWidget", str, None)

    def fillTables(self,datas):
        if datas[0] and len(datas[0]):
            self.List_1_lable.setVisible(False)
            self.tableWidget1.setRowCount(len(datas[0]))
            for x in datas[0]:
                self.tableWidget1.setItem(self.maxRows_1, 0, QTableWidgetItem(self.Mytranslate(x['campus'])))
                self.tableWidget1.setItem(self.maxRows_1, 1, QTableWidgetItem(self.Mytranslate(x['name'])))
                self.tableWidget1.setItem(self.maxRows_1, 2, QTableWidgetItem(self.Mytranslate(x['teacher'])))
                self.tableWidget1.setItem(self.maxRows_1, 3, QTableWidgetItem(self.Mytranslate(x['exammode'])))
                for i in range(4):
                    self.tableWidget1.item(self.maxRows_1,i).setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                self.maxRows_1+=1
        else:
            print "No such kind of lesson!"

        if datas[1] and len(datas[1]):
            self.List_2_lable.setVisible(False)
            self.tableWidget2.setRowCount(len(datas[1]))
            for x in datas[1]:
                self.tableWidget2.setItem(self.maxRows_2, 0, QTableWidgetItem(self.Mytranslate(x['campus'])))
                self.tableWidget2.setItem(self.maxRows_2, 1, QTableWidgetItem(self.Mytranslate(x['name'])))
                self.tableWidget2.setItem(self.maxRows_2, 2, QTableWidgetItem(self.Mytranslate(x['teacher'])))
                self.tableWidget2.setItem(self.maxRows_2, 3, QTableWidgetItem(self.Mytranslate(x['exammode'])))
                for i in range(4):
                    self.tableWidget2.item(self.maxRows_2,i).setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
                self.maxRows_2+=1
        else:
            print "No such kind of lesson!"

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HW = HadWidget(['2',0])
    HW.show()
    sys.exit(app.exec_())

