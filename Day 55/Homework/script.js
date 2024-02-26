document.getElementById("input2").onclick=function(event){
    event.preventDefault();
    const myNumber=document.getElementById("input1").value;
    if (myNumber%2==0){
        document.getElementById("label1").innerHTML="Your number is even!"
    }
    else{
        document.getElementById("label1").innerHTML="Your number is odd!"
    }
    document.getElementById("input1").value="";
}

// hw2:
const me={
    name: function(){
        console.log("David");
    },
    surname: "Tezelashvili",
    age: 15,
    Role: "Squad Leader",
    adress: "Tbilisi",
    country: "Georgia"
}
console.log(me.name)
console.log(me.Role)
console.log(me.country)
console.log(me.age)


// hw3:
// Multiples of six:
let myArr=[];
for (let x=0; x<100; x+=1){
    if (x%2==0 && x%3==0){
        myArr.push(x)
    }
}
console.log(myArr)