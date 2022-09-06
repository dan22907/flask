#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:43
# @Author : wangdan
# @File : email.py
# @Software: PyCharm

from model import db
from datetime import datetime

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    captcha = db.Column(db.String(10),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    # __table_arg__ = {"mysql_charset" : "utf8"}

