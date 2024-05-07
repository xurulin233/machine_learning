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

# 改变数组形状,重塑操作不改变数组中的元素总数，只是改变其布局。
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped = arr.reshape(3, 2)
print(reshaped)

# 水平拼接数组
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.hstack((arr1, arr2))
print(concatenated)

'''
这个操作在你需要将来自不同数据源的数据按列合并时非常有用，如合并两个数据集的特征。
'''

# 垂直拼接数组
concatenated = np.vstack((arr1, arr2))
print(concatenated)


A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)  # 输出解向量


A = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)  # 特征值
print(eigenvectors)  # 特征向量


