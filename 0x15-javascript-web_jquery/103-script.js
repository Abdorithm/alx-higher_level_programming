$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const parm = { lang: $('INPUT#language_code').val() };
    $.get('https://hellosalut.stefanbohacek.dev/', parm, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which == 13) {
      $('INPUT#btn_translate').trigger('click');
    }
  });
});
