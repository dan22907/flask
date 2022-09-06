from flask import Flask,session,g
from model.user import User
from model.articles import Article
import os


def creat_app(config=None):
    app = Flask(__name__)
    # app.config 本质上就是dict ，继承dict类 ，添加了from_object 方法
    app.config.from_object('config.config')
    # 加载系统配置，根据不同系统加载不同环境变量
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    import router
    router.init_app(app)

    import model
    model.init_app_db(app)

    @app.before_request
    def before_request():
        user_id = session.get("user_id")
        if user_id:
            try:
                user = User.query.get(user_id)
                # 给g绑定一个叫做user的变量，他的值是user这个变量
                # setattr(g,"user",user)
                g.user = user
            except:
                g.user = None

    # 请求来了 -> before_request -> 视图函数 -> 视图函数中返回模板 -> context_processor

    @app.context_processor
    def context_processor():
        if hasattr(g, "user"):
            return {"user": g.user}
        else:
            return {}

    return app



