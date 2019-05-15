from flask import Flask, jsonify, request
from cliente_api import cliente_app




app = Flask(__name__)
app.register_blueprint(cliente_app)


@app.route('/')
def all():
    from services.cliente_service import listar as listar_cliente

    database = {
        "cliente": listar_cliente()

    }
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)