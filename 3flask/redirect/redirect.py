from flask import Flask # 导入Flask模块
from flask import redirect

app = Flask(__name__) # 创建应用实例


@app.route('/redir')
def redir():
    return redirect('https://www.gdit.edu.cn/')

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式
