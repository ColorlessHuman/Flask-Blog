import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from celery import Celery
from elasticsearch import Elasticsearch


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9e97f3f224f049857cf9fd784d88d84'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
app.config['CELERY_BROKER_URL'] = 'amqp://'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://'
celery_down = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery_down.conf.update(app.config)
app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200'
ES_HOST = {'host': 'localhost', 'port': 9200}
elastic = Elasticsearch(hosts=[ES_HOST])

from flaskblog import routes
