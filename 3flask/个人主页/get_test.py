from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from flask import request

@app.route('/',)
def  index():
    print("------------------")
    print(request)
    print(request.method)
    print(request.args)
    print(request.args.get("name"))
    request_name = request.args.get("name")
    print("------------------")
    return request_name

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式