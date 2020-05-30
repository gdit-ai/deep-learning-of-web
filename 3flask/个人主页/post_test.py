from flask import Flask # 导入Flask模块
from flask import request
from  flask import render_template

app = Flask(__name__) # 创建应用实例

@app.route('/',methods = ["get", "post"])
def  index():
    print("------------------")
    print(request.method)
    print(request.form)
    print(request.form.get("username"))
    print(request.form.get("password"))
    print("------------------")
    response_data = "广东科学技术职业学院"
    return render_template("post_form.html")

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True, port=80) # 开始运行flask应用程序, debug启动app的调试模式
	# app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式