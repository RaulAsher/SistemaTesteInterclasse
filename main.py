from flask import Flask, render_template, redirect, request, session, jsonify, flash, url_for
from functools import wraps
from datetime import timedelta, datetime, date
from model import *
from calendar import *

print("Main iniciado")
# Assumindo que seu gestao_chaveamento.py está em model/funcoesBD/Chaveamento
# E que o Flask pode importá-lo a partir da raiz 'model'
try:
    from model.funcoesBD.Chaveamento.gestao_chaveamento import gerarChaveamento
except ImportError as e:
    print(f"ATENÇÃO: Falha ao importar gerarChaveamento. Certifique-se de que todas as pastas possuem __init__.py e o caminho está correto. Erro: {e}")
    # Define uma função placeholder para evitar quebra total
    def gerarChaveamento(esporte, classificacao):
        print("!!! FUNÇÃO DE CHAVEAMENTO NÃO CARREGADA !!!")
        return None


#Decorator para verificar se o usuario é Administrador
def requerAdmin(f):
    @wraps(f)
    def requerindoAdmin(*args, **kwargs):

        if session['nivel'] != "Administrador":
            return redirect('/')

        if session['nivel'] != "Administrador":
            flash("Faça login como Administrador para ativar esta função.", "error")
            return redirect('/')
        
        return f(*args, **kwargs)
    return requerindoAdmin

#Decorator para verificar se o usuario é Administrador ou AlunoMonitor
def requerAdminOuMonitor(f):
    @wraps(f)
    def requerindo(*args, **kwargs):
        
        if session['nivel'] not in ["Administrador", "AlunoMonitor"]:

            flash("Faça login para ativar esta função.", "warning")
            return redirect('/')
        
        return f(*args, **kwargs)
    return requerindo

def obterAcessoDoUsuario():
    nivel = session.get("nivel", "Visitante")
    turma = session.get("turma")

    if nivel == "Administrador":


        return {
            "nivel": nivel,
            "equipes": buscarEquipes(),
            "turmas": buscarTurmas()
        }

    if nivel == "AlunoMonitor":
        return {
            "nivel": nivel,
            "equipes": buscarEquipesPorTurma(turma),
            "turmas": [{"pk_nome_turma": turma}]
        }

    return {
        "nivel": "Visitante",
        "equipes": buscarEquipes(),
        "turmas": []
    }

app = Flask(__name__)
app.secret_key = '29bfd352-ed9e-4818-b05b-498b8f77e4e3'
app.permanent_session_lifetime = timedelta(days=30)

@app.route("/")
def home():
    nome_usuario = session.get('nome')
    return redirect('/home')


@app.context_processor
def inject_user():
    return dict(nome_usuario=session.get('nome'))


## ---------------LOGIN---------------- ##

# O usuário é considerado visitante se não estiver logado. Criamos uma sessão para ele:

@app.before_request
def criarSessaoVisitante():
    if 'nome' not in session:
        session['nome'] = 'Visitante'
        session['nivel'] = 'Visitante'
        session['turma'] = None

@app.route('/login')
def login():
    if session['nivel'] != 'Visitante':
        return redirect('/')
    else:
        return render_template('login.html')
    
@app.route('/login', methods=['POST'])
def verificarLogin():
    usuario = request.form['usuario']
    senha = request.form['senha']

    # Busca apenas pelo nome do usuário
    usuario_encontrado = buscarUsuarioPorNome(usuario)

    if not usuario_encontrado or senha != usuario_encontrado["senha"]:
        flash('Usuário ou senha estão incorretos.', 'error')
        return redirect(url_for('login'))
    
    # Login bem-sucedido
    session['nome'] = usuario
    session['nivel'] = usuario_encontrado['nivel']

    # Verificação do lembrar_me
    if request.form.get("lembrar_me"):
        session.permanent = True
    else:
        session.permanent = False

    # Verificação do Aluno Monitor
    if usuario_encontrado['nivel'] == 'AlunoMonitor':
        session['turma'] = usuario_encontrado['fk_nome_turma']
    else:
        session['turma'] = None

    return redirect('/')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/home")
