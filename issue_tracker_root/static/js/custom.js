// signup.html
$('input#id_username').addClass('form-control')
$('input#id_email').addClass('form-control')
$('input#id_password1').addClass('form-control')
$('input#id_password2').addClass('form-control')

// alerts
setTimeout(function() {
    $('#message').fadeOut('slow');
    $('#error').fadeOut('slow');
}, 3000);