from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/xx"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mysql@127.0.0.1:3306/xx"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@127.0.0.1:3306/db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@server/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WTF_CSRF_ENABLED'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    age = db.Column(db.Integer, default=18)

    def __repr__(self):
        return 'User:%s' % self.name


@app.route('/')
def demo():
    user = User.query.first()
    name = user.name
    age = user.age
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
        user = User(name=username, age=userage)
        db.session.add(user)
        db.session.commit()
    return render_template("login.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    manager.run()