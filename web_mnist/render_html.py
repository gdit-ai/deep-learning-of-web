from flask import Flask, render_template, request, jsonify



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    print(request.method)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)