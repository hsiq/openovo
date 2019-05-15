import pyodbc
from model.cliente import Cliente



class Banco:

    def enderecoDBO():
        return pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=knoxope2019.database.windows.net;"
                          "Database=OPE;"
                         "UID=equipeBD;PWD=equipeope2019!")
    
    def cadastrar(Cliente):
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=knoxope2019.database.windows.net;"
                          "Database=OPE;"
                         "UID=equipeBD;PWD=equipeope2019!")
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO CLIENTE(NOME,CPF,RG,PIS,CARTEIRA_TRABALHO) VALUES('" +
                       Cliente.nome + "','"+ Cliente.cpf +"','" + Cliente.rg + "','"+ Cliente.pis +"','"+ Cliente.carteira_trabalho +"')")
        cursor.commit()
        cursor.execute("SELECT CODIGO FROM CLIENTE WHERE CPF ='" + Cliente.cpf + "'")
        for codigo in cursor:
            break
        b = str(codigo)
        cursor.execute("INSERT INTO ENDERECO_CLI(COD_CLI,CEP,LOGRADOURO,NOMERUA,NUMERO,COMPLEMENTO,CIDADE,UF) VALUES(" +
                        b[1:5]+ ",'"+ Cliente.cep +"','" + Cliente.logradouro + "','"+ Cliente.nomeRua +"','"+ Cliente.numero +"','"+ Cliente.complemento +"','"+ Cliente.cidade +"','"+ Cliente.UF +"')")
        cursor.execute("INSERT INTO CONTATO_CLI(COD_CLI,TELEFONE_RESIDENCIAL,TELEFONE_COMERCIAL,CELULAR,EMAIL) VALUES(" +
                        b[1:5]+ ",'"+ Cliente.telefoneResidencial +"','" + Cliente.telefoneComercial  + "','"+ Cliente.celular +"','"+ Cliente.email +"')")
        cursor.commit()
        cnxn.close()
        return

    def remover(CPF):
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=knoxope2019.database.windows.net;"
                          "Database=OPE;"
                         "UID=equipeBD;PWD=equipeope2019!")
        cursor = cnxn.cursor()
        cursor.execute("SELECT CODIGO FROM CLIENTE WHERE CPF ='" + str(CPF) + "'")
        for codigo in cursor:
            break
        b = str(codigo)
        cursor.execute("DELETE ENDERECO_CLI WHERE COD_CLI = '"+ b[1:5] +"'")
        cursor.execute("DELETE CONTATO_CLI WHERE COD_CLI = '"+ b[1:5] +"'")
        cursor.execute("DELETE CLIENTE WHERE CODIGO = '"+ b[1:5] +"'")
        cursor.commit()
        cnxn.close()

    def verificar( CPF):
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=knoxope2019.database.windows.net;"
                          "Database=OPE;"
                          "UID=equipeBD;PWD=equipeope2019!")
        cursor = cnxn.cursor()
        cursor.execute("SELECT CPF FROM CLIENTE WHERE CPF = "+ CPF)
        for x  in cursor:
            if str(x) == "('"+CPF+"', )":
                cnxn.close()
                return True
        cnxn.close()
        return False

    def alterar(Cliente):
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=knoxope2019.database.windows.net;"
                          "Database=OPE;"
                         "UID=equipeBD;PWD=equipeope2019!")
        cursor = cnxn.cursor()
        cursor.execute("SELECT CODIGO FROM CLIENTE WHERE CPF ='" + Cliente.cpf + "'")
        for codigo in cursor:
            break
        b = str(codigo)
        cursor.execute("UPDATE CLIENTE SET NOME = '"+ Cliente.nome +"',CPF = '"+Cliente.cpf+"',RG = '"+Cliente.rg+"',PIS = '"+ Cliente.pis +"',CARTEIRA_TRABALHO = '"+ Cliente.carteira_trabalho +
                        "' WHERE CODIGO = " + b[1:5])
        cursor.execute("UPDATE ENDERECO_CLI SET CEP = '" + Cliente.cep +"',LOGRADOURO = '"+ Cliente.logradouro + "',NUMERO = '" + Cliente.numero + "',COMPLEMENTO = '" + Cliente.complemento + "',CIDADE = '" + Cliente.cidade +"',UF = '"+ Cliente.UF + 
                        "' WHERE COD_CLI = " + b[1:5])
        cursor.execute("UPDATE CONTATO_CLI SET TELEFONE_RESIDENCIAL = '"+ Cliente.telefoneResidencial + "',TELEFONE_COMERCIAL = '" + Cliente.telefoneComercial +"',CELULAR = '" + Cliente.celular + "',EMAIL = '" + Cliente.email +
                        "' WHERE COD_CLI = " + b[1:5])
        cursor.commit()
        cnxn.close()
    
    def consultar(cpf):
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=knoxope2019.database.windows.net;"
                          "Database=OPE;"
                         "UID=equipeBD;PWD=equipeope2019!")
        cursor.execute("SELECT CPF FROM CLIENTE WHERE CPF = "+ cpf)

        





#cli = Cliente('JHONATAS VELIS','43434332802','435610419','02466120','Rua','Alberto Silva','164','B','São Paulo','SP','1122352688','11747474748','11943044118','JHON_AVILEZ@HOTMAIL.COM','SHAUHSUA','KKKKKKKK')
#a = Banco()
#a.cadastrar(cli)
#a.remove('43434332856')
#a.alterar(cli)

#b = a.consultar('43434332801')