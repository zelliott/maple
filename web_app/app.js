var express = require('express');
var session = require('express-session')
var bodyParser = require('body-parser');
var logger = require('morgan');
var path = require('path');

var indexRoute = require('./routes/index');
var testRoute = require('./routes/test');
var apiRoute = require('./routes/api');
var errorRoute = require('./routes/error');

var db = require('./server/db');

var port = process.env.PORT || 8081;

// Define routes
var app = express();

// Add session
app.use(session({
  secret: 'maple-secret'
}));

// Views
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// Public
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(__dirname + '/public'));

// Setup routes
indexRoute(app);
testRoute(app);
apiRoute(app);
errorRoute(app);

app.listen(port, function () {
  console.log('App listening on port ' + port);
});