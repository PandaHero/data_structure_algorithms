#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/13 9:49
@Author  : TianCi
@File    : _double_link_list.py
@Software: PyCharm
@desc:双向链表
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.pre = None


class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head  # node指向下一个节点
            self.__head.pre = node
            self.__head = node
        # node.next.pre = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:  # 判断下一个节点是否为空
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, pos, item):
        cur = self.__head
        count = 0
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            if self.is_empty():
                self.__head = node
            else:
                while count < pos - 1:
                    count += 1
                    cur = cur.next
                node.next = cur.next
                cur.next.pre = node
                node.pre = cur
                cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self.__head
            # 首结点的元素就是要删除的元素
            if cur.elem == item:
                # 如果链表只有一个节点
                if not cur.next:
                    self.__head = None
                else:
                    # 将第二个节点的pre指向None
                    cur.next.pre = None
                    self.__head = cur.next
                return
            while cur.next:
                if cur.elem == item:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                    break
                else:
                    cur = cur.next

    def search(self, item):
        pass


if __name__ == '__main__':
    double_link_list = DoubleLinkList()
    double_link_list.add(1)
    double_link_list.append(2)
    double_link_list.append(3)
    double_link_list.insert(1, 1.5)
    double_link_list.remove(1)
    print(double_link_list.travel())
