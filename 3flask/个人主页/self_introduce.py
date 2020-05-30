from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from flask import render_template

@app.route('/')
def index():
    data = {
        "name":"广东科学技术职业学院",
        "s":"男",
        "born":1990
    }
    return render_template("introduce.html", data = data)

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True,port=5000) # 开始运行flask应用程序, debug启动app的调试模式