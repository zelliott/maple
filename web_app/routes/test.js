var TestService = require('./../services/test');

module.exports = function(app) {

  app.get('/test', function (req, res) {
    TestService.get(req.session.passkey, function (err, body) {

      if (err) {
        res.redirect('/error');
      }

      res.render('test', {
        passkey: body.passkey,
        questions: body.questions,
        current: Number(body.current)
      });
    });
  });

  app.post('/test/start', function (req, res) {
    TestService.start(req.body.passkey, function (err, body) {

      if (err) {
        res.redirect('/error');
        return;
      }

      req.session.passkey = body.passkey;

      res.redirect('/test');
    });
  });

  app.post('/test/continue', function (req, res) {
    req.session.passkey = req.body.passkey;
    res.redirect('/test');
  });

  app.post('/test/save', function (req, res) {

    var answers = req.body['answers[]'].map(function (ans) {
        return (ans.length === 0) ? null : ans;
    });

    TestService.save({
      passkey: req.session.passkey,
      current: req.body.current,
      next: req.body.next,
      answers: answers
    }, function (err, body) {
      if (err) {
        res.redirect('/error');
      }

      res.send(body);
    })
  });

};