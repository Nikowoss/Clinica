//API
function fetchFeriados(callbackName) {
    var script = document.createElement('script');
    var callbackFunctionName = 'jsonpCallback' + Math.floor(Math.random() * 100000);

    window[callbackFunctionName] = function (data) {
        var calendarData = data.map(function (feriado) {
            return {
                title: feriado.nombre,
                start: feriado.fecha
            };
        });

        $('#calendar').fullCalendar({
            events: calendarData
        });

        delete window[callbackFunctionName];
        document.body.removeChild(script);
    };

    var apiUrl = 'https://apis.digital.gob.cl/fl/feriados/2023?callback=' + callbackFunctionName;
    script.src = apiUrl;
    document.body.appendChild(script);
}

var callbackName = 'miCallback';
fetchFeriados(callbackName);
// API LISTA
// AGREGAR EVENTOS AL CALENDARIO
$(document).ready(function() {
    var calendar = $('#calendar');
    
    $('#eventForm').submit(function(e) {
        e.preventDefault();
        
        var title = $('#title').val();
        var start = $('#start').val();
        var end = $('#end').val();
        
        if (title && start) {
            var newEvent = {
                title: title,
                start: start
            };
            
            if (end) {
                newEvent.end = end;
            }
            
            calendar.fullCalendar('renderEvent', newEvent, true);
        }
    });
});
//AGREGAR EVENTOS AL CALENDARIO

