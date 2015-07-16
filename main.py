# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial
import sys
from login import Login
from mainwindow import Ui_MainWindow
from loginDialog import Ui_LoginDialog
from threads import thread_getCAPTCHA,thread_post,thread_getPage,thread_run

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

class LoginDialog(Ui_LoginDialog):
    def __init__(self,parent=None):
        super(LoginDialog,self).__init__(parent)
        self.lo = Login()
        self.lo.getCookie()
        self.readloadCode()
        self.setupUi(self)
        self.login.clicked.connect(self.loginFun)
        self.j_codeLabel.clicked.connect(self.readloadCode)
        self.j_codeLabel.resize(121,41)

    def readloadCode(self):
        self.tem_getCAPTCHA = thread_getCAPTCHA(self.lo, self.lo.jid)
        self.tem_getCAPTCHA.signal.connect(self.refresh)
        self.tem_getCAPTCHA.start()

    def refresh(self):
        self.tem_getCAPTCHA.quit()
        self.j_codeLabel.setPixmap(QtGui.QPixmap('./image/code.jpg'))
        self.toggleCheckBox()
        self.login.setText(_translate("LoginDialog", u"登录", None))
        self.checkbox.setDisabled(False)

    def loginFun(self):
        username = self.userNameEdit.text().toUtf8()
        password = self.passwordEdit.text().toUtf8()
        j_code = self.j_codeEdit.text().toUtf8()
        self.tem_post = thread_post(username, password, j_code, self.lo)
        self.tem_post.signal.connect(self.checkLogin)
        self.tem_post.start()
        self.login.setDisabled(True)
        self.checkbox.setDisabled(True)
        self.login.setText(_translate("LoginDialog", u"登录中...", None))

    def checkLogin(self,arg):
        self.tem_post.quit()
        self.lo.sid = arg[0]
        arg[1]
        if(self.lo.sid != ''):
            print 'login seccessed! sid:',self.lo.sid
            self.accept()
        else:
            print arg[1]
            QtGui.QMessageBox.critical(self, 'Error', _translate("LoginDialog", arg[1], None))
            self.readloadCode()
            self.j_codeEdit.clear()


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,lo,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.maxLength_1 = 0
        self.maxLength_2 = 0
        self.data = []
        self.lo = lo
        self.waitingDict = {} #储存候选列表
        self.setupUi(self)
        #self.setTables()
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint|Qt.WindowMinimizeButtonHint)
        self.kclb = 30 # 专选21 公选30
        self.xqm = 4 # 南1 北2 珠海3 东4
        self.connectBYNs() #连接槽和信号
        self.kclbShow = "公选" #用于标题处理
        self.xqShow = "东校区"
        self.virsion = 'v0.982'
        self.setTitle() #更新标题
        self.tableWidget1.cellDoubleClicked.connect(self.addToTableTwo)
        self.tableWidget2.cellDoubleClicked.connect(self.deleteFromTableTwo)
        self.successSelect = 0
        self.tryTimes = 0

    def connectBYNs(self):
        self.gongxuanBTN.clicked.connect(self.selectGX)
        self.zhuanxuanBTN.clicked.connect(self.selectZX)
        self.DxqBTN.clicked.connect(self.selectXQ_D)
        self.NxqBTN.clicked.connect(self.selectXQ_N)
        self.BxqBTN.clicked.connect(self.selectXQ_B)
        self.ZHxqBTN.clicked.connect(self.selectXQ_ZH)
        self.gongxuanBTN.setDisabled(True)
        self.DxqBTN.setDisabled(True)
        self.runBTN.clicked.connect(self.runrunrun)

    def setTitle(self):
        title = "选课小助手 - %s - %s - %s" % (self.xqShow,self.kclbShow,self.virsion)
        self.setWindowTitle(_translate("MainWindow", title, None))
        self.runBTN.setDisabled(True)
        self.tem_getPage = thread_getPage(self.lo,self.kclb,self.xqm)
        self.tem_getPage.start()
        self.tem_getPage.signal.connect(self.fillTableOne)

    def widgetshake(self):
        print "rollinginthedeep!!"
        (x,y) =  (self.x(),self.y())
        wid = 20
        self.animation = QPropertyAnimation(self, "geometry")
        self.animation.setDuration(350)
        self.animation.setStartValue(QRect(x, y, 800, 590))
        self.animation.setKeyValueAt(0.2, QRect(x-wid, y-wid, 800, 590))
        self.animation.setKeyValueAt(0.4, QRect(x+wid, y+wid, 800, 590))
        self.animation.setKeyValueAt(0.6, QRect(x-wid, y+wid, 800, 590))
        self.animation.setKeyValueAt(0.8, QRect(x+wid, y-wid, 800, 590))
        self.animation.setEndValue(QRect(x, y, 800, 590))
        self.animation.setEasingCurve(QEasingCurve.OutInBounce)
        self.animation.start()
        pass

    def Mytranslate(self,string):
        return _translate("MainWindow", string, None)

    def fillTableOne(self,data):
        print "get data!"
        self.tem_getPage.quit()
        self.maxLength_1 = 0
        self.tableWidget1.setRowCount(0)
        self.data = data
        for x in data:
            self.tableWidget1.setRowCount(self.maxLength_1+1)
            self.tableWidget1.setItem(self.maxLength_1, 0, QTableWidgetItem(self.Mytranslate(x['campus'])))
            self.tableWidget1.setItem(self.maxLength_1, 1, QTableWidgetItem(self.Mytranslate(x['name'])))
            self.tableWidget1.setItem(self.maxLength_1, 2, QTableWidgetItem(self.Mytranslate(x['teacher'])))
            self.tableWidget1.setItem(self.maxLength_1, 3, QTableWidgetItem(self.Mytranslate(x['free'])))
            self.tableWidget1.setItem(self.maxLength_1, 4, QTableWidgetItem(self.Mytranslate(x['percent'])))
            self.tableWidget1.setItem(self.maxLength_1, 5, QTableWidgetItem(self.Mytranslate(x['exammode'])))
            self.tableWidget1.setItem(self.maxLength_1, 6, QTableWidgetItem(self.Mytranslate(x['conflict'])))
            #如果冲突
            if x['free'] == '0':
                for c in range(7):
                    self.tableWidget1.item(self.maxLength_1,c).setTextColor(QColor(220,48,35))
            elif x['conflict'] == 'Yes':
                for c in range(7):
                    self.tableWidget1.item(self.maxLength_1,c).setTextColor(QColor(75,92,196))
            for i in range(7):
                self.tableWidget1.item(self.maxLength_1,i).setTextAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
            self.maxLength_1 += 1
        self.runBTN.setDisabled(False)

    def addToTableTwo(self,row,col):
        print 'clicked:(%s,%s)'%(row,col)
        if self.data[row]['free'] == '0' or self.data[row]['conflict'] == 'Yes' or self.tableWidget1.item(row,1).text() in self.waitingDict:
            self.widgetshake()
            return
        self.waitingDict[self.tableWidget1.item(row,1).text()] = self.data[row]['number']
        self.fillTableTwo(self.data[row])

    def fillTableTwo(self,datas):
        self.tableWidget2.setRowCount(self.maxLength_2+1)
        self.tableWidget2.setItem(self.maxLength_2, 0, QTableWidgetItem(self.Mytranslate(datas['campus'])))
        self.tableWidget2.setItem(self.maxLength_2, 1, QTableWidgetItem(self.Mytranslate(datas['name'])))
        self.tableWidget2.setItem(self.maxLength_2, 2, QTableWidgetItem(self.Mytranslate(datas['teacher'])))
        self.tableWidget2.setItem(self.maxLength_2, 3, QTableWidgetItem(self.Mytranslate(datas['free'])))
        self.tableWidget2.setItem(self.maxLength_2, 4, QTableWidgetItem(self.Mytranslate(datas['percent'])))
        self.tableWidget2.setItem(self.maxLength_2, 5, QTableWidgetItem(self.Mytranslate(datas['exammode'])))
        self.tableWidget2.setItem(self.maxLength_2, 6, QTableWidgetItem(self.Mytranslate(datas['conflict'])))
        #如果冲突
        if datas['conflict'] == 'Yes':
            for c in range(7):
                self.tableWidget2.item(self.maxLength_2,c).setTextColor(QColor(75,92,196))
        for i in range(7):
            self.tableWidget2.item(self.maxLength_2,i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.maxLength_2 += 1

    def deleteFromTableTwo(self,row,col):
        print 'delete:(%s,%s)'%(row,col)
        self.waitingDict.pop(self.tableWidget2.item(row,1).text())
        self.tableWidget2.removeRow(row)
        self.maxLength_2 -= 1

    def selectGX(self):
        self.kclb = 30
        self.gongxuanBTN.setDisabled(True)
        self.zhuanxuanBTN.setDisabled(False)
        print self.kclb
        self.kclbShow = "公选"
        self.setTitle()

    def selectZX(self):
        self.kclb = 21
        self.zhuanxuanBTN.setDisabled(True)
        self.gongxuanBTN.setDisabled(False)
        print self.kclb
        self.kclbShow = "专选"
        self.setTitle()
        
    def selectXQ_D(self):
        self.xqm = 4
        self.DxqBTN.setDisabled(True)
        self.NxqBTN.setDisabled(False)
        self.BxqBTN.setDisabled(False)
        self.ZHxqBTN.setDisabled(False)
        print self.xqm
        self.xqShow = "东校区"
        self.setTitle()
        
    def selectXQ_N(self):
        self.xqm = 1
        self.DxqBTN.setDisabled(False)
        self.NxqBTN.setDisabled(True)
        self.BxqBTN.setDisabled(False)
        self.ZHxqBTN.setDisabled(False)
        print self.xqm
        self.xqShow = "南校区"
        self.setTitle()
        
    def selectXQ_B(self):
        self.xqm = 2
        self.DxqBTN.setDisabled(False)
        self.NxqBTN.setDisabled(False)
        self.BxqBTN.setDisabled(True)
        self.ZHxqBTN.setDisabled(False)
        print self.xqm
        self.xqShow = "北校区"
        self.setTitle()
        
    def selectXQ_ZH(self):
        self.xqm = 3
        self.DxqBTN.setDisabled(False)
        self.NxqBTN.setDisabled(False)
        self.BxqBTN.setDisabled(False)
        self.ZHxqBTN.setDisabled(True)
        print self.xqm
        self.xqShow = "珠海校区"
        self.setTitle()

    #######################################################
    #######用于测试runrunrun################################
    ######################################################
    def setDict(self):
        self.tableWidget2.setRowCount(3)
        self.tableWidget2.setItem(0, 0, QTableWidgetItem(self.Mytranslate("北")))
        self.tableWidget2.setItem(0, 1, QTableWidgetItem(self.Mytranslate("中文")))
        self.tableWidget2.setItem(0, 2, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(0, 3, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(0, 4, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(0, 5, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(0, 6, QTableWidgetItem(self.Mytranslate("Name")))

        self.tableWidget2.setItem(1, 0, QTableWidgetItem(self.Mytranslate("东")))
        self.tableWidget2.setItem(1, 1, QTableWidgetItem(self.Mytranslate("bbb")))
        self.tableWidget2.setItem(1, 2, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(1, 3, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(1, 4, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(1, 5, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(1, 6, QTableWidgetItem(self.Mytranslate("Name")))

        self.tableWidget2.setItem(2, 0, QTableWidgetItem(self.Mytranslate("南")))
        self.tableWidget2.setItem(2, 1, QTableWidgetItem(self.Mytranslate("CCC英文")))
        self.tableWidget2.setItem(2, 2, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(2, 3, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(2, 4, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(2, 5, QTableWidgetItem(self.Mytranslate("Name")))
        self.tableWidget2.setItem(2, 6, QTableWidgetItem(self.Mytranslate("Name")))

        self.waitingDict = {}
        self.waitingDict[self.tableWidget2.item(0,1).text()] = '35000123151002'
        self.waitingDict[self.tableWidget2.item(1,1).text()] = '35000192151002'
        self.waitingDict[self.tableWidget2.item(2,1).text()] = '35000192151001'

    def runrunrun(self):
        ################################
        ##########test!!!!!!############
        ################################
        #self.setDict()

        print 'run!'
        self.successSelect = 0
        self.tryTimes = 0
        self.tem_run = thread_run(self.lo,self.kclb,self.waitingDict)
        self.tem_run.smq.exitSign.connect(self.endRun)
        self.tem_run.smq.sSignal.connect(self.sucOne)
        self.tem_run.smq.times.connect(self.addTimes)
        self.runBTN.clicked.disconnect(self.runrunrun)
        self.runBTN.clicked.connect(self.tem_run.stopSum)
        self.runBTN.setText(self.Mytranslate(u'停止选课！'))
        self.tem_run.start()


    def addTimes(self):
        self.tryTimes += 1
        self.refreshTitle()

    def endRun(self):
        self.runBTN.setText(self.Mytranslate(u'开始选课！'))
        self.runBTN.clicked.disconnect(self.tem_run.stopSum)
        self.runBTN.clicked.connect(self.runrunrun)
        self.tem_run.quit()

    def sucOne(self,num):
        print "get successed number:%s" % num
        key = ''
        for k in self.waitingDict.keys():
            if self.waitingDict[k] == num:
                self.waitingDict.pop(k)
                key = k
        for row in range(self.tableWidget2.rowCount()):
            print "rownumber:%s" % self.tableWidget2.rowCount()
            if self.tableWidget2.item(row,1).text() == key:
                print "green:%s" % key.toUtf8()
                for c in range(7):
                    self.tableWidget2.item(row,c).setTextColor(QColor(0,188,18))
                self.successSelect += 1
                break
        self.refreshTitle()

    def refreshTitle(self):
        title = "选课小助手 - 成功选课:%s门 - 第%s次尝试 - %s" % \
            (self.successSelect,self.tryTimes,self.virsion)
        self.setWindowTitle(_translate("MainWindow", title, None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./image/logo.png"))
    splash=QSplashScreen(QPixmap("./image/logo.png"))
    splash.show()
    app.processEvents()
    LDlog = LoginDialog()
    LDlog.show()
    splash.finish(LDlog)
    if LDlog.exec_():
        MWdow = MyMainWindow(LDlog.lo)
        MWdow.show()
    sys.exit(app.exec_())


