#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:34
# @Author : wangdan
# @File : manage.py
# @Software: PyCharm


from flask import render_template,session,g
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import creat_app
from model import db,mail
from model.user import User

app = creat_app()
manager = Manager(app)

mail.init_app(app)

migrate = Migrate(app)
migrate.init_app(app,db)
manager.add_command("db", MigrateCommand)






@app.route("/updat")
def updata():
    return render_template("imformation_updata.html")

if __name__ == "__main__":
    manager.run()


# python manage.py db migrate
# python manage.py db init 初始化版本变更目录
# python manage.py db migrate 生成版本记录
# Python manage.py db upgrade 生效到数据库
# Python manage.py db downgrade 回滚




# python manage.py runserver -d -h 0.0.0.0 -p 9000





