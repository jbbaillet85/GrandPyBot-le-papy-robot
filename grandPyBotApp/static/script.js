$(document).ready(function () {
    $(document).ajaxStart(function(){
        $("#wait").css("display", "block");
      });
      $(document).ajaxComplete(function(){
        $("#wait").css("display", "none");
      });
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
            });
    });
});