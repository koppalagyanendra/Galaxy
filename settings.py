import os

 # Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'galaxy.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SITE_NAME = 'GALAXY'
IMAGES_PATH=os.path.join(basedir, 'static/images/uploads')
SECRET_KEY='you-will-never-guess'
