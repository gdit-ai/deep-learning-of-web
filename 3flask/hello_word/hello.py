from flask import Flask # 导入Flask模块
from flask import render_template
app = Flask(__name__) # 创建应用实例
import json
import flask

print(flask.__version__)

@app.route('/') # 使用route装饰器创建一个路由
def hello(): # 视图函数，访问此路由时执行的函数
	# return 'Hello World' # 视图函数的返回值，称之为 ‘响应’
    return render_template('hello.html')

@app.route('/jsj')
def hello2():
	return '计算机工程技术学院（人工智能学院）'

@app.route('/json')
def json_test():
	iidct = {"name" :"gdit", "age": 20}
	print(type(iidct))
	print(iidct["name"])

	ijson = json.dumps(iidct)
	print(type(ijson))
	# print(ijson["name"])
	return ijson

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式
