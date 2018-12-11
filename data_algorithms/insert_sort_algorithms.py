#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/21 11:51
@Author  : TianCi
@File    : insert_sort_algorithms.py
@Software: PyCharm
@desc:插入排序:有一个已经排序好的n序列，当对第n+1个元素进行排序时，若第n+1元素大于(小于)该n元素，则往前排。
"""
import numpy

li = [30, 10, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 19, 50]


def insert_sort(li):
    for i in range(1, len(li)):
        for j in range(i, 0, -1):
            print(i, j, li[j], li[j - 1])
            if li[j] < li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
            else:
                break
            print(li)


def fibolaqie(num):
    a, b = 0, 1


if __name__ == '__main__':
    insert_sort(li)
    arr = numpy.array([1, 2, 3])
    print(arr)
    x = 1
    X = 2
    print(x, X)
    from collections import Iterable
    import os

    print(isinstance(range(10), Iterable))
    print(os.getcwd())  # current work directory
