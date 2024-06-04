#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 17:08
# @Author  : Arrow and Bullet
# @FileName: argsort.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366

import numpy as np  # 先引入numpy模块

A = [1, 0, 3]  # A是行向量，也称一维数组
B = np.argsort(A)  # 默认axis=-1
print(B)  # 结果 [1 0 2]
# 返回的是A按照从小到大排序的索引值

A = [[2, 4, 1], [3, 1, 5]]  # A是二维数组
B = np.argsort(A)  # 默认axis=-1，二维及以上按照行排列
print(B)  # 结果 [[2 0 1][1 0 2]]

A = [[2, 4, 1], [3, 1, 5]]  # A是二维数组
B = np.argsort(A, axis=0) # 默认axis=0，二维及以上按照列排列
print(B)  # 结果 [[0 1 0][1 0 1]]
