

DEBUG = True

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = 'san123'
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "sdfsadfskrwerfj1233453345"


# 邮箱配置
MAIL_SERVER = "smtp.163.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "15084920870@163.com"
MAIL_PASSWORD = "TZGKPARWIOKYSJWG"
MAIL_DEFAULT_SENDER = "15084920870@163.com"


# redis配置
REDIS_URL = "redis://:mN0PVh507MtBHwmvzsoObsFuUJUHkzTO5mcpNXf2lLk1kRjoCh70ItYlIOJXbFSF0krO+cVd5YUebLpY@192.168.2.179:6379/0"