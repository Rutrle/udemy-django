var bluePlayer = prompt("Player one please enter your name, you will be blue")
var bluecolor = ('rgb(86, 151, 255)')

var redPlayer = prompt("Player two please enter your name, you will be red")
var redcolor = ('rgb(237, 45, 73)') //rgb is used because of jquery

var game_on = true;
var table = $('table tr');


function reportWin(rowNum, colNum) {
    console.log("You won starting at this row,col");
    console.log(rowNum)
    console.log(colNum)
}

function changeColor(rowIndex, colIndex, color) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color)
}

function returnColor(rowIndex, colIndex) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color')
}

function checkBottom(colIndex) {
    var colorReport = returnColor(5, colIndex)
    for (var row = 5; row > -1; row--) {
        colorReport = returnColor(row, colIndex)
        if (colorReport === 'rgb(145, 145, 145)') {
            return row
        }
    }
}

function colorMatchCheck(one, two, three, four) {
    return (one === two && one === three && one === four && one !== 'rgb(145, 145, 145)' && one !== undefined)
}


function horizontalWinCheck() {
    for (var row = 0; row < 6; row++) {
        for (var col = 0; col < 4; col++) {
            if (colorMatchCheck(returnColor(row, col), returnColor(row, col + 1), returnColor(row, col + 2), returnColor(row, col + 3))) {
                console.log('horizontal');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

function verticalWinCheck() {
    for (var col = 0; col < 7; col++) {
        for (var row = 0; row < 3; row++) {
            if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col), returnColor(row + 2, col), returnColor(row + 3, col))) {
                console.log('vertical');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}


function diagonalWinCheck() {
    for (var col = 0; col < 5; col++) {
        for (var row = 0; row < 7; row++) {
            if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col + 1), returnColor(row + 2, col + 2), returnColor(row + 3, col + 3))) {
                console.log('diag');
                reportWin(row, col);
                return true;
            } else if (colorMatchCheck(returnColor(row, col), returnColor(row - 1, col + 1), returnColor(row - 2, col + 2), returnColor(row - 3, col + 3))) {
                console.log('diag');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

var currentPlayer = 1;
var currentName = bluePlayer;
var currentColor = bluecolor;

$('h3').text(bluePlayer + " it is your turn")

$('.board button').on('click', function () {
    var col = $(this).closest('td').index();
    var bottomAvail = checkBottom(col);
    changeColor(bottomAvail, col, currentColor);
    console.log(bottomAvail)
    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
        $('h1').text(currentName + "You have won!")
        $('h3').fadeOut('fast');
        $('h2').fadeOut('fast');
    }
    currentPlayer = currentPlayer * -1
    if (currentPlayer === 1) {
        currentName = bluePlayer
        currentColor = bluecolor;
        $('h3').text(bluePlayer + "it is your turn")
    } else {
        currentName = redPlayer;
        $('h3').text(bluePlayer + "it is your turn")
        currentColor = redcolor;

    }
})