document.addEventListener('DOMContentLoaded', function () {

    const calendarEl = document.getElementById('calendar');


    // =====================================================
    // CALENDÁRIO
    // =====================================================

    const calendar = new FullCalendar.Calendar(calendarEl, {

        // Idioma
        locale: 'pt-br',

        // Mês inicial
        initialView: 'dayGridMonth',

        // Segunda-feira primeiro
        firstDay: 1,

        // Cabeçalho
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },

        // Texto dos botões
        buttonText: {
            today: 'Hoje',
            month: 'Mês',
            week: 'Semana',
            day: 'Dia'
        },

        // Eventos
        events: '/calendario/eventos',

        // Clique no dia
        dateClick: function (info) {
            abrirPopupDia(info.dateStr);
        }

    });


    calendar.render();


    // =====================================================
    // POPUP DO DIA
    // =====================================================

    function abrirPopupDia(data) {

        const eventosDoDia = calendar.getEvents().filter(function (evento) {

            if (!evento.start) {
                return false;
            }

            return formatarData(evento.start) === data;

        });


        const dataFormatada =
            new Date(data + 'T00:00:00')
                .toLocaleDateString('pt-BR', {
                    weekday: 'long',
                    day: '2-digit',
                    month: 'long',
                    year: 'numeric'
                });


        let jogosHTML = '';


        if (eventosDoDia.length === 0) {

            jogosHTML = `
                <div class="sem-jogos">
                    Não há jogos cadastrados neste dia.
                </div>
            `;

        } else {

            eventosDoDia.forEach(function (evento) {

                const inicio = evento.start
                    ? evento.start.toLocaleTimeString('pt-BR', {
                        hour: '2-digit',
                        minute: '2-digit'
                    })
                    : '';

                const fim = evento.end
                    ? evento.end.toLocaleTimeString('pt-BR', {
                        hour: '2-digit',
                        minute: '2-digit'
                    })
                    : '';


                jogosHTML += `
                    <div
                        class="jogo-popup"
                        style="border-left-color:
                        ${evento.backgroundColor || '#3788d8'}">

                        <strong>
                            ${evento.title}
                        </strong>

                        <div class="jogo-detalhes">
                            ${evento.extendedProps.esporte}
                            -
                            ${evento.extendedProps.genero}
                            -
                            ${evento.extendedProps.etapa}
                        </div>

                        <span>
                            ${inicio} - ${fim}
                        </span>

                    </div>
                `;
            });
        }


        // Só ADMIN pode alterar
        const botoes = window.usuarioPodeEditar
            ? `
                <button
                    type="button"
                    class="btn-adicionar"
                    id="btnAdicionar">
                    + Adicionar partida
                </button>

                ${eventosDoDia.length > 0 ? `
                    <button
                        type="button"
                        class="btn-editar"
                        id="btnEditar">
                        Editar
                    </button>
                ` : ''}
            `
            : '';


        const popup = criarPopup(`

            <button
                type="button"
                class="fechar-popup"
                id="fechar">
                ×
            </button>

            <h2>
                Jogos do dia
            </h2>

            <p class="data-popup">
                ${dataFormatada}
            </p>

            <div class="lista-jogos-popup">
                ${jogosHTML}
            </div>

            <div class="popup-botoes">
                ${botoes}
            </div>

        `);


        popup.querySelector('#fechar').onclick =
            () => popup.remove();


        if (window.usuarioPodeEditar) {

            popup.querySelector('#btnAdicionar')
                ?.addEventListener('click', function () {

                    popup.remove();

                    abrirAdicionar(data);

                });


            popup.querySelector('#btnEditar')
                ?.addEventListener('click', function () {

                    popup.remove();

                    abrirEdicao(data, eventosDoDia);

                });

        }
    }


    // =====================================================
    // ADICIONAR PARTIDA
    // =====================================================

    async function abrirAdicionar(data) {

        const resposta =
            await fetch('/calendario/filtros');

        const filtros =
            await resposta.json();


        const popup = criarPopup(`

            <button
                type="button"
                class="fechar-popup"
                id="fechar">
                ×
            </button>

            <h2>
                Adicionar partida
            </h2>

            <p class="data-popup">
                ${formatarDataBR(data)}
            </p>


            <!-- Modalidade -->

            <div class="campo-formulario">

                <label>
                    Modalidade
                </label>

                <select id="esporte">

                    <option value="">
                        Selecione
                    </option>

                    ${filtros.esportes.map(function (esporte) {

                        return `
                            <option value="${esporte}">
                                ${esporte}
                            </option>
                        `;

                    }).join('')}

                </select>

            </div>


            <!-- Gênero -->

            <div class="campo-formulario">

                <label>
                    Gênero
                </label>

                <select id="genero">

                    <option value="">
                        Selecione
                    </option>

                    ${filtros.generos.map(function (genero) {

                        return `
                            <option value="${genero}">
                                ${genero}
                            </option>
                        `;

                    }).join('')}

                </select>

            </div>


            <!-- Rodada -->

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


            <!-- Partidas -->

            <div class="campo-formulario">

                <label>
                    Partida
                </label>

                <div
                    id="partidas"
                    class="lista-partidas">

                    Selecione modalidade, gênero e rodada.

                </div>

            </div>


            <!-- Horários -->

            <div class="linha-horarios">

                <div class="campo-formulario">

                    <label>
                        Início
                    </label>

                    <input
                        type="time"
                        id="inicio">

                </div>


                <div class="campo-formulario">

                    <label>
                        Fim
                    </label>

                    <input
                        type="time"
                        id="fim">

                </div>

            </div>


            <div
                id="mensagem"
                class="mensagem-formulario">
            </div>


            <div class="popup-botoes">

                <button
                    type="button"
                    class="btn-cancelar"
                    id="cancelar">

                    Cancelar

                </button>


                <button
                    type="button"
                    class="btn-salvar"
                    id="salvar">

                    Adicionar

                </button>

            </div>

        `);


        popup.querySelector('#fechar').onclick =
            () => popup.remove();


        popup.querySelector('#cancelar').onclick =
            () => {

                popup.remove();

                abrirPopupDia(data);

            };


        // =================================================
        // BUSCAR PARTIDAS
        // =================================================

        async function buscarPartidas() {

            const esporte =
                popup.querySelector('#esporte').value;

            const genero =
                popup.querySelector('#genero').value;

            const etapa =
                popup.querySelector('#etapa').value;

            const lista =
                popup.querySelector('#partidas');


            if (!esporte || !genero || !etapa) {

                lista.innerHTML =
                    'Selecione modalidade, gênero e rodada.';

                return;

            }


            lista.innerHTML =
                'Buscando partidas...';


            const url =
                `/calendario/partidas?` +
                `esporte=${encodeURIComponent(esporte)}` +
                `&genero=${encodeURIComponent(genero)}` +
                `&etapa=${etapa}`;


            const resposta =
                await fetch(url);


            const partidas =
                await resposta.json();


            if (!partidas.length) {

                lista.innerHTML =
                    'Nenhuma partida disponível.';

                return;

            }


            lista.innerHTML =
                partidas.map(function (partida) {

                    return `
                        <label class="partida-opcao">

                            <input
                                type="radio"
                                name="partida"
                                value="${partida.pk_partida}">

                            <span>
                                ${partida.equipe_casa}
                                ×
                                ${partida.equipe_visitante}
                            </span>

                        </label>
                    `;

                }).join('');

        }


        popup.querySelector('#esporte')
            .addEventListener(
                'change',
                buscarPartidas
            );


        popup.querySelector('#genero')
            .addEventListener(
                'change',
                buscarPartidas
            );


        popup.querySelector('#etapa')
            .addEventListener(
                'change',
                buscarPartidas
            );


        // =================================================
        // SALVAR
        // =================================================

        popup.querySelector('#salvar')
            .addEventListener('click', async function () {

                const partida =
                    popup.querySelector(
                        'input[name="partida"]:checked'
                    );


                const inicio =
                    popup.querySelector('#inicio').value;

                const fim =
                    popup.querySelector('#fim').value;


                const mensagem =
                    popup.querySelector('#mensagem');


                if (!partida || !inicio || !fim) {

                    mensagem.textContent =
                        'Preencha todos os campos.';

                    return;

                }


                if (fim <= inicio) {

                    mensagem.textContent =
                        'O horário final deve ser maior que o inicial.';

                    return;

                }


                const resposta =
                    await fetch(
                        '/calendario/adicionar',
                        {
                            method: 'POST',

                            headers: {
                                'Content-Type':
                                    'application/json'
                            },

                            body: JSON.stringify({

                                data: data,

                                fk_partida:
                                    partida.value,

                                hora_inicio:
                                    inicio,

                                hora_fim:
                                    fim

                            })

                        }
                    );


                const resultado =
                    await resposta.json();


                if (!resposta.ok) {

                    mensagem.textContent =
                        resultado.mensagem;

                    return;

                }


                popup.remove();

                calendar.refetchEvents();

                setTimeout(function () {

                    abrirPopupDia(data);

                }, 300);

            });

    }


    // =====================================================
    // EDITAR
    // =====================================================

    function abrirEdicao(data, eventos) {

        let jogosHTML = '';


        eventos.forEach(function (evento) {

            const inicio =
                evento.start.toLocaleTimeString(
                    'pt-BR',
                    {
                        hour: '2-digit',
                        minute: '2-digit'
                    }
                );


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


            jogosHTML += `

                <div
                    class="edicao-jogo"
                    data-id="${evento.id}">

                    <h3>
                        ${evento.title}
                    </h3>


                    <div class="linha-horarios">

                        <div class="campo-formulario">

                            <label>
                                Início
                            </label>

                            <input
                                type="time"
                                class="campo-inicio"
                                value="${inicio}">

                        </div>


                        <div class="campo-formulario">

                            <label>
                                Fim
                            </label>

                            <input
                                type="time"
                                class="campo-fim"
                                value="${fim}">

                        </div>

                    </div>


                    <button
                        type="button"
                        class="btn-remover btn-remover-jogo">

                        Remover do calendário

                    </button>

                </div>

            `;

        });


        const popup = criarPopup(`

            <button
                type="button"
                class="fechar-popup"
                id="fechar">
                ×
            </button>


            <h2>
                Editar jogos
            </h2>


            <p class="data-popup">
                ${formatarDataBR(data)}
            </p>


            ${jogosHTML}


            <div
                id="mensagem"
                class="mensagem-formulario">
            </div>


            <div class="popup-botoes">

                <button
                    type="button"
                    class="btn-cancelar"
                    id="cancelar">

                    Cancelar

                </button>


                <button
                    type="button"
                    class="btn-salvar"
                    id="salvar">

                    Salvar alterações

                </button>

            </div>

        `);


        popup.querySelector('#fechar').onclick =
            () => popup.remove();


        popup.querySelector('#cancelar').onclick =
            () => {

                popup.remove();

                abrirPopupDia(data);

            };


        // =================================================
        // REMOVER JOGO
        // =================================================

        popup.querySelectorAll('.btn-remover-jogo')
            .forEach(function (botao) {

                botao.addEventListener(
                    'click',
                    async function () {

                        const jogo =
                            botao.closest('.edicao-jogo');


                        const id =
                            jogo.dataset.id;


                        const resposta =
                            await fetch(
                                '/calendario/remover',
                                {
                                    method: 'POST',

                                    headers: {
                                        'Content-Type':
                                            'application/json'
                                    },

                                    body: JSON.stringify({
                                        id: id
                                    })

                                }
                            );


                        const resultado =
                            await resposta.json();


                        if (!resposta.ok) {

                            popup.querySelector(
                                '#mensagem'
                            ).textContent =
                                resultado.mensagem;

                            return;

                        }


                        jogo.remove();

                        calendar.refetchEvents();

                    }
                );

            });


        // =================================================
        // SALVAR HORÁRIOS
        // =================================================

        popup.querySelector('#salvar')
            .addEventListener('click', async function () {

                const jogos =
                    popup.querySelectorAll('.edicao-jogo');


                for (const jogo of jogos) {

                    const inicio =
                        jogo.querySelector(
                            '.campo-inicio'
                        ).value;


                    const fim =
                        jogo.querySelector(
                            '.campo-fim'
                        ).value;


                    if (!inicio || !fim || fim <= inicio) {

                        popup.querySelector(
                            '#mensagem'
                        ).textContent =
                            'Verifique os horários.';

                        return;

                    }


                    await fetch(
                        '/calendario/editar',
                        {
                            method: 'POST',

                            headers: {
                                'Content-Type':
                                    'application/json'
                            },

                            body: JSON.stringify({

                                id:
                                    jogo.dataset.id,

                                hora_inicio:
                                    inicio,

                                hora_fim:
                                    fim

                            })

                        }
                    );

                }


                popup.remove();

                calendar.refetchEvents();

                setTimeout(function () {

                    abrirPopupDia(data);

                }, 300);

            });

    }


    // =====================================================
    // FUNÇÕES AUXILIARES
    // =====================================================

    function criarPopup(conteudo) {

        const popup =
            document.createElement('div');

        popup.className =
            'popup-overlay';


        popup.innerHTML = `
            <div class="popup-calendario">
                ${conteudo}
            </div>
        `;


        document.body.appendChild(popup);


        popup.addEventListener(
            'click',
            function (evento) {

                if (evento.target === popup) {
                    popup.remove();
                }

            }
        );


        return popup;

    }


    function formatarData(data) {

        const ano =
            data.getFullYear();

        const mes =
            String(
                data.getMonth() + 1
            ).padStart(2, '0');

        const dia =
            String(
                data.getDate()
            ).padStart(2, '0');


        return `${ano}-${mes}-${dia}`;

    }


    function formatarDataBR(data) {

        return new Date(
            data + 'T00:00:00'
        ).toLocaleDateString(
            'pt-BR'
        );

    }

});