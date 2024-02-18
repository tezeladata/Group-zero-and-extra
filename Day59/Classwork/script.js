let myArr=[1,2,3,4,5]
console.log(myArr)

let person={name:"David", surname:"Tezelashvili", age: 15}
//      property: value
console.log(person)
console.log(person.age)
// Same:
console.log(person["name"])

console.log(person.name.concat(" " + person.age))
myArr.push(6, "Hello")
console.log(myArr)

//    პოზიცია, რამდენი ამოვარდეს
myArr.splice(2, 1)
console.log(myArr)

let Arr2=[1,2,3,4,5,6,7,8]
Arr2.splice(3,5)
console.log(Arr2)

const myName=["D", "a", "t", "a", "T", "e", "z", "e", "l","a", "s", "h", "v", "i", "l", "i"]
myName.splice(4,12)
console.log(myName)

document.write("Hello" + " " + "GOA best ")
document.write(person.surname.length)
// objectName.methodName()


let person2={name:"Andria", surname:"Tezelashvili", age: 8, myfunc(){console.log(person2.name,person2.age)}}
console.log(person2.myfunc())

let myObj={
    name: "David", 
    surname: "Tezelashvili",
    age: 15,
    myfunc: myfunc
}
function myfunc(year){
    console.log(year - myObj.age)
}
console.log(myfunc(2024))


// let Leader1={
//     name: "Vano",
//     age: 16,
//     rate: 10
// }
// let leader2={
//     name: "Sandro",
//     age: 16,
//     rate: 10
// }
// let leader3={
//     name: "Data",
//     age: 15,
//     rate: 10
// }


// constructor
function GoaLeaders(Name, Age, Rate){
    this.name=Name,
    this.age=Age,
    this.rate=Rate
}
const leaderVano=new GoaLeaders("Vano", 16, 10)
const leaderSandro=new GoaLeaders("Sandro", 16, 10)
//             new-ახალი ობიექტის შექმნა
console.log(leaderVano.name, leaderSandro.age)



// for (let i=0; i<20; i++){
//     if (i==15){
//         console.log("Hello World")
//     } else{
//         console.log(`${i} < 20`)
//     }
// }
let counter=0;
while (true){
    if (counter==20){
        break
    }
    counter++;
    console.log(counter);
}

let num1=1;
while (num1<=100){
    console.log(num1)
    num1++;
}

let age=20;
if (age>15){
    console.log(`${age}>15`)
} else if (age==15){
    console.log(15)
} else{
    console.log(`${age}<15`)
}

console.log(Math.sqrt(-1))

//initialization, condition, updating
for (let i=0; i<10; i++){
    console.log(i)
}