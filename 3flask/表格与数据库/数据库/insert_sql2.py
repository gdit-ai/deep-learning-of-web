import pymysql
def insert_one_test():
    sql = 'insert into student (user,pwd) values (%s,%s);'
    name = 'wuli'
    pwd = '123456789'
    cursor.execute(sql, [name, pwd])

def insert_many_test():
    # 定义要执行的sql语句
    sql = 'insert into student(user,pwd) values(%s,%s);'
    data = [
        ('a', '147'),
        ('b', '258'),
        ('c', '369')
    ]
    # 拼接并执行sql语句
    cursor.executemany(sql, data)

# 连接database
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       # db="cov",
                       db="gdit_student",
                       charset="utf8")
# 获取一个光标
cursor = conn.cursor()
insert_one_test()
insert_many_test()

# 涉及写操作要注意提交
conn.commit()
# 关闭连接
cursor.close()
conn.close()