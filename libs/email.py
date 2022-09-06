#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/23 14:57
# @Author : wangdan
# @File : email.py
# @Software: PyCharm


from flask_mail import Mail, Message

def sent_email(receiver,captcha):
    mail = Mail()
    message = Message(
        subject="邮箱测试",
        recipients=[receiver],
        body=f"【文】您的验证码为：{captcha}，该验证码 5 分钟内有效，请勿泄漏于他人！",
    )
    mail.send(message)
