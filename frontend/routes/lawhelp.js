const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('lawhelp', { title: 'Правовая помощь' })
});

module.exports = app;
