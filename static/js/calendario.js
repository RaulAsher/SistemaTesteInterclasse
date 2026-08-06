document.addEventListener('DOMContentLoaded', function () {

    const calendarEl = document.getElementById('calendar');

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

        // EVENTOS DO CALENDÁRIO
        events: "/calendario/eventos"
    });

    calendar.render();

});