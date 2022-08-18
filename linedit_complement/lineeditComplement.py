# -*- coding:utf-8 -*-
# @time:2022/7/2711:30
# @author:LX
# @file:lineeditComplement.py
# @software:PyCharm

import sys
import typing
import time
from PyQt5.QtCore import QPoint, QThread, QObject, pyqtSignal, QAbstractItemModel
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets


# 自带补全的输入框
class LineEditComplement(QLineEdit):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        # 补全单词列表
        self.__completer_list = []
        self.Init()

    def Init(self):
        pass


    # 补全单词列表
    def completerList(self)->list:
        return self.__completer_list

    # 添加单词列表
    def addCompleterList(self,words:list):
        self.__completer_list.extend(set(words))
        self.updateCompleter()

    # 更新补全单词
    def updateCompleter(self):
        # 给lineEdit添加补全功能
        self.completer = QtWidgets.QCompleter(self.completerList(), self)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.setCompleter(self.completer)

    # 移除补全单词
    def removeCompleter(self,word:str):
        if word in self.__completer_list:
            self.__completer_list.remove(word)
            self.updateCompleter()


# 测试类
class Test(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('测试')
        self.setGeometry(300, 300, 300, 200)
        self.lineEdit = LineEditComplement(self)
        self.lineEdit.addCompleterList(['dasd','add','dad'])
        self.lineEdit.addCompleterList(['drgr','dmnhn','dzxc'])
        self.lineEdit.removeCompleter("dasd")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit(app.exec_())