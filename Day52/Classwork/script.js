//objects and dot notation
// let myData={
//     name: "David", 
//     surname: "Tezelashvili",
//     age: 15,
//     Role: "Squad Leader"
// }
// console.log(myData.age)

// let greet=document.getElementById("label1").innerHTML;
// let name=window.prompt("Enter your name: ");
// document.getElementById("label1").innerHTML="Welcome " + name;

// const me={
//     name: function(){
//         console.log("David");
//     },
//     surname: "Tezelashvili",
//     age: 15,
//     Role: "Squad Leader"
// }
// console.log(me.name)

// for (i=0; i<=15; i+=15){
//     console.log(i)
// }

let car1={
    brand: "BMW",
    model: "e30",
    year: 1982,
    color: "red",
    doors: 2,
    feature: function(){
        let ftr1="great for drift"
        console.log(ftr1)
    }
}
let car2={
    brand: "mercedes",
    model: "190E",
    year: 1983,
    color: "black",
    doors: 2,
    feature: function(){
        let ftr2="DTM legend"
        console.log(ftr2)
    }
}
console.log(car1)
console.log(car2)

let name=document.getElementById("label1");
console.dir(name)

//checked is used to see if checkbox is ticked