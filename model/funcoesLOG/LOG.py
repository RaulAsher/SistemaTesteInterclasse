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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/Sistema.log",
    encoding="utf-8"
    )

logging.getLogger("werkzeug").disabled = True

def criarLOGInfo(query, cursor, params, usuario_logado, entidade):
    # ENTIDADES = aluno, turma, esporte e etc
    cursor.execute(query, params)

    operacao = query.split()[0].upper()

    match = re.search(r"(?:FROM|INTO|UPDATE)\s+(\w+)", query, re.IGNORECASE)
    tabela = match.group(1) if match else None
    nome_tabela = TABELAS.get(tabela, tabela)

    logger = logging.getLogger("Sistema")

    acao = OPERACOES.get(operacao, operacao)

    if acao == "Consultou":
        logger.info("%s %s os %s", usuario_logado, acao, nome_tabela)
    elif acao == "Cadastrou":
        if tabela == "alunos":
            logger.info("%s %s o(a) %s %s", usuario_logado, acao, nome_tabela)
        elif tabela == "equipes":
            logger.info("%s %s a equipe do %s na modalidade %s no genero %s", usuario_logado,acao, entidade[1], entidade[0], entidade[2])
        elif tabela == "esportes":
            logger.info("%s %s um %s", usuario_logado, acao, nome_tabela)
        elif tabela == "login":
            logger.info("%s %s o usuário %s", usuario_logado, acao, entidade)
