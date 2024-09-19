const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('treatment', { title: 'Лечение' })
});

module.exports = app;
