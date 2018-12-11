#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 14:19
@Author  : TianCi
@File    : _queue.py
@Software: PyCharm
@desc    :队列的实现
"""


class Queue(object):
    def __init__(self):
        self.__list = []
        pass

    def enqueue(self, item):
        """往队列尾部添加一个新元素"""
        self.__list.append(item)
        pass

    def dequeue(self):
        """从队列头部取出一个元素"""
        if self.is_empty():
            return None
        else:
            return self.__list.pop(0)
        pass

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []
        pass

    def size(self):
        """队列长度"""
        return len(self.__list)
        pass


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
