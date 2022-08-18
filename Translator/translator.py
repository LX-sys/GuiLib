# -*- coding:utf-8 -*-
# @time:2022/8/1117:43
# @author:LX
# @file:translator.py
# @software:PyCharm

import sys
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton



class Translator(QWidget):
    def __init__(self,*args,**kwargs):
        super(Translator, self).__init__()
        self.trans = QTranslator()
        s = QPushButton(self)
        s.setText(self.tr('hello'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = Translator()
    translator.show()

    sys.exit(app.exec_())