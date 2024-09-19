const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('adm', { title: 'Страница Администратора' })
});

module.exports = app;
