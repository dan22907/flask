#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:59
# @Author : wangdan
# @File : user.py
# @Software: PyCharm


from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    session,
    flash
)

from model import db, mail
from flask_mail import Message
from model.user import User
from model.articles import Article
from model.email import EmailCaptchaModel
import string
import random
from datetime import datetime
from forms.register import RegisterForm
from forms.login import LoginForm
from forms.imformation import ImformationForm
from werkzeug.security import check_password_hash
from libs.vercode import VercCode
from flask_restful import Api,Resource
from flask import make_response,g
from libs.response import generate_response


user_bp = Blueprint("user_api",__name__,url_prefix="/user")
api = Api(user_bp)


class Vercodeview(Resource):
    def post(self):
        path, vercode = VercCode.generate_vercode()
        session["vercode"] = vercode
        return render_template('login.html',path=path)


class LoginView(Resource):
    def get(self):
        temp = render_template("login.html")
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return  res
        # return render_template("login.html")
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            # ture_code = session.get("vercode")
            print("123")
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            print("fdfgg")
            if user and check_password_hash(user.password,password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                flash("邮箱和密码不匹配！")
                return redirect(url_for("user_api.loginview"))
        else:
            flash("邮箱或密码格式错误！")
            # return redirect(url_for("user.login"))
            temp = render_template('login.html',form=form)
            res = make_response(temp)
            res.headers['Content-Type'] = "text/html"
            return res
            # return render_template('login.html',form=form)




class RegisterView(Resource):
    def get(self):
        temp = render_template("register.html")
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res
        # return render_template("register.html")
    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # hash_password = generate_password_hash(password)
            # user = User(email=email, username=username, password=hash_password)
            # db.session.add(user)
            # db.session.commit()
            user = User.create_user(username,password,email)
            session['user_id'] = user.id
            return redirect("/")
            # return redirect(url_for("user_api.loginview"))
        # else:
        #     return redirect(url_for("user_api.registerview"))


class Logoutview(Resource):
    def get(self):
        # 清除session中所有的数据
        session.clear()
        return redirect(url_for('user_api.loginview'))



# memcached/redis/数据库中
class CaptchaView(Resource):
    def post(self):
        # GET,POST
        email = request.form.get("email")
        letters = string.ascii_letters + string.digits
        captcha = "".join(random.sample(letters,4))
        if email:
            message = Message(
                subject="邮箱测试",
                recipients=[email],
                body=f"【文】您的验证码为：{captcha}，该验证码 5 分钟内有效，请勿泄漏于他人！",
            )
            mail.send(message)
            captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
            if captcha_model:
                captcha_model.captcha = captcha
                captcha_model.create_time = datetime.now()
                db.session.commit()
            else:
                captcha_model = EmailCaptchaModel(email=email,captcha=captcha)
                db.session.add(captcha_model)
                db.session.commit()
            return jsonify({"code": 200})
        else:
            return jsonify({"code": 400,"message": "请先传递邮箱！"})


class ImformationView(Resource):
    def get(self):
        temp = render_template('imformation_updata.html')
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res


    def post(self):
        form = ImformationView(request.form)
        if form.form.validate():
            user = g.user
            user.username = form.username.data
            user.sex = form.sex.data
            user.signature = form.signature.data
            user.lived = form.lived.data
            db.session.commit()

        return redirect(url_for("user_api.imformationview"))

class UpdataImformation(Resource):
    def get(self):
        temp = render_template('updataimformation.html')
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res
    def post(self):
        form = ImformationForm(request.form)
        if form.validate():
            user = g.user
            #user.username = form.username.data
            user.sex = form.sex.data
            user.signature = form.signature.data
            user.lived = form.lived.data
            db.session.commit()
            return redirect(url_for('user_api.imformationview'))
        else:
            return generate_response(message={},data={})


class DisplayComment(Resource):
    def get(self):
        temp = render_template('all_comment.html')
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res


# class Thumbs_Up(Resource):
#     def post(self,article_id):
#         user_model = g.user
#         article_model = Article.query.get(article_id)
#         lis = [ each.id for each in article_model.manage]
#         if user_model.id in lis:





api.add_resource(LoginView,"/login")
api.add_resource(RegisterView,'/register')
api.add_resource(Logoutview,'/logout')
api.add_resource(CaptchaView,'/captcha')
api.add_resource(Vercodeview,'/vercode')
api.add_resource(ImformationView,'/imformation')
api.add_resource(UpdataImformation,"/updataimformmation")
api.add_resource(DisplayComment,"/displaycomment")



















