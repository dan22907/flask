#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/24 20:09
# @Author : wangdan
# @File : article.py
# @Software: PyCharm


import wtforms
from wtforms.validators import length,email,EqualTo,InputRequired


class ArticleForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=200)])
    content = wtforms.StringField(validators=[length(min=5)])