def homeRedirect():
    return render_template("home.html", nome_usuario=session.get("nome", "Visitante"), nivel=session.get("nivel", "Visitante"))

## ----------------LISTAGENS----------------- ##

@app.route("/turma")
def turma():
    turmas = buscarTurmas()
    print(turmas[0]['pk_nome_turma'])
    return render_template("turma.html", turmas=turmas)

@app.route("/alunosPorTurma/<turma>")
def alunosPorTurma(turma):
    alunos = buscarAlunosPorTurma(turma)
    # função do model que retorna lista de alunos da turma
    return jsonify({"alunos": [{"matricula": a[0], "nome": a[1]} for a in alunos]})

## ----------------CADASTRAR ALUNOS---------------##

@app.route("/cadastrarAluno", methods=["GET"])
@requerAdminOuMonitor
def paginacadastrarAluno():

    acesso = obterAcessoDoUsuario()

    return render_template(
        "cadastrarAluno.html",
        alunos=buscarAlunos(),
        turmas=buscarTurmas(),
        nivel=acesso["nivel"]
        )

@app.route("/cadastrarAluno", methods=["POST"])
@requerAdminOuMonitor
def rotaCadastrarAluno():

    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    genero = request.form.get("genero")

    if session['nivel'] == 'Administrador':
        turma = request.form.get("turma")
    else:
        turma = session["turma"]

    cadastrarAluno(matricula, nome, turma, genero)

    return redirect(url_for("paginacadastrarAluno"))

@app.route("/editarAluno/<antiga_matricula>", methods=["POST"])
@requerAdminOuMonitor
def rotaEditarAluno(antiga_matricula):

    nome = request.form["nome"]
    genero = request.form["genero"]
    nova_matricula = request.form["nova_matricula"]

    if session["nivel"] == "Administrador":
        turma = request.form["turma"]
    else:
        turma = session["turma"]

    editarAluno(
        nova_matricula,
        nome,
        turma,
        genero,
        antiga_matricula
    )

    return redirect(url_for("paginacadastrarAluno"))

@app.route("/deletarAluno/<matricula>")
@requerAdminOuMonitor
def rotaDeletarAluno(matricula):
    deletarAluno(matricula)
    
    return redirect(url_for("paginacadastrarAluno"))


## ------------------CADASTRAR TURMAS-------------------- ##

# Cadastrar
@app.route("/cadastrarTurma", methods=["POST"])
@requerAdminOuMonitor
def rotaCadastrarTurma():
    pk_nome_turma = request.form.get("pk_nome_turma")
    icone_url = request.form.get("icone_url") 
    cadastrarTurma(pk_nome_turma, icone_url)
    turmas = buscarTurmas()
    return render_template("turma.html", turmas=turmas)

# Editar
@app.route("/editarTurma/<string:turma>", methods=["POST"])
@requerAdminOuMonitor
def rotaEditarTurma(turma):
    novo_nome = request.form.get("pk_nome_turma")
    icone_url = request.form.get("icone_url") 
    editarTurma(turma, novo_nome, icone_url)
    turmas = buscarTurmas()
    return render_template("turma.html", turmas=turmas)

# Deletar
@app.route("/deletarTurma/<string:turma>")
@requerAdminOuMonitor
def rotaDeletarTurma(turma):
    deletarTurma(turma)
    turmas = buscarTurmas()
    return render_template("turma.html", turmas=turmas)


## ---------------------CADASTRAR EQUIPE---------------------- ##

@app.route("/cadastrarEquipe", methods=["GET"])
def paginaCadastrarEquipe():

    acesso = obterAcessoDoUsuario()

    return render_template(
        "cadastrarEquipe.html",
        equipes=acesso["equipes"],
        turmas=acesso["turmas"],
        esportes = buscarEsportes(),
        classificacoes = buscarClassificacoes(),
        nivel=acesso["nivel"],
        prazo_edicao=buscarConfiguracao("prazo_edicao_equipes")
    )


