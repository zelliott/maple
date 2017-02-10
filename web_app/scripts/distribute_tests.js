var fs = require('fs');
var _ = require('lodash');
fs.readFile('./generated_tests.csv', 'utf-8', function (err, data) {
  var tests = data.split('\n').slice(1);
  var numTests = tests.length;
  var orderedTests = [];

  var offset = -1;
  for (var i = 0; i < numTests; i++) {

    var index = (i * 3) % numTests;

    if (index == 0) { offset++; }

    var test = tests[index + offset];
    var passkey = test.split(',')[0];
    var url = 'http://custom-env-1.v8hharbp4m.us-west-1.elasticbeanstalk.com/test/' + passkey + '\n';
    orderedTests.push(url);

    if (i % 2 == 1) orderedTests.push('\n');

  }

  fs.unlink('./distributed_tests.txt');
  fs.appendFile('./distributed_tests.txt', orderedTests.join(''), function (err) {

    if (!err) {
      console.log(orderedTests.length * 2 / 3);
    }
  });
});