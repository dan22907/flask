#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/22 10:01
# @Author : wangdan
# @File : second_comment.py
# @Software: PyCharm


from model import db
from datetime import datetime


class SecondComment(db.Model):
    __tablename__ = "second_comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    father_id = db.Column(db.Integer, db.ForeignKey("first_comment.id"))
    article_id = db.Column(db.Integer,db.ForeignKey("article.id"))
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    flag = db.Column(db.String(150),default='first')

    author = db.relationship("User", backref="second_comments")
    father_comment = db.relationship("FirstComment", backref="children_comments")
    article = db.relationship("Article", backref=db.backref("second_comments", order_by=create_time.desc()))


