const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('index', { title: 'Каскад - сервис для предоставления информации об оказании помощи' })
});


module.exports = app;
