import pymysql

# 连接database
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       # db="cov",
                       db="gdit_student",
                       charset="utf8")
# 获取一个光标
cursor = conn.cursor()

# 定义要执行的sql语句
sql = 'insert into userinfo(user,pwd) values(%s,%s);'
# data = [
#     ('july', '147'),
#     ('june', '258'),
#     ('marin', '369')
# ]

data = [
    ('a', '147'),
    ('b', '258'),
    ('c', '369')
]
# 拼接并执行sql语句
cursor.executemany(sql, data)

# 涉及写操作要注意提交
conn.commit()

# 关闭连接
cursor.close()
conn.close()

