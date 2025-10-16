"""Package-level import to register routes.

Importando os módulos de rota aqui garantimos que as funções
decoradas com @app.route sejam registradas quando o pacote
`app.routes` for importado por `main.py`.
"""

from . import rota_usuario
from . import rota_produto
from . import rota_movimentacao