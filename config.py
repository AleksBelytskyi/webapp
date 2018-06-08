import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = None
    MAIL_PORT = 587
    MAIL_USE_TLS = 0
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    ADMINS = ['belitckiu.lex@gmail.com']
    WEB = 13

