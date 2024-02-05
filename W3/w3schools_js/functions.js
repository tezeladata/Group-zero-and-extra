// defining function:

function name(parameter1, parameter2, parameter3) {
    // code to be executed
}

let num1=3;
let num2=9;
let num3=10;
function multiplicator(parameter1, parameter2, parameter3){
    return (parameter1*parameter2*parameter3)
}
console.log(multiplicator(num1, num2, num3))

function toKelvin(Celcius){
    return (Celcius+273.15) 
    // If we want to work with variables, which will include this functions, it's important to use return inside function instead of console.log
}
let value=toKelvin(10);
let text="There is " + value + " Kelvin"
console.log(text)

// Variables which are defined inside function are called local variables
function function1(){
    let carName="BMW"
    console.log(carName)
    // We can use local variable only in this function
}
function1()
// We cannot use that variable here