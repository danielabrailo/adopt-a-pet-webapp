import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'adoptapetinisrael@gmail.com'
    MAIL_PASSWORD = ''
