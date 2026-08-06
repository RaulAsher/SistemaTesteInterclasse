# import mysql.connector

# database = 'etemfl83_inter_classe'

# def criarConexao():
#     conexaoBD = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='1234',
#         database=database
#         port=3306
#     )
#     return conexaoBD

mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database=_Database,
    port=3307
)