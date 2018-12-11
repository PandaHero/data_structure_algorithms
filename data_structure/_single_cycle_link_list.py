#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 14:41
@Author  : TianCi
@File    : _single_cycle_link_list.py
@Software: PyCharm
@desc:单向循环链表
"""


class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        if node:  # 如果传递的节点不为空，需要指向自己
            node.next = node

    # 判断单向循环列表是否为空
    def is_empty(self):
        return self.__head

    # 获取列表长度
    def length(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self.__head
            while cur.next != self.__head:
                count += 1
                cur = cur.next
        return count

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head  # node.next=cur.next

    def insert(self, pos, item):
        node = Node(item)
        count = 0
        cur = self.__head
        if pos < 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    # 遍历打印
    def travel(self):
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            print(cur.element)
            cur = cur.next
        print(cur.element)  # 打印最后一个元素

    def remove(self, item):
        cur = self.__head
        pre=None
        while cur.next!=self.__head:
            if cur.item==item:
                pre.next=cur.next
                return True
            else:
                pre=cur
                cur=cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:  # 判断头节点是否满足
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False
