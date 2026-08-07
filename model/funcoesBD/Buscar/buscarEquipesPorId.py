from ..Cadastrar.criarConexao import criarConexao, database

def buscarEquipesPorID(fk_equipe_casa, fk_equipe_visitante):


    conexao = criarConexao()
    
    query = 'SELECT fk_nome_turma FROM equipes WHERE pk_equipe = %s'
    cursor = conexao.cursor()
    cursor.execute(query, (fk_equipe_casa, ))
    equipe_casa= cursor.fetchone()[0]

    query = 'SELECT fk_nome_turma FROM equipes WHERE pk_equipe = %s'
    cursor = conexao.cursor()
    cursor.execute(query, (fk_equipe_visitante, ))
    equipe_visitante= cursor.fetchone()[0]

    equipes = (equipe_casa, equipe_visitante)

    return equipes