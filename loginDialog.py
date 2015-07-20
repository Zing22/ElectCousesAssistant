# -*- coding: utf-8 -*-

##############################################
# Filename: loginDialog.py
# Mtime: 2015/7/20 16:17
# Description:
#    本文件由 Qt designer 生成的ui文件转换而来
#    通过继承为QLable添加了点击信号
#    用于验证码点击切换功能
#    点击checkbox会启用或禁用登陆按钮
#    通过绑定信号和槽实现
# Author: Zing
##############################################

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial
import sys
from login import Login
from mainwindow import Ui_MainWindow

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

#为QLable添加点击信号
class MyQLabel(QLabel):
    clicked = pyqtSignal(str)
    def __init__(self,parent=None):
        super(MyQLabel, self).__init__(parent=parent)
        
    def mouseReleaseEvent(self,event):
        self.clicked.emit('refresh!')

class Ui_LoginDialog(QDialog):
    def __init__(self,parent=None):
        super(Ui_LoginDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(400, 330)
        LoginDialog.setMouseTracking(False)
        LoginDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        LoginDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        LoginDialog.setSizeGripEnabled(False)
        LoginDialog.setModal(False)
        self.userNameEdit = QtGui.QLineEdit(LoginDialog)
        self.userNameEdit.setGeometry(QtCore.QRect(40, 20, 330, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userNameEdit.setFont(font)
        self.userNameEdit.setToolTip(_fromUtf8(""))
        self.userNameEdit.setStatusTip(_fromUtf8(""))
        self.userNameEdit.setWhatsThis(_fromUtf8(""))
        self.userNameEdit.setAccessibleName(_fromUtf8(""))
        self.userNameEdit.setAccessibleDescription(_fromUtf8(""))
        self.userNameEdit.setAutoFillBackground(False)
        self.userNameEdit.setStyleSheet(_fromUtf8(""))
        self.userNameEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.userNameEdit.setInputMask(_fromUtf8(""))
        self.userNameEdit.setText(_fromUtf8(""))
        self.userNameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameEdit.setObjectName(_fromUtf8("userNameEdit"))
        self.passwordEdit = QtGui.QLineEdit(LoginDialog)
        self.passwordEdit.setGeometry(QtCore.QRect(40, 80, 330, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.passwordEdit.setText(_fromUtf8(""))
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.j_codeEdit = QtGui.QLineEdit(LoginDialog)
        self.j_codeEdit.setGeometry(QtCore.QRect(40, 140, 160, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.j_codeEdit.setFont(font)
        self.j_codeEdit.setInputMethodHints(QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferUppercase)
        self.j_codeEdit.setText(_fromUtf8(""))
        self.j_codeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.j_codeEdit.setObjectName(_fromUtf8("j_codeEdit"))
        self.j_codeLabel = MyQLabel(LoginDialog)
        self.j_codeLabel.setGeometry(QtCore.QRect(225, 141, 120, 38))
        self.j_codeLabel.setObjectName(_fromUtf8("j_codeLabel"))
        self.checkbox = QCheckBox(LoginDialog)
        self.checkbox.setGeometry(QtCore.QRect(75, 185, 260, 30))
        self.checkbox.setObjectName(_fromUtf8("checkbox"))
        self.login = QtGui.QPushButton(LoginDialog)
        self.login.setGeometry(QtCore.QRect(40, 220, 330, 40))
        self.login.setObjectName(_fromUtf8("login"))
        self.login.setDefault(True)
        self.cancel = QtGui.QPushButton(LoginDialog)
        self.cancel.setGeometry(QtCore.QRect(40, 270, 330, 40))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint|Qt.WindowCloseButtonHint)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT('quit()'))
        self.login.setDisabled(True)
        self.checkbox.toggled.connect(self.toggleCheckBox)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "登录系统", None))
        self.userNameEdit.setPlaceholderText(_translate("LoginDialog", "学号", None))
        self.passwordEdit.setPlaceholderText(_translate("LoginDialog", "密码", None))
        self.login.setText(_translate("LoginDialog", "登录", None))
        self.cancel.setText(_translate("LoginDialog", "退出", None))
        self.j_codeLabel.setPixmap(QtGui.QPixmap('./image/code.jpg'))
        self.checkbox.setText(u"已阅读并同意《使用前须知》")

    def toggleCheckBox(self):
        if self.checkbox.isChecked():
            self.login.setDisabled(False)
        else:
            self.login.setDisabled(True)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    LD = Ui_LoginDialog()
    LD.show()
    sys.exit(app.exec_())

