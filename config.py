import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

DB_USER = 'root'
DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'password'
DB_HOST = 'db_images'
DB_NAME = 'images'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

SQLALCHEMY_TRACK_MODIFICATIONS = False