#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/24 20:13
# @Author : wangdan
# @File : comment.py
# @Software: PyCharm

from flask import redirect, url_for, flash,g
from model import db
from flask import Blueprint,request
from flask_restful import Resource, Api
from forms.comment import CommentForm
from model.second_comment import SecondComment
from model.first_comment import FirstComment

comment_bp = Blueprint('comment_api',__name__, url_prefix='/')
api = Api(comment_bp)


class FirstCommentView(Resource):
    def post(self,article_id):
        form = CommentForm(request.form)
        if form.validate():
            content = form.content.data
            comment_model = FirstComment(content=content, author=g.user, article_id=article_id)
            db.session.add(comment_model)
            db.session.commit()
            return redirect(url_for("article.article_detail", article_id=article_id))
        else:
            flash("表单验证失败！")
            return redirect(url_for("article.article_detail", article_id=article_id))


class SecondCommentView(Resource):
    def post(self,comment_id):
        form = CommentForm(request.form)
        father_model = SecondComment.query.get(comment_id)
        if form.validate():
            content = form.content.data
            # father_model = SecondComment.query.filter_by(id=comment_id).first()
            print(father_model.id)
            comment_model = SecondComment(content=content, author=g.user, father_id=comment_id,
                                          article_id=father_model.article.id, flag=father_model.author.username)
            db.session.add(comment_model)
            db.session.commit()
            return redirect(url_for("article_detail", article_id=father_model.article.id))
        else:
            flash("表单验证失败！")
            return redirect(url_for("article.article_detail", article_id=father_model.article.id))
class SecondCommentUpView(Resource):
    def post(self,comment_id):
        form = CommentForm(data=request.json)
        father_model = FirstComment.query.get(comment_id)
        if form.validate():
            content = form.content.data
            comment_model = SecondComment(content=content, author=g.user, father_id=comment_id,
                                          article_id=father_model.article.id, flag='0')
            db.session.add(comment_model)
            db.session.commit()
            return redirect(url_for("article_detail", article_id=father_model.article.id))
        else:
            flash("表单验证失败！")
            return redirect(url_for("article.article_detail", article_id=father_model.article.id))


api.add_resource(FirstCommentView,"/first_comment/<int:article_id>")
api.add_resource(SecondCommentView,"/second_comment/<int:comment_id>")
api.add_resource(SecondCommentUpView,"/second_comment_up/<int:comment_id>")
