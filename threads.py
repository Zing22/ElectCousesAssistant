# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    print "hello world~"






