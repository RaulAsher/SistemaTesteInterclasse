document.addEventListener('DOMContentLoaded', () => {

    const calendarEl = document.getElementById('calendar');

    if (!calendarEl) return;


    // =====================================================
    // FILTROS
    // =====================================================

    let filtros = {
        esporte: '',
        genero: '',
        turma: ''
    };


    // =====================================================
    // CALENDÁRIO
    // =====================================================

    const calendar = new FullCalendar.Calendar(
        calendarEl,
        {

            locale: 'pt-br',

            initialView: 'dayGridMonth',

            firstDay: 1,


            // Semana removida
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridDay'
            },


            buttonText: {
                today: 'Hoje',
                month: 'Mês',
                day: 'Dia'
            },


            // Não esconder partidas quando houver várias
            // no mesmo dia.
            dayMaxEvents: false,

            eventDisplay: 'block',

            eventOrder: 'start,title',


            // Eventos
            events: carregarEventos,


            // Aparência dos eventos
            eventContent: mostrarEvento,


            // Clique no dia
            dateClick: info => {
                abrirPopupDia(info.dateStr);
            }

        }
    );


    calendar.render();


    // =====================================================
    // ELEMENTOS DO FILTRO
    // =====================================================

    const btnFiltro =
        document.getElementById(
            'btnFiltroCalendario'
        );

    const btnLimpar =
        document.getElementById(
            'btnLimparFiltro'
        );

    const filtrosAtivos =
        document.getElementById(
            'filtrosAtivos'
        );


    btnFiltro?.addEventListener(
        'click',
        abrirFiltro
    );


    btnLimpar?.addEventListener(
        'click',
        limparFiltros
    );


    // =====================================================
    // CARREGAR EVENTOS
    // =====================================================

    async function carregarEventos(
        fetchInfo,
        successCallback,
        failureCallback
    ) {

        try {

            const resposta =
                await fetch(
                    '/calendario/eventos'
                );


            if (!resposta.ok) {

                throw new Error(
                    `Erro HTTP ${resposta.status}`
                );

            }


            let eventos =
                await resposta.json();


            // ---------------------------------------------
            // APLICA OS FILTROS
            // ---------------------------------------------

            eventos =
                eventos.filter(
                    evento => {

                        const props =
                            evento.extendedProps || {};


                        const esporteOk =
                            !filtros.esporte ||
                            props.esporte ===
                                filtros.esporte;


                        const generoOk =
                            !filtros.genero ||
                            props.genero ===
                                filtros.genero;


                        const turmaOk =
                            !filtros.turma ||
                            (
                                Array.isArray(
                                    props.turmas
                                ) &&
                                props.turmas.includes(
                                    filtros.turma
                                )
                            );


                        return (
                            esporteOk &&
                            generoOk &&
                            turmaOk
                        );

                    }
                );


            successCallback(
                eventos
            );

        } catch (erro) {

            console.error(
                'Erro ao carregar eventos:',
                erro
            );

            failureCallback(
                erro
            );

        }

    }


    // =====================================================
    // APARÊNCIA DOS EVENTOS
    // =====================================================

    function mostrarEvento(info) {

        const props =
            info.event.extendedProps || {};


        // ---------------------------------------------
        // MODO DIA
        // ---------------------------------------------

        if (
            info.view.type ===
            'timeGridDay'
        ) {

            return {

                html: `

                    <div class="evento-dia">

                        <div class="evento-dia-titulo">

                            ${esc(
                                info.event.title
                            )}

                        </div>


                        <div class="evento-dia-info">

                            ${esc(
                                props.esporte || ''
                            )}

                            •
                            
                            ${esc(
                                props.genero || ''
                            )}

                        </div>

                    </div>

                `

            };

        }


        // ---------------------------------------------
        // MODO MÊS
        // ---------------------------------------------

        return {

            html: `

                <div
                    class="evento-mes"
                    title="${esc(
                        info.event.title +
                        ' — ' +
                        (props.esporte || '') +
                        ' • ' +
                        (props.genero || '')
                    )}"
                >

                    ${esc(
                        info.event.title
                    )}

                </div>

            `

        };

    }


    // =====================================================
    // POPUP DO DIA
    // =====================================================

    function abrirPopupDia(
        data
    ) {

        const eventos =
            calendar
                .getEvents()
                .filter(
                    evento => {

                        return (
                            evento.start &&
                            formatarData(
                                evento.start
                            ) === data
                        );

                    }
                )
                .sort(
                    (a, b) =>
                        a.start - b.start
                );


        const dataBR =
            new Date(
                `${data}T00:00:00`
            ).toLocaleDateString(
                'pt-BR',
                {
                    weekday: 'long',
                    day: '2-digit',
                    month: 'long',
                    year: 'numeric'
                }
            );


        const lista =
            eventos.length

                ? eventos
                    .map(
                        jogoHTML
                    )
                    .join('')

                : `

                    <div class="sem-jogos">

                        Não há jogos cadastrados
                        neste dia com os filtros atuais.

                    </div>

                `;


        const botoes =
            window.usuarioPodeEditar

                ? `

                    <button
                        class="btn-adicionar"
                        id="btnAdicionar"
                    >

                        + Adicionar partida

                    </button>


                    ${
                        eventos.length

                            ? `

                                <button
                                    class="btn-editar"
                                    id="btnEditar"
                                >

                                    Editar

                                </button>

                            `

                            : ''
                    }

                `

                : '';


        const popup =
            criarPopup(`

                <button
                    class="fechar-popup"
                    id="fechar"
                >

                    ×

                </button>


                <h2>
                    Jogos do dia
                </h2>


                <p class="data-popup">

                    ${dataBR}

                </p>


                <div class="lista-jogos-popup">

                    ${lista}

                </div>


                <div class="popup-botoes">

                    ${botoes}

                </div>

            `);


        popup.querySelector(
            '#fechar'
        ).onclick =
            () => popup.remove();


        popup.querySelector(
            '#btnAdicionar'
        )?.addEventListener(
            'click',
            () => {

                popup.remove();

                abrirAdicionar(
                    data
                );

            }
        );


        popup.querySelector(
            '#btnEditar'
        )?.addEventListener(
            'click',
            () => {

                popup.remove();

                abrirEdicao(
                    data,
                    eventos
                );

            }
        );

    }


    // =====================================================
    // JOGO DO POPUP
    // =====================================================

    function jogoHTML(
        evento
    ) {

        const props =
            evento.extendedProps || {};


        const inicio =
            evento.start
                ? evento.start.toLocaleTimeString(
                    'pt-BR',
                    {
                        hour: '2-digit',
                        minute: '2-digit'
                    }
                )
                : '';


        const fim =
            evento.end
                ? evento.end.toLocaleTimeString(
                    'pt-BR',
                    {
                        hour: '2-digit',
                        minute: '2-digit'
                    }
                )
                : '';


        return `

            <div
                class="jogo-popup"
                style="
                    border-left-color:
                    ${evento.backgroundColor || '#3788d8'};
                "
            >

                <strong>

                    ${esc(
                        evento.title
                    )}

                </strong>


                <div class="jogo-detalhes">

                    ${esc(
                        props.esporte || ''
                    )}

                    -

                    ${esc(
                        props.genero || ''
                    )}

                    -

                    ${esc(
                        props.turma_casa ||
                        'Turma não informada'
                    )}

                    ×

                    ${esc(
                        props.turma_visitante ||
                        'Turma não informada'
                    )}

                    -

                    ${esc(
                        props.etapa || ''
                    )}

                </div>


                <span>

                    ${inicio}
                    -
                    ${fim}

                </span>

            </div>

        `;

    }


    // =====================================================
    // ADICIONAR PARTIDA
    // =====================================================

    async function abrirAdicionar(
        data
    ) {

        const dados =
            await buscarFiltros();


        if (!dados) return;


        const popup =
            criarPopup(`

                <button
                    class="fechar-popup"
                    id="fechar"
                >

                    ×

                </button>


                <h2>
                    Adicionar partida
                </h2>


                <p class="data-popup">

                    ${formatarDataBR(
                        data
                    )}

                </p>


                ${selectHTML(
                    'esporte',
                    'Modalidade',
                    dados.esportes || [],
                    'Selecione'
                )}


                ${selectHTML(
                    'genero',
                    'Gênero',
                    dados.generos || [],
                    'Selecione'
                )}


                <div class="campo-formulario">

                    <label>
                        Rodada
                    </label>


                    <select id="etapa">

                        <option value="">
                            Selecione
                        </option>

                        <option value="1">
                            Rodada 1
                        </option>

                        <option value="2">
                            Rodada 2
                        </option>

                        <option value="3">
                            Rodada 3
                        </option>

                        <option value="4">
                            Rodada 4
                        </option>

                    </select>

                </div>


                <div class="campo-formulario">

                    <label>
                        Partida
                    </label>


                    <div
                        id="partidas"
                        class="lista-partidas"
                    >

                        Selecione modalidade,
                        gênero e rodada.

                    </div>

                </div>


                <div class="linha-horarios">

                    <div class="campo-formulario">

                        <label>
                            Início
                        </label>


                        <input
                            type="time"
                            id="inicio"
                        >

                    </div>


                    <div class="campo-formulario">

                        <label>
                            Fim
                        </label>


                        <input
                            type="time"
                            id="fim"
                        >

                    </div>

                </div>


                <div
                    id="mensagem"
                    class="mensagem-formulario"
                ></div>


                <div class="popup-botoes">

                    <button
                        class="btn-cancelar"
                        id="cancelar"
                    >

                        Cancelar

                    </button>


                    <button
                        class="btn-salvar"
                        id="salvar"
                    >

                        Adicionar

                    </button>

                </div>

            `);


        popup.querySelector(
            '#fechar'
        ).onclick =
            () => popup.remove();


        popup.querySelector(
            '#cancelar'
        ).onclick =
            () => {

                popup.remove();

                abrirPopupDia(
                    data
                );

            };


        // =================================================
        // BUSCAR PARTIDAS DISPONÍVEIS
        // =================================================

        async function buscarPartidas() {

            const esporte =
                popup.querySelector(
                    '#esporte'
                ).value;


            const genero =
                popup.querySelector(
                    '#genero'
                ).value;


            const etapa =
                popup.querySelector(
                    '#etapa'
                ).value;


            const lista =
                popup.querySelector(
                    '#partidas'
                );


            if (
                !esporte ||
                !genero ||
                !etapa
            ) {

                lista.textContent =
                    'Selecione modalidade, gênero e rodada.';

                return;

            }


            lista.textContent =
                'Buscando partidas...';


            try {

                const params =
                    new URLSearchParams({
                        esporte,
                        genero,
                        etapa
                    });


                const resposta =
                    await fetch(
                        `/calendario/partidas?${params}`
                    );


                if (!resposta.ok) {

                    const texto =
                        await resposta.text();

                    console.error(
                        'Erro ao buscar partidas:',
                        texto
                    );

                    throw new Error(
                        `HTTP ${resposta.status}`
                    );

                }


                const partidas =
                    await resposta.json();


                if (!partidas.length) {

                    lista.textContent =
                        'Nenhuma partida disponível.';

                    return;

                }


                lista.innerHTML =
                    partidas
                        .map(
                            partida => `

                                <label
                                    class="partida-opcao"
                                >

                                    <input
                                        type="radio"
                                        name="partida"
                                        value="${esc(
                                            partida.pk_partida
                                        )}"
                                    >


                                    <span>

                                        ${esc(
                                            partida.equipe_casa
                                        )}

                                        ×

                                        ${esc(
                                            partida.equipe_visitante
                                        )}

                                    </span>

                                </label>

                            `
                        )
                        .join('');


            } catch (erro) {

                console.error(
                    'Erro ao buscar partidas:',
                    erro
                );

                lista.textContent =
                    'Erro ao buscar partidas.';

            }

        }


        popup.querySelector(
            '#esporte'
        ).addEventListener(
            'change',
            buscarPartidas
        );


        popup.querySelector(
            '#genero'
        ).addEventListener(
            'change',
            buscarPartidas
        );


        popup.querySelector(
            '#etapa'
        ).addEventListener(
            'change',
            buscarPartidas
        );


        // =================================================
        // SALVAR / ADICIONAR
        // =================================================

        popup.querySelector(
            '#salvar'
        ).addEventListener(
            'click',
            async function () {

                const botao =
                    this;


                const partida =
                    popup.querySelector(
                        'input[name="partida"]:checked'
                    );


                const inicio =
                    popup.querySelector(
                        '#inicio'
                    ).value;


                const fim =
                    popup.querySelector(
                        '#fim'
                    ).value;


                const mensagem =
                    popup.querySelector(
                        '#mensagem'
                    );


                // -----------------------------------------
                // VALIDAÇÃO
                // -----------------------------------------

                if (
                    !partida ||
                    !inicio ||
                    !fim
                ) {

                    mensagem.textContent =
                        'Preencha todos os campos.';

                    return;

                }


                if (fim <= inicio) {

                    mensagem.textContent =
                        'O horário final deve ser maior que o inicial.';

                    return;

                }


                botao.disabled =
                    true;

                botao.textContent =
                    'Salvando...';


                try {

                    const resposta =
                        await fetch(
                            '/calendario/adicionar',
                            {
                                method:
                                    'POST',

                                headers: {
                                    'Content-Type':
                                        'application/json'
                                },

                                body:
                                    JSON.stringify({

                                        data:
                                            data,

                                        fk_partida:
                                            partida.value,

                                        hora_inicio:
                                            inicio,

                                        hora_fim:
                                            fim

                                    })
                            }
                        );


                    // -------------------------------------
                    // LÊ A RESPOSTA DO FLASK
                    // -------------------------------------

                    let resultado = {};

                    try {

                        resultado =
                            await resposta.json();

                    } catch {

                        resultado = {};

                    }


                    console.log(
                        'Resposta adicionar:',
                        resposta.status,
                        resultado
                    );


                    // -------------------------------------
                    // ERRO
                    // -------------------------------------

                    if (!resposta.ok) {

                        mensagem.textContent =
                            resultado.mensagem ||
                            `Erro ao adicionar partida (HTTP ${resposta.status}).`;


                        botao.disabled =
                            false;

                        botao.textContent =
                            'Adicionar';

                        return;

                    }


                    // -------------------------------------
                    // SUCESSO
                    // -------------------------------------

                    popup.remove();


                    // Atualiza o calendário
                    await calendar.refetchEvents();


                    // Mostra novamente os jogos daquele dia
                    abrirPopupDia(
                        data
                    );


                } catch (erro) {

                    console.error(
                        'Erro ao adicionar:',
                        erro
                    );


                    mensagem.textContent =
                        'Erro de comunicação com o servidor.';


                    botao.disabled =
                        false;

                    botao.textContent =
                        'Adicionar';

                }

            }
        );

    }


    // =====================================================
    // EDITAR
    // =====================================================

    function abrirEdicao(
        data,
        eventos
    ) {

        const jogos =
            eventos
                .sort(
                    (a, b) =>
                        a.start - b.start
                )
                .map(
                    evento => {

                        const inicio =
                            evento.start
                                ? evento.start.toLocaleTimeString(
                                    'pt-BR',
                                    {
                                        hour:
                                            '2-digit',
                                        minute:
                                            '2-digit'
                                    }
                                )
                                : '';


                        const fim =
                            evento.end
                                ? evento.end.toLocaleTimeString(
                                    'pt-BR',
                                    {
                                        hour:
                                            '2-digit',
                                        minute:
                                            '2-digit'
                                    }
                                )
                                : '';


                        const props =
                            evento.extendedProps || {};


                        return `

                            <div
                                class="edicao-jogo"
                                data-id="${esc(
                                    evento.id
                                )}"
                            >

                                <h3>

                                    ${esc(
                                        evento.title
                                    )}

                                </h3>


                                <div
                                    class="filtro-resumo"
                                >

                                    ${esc(
                                        props.esporte || ''
                                    )}

                                    -

                                    ${esc(
                                        props.genero || ''
                                    )}

                                    -

                                    ${esc(
                                        props.turma_casa ||
                                        'Turma não informada'
                                    )}

                                    ×

                                    ${esc(
                                        props.turma_visitante ||
                                        'Turma não informada'
                                    )}

                                </div>


                                <div
                                    class="linha-horarios"
                                >

                                    <div
                                        class="campo-formulario"
                                    >

                                        <label>
                                            Início
                                        </label>


                                        <input
                                            type="time"
                                            class="campo-inicio"
                                            value="${inicio}"
                                        >

                                    </div>


                                    <div
                                        class="campo-formulario"
                                    >

                                        <label>
                                            Fim
                                        </label>


                                        <input
                                            type="time"
                                            class="campo-fim"
                                            value="${fim}"
                                        >

                                    </div>

                                </div>


                                <button
                                    class="btn-remover btn-remover-jogo"
                                >

                                    Remover do calendário

                                </button>

                            </div>

                        `;

                    }
                )
                .join('');


        const popup =
            criarPopup(`

                <button
                    class="fechar-popup"
                    id="fechar"
                >

                    ×

                </button>


                <h2>
                    Editar jogos
                </h2>


                <p class="data-popup">

                    ${formatarDataBR(
                        data
                    )}

                </p>


                ${jogos}


                <div
                    id="mensagem"
                    class="mensagem-formulario"
                ></div>


                <div class="popup-botoes">

                    <button
                        class="btn-cancelar"
                        id="cancelar"
                    >

                        Cancelar

                    </button>


                    <button
                        class="btn-salvar"
                        id="salvar"
                    >

                        Salvar alterações

                    </button>

                </div>

            `);


        popup.querySelector(
            '#fechar'
        ).onclick =
            () => popup.remove();


        popup.querySelector(
            '#cancelar'
        ).onclick =
            () => {

                popup.remove();

                abrirPopupDia(
                    data
                );

            };


        // =================================================
        // REMOVER
        // =================================================

        popup.querySelectorAll(
            '.btn-remover-jogo'
        ).forEach(
            botao => {

                botao.addEventListener(
                    'click',
                    async () => {

                        const jogo =
                            botao.closest(
                                '.edicao-jogo'
                            );


                        if (!jogo) return;


                        if (
                            !confirm(
                                'Tem certeza que deseja remover esta partida do calendário?'
                            )
                        ) {

                            return;

                        }


                        const mensagem =
                            popup.querySelector(
                                '#mensagem'
                            );


                        botao.disabled =
                            true;


                        botao.textContent =
                            'Removendo...';


                        try {

                            const resposta =
                                await fetch(
                                    '/calendario/remover',
                                    {
                                        method:
                                            'POST',

                                        headers: {
                                            'Content-Type':
                                                'application/json'
                                        },

                                        body:
                                            JSON.stringify({
                                                id:
                                                    jogo.dataset.id
                                            })
                                    }
                                );


                            let resultado = {};

                            try {

                                resultado =
                                    await resposta.json();

                            } catch {

                                resultado = {};

                            }


                            if (!resposta.ok) {

                                mensagem.textContent =
                                    resultado.mensagem ||
                                    `Erro ao remover partida (HTTP ${resposta.status}).`;

                                botao.disabled =
                                    false;

                                botao.textContent =
                                    'Remover do calendário';

                                return;

                            }


                            jogo.remove();


                            await calendar.refetchEvents();


                            mensagem.classList.add(
                                'mensagem-sucesso'
                            );


                            mensagem.textContent =
                                resultado.mensagem ||
                                'Partida removida do calendário.';


                            if (
                                !popup.querySelector(
                                    '.edicao-jogo'
                                )
                            ) {

                                setTimeout(
                                    () => {

                                        popup.remove();

                                        abrirPopupDia(
                                            data
                                        );

                                    },
                                    400
                                );

                            }


                        } catch (erro) {

                            console.error(
                                'Erro ao remover:',
                                erro
                            );


                            mensagem.textContent =
                                'Erro de comunicação com o servidor.';


                            botao.disabled =
                                false;


                            botao.textContent =
                                'Remover do calendário';

                        }

                    }
                );

            }
        );


        // =================================================
        // SALVAR ALTERAÇÕES
        // =================================================

        popup.querySelector(
            '#salvar'
        ).addEventListener(
            'click',
            async function () {

                const botao =
                    this;


                const mensagem =
                    popup.querySelector(
                        '#mensagem'
                    );


                const jogos =
                    [
                        ...popup.querySelectorAll(
                            '.edicao-jogo'
                        )
                    ];


                const alteracoes = [];


                // -----------------------------------------
                // VALIDAÇÃO
                // -----------------------------------------

                for (
                    const jogo
                    of jogos
                ) {

                    const inicio =
                        jogo.querySelector(
                            '.campo-inicio'
                        ).value;


                    const fim =
                        jogo.querySelector(
                            '.campo-fim'
                        ).value;


                    if (
                        !inicio ||
                        !fim ||
                        fim <= inicio
                    ) {

                        mensagem.textContent =
                            'Verifique os horários.';

                        return;

                    }


                    alteracoes.push({

                        id:
                            jogo.dataset.id,

                        hora_inicio:
                            inicio,

                        hora_fim:
                            fim

                    });

                }


                botao.disabled =
                    true;


                botao.textContent =
                    'Salvando...';


                try {

                    for (
                        const alteracao
                        of alteracoes
                    ) {

                        const resposta =
                            await fetch(
                                '/calendario/editar',
                                {
                                    method:
                                        'POST',

                                    headers: {
                                        'Content-Type':
                                            'application/json'
                                    },

                                    body:
                                        JSON.stringify(
                                            alteracao
                                        )
                                }
                            );


                        let resultado = {};

                        try {

                            resultado =
                                await resposta.json();

                        } catch {

                            resultado = {};

                        }


                        if (!resposta.ok) {

                            mensagem.textContent =
                                resultado.mensagem ||
                                `Erro ao salvar (HTTP ${resposta.status}).`;

                            botao.disabled =
                                false;

                            botao.textContent =
                                'Salvar alterações';

                            return;

                        }

                    }


                    popup.remove();


                    await calendar.refetchEvents();


                    abrirPopupDia(
                        data
                    );


                } catch (erro) {

                    console.error(
                        'Erro ao salvar:',
                        erro
                    );


                    mensagem.textContent =
                        'Erro de comunicação com o servidor.';


                    botao.disabled =
                        false;


                    botao.textContent =
                        'Salvar alterações';

                }

            }
        );

    }


    // =====================================================
    // FILTRO
    // =====================================================

    async function abrirFiltro() {

        const dados =
            await buscarFiltros();


        if (!dados) return;


        const popup =
            criarPopup(`

                <button
                    class="fechar-popup"
                    id="fechar"
                >

                    ×

                </button>


                <h2>
                    Filtrar calendário
                </h2>


                <p class="filtro-ajuda">

                    O filtro altera somente
                    a visualização do calendário.

                </p>


                ${selectHTML(
                    'filtroEsporte',
                    'Modalidade',
                    dados.esportes || [],
                    'Todas as modalidades',
                    filtros.esporte
                )}


                ${selectHTML(
                    'filtroGenero',
                    'Gênero',
                    dados.generos || [],
                    'Todos os gêneros',
                    filtros.genero
                )}


                ${selectHTML(
                    'filtroTurma',
                    'Turma',
                    dados.turmas || [],
                    'Todas as turmas',
                    filtros.turma
                )}


                <div class="popup-botoes">

                    <button
                        class="btn-cancelar"
                        id="cancelar"
                    >

                        Cancelar

                    </button>


                    <button
                        class="btn-salvar"
                        id="filtrar"
                    >

                        Filtrar

                    </button>

                </div>

            `);


        popup.querySelector(
            '#fechar'
        ).onclick =
            () => popup.remove();


        popup.querySelector(
            '#cancelar'
        ).onclick =
            () => popup.remove();


        popup.querySelector(
            '#filtrar'
        ).onclick =
            () => {

                filtros = {

                    esporte:
                        popup.querySelector(
                            '#filtroEsporte'
                        ).value,

                    genero:
                        popup.querySelector(
                            '#filtroGenero'
                        ).value,

                    turma:
                        popup.querySelector(
                            '#filtroTurma'
                        ).value

                };


                atualizarFiltro();


                popup.remove();


                calendar.refetchEvents();

            };

    }


    // =====================================================
    // LIMPAR FILTROS
    // =====================================================

    function limparFiltros() {

        filtros = {
            esporte: '',
            genero: '',
            turma: ''
        };


        atualizarFiltro();


        calendar.refetchEvents();

    }


    // =====================================================
    // INDICADOR DO FILTRO
    // =====================================================

    function atualizarFiltro() {

        const ativos = [];


        if (filtros.esporte) {

            ativos.push(
                `Modalidade: ${filtros.esporte}`
            );

        }


        if (filtros.genero) {

            ativos.push(
                `Gênero: ${filtros.genero}`
            );

        }


        if (filtros.turma) {

            ativos.push(
                `Turma: ${filtros.turma}`
            );

        }


        if (!ativos.length) {

            if (filtrosAtivos) {

                filtrosAtivos.style.display =
                    'none';

                filtrosAtivos.textContent =
                    '';

            }


            if (btnLimpar) {

                btnLimpar.style.display =
                    'none';

            }


            return;

        }


        if (filtrosAtivos) {

            filtrosAtivos.textContent =
                `Filtros ativos — ${ativos.join(' | ')}`;

            filtrosAtivos.style.display =
                'block';

        }


        if (btnLimpar) {

            btnLimpar.style.display =
                'inline-block';

        }

    }


    // =====================================================
    // BUSCAR FILTROS
    // =====================================================

    async function buscarFiltros() {

        try {

            const resposta =
                await fetch(
                    '/calendario/filtros'
                );


            if (!resposta.ok) {

                throw new Error(
                    `HTTP ${resposta.status}`
                );

            }


            return await resposta.json();

        } catch (erro) {

            console.error(
                'Erro ao buscar filtros:',
                erro
            );


            alert(
                'Não foi possível carregar os filtros.'
            );


            return null;

        }

    }


    // =====================================================
    // SELECT
    // =====================================================

    function selectHTML(
        id,
        label,
        valores,
        primeiro,
        selecionado = ''
    ) {

        return `

            <div class="campo-formulario">

                <label>
                    ${esc(label)}
                </label>


                <select
                    id="${esc(id)}"
                >

                    <option value="">
                        ${esc(primeiro)}
                    </option>


                    ${valores
                        .map(
                            valor => `

                                <option
                                    value="${esc(valor)}"
                                    ${
                                        valor ===
                                        selecionado
                                            ? 'selected'
                                            : ''
                                    }
                                >

                                    ${esc(valor)}

                                </option>

                            `
                        )
                        .join('')}

                </select>

            </div>

        `;

    }


    // =====================================================
    // CRIAR POPUP
    // =====================================================

    function criarPopup(
        conteudo
    ) {

        const popup =
            document.createElement(
                'div'
            );


        popup.className =
            'popup-overlay';


        popup.innerHTML = `

            <div class="popup-calendario">

                ${conteudo}

            </div>

        `;


        document.body.appendChild(
            popup
        );


        popup.addEventListener(
            'click',
            evento => {

                if (
                    evento.target === popup
                ) {

                    popup.remove();

                }

            }
        );


        return popup;

    }


    // =====================================================
    // FORMATAR DATA
    // =====================================================

    function formatarData(
        data
    ) {

        const ano =
            data.getFullYear();


        const mes =
            String(
                data.getMonth() + 1
            ).padStart(
                2,
                '0'
            );


        const dia =
            String(
                data.getDate()
            ).padStart(
                2,
                '0'
            );


        return `${ano}-${mes}-${dia}`;

    }


    // =====================================================
    // DATA BR
    // =====================================================

    function formatarDataBR(
        data
    ) {

        return new Date(
            `${data}T00:00:00`
        ).toLocaleDateString(
            'pt-BR'
        );

    }


    // =====================================================
    // ESCAPAR HTML
    // =====================================================

    function esc(
        valor
    ) {

        return String(
            valor ?? ''
        )
            .replace(
                /&/g,
                '&amp;'
            )
            .replace(
                /</g,
                '&lt;'
            )
            .replace(
                />/g,
                '&gt;'
            )
            .replace(
                /"/g,
                '&quot;'
            )
            .replace(
                /'/g,
                '&#039;'
            );

    }

});