import numpy as np
# 从Python列表创建数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 创建一个全零数组
zeros = np.zeros((3, 4))  # 参数是一个表示形状的元组
print(zeros)


# 创建一个全一数组
ones = np.ones((2, 3))
print(ones)

# 创建一个空数组，其实是未初始化的数组，里面的值是随机的
empty = np.empty((2, 2))
print(empty)


# 创建一个具有指定范围内的数组
# 输出结果为[10 11 12 13 14 15 16 17 18 19]
range_array = np.arange(10, 20)
print(range_array)

# 创建一个线性空间数组
# 从0到1，总共5个元素，而且是线性（均等）分布
linspace_array = np.linspace(0, 1, 5)

print(linspace_array)

#这个初始化功能在数据可视化、科学计算的时候非常有用，一般用来给自变量x取样
