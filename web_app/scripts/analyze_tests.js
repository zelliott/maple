var _ = require('lodash');
var fs = require('fs');
var Snowball = require('snowball');

var stemmer = new Snowball('English');

var files = [
  {
    passkey: '8e5a6bfc88f891ea799bc6694436edb9',
    count: 62,
    name: 'Omar'
  },
  {
    passkey: 'e4b07377c07d2c3d95a737e4bf642082',
    count: 100,
    name: 'Zack'
  },
  {
    passkey: 'ffe359d641982de20dbc86eae7ccb522',
    count: 72,
    name: 'Spencer'
  },
  {
    passkey: '26ae945be740ffc1c6d7b2b88a0ec493',
    count: 100,
    name: 'Zhi'
  }
];

var compareStem = function (a, b) {

  if (_.isEmpty(b)) {
    return false;
  }

  stemmer.setCurrent(a);
  stemmer.stem();
  a = stemmer.getCurrent();

  stemmer.setCurrent(b);
  stemmer.stem();
  b = stemmer.getCurrent();

  return a === b;
};

var totalCorrect = 0;
var totalQuestions = 0;
var byTopic = {};

_.each(files, function(file) {
  var passkey = file.passkey;
  var count = file.count;
  var name = file.name;

  var questionsFilename = passkey + '.questions.json';
  var topicsFilename = passkey + '.topics.json';
  var questions = JSON.parse(fs.readFileSync(questionsFilename, 'utf8'));
  var topics = JSON.parse(fs.readFileSync(topicsFilename, 'utf8'));

  var numCorrect = 0;
  var numQuestions = 0;

  for (var i = 0; i < count; i++) {
    var question = questions[i];
    var correct = question.correct;
    var answers = question.answers;

    var removedWordsKey = correct.join('.');
    var topic = topics[removedWordsKey];

    if (!byTopic[topic]) {
      byTopic[topic] = {
        numCorrect: 0,
        numQuestions: 0
      };
    }

    for (var j = 0; j < 5; j++) {
      var cor = correct[j];
      var ans = answers[j];

      if (!cor) {
        continue;
      }

      if (compareStem(cor, ans)) {
        numCorrect++;
        byTopic[topic].numCorrect++;
      }

      numQuestions++;
      byTopic[topic].numQuestions++;
    }
  }

  totalCorrect += numCorrect;
  totalQuestions += numQuestions;

  console.log('Name: ' + name);
  console.log('Accuracy: ' + numCorrect / numQuestions);
});

var topicKeys = Object.keys(byTopic);
for (var k = 0; k < topicKeys.length; k++) {
  var topicKey = topicKeys[k];
  var numByTopic = byTopic[topicKey];

  console.log('Topic: ' + topicKey, numByTopic.numCorrect / numByTopic.numQuestions);
}

console.log('Overall accuracy: ' + totalCorrect / totalQuestions);