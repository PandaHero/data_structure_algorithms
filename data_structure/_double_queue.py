#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 14:35
@Author  : TianCi
@File    : _double_queue.py
@Software: PyCharm
@desc    : 双端队列
"""


class DoubleQueue(object):
    def __init__(self):
        self.__item = []
        pass

    def add_front(self, item):
        """往双端队列头部添加一个新元素"""
        self.__item.insert(0, item)
        pass

    def add_rear(self, item):
        """往双端队列尾部添加一个新元素"""
        self.__item.append(item)
        pass

    def remove_front(self):
        """从双端队列头部取出一个元素"""
        self.__item.pop(0)
        pass

    def remove_rear(self):
        """从双端队列尾部取出一个元素"""
        self.__item.pop()
        pass

    def is_empty(self):
        """判断队列是否为空"""
        return not self.__item
        pass

    def size(self):
        """队列长度"""
        return len(self.__item)
        pass
