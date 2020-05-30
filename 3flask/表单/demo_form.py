from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def demo():
    # user = User.query.first()
    name = "hujianhua"
    age = "99"
    data = {
        "name": name,
        "age": age
    }
    return render_template("index.html", data=data)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        userage = request.form.get("userage")
        print(username)
        print(userage)
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)