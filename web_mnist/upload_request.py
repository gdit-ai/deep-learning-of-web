from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
# from datetime import timedelta
import os

app = Flask(__name__)

# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
# 输出
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        print('post')
        # 通过file标签获取文件
        f = request.files['file']
        print(f.filename)
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "图片类型：png、PNG、jpg、JPG、bmp"})
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        show_path = "../static/images/" + f.filename
        return render_template('upload_ok.html',path = show_path)
        # return "上传成功"
    else:
        print('get')
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)