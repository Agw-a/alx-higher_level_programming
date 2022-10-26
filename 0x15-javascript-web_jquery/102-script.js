$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function (event) {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/' + $('INPUT#language_code').val();
    $.getJSON(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
