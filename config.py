import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/inz'

SQLALCHEMY_TRACK_MODIFICATIONS = False

PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = 'python'