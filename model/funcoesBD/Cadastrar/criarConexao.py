import mysql.connector

database = 'etemfl83_inter_classe'

def criarConexao():
    conexaoBD = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database=database,
        port=3307
    )
    return conexaoBD
