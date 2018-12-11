#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 11:47
@Author  : TianCi
@File    : single_link_list1.py
@Software: PyCharm
@desc:单链表节点作业
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, head=None):
        self.__head = head

    # 判断链表是否为空
    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            self.__head = node
            node.next = cur

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre = self.__head
            while count < pos - 1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.elem)
            cur = cur.next
        else:
            print("none")

    def remove(self, item):
        cur = self.__head
        pre = None
        if self.is_empty():
            return None
        while cur:
            if cur.elem == item:
                # 判断节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        return False

    def search(self, item):
        cur = self.__head
        if self.is_empty():
            return False
        while cur:
            if cur.elem == item:
                return True
            cur = cur.next
        return False
