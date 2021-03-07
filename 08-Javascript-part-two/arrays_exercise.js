


var students = []

function addNew() {
    var new_student = prompt("enter student name")
    students.push(new_student)
}

function remove() {
    var remName = prompt("what name would you like to remove?")
    var index = students.indexOf(remName);
    students.splice(index, 1)
}
function display() {
    console.log(students);
}
var continuation = prompt("would you like to use web app? (y/n)")
if (continuation === "y") {
    while (choose !== "quit") {
        if (continuation === "n") {
            alert("for trying again please refresh")
            break
        }
        var choose = prompt("would you like to add,remove or display or quit?")

        if (choose == "quit") {
            break
        } else if (choose === "add") {
            addNew()
        } else if (choose === "remove") {
            remove()
        } else if (choose === "display") {
            display()
        }
    }

    alert("Thanks for using web app! Please refresh to start again!")
}
