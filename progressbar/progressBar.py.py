# -*- coding:utf-8 -*-
# @time:2022/7/213:17
# @author:LX
# @file:progressBar.py.py
# @software:PyCharm
import sys
import typing
import time
from PyQt5.QtCore import QPoint, QThread, QObject,pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5 import QtCore, QtGui, QtWidgets

'''
    进度条
'''


# 监视进度条线程
class ProgressBarThread(QThread):
    # 进度条加载完成事件
    progress_bar_finish_signal = pyqtSignal(bool)

    def __init__(self,progressbar:QProgressBar, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.progressbar = progressbar
        print(self.progressbar.maximum())

    def run(self):
        # 监视进度条是否完成
        while True:
            if self.progressbar.value() == self.progressbar.maximum():
                # 发送进度条完成信号
                self.progress_bar_finish_signal.emit(True)
                break
            # self.sleep() # 秒
            self.msleep(450) # 豪毫（不能低于250）
            # self.usleep(100) # 微毫

# 具体事件线程
class EventThread(QThread):
    def __init__(self,progressbar:QProgressBar, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.progressbar = progressbar

    def add_f(self,f,args=tuple()):
        self.f = f
        self.args = args

    def run(self):
        if self.args:
            self.f(*self.args)
        else:
            self.f()


class MyQProgressBar(QProgressBar):
    # 进度条完成触发事件
    progress_bar_finish_signal = pyqtSignal(bool)

    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.setMaximum(100)
        self.setValue(0)
        # 内置qt线程
        self.built_thread = ProgressBarThread(self)
        self.built_thread.start()
        # 事件线程
        self.event_thread = EventThread(self)

        self.myEvent()

    # 进度条完成事件
    def progress_bar_finish_Event(self):
        self.progress_bar_finish_signal.emit(True)

    # 线程延时,不影响UI界面(微秒)
    def msleep(self,i:int):
        self.built_thread.msleep(i)

    # 事件线程
    def add_event_start(self,target,agrs=tuple()):
        self.event_thread.add_f(target,agrs)
        self.event_thread.start()

    def myEvent(self):
        # 进度条事件
        self.built_thread.progress_bar_finish_signal.connect(self.progress_bar_finish_Event)


class Test(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.s = MyQProgressBar(self)
        # 添加事件执行函数
        self.s.add_event_start(self.t)
        # 添加完成事件函数
        self.s.progress_bar_finish_signal.connect(self.wanc)

    def wanc(self):
        print("完成")

    def t(self):
        for i in range(101):
            self.s.msleep(700)
            self.s.setValue(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Test()
    win.show()

    sys.exit(app.exec_())
