#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/21 9:32
@Author  : TianCi
@File    : test.py
@Software: PyCharm
@desc:
"""


def sorted_algorithm(li):
    for j in range(len(li)):
        min_index = j
        # 先找到序列中最小的数,再循环以上操作
        for i in range(len(li)):
            if li[min_index] > li[i]:
                min_index = i
        li[j], li[min_index] = li[min_index], li[j]


lt = [3, 5, 2, 1, 8, 4]
# 求出lt的长度
n = len(lt)
# 外层循环确定比较的轮数，x是下标，lt[x]在外层循环中代表lt中所有元素
for x in range(n - 1):
    # 内层循环开始比较
    for y in range(x + 1, n):
        # lt[x]在for y 循环中是代表特定的元素，lt [y]代表任意一个lt任意一个元素。
        if lt[x] > lt[y]:
            # 让lt[x]和lt列表中每一个元素比较，找出小的
            lt[x], lt[y] = lt[y], lt[x]
            print(lt)
print(lt)
print(1 // 2)
