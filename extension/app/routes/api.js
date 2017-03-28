var express = require('express');
var router = express.Router();
var model = require('../lang_model/model.json');

function analyze(abstract) {
  var unseen = 0;
  var words = abstract.split('');

  for (var i = 0; i < words.length; i++) {
    var word = words[i].toLowerCase();

    if (!model[word]) unseen++;
  }

  return unseen;
}

/* POST analyze */
router.post('/analyze', function(req, res, next) {
  var abstractText = req.body.abstractText;
  var score = analyze(abstractText);

  res.json({
    score: score
  });
});

module.exports = router;
