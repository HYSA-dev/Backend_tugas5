from flask import Flask
from app.config import Config


from app.routes.v1.item_routes import item_bp_v1
from app.routes.v1.user_routes import user_bp_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    app.register_blueprint(item_bp_v1)
    app.register_blueprint(user_bp_v1)

    return app