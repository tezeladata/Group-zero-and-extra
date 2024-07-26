//checked property

//onclick func, checking checkbox propert
// document.getElementById("button1").onclick=function(event){
//     event.preventDefault();
//     const input1=document.getElementById("input1")
//     if(input1.checked){
//         console.log("You are subscribed");
//     }
//     else{
//         console.log("You are not subscribed");
//     }
// }

//switch is often better than else if
// let grade="D";
// switch(grade){
//     case "A":
//         console.log("You did great")
//         break;
//     case "B":
//         console.log("You did good")
//         break;
//     case "C":
//         console.log("You did normal")
//         break;
//     case "D":
//         console.log("You barely passed")
//         break;
//     case "F":
//         console.log("You failed")
//         break;
//     default:
//         console.log(grade, "is not grade.")
// }
//with nums
// let grade2=95;
// switch(true){
//     case grade2>=90:
//         console.log("You did great")
//         break;
//     case grade2>=80:
//         console.log("You did good")
//         break;
//     case grade2>=70:
//         console.log("You did normal")
//         break;
//     case grade2>=60:
//         console.log("You barely passed")
//         break;
//     case grade2>60:
//         console.log("You failed")
//         break;
//     default:
//         console.log(grade, "is not grade.")
// }



//logical operators:
// || - or
// && - and
// !  - not

// let temp=10;
// let sunny=false;
// if (temp>0 && temp<30 && sunny==true){
//     console.log("Good weather")
// }
// else {
//     console.log("Bad weather")
// }

// let temp2=5;
// if (temp<0 || temp>30){
//     console.log("Bad weather")
// }
// else{
//     console.log("Good weather")
// }

// let temp=15;

// if (!(temp>0 && temp<30)){
//     console.log("Cold")
// }
// else{
//     console.log("Warm")
// }

// let sunny=false;

// if (!(sunny==true)){
//     console.log("Not sunny")
// }
// else{
//     console.log("sunny")
// }


// we use === to check if values are equal
// let x = confirm("Proceed to payment?");
// console.log(x);


//while loops
// let userName="David Tezelashvili";
// while (userName=="David Tezelashvili" || userName==null){
//     userName=window.prompt("Enter your name");
// }
// console.log("Hello", userName)

// let counter=0;
// while (counter<10){
//     console.log(counter);
//     counter+=1;
// }


//do while loops
//you do something, then check condition, repeate if True

// let userName;
// do{
//     userName=window.prompt("Enter name")
// }
// while(userName="")


//for loops
// for(let counter=0; counter<=12; counter+=2){
//     console.log(counter)
// }
//It's better to use i
// for(let i=1; i<=100; i+=3){
//     console.log(i)
// }

//break, continue
//break - breaks entire loop
//continue - skips an iteration
// for (let i=0; i<=20; i+=1){
//     if(i==13){
//         continue
//         //skipping 13(unlucky number)
//     }
//     console.log(i)
// }

//nested loops
// for (let i=1; i<=4; i+=1){
//     for (let j=1; j<=4; j+=1){
//         console.log(j)
//     }
// }

//rectangle generator
// let symbol=window.prompt("Enter a symbol:")
// let rows=window.prompt("Enter number of rows:")
// let columns=window.prompt("Enter number of columns:")
// for (let i=1; i<=rows; i+=1){
//     for (let j=1; j<=columns; j+=1){
//         document.getElementById("myRectangle").innerHTML+=symbol;
//     }
//     document.getElementById("myRectangle").innerHTML+="<br>";
// }


//functions
function counter(){
    console.log(1)
    console.log(2)
    console.log(3)
    console.log(4)
    console.log(5)
}

counter();
counter();
counter();
// გამოძახება