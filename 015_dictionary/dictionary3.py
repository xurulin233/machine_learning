# 字典元素的获取
# 第一种方式,使用[]
scores = {'张三': 100, '李四': 99, '王五': 98}


# 获取所有的键
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys)) # 将所有的键转换成列表



# 获取所有的值
values = scores.values()
print(values)
print(type(values))
print(list(values))


items = scores.items()
print(items)
print(type(items))
print(list(items))


for i in scores:
    print(i, scores[i], scores.get(i))

