from ..Cadastrar.criarConexao import criarConexao
import mysql.connector

def buscarPartidasBanco(esporte, classificacao):
    """
    Busca todas as partidas de uma chave (esporte/classificação)
    trazendo os nomes das equipes.
    """
    conexao = criarConexao()
    if not conexao: return []

    try:
        # Usamos dictionary=True para retornar como dicionários
        with conexao.cursor(dictionary=True) as cursor: 
            query = """
            SELECT 
	   p.pk_partida_mae as id_Partida_mae,
	   p.pk_partida as id_partida,
	   p.fk_esporte as modalidade,
       e.grupo as tipo_modalidade,
       p.fk_genero as genero,
       p.fk_equipe_casa as cod_equipe_casa,
       p.fk_equipe_visitante as cod_equipe_vistante,
       p.etapa as rounde,
       p.definida as definida,
       p.pontos_turma_casa as pontos_turma_casa,
       p.pontos_turma_visitante as pontos_turma_visitante,
       p.pk_equipe_vencedora as vencedora,
       eq_casa.fk_nome_turma as nome_equipe_casa,
       eq_visitante.fk_nome_turma as nome_equipe_visitante


    FROM etemfl83_inter_classe.partidas p
    
    left join equipes eq_casa
    on eq_casa.pk_equipe = p.fk_equipe_casa
    
    left join equipes eq_visitante
    on eq_visitante.pk_equipe = p.fk_equipe_visitante

    left join esportes e
    on e.pk_esporte = p.fk_esporte
    
    WHERE  p.fk_esporte = %s AND  p.fk_genero = %s
    
    order by p.etapa,  p.pk_partida_mae asc, p.pk_partida
            """
            # Filtra pelo esporte E classificação, e traz todas as etapas
            cursor.execute(query, (esporte, classificacao))
            partidas = cursor.fetchall() 
            if partidas != []:
                return partidas
            else:
                return None
        
    except mysql.connector.Error as err:
        print(f"Erro ao buscar partidas para gestão: {err}")
        return []
    finally:
        conexao.close()


def getAlunoEquipe(idEquipe):
    """
    Buscar aluno da equipe individual
    """
    conexao = criarConexao()
    if not conexao: return []

    try:
        with conexao.cursor(dictionary=True) as cursor: 
            query = """select CONCAT(SUBSTRING_INDEX(a.nome_aluno, ' ', 1),' ',SUBSTRING_INDEX(a.nome_aluno, ' ', -1)) as nome_aluno

                        from etemfl83_inter_classe.membros_equipe me

                        left join etemfl83_inter_classe.alunos a
                        on a.pk_matricula = me.fk_matricula

                        where me.fk_equipe = %s;"""
            cursor.execute(query, (idEquipe,)) 
            resultado = cursor.fetchone()
            if not resultado:
                return ''
            else:
                return resultado['nome_aluno']

    except mysql.connector.Error as err:
        print(f"Erro ao buscar partidas para gestão: {err}")
        return []
    finally:
        conexao.close()

def buscarPartidasParaGestao(esporte, classificacao):
    partidas = buscarPartidasBanco(esporte,classificacao)
    if partidas != None:
        countRounds = 1
        roundAnterior = partidas[0]['rounde']
        tipoModalidade = partidas[0]['tipo_modalidade']
        totalPartidas = len(partidas) - 1
        tabela = {'modalidade':esporte, 'genero':classificacao, 'totalRounds': 0, 'tipoModalidade': tipoModalidade, 'roundes': []}
        countPartidas = 0
        listaRoundes = []

        for partida in partidas:
            if(tipoModalidade == 'Individual'):
                partida['NomeIndividualCasa'] = getAlunoEquipe(partida['cod_equipe_casa'])
                partida['NomeIndividualVisitante'] = getAlunoEquipe(partida['cod_equipe_vistante'])
            if(countPartidas == totalPartidas):
                rounde = {'rounde': roundAnterior, 'partidas': listaRoundes}
                tabela['roundes'].append(rounde)
                roundAnterior = partida['rounde']
                listaRoundes = []
                partida['id_Partida_mae'] = "Campeão"
                listaRoundes.append(partida)
                rounde = {'rounde': roundAnterior, 'partidas': listaRoundes}
                tabela['roundes'].append(rounde)
                countRounds += 1
                tabela['totalRounds'] = countRounds + 1
            else:
                if partida['rounde'] == roundAnterior:
                    listaRoundes.append(partida)
                else:
                    rounde = {'rounde': roundAnterior, 'partidas': listaRoundes}
                    tabela['roundes'].append(rounde)
                    roundAnterior = partida['rounde']
                    listaRoundes = []
                    listaRoundes.append(partida)
                    countRounds += 1
            countPartidas += 1
        if tabela != []:
            return tabela
            
    else:
        err =  mysql.connector.Error
        print(f"Erro ao buscar partidas para gestão: {err}")
        tabela = None
        return tabela