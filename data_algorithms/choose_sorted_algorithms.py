#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/20 15:40
@Author  : TianCi
@File    : choose_sorted_algorithms.py
@Software: PyCharm
@desc:选择排序:从序列中找到最小的/最大的元素，存放在序列的起始位置，
        然后再从剩余的序列中找到最大/最小的元素放在排序的末尾，直到所有元素排序完成
        时间复杂度：o(n^2)
        稳定性：不稳定
"""
li = [10, 30, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 19, 50]


def choose_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            print("第一轮循环:", li[min_index], li[j])
            if li[min_index] > li[j]:
                print("第二轮循环:", li[min_index], li[j])
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
        print(li)


choose_sort(li)
