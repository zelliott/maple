var aws = require('aws-sdk');

aws.config.update({
  region: 'us-west-1',
  endpoint: 'http://localhost:8000'
});

var db = new aws.DynamoDB();

var params = {
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

db.createTable(params, function (err, data) {
  if (err) {
    console.error("Error: ", JSON.stringify(err, null, 2));
  } else {
    console.log("Created table: ", JSON.stringify(data, null, 2));
  }
});

module.exports = db;