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

async function fetchLocations() {
	const response = await fetch('https://app.bits-company.ru/kronaclub/api/v1/locations', {
		method: "GET"
	});
	const locations = await response.json();
	return locations;
}

async function fetchThemes() {
	const response = await fetch('https://app.bits-company.ru/kronaclub/api/v1/types_of_events', {
		method: "GET"
	});
	const themes = await response.json();
	return themes;
}

async function fetchMoviesAndCategories() {
	const [moviesResponse, categoriesResponse] = await Promise.all([
		fetch('https://app.bits-company.ru/kronaclub/api/v1/locations'),
		fetch('https://app.bits-company.ru/kronaclub/api/v1/types_of_events')
	]);

	const movies = await moviesResponse.json();
	const categories = await categoriesResponse.json();

	return [movies, categories];
}



app.get('/new', (req, res) => {
	let locations;
	// fetchLocations().then(data => {
	// 	locations = data;
	// })
	let themes;

	// fetchLocations().then(data => {
	// 	themes = data;
	// })
	fetchMoviesAndCategories().then(([movies, categories]) => {
		locations = movies;     // fetched movies
		themes = categories; // fetched categories
	})
		.then(() => {
			console.log("locations", locations)
			console.log("themes", themes)
			res.render('newEvent', { title: 'Создать мероприятие', locations: locations, themes: themes, helpers: helpers })
		})
		.catch(error => {
			// /movies or /categories request failed
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
