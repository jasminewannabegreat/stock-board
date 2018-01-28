var express = require('express');
var path = require('path');

var index = require('./routes/index');

var app = express();
var stocks = require('./routes/stocks');
// view engine setup
app.set('views', path.join(__dirname, '../client/build'));
app.set('view engine', 'jade');

//TO DO: remove this after development is done
app.use('*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});


app.use('/static',express.static(path.join(__dirname, '../client/build/static/')));

app.use('/', index);
app.use('/stocks',stocks);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  res.send('404 Not Found');
});

module.exports = app;
