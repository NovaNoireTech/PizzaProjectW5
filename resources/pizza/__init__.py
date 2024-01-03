from flask_smorest import Blueprint

bp = Blueprint('piza', __name__, description='Ops on Pizza', url_prefix='/pizza')