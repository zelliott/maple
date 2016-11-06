var request = require('request');
var _ = require('lodash');
var aws = require('aws-sdk')
var db = require('./../server/db');
var dc = new aws.DynamoDB.DocumentClient(db);

module.exports = {
  start: function (passkey, cb) {

    // --------------------------------------------------
    // TODO:
    // Generate unique test here using Zhi's script.
    // --------------------------------------------------

    var questions = [
      {
        abstract: 'This is a <button type="button" class="btn btn-secondary btn-sm blank">1</button> test.  It has <button type="button" class="btn btn-secondary btn-sm blank">2</button> blanks.',
        answers: [null,null],
        difficulty: -1
      },
      {
        abstract: 'This is another <button type="button" class="btn btn-secondary btn-sm blank">1</button>  It has <button type="button" class="btn btn-secondary btn-sm blank">2</button> blanks.',
        answers: [null,null],
        difficulty: -1
      }
    ];

    var params = {
      TableName: 'Tests',
      Item: {
        passkey: passkey,
        questions: questions,
        current: 0,
        completed: false
      }
    };

    dc.put(params, function (err, data) {

      // TODO:
      // Handle any error here.

      if (err) {

      } else {
        cb(null, {
          passkey: passkey
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