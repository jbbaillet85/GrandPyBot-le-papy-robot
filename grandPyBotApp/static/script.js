$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
                data: {
                    userQuestion: $('#userQuestion').val(),
                },
                type: 'GET',
                url: '/data'
            })
            .done(function (data) {
                $('#data').text(data.output).show();
                dialogue = $('.dialogue').clone();
                dialogue.find('.dialogue').html(data);
                dialogue.appendTo('.dialogue');
            })
            .fail(function (jqxhr) {
                console.log(jqxhr.responseText)
                dialogue = $('.dialogue').clone();
                dialogue.find('.dialogue').html("Je n'ais pas compris ce que tu as dit, je dois etre fatigué");
                dialogue.appendTo('.dialogue');
            });
        event.preventDefault();
    });
});