import os


BASEDIR = os.path.abspath(os.getcwd())

class Config():
    DEBUG = False
    DATE_FORMAT = '%Y-%m-%d'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'yjJwlkj5nI2Vee2lq6oZwlvedo0'


class ProductionConfig(Config):
    SERVER_NAME = 'flinkshortener.herokuapp.com'
    PREFERRED_URL_SCHEME = 'https'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASEDIR + "/database.db"
    ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    SERVER_NAME = 'localhost:5000'
    PREFERRED_URL_SCHEME = 'http'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASEDIR + "/database.db"
    ENV = 'development'
    DEBUG = True
