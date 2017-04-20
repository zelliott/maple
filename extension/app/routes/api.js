var express = require('express');
var router = express.Router();
var model = require('../lang_model/model.json');
var webdict = require('webdict');
var ps = require('python-shell');
var async = require('async');

function determineReadability(abstract) {
  var unseen = 0;
  var words = abstract.split('');

  for (var i = 0; i < words.length; i++) {
    var word = words[i].toLowerCase();

    if (!model[word]) unseen++;
  }

  return unseen;
}

function simplifyWords(abstract) {
  var options = {
    mode: 'text',
    // pythonPath: '/usr/local/bin/python',
    pythonOptions: [],
    scriptPath: '/Users/Zack/Developer/maple/extension/app/simplify_service/',
    args: [ abstract ]
  };

  ps.run('get_difficult_words.py', options, function(err, results) {
    if (err) throw err;

    var words = JSON.parse(results).all;
    var promises = [];
    var wordsAndDefinitions = {};

    words.forEach(function(word) {
      promises.push(webdict('dictionary', word));
    });

    Promise.all(promises).then(function(results) {
      console.log(results.length);
      results.forEach(function(res) {
        if (res.statusCode === '200') {
          var definition = res.definitions[0];
          wordsAndDefinitions[word] = definition;
        }
      });
    });

    console.log(wordsAndDefinitions);

    return wordsAndDefinitions;
  });
}

/* POST analyze */
router.post('/analyze', function(req, res, next) {
  var abstractText = req.body.abstractText;
  var score = determineReadability(abstractText);
  var definitions = simplifyWords(abstractText);

  res.json({
    score: score,
    definitions: definitions
  });
});

router.get('/', function(req, res, next) {
  res.send('Test');
});

module.exports = router;
