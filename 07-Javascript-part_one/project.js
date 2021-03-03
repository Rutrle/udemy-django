var first_name = prompt("What is your first name?")
var last_name = prompt("What is your last name?")

var age = prompt("what is your age in years?")
var height = prompt("what is your height in cm?")
var pet_name = prompt("what is your pet name?")

var condition_1 = first_name[0] === last_name[0]
var condition_2 = age > 20 && age < 30
var condition_3 = height >= 170
var condition_4 = pet_name[pet_name.length - 1] == "y"

if (condition_1 && condition_2 && condition_3 && condition_4) {
    console.log("O-5 clearance granted")
} else (console.log("you will be terminated"))