from ..Cadastrar.criarConexao import criarConexao, database

def buscarEstatisticasPrincipal(modalidade):
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT fk_nome_estatistica FROM estatisticas_esporte where estatistica_principal = 1 and fk_esporte = %s;
    ''', modalidade)

    estatisticasBuscadas = cursor.fetchone()

    return estatisticasBuscadas[0] if estatisticasBuscadas else None
    