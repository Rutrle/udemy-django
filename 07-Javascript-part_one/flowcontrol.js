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

var ham = 10
var cheese = 0
var report = "blank"

if (ham >= 10 && cheese >= 10) {
    report = "strong sales of both ham and cheese!"
} else if (ham === 0 && cheese === 0) {
    report = "Nothing sold!"
} else {
    report = "we had some sales"
}

console.log(report);