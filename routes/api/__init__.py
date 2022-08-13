from flask import Blueprint

from controllers.users import bp_user

bind_api = Blueprint('api', __name__, url_prefix='/api')

bind_api.register_blueprint(bp_user)
