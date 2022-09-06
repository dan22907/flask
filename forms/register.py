#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/24 20:08
# @Author : wangdan
# @File : register.py
# @Software: PyCharm


import wtforms
from wtforms.validators import length,email,EqualTo
from model.user import User
from model.email import EmailCaptchaModel




class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3,max=20)])
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6,max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    def validate_captcha(self,field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError("邮箱验证码错误！")

    def validate_email(self,field):
        email = field.data
        user_model = User.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError("邮箱已经存在！")