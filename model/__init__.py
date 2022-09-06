#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:41
# @Author : wangdan
# @File : __init__.py
# @Software: PyCharm


from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()


def init_app_db(app):
    db.init_app(app)
    # 自动创建数据表，要求连接数据库的用户有创建权限
    # db.create_all(app=app)


from . import user
from . import first_comment
from . import email
from . import articles
from . import second_comment



