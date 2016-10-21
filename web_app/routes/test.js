var TestService = require('./../services/test');

module.exports = function(app) {

  app.get('/test', function (req, res) {
    TestService.get(req.session.passkey, function (err, body) {
      res.render('test', {
        passkey: body.passkey,
        test: body.test,
        current: body.current
      });
    });
  });

  app.post('/test/start', function (req, res) {
    TestService.start(req.body.passkey, function (err, body) {

      // Set any req.session.

      req.session.passkey = body.passkey;

      res.redirect('/test');
    });
  })

};