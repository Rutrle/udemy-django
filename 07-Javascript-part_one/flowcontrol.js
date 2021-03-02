var hot = false
var temp = 40

if (temp > 80) {
    console.log("hot")
} else if (temp <= 80 && temp >= 50) {
    console.log("average")
} else if (temp < 50 && temp >= 32) {
    console.log("pretty cold")
} else {
    console.log("It is very cold out")
}

