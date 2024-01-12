//checked property

//onclick func, checking checkbox propert
document.getElementById("button1").onclick=function(event){
    event.preventDefault();
    const input1=document.getElementById("input1")
    if(input1.checked){
        console.log("You are subscribed");
    }
    else{
        console.log("You are not subscribed");
    }
}

//switch is often better than else if
let grade="D";
switch(grade){
    case "A":
        console.log("You did great")
        break;
    case "B":
        console.log("You did good")
        break;
    case "C":
        console.log("You did normal")
        break;
    case "D":
        console.log("You barely passed")
        break;
    case "F":
        console.log("You failed")
        break;
    default:
        console.log(grade, "is not grade.")
}
//with nums
let grade2=95;
switch(true){
    case grade2>=90:
        console.log("You did great")
        break;
    case grade2>=80:
        console.log("You did good")
        break;
    case grade2>=70:
        console.log("You did normal")
        break;
    case grade2>=60:
        console.log("You barely passed")
        break;
    case grade2>60:
        console.log("You failed")
        break;
    default:
        console.log(grade, "is not grade.")
}



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

let temp=15;

if (!(temp>0 && temp<30)){
    console.log("Cold")
}
else{
    console.log("Warm")
}

let sunny=false;

if (!(sunny==true)){
    console.log("Not sunny")
}
else{
    console.log("sunny")
}