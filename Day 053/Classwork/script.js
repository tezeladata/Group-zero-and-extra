// let myStr="Hello World!";
// const myObject={
//     name: "David",
//     surname: "Tezelashvili",
//     age: 15,
//     role: "Github Controller",
//     changeRole: function(newRole){
//         myObject.role=newRole;
//     }
// }
// console.log("Squad Leader")
// myObject.changeRole();
// const bestAcademy=true;
// let myArr=[1,2,3,4,5]

// const bestCar={
//     brand: "BMW",
//     model: "e34",
//     doors: 4,
//     year: 1988,
//     engine: {
//         name: "S65B40",
//         type: "V",
//         cilinders: 8,
//         atmospheric: "yes",
//         rev: "9000rpms",
//         valves: 32,
//         cooler: "liquid"
//     },
//     getEngine: function(){
//         return bestCar.engine;
//     }
// }
// console.log(bestAcademy.engine)

// const acc={};
// let form=document.getElementById("form");
// let button=document.getElementById("button");
// button.addEventListener("click", function(){
//     acc.name=form.elements.name.value;
//     acc.lastname=form.elements.lastname.value;
//     acc.age=form.elements.age.value;
//     console.log(acc)
// })
// console.log(acc)

// const changer={
//     changeName: function(acc, newName){
//         acc.name=newName;
//     }
// }
// changer.changeName=(myObject, "Nika")

//hw1, hw2, hw5:
const me={
    name: "David",
    surname: "Tezelashvili",
    age: 15,
    role: "Github Controller",
    getName: function(){
        console.log(me.name);
    },
    bankAccount:{
        amount: 500,
        currency: "Gel",
        accNum: 14983248293
    }
}
const you={
    name: "Luka",
    surname: "Tskhvaradze",
    age: 17,
    role: "Mentor",
    getName: function(){
        console.log(me.name);
    },
    bankAccount:{
        amount: 100,
        currency: "usd",
        accNum: 298342390877423
    }
}
console.log(me.bankAccount.currency)
console.log(you.bankAccount.amount)

//hw3:
const data1={}
let form=document.getElementById("form");
let btn=document.getElementById("button1");
btn.addEventListener("click", function(){
    data1.num1=form.elements.num1.value;
    data1.num2=form.elements.num2.value;
    console.log(data1)
})
console.log(data1)

//hw4
const data2={}
let form2=document.getElementById("form1");
let btn2=document.getElementById("button2");
btn2.addEventListener("click", function(){
    data2.name=form2.elements.name.value;
    data2.surname=form2.elements.surname.value;
    data2.age=form2.elements.age.value;
    data2.password=form2.elements.password.value;
    console.log(data2)
})
const array1=[data2.name, data2.surname, data2.age, data2.password];
console.log(array1);