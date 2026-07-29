from .criarConexao import criarConexao
from ...funcoesLOG.LOG import criarLOGInfo

def cadastrarTurma(pk_nome_turma, icone_url, usuario_logado):
    conn = criarConexao()
    cursor = conn.cursor()

    query = "INSERT INTO turmas (pk_nome_turma, icone_url) VALUES (%s, %s)"
    params = (pk_nome_turma, icone_url)

    criarLOGInfo(query, cursor, params, usuario_logado)
    

    conn.commit()
    conn.close()