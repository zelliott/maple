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

function saveAnswer(delta) {
  var answers = [];

  $('.answer:visible').each(function (i) {
    answers.push($(this).val());
  });

  $.post('http://localhost:3000/test/save', {
    current: this.current,
    next: this.current + delta,
    answers: answers
  }).done(function () {

  }).fail(function () {

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