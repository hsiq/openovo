from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.cliente_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    clienteJaExiste

cliente_app = Blueprint('cliente_app', __name__, template_folder='templates')

campos = ["id", "nome"]
tipos = [int, str]

@cliente_app.route('/cliente', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@cliente_app.route('/cliente/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@cliente_app.route('/cliente', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    try:
        criado = service_criar(dados['nome'],dados['cpf'],dados['rg'],dados['cep'],dados['logradouro'],dados['nomeRua'],dados['numero'],dados['complemento'],dados['cidade'],dados['UF'],dados['telefoneResidencial'],dados['telefoneComercial'],dados['celular'],dados['email'],dados['pis'],dados['carteira_trabalho'])
        return jsonify(to_dict(criado))
    except clienteJaExiste:
        return '', 409

@cliente_app.route('/cliente/<int:cpf>', methods=['DELETE'])
def remover(cpf):
    removido = service_remover(cpf)
    return jsonify(to_dict(removido))

@cliente_app.route('/cliente', methods=['PUT'])
def atualizar():
    dados = request.get_json()
    atualizado = service_atualizar(dados['nome'],dados['cpf'],dados['rg'],dados['cep'],dados['logradouro'],dados['nomeRua'],dados['numero'],dados['complemento'],dados['cidade'],dados['UF'],dados['telefoneResidencial'],dados['telefoneComercial'],dados['celular'],dados['email'],dados['pis'],dados['carteira_trabalho'])
    return jsonify(to_dict(atualizado))