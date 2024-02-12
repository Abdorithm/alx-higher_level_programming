$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (res) {
  const films = res.results;
  films.forEach(film => {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  });
});
