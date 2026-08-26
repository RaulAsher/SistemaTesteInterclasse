import mysql.connector
from mysql.connector import Error


database = 'etemfl83_inter_classe'


def criarConexao():
    conexaoBD = mysql.connector.connect(
        host='localhost',
        user='root',
        password='pitang',
        database=database
    )
    return conexaoBD
