var request = require('request');
var _ = require('lodash');
var fs = require('fs');
var aws = require('aws-sdk')
var db = require('./../server/db');
var dc = new aws.DynamoDB.DocumentClient(db);

var formatQuestions = function(rawQuestions) {

  var generateButton = function (i) {
    return '<button type="button" class="btn btn-secondary btn-sm blank">' + i + '</button>';
  };


  return _.map(rawQuestions, function(question) {
    var splitAbstract = question.originalString.split(/\s+/g);
    var removed = question.removedWords;

    _.forEach(question.indices, function(index, i) {
      splitAbstract.splice(index, 1, generateButton(i + 1));
    });

    var abstract = splitAbstract.join(' ');
    var answers = [];

    for (var i = 0; i < removed.length; i++) {
      answers.push(null);
    }

    return {
      correct: removed,
      answers: answers,
      abstract: abstract,
      difficulty: -1
    };
  });
};

var getNextId = function (cb) {
    var filename = 'data/currentTest.json';
    var id = JSON.parse(fs.readFileSync(filename, 'utf8')).id;

    fs.writeFile(filename, JSON.stringify({ id: id + 1 }), function (err) {
      if (err) {
        cb(err, null);
        return;
      }
    });

    return id;
}

module.exports = {
  start: function (passkey, cb) {

    var id = getNextId(cb);
    var paramsGet = {
      TableName: 'RawTests',
      Key: {
        id: id
      }
    };

    dc.get(paramsGet, function (err, data) {

      if (err) {
        cb(err, null);
        return;
      }

      var rawQuestions = data.Item.test;
      var questions = formatQuestions(rawQuestions);

      var paramsPut = {
        TableName: 'Tests',
        Item: {
          passkey: passkey,
          questions: questions,
          current: 0,
          completed: false
        }
      };

      dc.put(paramsPut, function (err, data) {

        // TODO:
        // Handle any error here.

        if (err) {
          cb(err, null);
          return;
        }

        cb(null, {
          passkey: passkey
        });
      });
    });
  },

  get: function (passkey, cb) {

    var params = {
      TableName: 'Tests',
      Key: {
        passkey: passkey
      }
    };

    dc.get(params, function (err, data) {
      var test = data.Item;

      // TODO:
      // If test is already completed, don't load.
      if (test.completed) {

      }

      if (err) {
        cb(err, null);
        return;
      }

      cb(null, data.Item);
    });
  },

  save: function(data, cb) {
    var TestService = this;
    this.get(data.passkey, function (err, body) {

      if (err) {
        cb(err, null);
        return;
      }

      var questions = body.questions;
      var current = data.current;
      var next = Number(data.next);
      var completed = questions.length < next + 1;

      questions[current].answers = data.answers;

      var params = {
        TableName: 'Tests',
        Key: {
          passkey: data.passkey
        },
        UpdateExpression: 'set #propA = :valueA, #propB = :valueB, #probC = :valueC',
        ExpressionAttributeNames: {
          '#propA': 'questions',
          '#propB': 'current',
          '#probC': 'completed'
        },
        ExpressionAttributeValues: {
          ':valueA': questions,
          ':valueB': next,
          ':valueC': completed
        },
        ReturnValues: 'ALL_NEW'
      };

      dc.update(params, function (err, data) {

        if (err) {
          cb(err, null);
          return;
        }

        var test = data.Attributes;

        if (test.completed) {
          TestService.complete(test, function (err, body) {
            if (err) {
              cb(err, null);
              return;
            }

            // TODO:
            // Pass back current thing
            cb(null, body);
          });

          return;
        }

        // TODO:
        // Pass back current thing
        cb(null, test);
      })
    })
  },

  complete: function(data, cb) {

    var params = {
      TableName: 'CompletedTests',
      Item: data
    };

    dc.put(params, function (err, data) {

      if (err) {
        cb(err, null);
        return;
      }

      // TODO:
      // Pass back current thing
      cb(null, data);
    });
  }
};