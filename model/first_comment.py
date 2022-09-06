#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:45
# @Author : wangdan
# @File : answer.py
# @Software: PyCharm

from model import db
from datetime import datetime

class FirstComment(db.Model):
    __tablename__ = "first_comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    article_id = db.Column(db.Integer,db.ForeignKey("article.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    __table_arg__ = {"mysql_charset": "utf8"}

    article = db.relationship("Article",backref=db.backref("comments",order_by=create_time.desc()))
    author = db.relationship("User",backref="first_comments")





