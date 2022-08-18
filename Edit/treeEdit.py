# -*- coding:utf-8 -*-
# @time:2022/8/1811:12
# @author:LX
# @file:treeEdit.py
# @software:PyCharm
'''
    带目录和tab的编译器

'''

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QColor, QCursor,QFont
from PyQt5.QtWidgets import QApplication, QMenu,QWidget,QGridLayout,QSplitter

from Edit.edit import QSSEdit
from Tab.tab import Tab
from Tree.Tree import Tree


class TreeEdit(QWidget):
    def __init__(self,*args,**kwargs):
        super(TreeEdit, self).__init__(*args,**kwargs)

        # 网格布局,水平分裂器
        self.gbox = QGridLayout(self)
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal)
        self.gbox.addWidget(self.splitter)

        # 树,tab
        self.tree = Tree(self.splitter)
        self.tab = Tab(self.splitter)

        # 初始化
        self.Init()
        # 事件初始化
        self.myEvent()

    def Init(self):
        self.tree.setCloseMouseRight(True)

        # 调整布局
        tree_w = int(self.width()*0.25)
        self.splitter.setSizes([tree_w,self.width()-tree_w])

    # 添加
    def add(self,name:str=None):
        if name:
            print(name)
            self.tab.addTab(QSSEdit(),name)
            print(self.tree.get_all_file_name())
        else:
            print("没有名字")
        # self.tree.create_file(name)

    def delete_file(self,name:str):
        print("delete_file",name)
        self.tab.delete(name)

    # 点击树打开tab
    def open_tab(self,name:str):
        print("open_tab",name)
        self.tab.setTabState(name,True)

    def myEvent(self):
        self.tree.rightClickFile.connect(self.add)
        self.tree.rightClicked.connect(self.add)
        self.tree.delefile.connect(self.delete_file)
        self.tree.filenameedit.connect(self.open_tab)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TreeEdit()
    win.show()

    sys.exit(app.exec_())
