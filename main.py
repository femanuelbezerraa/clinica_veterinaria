from app import app
from app.routes import rota_usuario, rota_produto, rota_movimentacao

if __name__ == '__main__':
    app.run(debug=True)
