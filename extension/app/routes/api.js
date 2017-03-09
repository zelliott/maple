var express = require('express');
var router = express.Router();

/* POST analyze */
router.post('/analyze', function(req, res, next) {
  var abstractText = req.body.abstractText;
  var score = Math.floor(Math.random() * 100);

  res.json({
    score: score
  });
});

module.exports = router;