@app.route("/cadastrarEquipe", methods=["POST"])
@requerAdminOuMonitor
def rotaCadastrarEquipe():
    esporte = request.form.get("esporte")
    turma = request.form.get("turma")
    genero = request.form.get("genero")
    alunos = request.form.getlist("alunos")

    cadastrarEquipe(esporte, turma, genero, alunos)
    flash("Equipe cadastrada com sucesso.", "success")

    return redirect("/cadastrarEquipe")

@app.route("/editarEquipe/<int:pk_equipe>", methods=["POST"])
@requerAdminOuMonitor
def rotaEditarEquipe(pk_equipe):

    if not edicaoEquipesPermitida():
        flash("O prazo para editar equipes foi encerrado.", "error")
        return redirect("/cadastrarEquipe")

    esporte = request.form.get("esporte")
    turma = request.form.get("turma")
    genero = request.form.get("genero")
    alunos = request.form.getlist("alunos")

    editarEquipe(pk_equipe, esporte, turma, genero, alunos)

    flash("Equipe editada com sucesso.", "success")
    return redirect("/cadastrarEquipe")

@app.route("/alterarPrazoEdicao", methods=["POST"])
@requerAdmin
def alterarPrazo():

    prazo = request.form.get("prazo")

    alterarConfiguracao(
        "prazo_edicao_equipes",
        prazo
    )

    flash("Prazo atualizado com sucesso!", "success")

    return redirect(url_for("paginaCadastrarEquipe"))

#Deletar equipe
@app.route("/deletarEquipe/<int:pk_equipe>")
@requerAdminOuMonitor
def rotaDeletarEquipe(pk_equipe):
    resultado = deletarEquipe(pk_equipe)
    flash("Equipe deletada com sucesso.", "success")
    return resultado  # retorna texto direto pro fetch()


# Buscar alunos por turma (JSON)
@app.route("/alunosPorTurma/<nome_turma>/<classificacao>")
def alunosPorTurmaEquipes(nome_turma, classificacao):
    alunos = alunosPorTurmaListaEquipes(nome_turma, classificacao)
    return jsonify({"alunos": alunos})

# Jogadores de uma equipe (JSON)
@app.route("/jogadoresPorEquipe/<int:id_equipe>")
def jogadoresPorEquipe(id_equipe):
    jogadores = buscarJogadoresPorEquipe(id_equipe)
    return jsonify({"jogadores": jogadores})


## -------------------CADASTRO DO USUARIO------------------ ##

# Página de cadastro
@app.route("/cadastrarUsuario", methods=["GET"])
def paginaCadastrarUsuario():
    usuarios = telaUsuarios()
    turmas = buscarTurmas()
    return render_template("cadastrarUsuario.html", usuarios=usuarios, turmas=turmas)

# Inserção no banco
@app.route("/cadastrarUsuario", methods=["POST"])
def rotaCadastrarUsuario():
    pk_usuario = request.form.get("pk_usuario")
    senha = request.form.get("senha")
    nivel = request.form.get("nivel")
    fk_nome_turma = request.form.get("fk_nome_turma") if nivel == "AlunoMonitor" else None

        #--Validação: aluno monitor precisa de turma
    if nivel == "AlunoMonitor" and (not fk_nome_turma or fk_nome_turma.strip() == ""):
        flash("Erro: Aluno Monitor precisa estar vinculado a uma turma.", "error")
        return redirect(url_for("paginaCadastrarUsuario"))


    try:

        cadastrarUsuario(pk_usuario, senha, nivel, fk_nome_turma)
        flash("Usuário cadastrado com sucesso!", "success")

    except Exception as e:
        flash("O nome de usuário que você tentou cadastrar já existe.\n" "Por favor, tente outro.", "error")

    return redirect(url_for("paginaCadastrarUsuario"))

