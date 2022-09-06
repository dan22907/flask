#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/25 10:47
# @Author : wangdan
# @File : imformation.py
# @Software: PyCharm


import wtforms
from wtforms.validators import length,DataRequired



class ImformationForm(wtforms.Form):
    sex = wtforms.StringField(validators=[DataRequired()])
    lived = wtforms.StringField(validators=[DataRequired()])
    signature = wtforms.StringField(validators=[DataRequired(),length(min=8,max=40)])
  #  username = wtforms.StringField(validators=[DataRequired(),length(min=2,max=9)])

    # def validate_sex(self,filed):
    #     sex = filed.data
    #     if sex in ["男","女"]:
    #        raise wtforms.ValidationError("性别不合法")


