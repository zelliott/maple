var request = require('request');
var _ = require('lodash');
var aws = require('aws-sdk')
var db = require('./../server/db');
var dc = new aws.DynamoDB.DocumentClient(db);

var formatQuestions = function(rawQuestions) {

  var generateButton = function (i) {
    return '<button type="button" class="btn btn-secondary btn-sm blank">' + i + '</button>';
  };


  return _.map(rawQuestions, function(question) {
    var splitAbstract = question.originalString.split(' ');
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

module.exports = {
  start: function (passkey, cb) {

    var id = 0;
    var paramsGet = {
      TableName: 'RawTests',
      Key: {
        id: id
      }
    };

    dc.get(paramsGet, function (err, data) {

      if (err) {

      } else {
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

          } else {
            cb(null, {
              passkey: passkey
            });
          }
        });
      }
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

      // TODO:
      // Handle any error here.

      var test = data.Item;

      // TODO:
      // If test is already completed, don't load.
      if (test.completed) {

      }

      if (err) {

      } else {

        cb(null, data.Item);
      }
    });
  },

  save: function(data, cb) {
    this.get(data.passkey, function (err, body) {
      var questions = body.questions;
      var current = data.current;
      var next = data.next;
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
        ReturnValues: 'UPDATED_NEW'
      };

      dc.update(params, function (err, data) {

        if (err) {

        } else {
          cb(null, data.Attributes);
        }
      })
    })
  }
};