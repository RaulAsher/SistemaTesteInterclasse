import logging
import os
import re

os.makedirs("logs", exist_ok=True)

OPERACOES = {
    "SELECT":"Consultou",
    "INSERT":"Cadastrou",
    "UPDATE":"Atualizou",
    "DELETE":"Deletou"
}

TABELAS = {
    "alunos":"Aluno(a)",
    "equipes":"Equipe",
    "estatisticas_esporte":"Estatistica Esportiva",
    "esportes":"Esporte",
    "partidas":"Chaveamento",
    "login":"Usuario",
    "turmas":"Turma"
}

logger = logging.getLogger("Sistema")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    "logs/Sistema.log", encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.propagate = False

def criarLOGInfo(query, cursor, params, usuario_logado):
    """
    Coloca informações dentro do Sistema.log
    """

    # ENTIDADES = aluno, turma, esporte e etc
    cursor.execute(query, params)

    operacao = query.split()[0].upper()

    match = re.search(r"(?:FROM|INTO|UPDATE)\s+(\w+)", query, re.IGNORECASE)
    tabela = match.group(1) if match else None
    if tabela != None:
        nome_tabela = TABELAS.get(tabela, tabela)

    acao = OPERACOES.get(operacao, operacao)

    if acao == "Consultou":
        logger.info("%s %s os(as) %s", usuario_logado, acao, nome_tabela)
    elif acao == "Cadastrou":
        if tabela == "alunos":
            aluno_cadastrado = params[1]
            turma = params[2]
            logger.info("%s %s o(a) Aluno(a) %s na turma %s", usuario_logado, acao, aluno_cadastrado, turma)

        elif tabela == "equipes":
            turma = params[1]
            esporte = params[0]
            genero = params[2]
            
            logger.info("%s %s a equipe do %s na modalidade %s do genero %s", usuario_logado,acao, turma, esporte, genero)

        elif tabela == "esportes":
            esporte = params[0]
            grupo = params[1]
            qtdjogadores = params[2]

            logger.info("%s %s a modalidade: %s - %s com um maximo de %s jogadores", usuario_logado, acao, esporte, grupo, qtdjogadores)

        elif tabela == "login":
            nome_usuario = params[0]
            nivel = params[2]

            if nivel == "AlunoMonitor":
                nivel = "Aluno Monitor"
                turma = params[3]
                logger.info("%s %s o usuário %s como %s da turma %s", usuario_logado, acao, nome_usuario, nivel, turma)
            else:
                logger.info("%s %s o usuário %s como %s", usuario_logado, acao, nome_usuario, nivel)

        elif tabela == "turmas":
            turma = params[0]
            logger.info("%s %s a turma %s", usuario_logado, acao, turma)
    elif acao == "Deletou":
        if tabela == "alunos":
            aluno_cadastrado = params[1]
            turma = params[2]

            logger.info("%s %s o(a) Aluno(a) %s da turma %s",usuario_logado, acao, aluno_cadastrado, turma)

        elif tabela == "equipes":
            turma = params[0]
            esporte = params[1]
            genero = params[2]

            logger.info("%s %s a equipe da turma %s na modalidade %s do genero %s",usuario_logado, acao, turma, esporte, genero)

        elif tabela == "esportes":
            esporte = params[0]
            grupo = params[1]
            qtdjogadores = params[2]

            logger.info("%s %s a modalidade: %s - %s com um maximo de %s jogadores",usuario_logado, acao, esporte, grupo, qtdjogadores)

        elif tabela == "login":
            nome_usuario = params[0]
            nivel = params[2]

            if nivel == "AlunoMonitor":
                nivel = "Aluno Monitor"
                turma = params[3]
                logger.info("%s %s o usuário %s como %s da turma %s",usuario_logado, acao, nome_usuario, nivel, turma)

            else:
                logger.info("%s %s o usuário %s como %s",usuario_logado, acao, nome_usuario, nivel)

        elif tabela == "turmas":
            turma = params[0]

            logger.info("%s %s a turma %s",usuario_logado, acao, turma)