from app import app
from app.routes import rota_usuario, rota_produto, rota_movimentacao

if __name__ == '__main__':
    app.run(debug=True)
Criação da minha estrutura do briefin 3 sobre a clinica veterinaria, criação do app e dentro do app tem as pastas controller, database, models, routes e views. Cada pasta tem uma função para o codigo para no fim, todas serem conectadas ao main.py