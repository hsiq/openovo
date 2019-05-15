class Cliente:
    def __init__(self,nome,cpf,rg,cep, logradouro,nomeRua,numero,complemento,cidade,UF,telefoneResidencial,telefoneComercial, celular, email ,pis,carteira_trabalho):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__cep = cep
        self.__logradouro = logradouro
        self.__nomeRua = nomeRua
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__UF = UF
        self.__telefoneResidencial = telefoneResidencial
        self.__telefoneComercial = telefoneComercial
        self.__celular = celular
        self.__email = email
        self.__pis = pis
        self.__carteira_trabalho = carteira_trabalho

    def atualizar(self,nome,cpf,rg,cep, logradouro,nomeRua,numero,complemento,cidade,UF,telefoneResidencial ,telefoneComercial, celular, email  ,pis,carteira_trabalho):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__cep = cep
        self.__logradouro = logradouro
        self.__nomeRua = nomeRua
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__UF = UF
        self.__telefoneResidencial = telefoneResidencial
        self.__telefoneComercial = telefoneComercial
        self.__celular = celular
        self.__email = email
        self.__pis = pis
        self.__carteira_trabalho = carteira_trabalho
    @property 
    def nome(self):
        return self.__nome
    
    @property 
    def cpf(self):
        return self.__cpf
    
    @property 
    def rg(self):
        return self.__rg
    
    @property 
    def cep(self):
        return self.__cep
    
    @property 
    def logradouro(self):
        return self.__logradouro
    
    @property 
    def nomeRua(self):
        return self.__nomeRua
    
    @property 
    def numero(self):
        return self.__numero
    
    @property 
    def complemento(self):
        return self.__complemento
    
    @property 
    def cidade(self):
        return self.__cidade
    
    @property 
    def UF(self):
        return self.__UF
    
    @property 
    def telefoneResidencial(self):
        return self.__telefoneResidencial
    
    @property 
    def telefoneComercial(self):
        return self.__telefoneComercial
    
    @property 
    def celular(self):
        return self.__celular

    @property 
    def email(self):
        return self.__email
    
    @property 
    def pis(self):
        return self.__pis
    
    @property 
    def carteira_trabalho(self):
        return self.__carteira_trabalho
    

    