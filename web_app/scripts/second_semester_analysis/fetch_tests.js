var _ = require('lodash');
var fs = require('fs');
var aws = require('aws-sdk')
var db = require('./../../server/db');
var dc = new aws.DynamoDB.DocumentClient(db);

var params = {
  TableName: 'CompletedTests'
};

var results = [];

dc.scan(params, onScan);

function onScan (err, data) {
  if (!err) {

    results = results.concat(data.Items);

    if (typeof data.LastEvaluatedKey !== 'undefined') {

      params.ExclusiveStartKey = data.LastEvaluatedKey;
      dc.scan(params, onScan);

    } else {

      fs.writeFile('results.json', JSON.stringify(results, null, 2), function (err) {
        if (err) return console.log(err);
      });

    }
  }
}