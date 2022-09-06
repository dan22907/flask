#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/24 17:55
# @Author : wangdan
# @File : response.py
# @Software: PyCharm


def generate_response(status_code = 1000, message = 'ok', data = None):
    if data is None:
        data = []
    return {
        "status_code": status_code,
        "message": message,
        "data": data
    }