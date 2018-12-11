#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/11 10:56
@Author  : TianCi
@File    : quick_sort.py
@Software: PyCharm
@desc:快速排序
"""
li = [30, 10, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 19, 50]


def quick_sort(li):
    less = []
    pivot_list = []
    more = []
    # 递归出口
    if len(li) <= 1:
        return li
    else:
        # 将第一个值作为基准
        pivot = li[0]
        for i in li:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more
