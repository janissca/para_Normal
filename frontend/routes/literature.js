const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('literature', { title: 'Литература' })
});

module.exports = app;