# Edição
@app.route("/editarUsuario/<pk_usuario>", methods=["POST"])
def rotaEditarUsuario(pk_usuario):
    novo_usuario = request.form.get("pk_usuario")
    senha = request.form.get("senha")  # opcional
    nivel = request.form.get("nivel")
    fk_nome_turma = request.form.get("fk_nome_turma") if nivel == "AlunoMonitor" else None

    #--Validação
    if nivel == "AlunoMonitor" and (not fk_nome_turma or fk_nome_turma.strip() == ""):
        flash("Erro: Aluno Monitor precisa estar vinculado a uma turma.", "error")
        return redirect(url_for("paginaCadastrarUsuario"))

    editarUsuario(pk_usuario, novo_usuario, senha, nivel, fk_nome_turma)
    flash("Usuário atualizado com sucesso!", "success")
    return redirect(url_for("paginaCadastrarUsuario"))

# Deleção
@app.route("/deletarUsuario/<pk_usuario>")
def rotaDeletarUsuario(pk_usuario):
    deletarUsuario(pk_usuario)
    usuarios = telaUsuarios()
    turmas = buscarTurmas()
    return render_template("cadastrarUsuario.html", usuarios=usuarios, turmas=turmas)


## ----------------GERENCIAR/CADASTRAR MODALIDADES------------------ ##

@app.route("/gerenciarModalidades")
def gerenciarModalidades():
    esportes = buscarEsportes()
    return render_template("gerenciarModalidades.html", esportes=esportes)

#Cadastra modalidade juntamente com a classificação dela (Individual, Coletivo) e Quantidade de jogadores
@app.route('/cadastrarModalidades', methods=['POST'])
@requerAdmin
def processarCadastroModalidades():
    esporte = request.form['esporte']
    esporte = esporte.title()
    grupo = request.form['grupo']
    qtdJogadores = request.form['qtdJogadores']
    cadastrarEsportes(esporte, grupo, qtdJogadores)
    return redirect('/gerenciarModalidades')


## ----------------CHAVEAMENTO------------------ ##

@app.route("/gerarChaveamento", methods=["GET"])
def paginaGerarChaveamento():
    # Buscar esportes e classificações para preencher os <select> no HTML
    esportes = buscarEsportes()
    classificacoes = buscarClassificacoes()
    
    return render_template(
        "gerarChaveamento.html", 
        esportes=esportes, 
        classificacoes=classificacoes
    )


@app.route("/chaveamento/gerar", methods=["POST"])
@requerAdmin # Proteja a rota de geração
def rotaGerarChaveamento():
    # Recebe os dados JSON enviados pelo JavaScript
    dados = request.get_json()
    esporte = dados.get('esporte')
    classificacao = dados.get('classificacao')

    if not esporte or not classificacao:
        return jsonify({"status": "erro", "mensagem": "Esporte e Classificação são obrigatórios."}), 400

    try:
        # CHAMA SUA LÓGICA PYTHON
        chaveamento = gerarChaveamento(esporte, classificacao) 
        
        # Sua função gera o chaveamento e JÁ SALVA as partidas no BD.
        # Agora precisamos apenas retornar o status para o frontend.
        
        # O resultado impresso no terminal será o log do 'gerarChaveamento'.
        
        # Como sua função retorna o chaveamento completo, podemos retornar o número de partidas da 1ª rodada
        total_partidas_1a_rodada = len(chaveamento[0]) if chaveamento and chaveamento[0] else 0

        # Retorna o JSON de sucesso para o JavaScript
        return jsonify({
            "status": "sucesso",
            "mensagem": f"Chaveamento de {esporte} ({classificacao}) gerado e salvo.",
            "total_partidas": total_partidas_1a_rodada
        })

    except Exception as e:
        print(f"Erro Crítico ao Gerar Chaveamento: {e}")
        # Retorna o JSON de erro
        return jsonify({
            "status": "erro", 
            "mensagem": f"Erro interno ao gerar chaveamento: {str(e)}"
        }), 500
    
