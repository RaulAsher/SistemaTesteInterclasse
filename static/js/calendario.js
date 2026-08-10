document.addEventListener('DOMContentLoaded', function () {

    const calendarEl = document.getElementById('calendar');

    // Controle para detectar duplo clique
    let ultimoClique = 0;
    let ultimoDia = null;

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
        events: "/calendario/eventos",

        // Clique no dia
        dateClick: function(info) {

            const agora = Date.now();

            // Verifica se foi no mesmo dia e dentro de 300ms
            if (
                ultimoDia === info.dateStr &&
                agora - ultimoClique < 300
            ) {

                abrirPopupDia(info.dateStr);

                // Reseta o controle
                ultimoClique = 0;
                ultimoDia = null;

                return;
            }

            // Primeiro clique
            ultimoClique = agora;
            ultimoDia = info.dateStr;

            // Abre o popup no primeiro clique
            abrirPopupDia(info.dateStr);
        }

    });

    calendar.render();


    // =====================================================
    // POPUP DO DIA
    // =====================================================

    function abrirPopupDia(data) {

        // Pega todos os eventos carregados no calendário
        const eventos = calendar.getEvents();

        // Filtra somente os eventos daquele dia
        const eventosDoDia = eventos.filter(function(evento) {

            if (!evento.start) {
                return false;
            }

            const ano = evento.start.getFullYear();
            const mes = String(evento.start.getMonth() + 1).padStart(2, '0');
            const dia = String(evento.start.getDate()).padStart(2, '0');

            const dataEvento = `${ano}-${mes}-${dia}`;

            console.log(
                "Evento:",
                evento.title,
                "| Data:",
                dataEvento,
                "| Procurando:",
                data
            );

            return dataEvento === data;
        });


        // Formata a data para português
        const dataFormatada = new Date(data + 'T00:00:00')
            .toLocaleDateString('pt-BR', {
                weekday: 'long',
                day: '2-digit',
                month: 'long',
                year: 'numeric'
            });


        // Cria o conteúdo dos jogos
        let jogosHTML = '';


        if (eventosDoDia.length === 0) {

            jogosHTML = `
                <div class="sem-jogos">
                    <p>Não há jogos cadastrados neste dia.</p>
                </div>
            `;

        } else {

            eventosDoDia.forEach(function(evento) {

                const horaInicio = evento.start
                    ? evento.start.toLocaleTimeString('pt-BR', {
                        hour: '2-digit',
                        minute: '2-digit'
                    })
                    : '';

                const horaFim = evento.end
                    ? evento.end.toLocaleTimeString('pt-BR', {
                        hour: '2-digit',
                        minute: '2-digit'
                    })
                    : '';

                const cor = evento.backgroundColor || '#3788d8';


                jogosHTML += `
                    <div class="jogo-popup"
                         style="border-left: 6px solid ${cor};">

                        <div class="jogo-cor"
                             style="background-color: ${cor};">
                        </div>

                        <div class="jogo-info">

                            <strong>
                                ${evento.title}
                            </strong>

                            <span>
                                ${horaInicio} - ${horaFim}
                            </span>

                        </div>

                    </div>
                `;
            });
        }


        // Verifica se o usuário é administrador
        const podeEditar = window.usuarioEhAdministrador === true;


        // Botão de editar somente para ADMIN
        let botaoEditar = '';

        if (podeEditar && eventosDoDia.length > 0) {

            botaoEditar = `
                <button
                    type="button"
                    class="btn-editar-dia"
                    id="btnEditarDia">
                    Editar
                </button>
            `;
        }


        // Cria o popup
        const popup = document.createElement('div');

        popup.className = 'popup-overlay';

        popup.innerHTML = `
            <div class="popup-calendario">

                <button
                    type="button"
                    class="fechar-popup"
                    id="fecharPopup">
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
                    ${botaoEditar}
                </div>

            </div>
        `;


        document.body.appendChild(popup);


        // Fechar popup
        document
            .getElementById('fecharPopup')
            .addEventListener('click', function () {

                popup.remove();

            });


        // Fechar clicando fora
        popup.addEventListener('click', function (e) {

            if (e.target === popup) {
                popup.remove();
            }

        });


        // Botão editar
        const btnEditar = document.getElementById('btnEditarDia');

        if (btnEditar) {

            btnEditar.addEventListener('click', function () {

                abrirEdicaoDia(data, eventosDoDia);

            });

        }

    }


    // =====================================================
    // EDIÇÃO
    // =====================================================

    function abrirEdicaoDia(data, eventos) {

        let jogosHTML = '';


        eventos.forEach(function(evento, index) {

            const horaInicio = evento.start
                ? evento.start.toLocaleTimeString('pt-BR', {
                    hour: '2-digit',
                    minute: '2-digit'
                })
                : '';

            const horaFim = evento.end
                ? evento.end.toLocaleTimeString('pt-BR', {
                    hour: '2-digit',
                    minute: '2-digit'
                })
                : '';


            jogosHTML += `
                <div class="edicao-jogo">

                    <h3>
                        ${evento.title}
                    </h3>

                    <label>
                        Data:
                    </label>

                    <input
                        type="date"
                        value="${data}"
                        class="campo-data"
                        data-evento="${evento.id}"
                    >

                    <label>
                        Hora de início:
                    </label>

                    <input
                        type="time"
                        value="${horaInicio}"
                        class="campo-inicio"
                        data-evento="${evento.id}"
                    >

                    <label>
                        Hora de fim:
                    </label>

                    <input
                        type="time"
                        value="${horaFim}"
                        class="campo-fim"
                        data-evento="${evento.id}"
                    >

                    <hr>

                </div>
            `;
        });


        const popup = document.createElement('div');

        popup.className = 'popup-overlay';

        popup.innerHTML = `
            <div class="popup-calendario popup-edicao">

                <button
                    type="button"
                    class="fechar-popup"
                    id="fecharEdicao">
                    ×
                </button>

                <h2>
                    Editar jogos
                </h2>

                <div>
                    ${jogosHTML}
                </div>

                <div class="popup-botoes">

                    <button
                        type="button"
                        class="btn-cancelar"
                        id="cancelarEdicao">
                        Cancelar
                    </button>

                    <button
                        type="button"
                        class="btn-salvar"
                        id="salvarEdicao">
                        Salvar alterações
                    </button>

                </div>

            </div>
        `;


        document.body.appendChild(popup);


        document
            .getElementById('fecharEdicao')
            .addEventListener('click', function () {

                popup.remove();

            });


        document
            .getElementById('cancelarEdicao')
            .addEventListener('click', function () {

                popup.remove();

            });


        document
            .getElementById('salvarEdicao')
            .addEventListener('click', function () {

                alert(
                    'A tela de edição está pronta. Agora vamos ligar o botão ao banco de dados.'
                );

            });

    }

});