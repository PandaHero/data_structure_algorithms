#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/22 10:07
@Author  : TianCi
@File    : hotPotato.py
@Software: PyCharm
@desc:烫山芋
"""
from pythonds.basic.queue import Queue


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
