var _ = require('lodash');
var fs = require('fs');

// var rawTests = JSON.parse(fs.readFileSync('../data/rawTests.json', 'utf8'));

var testIds = [
    {
        passkey: 'e4b07377c07d2c3d95a737e4bf642082',
        test: 'Test100'
    },
    {
        passkey: 'ffe359d641982de20dbc86eae7ccb522',
        test: 'Test11'
    },
    {
        passkey: '8e5a6bfc88f891ea799bc6694436edb9',
        test: 'Test10'
    },
    {
        passkey: '26ae945be740ffc1c6d7b2b88a0ec493',
        test: 'Test12'
    }
];

// _.each(testIds, function (t) {
//     fs.writeFile(t.test + '.questions.json', JSON.stringify(rawTests[t.test], null, 2), function (err) {
//         if (err) return console.log(err);
//     });
// });


// Confirmed that the pairs above area accurate

// var i = 0;
// _.each(testIds, function(t) {
//     var a = JSON.parse(fs.readFileSync(t.passkey + '.questions.json', 'utf8'));
//     var b = JSON.parse(fs.readFileSync(t.test + '.questions.json', 'utf8'));

//     var ids = {};

//     _.each(a, function(question, id) {
//         ids[question.correct.join('.')] = true;
//     });

//     _.each(b, function(question, id) {
//         if (!ids[question.removedWords.join('.')]) {
//             i++;
//         }
//     });
// });

// console.log(i);

var testAName = testIds[0].test;
var testA = JSON.parse(fs.readFileSync(testAName + '.questions.json', 'utf8'));

var sharedIds = {};
var allQuestions = {};
var i = 0;

_.each(testA, function(question, qId) {
    allQuestions[question.originalString] = question.removedWords;
});

for (var id = 1; id < 4; id++) {
    var testBName = testIds[id].test;
    var testB = JSON.parse(fs.readFileSync(testBName + '.questions.json', 'utf8'));
    _.each(testB, function(question, qId) {
        if (allQuestions[question.originalString]) {
            sharedIds[question.removedWords.join('.')] = id;
            sharedIds[allQuestions[question.originalString].join('.')] = 0;
            i++
        }
    });
}

console.log(i)

fs.writeFile('shared_ids.json', JSON.stringify(sharedIds, null, 2), function (err) {
    if (err) return console.log(err);
});