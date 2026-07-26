from flask import Flask, render_template, redirect, request, session, jsonify, flash, url_for
from functools import wraps
from datetime import timedelta, datetime
from model import *
from calendar import *

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

    if not usuario_encontrado:
        flash('Usuário não encontrado.', 'error')
        return redirect(url_for('login'))

    if senha != usuario_encontrado['senha']:
        flash('Senha incorreta.', 'error')
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
    return render_template("home.html", nome_usuario=session['nome'], nivel=session['nivel'])

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
def paginacadastrarAluno():
    if session['nivel'] == 'AlunoMonitor':
        alunos = buscarAlunosPorTurma(session['turma'])  # apenas a turma do monitor
        turmas = [ {"pk_nome_turma": session['turma']} ] # só a turma dele
    else:  # Administrador
        alunos = buscarAlunos()
        turmas = buscarTurmas()
    
    return render_template("cadastrarAluno.html", alunos=alunos, turmas=turmas)

@app.route("/cadastrarAluno", methods=["POST"])
def rotaCadastrarAluno():
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    turma = request.form.get("turma")
    genero = request.form.get("genero")

    cadastrarAluno(matricula, nome, turma, genero)
    return redirect(url_for("paginacadastrarAluno"))

@app.route("/editarAluno/<antiga_matricula>", methods=["POST"])
def rotaEditarAluno(antiga_matricula):
    nome = request.form.get("nome")
    turma = request.form.get("turma")
    genero = request.form.get("genero")
    antiga_matricula = request.form.get("antiga_matricula")
    nova_matricula = request.form.get("nova_matricula")

    editarAluno(nova_matricula, nome, turma, genero, antiga_matricula)
    
    return redirect(url_for("paginacadastrarAluno"))

@app.route("/deletarAluno/<matricula>")
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
    esportes = buscarEsportes()
    classificacoes = buscarClassificacoes()

    # Visitante (sem login) → session.get('nivel') será None
    nivel = session.get("nivel")
    turma = session.get("turma")

    if nivel == "AlunoMonitor":
        equipes = buscarEquipesPorTurma(turma) if turma else []
        turmas = [{"pk_nome_turma": turma}] if turma else []
    elif nivel == "Administrador":
        equipes = buscarEquipes()
        turmas = buscarTurmas()
    else:  # visitante
        equipes = buscarEquipes()
        turmas = []  # visitante não precisa cadastrar, só visualizar

    return render_template(
        "cadastrarEquipe.html",
        equipes=equipes,
        esportes=esportes,
        turmas=turmas,
        classificacoes=classificacoes,
        nivel=nivel
    )


@app.route("/cadastrarEquipe", methods=["POST"])
def rotaCadastrarEquipe():
    esporte = request.form.get("esporte")
    turma = request.form.get("turma")
    genero = request.form.get("genero")
    alunos = request.form.getlist("alunos")

    cadastrarEquipe(esporte, turma, genero, alunos)
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

    flash("Equipe atualizada com sucesso.", "success")
    return redirect("/cadastrarEquipe")

#Deletar equipe
@app.route("/deletarEquipe/<int:pk_equipe>")
@requerAdminOuMonitor
def rotaDeletarEquipe(pk_equipe):
    resultado = deletarEquipe(pk_equipe)
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

    cadastrarUsuario(pk_usuario, senha, nivel, fk_nome_turma)
    flash("Usuário cadastrado com sucesso!", "success")
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


## ----------------GERENCIAR MODALIDADES/ESTATÍSTICAS------------------ ##

@app.route("/gerenciarModalidades/")
def gerenciarModalidades():
    ano, mes, dia = datetime.now().strftime("%Y"), datetime.now().strftime("%m"), datetime.now().strftime("%d")
    return render_template("gerenciarModalidades.html", ano=ano, mes=mes, dia=dia)

@app.route("/gerenciarEstatisticas/")
def gerenciarEstatisticas():
    ano, mes, dia = datetime.now().strftime("%Y"), datetime.now().strftime("%m"), datetime.now().strftime("%d")
    return redirect(f"/gerenciarEstatisticas/{ano}/{mes}/{dia}")

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