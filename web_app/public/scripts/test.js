function displayButtons(current, total) {
    $('.previous-abstract').toggle(current > 0);
    $('.next-abstract').toggle(total - current > 1);
    $('.finish-abstract').toggle(total - current === 1);
}

function changeAbstract(current, delta, total) {
  $('.abstract-current').hide();
  $('.abstract-' + current).removeClass('abstract-current');

  current += delta;

  $('.abstract-' + current).addClass('abstract-current');
  $('.abstract-current').show();

  $('.current').text((total - current) + ' remaining');
  $('.current').data('value', current);
  $('.progress').attr('value', current);
}

$(document).ready(function () {
  var current = Number($('.current').data('value'));
  var total = Number($('.total').data('value'));

  $('.abstract').hide();
  $('.abstract-current').show();

  displayButtons(current, total);

  $('.previous-abstract').on('click', function () {
    changeAbstract(current, -1, total);
    displayButtons(--current, total);
  });

  $('.next-abstract').on('click', function () {
    changeAbstract(current, 1, total);
    displayButtons(++current, total);
  });

  $('.finish-abstract').on('click', function () {

  })

  $('.blank').on('click', function () {
    var num = Number($(this).text())

    $('.answer-' + num).focus();
  });

});