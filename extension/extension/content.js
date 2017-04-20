var Maple = function () {

};

Maple.prototype = {

  determineReadability: function () {
    console.log('determineReadability');

    $('.rprt').each(function (i) {
      var $item = $(this);
      var $itemInfo = $item.find('.rprtnum');
      var url = $item.find('a').attr('href');
      // var mapleUrl = 'https://sample-env.q6yemetfiv.us-west-1.elasticbeanstalk.com/api/analyze';
      var mapleUrl = 'https://localhost:8443/api/analyze';

      var $mapleLoading = $(document.createElement('div'))
        .text('...')
        .addClass('maple-loading')
        .appendTo($itemInfo);

      $.ajax({
        url: url,
        async: true,
        success: function (data) {
          var abstractText = $(data).find('abstracttext').text();

          // POST abstract text to our web app analysis api

          $.ajax({
            type: 'POST',
            async: true,
            crossDomain: true,
            url: mapleUrl,
            data: abstractText,
            dataType: 'application/json',
            success: function (data) {
              var score = Math.floor(data.score * 100);
              var scoreColorClass = (score < 33) ? 'maple-score-green' :
                                    (score < 66) ? 'maple-score-yellow' :
                                                   'maple-score-red';

              var $mapleScore = $(document.createElement('div'))
                .text(score)
                .addClass('maple-score')
                .addClass(scoreColorClass)
                .appendTo($itemInfo);

              $itemInfo.find('.maple-loading').hide();
            },
            error: function (xhr, status, error) {
              console.log(xhr, status, error);
            }
          });
        },
        error: function (xhr, status, error) {
          var $mapleError = $(document.createElement('div'))
            .text('!')
            .addClass('maple-error')
            .appendTo($itemInfo);

          $itemInfo.find('.maple-loading').hide();
        }
      });
    });
  },

  simplifyWords: function() {
    console.log('simplifyWords');

    // var mapleUrl = 'https://sample-env.q6yemetfiv.us-west-1.elasticbeanstalk.com/api/analyze';
    var mapleUrl = 'https://localhost:8443/api/analyze';
    var abstractText = $('abstracttext').text();

    $.ajax({
      type: 'POST',
      async: true,
      url: mapleUrl,
      data: abstractText,
      dataType: 'json',
      success: function (data) {
        var definitions = data.definitions;
        var abstractTextWords= abstractText.split('');

        abstractTextWords.forEach(function(word) {
          if (definitions[word]) {
            // TODO
            // Highlight this word
            // Insert definition
          }
        });
      },
      error: function (xhr, status, error) {
        console.log(xhr, status, error);
      }
    });
  }

};

$(document).ready(function() {
  var maple = new Maple();
  var isSearchResults = window.location.href.indexOf('term') >= 0;

  if (isSearchResults) {
    maple.determineReadability();
  } else {
    maple.simplifyWords();
  }
});