@app.route("/chaveamento/partidas", methods=["GET"])
def rotaBuscarPartidas():
    """
    Busca as partidas de uma chave (filtrada por GET) para listagem no painel.
    """
    # Recebe os filtros do JavaScript via URL params (request.args)
    esporte = request.args.get('esporte')
    classificacao = request.args.get('classificacao')
    
    if not esporte and not classificacao:
        return jsonify({"status": "erro", "mensagem": "Filtros são obrigatórios para buscar partidas."}), 400

    try:
        # 1. Busca no BD a lista completa de partidas da chave (com nomes das equipes)
        partidas_bd = buscarPartidasParaGestao(esporte, classificacao) 
        print(partidas_bd)

        # 2. Prepara o JSON para o frontend
        partidas_json = []
        for p in partidas_bd:
            # Assumimos que a função de busca (buscarPartidasParaGestao) já traz 'pk_equipe_vencedora'
            partidas_json.append({
                "pk_partida": p['pk_partida'],
                "esporte": p['fk_esporte'],
                "classificacao": p['fk_genero'],
                "etapa": p['etapa'],
                "fk_equipe_casa": p['fk_equipe_casa'],
                "equipe_casa_nome": p['nome_equipe_casa'],
                "fk_equipe_visitante": p['fk_equipe_visitante'],
                "equipe_visitante_nome": p['nome_equipe_visitante'],
                "vencedor_pk": p.get('pk_equipe_vencedora')
            })

        return jsonify({"status": "sucesso", "partidas": partidas_json})

    except Exception as e:
        print(f"Erro ao buscar partidas: {e}")
        return jsonify({"status": "erro", "mensagem": "Falha ao carregar partidas do banco de dados."}), 500


@app.route("/chaveamento", methods=['GET'])
def chaveamentoTeste():
    esportes = buscarEsportes()
    generos = buscarClassificacoes()

    return render_template("chaveamento.html", esportes=esportes, generos=generos)

@app.route("/chaveamento", methods=['POST'])
def chaveamentoTesteCarregar():
    esporte = request.form['esporte']
    genero = request.form['genero']

    tabela = buscarPartidasParaGestao(esporte, genero)
    print(tabela)
    esportes = buscarEsportes()
    generos = buscarClassificacoes()
    return render_template("chaveamento.html", esportes=esportes, generos=generos, tabela=tabela)


@app.route("/chaveamento/vencedor", methods=["POST"])
@requerAdmin
def rotaRegistrarVencedor():
    partida_id = request.form['partida_id']
    cod_partida_mae = request.form.get('cod_partida_mae')

    cod_equipe_casa = request.form['cod_equipe_casa']
    cod_equipe_visitante = request.form['cod_equipe_visitante']

    pontos_equipe_casa = int(request.form['pontos_equipe_casa'])
    pontos_equipe_visitante = int(request.form['pontos_equipe_visitante'])

    genero = request.form['genero']
    esporte = request.form['esporte']

    vencedor_id = (
        cod_equipe_casa
        if pontos_equipe_casa > pontos_equipe_visitante
        else cod_equipe_visitante
    )

    salvarVencedorPartida(
        partida_id,
        vencedor_id,
        pontos_equipe_casa,
        pontos_equipe_visitante,
        cod_partida_mae
    )

    tabela = buscarPartidasParaGestao(esporte, genero)
    esportes = buscarEsportes()
    generos = buscarClassificacoes()

    return render_template(
        "chaveamento.html",
        esportes=esportes,
        generos=generos,
        tabela=tabela
    )

#---------------- CALENDÁRIO ------------------#

@app.route('/calendarioteste')
def calendarioteste():
    # Somente Administrador pode alterar o calendário.
    podeEditar = session.get('nivel') == 'Administrador'
    return render_template('calendario2.html', podeEditar=podeEditar)


