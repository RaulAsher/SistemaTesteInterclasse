import mysql.connector
from mysql.connector import Error


database = 'etemfl83_inter_classe'


def criarConexao():
    conexaoBD = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        port=3307,
        database=database
    )
    return conexaoBD
