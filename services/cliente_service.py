from model.cliente import Cliente
from infra.log import Log
from dao.DBO import Banco

cliente_db = []

class clienteJaExiste(Exception):
    pass

def listar():
    return cliente_db

def localizar(id):
    for x in cliente_db:
        if x.id == id:
            return x
    return None

def criar(nome,cpf,rg,cep, logradouro,nomeRua,numero,complemento,cidade,UF,telefoneResidencial ,telefoneComercial , celular , email  ,pis,carteira_trabalho):
    criado = Cliente(nome,cpf,rg,cep, logradouro,nomeRua,numero,complemento,cidade,UF,telefoneResidencial ,telefoneComercial , celular , email  ,pis,carteira_trabalho)
    Banco.cadastrar(criado)
    return criado

def remover(cpf):
    Banco.remover(cpf)
    return cpf

def atualizar(nome,cpf,rg,cep, logradouro,nomeRua,numero,complemento,cidade,UF,telefoneResidencial ,telefoneComercial , celular , email  ,pis,carteira_trabalho):
    cli = Cliente(nome,cpf,rg,cep, logradouro,nomeRua,numero,complemento,cidade,UF,telefoneResidencial ,telefoneComercial , celular , email  ,pis,carteira_trabalho)
    Banco.alterar(cli)
    return cli