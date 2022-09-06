#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/21 21:08
# @Author : wangdan
# @File : access_limit.py
# @Software: PyCharm


from flask import g,redirect,url_for
from functools import wraps


def login_required(func):
    # @wraps这个装饰器一定不要忘记写了
    @wraps(func)
    def wrapper(*args,**kwargs):
        if hasattr(g,'user'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for("user_api.loginview"))

    return wrapper