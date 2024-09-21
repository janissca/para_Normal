const express = require('express');
const app = express();

const helpers = require('../utils/helpers.js');

var events;

fetch('http://localhost:8000/api/v1/events')
	.then(res => res.json())
	.then(data => {
		events = data;
	})
	.then(() => {
		console.log(events);
	})
	.catch();

app.get('/', function (req, res) {

	res.render('index', { title: 'Крона - Мероприятия', events: events, helpers:helpers })
});



module.exports = app;
