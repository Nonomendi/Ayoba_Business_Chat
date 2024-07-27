import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #Update with your DB URI if using a different DB
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	TEMPLATES_AUTO_RELOAD = True
