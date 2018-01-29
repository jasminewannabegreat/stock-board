var bodyParser = require('body-parser');
var config = require('./config/config.json');
var express = require('express');
var cors = require('cors');
var path = require('path');
var passport = require('passport');

//routes
var auth = require('./routes/auth');
var index = require('./routes/index');
var stocks = require('./routes/stocks');
// view engine setup

var app = express();
require('./models/main.js').connect(config.mongoDbUri);

app.set('views', path.join(__dirname, '../client/build'));
app.set('view engine', 'jade');
app.use('/static',express.static(path.join(__dirname, '../client/build/static/')));

//TO DO: remove this after development is done
app.use(cors());

app.use(bodyParser.json());

// Load passport strategies
app.use(passport.initialize());
var localSignupStrategy = require('./passport/signup_passport');
var localLoginStrategy = require('./passport/login_passport');
passport.use('local-signup', localSignupStrategy);
passport.use('local-login', localLoginStrategy);

app.use('/', index);
app.use('/auth', auth);
const authCheckMiddleware = require('./middleware/auth_checker');
app.use('/stocks', authCheckMiddleware);
app.use('/stocks', stocks);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  res.send('404 Not Found');
});

module.exports = app;
