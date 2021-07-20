$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
                data: {
                    userQuestion: $('#userQuestion').val(),
                },
                type: 'GET',
                url: '/data'
            })
            .done(function (data) {
                dialogue = $("<section></section>");
                dialogue.addClass("col-12 dialogue");
                dialogue.html(data);
                dialogue.appendTo("#all-responses");
            })
            .fail(function () {
                dialogue = $("<section></section>");
                dialogue.addClass("col-12 dialogue");
                dialogue.html("Je n'ais pas compris ce que tu as dis, je dois etre fatigué.\nPeux tu reformuler?");
                dialogue.appendTo("#all-reponses");
            });
    });
});