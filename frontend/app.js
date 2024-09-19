const express = require('express');
const path = require('path');

const index = require('./routes/index');
const prevent = require('./routes/prevent');
const treatment = require('./routes/treatment');
const lawhelp = require('./routes/lawhelp');
const literature = require('./routes/literature');
const info = require('./routes/info');
const adm = require('./routes/adm');

const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static('public'))

const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const methodOverride = require('method-override');


app.use(methodOverride(function (req, res) {
  if (req.body && typeof req.body === 'object' && '_method' in req.body) {
    const method = req.body._method
    delete req.body._method
    return method
  }
}));

const session = require('express-session');

app.use(session({
  cookie: { maxAge: 60000 },
  secret: 'woot',
  resave: false,
  saveUninitialized: false
}));

const flash = require('express-flash');
app.use(flash());


app.use('/prevent', prevent);
app.use('/treatment', treatment);
app.use('/lawhelp', lawhelp);
app.use('/literature', literature);
app.use('/info', info);
app.use('/adm', adm);
app.use('/', index);

// app.all('*', (req, res, next) => {
//   next(new ExpressError('Page not found', 404));
// })


app.listen(3000, function () {
  console.log('Server running at port 3000: http://127.0.0.1:3000')
});
