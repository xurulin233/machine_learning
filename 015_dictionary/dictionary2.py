# 字典元素的获取
# 第一种方式,使用[]
scores = {'张三': 100, '李四': 99, '王五': 98}


# 字典元素的删除
del scores['张三']  # 删除指定的key-value对
print(scores)

# 字典元素的清空 clear()
scores.clear()
print(scores)



scores1 = {'张三': 100, '李四': 99, '王五': 98}
print(scores1)
scores1['陈六'] = 98
print(scores1)


# 字典元素的修改
scores1['陈六'] = 100
print(scores1)
