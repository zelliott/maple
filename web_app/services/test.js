var request = require('request');
var _ = require('lodash');
var doc = require('dynamodb-doc');
var db = require('./../server/db');
var dc = new doc.DynamoDB(db);

module.exports = {
  start: function (passkey, cb) {

    // --------------------------------------------------
    // TODO:
    // Generate unique test here using Zhi's script.
    // --------------------------------------------------

    var test = [
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
        test: test,
        current: 0
      }
    };

    dc.putItem(params, function (err, data) {
      console.log(err, data);
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

    dc.getItem(params, function (err, data) {

      // TODO:
      // Handle any error here.

      if (err) {

      } else {

        cb(null, data.Item);
      }
    });
  }
};