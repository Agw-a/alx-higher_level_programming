$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
	$('UL#list_movies').text(data.title);
});
