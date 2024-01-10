from flask import Flask
from flask_smorest import Api
# flask marshmallow need to be re ran? flask db upgrade is not allowing pizza folder to be shown in SQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import UserModel
from models import pizzamodel

from resources.users import bp as user_bp
api.register_blueprint(user_bp)

from resources.pizza import bp as post_bp
api.register_blueprint(post_bp)