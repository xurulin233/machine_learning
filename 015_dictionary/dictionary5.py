# 字典生成式
# 内置函数zip()
i = ['aaa', 'bbb', 'ccc']
j = [99, 98, 100]
A = {i:j for i, j in zip(i, j)}
print(A)
