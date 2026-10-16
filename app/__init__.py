from flask import Flask

from app.routes.item_routes import item_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(item_bp)
    return app