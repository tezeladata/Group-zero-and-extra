// JavaScript variables are containers for data values. Objects are variables too, but they can contain many values.

const myData={
    name: "David", 
    // name არის ობიექტის მახასიათებელი - property
    surname: "Tezelashvili", 
    age: 15, 
    country: "Georgia", 
    favColor: "Green",
    newNum: function(number){
        console.log(number)
    }
}
myData.number=123
const friendData={
    name: "Giorgi", 
    surname: "Maxarashvili", 
    age: 15, 
    country: "Georgia", 
    favColor: "Black"
}

myData.role="Crew Leader"
myData.favColor="Blue"
// Dot notation

console.log(myData)
console.log(friendData)

// Best practice: 
// Use const to create objects, because object data won't be changed (It won't affect properties)

const car={
    carName: "BMW",
    model: "E92", 
    weight: "1500kgs",
    start: function(){
        console.log("Car is starting.")
    }
}
car.start(console.log("Hello World!"))
car.break=function(seconds){
    for (let i=seconds; i>=0; i--){
        if (i==0){
            console.log("Car breaked!")
        } else if (i==1){
            console.log("Car breaks in 1 second")
        } else{
            console.log(`Car will break in ${i} seconds`)
        }
    }
}
car.break(10)
console.log(car["carName"], car["model"], car["weight"], car["start"])

console.log("David".indexOf("a"))

// Log is method of console object
console.dir(console)


const userChoice={
    color: "Green", 
    day: "Thursday",
    planet: "Earth",
    country: "Georgia"
}
document.getElementById("button1").onclick=function(){
    let data=document.getElementById("input1").value;
    console.log(userChoice[data])
}