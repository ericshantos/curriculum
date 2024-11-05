# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por criar e configurar a aplicação Flask.
"""

from flask import Flask
from .routes.curriculum import bp_curriculum


def create_app() -> Flask:
    """
    Cria e configura uma instância da aplicação Flask.

    Esta função inicializa a aplicação Flask, configura o diretório estático
    e registra os blueprints. A aplicação resultante pode ser utilizada para
    gerenciar as rotas e a lógica da aplicação web.

    Returns:
        Flask: A instância da aplicação Flask configurada.
    """
    app = Flask(__name__)

    # Configuração do diretório estático
    app.static_folder = "static"

    # Registro de blueprints
    app.register_blueprint(bp_curriculum, url_prefix="/")

    return app
