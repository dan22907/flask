#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/24 20:09
# @Author : wangdan
# @File : comment.py
# @Software: PyCharm


import wtforms
from wtforms.validators import length,email,EqualTo,InputRequired


class CommentForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])

