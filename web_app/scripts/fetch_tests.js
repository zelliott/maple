var _ = require('lodash');
var fs = require('fs');
var aws = require('aws-sdk')
var db = require('./../server/db');
var dc = new aws.DynamoDB.DocumentClient(db);

var files = [
  {},
  {
    passkey: '8e5a6bfc88f891ea799bc6694436edb9',
    count: 100,
    name: 'Omar',
    id: 1
  },
  {
    passkey: 'e4b07377c07d2c3d95a737e4bf642082',
    count: 100,
    name: 'Zack',
    id: 2
  },
  {
    passkey: 'ffe359d641982de20dbc86eae7ccb522',
    count: 100,
    name: 'Spencer',
    id: 3
  },
  {
    passkey: '26ae945be740ffc1c6d7b2b88a0ec493',
    count: 100,
    name: 'Zhi',
    id: 4
  }
];

var id = 1;
var passkey = files[id].passkey;
var paramsA = {
  TableName: 'Tests',
  Key: {
    passkey: passkey
  }
};

dc.get(paramsA, function (err, data) {
  var test = data.Item;

  var questions = {};

  _.each(test.questions, function(question, i) {
    questions[i] = question;
  });

  fs.writeFile(passkey + '.questions.json', JSON.stringify(questions, null, 2), function (err) {
    if (err) return console.log(err);
  });
});

var paramsB = {
  TableName: 'RawTests',
  Key: {
    id: id
  }
};

dc.get(paramsB, function (err, data) {
  var test = data.Item.test;

  var questionTopics = {};

  _.each(test, function(question, id) {
    var removedWordsKey = question.removedWords.join('.');
    var topic = question.topic;

    questionTopics[removedWordsKey] = topic;
  });

  fs.writeFile(passkey + '.topics.json', JSON.stringify(questionTopics, null, 2), function (err) {
    if (err) return console.log(err);
  });
});
