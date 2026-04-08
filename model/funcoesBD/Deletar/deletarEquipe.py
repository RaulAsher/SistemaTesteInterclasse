from ..Cadastrar.criarConexao import criarConexao
import mysql.connector

def deletarEquipe(id):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            # Apaga todos os jogadores vinculados à equipe
            cursor.execute("DELETE FROM membros_equipe WHERE fk_equipe = %s", (id,))

            # Agora apaga a equipe
            cursor.execute("DELETE FROM equipes WHERE pk_equipe = %s", (id,))
            conexao.commit()

        return "OK"

    except mysql.connector.Error as e:
        print("Erro ao deletar equipe:", e)
        return "ERRO"

    finally:
        conexao.close()



