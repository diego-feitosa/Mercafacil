from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@mercafacil_mysql_1:3306/admin'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(200), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)

    def __repr__(self):
        return '<Nome: %r' % self.name

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True, nullable=False)
    celular = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return '<Nome: %r | Celular: %r>' % (self.nome, self.celular)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"