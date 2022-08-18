# -*- coding:utf-8 -*-
# @time:2022/7/2815:50
# @author:LX
# @file:typewriter.py
# @software:PyCharm

'''
    打字机TextEdit
'''

import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QTextEdit,QTextBrowser


# 打字机线程
class TypewriterThread(QThread):
    typewriting = pyqtSignal(str)
    typewrite_end = pyqtSignal()  # 完成时触发信号
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.__text = ""

    def setText(self,text:str):
        self.__text = text

    def text(self)->str:
        return self.__text

    def run(self):
        for c in self.text():
            self.typewriting.emit(c)
            self.msleep(50)
        self.typewrite_end.emit()



class Typewriter(QTextBrowser):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.defaultStyle()
        self.ty = TypewriterThread()
        self.ty.typewriting.connect(self.__write)

    def setText(self, text: str,typewriting:bool=False) -> None:
        if typewriting:
            self.ty.setText(text)
            self.ty.start()
        else:
            super(Typewriter, self).setText(text)

    def append(self, text: str,typewriting:bool=False) -> None:
        if typewriting:
            self.ty.setText(text)
            self.ty.start()
        else:
            super(Typewriter, self).append(text)

    def tyObj(self)->TypewriterThread:
        return self.ty

    def __write(self,c):
        # 这个会自带换行
        # self.append(c)
        # 这个不会自带换行
        self.insertPlainText(c)
        # 光标始终在最后
        self.moveCursor(QTextCursor.End)

    # 默认风格
    def defaultStyle(self):
        self.setStyleSheet('''
QWidget{
background-color: rgb(255, 255, 255);
font: 12pt "黑体";
}
        ''')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Typewriter()
    test.setText("Hello World!",True)
    test.append("Hello World")
    test.show()
    sys.exit(app.exec_())