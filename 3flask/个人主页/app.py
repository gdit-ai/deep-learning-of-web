from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from  flask import render_template
# import request
from flask import request

@app.route('/pos_test')
def pos_test():
    print(request.form)
    # print(request.args["name"])
    return "hello"

@app.route('/get_test')
def  get_test():
    print(request.args)
    print(request.args["name"])
    return request.args["name"]

@app.route('/')
def  index():
   data = {
       "name": "gdit",
       "age": 100
   }
   return  render_template('table.html',  data=data)

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式