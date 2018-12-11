#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/20 14:00
@Author  : TianCi
@File    : bubbling_sorted_algorithms.py
@Software: PyCharm
@desc:冒泡排序
"""
li = [10, 30, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 19, 50]


def bubbling_sorted(li):
    for i in range(len(li) - 1):
        count = 0
        for j in range(0, len(li) - i - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                count += 1
        if count == 0:
            return li
    return li


print(bubbling_sorted(li))
