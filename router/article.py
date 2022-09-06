#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/20 15:58
# @Author : wangdan
# @File : article.py
# @Software: PyCharm


from flask import Blueprint,render_template,request,g,redirect,url_for,flash,make_response
from libs.access_limit import login_required
from forms.article import ArticleForm
from model.articles import Article,User_Artilce
from model.user import User
from model import db
from sqlalchemy import or_,and_
from flask_restful import Api,Resource
from libs.response import generate_response

article_bp = Blueprint("article",__name__,url_prefix="/")
api = Api(article_bp)

class Index(Resource):
# @article_bp.route("/")
    def get(self):
        articles = Article.query.order_by(db.text("-create_time")).all()
        temp = render_template("index.html",articles=articles)
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res
        # return render_template("index.html",articles=articles)

class Public_Article(Resource):
# @article_bp.route("/article/public",methods=['GET','POST'])
    @login_required
    def get(self):
        # 判断是否登录，如果没有登录，跳转到登录页面
        temp = render_template("public_article.html")
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res
        # return render_template("public_article.html")
    def post(self):
        form = ArticleForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            article = Article(title=title,content=content,author=g.user)
            db.session.add(article)
            db.session.commit()
            return redirect("/")
        else:
            flash("标题或内容格式错误！")
            return redirect(url_for("article.public_article"))

class Article_Detail(Resource):
# @article_bp.route("/article/<int:article_id>")
    @login_required
    def get(self,article_id):
        try:
            user_model = g.user
        finally:
            article = Article.query.get(article_id)
            lis = [each.id for each in article.manage]
            sign = 1 if user_model.id not in lis else 0
            content = {"article":article,"sign":sign}
            temp = render_template("detail.html",**content)
            res = make_response(temp)
            res.headers['Content-Type'] = "text/html"
            return res
        # return render_template("detail.html", article=article)



class Search(Resource):
# @article_bp.route("/search")
    def get(self):
        q = request.args.get("q")
        articles =Article.query.filter(or_(Article.title.contains(q),Article.content.contains(q))).order_by(db.text("-create_time"))
        temp = render_template("index.html",articles=articles)
        res = make_response(temp)
        res.headers['Content-Type'] = "text/html"
        return res
        # return render_template("index.html",articles=articles)

class Star(Resource):
    def post(self,article_id):
        # user_model = User.query.get(1)
        user_model = g.user
        if user_model:
            article_model = Article.query.get(article_id)
            lis = [ each.id for each in article_model.manage]
            if user_model.id not in lis:
                # article_model = Article.query.get(article_id)
                # user_model = g.user
                article_model.stars += 1
                article_user1 = User_Artilce(user_id=user_model.id,article_id=article_id)
                db.session.add(article_user1)
                db.session.commit()
                # return redirect(url_for('article.article_detail',article_id=article_id))
                # return generate_response(message="增加成功",data={})
            else:
                article_model.stars -= 1
                User_Artilce.query.filter(and_(User_Artilce.user_id==user_model.id,User_Artilce.article_id==article_id)).delete()
                db.session.commit()
                # return redirect(url_for('article.article_detail', article_id))
                # return generate_response(message="减少成功", data={})
            return redirect(url_for('article.article_detail', article_id=article_id))
        else:
            flash("请先登录")


api.add_resource(Index,'/')
api.add_resource(Public_Article,'/article/public')
api.add_resource(Article_Detail,'/article/<int:article_id>')
api.add_resource(Search,'/search')
api.add_resource(Star,'/star/<int:article_id>')












