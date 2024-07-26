// hw1
const numArr = [1, 2, 3, -4, 5, 6]
console.log(numArr.every(function(value){
    return value > 0
}))


// hw2
const strArr = ["hello", "this", "is", ""]
console.log(strArr.every(function(value){
    return value != ""
}))


// hw3
const boolArr = [true, false, false, true, true, true]
console.log(boolArr.every(function(value){
    return value == true
}))


// hw4
console.log(numArr.every(function(value){
    return value %2 == 0
}))


// hw5
function manualEvery(iterable, userFunc){
    for (let i = 0; i<iterable.length; i++){
        if (! userFunc(iterable[i])){
            return false
        }
    }

    return true
}


// hw6
const gradeArr = [10, 5, 7, 8, 2, 2, 3, 4, 5]
console.log(gradeArr.some(function(value){
    return value >= 5
}))


// hw7
const userArr = [{role: "Civilian"}, {role: "Policeman"}, {role: "Nurse"}, {role: "Detective"}, {role: "Admin"}]
console.log(userArr.some(function(value){
    return value["role"].toLowerCase() == "admin"
}))


// hw8
const itemArr = [{overdue: false}, {overdue: false}, {overdue: false}, {overdue: false}, {overdue: true}]
console.log(itemArr.some(function(value){
    return value["overdue"] == true
}))


// hw9
const numArr2 = [10, 12, 13, 14, 15, 16, 17]
console.log(numArr2.some(function(value){
    return primeCheck(value)
}))

function primeCheck(num) {
    if (num <= 1) return false;

    for (let i = 2; i <= Math.floor(num ** 0.5); i++) {
        if (num % i === 0) {
            return false; 
        }
    }

    return true;
}


// hw10
function manualSome(iterable, userFunc){
    for (let i = 0; i<iterable.length; i++){
        if (userFunc(iterable[i])){
            return true
        }
    }

    return false
}


// hw11
console.log(numArr.find(function(value){
    return value < 0
}))


// hw12
const userArr2 = [{id: 1234}, {id: 2234}, {id: 3234}, {id: 4234}]
console.log(userArr2.find(function(value){
    return value.id == 3234
}))


// hw13
const taskArr = [{status: "complete", id: 1}, {status: "complete", id: 2}, {status: "incomplete", id: 1}, {status: "incomplete", id: 2}]
console.log(taskArr.find(function(value){
    return value.status === "incomplete"
}))


// hw14
const productArr = ["apple", "banana", "mango", "peach", "melon"]
console.log(productArr.find(function(value){
    return value === "peach"
}))


// hw15
function manualFind(iterable, user_value){
    for (let i = 0; i<iterable.length; i++){
        if (iterable[i] === user_value){
            return iterable[i]
        }
    }

    return undefined
}


// hw16
const numArr3 = [4, 5, 6, 7];
console.log(numArr3.findIndex(function(value){
    return primeCheck(value);
}));

function primeCheck(value){
    if (value <= 1){
        return false;
    }
    
    for (let i = 2; i <= Math.floor(Math.sqrt(value)); i++){
        if (value % i == 0){
            return false;
        }
    }
    
    return true;
}


// hw17
const userArr3 = [{role: "a"}, {role: "a"}, {role: "Admin"}]
console.log(userArr3.findIndex(function(value){
    return value.role.toLowerCase() === "admin"
}))


// hw18
const itemArr2 = [{overdue: false}, {overdue: true}, {overdue: false}]
console.log(itemArr2.findIndex(function(value){
    return value.overdue === true
}))


// hw19
const itemArr3 = [{inStock: false}, {inStock: true}, {inStock: true}]
console.log(itemArr3.findIndex(function(value){
    return value.inStock === false;
}))


// hw20
function manualFindIndex(iterable, userFunc){
    for (let i=0; i<iterable.length; i++){
        if (userFunc(iterable[i])){
            return iterable[i]
        }
    }

    return -1
}


// hw21
console.log("Hello world!".indexOf("l"))


// hw22
console.log(numArr.indexOf(6))


// hw23
console.log("hello hello".indexOf("ll"))


// hw 24
console.log(itemArr.indexOf({overdue: true}))


// hw25
function manualIndexOf(iterable, value){
    for (let i=0; i<iterable.length; i++){
        if (userFunc(iterable[i]) === value){
            return i
        }
    }

    return -1
}


// hw26
console.log("david".lastIndexOf("d"))


// hw27
function isPrime(num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}

function lastIndexOfPrime(arr) {
    const primes = arr.filter(isPrime);
    if (primes.length === 0) return -1;
    
    const lastPrime = primes[primes.length - 1]; 
    return arr.lastIndexOf(lastPrime); 
}

const numArr4 = [4, 5, 6, 7];
console.log(lastIndexOfPrime(numArr4));


// hw28
const strArr2 = ["a", "b", "c", "a", "b", "c"]
console.log(strArr2.lastIndexOf("c"))


// hw29
const obj1 = {isActive: true};
const obj2 = {isActive: false};
const obj3 = {isActive: true};

const userArr4 = [obj1, obj2, obj3]
console.log(userArr4.lastIndexOf(obj3))


// hw30
function manualIndexOf(iterable, value){
    for (let i=iterable.length - 1; i>= 0; i--){
        if (userFunc(iterable[i]) === value){
            return i
        }
    }

    return -1
}