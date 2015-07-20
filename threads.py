# -*- coding: utf-8 -*-

##############################################
# Filename: threads.py
# Mtime: 2015/7/20 16:28
# Description:
#    多线程模块
#    每个类继承QThread类
#    改写其中的run函数，实现所需功能
#    某些需要返回信号通知主线程的
#    添加了信号，在主进程声明的时候连接槽
#    某些添加了槽，可以外部控制循环结束
#    具体作用在类的声明上有注释
# Author: Zing
##############################################

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial
import sys
from login import Login
from mainwindow import Ui_MainWindow
from loginDialog import Ui_LoginDialog
from summitReq import SummitReq
from processData import ProData

#获取验证码线程
class thread_getCAPTCHA(QThread):
    signal = QtCore.pyqtSignal()
    def __init__(self,lo,jid,parent=None): 
        super(thread_getCAPTCHA,self).__init__(parent)
        self.lo = lo
        self.jid = jid
    def run(self):
        self.lo.getCAPTCHA(self.jid)
        self.signal.emit()

#post线程
class thread_post(QThread):
    signal = QtCore.pyqtSignal(tuple)
    def __init__(self, username, password, j_code, lo):
        super(thread_post, self).__init__()
        self.username = username
        self.password = password
        self.j_code = j_code
        self.lo = lo
    def run(self):
        arg = self.lo.getSid(self.username, self.password, self.j_code)
        self.signal.emit(arg)

#获取待选列表线程
class thread_getPage(QThread):
    signal = QtCore.pyqtSignal(list)
    def __init__(self,lo,kclb,xqm):
        super(thread_getPage, self).__init__()
        self.sumReq = SummitReq(lo)
        self.kclb = kclb
        self.xqm = xqm
        print "build thread_getPage object"

    def run(self):
        url ,header = self.sumReq.bulidCheckHeader(self.kclb,self.xqm)
        print "get url and header!"
        pageResp = self.sumReq.getPage(url,header)
        print "get response!"
        if pageResp:
            pro = ProData()
            data = pro.getDataList(pageResp)
            self.signal.emit(data)
        else:
            return None

#开始选课线程
class thread_run(QThread):
    signal = QtCore.pyqtSignal()
    eachTime = QtCore.pyqtSignal()

    def __init__(self,lo,kclb,wdic):
        super(thread_run, self).__init__()
        self.Lsn = wdic.values()
        self.kclb = kclb
        self.smq = SummitReq(lo)

    def run(self):
        print "submit begin!"
        self.Lsn = self.smq.submit(self.Lsn,self.kclb)

    def stopSum(self):
        print 'user stop'
        self.smq.runFlag = False

#获取已选列表
class thread_showHad(QThread):
    finished = QtCore.pyqtSignal(list)

    def __init__(self,lo):
        super(thread_showHad, self).__init__()
        self.sumReq = SummitReq(lo)
        self.datas = list()

    def run(self):
        url ,header = self.sumReq.bulidCheckHeader(30,4)
        print "get url and header!"
        pageResp = self.sumReq.getPage(url,header)
        if pageResp:
            pro = ProData()
            self.datas.append(pro.getHadDataList(pageResp))
        else:
            self.datas.append(0)
        url ,header = self.sumReq.bulidCheckHeader(21,4)
        print "get url and header!"
        pageResp = self.sumReq.getPage(url,header)
        if pageResp:
            pro = ProData()
            self.datas.append(pro.getHadDataList(pageResp))
        else:
            self.datas.append(0)
        self.finished.emit(self.datas)
        


if __name__ == '__main__':
    print "hello world~"






