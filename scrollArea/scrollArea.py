# -*- coding:utf-8 -*-
# @time:2022/8/9 9:15
# @author:LX
# @file:scrollArea.py
# @software:PyCharm

import sys
from PyQt5.QtWidgets import QScrollArea, QApplication, QGridLayout, QLayout, QWidget, QPushButton, QHBoxLayout, \
    QVBoxLayout, QSpacerItem, QSizePolicy


class ScrollArea(QScrollArea):
    # 三种布局
    GridLayout = 1
    HBoxLayout = 2
    VBoxLayout = 3

    def __init__(self,*args,**kwargs):
        super(ScrollArea, self).__init__(*args,**kwargs)
        # 内置属性
        self.__pos = [0,-1]
        self.__mode = ScrollArea.GridLayout
        self.__rowMax = 5
        self.__springEnable = False

        self.resize(500, 300)
        self.setWidgetResizable(True) # 窗口大小自适应
        self.scrollAreaWidgetContents = QWidget()
        self.setWidget(self.scrollAreaWidgetContents)

        self.setLayout(1)

        # for _ in range(5):
        #     btn = QPushButton("添加按钮")
        #     self.addWin(btn)
        #
        # self.setSpring(True)
        # for _ in range(40):
        #     btn = QPushButton("添加按钮")
        #     self.addWin(btn)

    # 设置一行最多控件的数量,只有在网格布局下有效
    def setRowMax(self,number:int=5):
        self.__rowMax = number

    # 判断是否有弹簧
    def is_Spring(self)->bool:
        return self.__springEnable

    def setSpring(self,enable:bool=False):
        self.__springEnable = enable
        if enable:
            self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
            # 立即生效
            if self.currentMode() == ScrollArea.HBoxLayout:
                self.box().addItem(self.horizontalSpacer)

            if self.currentMode() == ScrollArea.VBoxLayout:
                self.box().addItem(self.verticalSpacer)

            if self.currentMode() == ScrollArea.GridLayout:
                self.box().addItem(self.horizontalSpacer,0,self.__pos[1]+1)
                self.box().addItem(self.verticalSpacer,self.__pos[0]+1,0)

    def __nextPos(self)->list:
        self.__pos[1] += 1
        if self.__pos[1]>self.__rowMax-1:
            self.__pos[1] = 0
            self.__pos[0] += 1
        return self.__pos

    def addWin(self,win:QWidget,row:int=0,col:int=0):
        spacer = None
        hv_spacer = {"h":None,"v":None}
        # 弹簧判断,并移除
        if self.is_Spring():
            if self.currentMode() == ScrollArea.GridLayout:
                self.box().removeItem(self.horizontalSpacer)
                self.box().removeItem(self.verticalSpacer)
                hv_spacer["h"] = self.horizontalSpacer
                hv_spacer["v"] = self.verticalSpacer

            if self.currentMode() == ScrollArea.HBoxLayout:
                self.box().removeItem(self.horizontalSpacer)
                spacer = self.horizontalSpacer

            if self.currentMode() == ScrollArea.VBoxLayout:
                self.box().removeItem(self.verticalSpacer)
                spacer = self.verticalSpacer

        # 添加控件
        if self.currentMode() in [ScrollArea.HBoxLayout,ScrollArea.VBoxLayout]:
            self.box().addWidget(win)
            if spacer:
                self.box().addItem(spacer)

        if self.currentMode() == ScrollArea.GridLayout:
            self.box().addWidget(win,*self.__nextPos())

            if hv_spacer.get("h"):
                self.box().addItem(hv_spacer.get("h"),0,self.__pos[1]+1)
            if hv_spacer.get("v"):
                self.box().addItem(hv_spacer.get("v"), self.__pos[0]+1, 0)


    # 当前布局模式
    def currentMode(self)->int:
        return self.__mode

    # 设置布局模式,默认网格布局
    def setLayout(self,mode:int=1):
        if mode < 1 or mode > 3:
            # 抛出异常
            raise Exception("布局模式错误")

        if mode == ScrollArea.GridLayout:
            # 创建网格布局
            self.__box = QGridLayout(self.scrollAreaWidgetContents)

        if mode == ScrollArea.HBoxLayout:
            # 创建水平布局
            self.__box = QHBoxLayout(self.scrollAreaWidgetContents)

        if mode == ScrollArea.VBoxLayout:
            # 创建垂直布局
            self.__box = QVBoxLayout(self.scrollAreaWidgetContents)

        self.__mode = mode

    # 返回布局对象
    def box(self)->QLayout:
        return self.__box

    # 清空布局
    def clear(self):
        win_list = self.scrollAreaWidgetContents.children()[1:]
        for win in win_list:
            self.box().removeWidget(win)

        if self.currentMode() == ScrollArea.GridLayout:
            self.__pos = [0, -1]


if __name__ == '__main__':
    app = QApplication(sys.argv)

    scrollArea = ScrollArea()
    scrollArea.show()

    sys.exit(app.exec_())