import mysql.connector
from mysql.connector import Error


database = 'etemfl83_inter_classe'


def criarConexao():
    try:
        conexaoBD = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            port=3307,
            database=database,
            connection_timeout=5
        )

        if conexaoBD.is_connected():
            return conexaoBD

        raise ConnectionError("Não foi possível estabelecer conexão com o banco de dados.")

    except Error as erro:
        print(f"Erro ao conectar com o MySQL: {erro}")
        raise ConnectionError(
            "Não foi possível conectar ao banco de dados. "
            "Verifique se o MySQL está ligado."
        ) from erro