@app.route('/calendario/eventos')
def eventosCalendario():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                c.pk_evento,
                c.dia_evento,
                c.hora_inicio,
                c.hora_fim,
                p.fk_esporte,
                p.fk_genero,
                p.etapa,
                ec.nome_equipe AS equipe_casa,
                ev.nome_equipe AS equipe_visitante
            FROM calendario c
            INNER JOIN partidas p
                ON c.fk_partida = p.pk_partida
            INNER JOIN equipes ec
                ON p.fk_equipe_casa = ec.pk_equipe
            INNER JOIN equipes ev
                ON p.fk_equipe_visitante = ev.pk_equipe
            ORDER BY c.dia_evento, c.hora_inicio
        """)

        cores = {
            'Vôlei': '#1976d2',
            'Futsal': '#111111',
            'Basquete': '#f57c00',
            'Handebol': '#d32f2f',
            'Queimada': '#2e7d32',
            'Xadrez': '#6a1b9a',
            'Tênis de Mesa': '#c9a227'
        }

        etapas = {
            1: 'Rodada 1',
            2: 'Rodada 2',
            3: 'Rodada 3',
            4: 'Rodada 4'
        }

        eventos = []

        for e in cursor.fetchall():
            etapa = e['etapa']

            eventos.append({
                'id': str(e['pk_evento']),
                'title': f"{e['equipe_casa']} × {e['equipe_visitante']}",
                'start': f"{e['dia_evento']}T{e['hora_inicio']}",
                'end': f"{e['dia_evento']}T{e['hora_fim']}",
                'backgroundColor': cores.get(e['fk_esporte'], '#3788d8'),
                'extendedProps': {
                    'esporte': e['fk_esporte'],
                    'genero': e['fk_genero'],
                    'etapa': etapas.get(etapa, f'Rodada {etapa}')
                }
            })

        return jsonify(eventos)

    except Exception as erro:
        print("Erro ao carregar calendário:", erro)
        return jsonify({'erro': 'Não foi possível carregar o calendário.'}), 500

    finally:
        cursor.close()
        conexao.close()


@app.route('/calendario/filtros')
def filtrosCalendario():
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        # Puxa somente valores que realmente existem em partidas
        # e que possuem as duas equipes definidas.
        cursor.execute("""
            SELECT DISTINCT fk_esporte
            FROM partidas
            WHERE fk_esporte IS NOT NULL
              AND fk_equipe_casa IS NOT NULL
              AND fk_equipe_visitante IS NOT NULL
            ORDER BY fk_esporte
        """)
        esportes = [x[0] for x in cursor.fetchall()]

        cursor.execute("""
            SELECT DISTINCT fk_genero
            FROM partidas
            WHERE fk_genero IS NOT NULL
              AND fk_equipe_casa IS NOT NULL
              AND fk_equipe_visitante IS NOT NULL
            ORDER BY fk_genero
        """)
        generos = [x[0] for x in cursor.fetchall()]

        return jsonify({
            'esportes': esportes,
            'generos': generos
        })

    except Exception as erro:
        print("Erro ao carregar filtros:", erro)
        return jsonify({
            'esportes': [],
            'generos': []
        }), 500

    finally:
        cursor.close()
        conexao.close()


@app.route('/calendario/partidas')
def partidasCalendario():
    esporte = request.args.get('esporte')
    genero = request.args.get('genero')
    etapa = request.args.get('etapa', type=int)

    if not esporte or not genero or etapa is None:
        return jsonify([])

    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                p.pk_partida,
                p.fk_esporte,
                p.fk_genero,
                p.etapa,
                ec.nome_equipe AS equipe_casa,
                ev.nome_equipe AS equipe_visitante
            FROM partidas p
            INNER JOIN equipes ec
                ON p.fk_equipe_casa = ec.pk_equipe
            INNER JOIN equipes ev
                ON p.fk_equipe_visitante = ev.pk_equipe
            LEFT JOIN calendario c
                ON c.fk_partida = p.pk_partida
            WHERE p.fk_esporte = %s
              AND p.fk_genero = %s
              AND p.etapa = %s
              AND c.fk_partida IS NULL
            ORDER BY p.pk_partida
        """, (esporte, genero, etapa))

        return jsonify(cursor.fetchall())

    except Exception as erro:
        print("Erro ao buscar partidas do calendário:", erro)
        return jsonify([]), 500

    finally:
        cursor.close()
        conexao.close()


