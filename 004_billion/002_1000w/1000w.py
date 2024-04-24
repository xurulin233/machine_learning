import pymysql
import csv


file_path = "1000w-douban-movie.csv"
table_name = "douban"
count = 0

# 连接数据库
connect = pymysql.connect(host='localhost', user='root', password='password', db='commentsDB')

# 创建游标对象
cursor = connect.cursor()
# 定义 SQL 语句
drop_sql = 'DROP TABLE IF EXISTS douban' 

cursor.execute(drop_sql)
connect.commit()


creat_sql = "CREATE TABLE douban(id INTEGER PRIMARY KEY,movie_name VARCHAR(150) CHARACTER SET utf8,score DECIMAL(2,1),reviex_people INT,star_distruvbution VARCHAR(50),craw_date DATE,username VARCHAR(50) CHARACTER SET utf8mb4,date DATE,star INT,comment VARCHAR(1200) CHARACTER SET utf8mb4,conmement_distibutionn VARCHAR(50),like_people INT)"

try:
    cursor.execute(creat_sql)
    connect.commit()
except:
    print("表已存在")
    print('成功创建表格')


with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f,delimiter=',')
    # 跳过第一行标题行
    next(reader)
    for row in reader:
        # 将每一行数据插入到数据库中
      #  print((row[0], row[1], row[2],row[3], row[4], row[5],row[6], row[7], row[8],row[9], row[10], row[11]))
        insert_sql = "INSERT INTO douban VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        count += 1 
        if(count % 10000 == 0):
            print(count)
        cursor.execute(insert_sql, tuple(row))
# 提交
connect.commit()


# 关闭游标
cursor.close()
# 关闭连接
connect.close()





