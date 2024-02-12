$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (res) {
    $('DIV#hello').text(res.hello);
  });
});
