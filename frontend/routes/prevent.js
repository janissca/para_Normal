const express = require('express');
const app = express();

app.get('/', function (req, res) {
	res.render('prevent', { title: 'Профилактика заболеваний' })
});

module.exports = app;
