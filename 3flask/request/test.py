import face_recognition
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
# Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

    # print("get")

    return'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask网页上传图片演示</title>
</head>
<body>
    <form enctype='multipart/form-data' method='POST'>
        <input type="file" name="file" style="margin-top:20px;"/>
        <input type="submit" value="上传" class="button-new" style="margin-top:15px;"/>
    </form>
</body>
</html>
'''

@app.route('/sendrequest', methods=['GET', 'POST'])
def sendrequest():
    print(request.method)
    print(request.args)
    print(type(request.args))
    print('----------------------')
    print(request.form)
    # return 'success'
    return request.method


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)