from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask import Flask
from datetime import datetime

# 创建flask对象
app = Flask(__name__)


# 配置flask配置对象中键：SQLALCHEMY_DATABASE_URI
class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/sayhello"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "12345678"  # csrf_token


app.config.from_object(Config)

# 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy(app)


# 创建模型对象
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now(), index=True)


def __repr__(self):
    return '<User %r>' % self.username
