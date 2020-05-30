from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from  flask import  render_template
from flask import request

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
        return render_template('index.html', data=get_form)
    else: # get请求
        return render_template('login.html')
if __name__ == '__main__':
	app.run(debug=True)