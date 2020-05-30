import pymysql

# 连接database
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       db="gdit_student",
                       charset="utf8")
# 获取一个光标
cursor = conn.cursor()
# 定义将要执行的SQL语句
sql = "delete from student where user=%s;"
# name = "june"
name = "ddddd"
# 拼接并执行SQL语句
cursor.execute(sql, [name])
# 涉及写操作注意要提交
conn.commit()
# 关闭连接

cursor.close()
conn.close()