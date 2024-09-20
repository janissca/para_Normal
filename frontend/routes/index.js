const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('index', { title: 'Крона - Мероприятия' })
});


module.exports = app;
