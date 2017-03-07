var MapleAnalyzer = function () {
};

MapleAnalyzer.prototype = {

  analyze: function () {
    $('.rprt').each(function (i) {
      var $item = $(this);
      var $itemInfo = $item.find('.rprtnum');
      var url = $item.find('a').attr('href');

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

          var score = Math.floor(Math.random() * 100);
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
          var $mapleError = $(document.createElement('div'))
            .text('!')
            .addClass('maple-error')
            .appendTo($itemInfo);

          $itemInfo.find('.maple-loading').hide();
        }
      });
    });
  }

};

$(document).ready(function() {

  var analyzer = new MapleAnalyzer();
  analyzer.analyze();
});