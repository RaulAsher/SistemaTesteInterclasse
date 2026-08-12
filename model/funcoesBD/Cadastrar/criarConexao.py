import mysql.connector

database = 'etemfl83_inter_classe'

def criarConexao():
    conexaoBD = mysql.connector.connect(
        host='localhost',
        user='root',
        password='21102008M',
        database=database,
        port=3306
    )
    return conexaoBD
