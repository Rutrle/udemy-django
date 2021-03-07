var boxOne = document.querySelector('#one')

console.log("loaded")


//headOne.addEventListener('mouseover', function () {
//    headOne.textContent = "Mouse currently over";
//    headOne.style.color = 'red';
//})

boxOne.addEventListener('click', function () {
    if (boxOne.textContent === "") {
        boxOne.textContent = "X";
    } else if (boxOne.textContent === "X") {
        boxOne.textContent = "O";
    } else if (boxOne.textContent === "O") {
        boxOne.textContent = "";
    }
})
