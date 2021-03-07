$('h1').click(function () {
    $(this).text("I was changed")
})

$('li').click(function () {
    console.log('There was a click on li')
})

//Key Press
$('input').eq(0).keypress(function (event) {
    if (event.which === 13) {
        $('h3').toggleClass('turnBlue');
    }
})

// on()

$('h1').on('mouseenter', function () {
    $(this).toggleClass('turnBlue')
})


$('input').eq(1).on('click', function () {
    $('.container').fadeOut(3000)
})