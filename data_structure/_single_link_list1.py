#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/6 15:00
@Author  : TianCi
@File    : _single_link_list1.py
@Software: PyCharm
@desc:单链表实现
"""


class Node(object):
    """单链表的节点"""

    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):  # 设置默认参数
        self.__head = node  # 私有化属性

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """获取链表长度"""
        # cursor游标，用来遍历链表(self.__head保存的是节点的地址值)
        cursor = self.__head
        # 计数
        count = 0
        while cursor:
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        """遍历链表"""
        cursor = self.__head
        while cursor:
            print(cursor.element)
            cursor = cursor.next

    def add(self, item):
        """添加头部元素O(1)"""
        node = Node(item)
        # 将新节点的链接域指向头节点(把头节点的地址值给next)
        node.next = self.__head
        # 将链表的头节点指向新节点(把新节点的地址值给head)
        self.__head = node

    def append(self, item):
        """添加尾部元素O(n)"""
        # 创建新节点
        node = Node(item)
        # 判断节点是否为空
        if self.is_empty():
            self.__head = node
        else:
            # 初始化游标位置
            cursor = self.__head
            # 判断游标的链接域是否为空
            while cursor.next:
                cursor = cursor.next
            cursor.next = node

    def insert(self, pos, item):
        """任意位置添加元素O(n)"""
        node = Node(item)
        count = 0
        pre = self.__head
        # 如果位置小于0,执行头部添加元素
        if pos <= 0:
            self.add(item)
        # 如果位置大于等于链表长度,执行尾部添加元素
        elif pos >= self.length():
            self.append(item)
        else:
            # 循环结束后，游标指向插入位置的前一个节点
            while count < pos - 1:
                # 获取后一个节点
                pre = pre.next
                count += 1
            # 将新节点的node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除元素"""
        cursor = self.__head
        pre = None
        while cursor:
            if cursor.element == item:
                # 先判断此节点是否是头节点
                if cursor == self.__head:
                    self.__head = cursor.next
                    return True
                pre.next = cursor.next
                return True
            else:
                pre = cursor
                cursor = cursor.next
        return False

    def search(self, item):
        """查找元素O(n)"""
        cursor = self.__head
        # 判断节点是否存在
        while cursor:
            # 判断元素是否相等
            if cursor.element == item:
                return True
            else:
                # 获取下一个节点
                cursor = cursor.next
        # 循环结束返回False
        return False


if __name__ == '__main__':
    link_list = SingleLinkList()
    # print(link_list.is_empty())
    # print(link_list.length())
    link_list.append(1)
    link_list.add(2)
    link_list.append(1)
    link_list.append(1)
    link_list.insert(2, 100)
    link_list.remove(1)
    link_list.remove(100)
    print(link_list.travel())
