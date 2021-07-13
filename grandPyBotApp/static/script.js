$(document).ready(function() {
    $('form').on('submit', function(event) {
      $.ajax({
         data : {
            userQuestion : $('#userQuestion').val(),
                },
            type : 'GET',
            url : '/data'
           })
       .done(function(data) {
         $('#data').text(data.output).show();
     });
     event.preventDefault();
     });
});
