#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 11:00
@Author  : TianCi
@File    : _sorted_algorithms.py
@Software: PyCharm
@desc: 排序算法:冒泡排序、选择排序、插入排序、快速排序、希尔排序、归并排序、堆排序
"""
lis = [10, 30, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 19, 50]


def bubble_sort(lis):
    """冒泡排序"""
    """时间复杂度:o(n^2)"""
    count = len(lis)
    for i in range(count - 1):
        for j in range(i + 1, count):
            print(lis[i], lis[j], lis)
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
        print("******")
    return lis


def bubble_sort2(lis):
    """冒泡排序"""
    count = len(lis)
    for i in range(count - 1):
        count = 0
        for j in range(0, count - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                count += 1
        if count == 0:
            break
    return lis


print(bubble_sort(lis))
