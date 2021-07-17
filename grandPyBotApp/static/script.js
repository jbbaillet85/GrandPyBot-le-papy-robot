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
                alert(jqxhr.responseText)
            });
        event.preventDefault();
    });
});