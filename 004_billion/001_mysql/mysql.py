import pymysql
# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='password', db='myDB')
# 创建游标对象
cursor = conn.cursor()
# 定义 SQL 语句
insert_sql = "INSERT INTO person VALUES (%s, %s, %s)"

# 定义数据
data = [
    ('1', '张三', 18),
    ('2', '李四', 19),
    ('3', '王五', 20)
]
# 批量插入数据
cursor.executemany(insert_sql, data)
# 提交
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

