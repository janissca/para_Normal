const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('info', { title: 'Информационные ресурсы' })
});

module.exports = app;