@app.route('/calendario/adicionar', methods=['POST'])
def adicionarCalendario():
    if session.get('nivel') != 'Administrador':
        return jsonify({
            'mensagem': 'Apenas o Administrador pode alterar o calendário.'
        }), 403

    dados = request.get_json(silent=True) or {}
    data_evento = dados.get('data')
    partida = dados.get('fk_partida')
    inicio = dados.get('hora_inicio')
    fim = dados.get('hora_fim')

    if not all([data_evento, partida, inicio, fim]):
        return jsonify({'mensagem': 'Preencha todos os campos.'}), 400

    if fim <= inicio:
        return jsonify({
            'mensagem': 'O horário final deve ser maior que o inicial.'
        }), 400

    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        # A partida precisa existir e ter as duas equipes.
        cursor.execute("""
            SELECT pk_partida
            FROM partidas
            WHERE pk_partida = %s
              AND fk_equipe_casa IS NOT NULL
              AND fk_equipe_visitante IS NOT NULL
        """, (partida,))

        if not cursor.fetchone():
            return jsonify({'mensagem': 'Partida inválida.'}), 400

        # A mesma partida só pode aparecer uma vez no calendário.
        cursor.execute("""
            SELECT pk_evento
            FROM calendario
            WHERE fk_partida = %s
        """, (partida,))

        if cursor.fetchone():
            return jsonify({
                'mensagem': 'Essa partida já está no calendário.'
            }), 400

        cursor.execute("""
            INSERT INTO calendario
                (dia_evento, fk_partida, hora_inicio, hora_fim)
            VALUES (%s, %s, %s, %s)
        """, (data_evento, partida, inicio, fim))

        conexao.commit()

        return jsonify({'mensagem': 'Partida adicionada!'})

    except Exception as erro:
        conexao.rollback()
        print("Erro ao adicionar partida:", erro)
        return jsonify({
            'mensagem': 'Erro ao adicionar partida.'
        }), 500

    finally:
        cursor.close()
        conexao.close()


@app.route('/calendario/editar', methods=['POST'])
def editarCalendario():
    if session.get('nivel') != 'Administrador':
        return jsonify({
            'mensagem': 'Apenas o Administrador pode editar.'
        }), 403

    dados = request.get_json(silent=True) or {}
    evento = dados.get('id')
    inicio = dados.get('hora_inicio')
    fim = dados.get('hora_fim')

    if not all([evento, inicio, fim]):
        return jsonify({'mensagem': 'Dados incompletos.'}), 400

    if fim <= inicio:
        return jsonify({
            'mensagem': 'O horário final deve ser maior que o inicial.'
        }), 400

    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE calendario
            SET hora_inicio = %s,
                hora_fim = %s
            WHERE pk_evento = %s
        """, (inicio, fim, evento))

        conexao.commit()

        return jsonify({'mensagem': 'Horário atualizado!'})

    except Exception as erro:
        conexao.rollback()
        print("Erro ao editar:", erro)
        return jsonify({
            'mensagem': 'Erro ao editar horário.'
        }), 500

    finally:
        cursor.close()
        conexao.close()


@app.route('/calendario/remover', methods=['POST'])
def removerCalendario():
    if session.get('nivel') != 'Administrador':
        return jsonify({
            'mensagem': 'Apenas o Administrador pode remover.'
        }), 403

    dados = request.get_json(silent=True) or {}
    evento = dados.get('id')

    if not evento:
        return jsonify({'mensagem': 'Evento inválido.'}), 400

    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        # Remove somente a programação.
        # A partida continua existindo em "partidas".
        cursor.execute("""
            DELETE FROM calendario
            WHERE pk_evento = %s
        """, (evento,))

        conexao.commit()

        return jsonify({
            'mensagem': 'Partida removida do calendário!'
        })

    except Exception as erro:
        conexao.rollback()
        print("Erro ao remover:", erro)
        return jsonify({
            'mensagem': 'Erro ao remover partida.'
        }), 500

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    app.run(debug=True)