var _ = require('lodash');
var fs = require('fs');
var Snowball = require('snowball');

var stemmer = new Snowball('English');

var compareStem = function (a, b) {

  if (_.isEmpty(b)) {
    return false;
  }

  a = a.toLowerCase();
  b = b.toLowerCase();

  stemmer.setCurrent(a);
  stemmer.stem();
  a = stemmer.getCurrent();

  stemmer.setCurrent(b);
  stemmer.stem();
  b = stemmer.getCurrent();

  return a === b;
};

var arrayToCsv = function (data) {
  var lineArray = [];
  data.forEach(function (infoArray, index) {
      var line = infoArray.join(",");
      lineArray.push(index == 0 ? "data:text/csv;charset=utf-8," + line : line);
  });

  return csvContent = lineArray.join("\n");
};

var results = JSON.parse(fs.readFileSync('results.json', 'utf8'));
var topics = {};

var csvResults = [];

_.each(results, function (test) {
  var questions = test.questions;

  _.each(questions, function (question) {
    var answers = question.answers;
    var correct = question.correct;
    var difficulty = question.difficulty;
    var timeElapsed = question.timeElapsed;
    var questionId = question.questionId;
    var topic = question.topic;

    var count = 0;

    for (var i = 0; i < answers.length; i++) {
      var ans = answers[i];
      var cor = correct[i];

      if (ans === cor) {
        count++;
      }
    }

    var accuracy = count / answers.length;

    csvResults.push([ questionId, topic, accuracy, difficulty, timeElapsed ]);
  });

  var csvString = arrayToCsv(csvResults);

  fs.writeFile('results.csv', csvString, function (err) {
    if (err) return console.log(err);
  });
});
