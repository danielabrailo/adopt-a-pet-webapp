from flask import Flask
import os
import flask_sqlalchemy
import flask_migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f463f37daf12dc40a0b120d857a2644'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'adoptapetinisrael@gmail.com'
app.config['MAIL_PASSWORD'] = 'kfvevuworvxsjh'
mail = Mail(app)

from app import routes



