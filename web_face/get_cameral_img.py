from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from  flask import render_template
from flask import request
import base64
import numpy as np
import cv2

@app.route('/ajax',methods=["get","post"])
def hello_world4():
    # name = request.values.get("name")
    print(request.values)
    img_base64 = request.values.get("img")
    print(img_base64[22:])
    img_base64_encode = img_base64[22:]
    img_b64decode = base64.b64decode(img_base64_encode)  # base64解码
    print(img_b64decode)
    img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
    cv2.imwrite("./save.jpg",img)
    cv2.imshow("img", img)
    cv2.waitKey()
    return '10000'

@app.route('/')
def  index():
   return  render_template('camera.html')

if __name__ == '__main__': # 判断是否运行此文件，还是被当做模块导入
	app.run(debug=True) # 开始运行flask应用程序, debug启动app的调试模式