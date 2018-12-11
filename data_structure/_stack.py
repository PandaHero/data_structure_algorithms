#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 11:26
@Author  : TianCi
@File    : _stack.py
@Software: PyCharm
@desc    : 列表实现栈
@method  :  stack()：创建一个新的空栈,返回一个空栈
            push()：添加一个新的元素到栈顶
            pop()：弹出栈顶元素
            peek()：查看栈顶元素
            is_empty()：判断栈是否为空
            size()：返回栈的元素个数
"""


class StackList(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """压栈"""
        self.__list.append(item)
        pass

    def pop(self):
        """出栈"""
        return self.__list.pop()

    def peek(self):
        """查看栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        if self.__list:
            return False
        else:
            return True

    def size(self):
        """返回栈的元素个数"""
        if self.is_empty():
            return 0
        else:
            return len(self.__list)


if __name__ == '__main__':
    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
