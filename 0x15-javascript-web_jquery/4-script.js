$('DIV#toggle_header').on('click', function (e) {
if ($('header').hasClass('green')) {
	$('header').removeClass('green').addClass('red');
} else {
	$('header').removeClass('red').addClass('green');
}
});
