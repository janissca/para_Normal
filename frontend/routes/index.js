const express = require('express');
const app = express();

var obj;

fetch('https://jsonplaceholder.typicode.com/posts/')
	.then(res => res.json())
	.then(data => {
		obj = data;
	})
	.then(() => {
		console.log(obj);
	});

app.get('/', function (req, res) {

	res.render('index', { title: 'Крона - Мероприятия', data: obj })
});


module.exports = app;
