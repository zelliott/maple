var request = require('request');
var _ = require('lodash');
var doc = require('dynamodb-doc');
var db = require('./../server/db');
var dc = new doc.DynamoDB(db);

module.exports = {
  start: function (passkey, cb) {

    var params = {
      TableName: 'Tests',
      Item: {
        passkey: passkey,
        test: 'Test 1'
      }
    };

    dc.putItem(params, function (err, data) {
      if (err) {
        console.error("Error: ", JSON.stringify(err, null, 2));
      } else {
        console.log("Added item: ", JSON.stringify(data, null, 2));
        cb(JSON.stringify(data, null, 2));
      }
    });
  }
};