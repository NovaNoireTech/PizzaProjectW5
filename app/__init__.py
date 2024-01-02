from flask import Flask

app = Flask(__name__)

from resources.pizza import routes
from resources.users import routes