var TestService = require('./../services/test');

module.exports = function (app) {

  app.get('/api/test', function (req, res) {
    TestService.get(req.session.passkey, function (err, body) {

      if (err) {
        res.redirect('/error');
      }

      res.send(body);
    });
  });

}