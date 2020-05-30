from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from  flask import  render_template
from flask import request
import pymysql

def insert_data_database(input_username, input_pwd):
    # 连接database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="123456",
                           # db="cov",
                           db="gdit_student",
                           charset="utf8")
    # 获取一个光标
    cursor = conn.cursor()

    sql = 'insert into student (user,pwd) values (%s,%s);'
    name = input_username
    pwd = input_pwd
    cursor.execute(sql, [name, pwd])

    # 涉及写操作要注意提交
    conn.commit()
    # 关闭连接
    cursor.close()
    conn.close()

@app.route('/',methods=["GET", "POST"])
def  index():
    print(request.method)
    if request.method == "POST":
        get_form = request.form
        print(get_form)
        username = request.form.get("user")
        pwd = request.form.get("pwd")
        print(username)
        print(pwd)
        insert_data_database(username, pwd)
        return render_template('show_table.html', data=get_form)
    else: # get请求
        return render_template('login.html')
if __name__ == '__main__':
	app.run(debug=True)