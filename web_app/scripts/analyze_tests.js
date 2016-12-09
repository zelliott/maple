var _ = require('lodash');
var fs = require('fs');
var Snowball = require('snowball');

var stemmer = new Snowball('English');

var sharedIds = JSON.parse(fs.readFileSync('shared_ids.json', 'utf8'));
var repeatedIds = JSON.parse(fs.readFileSync('repeated_ids.json', 'utf8'));

var files = [
  {
    passkey: '8e5a6bfc88f891ea799bc6694436edb9',
    count: 100,
    name: 'Omar'
  },
  {
    passkey: 'e4b07377c07d2c3d95a737e4bf642082',
    count: 100,
    name: 'Zack'
  },
  {
    passkey: 'ffe359d641982de20dbc86eae7ccb522',
    count: 100,
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

var totalCorrect = 0;
var totalQuestions = 0;
var accuracyByTopic = {};
var lengthsByTopic = {}
var numOfTopics = {}
var test = 0;
_.each(files, function(file) {
  var passkey = file.passkey;
  var name = file.name;

  var questionsFilename = passkey + '.questions.json';
  var topicsFilename = passkey + '.topics.json';
  var questions = JSON.parse(fs.readFileSync(questionsFilename, 'utf8'));
  var topics = JSON.parse(fs.readFileSync(topicsFilename, 'utf8'));

  var numCorrect = 0;
  var numQuestions = 0;

  var numSharedCorrect = 0;
  var numSharedQuestions = 0;

  var numRepeatedCorrect = 0;
  var numRepeatedQuestions = 0;

  var numCorrectPerTopic = {};
  var numQuestionsPerTopic = {};

  for (var i = 0; i < 100; i++) {
    var question = questions[i];
    var correct = question.correct;
    var answers = question.answers;
    var numWords = question.abstract.split(' ').length;
    var numChars = question.abstract.split('').length;

    var removedWordsKey = correct.join('.');
    var topic = topics[removedWordsKey];

    var isShared = sharedIds[removedWordsKey] !== undefined;
    var isRepeated = repeatedIds[passkey].indexOf(removedWordsKey) != -1;

    if (!accuracyByTopic[topic]) {
      accuracyByTopic[topic] = {
        numCorrect: 0,
        numQuestions: 0
      };
    }

    if (!lengthsByTopic[topic]) {
      lengthsByTopic[topic] = {
        words: 0,
        chars: 0
      }
    }

    lengthsByTopic[topic].words += numWords;
    lengthsByTopic[topic].chars += numChars;

    for (var j = 0; j < 5; j++) {
      var cor = correct[j];
      var ans = answers[j];

      if (!cor) {
        continue;
      }

      if (compareStem(cor, ans)) {
        numCorrect++;
        accuracyByTopic[topic].numCorrect++;

        if (isShared) {
          numSharedCorrect++;
        }

        if (isRepeated) {
          numRepeatedCorrect++;
        }

        if (!numCorrectPerTopic[topic]) {
          numCorrectPerTopic[topic] = 0;
        }

        numCorrectPerTopic[topic]++;
      }

      numQuestions++;
      accuracyByTopic[topic].numQuestions++;

      if (isShared) {
        numSharedQuestions++;
      }

      if (isRepeated) {
        numRepeatedQuestions++;
      }

      if (!numQuestionsPerTopic[topic]) {
        numQuestionsPerTopic[topic] = 0;
      }

      numQuestionsPerTopic[topic]++;
    }

    if (!numOfTopics[topic]) {
      numOfTopics[topic] = 0
    }

    numOfTopics[topic]++;
  }

  totalCorrect += numCorrect;
  totalQuestions += numQuestions;

  console.log('Name: ' + name);
  console.log('Accuracy: ' + numCorrect / numQuestions);
  console.log('Shared Accuracy: ' + numSharedCorrect / numSharedQuestions);
  // console.log('Repeated Accuracy: ' + numRepeatedCorrect, numRepeatedQuestions);

  // _.each(numCorrectPerTopic, function(num, topic) {
  //   console.log(topic + ' : ' + num);
  // });

  // _.each(numQuestionsPerTopic, function(num, topic) {
  //   console.log(topic + ' : ' + num);
  // });
});

var topicKeys = Object.keys(accuracyByTopic);
for (var k = 0; k < topicKeys.length; k++) {
  var topicKey = topicKeys[k];
  var numAccuracyByTopic = accuracyByTopic[topicKey];
  var numLengthsByTopic = lengthsByTopic[topicKey];
  var topicCount = numOfTopics[topicKey];
  var avgLength = numLengthsByTopic.words / topicCount;

  console.log('Topic: ' + topicKey, numAccuracyByTopic.numCorrect / numAccuracyByTopic.numQuestions);
  console.log('Topic: ' + topicKey, 'Words: ' + numLengthsByTopic.words, 'Chars: ' + numLengthsByTopic.chars, 'Number: ' + topicCount, 'Avg. words: ' + avgLength);
}

console.log('Overall accuracy: ' + totalCorrect / totalQuestions);
