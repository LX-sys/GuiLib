# -*- coding:utf-8 -*-
# @time:2022/8/411:08
# @author:LX
# @file:__init__.py.py
# @software:PyCharm


s= [1,2,3,[1,3,4]]

def deep_copy(s):
    return s[3]

deep_copy(s).append(5)

print(s)