from flask import Flask


def create_app():
    from routes.api import bind_api
    app = Flask(__name__)
    app.register_blueprint(bind_api)
    return app
