module.exports = function(app) {

  app.get('/error', function (req, res) {
    res.render('error', {
      message: 'The application administrator has been notified.  Please close this window and try again.'
    });
  });

};