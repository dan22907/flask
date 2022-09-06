#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/23 23:02
# @Author : wangdan
# @File : redis.py
# @Software: PyCharm

import time
from flask_redis import FlaskRedis
from manage import app

redis_cli = FlaskRedis()
redis_cli.init_app(app)


def mark_dyn_data(id, data):
    user_id = str(id).encode('utf-8')
    data = str(data).encode('utf-8')
    expires = int(time.time()) + 60
    data_key = "dyn_data/%s" % user_id
    p = redis_cli.pipeline()
    p.set(data_key, data)
    p.expireat(data_key, expires)
    p.execute()

def get_dyn_data(id):
    user_id = str(id).encode('utf-8')
    data_key = "dyn_data/%s" % user_id
    data = redis_cli.get(data_key)
    if data:
        return int(data)
    return None