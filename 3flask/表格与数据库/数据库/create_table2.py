# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       db="gdit_student",
                       charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
sql = """
CREATE TABLE student (
user CHAR(20),
pwd int(10)
); """
print("create table")
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()