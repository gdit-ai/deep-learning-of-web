# 导入pymysql模块
import pymysql

# 连接database
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       db="gdit_student",
                       charset="utf8")

# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示


# 定义要执行的SQL语句
# sql = """
# CREATE TABLE USER1 (
# id INT auto_increment PRIMARY KEY ,
# name CHAR(10) NOT NULL UNIQUE,
# age TINYINT NOT NULL
# )ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
# """

# sql = """
# CREATE TABLE userinfo (
# id INT auto_increment PRIMARY KEY ,
# user CHAR(10) NOT NULL UNIQUE,
# pwd TINYINT NOT NULL
# )ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
# """

sql = """
CREATE TABLE student (
id INT auto_increment PRIMARY KEY ,
user CHAR(20) NOT NULL UNIQUE,
pwd int(10)
)ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
"""

print("create table")
# 执行SQL语句
cursor.execute(sql)

# sql = 'select * from userinfo where user = "%s" and pwd="%s"' % (user, pwd)
# sql = 'select * from userinfo'
# print(sql)
# res = cursor.execute(sql)
# print(res)
# # 进行判断
# if res:
#     print('登录成功')
# else:
#     print('登录失败')


# 关闭光标对象
cursor.close()

# 关闭数据库连接
conn.close()