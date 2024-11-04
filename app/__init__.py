from flask import Flask
from .routes.curriculum import bp_curriculum


def create_app():
    app = Flask(__name__)

    # configuração do diretório estático
    app.static_folder = "static"

    # registro de bluepints
    app.register_blueprint(bp_curriculum, url_prefix="/")

    return app
