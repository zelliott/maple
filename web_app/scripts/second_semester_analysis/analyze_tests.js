var _ = require('lodash');
var fs = require('fs');
var Snowball = require('snowball');

var stemmer = new Snowball('English');

var compareStem = function (a, b) {

  if (_.isEmpty(b) || _.isEmpty(a)) {
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

var calculateAccuracy = function (answers, correct) {
  var count = 0;

  for (var i = 0; i < answers.length; i++) {
    var ans = answers[i];
    var cor = correct[i];

    if (compareStem(ans, cor)) {
      count++;
    }
  }

  return count / answers.length;
};

var arrayToCsv = function (data) {
  var lineArray = [];
  data.forEach(function (infoArray, index) {
      var line = infoArray.join(",");
      lineArray.push(line);
  });

  return csvContent = lineArray.join("\n");
};

var results = JSON.parse(fs.readFileSync('results.json', 'utf8'));
var topics = {};

var csvResults = [];
var csvTopics = [];

_.each(results, function (test) {
  var questions = test.questions;

  _.each(questions, function (question) {
    var answers = question.answers;
    var correct = question.correct;
    var difficulty = Number(question.difficulty);
    var timeElapsed = question.timeElapsed;
    var questionId = question.questionId;
    var topic = question.topic;

    var accuracy = calculateAccuracy(answers, correct);

    if (!topics[topic]) {
      topics[topic] = {
        accuracy: 0,
        difficulty: 0,
        accuracyCount: 0,
        difficultyCount: 0
      };
    }

    // Cleaning
    if (difficulty !== 0) {
      topics[topic].difficulty += difficulty;
      topics[topic].difficultyCount += 1;
    }

    topics[topic].accuracy += accuracy;
    topics[topic].accuracyCount += 1;

    csvResults.push([ questionId, topic, accuracy, difficulty, timeElapsed ]);
  });
});

_.each(topics, function (value, key) {
  value.accuracy /= value.accuracyCount;
  value.difficulty /= value.difficultyCount;

  var csvTopic = [ key, value.accuracy, value.difficulty, value.accuracyCount, value.difficultyCount ];

  csvTopics.push(csvTopic);
});

var csvResultsStr = arrayToCsv(csvResults);
var csvTopicsStr = arrayToCsv(csvTopics);

fs.writeFile('results.csv', csvResultsStr, function (err) {
  if (err) return console.log(err);
});

fs.writeFile('topics.csv', csvTopicsStr, function (err) {
  if (err) return console.log(err);
});
