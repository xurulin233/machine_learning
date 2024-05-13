# 字典元素的获取
# 第一种方式,使用[]
scores = {'张三': 100, '李四': 99, '王五': 98}
print(scores['张三'])
# 第二种方式,使用get()方法
print(scores.get('张三'))
print(scores.get('陈六', 99))  # 99是在查找不存在时提供的一个默认值
