// let name=prompt("Enter your name:");
// if (name=="David"){
//     console.log("Squad Leader")
// }else if(name="david"){
//     console.log("Github Controller")
// }
// else{
//     console.log("GOA student")
// }

// = მინიჭების ოპერატორი
// = შედარების ოპერატორი
// = მკაცრი ტოლობა(data type-იც მოწმდება)

// let decision=prompt("Do you want to join GOA?")
// if (decision=="yes" || decision=="Yes"){
//     let age=prompt("Enter your age:");
//     if (age>=18){
//     console.log("You joined GOA group 4")
//     }else{
//     console.log("You joined group 3")
//     }
// }
// else{
//     console.log("So bad, part of matrix")
// }

// set timeout - for timers

// for (let i=0; i<10; i++){
//     console.log(i)
// }
// for (let i=0; i<1000; i++){
//     console.log("GOA is " + i + " better than other academies.")
// }
// let a=function(){
//     let myNumber=prompt("Enter number: ")
//     if (myNumber!=0){
//         console.log(myNumber*(-1))
//     }else{
//         console.log(0)
//     }
// }
// a()
// better:
// console.log(Math.abs(prompt("Enter your number: ")))

let myArr = [234324, 22324, 356456, 22, 5646];
let sum = 0;
for (let i = 0; i < myArr.length; i++) {
    sum += myArr[i];
}
console.log(sum / myArr.length);