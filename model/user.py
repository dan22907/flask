#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:40
# @Author : wangdan
# @File : user.py
# @Software: PyCharm

from model import db
from _datetime import datetime
from random import randint
from werkzeug.security import generate_password_hash



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    _password = db.Column("password",db.String(200),nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now)
    avartar = db.Column(db.String(250),default='dafault_image/'+f"{randint(1,12)}"+'.jpg')
    sex = db.Column(db.String(20))
    signature = db.Column(db.String(150))
    lived = db.Column(db.String(50))



    __table_arg__ = {"mysql_charset": "utf8"}

    @property  # -----> password.setter
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @classmethod
    def create_user(cls, username, password, email):
        user = cls()
        user.username = username
        user.password = password
        user.email = email
        db.session.add(user)
        db.session.commit()
        return user



