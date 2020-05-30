import pymysql

# 连接database
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       db="gdit_student",
                       # db="cov",
                       charset="utf8")

# 获取一个光标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典数据类型

# 定义将要执行的sql语句
# sql = 'select user,pwd from student;'
# sql = 'select user from student;'
sql = 'select * from student;'
# 拼接并执行sql语句
cursor.execute(sql)

# 取到查询结果
ret1 = cursor.fetchone()  # 取一条
ret2 = cursor.fetchmany(3)  # 取三条
ret3 = cursor.fetchone()  # 取一条
print(ret1)
print(ret2)
print(ret3)

cursor.close()
conn.close()

#
# # 可以获取指定数量的数据
# cursor.fetchmany(3)
# # 光标按绝对位置移动1
# cursor.scroll(1, mode="absolute")
# # 光标按照相对位置(当前位置)移动1
# cursor.scroll(1, mode="relative")