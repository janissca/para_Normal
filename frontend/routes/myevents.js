const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('myevents', { title: 'Мои мероприятия' })
});

module.exports = app;
