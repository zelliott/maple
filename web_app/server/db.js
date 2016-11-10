var aws = require('aws-sdk');
var fs = require('fs');
var _ = require('lodash');

aws.config.update({
  region: 'us-west-1',
  endpoint: 'dynamodb.us-west-1.amazonaws.com' // http://localhost:8000
});

var db = new aws.DynamoDB();
var dc = new aws.DynamoDB.DocumentClient(db);

var createTable = function (params) {
  db.createTable(params, function (err, data) {
    if (err) {
      console.error("Error: ", JSON.stringify(err, null, 2));
    } else {
      console.log("Created table: ", JSON.stringify(data, null, 2));
    }
  });
};

var deleteTable = function (tableName) {
  var params = {
      TableName: tableName
  };

  db.deleteTable(params, function(err, data) {
      if (err) {
          console.error("Unable to delete table. Error JSON:", JSON.stringify(err, null, 2));
      } else {
          console.log("Deleted table. Table description JSON:", JSON.stringify(data, null, 2));
      }
  });
};

var populateRawTests = function (filename) {
  var rawTests = JSON.parse(fs.readFileSync(filename, 'utf8'));
  var id = 0;

  var requests = _.map(rawTests, function (test) {

    return {
      PutRequest: {
        Item: {
          id: id++,
          test: test
        }
      }
    };
  });

  var slicedRequests = requests.slice(0, 20);

  var params = {
    RequestItems: {
      'RawTests': slicedRequests
    }
  };

  dc.batchWrite(params, function (err, data) {
    console.log(err, data);
  });
};

var paramsTests = {
  TableName: 'Tests',
  KeySchema: [
    { AttributeName: 'passkey', KeyType: 'HASH' }
  ],
  AttributeDefinitions: [
    { AttributeName: 'passkey', AttributeType: 'S' }
  ],
  ProvisionedThroughput: {
    ReadCapacityUnits: 10,
    WriteCapacityUnits: 10
  }
};

var paramsRawTests = {
  TableName: 'RawTests',
  KeySchema: [
    { AttributeName: 'id', KeyType: 'HASH' }
  ],
  AttributeDefinitions: [
    { AttributeName: 'id', AttributeType: 'N' }
  ],
  ProvisionedThroughput: {
    ReadCapacityUnits: 10,
    WriteCapacityUnits: 10
  }
};

var paramsCompletedTests = {
  TableName: 'CompletedTests',
  KeySchema: [
    { AttributeName: 'passkey', KeyType: 'HASH' }
  ],
  AttributeDefinitions: [
    { AttributeName: 'passkey', AttributeType: 'S' }
  ],
  ProvisionedThroughput: {
    ReadCapacityUnits: 10,
    WriteCapacityUnits: 10
  }
};

// deleteTable('Tests');
// deleteTable('RawTests');
// deleteTable('CompletedTests');

// createTable(paramsTests);
// createTable(paramsRawTests);
// createTable(paramsCompletedTests);

// populateRawTests('data/rawTests.json');

module.exports = db;