# -*- coding:utf-8 -*-
# @time:2022/8/411:08
# @author:LX
# @file:table.py
# @software:PyCharm
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt,pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import (QApplication, QTableWidget, QWidget, QTabWidget, QMainWindow, QHeaderView,
                             QTableWidgetItem)


class Table(QTableWidget):
    def __init__(self, *args, **kwargs) -> None:
        super(Table, self).__init__(*args, **kwargs)

        self.__header = []

        self.Init()

    def Init(self):
        # 默认等宽
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setVerticalHeaderVisible(False)
        self.setHorizontalHeaderVisible(False) # 隐藏头


    def setHeaders(self,header:list):
        self.__header = header
        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)

    def getHeaders(self)->list:
        return self.__header

    # 隐藏表头
    def setHorizontalHeaderVisible(self,visible:bool):
        self.horizontalHeader().setVisible(visible)


    # 隐藏侧边栏
    def setVerticalHeaderVisible(self,visible:bool):
        self.verticalHeader().setVisible(visible)

    def is_HorizontalHeaderVisible(self):
        if self.__header:
            return False
        return True

    # 添加单条信息
    def addTable(self,info:list):
        if self.is_HorizontalHeaderVisible():
            self.setHeaders(info)

        row = self.rowCount()
        self.insertRow(row)

        for i,t in enumerate(info):
            item = QTableWidgetItem(t)
            item.setTextAlignment(Qt.AlignCenter)
            self.setItem(row,i,item)


    # 删除单条信息
    def delTable(self,row:int):
        self.removeRow(row)

    # 清除所有数据
    def tableUrlClear(self):
        for rowNum in range(0, self.rowCount())[::-1]:  # 逆序删除
            self.removeRow(rowNum)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
