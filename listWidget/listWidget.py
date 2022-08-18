# -*- coding:utf-8 -*-
# @time:2022/8/59:14
# @author:LX
# @file:listWidget.py
# @software:PyCharm

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt,pyqtSignal,QSize
from PyQt5.QtGui import QMouseEvent, QCursor
from PyQt5.QtWidgets import (QApplication, QListWidget, QMenu,
                             QListWidgetItem, QMessageBox)





class ListWidget(QListWidget):
    def __init__(self,*args,**kwargs):
        super(ListWidget,self).__init__(*args,**kwargs)

        # 注册右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.myEvent()
        self.Init()

    def Init(self):
       self.addList("1")
       self.addList("1")
       self.addList("1")
       # self.clearList()

    def addList(self,info:str):
        item = QListWidgetItem(info)
        item.setTextAlignment(Qt.AlignCenter)
        self.addItem(item)

    # 获取鼠标右键选中的菜单文本
    def getMouseSelectMenuText(self)->str:
        try:
            return self.currentItem().text()
        except:
            return ""

    # 菜单-查看事件
    def look_Action(self):
        text = self.getMouseSelectMenuText()

    # 菜单-删除事件
    def del_Action(self):
        text = self.getMouseSelectMenuText()
        # 删除提示
        reply = QMessageBox.warning(self,"删除提示","确定删除{}吗?".format(text),QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.delList(text)

    # 清空所有子项
    def clearList(self):
        self.clear()
        self.clearSelection()

    def showContextMenu(self,pos):
        menu = QMenu(self)
        look_action = menu.addAction("查看信息")
        look_action.triggered.connect(self.look_Action)
        del_action = menu.addAction("删除")
        del_action.triggered.connect(self.del_Action)
        menu.exec_(QCursor.pos())

    # 删除子项
    def delList(self,text:str):
        for i in range(self.count()):
            if self.item(i).text() == text:
                self.takeItem(i)
                self.removeItemWidget(self.item(i))
                break

    # def itemClickedEvent(self,item:QListWidgetItem):
    #     print(item.text())

    def myEvent(self):
        # 鼠标右键菜单事件
        self.customContextMenuRequested.connect(self.showContextMenu)
        #
        # self.itemClicked.connect(self.itemClickedEvent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ListWidget()
    w.show()
    sys.exit(app.exec_())