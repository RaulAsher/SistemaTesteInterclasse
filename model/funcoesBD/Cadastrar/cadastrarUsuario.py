from .criarConexao import criarConexao
from ...funcoesLOG.LOG import criarLOGInfo

def cadastrarUsuario(pk_usuario, senha, nivel, usuario_logado, fk_nome_turma=None):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            
            query = """
                INSERT INTO login (pk_usuario, senha, nivel, fk_nome_turma)
                VALUES (%s, %s, %s, %s)
            """
            params = (pk_usuario, senha, nivel, fk_nome_turma)
            criarLOGInfo(query, cursor, params, usuario_logado)
        conexao.commit()
    finally:
        conexao.close()