from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from  flask import  render_template

import pymysql

def get_sql_data():
    # 连接database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="123456",
                           db="cov",
                           charset="utf8")

    # 获取一个光标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典数据类型

    # 定义将要执行的sql语句
    sql = 'select user,pwd from userinfo;'
    # 拼接并执行sql语句
    cursor.execute(sql)

    # 取到查询结果
    ret1 = cursor.fetchone()  # 取一条
    ret2 = cursor.fetchmany(3)  # 取三条
    ret3 = cursor.fetchone()  # 取一条

    cursor.close()
    conn.close()

    print(ret1)
    print(ret2)
    print(ret3)
    return ret1

@app.route('/show')
def  hello():
   data = {
       "user": "gdit",
       "pwd": 100
   }
   # data = None
   ret_data = get_sql_data()
   print(ret_data)
   return  render_template('table.html',  data=ret_data)

@app.route('/')
def  index():
   return  "hello"

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式