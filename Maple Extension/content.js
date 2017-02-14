function fetchText(x) {
  //modify this function infuture to fetch pdf text.
  //currently fetches only the abstracts
  var hrefData;
  var abstractText;
  var href = $(x).find('a').attr('href');
  $.ajax({
    url: href,
    async: false,
    success: function(data) {
              hrefData = data;
            }
  });
  abstractText = $(hrefData).find('.abstr').text();
  return abstractText;
}

function averageWord(passage) {
    var words = passage.split(" ");
    var total = 0;
    for (var i = 0; i < words.length; i++) {
        total += words[i].length;
    }
    return total / words.length;
}

function generateScore(passage) {
  //modify this function in future to calculate true score.
  //currently just scales the score according to avg word length.
    if(passage.length == 0) {
      return "N/A";
    }
    passage = passage.replace(/ *\([^)]*\) */g, "");
    passage = passage.replace(/[:\.\r\n]+/g,' ');
    passage = passage.replace(/[^a-zA-Z ]+/g, '');
    var avgLen = averageWord(passage);
    var score = Math.round((((avgLen - 4) * 80) / 3.5) + 20)
    return score;
}


//listens for pageAction button click request from background.js
chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    if (msg.text === 'Analyze') {
        $('.rprt').each( function(i) {
          var resultText = fetchText(this);
          var score = generateScore(resultText);
          if (score < 54) {
            var imageURL = chrome.extension.getURL('icon_green.png');
            $(this).children('.rprtnum.nohighlight').append("<img src="+imageURL+"><br><big><b>"+score+"</b></big>");
          }
          else if (score < 70) {
            var imageURL = chrome.extension.getURL('icon_yellow.png');
            $(this).children('.rprtnum.nohighlight').append("<img src="+imageURL+"><br><big><b>"+score+"</b></big>");
          }
          else{
            var imageURL = chrome.extension.getURL('icon_red.png');
            $(this).children('.rprtnum.nohighlight').append("<img src="+imageURL+"><br><big><b>"+score+"</b></big>");
          }
        });
        console.log("trying to send response");
        sendResponse("Done"); // having trouble with sending things back to background.js
    }
});

