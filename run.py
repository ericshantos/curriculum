# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por iniciar a aplicação principal da web.

Este módulo importa a função `create_app` do pacote `app` para criar uma instância
da aplicação Flask. A aplicação é executada em modo de produção, com o debug desativado.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
