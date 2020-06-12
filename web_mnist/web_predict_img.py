from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
# from datetime import timedelta
import os
import cv2
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 附windows下中文路径图片解决方案：
def cv_imread(file_path=""):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img

def predict_img(input_img):
    print(input_img)
    # img = cv2.imread(input_img)
    img = cv_imread(input_img)
    print(img.shape)
    # grey_img = img[:, :, 0:1]
    grey_img = img
    print(grey_img.shape)
    shape_img = (grey_img.reshape(1, 28, 28, 1)).astype('float32') / 255

    # model = load_model('SaveModel/minist_model.h5')  #选取自己的.h模型名称
    model = load_model('SaveModel/minist_model_graphic.h5')  # 选取自己的.h模型名称
    prediction = model.predict_classes(shape_img)
    label = prediction[0]
    print(label)
    return label

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        print('post')
        # 通过file标签获取文件
        f = request.files['file']
        # print(f.filename)
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "图片类型：png、PNG、jpg、JPG、bmp"})
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'static\images', secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        show_path = "../static/images/" + f.filename
        label = predict_img(upload_path)
        return render_template('upload_ok.html',path = show_path, label = label)
        # return "上传成功"
    else:
        print('get')
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)