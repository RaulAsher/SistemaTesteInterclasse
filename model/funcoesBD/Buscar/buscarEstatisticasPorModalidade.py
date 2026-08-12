from ..Cadastrar.criarConexao import criarConexao
from flask import flash

def buscarEstatisticasPorModalidade(modalidade):
    conexao = criarConexao()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT fk_nome_estatistica, estatistica_principal FROM estatisticas_esporte WHERE fk_esporte = %s', (modalidade,))
        estatisticasBuscadas = cursor.fetchall()
        return estatisticasBuscadas
    except:
        conexao.rollback()
        flash('Ocorreu um erro inesperado', 'erro')
    finally:
        cursor.close()
        conexao.close()