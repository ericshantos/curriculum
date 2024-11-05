# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por definir as rotas da seção de currículo da aplicação.
"""

from flask import Blueprint, render_template, Response

# Cria um Blueprint chamado "main" para organizar as rotas da aplicação
bp_curriculum = Blueprint("main", __name__)


@bp_curriculum.route("/", methods=["GET"])
def send_curriculum() -> Response:
    """
    Rota para exibir o currículo.

    Esta função é acionada quando a rota raiz ("/") é acessada via método GET.
    Ela renderiza o template "curriculum.html" que exibe as informações do currículo.

    Returns:
        str: O template HTML renderizado com o currículo.
    """
    return render_template("curriculum.html")
