// Based upon the current abstract and the total number of abstracts,
// determine which buttons to show.
function displayButtons () {
    $('.previous-abstract').toggle(this.current > 0);
    $('.next-abstract').toggle(this.total - this.current > 1);
    $('.finish-abstract').toggle(this.total - this.current === 1);
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
function focusAnswer(el) {
    var num = Number(el.text())
    $('.answer-' + num).focus();
}

function disableBtns(isDisabled) {
  if (isDisabled) {
    $('.previous-abstract, .next-abstract').attr('disabled', 'disabled');
    $('.saving-status').text('Saving...')
  } else {
    $('.previous-abstract, .next-abstract').removeAttr('disabled');
    $('.saving-status').text('Saved');
  }
}

function saveAnswer(delta) {
  var answers = [];

  disableBtns(true);
  $('.answer:visible').each(function (i) {
    answers.push($(this).val());
  });

  // var baseURL = 'http://node-express-env.8nhudetmtc.us-west-1.elasticbeanstalk.com/';
  var baseURL = 'http://localhost:3000/';
  $.post(baseURL + 'test/save', {
    current: this.current,
    next: this.current + delta,
    answers: answers
  }).done(function (data, status) {
    disableBtns(false);
  }).fail(function (data, status) {
    console.log('Something bad happened and was not caught...');
  });
}

var Test = function () {
  this.current = Number($('.current').data('value'));
  this.total = Number($('.total').data('value'));

  $('.abstract').hide();
  $('.abstract-current').show();
  $('.test-completed').hide();

  var self = this;

  $('.previous-abstract').on('click', function () {
    self.saveAnswer(-1);
    self.changeAbstract(-1);
    self.displayButtons();
  });

  $('.next-abstract').on('click', function () {
    self.saveAnswer(1);
    self.changeAbstract(1);
    self.displayButtons();
  });

  $('.finish-abstract').on('click', function () {
    self.saveAnswer(1);
    self.changeAbstract(1);
    $('.test-content').hide();
    $('.test-completed').show();
  })

  $('.blank').on('click', function () {
    self.focusAnswer($(this));
  });
};

Test.prototype = {
  displayButtons: displayButtons,
  changeAbstract: changeAbstract,
  focusAnswer: focusAnswer,
  saveAnswer: saveAnswer
};

$(document).ready(function () {
  var test = new Test();

  test.displayButtons();
});