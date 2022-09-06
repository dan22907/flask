#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:44
# @Author : wangdan
# @File : questions.py
# @Software: PyCharm

from datetime import datetime
from model import db

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    stars = db.Column(db.Integer,default=0)

    # manage = db.relationship("User", secondary='user_article', backref="likes")
    # __mapper_args__ = {
    #     "order_by": create_time.desc()
    # }
    __table_arg__ = {"mysql_charset": "utf8"}

    author = db.relationship("User",backref="my_articles")

    manage = db.relationship("User", secondary='user_article', backref="thumbs_up")

# User_Artilce = db.Table("user_article",
#                           db.Column("user_id",db.ForeignKey("user.id")),
#                           db.Column("article_id",db.ForeignKey("article.id"))
#                           )


class User_Artilce(db.Model):
    __tablename__ = "user_article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))


# class UserArticle(db.Model):
#     __tablename__ = "user_article"
#     article1_id = db.Column(db.Integer,primary_key=('article.id'))
#     author1_id = db.Column(db.Integer,primary_key=('user.id'))

