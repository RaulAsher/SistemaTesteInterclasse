import mysql.connector
from mysql.connector import Error


database = 'etemfl83_inter_classe'


def criarConexao():

    try:

        conexaoBD = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database=database
        )

        if conexaoBD.is_connected():
            return conexaoBD

    except Error as erro:

        print("======================================")
        print("ERRO AO CONECTAR COM O BANCO DE DADOS")
        print("======================================")

        if erro.errno == 1045:
            print("Usuário ou senha do MySQL estão incorretos.")

        elif erro.errno == 1049:
            print(f"O banco de dados '{database}' não existe.")

        elif erro.errno == 2003:
            print("Não foi possível conectar ao servidor MySQL.")
            print("Verifique se o MySQL está em execução.")

        else:
            print(f"Erro MySQL: {erro}")

        print("======================================")

        return None