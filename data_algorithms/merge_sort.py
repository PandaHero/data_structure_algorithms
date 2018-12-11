#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/10 16:03
@Author  : TianCi
@File    : merge_sort.py
@Software: PyCharm
@desc:归并排序
"""
li = [4, 2, 1, 3, 5, 6]


def merge_sort(li):
    if len(li) <= 1:  # 若待拆分数组长度为1，直接返回
        return li
    num = len(li) // 2  # 取拆分中间位置
    left = merge_sort(li[:num])  # 递归拆分
    right = merge_sort(li[num:])
    return merge(left, right)


def merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    print(result)
    return result


merge_sort(li)
