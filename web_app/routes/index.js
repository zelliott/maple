var crypto = require('crypto');

module.exports = function(app) {

  app.get('/', function (req, res) {
    res.render('index', {
      passkey: crypto.randomBytes(16).toString('hex')
    });
  });

};