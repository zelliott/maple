var _ = require('lodash');
var fs = require('fs');

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

var repeatedIds = {};

_.each(testIds, function(t) {
    var test = JSON.parse(fs.readFileSync(t.test + '.questions.json', 'utf8'));
    var seenIds = {};
    var i = 0;

    _.each(test, function(question) {
        var id = question.originalString;
        var key = question.removedWords.join('.');
        if (seenIds[id]) {
            if (!repeatedIds[t.passkey]) {
                repeatedIds[t.passkey] = [seenIds[id][0]];
            }

            repeatedIds[t.passkey].push(key);
            i++;
        } else {
            seenIds[id] = [key];
        }
    });

    console.log(i);

});

fs.writeFile('repeated_ids.json', JSON.stringify(repeatedIds, null, 2), function (err) {
    if (err) return console.log(err);
});