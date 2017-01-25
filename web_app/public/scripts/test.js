// Global URL
var baseURL = 'http://custom-env-1.v8hharbp4m.us-west-1.elasticbeanstalk.com/';
// var baseURL = 'http://localhost:8081/';

// Activate all tooltips
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

// Test modes.
var MODE = {
  CLOZE: 'CLOZE',
  READABILITY: 'READABILITY'
};

// Based upon the current abstract and the total number of abstracts,
// determine which buttons to show.
function displayButtons () {
    $('.previous').toggle(this.current > 0);
    $('.next').toggle(this.total - this.current > 1);
    $('.finish-1').toggle((this.total - this.current === 1) && (this.mode === MODE.CLOZE));
    $('.finish-2').toggle((this.total - this.current === 1) && (this.mode === MODE.READABILITY));
}

// Based upon the current abstract and the move (forwards/backwards),
// determine which abstract to show.
function changeAbstract (delta) {
  $('.abstract-current').hide();
  $('.abstract-' + this.current).removeClass('abstract-current');

  this.current += delta;

  $('.abstract-' + this.current).addClass('abstract-current');
  $('.abstract-current').show();

  $('.current').text((this.total - this.current) + ' remaining');
  $('.current').data('value', this.current);
  $('.progress').attr('value', this.current);
}

// Focus the current answer.
function focusAnswer (el) {
    var num = Number(el.text())
    $('.answer-' + num).focus();
}

function disableBtns (isDisabled) {
  if (isDisabled) {
    $('.previous, .next').attr('disabled', 'disabled');
    $('.saving-status').text('Saving answers...')
  } else {
    $('.previous, .next').removeAttr('disabled');
    $('.saving-status').text('Answers saved');
  }
}

function saveAnswer (delta) {

  var saveURL;
  var data;

  disableBtns(true);

  if (this.mode == MODE.CLOZE) {

    var answers = [];

    $('.answer:visible').each(function (i) {
      answers.push($(this).val());
    });

    saveURL = baseURL + 'test/save/cloze';
    data = {
      current: this.current,
      next: this.current + delta,
      answers: answers,
      timeElapsed: Date.now() - this.timer
    };

    this.timer = Date.now();
  } else {

    var difficulty = Number($('.difficulty:visible').val());

    saveURL = baseURL + 'test/save/readability';
    data = {
      current: this.current,
      next: this.current + delta,
      difficulty: difficulty
    };

  }

  $.post(saveURL, data).done(function (data, status) {
    disableBtns(false);
  }).fail(function (data, status) {
    console.log('Something bad happened and was not caught...');
  });

}

function changeMode (mode) {
  var value = mode;
  var text;

  if (mode === MODE.CLOZE) {
    text = 'Part 1: Cloze';
  } else {
    text = 'Part 2: Readability';
  }

  $('.mode').data('value', value);
  $('.mode').text(text);

  this.mode = mode;
}

function displayAbstracts () {
  var isCloze = this.mode === MODE.CLOZE;

  return $.get(baseURL + 'api/test').done(function (data, status) {

    var numQuestions = data.questions.length;
    for (var i = 0; i < numQuestions; i++) {
      var question = data.questions[i];
      var text = isCloze ? question.clozeAbstract : question.fullAbstract;

      var $el = $('.abstract-' + i + ' .abstract-text');
      $el.html(text);
    }

  }).fail(function (data, status) {
    console.log('Something bad happened and was not caught...');
  });
}

function displayPanel () {
  var isCloze = this.mode === MODE.CLOZE;

  $('.part-1-panel').toggle(isCloze);
  $('.part-2-panel').toggle(!isCloze);
}

function displayMessage (shouldDisplay) {
  $('.test-message').toggle(shouldDisplay);
  $('.test-content').toggle(!shouldDisplay);
}

var Test = function () {
  this.current = Number($('.current').data('value'));
  this.total = Number($('.total').data('value'));
  this.timer = Date.now();
  this.mode = $('.mode').data('value');

  $('.abstract').hide();
  $('.abstract-current').show();

  var self = this;

  $('.previous').on('click', function () {
    self.saveAnswer(-1);
    self.changeAbstract(-1);
    self.displayButtons();

    self.timer = Date.now();
  });

  $('.next').on('click', function () {
    self.saveAnswer(1);
    self.changeAbstract(1);
    self.displayButtons();

    self.timer = Date.now();
  });

  $('.finish-1').on('click', function () {
    self.saveAnswer(1);
    self.changeAbstract(1);
    self.displayMessage(true);

    var message = 'Thank you for completing Part 1 of this test.  Click the button below to start Part 2.'

    $('.test-message p').text(message);
  });

  $('.finish-2').on('click', function () {
    self.saveAnswer(1);
    self.changeAbstract(1);
    self.displayMessage(true);

    var message = 'Thank you for completing both parts of this test.  You may now close this window.'

    $('.test-message p').text(message);
    $('.test-message button').hide();
  });

  $('.start-2').on('click', function () {
    self.changeMode(MODE.READABILITY);
    self.displayAbstracts(MODE.READABILITY).done(function (data, status) {

      self.changeAbstract(-1 * self.total);
      self.displayButtons();
      self.displayPanel();
      self.displayMessage(false);

    }).fail(function (data, status) {
      console.log('Something bad happened and was not caught...');
    });
  });

  $('.blank').on('click', function () {
    self.focusAnswer($(this));
  });
};

Test.prototype = {
  displayButtons: displayButtons,
  changeAbstract: changeAbstract,
  focusAnswer: focusAnswer,
  saveAnswer: saveAnswer,
  changeMode: changeMode,
  displayAbstracts: displayAbstracts,
  displayPanel: displayPanel,
  displayMessage: displayMessage
};

$(document).ready(function () {
  var test = new Test();

  test.displayAbstracts();
  test.displayButtons();
  test.displayPanel();
  test.displayMessage(false);
});