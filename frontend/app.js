const express = require('express');
const path = require('path');

const ExpressError = require('./utils/ExpressError');


const index = require('./routes/index');
const myevents = require('./routes/myevents');
const account = require('./routes/account');



const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static('public'))

const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const methodOverride = require('method-override');
app.use(methodOverride('_method'));
app.use(express.static(path.join(__dirname, 'public')))


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
const config = require('./config');
app.use(flash());


app.use('/myevents', myevents);
app.use('/account', account);
app.use('/', index);

app.listen(config.server.port, function () {  
  console.log(`Server running at port ${config.server.port}: ${config.server.host}`)
});
