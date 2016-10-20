var TestService = require('./../services/test');

module.exports = function(app) {

  app.get('/test', function (req, res) {
    res.render('test');
  });

  app.post('/test/start', function (req, res) {
    TestService.start(req.body.passkey, function (err, body) {
      res.redirect('/test');
    });
  })

};