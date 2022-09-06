#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:50
# @Author : wangdan
# @File : __init__.py
# @Software: PyCharm



from .article import article_bp
from .user import user_bp
from .comment import comment_bp



def init_app(app):
    app.register_blueprint(article_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(comment_bp)


