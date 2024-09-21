const express = require('express');
const app = express.Router();
const catchAsync = require('../utils/catchAsync');

const helpers = require('../utils/helpers.js');



app.get('/', function (req, res) {
	let events;

	fetch('https://app.bits-company.ru/kronaclub/api/v1/events', {
		method: "GET"
	})
		.then(res => res.json())
		.then(data => {
			events = data;
		})
		.then(() => {
			res.render('index', { title: 'Крона - Мероприятия', events: events, helpers: helpers })
		})
		.catch((error) => console.error(error));

});


async function fetchInfoForNewEvent() {
	const [locationsResponse, typesResponse] = await Promise.all([
		fetch('https://app.bits-company.ru/kronaclub/api/v1/locations'),
		fetch('https://app.bits-company.ru/kronaclub/api/v1/types_of_events')
	]);

	const locations = await locationsResponse.json();
	const types = await typesResponse.json();

	return [locations, types];
}



app.get('/new', (req, res) => {
	let locations;
	let themes;

	fetchInfoForNewEvent().then(([movies, categories]) => {
		locations = movies;
		themes = categories;
	})
		.then(() => {
			console.log("locations", locations)
			console.log("themes", themes)
			res.render('newevent', { title: 'Создать мероприятие', locations: locations, themes: themes, helpers: helpers })
		})
		.catch(error => {
			console.log(error)
		});

})

app.post('/', catchAsync(async (req, res, next) => {
	const event = req.body.event;

	const myHeaders = new Headers();
	myHeaders.append("Content-Type", "application/json");

	const raw = JSON.stringify({
		name: event.name,
		description: event.description,
		event_type: "PM",
		start_date: event.start_date,
		end_date: event.end_date,
		host_id: 1,
		location_id: 1
	});
	console.log(raw);

	const requestOptions = {
		method: "POST",
		headers: myHeaders,
		body: raw,
		redirect: "follow"
	};

	fetch("https://app.bits-company.ru/kronaclub/api/v1/events/", requestOptions)
		.then((response) => response.text())
		.then((result) => console.log(result))
		.then(function (result) {
			res.redirect('/')
		})
		.catch((error) => console.error(error));


}))


module.exports = app;
