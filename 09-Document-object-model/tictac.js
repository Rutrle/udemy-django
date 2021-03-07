var restart = document.querySelector('#b');
var squares = document.querySelectorAll('td');


function Clearboard() {
    console.log('restart')
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
}


restart.addEventListener('click', Clearboard)




var boxOne = document.querySelector('#one')

console.log("loaded")

boxOne.addEventListener('click', function () {
    if (boxOne.textContent === "") {
        boxOne.textContent = "X";
    } else if (boxOne.textContent === "X") {
        boxOne.textContent = "O";
    } else if (boxOne.textContent === "O") {
        boxOne.textContent = "";
    }
})
