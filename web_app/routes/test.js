var TestService = require('./../services/test');

module.exports = function (app) {

  app.get('/test', function (req, res) {
    TestService.get(req.session.passkey, function (err, body) {

      if (err) {
        res.redirect('/error');
      }

      res.render('test', {
        passkey: body.passkey,
        questions: body.questions,
        current: Number(body.current),
        mode: body.mode
      });
    });
  });

  app.get('/test/:passkey', function (req, res) {
    req.session.passkey = req.params.passkey;
    res.redirect('/test');
  });

  // TODO:
  // Uncomment if you want to generate tests
  // app.get('/test/generate/:n', function (req, res) {
  //   var n = req.params.n;

  //   TestService.generate(n, function (err) {
  //     res.send('Generated ' + n + ' tests');
  //   });
  // });

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

  app.post('/test/save/cloze', function (req, res) {

    var answers = req.body['answers[]'].map(function (ans) {
        return (ans.length === 0) ? null : ans;
    });

    TestService.saveCloze({
      passkey: req.session.passkey,
      current: req.body.current,
      next: req.body.next,
      timeElapsed: req.body.timeElapsed,
      answers: answers
    }, function (err, body) {
      if (err) {
        res.redirect('/error');
      }

      res.send(body);
    });
  });

  app.post('/test/save/readability', function (req, res) {

    TestService.saveReadability({
      passkey: req.session.passkey,
      current: req.body.current,
      next: req.body.next,
      difficulty: req.body.difficulty,
    }, function (err, body) {
      if (err) {
        res.redirect('/error');
      }

      res.send(body);
    });
  });

};