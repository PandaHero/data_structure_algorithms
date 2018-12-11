#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/10 11:58
@Author  : TianCi
@File    : shell_sort.py
@Software: PyCharm
@desc:希尔排序
"""
li = [5, 4, 3, 2, 1]


def shell_sort(li):
    n = len(li)
    gap = n // 2  # 步长增量
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and li[j] < li[j - gap]:
                li[j], li[j - gap] = li[j - gap], li[j]
                j -= gap
        gap = gap // 2
    return li


print(shell_sort(li))

shell_sort(li)
