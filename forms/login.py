#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/24 20:08
# @Author : wangdan
# @File : login.py
# @Software: PyCharm


import wtforms
from wtforms.validators import length,email,EqualTo,InputRequired



class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6,max=20)])